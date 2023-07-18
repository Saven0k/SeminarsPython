def SimpleNumber():
    number = int(input("Введите не отрицальное число, которое не больше 100.000: "))
    if number < 0 or number > 100000:
        print("Число или отрицательное или больше 100000, введите число заново")
        SimpleNumber()
    else:
        temp = False
        for g in range(2, 11):
            if number % g == 0 and number // 1 == number: temp = False
            if number % g != 0 and number // 1 and number % 2 == 0: temp = True

        if temp:
            print(f"Число {number}, простое")
        else:
            print(f"Число {number}, составное")


SimpleNumber()