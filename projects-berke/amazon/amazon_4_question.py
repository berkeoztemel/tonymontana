def main():
    counter = 5
    AlwaysTrue = True
    value1 = 10
    FloatValue1 = 5.5

    if value1 < FloatValue1 or AlwaysTrue:
        counter += 1
    else:
        counter = 1

    while counter > 0:
        counter-= 1
        AlwaysTrue = not AlwaysTrue

    if AlwaysTrue:
        print("It is always true")

    else:
        print("It seems it is not always true after all")

main()
