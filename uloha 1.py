import math
l=input("Zadaj mi priemer podstavy: ")
l=int(l)
u=l/2
k=input("Zadaj mi výšku valca: ")
u=int(u)
k=int(k)
podstava=math.pi*(u**2)
plast=(2*math.pi)*u*k
povrch=(podstava+plast)*2
plechovky=povrch//7.5
print("Na natrenie fontánky treba ",plechovky," plechoviek.")
