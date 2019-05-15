p = int(input("Enter the value of Prime modulus 'p' : "))
g = int(input("Enter the value of generator 'g' : "))
Xa = int(input("Enter the value of first secret number 'Xa': "))
Xb = int(input("Enter the value of second secret number 'Xb': "))

if Xa < p and Xb < p:
    Ya = (g**Xa) % p
    Yb = (g**Xb) % p

    print("Sending Ya= " + str(Ya) + " to Bob ")
    print("Sending Yb= " + str(Yb) + " to Alice")

    Ka = (Yb**Xa) % p
    Kb = (Ya**Xb) % p

    if Ka == Kb:
        print("Key K = " + str(Ka) + " Generated Successfully")
    else:
        print("Key not generated")

else:
    print("Values of Xa and Xb are not less than prime modulus")