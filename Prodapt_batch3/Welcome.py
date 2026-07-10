print("Welcome to python VS Code")
x=1
print(x+1)
print(eval("x+1"))

a=5
b=5
print(a==b) #2 variables are equal 
print(a is b) #two variables are same object in memory
print(id(a))
print(id(b))

#eval example

expression= "10 * 20"
print(expression)
print(eval(expression))
expression = input("Enter an expression to evaluate:") #15*7
#"15 *7"
result = eval(expression)
print("Answer:",result)


