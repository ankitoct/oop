# nums=[1,2,3,4,5,2,6,7,8,22,33,44]
# it=iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return  self
    def __next__(self):
        if self.num<=10:

            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values= TopTen()
print(values.__next__())
for i in values:
    print(i)
 