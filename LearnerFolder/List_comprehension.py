'''pythonSimplified
List Comprehension 
chat:  https://chatgpt.com/c/68594067-58fc-800f-84a5-ba31d9847493
   /Documents/Shared_Folders/PyQt5/LearnerFolder/List_comprehension.py
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
