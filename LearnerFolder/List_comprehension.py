from collections import defaultdict

'''pythonSimplified
List Comprehension 
chat:  https://chatgpt.com/c/68594067-58fc-800f-84a5-ba31d9847493
   /Documents/Shared_Folders/PyQt5/LearnerFolder/List_comprehension.py
   list comprehension https://www.youtube.com/watch?v=Bw_4gcB6kg8  ryan and matt data sciences
   dictionary comprehension. https://www.youtube.com/watch?v=wxd-rQkmq4Y. ryan and matt data sciences
   
merging lists of directories -future study https://www.reddit.com/r/learnpython/comments/15mufyp/merge_two_lists_each_list_contains_dictionaries/   
'''

fruits =['apples','bananas', 'strawberries']

new_fruits= []

# for fruit in fruits:
#     fruit=fruit.capitalize()
#     new_fruits.append(fruit)
# print(new_fruits)

Fruits =[fruit.upper() for fruit in fruits]
print(fruits)
print(Fruits)
## next work with boolean values
bits = [0,1,1,1,0,0,0,1,1,1]
# new_bits =[]
# for bit in bits:
#     if bit == True:
#         new_bits.append(True)
#     else:
#         new_bits.append(False)
# print(new_bits)
        
myNewBits=[True if bit == 1 else False for bit in bits]
print(myNewBits)
myCount=[bit+1 for bit in bits]
print(myCount)


### from Chat  exploring dictionary comprehensions and the use of a conditional expression (a ternary expression) inside them
my_dict = {'Spider': 'photographer', 'Bat': 'philantropist', 'Wonder Wo': 'nurse'}

my_dict = {
    (key + 'man' if key != 'Spider' else 'Superman'): val
    for (key, val) in my_dict.items()
}
my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
# my_dict={key+'man':val for (key,val) in my_dict.items()}
# print(my_dict)
## replace Spider with Superman !note the key!='Spider' refers to the new dicitionary
## the logic: Since you're doing the normal name + 'man' for everyone except Spider, the best logic is:

# "If the guest is not Spider, give them a name tag that adds 'man'"
# "Else, for Spider, write 'Superman' instead"
## the if goes with the first part so if A is not B then do C
## do A if condition is not B else C
## if the key is NOT spider Do This 
my_dict={(key +'man' if key != 'Spider' else 'Superman'):val for (key,val)in my_dict.items()}
print(my_dict)
## do this but if the key is not spider do else
my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
my_dict={(key +'man' if key != 'Spider' else 'Superman'):val for (key,val)in my_dict.items()}
print(my_dict)

my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
my_dict={(key +'man' if key != 'Spider' else 'Superman'):val if val != 'photographer' else 'philanthropist' for (key,val) in my_dict.items()}
print(my_dict)

my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
###convert to a list of strings['Superman is a journalist', 'Batman is a philantropist', ...]
myList=[ (key +'man' if key != 'Spider'else 'Superman') +' is a ' + (val if val != 'photographer' else 'philanthropist' ) for (key,val) in my_dict.items() ]
print(myList)


my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
## switch 'spider and superman and ocupations and then swap key and values
my_dict ={val:key for (key,val) in my_dict.items()} #step 1 
my_dict={val if val != 'photographer'else 'journalist':key +'man' if key != 'Spider' else 'Superman' for (key,val)in my_dict.items()} #step 2

print(my_dict)

my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
# Challenge#2 I did two challenges. 
# change {'Superman': 'journalist', 'Batman': 'philantropist', 'Wonder Woman': 'nurse'}
# to {'journalist': 'Superman', 'philantropist': 'Batman', 'nurse': 'Wonder Woman'}
# Hint: Swap key and value, but do it after transforming 'Spider' → 'Superman', etc.
#challenge 2A
myDict1={'Superman': 'journalist', 'Batman': 'philantropist', 'Wonder Woman': 'nurse'}
myDict2={key :val  for (val,key) in myDict1.items()}
print(myDict2) # output:   {'journalist': 'Superman', 'philantropist': 'Batman', 'nurse': 'Wonder Woman'}
print('Challenge 2:')
#challenge 2B
## below was tricky in that I had to append '+man' to val since apparantly the key  became the val earlier in the processing       
my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
myList={((key) if key!='photographer' else 'journalist'):(val+'man' if val != 'Spider' else 'Superman') for (val,key) in my_dict.items()}
print(myList) # output: {'photographer': 'Spiderman', 'philantropist': 'Batman', 'nurse': 'Wonder Woman'}





my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}

# my_dict={(key+'man' if key!='Spider' else 'Superman'):
#           (val if key!='Spider'else 'journalist') 
#           for(key,val)  in my_dict.items()  }
# print(my_dict)


#  🔥 Want a Challenge #3?
# Create a set of strings that say which superhero is NOT a "journalist", like:       
# {"Batman is not a journalist", "Wonder Woman is not a journalist"}
# Only exclude the one where the value is 'journalist'.
# 💡 Explanation:
# We're using a set comprehension
# We filter out any entry where v == 'journalist'
# For the rest, we format the string as needed
my_dict={'Superman': 'journalist', 'Batman': 'philantropist', 'Wonder Woman': 'nurse'}
myStrings ={ key +' is not a journalist'   for (key,val)in my_dict.items()if val !='journalist'}
print('')
print(myStrings)

