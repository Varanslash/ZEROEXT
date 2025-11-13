

sixteenbit = 0
cell = 0

# ZEROEXT Parser/Lexer

while True:
    userinput = input(">>>0;")
    for ch in userinput:
        match ch:
            case ">":
                sixteenbit += 1
            case "<":
                sixteenbit -= 1
            case "0":
                print(sixteenbit, end="")
                print()
            case "/":
                exit()
            case "%":
                asci = chr(sixteenbit)
                print(asci, end="")
                print()
            case "@":
                print(">, <, 0, /, %")
            case "_":
                print(sixteenbit, cell)
            case "+":
                cell += 1
            case "-":
                cell -= 1
            case "1":
                print(cell)
            case "!":
                sixteenbit = 0
            case "$":
                cell = 0
            case "#":
                cell = sixteenbit
            case "^":
                sixteenbit = cell
            case "&":
                sixteenbit += cell
            case "*":
                cell += sixteenbit
            case "{":
                userinput = input(">>>{")
                for _ in range(cell):
                    for ch in userinput:
                        match ch:
                            case ">":
                                sixteenbit += 1
                            case "<":
                                sixteenbit -= 1
                            case "0":
                                print(sixteenbit)
                            case "%":
                                asci = chr(sixteenbit)
                                print(asci)
                            case "1":
                                print(cell)
                            case "}":
                                break
                break