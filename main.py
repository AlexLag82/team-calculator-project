def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # ИСПРАВЛЕНИЕ 1: Проверка деления на ноль
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    # ИСПРАВЛЕНИЕ 2: Обработка отрицательных степеней
    try:
        result = a ** b
        return result
    except:
        return "Ошибка: невозможно вычислить степень"


def main():
    print("Простой калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Выберите операцию (1/2/3/4): ")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"Результат: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Результат: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Результат: {result}")
    elif choice == '4':
        result = divide(num1, num2)  # Здесь может быть ошибка деления на 0!
        print(f"Результат: {result}")
    else:
        print("Неверный выбор")


if __name__ == "__main__":
    main()