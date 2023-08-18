# Tuples - ()
# Properties - ordered, allows duplication, immutable(unchangeable)
# Data from database to/from an application are enclosed on a tuple

counties= ('Nairobi', 'Baringo', 'Siaya', 'Nairobi')
print(type(counties))

# Create a tuple of one item
# Print the type

showergel=('Olay',)
print(type(showergel))

newshowergel= tuple('Dove')
print(type(newshowergel))

print(counties[0])

# Methods
counties.index('Nairobi')
newcounties=list(counties)
newcounties.append('Muranga')
counties=tuple(newcounties)
print(counties)