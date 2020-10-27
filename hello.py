# var=


def one(x):
    """input is variable, unit is work is x+1, result is return"""
    return x + 1


def two(xx):
    """input, unit of work, result"""

    return xx + 2


def three(xxx):
    """input, unit of work, result"""

    return xxx + 3


def main(myinput=1):
    x = one(myinput)
    print(x)
    xx = two(x)
    print(xx)
    xxx = three(xx)
    print(xxx)
    return xxx


if __name__ == "__main__":
    main()
