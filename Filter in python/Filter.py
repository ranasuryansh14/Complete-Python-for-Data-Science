def even(num):
    if num % 2 == 0:
        return True

# with Filter function
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
x =list(filter(even, lst))
print(x)


grt_num = list(filter(lambda v: v>6, lst))
print(grt_num)


## Filter With a Lambda Function And Multiple Conditions

numbers = [1,2,3,4,5,6,7,8,9]
evn_grt = list(filter(lambda x: x>3 and x%2 == 0, numbers))
print(evn_grt)

# filter operation on Dictionary

people = [
    {"Name":"Suryansh", "Age":22},
    {"Name":"Krishna", "Age":25},
    {"Name":"Kittu", "Age":15}
]
def age_grt_thn_20(person):
    return person['Age']>20
print(list(filter(age_grt_thn_20, people)))
