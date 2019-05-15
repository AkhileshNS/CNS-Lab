import random

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
           else:
               return True
    else:
       return False

def main():
    print ("Sender's Side")
    print ("-------------")
    #key = int(raw_input("Enter Key: "))
    #message = raw_input("Enter message: ")
    key = int(input("Enter Key: "))
    message = input("Enter message: ")
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + key)

    print ("Encrypted message:", encrypted_message)

    p = int(input("Enter a prime number: "))
    if not is_prime(p):
        print ("Not Prime")
        return
    q = int(input("Enter another prime number: "))
    if not is_prime(q) and q != p:
        print ("Not Prime or Same as previous")
        return
    
    n = p * q
    z = (p - 1) * (q - 1)
    smallest = p if p < q else q
    e = random.randrange(2, smallest)
    while gcd(e, z) != 1:
        e = random.randrange(e,z)

    for i in range(1,100):
        if (i * e) % z == 1:
            d = i
            break

    public_key = (n, e)
    private_key = (n, d)
    print (public_key, private_key)

    cp = (key ** e) % n
    print ("Encrypted Key:", cp)
    
    decrypted_key = (cp ** d) % n
    print ("Decrypted Key:", decrypted_key)

    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - decrypted_key)

    print ("Decrypted message:", decrypted_message)
    
main()
