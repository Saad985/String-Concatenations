#string concatenation
first_name="Muhammad Saad"
last_name="Amjad"

full_name=first_name+last_name           #without space
print(full_name)

full_name=first_name +" "+ last_name       #with space
print (full_name)

#full_name=first_name+3     #error
#print(full_name)

full_name=first_name+"3"         #no error,withoutspace
print(full_name)

full_name=first_name+str(3)       #no error,without space
print (full_name)

full_name=first_name+" "+str(3)          #no error,with space
print (full_name)