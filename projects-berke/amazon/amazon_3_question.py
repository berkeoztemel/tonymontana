

def main():
    # basic maths and types
    a = 10
    b = 4
    c = 0
    c = a // b

    print(f"c = {c}")

    # Array and loop
    int_array = [0] * 7
    int_array[0] = 1
    int_array[1] = 1

    for i in range(2, 7):
        int_array[i] = int_array[i - 1] + int_array[i - 2]

    print(f"int_array[6] = {int_array[6]}")

main()
