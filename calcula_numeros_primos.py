def is_prime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('Write a number: '))
    new_num = mersenne_number(num)
    result = is_prime(new_num)
    print("Mersenne number:", new_num)
    if(result):
        print("El numero:", num ,"es numero primo")
    else:
        print("El numero:", num ,"NO es numero primo")

def mersenne_number(p) :
    if not isinstance(p, int):
        raise TypeError("p must be integer")
    return (2 ** p) - 1


if __name__ == '__main__':
    app()
