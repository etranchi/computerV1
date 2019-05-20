
print("coucou")

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
    def sortMonomes(self):
        return sorted(self.monomes, key= lambda monome : monome.power)
    def putPolyDegree(self):
        print("Polynome de degrée : " + str(self.monomes[0].power))
        return self.monomes[0].power
    def findMonomeWithPowerOf(self, power):
        for el in self.monomes:
            if el.power == power:
                return el
        else :
            return None

    def createABC(self):
        self.a = self.findMonomeWithPowerOf(2).value
        self.b = self.findMonomeWithPowerOf(1).value
        self.c = self.findMonomeWithPowerOf(0).value
        print(self.a, self.b, self.c)

    def solve(self):
        self.createABC()
        discriminant = (self.b * self.b) - (4 * self.a * self.c)
        print(discriminant)
        self.putSolution(discriminant)
    
    def putSolution(self, val):
        if val < 0:
            print("Don't handle imaginary right now.")
        if val == 0:
            print("Une solution, x = " + str(-self.b / 2 * self.a))
        if val > 0:
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
    if power == 0:
        return " "
    if power == 1:
        return "*X "
    if power > 1 :
        return "*X^" + str(power) + " "

def createMonome(tab, right):
    monome = None
    val = -int(tab[0].replace("=", "")) if right else int(tab[0].replace("=", ""))
    if len(tab) == 1:
        monome = Monome(val, 0)
    else :
        pow = int(tab[1].split("^")[1])
        monome = Monome(val,pow)
    ref = poly.findMonomeWithPowerOf(monome.power)
    print(monome.value) 
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
    print("la")
    print(str)
    createMonome(str.split("*"), right)
    return str

def getInput():
    right = 0
    val = input("Entrez une équation: ")
    expr = val.replace("-", "+-").split("+")
    print(expr)
    for ex in expr:
        if ex.find("=") > 0:
            tmp = ex.split("=")
            getPower(tmp[0], right)
            right = 1
            getPower(tmp[1], right)
            
        else :
            getPower(ex, right)


getInput()
poly.sortMonomes()
if poly.putPolyDegree() > 2 :
    print("Ne gère pas les puissances supérieures à 2.")

for mo in poly.monomes :
    if mo.value != 0:
        poly.string += str(mo.value) if poly.string == "" else getSignAndValue(mo.value)
        poly.string += getStringPower(mo.power)

poly.string += " = 0"
print("Reduced form : " + poly.string)
poly.solve()