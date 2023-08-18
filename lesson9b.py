# Calling functions from the module(lesson 9a file)

# Keywords;

# 1. Import - used to call all the functions from a module
# Syntax - eg  import lesson9a

# import lesson9a
# Calling the functions
# Syntax - eg filename.function()
# lesson9a.add(3,6)
# lesson9a.subtract(15,5)
# lesson9a.multiply(7,8)
# lesson9a.divide(100,20)

# 2. From - calling specific functions from a module
# * is put after import to include all the functions in your execution
# Syntax - eg from filename import function
from lesson9a import subtract, add
subtract(9,7)
add(10,8)

# Types of Modules
# 1. User defined modules - created by the developer

# 2. In built modules - already existing modules 
import math 
answer = math.sqrt(121)
print(answer)

# For shuffling cards
import random
numbers = [3,5,7,9]
result = random.shuffle(numbers)
print(result)

# 3. Modules from the Internet
import pygame
# Syntax - pip3 install module

# Research on popular Python modules for;
# 1. Web Applications
# 2. Machine Learning/Artificial Intelligence/Deep Learning
# 3. Data Analysis
# 4. Cyber Security
# 5. Gaming
# 6. Graphics
# 7. Sounds(Speech Recognition)