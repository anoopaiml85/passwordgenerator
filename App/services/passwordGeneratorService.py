import string
import random

class Passwordgenerator():
    def __init__(self,length,pattern):
        self.length = length
        self.pattern =pattern # sample : [1,2,3,4]
        self.pattern_lookup = {
            1:string.ascii_uppercase,
            2:string.ascii_lowercase,
            3:string.digits,
            4:string.punctuation
        } 

    # lower_case_letters= string.ascii_lowercase
    # upper_case_letters= string.ascii_uppercase
    # numbers= string.digits
    # special_characters=string.punctuation
    def generate_password(self):
        try:
            print(len(self.pattern))
            num_chars=self.length//len(self.pattern)
            print(num_chars)
            num_spl=0
            if(self.length%len(self.pattern)!= 0):
                num_spl=self.length%len(self.pattern)
                print(num_spl)
            passwd = []
            
            for idx,i in enumerate(self.pattern):
                _num_chars=num_chars
                print (idx,i)
                if num_spl and idx ==0:
                    _num_chars= num_chars+num_spl
                print(self.pattern_lookup[i])            
                passwd +=  random.choices(self.pattern_lookup[i],k=_num_chars) 
            random.shuffle(passwd) 
            #print(passwd)
            passwd=''.join(passwd)         
            return passwd  
        except KeyError:
            return KeyError     

# length = int(input('Provide the length of the password: '))
# password_pattern = input('Password pattern \n * Do not repeat the characters \n * 1:Upper_case,2:lower_case,3:numbers,4:special characters;\n * Example:2 3 4 :')
# password_pattern=list(set([int(i) for i in password_pattern.split()]))
# #username,login url ,Appname
# if len(password_pattern)>2:

#     pg=  Passwordgenerator(length,password_pattern) 
#     print(pg.generate_password())
# else:
#     print('Provide atleast 2 pattern choices')

 