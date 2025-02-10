from scipy.optimize import root
def equation(x):
    return x**2-4
sol=root(equation,x0=1)
print(f"Root : {sol.x}")
