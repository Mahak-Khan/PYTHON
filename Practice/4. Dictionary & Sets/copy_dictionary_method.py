info = {
    "Name" : "Mahak",
    "Age" : 21,
    "City" : "Kurukshetra",
    "Course" : "Python"
}

info_cpy = info.copy()
print(info_cpy)

info.pop("Age")  
print(info)