
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
    

poly = Polynome()


def createMonome(tab):
    monome = None
    if len(tab) == 1:
        monome = Monome(int(tab[0]), 0)
    else :
        val = int(tab[0])
        pow = int(tab[1].split("^")[1])
        monome = Monome(val,pow)
    poly.monomes.append(monome)

def getPower(str):
    str = str.replace(" ", "")
    str = str.replace('-x', '-1*x')
    if str.startswith('x'):
        str = str.replace('x', '1*x')
    if str.endswith('x'):
        str = str.replace('x', 'x^1')
    print(str)
    createMonome(str.split("*"))
    return str

def getInput():
    val = input("Entrez une équation: ")
    expr = val.replace("-", "+-").split("+")
    print(expr)
    for ex in expr:
        getPower(ex)


getInput()
poly.sortMonomes()
if poly.putPolyDegree() > 2 :
    print("Ne gère pas les puissances supérieures à 2.")

for mo in poly.monomes :
    print(mo.value, mo.power)