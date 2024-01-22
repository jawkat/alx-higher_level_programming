try:
    file = open("test.py","r")
    print(file.read())
except FileNotFoundError as er:
    print("File not found",er)
finally:
    file.close()
