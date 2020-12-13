import os
def volumeprism(panjang,lebar,tinggi):
    return panjang*lebar*tinggi/2
def volumeLimEmpat(panjang,lebar,tinggi):
    return panjang*lebar*tinggi/3
def volumetab(jarijari,tinggi):
    return 3.14*jarijari*jarijari*tinggi
def menu():
    jawaban = 999999
    while(jawaban != 0):
        print("pilih menu")
        print("1. volume prisma segi tiga")
        print("2. volume limas segi empat")
        print("3. volume tabung")
        print("0. keluar")
        jawaban = int(input("jawaban anda : "))
        if jawaban == 1 :
            panjang = float(input("panjang :"))
            lebar = float(input("lebar :"))
            tinggi = float(input("tinggi :"))
            print("volumenya adalah : " + str(volumeprism(panjang,lebar,tinggi)))
            input("Press Enter to continue...")
        elif jawaban == 2 :
            panjang = float(input("panjang :"))
            lebar = float(input("lebar :"))
            tinggi = float(input("tinggi :"))
            print("volumenya adalah : " + str(volumeLimEmpat(panjang,lebar,tinggi)))
            input("Press Enter to continue...")
        elif jawaban == 3:
            jarijari = float(input("jari jari :"))
            tinggi = float(input("tinggi :"))
            print("volumenya adalah : " + str(volumetab(jarijari,tinggi)))
            input("Press Enter to continue...")
        elif jawaban == 0:
            print("terima kasih")
        else :
            input("apaan tuh?")
        os.system("cls")
panjang = 0.0
lebar = 0.0
tinggi = 0.0
jarijari = 0.0
menu()

