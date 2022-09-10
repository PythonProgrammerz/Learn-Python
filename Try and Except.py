def main():
    l = loop("Enter a integer: ")
    print(f"x is {l}")


def loop(x):
    while True:
        try:
            return int(input(x))
        except ValueError:
            continue


main()
