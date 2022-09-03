def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a positive number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")


main()
