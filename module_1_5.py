immutable_var = ("У", "лукоморья", ["дуб", "зеленый"], 33, "богатыря", True, 3.14)
print(immutable_var)

immutable_var[3] = 43
print(immutable_var)
# нельзя менять кортеж, так как он является неизменяемым элементом коллекции

mutable_list = ['Apple', 'Samsung', 'Huawei', 'Xiaomi']
print(mutable_list)

mutable_list.extend(['Honor', 'Poco', 'Realme'])
print(mutable_list)

mutable_list.sort()
print(mutable_list)