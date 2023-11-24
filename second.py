import random
 
def random_sign() -> str:
    c_value = "С"
    m_value = "М"
    sign = random.choice([c_value, m_value])
    return sign

random_sign: str = random_sign()
string_without_sign: str = "Наша аша глупая!"
print(string_without_sign)


# sign_index: str = string_without_sign.find(random_sing)
# if sign_index != -1:
#     new_string = string_without_sign[:sign_index] + random_sing + string_without_sign[sign_index+len(random_sing):]
#     print(new_string)
# else:
#     print("Sign not found")

# Подставь в строку недостающий знак используя переменные random_sing и string_without_sign
# x = 5
# y = 10
# print(f"Сумма чисел {x} и {y} равна {x + y}.")

