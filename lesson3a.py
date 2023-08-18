# Collections(Arrays) - group of data on the same variable

# We have:
# 1. Lists - []
# 2. Tuple - ()
# 3. Dictionary - {}
# 4. Sets - {}

student1='Sally'
student2='Bob'
student3='Jane'

students=('Sally', 'Bob', 'Jane')

# 1. Lists - ordered collection of items using the square brackets []. Each is comma separated
# Properties - ordered, mutable(changeable), allows duplication of data
counties=['Nairobi','Mombasa', 'Kisumu', 'Nyeri', 'Kitale', 'Kajiado']
student=['Sally', '21', 'True', '3.5']
print(type(counties))
print(type(student))

# List Operations
# 1. Printing elements of a list - print()

# 2. Accessing items on a list - indexing(each item should be given numeric values starting from 0)
print(counties[2])
print(counties[4])

# 3. Range of values
# When working with a range the first index(number 1)is included but the last index is excluded
print(counties[1:])
print(counties[:3])
print(counties[1:3])
#Accessing all items in the list
print(counties[0:6])
print(counties[:])

# 4. List Methods
# Add a new item on the list - append()
counties.append('Turkana')
print(counties)
newcounties=['Kilifi', 'Nyandarua', 'Lamu']
counties.extend(newcounties)
print(counties)
# a)Insert - (0,'')
counties.insert(1,'Marsabit')
print(counties)
# b) Removing an item from a list - pop()
counties.pop()
print(len(counties))

counties[2:2]=['Uasin Gishu','Makueni']
print(counties)

counties.remove('Kilifi')
print(counties)

counties.clear()
print(counties)
print(counties.count('Kajiado'))

