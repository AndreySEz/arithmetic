def arithmetic(a, b, sym):
	if sym == "+":
		print("Ответ: ", a+b)
	elif sym == "-":
		print("Ответ:", a-b)
	elif sym == "*":
		print("Ответ:", a*b)
	elif sym == "/":
		print("Ответ:", a/b)
	else:
		print("Неизвестная операция.")

a = int(input("Введите первое число: "));
b = int(input("Введите второе число: "));
sym = input("Выберите знак: (+, -, *, /): ");
arithmetic(a, b, sym)