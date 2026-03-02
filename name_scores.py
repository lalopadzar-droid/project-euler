
name=[]
name_sort=[]
temp=[]
suma=0
score=0

with open("names.txt", mode="r") as archivo:
    content = archivo.read()

name = content.replace('"','').split(',')
print(len(name))
        
name_sort=sorted(name)
print(name_sort)

for i in name_sort:
    pos = name_sort.index(i)+1
    for j in i:
        temp.append(j)
    for k in i:
        match(k):
            case 'A':
                suma+=1
            case 'B':
                suma+=2
            case "C":
                suma+=3
            case 'D':
                suma+=4
            case 'E':
                suma+=5
            case 'F':
                suma+=6
            case 'G':
                suma+=7
            case 'H':
                suma+=8
            case "I":
                suma+=9
            case 'J':
                suma+=10
            case 'K':
                suma+=11
            case "L":
                suma+=12
            case 'M':
                suma+=13              
            case "N":
                suma+=14
            case "O":
                suma+=15
            case 'P':
                suma+=16
            case 'Q':
                suma+=17
            case 'R':
                suma+=18
            case 'S':
                suma+=19
            case 'T':
                suma+=20
            case 'U':
                suma+=21
            case 'V':
                suma+=22
            case 'W':
                suma+=23
            case 'X':
                suma+=24
            case 'Y':
                suma+=25
            case 'Z':
                suma+=26
    temp=[]

    # print(suma)
    # print(suma*pos)
    score+=suma*pos
    suma=0

print(f"Total: {score}")