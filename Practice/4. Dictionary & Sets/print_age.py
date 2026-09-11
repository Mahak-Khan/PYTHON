name = input("Name:")
age = int(input("Age:"))
city = input("City:")

info = {}
info.update({"Name" : name})
info.update({"Age" : age})
info.update({"City" : city})

print(info)
print(info.get("Age"))