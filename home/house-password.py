# Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

# Input: A password as a string.

# Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.

# checkio('A1213pokl') == False
# checkio('bAse730onE') == True
# checkio('asasasasasasasaas') == False
# checkio('QWERTYqwerty') == False
# checkio('123456123456') == False
# checkio('QwErTy911poqqqq') == True


def checkio(data):
    a=0
    b=0
    c=0
    if len(data)>=10:
        for i in data:
            if i.isnumeric():
                a=1
            if i.islower():
                b=1
            if i.isupper():
                c=1
    else:
        return False
    if a==1 and b==1 and c==1:
        return True
    else:
        return False
