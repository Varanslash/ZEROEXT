import time

sixteenbit = 0
cell = 0
loop = 0
counter = 0

# ZEROEXT Parser/Lexer

while True:
    i = 0
    userinput = input("\n>>>0;")
    while i < len(userinput):
        ch = userinput[i]
        match ch:
            case ">":
                sixteenbit += 1
                i += 1
            case "<":
                sixteenbit -= 1
                i += 1
            case "0":
                print(sixteenbit, end="")
                i += 1
            case "%":
                asci = chr(sixteenbit)
                print(asci, end="")
                i += 1
            case "_":
                print(sixteenbit, cell)
                i += 1
            case "|":
                sixteenbit |= cell
                i += 1
            case "+":
                cell += 1
                i += 1
            case "-":
                cell -= 1
                i += 1
            case "1":
                print(cell)
                i += 1
            case "^":
                sixteenbit &= cell
                i += 1
            case "!":
                sixteenbit = 0
                i += 1
            case "$":
                cell = 0
                i += 1
            case "#":
                cell = sixteenbit
                i += 1
            case "?":
                sixteenbit = cell
                i += 1
            case "&":
                sixteenbit += cell
                i += 1
            case "*":
                cell += sixteenbit
                i += 1
            case ",":
                sixteenbit ^= cell
                i += 1
            case ";":
                break
            case "a":
                sixteenbit = 65
                i += 1
            case "/":
                break
            case ".":
                sixteenbit = 32
                i += 1
            case "~":
                print("\n")
                i += 1
            case "=":
                time.sleep(1)
                i += 1
            case "x":
                counter += 1
                i += 1
            case "y":
                counter -= 1
                i += 1
            case "{":
                loop = i + 1
                counter = cell
                i += 1
                continue
            case "}":
                if counter > 0:
                    counter -= 1
                    i = loop
                    continue
                else:
                    i += 1
