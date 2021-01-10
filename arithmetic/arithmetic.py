a = int(input("Введи первое число: "));
b = int(input("Введи второе число: "));
s = input("Выберите знак:=(+,-,*,/): ");
if s == "+":
	print(a+b)
elif s == "-":
	print(a-b)
elif s == "*":
	print(a*b)
elif s == "/":
	print(a/b)
else:
	print("Неизвестная операция.")
