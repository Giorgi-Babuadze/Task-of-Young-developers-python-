try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("შეცდომა: ფაილი არ მოიძებნა")