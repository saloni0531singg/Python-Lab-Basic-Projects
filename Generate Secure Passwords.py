import random
char_seq="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()."
print("Enter the required length of the password ranging from 8 to 12: ")
length=int(input())
if length>=8 and length<=14:
    password="".join(random.sample(char_seq,length))
    print("Your password is:" +password)
else:
    print("Enter a suitable range")
    








































