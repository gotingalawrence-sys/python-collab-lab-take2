# ✏️ Your Code Here
for n in range(1, 31):
    # YOUR CODE HERE
    if n % 3 == 0 and n % 5 == 0:
        print ("FizzBuzz")
        #return()
    elif n % 3 == 0:
        print("Fizz")
        #return
    elif n % 5 == 0:
        print ("Buzz")
        #return
    else:
        print (n)