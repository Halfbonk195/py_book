guests_list = ['Tesla', 'Yagami', 'L', 'Whicher', 'Andromed',]
invite_massage = 'I invite you to my super mega monday party!'


for guest in guests_list:
    print(f'{guest}, {invite_massage}')

not_visit_guest = 'L'
print(f'{not_visit_guest}, will not be able to attend the party')
guests_list[2] = 'Shakira'
print()
for guest in guests_list:
    print(f'{guest}, {invite_massage}')

print()
print('3 more guests want to come to the party: Irakly, Madonna, Afonya')

guests_list.insert(0, 'Irakly')
guests_list.insert(4, 'Madonna')
guests_list.append('Afonya')
for guest in guests_list:
    print(f'{guest}, {invite_massage}')

print()
print('Unfortunately only two guests are invited to the party...')
print(f'{guests_list.pop(0)}, we dont love you!')
print(f'{guests_list.pop(0)}, we dont love you!')
print(f'{guests_list.pop(0)}, we dont love you!')
print(f'{guests_list.pop(0)}, we dont love you!')
print(f'{guests_list.pop(0)}, we dont love you!')
print(f'{guests_list.pop(0)}, we dont love you!')
for guest in guests_list:
    print(f'{guest}, {invite_massage}')
