food: list = ["mango", "cucumber", "tomato",  "onion"]
index: int = 1
print(food[1])
  
my_string: str = "London is the capital of GB"

for index, sign in enumerate(my_string):
    if index == 5:
        my_string = my_string[1:] + my_string[0] + "!"
    else:    
        my_string = my_string[1:] + my_string[0]  
print(my_string)         
