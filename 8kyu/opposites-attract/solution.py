from random import randrange

flower1 = randrange(3000)
flower2 = randrange(3000)
print(flower1, flower2)

def lovefunc(flower1, flower2):
    return ((flower1 + flower2) % 2) != 0

if __name__ == '__main__':
    print(lovefunc(flower1, flower2))