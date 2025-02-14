# # class MyIterator:
# #     def __init__(self,data):
# #         self.data=data
# #         self.position=0
        
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.position>=len(self.data):
# #             raise StopIteration
# #         result = self.data[self.position]
# #         self.position += 1
# #         return result
# # i=MyIterator([1,2,3])
# # for j in i:
# #     print(j)
        
# def mygen():
#     yield 'a'
#     yield 'b'
#     yield 'c'
# g=mygen()
# print(next(g))
# print(next(g))
print('신씨가 소리질렀다 "도둑이야"')