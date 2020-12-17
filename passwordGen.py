import random
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
specialChar ="!@#$%^&*()_-+=`~[{]};:',<.>/?"
nums = '1234567890'
allchar = caps + lower + specialChar + nums
#creates password
def makePass():
    password = ''
    while len(password) < length:
        #find random char in allchar to add to password
        password += allchar[random.randint(0, len(allchar) - 1)]
    return(password)
while True:
    print('Length of password?')
    length = (int(input()))
    print(makePass())
    print('Continue (Y/N)')
    answer = input()
    if answer == 'Y' or answer == 'y':
        continue
    else:
        quit()