
print("coucou")

class Monome:
    def __init__(self, v, p):
        self.value = v
        self.power = p

class Polynome:
    a = 0
    b = 0
    c = 0
    monomes = []
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

poly = Polynome()


def createMonome(tab, right):
    monome = None
    val = -int(tab[0].replace("=", "")) if right else int(tab[0].replace("=", ""))
    if len(tab) == 1:
        monome = Monome(val, 0)
    else :
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
            right = 1
        getPower(ex, right)


getInput()
poly.sortMonomes()
if poly.putPolyDegree() > 2 :
    print("Ne gère pas les puissances supérieures à 2.")

for mo in poly.monomes :
    print(mo.value, mo.power)