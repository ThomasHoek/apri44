import math

class afq():
    def __init__(self, firstinput , secondinput):
        '''The init is used in the start defining of the class, when defining you can give inputs with it.
        The self defines which inputs are used. And to what they are binded.
        
        In a function this would be:

        def afq(firstinput, secondinput):
        '''

        self.firstvariable= firstinput
        self.secondvariable = secondinput

    def returnfirst(self):
        '''If this function is called it returns self.firstvariable, aka the first input number'''
        return self.firstvariable
    
    def returnsecond(self):
        '''If this function is called it returns the second input number'''
        return self.secondvariable


    def add(self):
        '''Takes the class's first variable and second and adds them.'''
        return (self.firstvariable + self.secondvariable)

    def add_user(self, a, b):
        '''Takes the inputs variables adds them.'''
        return (a + b)

    def add_class_and_user(self,a):
        ''' Function which shows that you can combine user and class inputs'''
        return (self.firstvariable + a)


    def add_new_var(self,a):
        '''Using a class function inside another class function. The result of it is made a new var called c.'''
        self.c = self.add_class_and_user(a)

    d = 5      # this way we make a new variable in the class that is a constant.

    def change_var(self):
        self.d = 10

    
    def user_change_var(self,d):
        ''''''
        self.d = d
        
    def Pythagoras(self):
        '''Inside out classes we can create longer functions, Which can solve complicated tasks.'''
        a_squared = (self.firstvariable ** 2) 
        # a_squared is a variable that only exists inside this function. It can not be used in another function. 
        # Unless we add self.a_squared. Then any function in the class can use this.

        b_squared = (self.secondvariable ** 2) 
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        print("First we square a, a is:", self.firstvariable, "Then we get:", a_squared)
        print("Then we square b, b is:", self.secondvariable, "Then we get:", b_squared)
        print("To get c we add the squares of a and b", a_squared , "+" ,b_squared ,"=" , c_squared)
        print("Then we take the square root of c squared to get:", c)
        
        
    # def Pythagoras2(self):
    #     try:
    #         print(a_squared)
    #     except Exception as e:
    #         print(e)

firstclass = afq(5,10)  # I make a new class with inputs: 5 and 10 and call it firstclass
secondclass = afq(10,15)  # I now make a second class with the inputs 10 and 15.



# ----------------- TESTING -----------------
'''
    print(firstclass.returnfirst())          # first class, first returns 5
    print(firstclass.returnsecond())         # first class, second returns 10
    print(secondclass.returnfirst())         # second class, first returns 10
    print(secondclass.returnsecond())        # second class, second returns 10

    print(firstclass.add())                     # returns 15 -> 5 + 10
    print(secondclass.add())                    # returns 25 -> 10 + 15

    print(firstclass.add_user(5,25))            # returns 30
    print(secondclass.add_user(40,25))          # returns 65
    print(firstclass.add_class_and_user(5))     # returns 10 -> 5 from the class itself and 5 from input.


    # print(firstclass.c)                         # calls an error because the var isnt defined yet.
    print(firstclass.add_new_var(5))            # returns a none because there is no return in the function
    print(firstclass.c)                         # returns the new made variable.


    print(firstclass.d)                 # variable d is 5
    firstclass.change_var()             # function is called and changes variable to 10
    print(firstclass.d)                 # variable d is now 10.
    firstclass.user_change_var(15)      # function is called and user changes variable to 15
    print(firstclass.d)                 # variable d is now 15.


    firstclass.Pythagoras()         # showing a more difficult class with variables in it that dont exist in the other functions
    firstclass.Pythagoras2()        # gives us an error a_squared is not defined.
'''

