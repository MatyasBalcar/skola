from poj import *
list_pojistenych = []
while True:
    print("\n")
    print("Evidence pojistenych")
    print("\n")
    print("Zadejte kod pro akci:\n")
    akce = str(input("->1 -- pridani noveho pojistence \n->2 -- Vypsat vsechny pojistence \n->3 -- Vyhledat v seznamu pojistencu podle tel. cisla\n->4 -- Ukoncit porgram\n->"))

    if akce == '4':
        break
    elif akce == "1":
        jmeno = input("Zadejte jmeno\n")
        prijmeni = input("Zadejte prijmeni\n")
        vek = input("Zadejte vek\n")
        telefoni_cislo = input("Zadejte telefonni cislo\n")
        data_pojistence = Pojistenec(jmeno,prijmeni,vek,telefoni_cislo)
        list_pojistenych.append(data_pojistence)
        print("Uspech! Data se podarilo ulozit")
        input("Pro pokracovani zmacknete libovolnou klavesu")
    elif akce == "2":
        i=0
        for pojistenec in list_pojistenych:
            i+=1
            print(f"->{i} | {pojistenec}")
            
        input("Pro pokracovani zmacknete libovolnou klavesu")
    elif akce == "3":
        cislo = input("Zadejte tel cislo\n")
        for i in list_pojistenych:
            a = i.split("\t")
            if a[3] == cislo:
                print(i)
                break
            else:
                continue
        input("Pro pokracovani zmacknete libovolnou klavesu")
    else:
        print("Tohle neni validni moznost")
        input("Pro pokracovani zmacknete libovolnou klavesu")