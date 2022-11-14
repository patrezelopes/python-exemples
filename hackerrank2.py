def sequence(start, n):
    return list(map(lambda x: start ** x, range(1, n+1)))

if __name__ == '__main__':
    print(sequence(2, 4))