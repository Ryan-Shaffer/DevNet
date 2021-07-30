'''
Input1 = (int(input('Enter the first #')))
#print (inpt,"is our planet",1,"\b:")
Input2 = (int(input("Enter the second #")))
#print (inpt2)
Sum = 0
def Addition(Num1, Num2):
    Sum = Num1 + Num2
    return Sum
    #print(Sum)
Value = Addition(Input1,Input2)
print(Addition)
'''




class Family:
    '''Describes units of family'''
    def __init__(self, role, sex, age):
        '''Init Values'''
        self.role = role
        self.sex = sex
        self.age = age
    

    def rolecall(self):
        '''Returns information about a family member'''
        role = self.role,self.sex,self.age
        return role

kelsey = Family('Wife','Female',"31")
willy = Family('Pet','Male','4')
ruby = Family('Baby','Female','10 Weeks')

print(kelsey,'is my ',kelsey.rolecall())
print('willy', 'is my', willy.rolecall())


