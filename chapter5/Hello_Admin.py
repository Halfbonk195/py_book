names_list = ['Drakula', 'Antosha', 'admin', 'Timofey']
new_users = ['AnToShA', 'LenA', 'Dasha', 'Timofey']

if names_list:
    for name in names_list:
        if name == 'admin':
            print(f'Hello {name}! Would you like to see a status report?')
        else:
            print(f'Hello {name}! Welcome to the site!')
else:
    print('We need to find some users!')
print()

tmp_new_users = [x.lower() for x in new_users]
tmp_names_list = [x.lower() for x in names_list]

for user in tmp_new_users:
    if user in tmp_names_list:
        print(f'Name "{user.title()}" is taken! Please choose another name.')
    else:
        print(f'Name "{user.title()}" is valid!')
