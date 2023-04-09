# nums = [7, 8, 9, 5]
#
#
# # for i in nums:
# #     print(i)
#
# it = iter(nums) #not give all the value but give one value at a time
#
# # print(it) #object  of the `it`
# # first method
# print(it.__next__()) #give first value
# print(it.__next__())
#
# #  when we call the function of the iterator it will preserve the old value
#
# # second method
# print(next(it))
#
# for i in nums:
#     print(i)
#
#

class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration #exeption


values = TopTen()

print(next(values))

for i in values:
    print(i)
# print(next(values)) # error
