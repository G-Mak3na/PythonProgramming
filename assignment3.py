# Multi-Dimension List(Nested List)

customer=['Joseph','Nakuru',['jose@gmail.com','0712764453'],['Vegetables','Flowers','Fruits']]

# Access Joseph's Phone Number
phonenumber=customer[2][1]
print(phonenumber)
# Access his order ie Vegetables and Flowers only
order=customer[3][0:2]
print(order)