numer=input("Nnumero: ")

cad = [numer]
temp = []

# for i in range(1,1001):
#     cad.append(str(i))
lista=[]
num=""
test=""

for i in cad:
    for j in i:
        temp.append(j)
    for k in temp:
        match(k):
            case "1":
                num="One"
            case "2":
                num="Two"
            case "3":
                num="Three"
            case "4":
                num="Four"
            case "5":
                num="Five"
            case "6":
                num="Six"
            case "7":
                num="Seven"
            case "8":
                num="Eight"
            case "9":
                num="Nine"
            case "0":
                num=""

        lista.append(num)

    lista.reverse()

    if len(lista) > 1:
        match lista[1]:
            case "One":
                if lista[0]=="One":
                    lista[1]="Eleven"
                    lista[0]=""
                elif lista[0]=="Two":
                    lista[1]="Twelve"
                    lista[0]=""
                elif lista[0]=="Three":
                    lista[1]="Thirteen"
                    lista[0]=""
                elif lista[0]=="Four":
                    lista[1]="Fourteen"
                    lista[0]=""
                elif lista[0]=="Five":
                    lista[1]="Fifteen"
                    lista[0]=""
                elif lista[0]=="Six":
                    lista[1]="Sixteen"
                    lista[0]=""
                elif lista[0]=="Seven":
                    lista[1]="Seventeen"
                    lista[0]=""
                elif lista[0]=="Eight":
                    lista[1]="Eighteen"
                    lista[0]=""
                elif lista[0]=="Nine":
                    lista[1]="Nineteen"
                    lista[0]=""
                elif lista[0]=="":
                    lista[1]="Ten"
                    lista[0]=""
            case "Two":
                lista[1]="Twenty"
            case "Three":
                lista[1]="Thirty"
            case "Four":
                lista[1]="Forty"
            case "Five":
                lista[1]="Fifty"
            case "Six":
                lista[1]="Sixty"
            case "Seven":
                lista[1]="Seventy"
            case "Eight":
                lista[1]="Eighty"
            case "Nine":
                lista[1]="Ninety"
            case "":
                lista[1]=""

    if len(lista)==1:
        test+=f"{lista[0]}"
    elif len(lista)==2:
        test+=f"{lista[1]}{lista[0]}"
    elif len(lista)==3:
        if lista[1]=="" and lista[0]=="":
            test+=f"{lista[2]}Hundred"
        else:
            test+=f"{lista[2]}Hundredand{lista[1]}{lista[0]}"
    elif len(lista)==4:
        test+=f"OneThousand"

    temp=[]
    lista=[]

# with open("numerote.txt","w") as f:
#     f.write(test)

print(len(test))
print(test)