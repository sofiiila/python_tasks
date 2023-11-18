def random_value() -> str:
    string_value = "число"
    num_value = "54"
    return num_value

# C помощью одной встроенной функции напечатай только число

random_value: str = random_value()
if random_value.isdigit():
    print(random_value)
# print(type(random_value))