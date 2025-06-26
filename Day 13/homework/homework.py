def chaanacvle_simbolebi(sityva):
    xmovnebi = "aeiouAEIOUაეიიოუ"
    rezultati = ""
    for aso in sityva:
        if aso.isalpha():  # თუ ასოა
            if aso in xmovnebi:
                rezultati += "!"
            else:
                rezultati += "*"
        else:
            rezultati += aso  
    return rezultati
print(chaanacvle_simbolebi("hello123"))

