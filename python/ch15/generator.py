# def mygen():
#     yield 'a'
#     yield 'b'
#     yield 'c'
# g=mygen()
# print(next(g))
# print(next(g))
# print(next(g))
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result
gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))