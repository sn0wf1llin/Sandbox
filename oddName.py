"""Author"""


def main():
    print("Input your name: ")
    name = input()
    s = ''
    if len(name) != 0:
        for i in range(1, len(name)):
            if i % 2 == 1:
                s += name[i]
        print(s)

    else:
        print("Error")

if __name__ == "__main__":
    main()