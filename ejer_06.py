
import string

p = input('Contraseña: ')
char = string.ascii_letters + string.digits

for i in p:
    pwd = i + char[:30:2] + char[31::-2]

print(pwd)
