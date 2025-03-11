numone = int(input("the first number"))
numtwo = int(input("input the second number"))

result = int(numone * numtwo)
print(str(numtwo)+" "+"x"+" "+str(numtwo)+" "+"="+" "+str(result))

if result > 0:
    print("This result is positive.")

elif result < 0:
    print("The result is negative.")
    
else:
    print("The result is positive and negagive.")