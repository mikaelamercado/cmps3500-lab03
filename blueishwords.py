#course:cmps3500
#lab3
#date:2/18/20
#username:mmercado
#name:Ma Mikaela Mercado
#description: PART C: Blueish Words
blue = []
with open("constitution.txt") as file:
    data = file.read()
    for line in data.split():
        if 'e' in line and 'l' in line and 'u' in line:
            blue.append(line)
    print(len(blue))
