first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f'Hello, {full_name.title()}!')
massage = f'Hello, {full_name.title()}!'
print(massage)

symbols = '\n\t'
print(f"Languages:{symbols}Python{symbols}C{symbols}JavaScript")

# Лишние пропуски

favorite_language = 'python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = '   python'
favorite_language = favorite_language.lstrip()
print(favorite_language)
