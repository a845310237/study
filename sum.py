
def add(n):
    sum = 0
    while n > 0:
        n = n //5
        sum += n
    return sum
print(add(100))