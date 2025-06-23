def binario(num, binMode = 0):
    answer = []
    num = int(num)
    while num > 0:
        answer.append(str(num%2))
        num //= 2
    
    leng = 5 if binMode == 0 else 7 if binMode == 1 else 8 
    while len(answer) < leng:
        answer.append("0")
    if binMode == 1:
        answer.insert(2, " ")
    elif binMode == 2:
        answer.insert(0, "   ")
        answer.insert(6, " ")
        answer.append("  ")

    return "".join(answer)

comandos = {
    "inc" : "10010",
    "dec" : "01000",
    "sub" : "01010",
    "add" : "00000",
    "shfr": "00011",
    "xnor": "00001",
    "nand": "11100",
    "rnd" : "10010",
    "xor" : "01001",
    "nor" : "00101",
    "and" : "11101",
    "or"  : "00100",
    "str" : "11111",
    "jmf" : "11000",
    "cpy" : "00010",
    "jmp" : "11110",
    "end" : "01111",
}

memorias = {
    "R":"00",
    "M":"01",
    "?":"10",
    "!":"11"
}

def modele(linha):
    if linha[-1] != "\n":
        linha += "\n"
    termo = ""
    total = ""

    binMode = 0

    for char in linha:
        if char == " " or char == "\n":
            if termo.isnumeric():
                termo = binario(termo, binMode)
            total += termo + char
            termo = ""
            binMode = 0
            
        elif char in memorias:
            total += memorias[char] + " "
            termo = ""

        elif char in "LN":
            if char == "L":
                binMode = 1
            else:
                binMode = 2
        else:
            termo += char
        
    qtd = total.count(" ")
                
    if qtd == 3:
        total = total[:8] + "      " + total[8:]
    elif qtd == 1:
        total = total[:0] + "               " + total[0:]

    return(" "+total)

total = ""
with open("in.txt", "r") as file:
    l = 0
    for line in file:
        tokens = line.strip().split()
        for comando in comandos:
            if tokens and tokens[0] == comando:
                if comando != "end":
                    line = str(l) + " - " + comandos[comando] + modele(line.replace(comando, "")[1:])
                else:
                    line = str(l) + " - " + comandos[comando]
        l += 1
        total += (line)

with open("out.txt", "w") as file:
    file.write(total) 