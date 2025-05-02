#Day 10 Calculator App 



def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    should_continue = True
    first_num = int(input("Enter the number : "))
        
    
            
    while should_continue :
        for operators in operations:
            print(operators)

        operator = input("Select Operator : ")
        second_num = int(input("Enter the number : "))
        
        calculator_function = operations[operator]

        calculation_answer = calculator_function(n1=first_num,n2=second_num)
        
        print(f"{first_num} {operator} {second_num} = {calculation_answer} \n")
        
        more_operations= input(f"Would you like to continue operations on {calculation_answer} ? (Y/N) : ")
        
        if more_operations == "y":
            first_num = calculation_answer
        else:
            should_continue=False
            calculator()
            
        
calculator()
        
    

