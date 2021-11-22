guests_list = ['Tesla', 'Yagami', 'L', 'Whicher', 'Andromed',]
invite_massage = 'I invite you to my super mega monday party!'

print(f'{guests_list[0]}, {invite_massage}')
print(f'{guests_list[1]}, {invite_massage}')
print(f'{guests_list[2]}, {invite_massage}')
print(f'{guests_list[3]}, {invite_massage}')

for guest in guests_list:
    print(f'{guest}, {invite_massage}')
