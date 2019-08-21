def collatz(usrinpt):
    if(usrinpt == 1):
        return
    elif(usrinpt%2 == 0):
        print(str(usrinpt//2))
        return collatz(usrinpt//2)
    elif(usrinpt%2 == 1):
        print(str((3*usrinpt+1)))
        return collatz((3*usrinpt+1))


numberToCollatz = int(input("Digit to collatz: "))
collatz(numberToCollatz)
print("digit was collatzed")
