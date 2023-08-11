courses = ['maths', 'physics', 'chemistry', 'eng']

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[2])

print(courses[0:2])

print(courses[2:])

courses.append('art') #.append helps us to add anything in the list
print(courses)

courses.insert(1, 'art') #.insert helps us to insert the value in the mid of the list 
print(courses)

courses_2 =['art' , 'education']
courses.extend(courses_2) # extend help us to add the individual whereas the append add the whole list with bracket also 
print(courses)

courses.remove('maths') #remove help us to remove anything from the list 
print(courses)

courses.pop() #.pop help us to remove the last element from the list 
print(courses)

# how to sort the list 

courses.reverse() # reverse is help to reverse the whole list 
print(courses)
 
courses.sort() # sort help us to sort the list in alphabetical order after sorting we can use the reverse methid to make it in descending order
print(courses)

# or we can use sorted directly to sort the course

sorted_courses = sorted(courses)
print(courses)

nums = [1, 2, 6, 8]
print(min(nums))
print(max(nums))
print(sum(nums))

courses = ['maths', 'eng', 'himdi']

for m in courses:  # this is used to help to write in vertical 
    print(m)

list_1 = ['shag', 'riya', 'pri', 'aru']
list_2 = list_1

list_1[0] = 'shagun'
print(list_1)
print(list_2)

#tuple_1 = ('shag', 'riya', 'pri', 'aru')
#tuple_2 = tuple_1 # tuple doesnt not support item assignement becuase it is immutable

#tuple_1[0] = 'shagun'
#print(tuple_1)
#print(tuple_2)
#tuple cant be delete

# sets start with {}
#
cs_courses = {'maths', 'phy', 'maths'}
print(cs_courses)










