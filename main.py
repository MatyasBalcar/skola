def cteni(cesta):
    try:
        f = open(cesta, "r")
        
    except FileNotFoundError:
        print(f"soubor {cesta} neexistuje")
        return []
    obsah = f.read()
    f.close()
    return obsah
print(cteni("soubor.txt"))


def hledat(klic, hodnota,slovnik):
    try:
        hodnota_=slovnik[klic]
        
    except KeyError:
        print("klic neexistuje")
        return False
    if hodnota_==hodnota:
        print("hodnota se shoduje")
        return True
    else:
        print("hodnota se neshoduje")
hledat("ahoj","cus",{"ahoj":"cus"})

def test():
    diction={"ahoj":"cus"}
    print(diction["ahoj2"])
