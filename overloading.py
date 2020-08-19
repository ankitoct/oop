class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        s3=r1+r2
        return s3
    def __mul__(self, other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        s3=r1*r2
        return s3
s1=student()
s2=student()
print(s1)

print()
print("multiply ")