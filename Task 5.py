#Pat 5 ques1 expected output of the pythoncode 
data =[10,501,22,37,100,999,87,351]
#lamdba expression check for value which is greater than 4 and in given input list all values are greater than 4
result=filter(lambda x:x>4,data) 
print(list(result))


#Pat 5 ques 2 write a python code using Lambda function to check every element of alist is an integer or string?
#take a list which is having int and string value
List =[20,30,"Priyanka",45]
# here in lambda function we are checking for int values
Intger=list(map(lambda List:int if isinstance(List,int) else str ,List)) 
print(Intger)


#Pat 5 ques 3 Fibonacee series from 1 to 50 using Lambda function
#creating fibonacci function
def fibonacci(count):
  #declaring list
	fib_list = [1, 2]
 
	                                                                        
	any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count))) 
	                                                                        
	                                                                         
#returning list of elemnts from starting to end count-1
	return fib_list[:count] 
#print and calling of fibonacci function
print(fibonacci(50)) 

#Pat5 ques4 A) email address
import re
# created function to validate email address
def validate_emailaddress(emailaddress): 
   pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' 
   #condiiton to validate email address with pattern of email address
   if re.fullmatch(pattern,emailaddress): 
    return("yes")
   else :
    return("no")
emailaddress1="priyanka.kapoor@hmail.com"
#calling of function inside print statement
print("valid password",validate_emailaddress(emailaddress1)) 
emailaddress2="1234@gmail.com"
print("valid password",validate_emailaddress(emailaddress2))
emailaddress3="priya%gmail.com"
print("valid password",validate_emailaddress(emailaddress3))

#B)mobile no of bangladesh 880 1xxx NNNNNN  this is tha pattern(13 digit number)
#to use regular expression class
import re  
#create function to  validate bangaldesh number
def validate_bangladeshno(number):
  #regular expresssion of banagladesh
  pattern =r'^(\+880)+([\s.-]?1[0-9]{3})+([\s.-]?[0-9]{6})$'
  if re.fullmatch(pattern,number):
    return True
  else:
     return False


banglanumber1="+880.1234.567453"
#call of function through print statements
print("valid bangaldesh number:",validate_bangladeshno(banglanumber1))
banglanumber2="111234567453"
print("valid bangaldesh number:",validate_bangladeshno(banglanumber2))
banglanumber3="+8801234567453"
print("valid bangaldesh number:",validate_bangladeshno(banglanumber3))


#C)mobike no of US starts with +1 and total of 10 digit
import re
#create validate US number function
def validate_Usnumber(number):
  #regular expression of US number
  pattern =r'^(\+1)+([\s.-]?[0-9]{3})+([\s.-]?[0-9]{3})+([\s.-]?[0-9]{4})$'
  if re.match(pattern,number):
    return True
  else:
     return False


number1="+1-234-768-6871"
#call of function inside print statement
print("valid US number:",validate_Usnumber(number1))
number2="+11123456745"
print("valid US number:",validate_Usnumber(number2))
number3="1880 1234 567453"
print("valid  US number:",validate_Usnumber(number3))



#d)check correct format of password-16 alphanumericchars uparcase, lowercase, special chars, numbers
import re
#create function to validate password
def validate_Password(password):
   #regular expression of password 
   pattern=r'\b[A-Za-z0-9@$!%*#?&]{16}$'
   #condiiton to validate password with pattern of password
   match=re.fullmatch(pattern,password) 
   if match:
    return("yes")
   else :
    return("no")

password1="Yh54@#bn89&*%er5"
print("valid password",validate_Password(password1))#call of function inside print statement
password2="AAAAAAZZYYHH1&RG"
print("valid password",validate_Password(password2))
password3="$2#$@#%%$&^RFVG1"
print("valid password",validate_Password(password3))


