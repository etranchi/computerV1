
import numpy as np
import matplotlib.pyplot as plt

class Monome:
    def __init__(self, v, p):
        self.value = v
        self.power = p

class Polynome:
    a = 0
    b = 0
    c = 0
    discriminant = None
    monomes = []
    string = ""

    def draw(self):
        x = np.linspace(-20,20,400)
        y = self.c + self.b*x + self.a*x*x
        plt.plot(x,y)
        plt.show()

    def sortMonomes(self):
        self.monomes = sorted(self.monomes, key= lambda monome : monome.power, reverse= True)
        return

    def putPolyDegree(self):
        self.power = self.monomes[0].power
        print("Polynome de degrée : " + str(self.monomes[0].power))
        return self.monomes[0].power

    def findMonomeWithPowerOf(self, power):
        for el in self.monomes:
            if el.power == power:
                return el
        else :
            return None

    def createABC(self):

        self.a = self.findMonomeWithPowerOf(2).value if self.findMonomeWithPowerOf(2) != None else 0
        self.b = self.findMonomeWithPowerOf(1).value if self.findMonomeWithPowerOf(1) != None else 0
        self.c = self.findMonomeWithPowerOf(0).value if self.findMonomeWithPowerOf(0) != None else 0
        print(self.a, self.b, self.c)

    def solve(self):
        self.createABC()
        if self.a == 0 and self.b == 0 and self.c == 0:
            print("Tous les nombres réels sont solutions.")
            return
        if self.a == 0 and self.b == 0 and self.c != 0:
            print("Pas de solutions.")
            return
        discriminant = (self.b * self.b) - (4 * self.a * self.c)
        self.putSolution(discriminant)
    
    def putSolution(self, val):
        if self.power == 1:
            print(self.a, self.b, self.c)
            print("Une solution, x = " + str(-self.c / self.b))
        elif val < 0:
            print("Discriminant strictement négatif.")
            print("Don't handle imaginary right now.")
        elif val == 0:
            print("Discriminant égal à 0.")
            print("Une solution, x = " + str(-self.b / 2 * self.a))
        elif val > 0:
            print("Discriminant strictement positif.")
            print("Deux solutions, x1 = " + str((-self.b - (val ** 0.5))/ (2 * self.a)) + ", x2 = " + str((-self.b + (val ** 0.5))/ (2 * self.a)))

poly = Polynome()



def getSignAndValue(val):
    string = ""
    if val < 0:
        string = "- " + str(-val)
    else :
        string = "+ " + str(val)
    return string

def getStringPower(power):
    if power == 0 and poly.a != 0 and poly.b != 0 and poly.c != 0:
        return " "
    if power >= 1 or (poly.a == 0 and poly.b == 0):
        return "*X^" + str(power) + " "

def createMonome(tab, right):
    monome = None
    print(tab)
    val = -int(tab[0].replace("=", "")) if right else int(tab[0].replace("=", ""))
    if len(tab) == 1:
        monome = Monome(val, 0)
    else :
        print(tab[1])
        if len(tab[1]) < 3:
            print("Erreur.")
            exit()
        pow = int(tab[1].split("^")[1])
        monome = Monome(val,pow)
    ref = poly.findMonomeWithPowerOf(monome.power)
    if ref != None:
        print(ref.value, monome.value)
        ref.value += monome.value
    else :
        poly.monomes.append(monome)

def getPower(str, right):
    str = str.replace(" ", "")
    str = str.replace('-x', '-1*x')
    if str.startswith('x'):
        str = str.replace('x', '1*x')
    if str.endswith('x'):
        str = str.replace('x', 'x^1')
    createMonome(str.split("*"), right)
    return str

def getInput():
    right = 0
    val = input("Entrez une équation: ")
    expr = val.replace("-", "+-").split("+")
    for ex in expr:
        if ex.find("=") > 0:
            tmp = ex.split("=")
            getPower(tmp[0], right)
            right = 1
            if tmp[1] != " ":
                getPower(tmp[1], right)    
        else :
            getPower(ex, right)


getInput()
poly.sortMonomes()
poly.sortMonomes()
if poly.putPolyDegree() > 2 :
    print("Ne gère pas les puissances supérieures à 2.")

for mo in poly.monomes:
        poly.string += str(mo.value) if poly.string == "" else getSignAndValue(mo.value)
        poly.string += getStringPower(mo.power)

poly.string += "= 0"
print("Reduced form : " + poly.string)
poly.solve()
poly.draw()