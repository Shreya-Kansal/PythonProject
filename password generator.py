import string
import random

if __name__ == "__main__":
# use lowercase alphabets
    s1 = string.ascii_lowercase
# useuppercase alphabets
    s2 = string.ascii_uppercase
# use digits to create password
    s3 = string.digits
# use special characters
    s4 = string.punctuation
# take the input from the user
    pass_len =int(input("enter the length of the passsword"))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    print("your password is :")
    print("".join(s[:pass_len]))