def params(req, de= "Mahak"):
    print(req, de)


r = 9
d = "India"
#dono arguments ke saath
params(r,d)   #9, India
#sirf required argument ke saath
params(r)     #9, Mahak