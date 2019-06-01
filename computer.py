#!/Users/etranchi/.brew/bin/python3
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

class Monome:
    def __init__(self, v, p):
        self.value = v
        self.power = p


def end(reason):
    print(reason)
    exit()

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

class Polynome:
    a = 0
    b = 0
    c = 0
    discriminant = None
    monomes = []
    string = ""

    def draw(self):
        x = np.linspace(-20,20,200)
        y = self.c + self.b*x + self.a*x*x
        fig = plt.figure()
        fig.canvas.mpl_connect('button_press_event', onclick)
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

    def solve(self):
        self.createABC()
        if self.a == 0 and self.b == 0 and self.c == 0:
            end("Tous les nombres réels sont solutions.")
        if self.a == 0 and self.b == 0 and self.c != 0:
            end("Pas de solutions.")
        discriminant = (self.b * self.b) - (4 * self.a * self.c)
        self.putSolution(discriminant)
    
    def putSolution(self, val):
        print("Forme réduite : " + poly.string)
        if self.power == 1:
            print("Une solution, x = " + str(-self.c / self.b))
        elif val < 0:
            print("Discriminant : \u0394 = b^2 - 4*a*c = " + str(val))
            print("Discriminant strictement négatif.")
            print("Deux solutions imaginaire, x1 = (-b - " + u"\u221a\u0394*i^2) / 2*a, x2 = (-b + " + u"\u221a\u0394*i^2) / 2*a.")
        elif val == 0:
            print("Discriminant : b^2 - 4*a*c = " + str(val))
            print("Discriminant égal à 0.")
            print("Une solution double, -b/2a : x = " + str(-self.b / 2 * self.a))
        elif val > 0:
            print("Discriminant : \u0394 = b^2 - 4*a*c = " + str(val))
            print("Discriminant strictement positif.")
            print("Deux solutions, x1 = (-b - " + u"\u221a\u0394) / 2*a, x2 = (-b + " + u"\u221a\u0394) / 2*a.")
            print("x1 = " + str((-self.b - (val ** 0.5))/ (2 * self.a)) + ", x2 = " + str((-self.b + (val ** 0.5))/ (2 * self.a)))

poly = Polynome()



def checkForMonome(mo):
    if mo.isdigit() == True:
        return
    elif len(mo) > 0:
        if mo[0] == "-":
            return
        if mo[0] == 'x':
            mo = "1*" + mo
        if mo.count('^') > 1 or mo.count('*') > 1 or mo.count('^') == 0 or mo.count('*') == 0 :
            end("Erreur parsing ici.")

def getSignAndValue(val):
    string = ""
    if val < 0:
        string = "- " + str(-val)
    else :
        string = "+ " + str(val)
    return string

def getStringPower(power):
    if power == 0 or poly.a != 0 and poly.b != 0 and poly.c != 0:
        return " "
    if power >= 1 or (poly.a == 0 and poly.b == 0):
        return "*X^" + str(power) + " "

def createMonome(tab, right):
    monome = None
    if len(tab) == 1 and tab[0] == "":
        return
    for v in tab : checkForMonome(v)
    val = -int(tab[0].replace("=", "")) if right else int(tab[0].replace("=", ""))
    if len(tab) == 1:
        monome = Monome(val, 0)
    else :
        if len(tab[1]) < 3:
            end("Erreur parsing.")
        pow = int(tab[1].split("^")[1])
        monome = Monome(val,pow)
    ref = poly.findMonomeWithPowerOf(monome.power)
    if ref != None:
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


def checkInput(string):
    if string.isdigit():
        end("Aucune équation a résoudre")
    if string.count('=') > 1:
        end("Erreur parsing.")
    for c in string:
        if c.isdigit() == False and (c != 'x' and c != '+' and c != '-' and c != '*' and c != '=' and c != '^' and c != 'X' and c != ' '):
            end("Erreur parsing.")

def getInput():
    right = 0
    try:
        val = input("Entrez une équation: ")
    except EOFError:
        end("Erreur input.")
    except KeyboardInterrupt:
        end("Erreur input.")
    except IOError:
        end("Erreur input.")
    if len(val) == 0:
        end("No input.")
    checkInput(val)

    expr = val.lower().replace("-", "+-").split("+")
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
if poly.putPolyDegree() > 2 :
    end("Ne gère pas les puissances supérieures à 2.")

for mo in poly.monomes:
        poly.string += str(mo.value) if poly.string == "" else getSignAndValue(mo.value)
        poly.string += getStringPower(mo.power)

poly.string += "= 0."

poly.solve()
# poly.draw()
