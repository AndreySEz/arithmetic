a = int(input("Введите первое число: "));
b = int(input("Введите второе число: "));
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
