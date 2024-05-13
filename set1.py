myset={"ritika","bhandari","prashant","laptop","table"}
rset={'apple','kiwi','strawberry'}
# print(type(myset))
# print(len(myset))

# accessing elements using loops
# for i in myset:
#     print(i)

# print('laptop'in myset)

# myset.add('chair')
# print(myset)

# myset.append("chair")
# print(myset)

# myset.update(rset)
# print(myset)

# myset.remove(rset)
# print(myset)

# myset.discard('laptop')
# print(myset)

# a=myset.pop()
# print(a)

# del myset
# print(myset)

# ans=myset.union(rset)
# print(ans)

ans=myset|rset
print(ans)