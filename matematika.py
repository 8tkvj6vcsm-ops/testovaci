def funkce_scitej(a,b):
    soucet = a + b
    return soucet

def funkce_nasob(a,b):
    soucin = a * b 
    return soucin

def funkce_odecet(a,b):
    rozdil = a - b
    return rozdil

if __name__ == "__main__":
    soucet = funkce_scitej(1,1)
    soucin = funkce_nasob(2,2)
    rozdil = funkce_odecet(1,1)

    print(soucet, soucin, rozdil)