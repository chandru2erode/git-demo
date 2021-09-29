def cube(num):
    return num * num * num

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(list(map(cube, numbers)))
