# 1) Попросить пользователя ввести текст. В результате вывести 
# процент букв в верхнем
# регистре (заглавные) и в нижнем регистре (прописные).

text = input("Enter your text: ")
lenght = len(text)
space = 0
lower = 0
upper = 0
for i in text:
    if i.isupper():
        lower+=1
    elif i.islower():
        upper+=1
    elif i == " ":
        space+=1
full_lenght = lenght - space
percentage = 100 / full_lenght
upper_percentage = upper * percentage 
lower_percentage = lower * percentage
    
print(full_lenght)
print(percentage)
print(upper_percentage)
print(lower_percentage)