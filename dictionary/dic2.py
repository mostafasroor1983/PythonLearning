digits = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

output = ''
while True:
    phone = input("Enter your phone number: ")
    for ch in phone:
        if ch in digits:
            output += digits[ch] + " "
        else:
            print("Not a digit")
    print(output.strip())
