number = int(input("შეიყვანე რიცხვი: "))
try:
    result = 10 / number
except ZeroDivisionError:
    print("შეცდომა: ნულით გაყოფა არ შეიძლება")
else:
    print("შედეგია: ", result)