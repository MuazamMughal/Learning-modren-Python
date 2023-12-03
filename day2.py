name :str = "muazam mughal"
print(name)

id:str ="12y31"

age : int = 31
# now understanding the quates in the strig
message :str ="Piaic student's id is that"
print(message)

# concatination
card : str = name + message +" "+ id
print(card)
#in concatination both f the items is must be in same type otherwise 
#coved in a string using the str()

print (card + "  age :"+ str(age))

# using \ back slash meanss line is continue but line changed

print(1 + 3\
          +5 \
      +9)

#using define multiline string ""","""
details : str = """ 
studdent card
student name
father name
class 
etc

"""
print(details)

#F-string
# very power full using as an multiline concatinaging
#  considering the all the stuf as string
# including the exprision
cridentionals : str =f""" 
studdent card {id}
student name {name}
father name : ...
class : 15
etc : age = {age}
sum {1+1+1+2}
"""
print(cridentionals)


#f-string ans ninja style
#fstring  =     f"""student{name}"""
# jinja style =   """student{{name}}"""



#methods for string & some attribute
#.removeprefix("jo bi remov karna ha")
# .formate()


