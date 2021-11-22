country_list = ['Russia', 'Italy', 'USA', 'England', 'French', 'Andromeda']

print(country_list)
print(sorted(country_list))
print(country_list)
print(list(reversed(country_list)))

even_numbers = list()
for even_number in range(2, 11321, 2):
    even_numbers.append(even_number ** 2)
print(even_numbers)

even_numbers = [x ** 2 for x in range(2, 11, 2)]
print(even_numbers)

million_list = [x for x in range(1000001)]

print(max(million_list))
print(min(million_list))
print(sum(million_list))

