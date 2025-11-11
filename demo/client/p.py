def sum_all(*args):
    return sum(args)
    # res=0
    # for i in args:
    #     res+=i 
    # print(res)

# list = ["1", "4", "0", "6", "9"]
# res=[int(i) for i in list]
# res.sort()
# print(res)

# even_numbers=list(filter(lambda x:x%2==0,range(1,12)))
# odd_numbers=list(filter(lambda x:x%2,range(1,12)))
# print(even_numbers)
# print(odd_numbers)

# from functools import reduce
# res= reduce(lambda x,y:x+y,[1,2,3])
# print(res)
# name="mahesh patil"
# s=name.split()
# print(s)
# res=[x[::-1] for x in s]
# print(res)
# print(res[::-1])
# print(" ".join(res))

# def do_sum(n):
#     if len(n)==1:
#         return n[0]
#     else:
#         result=n[0]+do_sum(n[1:])
#         return result

# n=[1,2,3]
# print(do_sum(n))