import string, random

pass_len = int(input("Enter the length?"))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Combined
         5. Exit''')

chars = ''

while True:
    choice = int(input('Pick a number '))
    if choice == 1:
        chars += string.digits
        break
    elif choice == 2:
        chars += string.ascii_letters
        break
    elif choice == 3:
        chars += string.punctuation
        break
    elif choice == 4:
        chars += string.digits + string.ascii_letters + string.punctuation
        break
    elif choice == 5:
        break
    else:
        print("Enter a valid option")

password = []

for _ in range(pass_len):
    
    randomchar = random.choice(chars)
    
    password.append(randomchar)

print('generated ' + "".join(password))