print('Challenge 4')
my_dict={'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
# goal: ['Spider fights crime as a photographer', 'Bat fights crime as a philantropist', ...]
# myList=[ key +'man' +' fights crime as a '+val+'.' for (key,val) in my_dict.items()]
myList=[f'{key}man fights crime as a {val}. 'for (key,val)in my_dict.items()]
print(myList)
print('''Challenge #5 — maybe one with sorting, filtering, or combining two dictionaries
      this one mixes dictionary merging, filtering, and list comprehension
      ''')
jobs = {'Spider': 'photographer', 'Bat': 'philantropist', 'Wonder Wo': 'nurse'}
cities = {'Spider': 'New York', 'Bat': 'Gotham', 'Wonder Wo': 'Themyscira'}
['Spiderman protects New York as a photographer', 
 'Batman protects Gotham as a philantropist', 
 'Wonder Woman protects Themyscira as a nurse']
# 🧠 Requirements:
# Merge data from both dictionaries
# Use a list comprehension
# Apply conditionals as needed
# Final list should have 3 strings in the form:
# Name protects City as a Job

#merge dictionaries
dict_1 = {'Spider': 'photographer', 'Bat': 'philantropist', 'Wonder Wo': 'nurse'}
dict_2 = {'Spider': 'New York', 'Bat': 'Gotham', 'Wonder Wo': 'Themyscira'}
print(dict_1['Spider'])
# Merge the dictionaries into a new one with tuples: {key: (city, job)}
dict_3 = {
    key: (dict_2[key], dict_1[key])
    for (key)in dict_1 if key in dict_2
}

print(dict_3)







# myStrings={(k  if v == 'journalist'  else k+' is not a journalist' )for (k,v)in myDict1.items()}
# print(myStrings) #  output: {'Superman', 'Batman is not a journalist', 'Wonder Woman is not a journalist'}
# ## i was not able to preserve 'Superman is a journalist'
# myStrings2={(k if k != 'Superman' else k+ ' is not a journalist') for (k,v) in myDict.items()}       
# print(myStrings2) #output. {1,3} I do not understand this output

## Ryan and Matt Data Science. 'learn Python dictionary comprehension fast:  '
### Syntax    dictionary ={key:expression for key,value in iterabel}
# add 15 to each value in dict

concerts ={
    'Trivium':100,
    'Nine Inch Nails': 90,
    'Queens of the Stone Age':110
}
## add 15
# new_concerts ={key:value+15 for (key,value) in concerts.items()if key !='Trivium'}
# print(new_concerts)
# new_concerts ={key if key != 'Trivium' else 'AC-DC': value +15 for (key,value) in concerts.items()}
# print(new_concerts)

## if statement based on how loud the concert is
loud_concert ={key:value for (key,value) in concerts.items() if value >=100}
print(loud_concert)
## create dict from a list
songs=['innagadavidda','Eli\'s Comming','Mony Mony','Grazin in the Grass']
song_length=[12,5,3,2]

song_len={key:len(key) for key in songs}
print(song_len)
## TO ZIP TW LISTS TOGETHER IN A NEW DICT
song_dict= dict(zip(songs,song_length))

print(song_dict)





fruits =['apples','bananas', 'strawberries','Kiwi','apricots']
bits = [0,1,1,1,0,0,0,1,1,1]
new_fruits=dict(zip(fruits,bits))
print(new_fruits)
my_fruits ={'apples': ['red','big'], 'bananas': 'yellow', 'strawberries': 'red', 'Kiwi': 'lime', 'apricots': 'orange'}
concerts ={
    'Trivium':100,
    'Nine Inch Nails': 90,
    'Queens of the Stone Age':110
}
## merging dictionaries 
# myDict3={key:(my_fruits[key],new_fruits[key]) for (key) in new_fruits if key in my_fruits}
# myDict3={key:(my_fruits[key],new_fruits[key]) for (key) in my_fruits if key in new_fruits}
myDict3={key:(my_fruits[key],new_fruits[key]) for (key) in my_fruits.keys()if key in new_fruits.keys()}
print(myDict3) ## this does not combince 


# dict_3 = {
#     key: (dict_2[key], dict_1[key])
#     for (key)in dict_1 if key in dict_2
# }

# print(dict_3)


# https://favtutor.com/blogs/merge-dictionaries-python
dict1 = {"a": 1, "b": [4,3]}
dict2 = {"c": 3, "d": 4, 'b': 12}

# Combine values for duplicate keys into a list THIS IS AWESOME, uses the defaultdict(list)
# /Shared_Folders/PyQt5/LearnerFolder/List_comprehension.py
dict1 = {"a": 1, "b": [4,3]}
dict2 = {"c": 3, "d": 4, 'b': 12}
dict3 = defaultdict(list)
for d in (dict1, dict2):
    for k, v in d.items():
        dict3[k].append(v)
print(dict(dict3))

merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        # If the value is not already a list, make it a list
        if not isinstance(merged_dict[key], list):
            merged_dict[key] = [merged_dict[key]]
        # If the new value is a list, extend; else, append
        if isinstance(value, list):
            merged_dict[key].extend(value)
        else:
            merged_dict[key].append(value)
    else:
        # If value is a list, assign as is; else, wrap in a list
        merged_dict[key] = value if isinstance(value, list) else value ## i controlled this by not using [value] which would have made singel values into lists of one element
print(merged_dict)  # output: {'a': [1], 'b': [4, 3, 12], 'c': [3], 'd': [4]}

dict_1={'John': 15, 'Rick': 10, 'Misa': 12}
dict_2={'Bonnie': 18, 'Rick': 20, 'Matt': 16}
dict_3={k:v for d in (dict_1,dict_2) for k,v in d.items()}
print (dict_3)




# https://www.google.com/search?client=safari&rls=en&q=explain+syntax+of++++++++if+not+isinstance(merged_dict%5Bkey%5D%2C+list)%3A+++++++++++++merged_dict%5Bkey%5D+%3D+%5Bmerged_dict%5Bkey%5D%5D&ie=UTF-8&oe=UTF-8

merged_dict = {'a': 1, 'b': [2, 3]}
print(merged_dict['a'])
print(type(merged_dict['a']))
# Check if the value for key 'a' is a list
if not isinstance(merged_dict['a'], list):
    # If not a list, make it a list
    merged_dict['a'] = [merged_dict['a']]

print(merged_dict)
# Output: {'a': [1], 'b': [2, 3]}
print(merged_dict['a'])
print(type(merged_dict['a']))


# AI explained :         # If the value is not already a list, make it a list
#         if not isinstance(merged_dict[key], list):
#             merged_dict[key] = [merged_dict[key]]
            
# The syntax if not isinstance(merged_dict[key], list): merged_dict[key] = [merged_dict[key]] in Python is used to ensure that the value associated with a specific key in a dictionary is always a list. 
# Here's a breakdown:
# if not isinstance(...): This part checks if a condition is false.
# isinstance(merged_dict[key], list): This checks if the value associated with the key in the merged_dict is an instance of the list data type. The isinstance() function takes two arguments: the object to check and the class or type to check against.
# merged_dict[key] = [merged_dict[key]]: If the isinstance check returns False (meaning the value is not already a list), this part of the code converts the existing value into a single-element list containing that value. 
# In essence, the code ensures that if merged_dict[key] is not a list, it becomes a list containing the original value. 
# Example:
# python
# merged_dict = {'a': 1, 'b': [2, 3]}

# # Check if the value for key 'a' is a list
# if not isinstance(merged_dict['a'], list):
#     # If not a list, make it a list
#     merged_dict['a'] = [merged_dict['a']]

# print(merged_dict)
# # Output: {'a': [1], 'b': [2, 3]}
# In this example, the value associated with 'a' was initially 1 (an integer), not a list. The if statement evaluated to True because isinstance(1, list) is False. The Python documentation says that if the condition is true, the code block following the if statement is executed. Thus, the value for 'a' was converted to [1]. The value for 'b' was already a list, so that part of the code was skipped




## LIST COMPREHENSIONS Ryan and Matt Data Sciences
#Obsidian 2024/List Comprehension
teams = ['Rays', 'Yankees', 'Red Sox', 'Blue Jays', 'Orioles']
upper_case_teams=[x.upper() for x in teams] 
print(upper_case_teams)
team_length=[len(x) for x in teams]
print(team_length)
# Example 7
bands = ['Metallica', 'NIN', 'A Perfect Circle', 'Northlane']
## substitute Nine in Nails for NIN
new_bands=[band if band != 'NIN' else 'Nine in Nails' for band in bands]
print(new_bands)
#Example 9 search fo char
# myString ='"We're off to never-never land"'
myVowels =[(char.count('e'),char)  for char in "We're off to never-never land" if char in 'aeiou' ]
print(myVowels)
myVowels =[char  for char in "We're off to never-never land" if char in 'aeiou' ]
print(myVowels)
# Example 10 using multiple if conditions
numbers = [2, 5, 8, 9, 12, 15, 18, 20, 24]
myNum= [num  for num in numbers if num <=10 if num/3==3 ]
print(myNum)
#Example 11 Range 
numbers_squared =[num **2 for num  in range(10)]
print(numbers_squared)
# Example 12 - Function with list comprehension
number_list = [10, 20, 30]
# Let’s create a function plusfive which adds 5 to a number
def plus_five(num):
    return num+5
number_plus_5_v2 = [plus_five(x) for x in number_list] 
print(number_plus_5_v2)

num= plus_five(5)
print(num)
#Example Nested list comprehension
matrix = [[j for j in range(3)] for i in range(5)] 
print(matrix)
## note difference,  need the list square brackets in order to establish the col and then make 5  rows

matrix =[col for col in range(3) for row in range(5) ]
print(matrix)