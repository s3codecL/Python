from main1 import *
from main2 import *
from main3 import *

def main():
    print("Que ejecutamos? (main1, main2 o main3):")
    a = int(input("numero:"))
        
    if a == 1: parte1()
    elif a == 2: parte2()
    elif a == 3: parte3()
    else:
        exit("el número debe ser 1, 2 o 3")
main()