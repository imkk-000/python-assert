def main():
    msg = "Hello World"
    print("string: ", msg)
    print("len of: ", len(msg))

def power(baseNumber, powerNumber):
    return baseNumber ** powerNumber

if __name__ == "__main__":
    main()
    print("power: " + str(power(2, 10)))
