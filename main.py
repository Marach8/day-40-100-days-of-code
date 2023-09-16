print('Contact Card')
print()
dict = {}

ask1 = input('Input your name: ')
print()
ask2 = input('Input your date of birth: ')
print()
ask3 = input('Input your telephone number: ')
print()
ask4 = input('Input your email: ')
print()
ask5 = input('Enter your house address: ')

dict['name'] = ask1
dict['DOB'] = ask2
dict['telephone'] = ask3
dict['email'] = ask4
dict['address'] = ask5


print(f'''
Hi {dict['name']}. Our dictionary says that you were born on {dict['DOB']}, we can call you on {dict['telephone']}, email {dict['email']}, or write to {dict['address']}.
''')
