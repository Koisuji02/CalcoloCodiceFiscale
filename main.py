def calcola_codice_fiscale(nome, cognome, data_nascita, sesso, stato_nascita, comune_nascita):

    #! COGNOME
    cognome = cognome.replace(" ", "")
    cognome = cognome.upper()

    if len(cognome) < 3:
        cognome_codice = cognome + "X" * (3 - len(cognome))
    else:
        consonanti = ""
        for char in cognome:
            if char not in "AEIOU":
                consonanti += char
        if len(consonanti) < 3:
            cognome_codice = cognome[:3]
        else:
            cognome_codice = consonanti[:3]

    #! NOME
    nome = nome.replace(" ", "")
    nome = nome.upper()

    if len(nome) < 3:
        nome_codice = nome + "X" * (3 - len(nome))
    else:
        consonanti = ""
        vocali = ""
        for char in nome:
            if char not in "AEIOU":
                consonanti += char
            else:
                vocali += char
        if len(consonanti) >= 4:
            nome_codice = consonanti[0] + consonanti[2] + consonanti[3]
        else:
            nome_codice = consonanti + vocali[:(3 - len(consonanti))]

    #! ANNO
    anno_nascita = data_nascita[8:]

    #! MESE
    mesi_codice = {"01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "H", "07": "L", "08": "M", "09": "P", "10": "R", "11": "S", "12": "T"}
    mese_nascita = mesi_codice[data_nascita[3:5]]

    #! GIORNO
    giorno_numero = int(data_nascita[:2]);
    if sesso == "F":
        giorno_numero += 40
    giorno_nascita = str(giorno_numero).zfill(2)

    #! CODICE_CATASTALE
    comune_nascita = comune_nascita.upper()
    # CODICE PER ITALIANI
    if stato_nascita.upper() == "ITALIA":
        file = open('C:\\Users\\matdo\\Desktop\\CODICI\\VSCode_Projects\\Python\\CodFiscalePy\\codici_catastali.txt', 'r')
        for line in file:
            line = line.strip()
            codice_catastale, comune = line.split("\t")
            if comune == comune_nascita:
                comune_codice = codice_catastale
                break
    # CODICE PER NON ITALIANI
    else:
        file = open('C:\\Users\\matdo\\Desktop\\CODICI\\VSCode_Projects\\Python\\CodFiscalePy\\codici_at_estero.txt', 'r')
        for line in file:
            line = line.strip()
            nazione, codice_catastale = line.split("\t")
            if nazione.upper() == stato_nascita.upper():
                comune_codice = codice_catastale
                break

    #! CARATTERE DI CONTROLLO
    tmp = cognome_codice + nome_codice + anno_nascita + mese_nascita + giorno_nascita + comune_codice
    somma = 0

    dispari_codice = {"0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, "6": 15, "7": 17, "8": 19, "9": 21,
                      "A": 1, "B": 0, "C": 5, "D": 7, "E": 9, "F": 13, "G": 15, "H": 17, "I": 19, "J": 21,
                      "K": 2, "L": 4, "M": 18, "N": 20, "O": 11, "P": 3, "Q": 6, "R": 8, "S": 12, "T": 14,
                      "U": 16, "V": 10, "W": 22, "X": 25, "Y": 24, "Z": 23 }
    
    pari_codice =    {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                      "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
                      "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
                      "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25 }
    
    resto_codice =   {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
                      10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
                      20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z" }
    
    for i in range(0, len(tmp)):
        if ((i+1) % 2) == 0:                                # i+1 perchè nel vettore i va da 0, ma le posizioni sono contate da 1 per il calcolo
            somma += pari_codice[tmp[i]]
        else:
            somma += dispari_codice[tmp[i]]
    resto = somma % 26
    carattere_controllo = resto_codice[resto]
    
    #! TUTTO INSIEME
    codice_fiscale = tmp + carattere_controllo

    return codice_fiscale


def main():
    
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    data_nascita = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    sesso = input("Inserisci il genere (M/F): ")
    stato_nascita = input("Inserisci lo stato di nascita: ")
    if stato_nascita.upper() == "ITALIA":
        comune_nascita = input("Inserisci il comune di nascita (con gli eventuali spazi): ")
    else:
        comune_nascita = ""

    codice = calcola_codice_fiscale(nome, cognome, data_nascita, sesso, stato_nascita, comune_nascita)
    print("Il codice fiscale è:", codice)

    return 0

if __name__ == "__main__":
    main()