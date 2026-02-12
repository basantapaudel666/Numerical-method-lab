#Newton-Raphson Method in python
def f(sinx, x):
    #Define the fuction
    #Example: f(x)= x...............
    return sinx - x
def df(x):
    return 3*x**2-1
def newton_rapson(x0, tolerance, max_iterations):
    print("Iteration\t x\t\t f(x)")

    for i in range (1, max_iterations + 1):
        fx= f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Derivative is zero. MEthod fails")
            return None
        x1= x0 - (fx/dfx)
        print(f"{i}\t\t {x1:.6f}\t {f(x1):.6f}")
        if abs (f(x1))<tolerance:
            print("\nRoot found",x1)
            return x1
        x0 = x1
    print("\nApproximate root after maximum iteration:", x1)
    return x1
#input values
x0= float(input("Enter initial guess:"))
tolerance = float(input("Enter tolerance:"))
max_iterations= int(input("Enter maximum iterations:"))
#call the function
newton_rapson(x0, tolerance, max_iterations)    