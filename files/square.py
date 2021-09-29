def square(num):
    return num * num

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(list(map(square, numbers)))