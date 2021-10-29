ones = ["zero","One","Two","Three","Four","Five","six","seven","eight","nine"]

teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

ten = ["ten","Tewenty","thirty","fourty","Fifty","Sixty","Eeventy","Eighty","Ninety"]


def numberinwords(number):
    length = (len(str(number)))
    if(length ==0):
        print("No Input")
    elif(length == 1):
        print(ones[number-1].capitalize())
    elif(length == 2):
        if((str(number)[1]) == '0'):
            print(ten[(int(number/10)-1)].capitalize())
        elif((str(number)[0]) == '1'):
            print(teens[(int(number%10)-1)].capitalize())  
        else:
            print(ten[(int(number/10)-1)].capitalize(), ones[(int(number%10))].capitalize())
    else:
        print("sorry idk")
print("###########################################")
for i in range(1,100):
    numberinwords(i)

