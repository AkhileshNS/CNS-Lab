generator = "101"

def getbinary(val):
    return "{0:b}".format(val)

def checkcrc(message, check):
    if check:
        extension = ""
        for i in range(len(generator)-1):
            extension = extension + "0"
        message = message + extension
    message = message[1:]
    rem = (int(generator, 2) - (int(message, 2))) % int(generator, 2)
    if rem == 0:
        return 0
    else:
        return int(message, 2) + rem

def sender(message):
    return checkcrc("b" + message, True)

def receiver(message):
    message = getbinary(message)
    check = checkcrc("b" + message, False)
    if check == 0:
        print("Data transmitted with no errors")
    else:
        print("Error in data")

receiver(sender("1011011"))