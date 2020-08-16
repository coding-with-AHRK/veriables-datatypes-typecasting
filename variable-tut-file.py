'''
in this file we are going to discuss everything about variables
today's agenda is
string ,float,int,
type() function
int(),str(),float() function
role of plus when you are going to add 2 strings or 2 variables
role of *
'''
var1 = 12 #int datatype
var2 = 33.3 #float datatype
var3 = "2" #string datatype
var4 = "32" #string datatype
print(var1,var2,var3,var4,end='\n') #print veriable var1,var2,var3,var4

print(type(var1),type(var2),type(var3),type(var4)) #print type of var1,var2,var3,var4

print(var1 + var2) #print addtion of 2 veriables and if type is int thn result could be addition of two

#veriables and if var1,var2 are string veriables thn result could be concatenation of two veriables

print(10 *(var1 + var2))  #first add 2 int variables thn multiply by 10 and print it

print(10 * str(var1 + var2) ) #first add two int variables thn convert it into string and then multiply it
#answer should b it shows 10 times answer of addition of two veriables

print(var3 + var4) #print two  string veriable

print(10 * str(int(var3) + int(var4))) #first convert string integar value into int value
#thn add it now convert the addition of two variable into string and thn multiply it by 10 times 


