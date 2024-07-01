a= "L8G ZPF2103075"
# b= "ZPF 2103075"
b="[| 85 ZPF0723189"
b="| ZPF 1852672"

# un_id = "LJ NUE2415065"

# print("before split",un_id)
# un_id2=un_id.split(' ')
# print(un_id2)
# if len(un_id2[-1])+len(un_id2[-2]) == 10:
#     un_id=un_id
# else:
#     print("after split",un_id2[-1])
#     un_id=un_id2[-1]

# print("f",un_id)



un_id2 =['UP/9/041/0024532WW:','']

for i in range(len(un_id2)):
    print("after split",un_id2[-i])
    if len(un_id2[-i]) <= 6:
        un_id=un_id2[-i-1]
    else:
        un_id=un_id2[-i]
print("final",un_id)