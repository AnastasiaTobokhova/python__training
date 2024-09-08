immutable_var = (1,2,3,4,5)
print(immutable_var)
immutable_var = (1,2, True, [1,2] )
print(immutable_var)
immutable_var = (1,2, True, [1,2])+(6,7)  #1 изменение
print(immutable_var)
immutable_var = (1,2,3,4,5)*3   #2изменение
print(immutable_var)
mutable_list = [1,2,3,4,5]
print(mutable_list)
mutable_list[2] = 'peach'
print(mutable_list)