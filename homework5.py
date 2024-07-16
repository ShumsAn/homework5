immutable_var = (1,2,3,[123,5],'string',True)
print(immutable_var)
immutable_var[3][0] = 4
print(immutable_var)
mutable_list = [1,2,3,4,5,6,7,'восемь','десять']
mutable_list[7] = (8)
mutable_list.remove('десять')
mutable_list.append(9)
mutable_list.extend('0123456789')
print(mutable_list)


