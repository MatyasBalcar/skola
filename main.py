def cteni(cesta):
    try:
        f = open(cesta, "r")
        obsah = f.read()
        f.close()
        return obsah
    except FileNotFoundError:
        print(f"soubor {cesta} neexistuje")
        return []
cteni("soubor.txt")


def hledat(klic, hodnota,slovnik):
    try:
        hodnota_=slovnik[klic]
        if hodnota_==hodnota:
            print("hodnota se shoduje")
            return True
        else:
            print("hodnota se neshoduje")
    except KeyError:
        print("klic neexistuje")
        return False

hledat("ahoj","cus",{"ahoj":"cus"})

def test():
    diction={"ahoj":"cus"}
    print(diction["ahoj2"])
