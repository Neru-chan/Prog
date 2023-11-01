def task1():
    print("--- TASK 1 ---")
    name = input("Enter your name: ");
    print(f"Hello {name}!")

def task2():
    print("--- TASK 2 ---")
    name = input("What is your name? ")
    age  = input("How old are you? ")
    place= input("Where do you live?" )
    result = f'''
        "This is {name}"
    "(S)he is {age} years old"
    "(S)he lives in {place}"
    '''
    print(result)

def task3():
    print("--- TASK 3 ---")

    while True:
        try:
            a, b = input("Enter 2 variables separated by a ',' symbol ").split(',')
            print(f"a = {a}, b = {b}")
            break;
        except ValueError:
            print("ERROR: Should 2 variables separated by a ',' symbol")

def task4():
    print("--- TASK 4 ---")

    while True:
        try:
            a,b,c,d = input("Enter 4 variables separated by a ';' symbol ").split(';')
            for i in a,b,c,d:
                print(i)
            break
        except ValueError:
            print("ERROR: Should 4 variables separated by a ';' symbol")

def task5():
    print("--- TASK 5 ---")

    while True:
        try:
            year = int(input("What is current year? "))
            print(f"In 50 years it will be {year + 50} year")
            break
        except ValueError:
            print("ERROR: Enter valid int number")

def task6():
    print("--- TASK 6 ---")

    while True:
        try:
            d, m, y = input("What is your birthday? Enter Date in dd.mm.yyyy format: ").split('.')
            print(f"Your birthday is {d} Day, {m} Month, {y} Year")
            break
        except ValueError:
            print("ERROR: Enter 3 valid int numbers separated by '.'")

def task7():
    print("--- TASK 7 ---")

    while True:
        try:
            a, b = input("Enter 2 numbers ").split(' ')
            a, b = int(a), int(b)
            print(f"a + b = {a+b}")
            print(f"a - b = {a-b}")
            print(f"a * b = {a*b}")
            print(f"a / b = {a/b}")
            print(f"a {'>' if a > b else '<'} b")

            break
        except ValueError:
            print("ERROR: Enter 2 valid numbers separated by ' '")

def task8():
    print("--- TASK 8 ---")

    while True:
        try:
            li = [a, b, c, d] = input("Enter 4 numbers ").split(' ')
            [a, b, c, d] = [int(i) for i in li]
            print(f"(a + b) / (c + d) = {(a + b) / (c + d):.2f}")
            break
        except ValueError:
            print("ERROR: Enter 4 valid numbers separated by ' '")

def task9():
    print("--- TASK 9 ---")

    while True:
        try:
            li = [a, b] = input("Enter 2 numbers ").split(' ')
            [a, b] = [int(i) for i in li]
            print(f"a / b = {int(a / b)}, ({a % b})")
            break
        except ValueError:
            print("ERROR: Enter 2 valid numbers separated by ' '")

def task10():
    print("--- TASK 10 ---")

    while True:
        try:
            a = int(input("Enter 2 digit number "))
            if (a < 10 or a > 99): continue
            li = str(a)
            li = [int(i) for i in li]
            print(f"sum of digits in {a} = { sum(li) }")
            break
        except ValueError:
            print("ERROR: Enter valid 2 digit number")

def task11():
    print("--- TASK 11 ---")

    while True:
        try:
            a = int(input("Enter number "))
            print(f"last digit of {a} is {a % 10})")
            break
        except ValueError:
            print("ERROR")

task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()
task11()