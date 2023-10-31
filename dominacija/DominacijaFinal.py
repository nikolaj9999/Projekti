 # redovi i kolone

#X su horizontalno postavljene plocice
#O su vertikalno postavljene plocice 

# pamte se trenutne kooridinate plocica

def prikaziIgru(matPolja):
    global matZidovi
    matCela = list()
    for i in range(len(matZidovi)):
        if i % 2 == 0:
            tmpLista1 = list()
            for j in range(len(matPolja[0])):
                tmpLista1.append('')
                tmpLista1.append(matZidovi[i][j])
            tmpLista1.append('')
            matCela.append(tmpLista1)
        elif i % 2 != 0:
            tmpLista = list()
            for j in range(len(matPolja[0])):
                tmpLista.append(matZidovi[i][j])
                tmpLista.append(matPolja[i//2][j])
            tmpLista.append(matZidovi[i][len(matZidovi[i])-1])
            matCela.append(tmpLista)
    print("Cela tabla: \n")
    for i in range(len(matCela)):
        print(' '.join(map(str, matCela[i])))

def prikaziTablu(mat,matPolja):
    global matZidovi
    matCela = list()
    for i in range(len(matZidovi)):
        if i % 2 == 0:
            tmpLista1 = list()
            for j in range(len(mat[0])):
                tmpLista1.append('')
                tmpLista1.append(matZidovi[i][j])
            tmpLista1.append('')
            matCela.append(tmpLista1)
        elif i % 2 != 0:
            tmpLista = list()
            for j in range(len(mat[0])):
                tmpLista.append(matZidovi[i][j])
                tmpLista.append(matPolja[i//2][j])
            tmpLista.append(matZidovi[i][len(matZidovi[i])-1])
            matCela.append(tmpLista)
    print("Cela tabla: \n")
    for i in range(len(matCela)):
        print(' '.join(map(str, matCela[i])))


# def unosPocetnihParametara():
#     global matPolja, matZidovi

#     # 0 su inicijalno prazna polja
#     # X je plocica prvog igraca 
#     # O je plocica drugog igraca

#     matP = [[0 for i in range(brojKolona)] for j in range(brojVrsta)]
#     matZ = []

#     for i in range(2 * brojVrsta + 1):
#         matZ.append([])
#         if i % 2 == 0:
#             for k in range(brojKolona):
#                 if i == 0 or i == 2*brojVrsta:
#                     matZ[i].append(" =")
#                 else:
#                     matZ[i].append(" -")
#         else:
#             for k in range(brojKolona + 1):
#                 if k == 0 or k == brojKolona:
#                     matZ[i].append(chr(0x01C1))
#                 else:
#                     matZ[i].append("|")
#     matPolja = matP
#     matZidovi = matZ

def unosPocetnihParametara():
    global matZidovi

    # 0 su inicijalno prazna polja
    # X je plocica prvog igraca 
    # O je plocica drugog igraca

    matP = [[0 for i in range(brojKolona)] for j in range(brojVrsta)]
    matZ = []
    tmp = 'A'
    tem = 0
    q = 1
    for i in range(2 * brojVrsta + 1):
        w = 1
        matZ.append([])
        if i % 2 == 0:
            for k in range(brojKolona):
                if i == 0:
                    if tmp == 'A':
                        p = ("   ",tmp)
                        matZ[i].append(''.join(map(str, p))) 
                    else:
                        p = (" ",tmp)
                        matZ[i].append(''.join(map(str, p))) 
                    tmp = chr (ord (tmp) + 1)    
                elif i == 2*brojVrsta:
                    if(q == 1):
                        matZ[i].append("   =")
                        q = 0
                    else:
                        matZ[i].append(" =")
                else:
                    if(w == 1):
                        matZ[i].append("   -")
                        w = 0
                    else:
                        matZ[i].append(" -")
        else:
            for k in range(brojKolona + 1):
                if k == 0:
                    tem+=1
                    t = [tem, " ", chr(0x01C1)]
                    matZ[i].append(''.join(map(str, t)))
                elif k == brojKolona:
                    matZ[i].append(chr(0x01C1))
                else:
                    matZ[i].append("|")
    matPolja = matP
    matZidovi = matZ
    return matPolja

def proveraKrajaIgre(stanje):
    kraj = 0
    for i in range(brojVrsta):
        for j in range(brojKolona-1): 
            if stanje[i][j] == stanje[i][j+1] == 0:
                kraj = 0
                return kraj
            else:
                kraj = -10
    for i in range(brojVrsta-1):
        for j in range(brojKolona):
            if stanje[i][j] == stanje[i+1][j] == 0:
                kraj = 0
                return kraj
            else:
                kraj = 10
    return kraj

def proveraKrajaIgreZaWhile(stanje):
    kraj = 0
    if (inputIgrac=="O"):
        for i in range(brojVrsta):
            for j in range(brojKolona-1): 
                if stanje[i][j] == stanje[i][j+1] == 0:
                    kraj = 0
                    return kraj
                else:
                    kraj = -10
    else:
        for i in range(brojVrsta-1):
            for j in range(brojKolona):
                if stanje[i][j] == stanje[i+1][j] == 0:
                    kraj = 0
                    return kraj
                else:
                    kraj = 10
    return kraj
                
                
def unosPoteza():   
    if inputIgrac == "X":
        x1 = koordinataX - 1
        y1 = ord(koordinataY) - 65
        x2 = x1 + 1
        y2 = y1
    else:
        x1 = koordinataX - 1
        y1 = ord(koordinataY) - 65
        x2 = x1
        y2 = y1 + 1
    potezX = (x1, y1)
    potezY = (x2, y2)
    return ((potezX, potezY))


     
def proveraPoteza(potez, matPolja):
    if inputIgrac == "X":
        if potez[1][0] >= brojVrsta or potez[1][1] >= brojKolona:
            return False
        if matPolja[potez[0][0]][potez[0][1]] or matPolja[potez[1][0]][potez[1][1]] != 0:
            return False
    else:
        if potez[1][0] >= brojVrsta or potez[1][1] >= brojKolona:
            return False
        if matPolja[potez[0][0]][potez[0][1]] or matPolja[potez[1][0]][potez[1][1]] != 0:
            return False
    return True

def postaviPlocicu(potez,matPolja):
    global brPotezaX
    global brPotezaY
    global inputIgrac
    if inputIgrac == "X":
        matPolja[potez[0][0]][potez[0][1]] = "X"
        matPolja[potez[1][0]][potez[1][1]] = "X"
        inputIgrac="O"
    else:
        matPolja[potez[0][0]][potez[0][1]] = "O"
        matPolja[potez[1][0]][potez[1][1]] = "O"
        inputIgrac="X"


def prikaziPotez(ispravnostPoteza):
    global brIspravnihPotezaX
    global brNeispravnihPotezaX
    global brIspravnihPotezaO
    global brNeispravnihPotezaO
    global ispravniPotezX
    global neispravniPotezX
    global ispravniPotezO
    global neispravniPotezO
    if inputIgrac == "X":
        if ispravnostPoteza == True:
            brIspravnihPotezaX+=1
            ispravniPotezX.update({brIspravnihPotezaX: [koordinataX, koordinataY]})
        else:
            brNeispravnihPotezaX+=1
            neispravniPotezX.update({brNeispravnihPotezaX: [koordinataX, koordinataY]})
        print ("Dobri potezi X:")
        print(*[str(k) + ':' + ' ' + ' '.join(map(str, v)) for k,v in ispravniPotezX.items()], sep='\n')
        print("Losi potezi X:")
        print(*[str(k) + ':' + ' ' + ' '.join(map(str, v)) for k,v in neispravniPotezX.items()], sep='\n')
    else:
        if ispravnostPoteza == True:
            brIspravnihPotezaO+=1
            ispravniPotezO.update({brIspravnihPotezaO: [koordinataX, koordinataY]})
        else:
            brNeispravnihPotezaO+=1
            neispravniPotezO.update({brNeispravnihPotezaO: [koordinataX, koordinataY]})
        print("Dobri potezi O")
        print(*[str(k) + ':' + ' ' + ' '.join(map(str, v)) for k,v in ispravniPotezO.items()], sep='\n')
        print("Losi potezi O")
        print(*[str(k) + ':' + ' ' + ' '.join(map(str, v)) for k,v in neispravniPotezO.items()], sep='\n')

def unosParametara():
    print("Unesite koordinate poteza")
    inputpotez = input()
    args1 = inputpotez.split(" ")
    global koordinataX 
    koordinataX = int(args1[0])
    global koordinataY
    koordinataY = str(args1[1])

def odigravanjePartije():
    matPolja = unosPocetnihParametara()
    while(proveraKrajaIgreZaWhile(matPolja) == 0):
        unosParametara()
        potez = unosPoteza()
        ispravnostPoteza = proveraPoteza(potez,matPolja)
        prikaziPotez(ispravnostPoteza)
        if ispravnostPoteza==True:
            postaviPlocicu(potez, matPolja)
            prikaziIgru(matPolja)
        else:
             print("Neispravne koordinate, odigrajte ponovo")
        #print("\nSledeci igrac moze odigrati sledece poteze:\n")
        #prikaziMogucaStanja()
        #print(novaStanja())
    if(inputIgrac=="O"):
        print("Kraj igre X je pobedik")
    else:
        print("Kraj igre O je pobedik")

def operatorPromeneStanja(stanje):
    listaIndexaZaO=[]
    listaIndexaZaX=[]
    if(inputIgrac=="O"):
        for i in range(brojVrsta):
            for j in range(brojKolona-1): 
                if stanje[i][j] == stanje[i][j+1] == 0:
                    tmp = (i,j)
                    stanje[i][j] = 'O'
                    stanje[i][j+1] = 'O'
                    prom = proceniPotez(stanje, inputIgrac)
                    stanje[i][j] = 0
                    stanje[i][j+1] = 0
                    listaIndexaZaO.append((tmp,prom))
        return listaIndexaZaO
    else:
        for i in range(brojVrsta-1):
            for j in range(brojKolona): 
                if stanje[i][j] == stanje[i+1][j] == 0:
                    tmp = (i,j)
                    stanje[i][j] = 'X'
                    stanje[i+1][j] = 'X'
                    prom = proceniPotez(stanje)
                    stanje[i][j] = 0
                    stanje[i+1][j] = 0
                    listaIndexaZaX.append((tmp,prom))
        return listaIndexaZaX

def novaStanja(stanje, igrac):
    listaIndexaZaO=[]
    listaIndexaZaX=[]
    if(igrac=="O"):
        for i in range(brojVrsta):
            for j in range(brojKolona-1): 
                if stanje[i][j] == stanje[i][j+1] == 0:
                    tmp =((i,j),(i,j+1))
                    listaIndexaZaO.append(tmp)
        return listaIndexaZaO
    else:
        for i in range(brojVrsta-1):
            for j in range(brojKolona): 
                if stanje[i][j] == stanje[i+1][j] == 0:
                    tmp =((i,j),(i+1,j))
                    listaIndexaZaX.append(tmp)
        return listaIndexaZaX

def prikaziMogucaStanja(stanje, matPolja):
    lista = operatorPromeneStanja(stanje)
    if(inputIgrac=="O"):
        for x in lista:
            stanje[x[0]][x[1]]='O'
            stanje[x[0]][x[1]+1]='O'
            prikaziTablu(stanje, matPolja)
            stanje[x[0]][x[1]]=0
            stanje[x[0]][x[1]+1]=0
    else:
        for x in lista:
            stanje[x[0]][x[1]]='X'
            stanje[x[0]][x[1]]='X'
            prikaziTablu(stanje,matPolja)
            stanje[x[0]][x[1]]=0
            stanje[x[0]][x[1]+1]=0

def proceniPotez(stanje, igrac):
    max=0
    brojSlobodnih=0
    if(igrac=="O"):
         for i in range(brojVrsta):
            brojSlobodnih=0
            for j in range(brojKolona): 
                if(stanje[i][j]==0):
                 brojSlobodnih+=1
            if(max<brojSlobodnih):
              max=brojSlobodnih
    else:
         for i in range(brojKolona):
            brojSlobodnih=0
            for j in range(brojVrsta): 
                if(stanje[j][i]==0):
                 brojSlobodnih+=1
            if(max<brojSlobodnih):
              max=brojSlobodnih
    return max

def postaviPlocicuZaStanje(stanje, s, igrac):
    if igrac == 'X':
        stanje[s[0][0]][s[0][1]] = 'X'
        stanje[s[1][0]][s[1][1]] = 'X'
    else:
        stanje[s[0][0]][s[0][1]] = 'O'
        stanje[s[1][0]][s[1][1]] = 'O'
    return stanje

def max_value(stanje, dubina, alpha, beta, potez=None):
    if proveraKrajaIgre(stanje) == -10 or proveraKrajaIgre(stanje) == 10:
        return (potez, proveraKrajaIgre(stanje))
    if(inputIgrac == 'X'):
        lista_poteza = novaStanja(stanje, 'X')
        if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
            return (potez, proceniPotez(stanje, 'X'))
        else:
            for s in lista_poteza:
                alpha = max(alpha, min_value(postaviPlocicuZaStanje(stanje, s, 'X'), dubina - 1, alpha, beta, s if potez is None else potez), key=lambda x: x[1])
                if abs(proveraKrajaIgre(stanje)) == 10 or proveraKrajaIgre(stanje) == -10:
                    return (s, proveraKrajaIgre(stanje))
                if alpha[1] >= beta[1]:
                    return beta
    else:
        lista_poteza = novaStanja(stanje, 'O')
        if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
            return (potez, proceniPotez(stanje, 'O'))
        else:
            for s in lista_poteza:
                alpha = max(alpha, min_value(postaviPlocicuZaStanje(stanje, s, 'O'), dubina - 1, alpha, beta, s if potez is None else potez), key=lambda x: x[1])
                if abs(proveraKrajaIgre(stanje)) == 10 or proveraKrajaIgre(stanje) == -10:
                    return (s, proveraKrajaIgre(stanje))
                if alpha[1] >= beta[1]:
                    return beta
    return alpha

def min_value(stanje, dubina, alpha, beta, potez=None):
    if abs(proveraKrajaIgre(stanje)) == 10 or proveraKrajaIgre(stanje) == -10:
        return (potez, proveraKrajaIgre(stanje))
    if(inputIgrac == 'O'):
        lista_poteza = novaStanja(stanje, 'O')
        if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
            return (potez, proceniPotez(stanje, 'O'))
        else:
            for s in lista_poteza:
                beta = min(beta, max_value(postaviPlocicuZaStanje(stanje, s, 'O'), dubina - 1, alpha, beta, s if potez is None else potez), key=lambda x: x[1])
                if abs(proveraKrajaIgre(stanje)) == 10 or proveraKrajaIgre(stanje) == -10:
                    return (s, proveraKrajaIgre(stanje))
                if beta[1] <= alpha[1]:
                    return alpha
    else:
        lista_poteza = novaStanja(stanje, 'X')
        if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
            return (potez, proceniPotez(stanje, 'X'))
        else:
            for s in lista_poteza:
                beta = min(beta, max_value(postaviPlocicuZaStanje(stanje, s, 'X'), dubina - 1, alpha, beta, s if potez is None else potez), key=lambda x: x[1])
                if abs(proveraKrajaIgre(stanje)) == 10 or proveraKrajaIgre(stanje) == -10:
                    return (s, proveraKrajaIgre(stanje))
                if beta[1] <= alpha[1]:
                    return alpha
    return beta

def minimax_alpha_beta(stanje, dubina, moj_potez, alpha=(None, -10), beta=(None, 10)):
    if moj_potez:
        return max_value(stanje, dubina, alpha, beta)
    else:
        return min_value(stanje, dubina, alpha, beta)

def odigravanjePartijeRacunara():
    pamtiSvePoteze = []
    if inputIgrac == 'X': 
        potez = True
    else: potez = False
    matPolja = unosPocetnihParametara()
    temp = [[0 for i in range(brojKolona)] for j in range(brojVrsta)]
    while(proveraKrajaIgre(matPolja) == 0):
        min_max_alpha_beta_result = minimax_alpha_beta(temp, brojVrsta, potez)
        naj = min_max_alpha_beta_result[0] if type(min_max_alpha_beta_result) is tuple else (0, 0)
        pamtiSvePoteze.append([naj, inputIgrac])
        temp = [[0 for i in range(brojKolona)] for j in range(brojVrsta)]
        for x in pamtiSvePoteze:
            postaviPlocicuZaStanje(temp, x[0], x[1])
        postaviPlocicu(naj,matPolja)
        prikaziIgru(matPolja)
        potez = not potez
    #pobednik = ('X' if proveraKrajaIgre(matPolja) == 10 else
    #('O' if proveraKrajaIgre(matPolja) == -10 else "Nerešeno"))
    pobednik = ('O' if proveraKrajaIgre(matPolja) == 10 else
    ('X' if proveraKrajaIgre(matPolja) == -10 else "Nerešeno"))
    print(f"Pobednik je: {pobednik}")

def igraRacunar(pamtiSvePoteze, matPolja, temp, potez):
    min_max_alpha_beta_result = minimax_alpha_beta(temp, brojVrsta, potez)
    naj = min_max_alpha_beta_result[0] if type(min_max_alpha_beta_result) is tuple else (0, 0)
    pamtiSvePoteze.append([naj, inputIgrac])
    temp = [[0 for i in range(brojKolona)] for j in range(brojVrsta)]
    for x in pamtiSvePoteze:
        postaviPlocicuZaStanje(temp, x[0], x[1])
    postaviPlocicu(naj,matPolja)
    prikaziIgru(matPolja)
    potez = not potez
    return pamtiSvePoteze, matPolja, temp, potez

def igraCovek(pamtiSvePoteze, matPolja, temp, potez):
    unosParametara()
    potezz = unosPoteza()
    ispravnostPoteza = proveraPoteza(potezz,matPolja)
    prikaziPotez(ispravnostPoteza)

   
    if(ispravnostPoteza==True):
          pamtiSvePoteze.append([potezz,inputIgrac])
          
    else:
        while(ispravnostPoteza==False):
            print("Neispravne koordinate, odigrajte ponovo")
            unosParametara()
            potezz = unosPoteza()
            ispravnostPoteza = proveraPoteza(potezz,matPolja)
            prikaziPotez(ispravnostPoteza)
    postaviPlocicu(potezz, matPolja)
    prikaziIgru(matPolja)

    pamtiSvePoteze.append([potezz,inputIgrac])
    for x in pamtiSvePoteze:
        postaviPlocicuZaStanje(temp, x[0], x[1])

    
    potez=not potez
    return pamtiSvePoteze, matPolja, temp, potez


def odigravanjePartijeRacunarCovek():
    global inputIgrac
    pamtiSvePoteze = []
    if(CovekRacunar == '0'):
        if inputIgrac == 'X':
            inputIgrac = 'O'
        else : inputIgrac = 'X'
    if inputIgrac == 'X': 
        potezX = True
        prviIgrac = True
        potezO = False
    else: 
        potezX = False
        prviIgrac = False
        potezO = True
    matPolja = unosPocetnihParametara()
    temp = [[0 for i in range(brojKolona)] for j in range(brojVrsta)]


    while(proveraKrajaIgreZaWhile(matPolja) == 0):
        if(CovekRacunar=='1'):
            if(prviIgrac == True):
                if(potezX == True):
                    pamtiSvePoteze, matPolja, temp, potezX = igraCovek(pamtiSvePoteze, matPolja, temp, potezX)
                else:
                    pamtiSvePoteze, matPolja, temp, potezX = igraRacunar(pamtiSvePoteze, matPolja, temp, potezX)
            else:
                if(potezO == True):
                    pamtiSvePoteze, matPolja, temp, potezO = igraCovek(pamtiSvePoteze, matPolja, temp, potezO)
                else:
                    pamtiSvePoteze, matPolja, temp, potezO = igraRacunar(pamtiSvePoteze, matPolja, temp, potezO)
        else:
            if(prviIgrac == False):
                if(potezO == True):
                    pamtiSvePoteze, matPolja, temp, potezO = igraRacunar(pamtiSvePoteze, matPolja, temp, potezO)
                else:
                    pamtiSvePoteze, matPolja, temp, potezO = igraCovek(pamtiSvePoteze, matPolja, temp, potezO)
            else:
                if(potezX == True):
                    pamtiSvePoteze, matPolja, temp,  potezX = igraRacunar(pamtiSvePoteze, matPolja, temp,  potezX)
                else:
                    pamtiSvePoteze, matPolja, temp,  potezX = igraCovek(pamtiSvePoteze, matPolja, temp,  potezX)

    pobednik = ('X' if proveraKrajaIgreZaWhile(matPolja) == -10 else
    ('O' if proveraKrajaIgreZaWhile(matPolja) == 10 else "Nerešeno"))
    print(f"Pobednik je: {pobednik}")

def mainRacunara():
    print("Unesite da li prvo igra covek(1) ili racunar(0):")
    global CovekRacunar
    CovekRacunar = input()

    print("Unesite kog igraca hocete da igrate (X/O):")
    global inputIgrac 
    inputIgrac = input()

    print("Postavi igru: broj_vrsta broj_kolona ")
    inputStr = input()
    args = inputStr.split(" ")
    global brojVrsta
    brojVrsta = int(args[0])
    global brojKolona
    brojKolona = int(args[1])

    global brIspravnihPotezaX
    global brIspravnihPotezaO
    global brNeispravnihPotezaX
    global brNeispravnihPotezaO

    brIspravnihPotezaX = 0
    brIspravnihPotezaO = 0
    brNeispravnihPotezaX = 0
    brNeispravnihPotezaO = 0

    global ispravniPotezX
    global neispravniPotezX
    global ispravniPotezO
    global neispravniPotezO

    ispravniPotezX = {"":[]}
    neispravniPotezX = {"":[]}
    ispravniPotezO = {"":[]}
    neispravniPotezO = {"":[]}

    #odigravanjePartijeRacunara()
    odigravanjePartijeRacunarCovek()

def main():
    print("Unesite kog igraca hocete da igrate (X/O):")
    global inputIgrac 
    inputIgrac = input()

    print("Postavi igru: broj_vrsta broj_kolona ")
    inputStr = input()
    args = inputStr.split(" ")
    global brojVrsta
    brojVrsta = int(args[0])
    global brojKolona
    brojKolona = int(args[1])

    # print("Unesite koordinate poteza")
    # inputpotez = input()
    # args1 = inputpotez.split(" ")
    # global koordinataX 
    # koordinataX = int(args1[0])
    # global koordinataY
    # koordinataY = str(args1[1])
    
    global brIspravnihPotezaX
    global brIspravnihPotezaO
    global brNeispravnihPotezaX
    global brNeispravnihPotezaO

    brIspravnihPotezaX = 0
    brIspravnihPotezaO = 0
    brNeispravnihPotezaX = 0
    brNeispravnihPotezaO = 0

    global ispravniPotezX
    global neispravniPotezX
    global ispravniPotezO
    global neispravniPotezO

    ispravniPotezX = {"":[]}
    neispravniPotezX = {"":[]}
    ispravniPotezO = {"":[]}
    neispravniPotezO = {"":[]}

    odigravanjePartije()
   
#main()
mainRacunara()