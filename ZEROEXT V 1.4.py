import time

sixteenbit = 0
cell = 0
loop = 0
counter = 0
stack = []

# ZEROEXT Parser/Lexer

while True:
    i = 0
    n = 0
    userinput = input("\n>>>0;")
    try:
        while n < len(userinput):
            ch = userinput[n]
            match ch:
                case ">":
                    n += 1
                case "<":
                    n += 1
                case "0":
                    n += 1
                case "%":
                    n += 1
                case "_":
                    n += 1
                case "|":
                    n += 1
                case "+":
                    n += 1
                case "-":
                    n += 1
                case "1":
                    n += 1
                case "^":
                    n += 1
                case "!":
                    n += 1
                case "$":
                    n += 1
                case "#":
                    n += 1
                case "?":
                    n += 1
                case "&":
                    n += 1
                case "*":
                    n += 1
                case ",":
                    n += 1
                case "[":
                    n += 1
                case "a":
                    n += 1
                case "/":
                    n += 1
                case ".":
                    n += 1
                case "~":
                    n += 1
                case "=":
                    n += 1
                case "x":
                    n += 1
                case "y":
                    n += 1
                case "{":
                    n += 1
                case "}":
                    n += 1
                case "]":
                    n += 1
                case "(":
                    ifs = n + 1
                    stack.append(ifs)
                    n += 1
                case ":":
                    counter -= 1
                    ifelsemedian = n
                    stack.append(ifelsemedian)
                    n += 1
                case ")":
                    elses = n
                    stack.append(elses)
                    n += 1
                case _:
                    n += 1

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
                case "[":
                    while i < len(userinput) and userinput[i] != "]":
                        i += 1
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
                    stack.append(loop)
                    counter = cell
                    i += 1
                    continue
                case "}":
                    if counter > 0:
                        counter -= 1
                        i = stack[-1]
                        continue
                    else:
                        stack.pop()
                        i += 1
                case "]":
                    i += 1
                case "(":
                    if cell != 0:
                        pass
                    else:
                        i = ifelsemedian
                    i += 1
                    continue
                case ":":
                    if cell != 0:
                        counter -= 1
                        i = elses
                        cell = 0
                        counter = 0
                        continue
                    else:
                        i += 1
                case ")":
                    if counter > 0:
                        counter -= 1
                        i = stack[-1]
                        continue
                    else:
                        try:
                            stack.pop()
                            i += 1
                        except IndexError:
                            i += 1
                case _:
                    i += 1
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt Error")
        print("Luckily, Varan recovered the IDE safely!")