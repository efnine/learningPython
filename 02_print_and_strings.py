print("hello","there")

print("hello","there",5,"jojo" + "wow")

print("hello" + " " +str(5))
print("hello 5")
print("hello",5)
print("hello",int("3")+2)
print("hello", 3+2)

"""this is a multi line 
comment"""

variable_str_1 = "Hello"
variable_str_2 = "World!"
print ('%s, %s' % (variable_str_1,variable_str_2))
print(variable_str_1 + ",",variable_str_2)

print ('\n')
from datetime import datetime
now = datetime.now()
print ('%s-%s-%s' % (now.year, now.month, now.day))
print ('%s/%s/%s' % (now.month, now.day, now.year))
