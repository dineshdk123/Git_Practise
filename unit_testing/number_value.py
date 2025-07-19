class check_no():
    def __init__(self):
        pass

    def even_no(self,a):
        return a%2==0

    def odd_no(self,a):
        return a%2!=0
    
    def add(self, a, b):
        return a + b 
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# value=check_no()
# print(value.add(2,5))

    