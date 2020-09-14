from sympy import series, Symbol
from sympy.functions import sin, cos, exp
from sympy.plotting import plot
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import root

plt.rcParams['figure.figsize'] = 13,10
plt.rcParams['lines.linewidth'] = 2


# Define symbol
x = Symbol('x')

def taylor(function, x0, n):
    """
    Parameter "function" is our function which we want to approximate
    "x0" is the point where to approximate
    "n" is the order of approximation
    """
    return function.series(x,x0,n).removeO()


f = lambda x: x**3 - 2*x**2 + (4*x)/3  - 8/27
taylorParam = [x**3 - 2*x**2 + (4*x)/3  -8/27, 0.6, 4 ]
a= 0.5
b= 1
print('a:', a, ' b:', b)
brent = optimize.brentq(f, a, b, xtol=2**-16, full_output=True, disp=True)
print('Brent')
print(brent[1])
##print('taylor', taylor(taylorParam[0], taylorParam[1], taylorParam[2]))
fp = lambda x: 0.0133333333333332*x + (x - 0.6)**3 - 0.2*(x - 0.6)**2 - 0.00829629629629627
taylor = optimize.brentq(fp, 0.5, 1, xtol=2**-90, full_output=False, disp=True)
print('Taylor ', taylor)
print('error: ', abs(brent[0] - taylor))

# This will plot sine and its Taylor approximations

####p = plot(x**3 - 2*x**2 + (4*x)/3  -8/27,taylor(x**3 - 2*x**2 + (4*x)/3  -8/27,0,1),taylor(x**3 - 2*x**2 + (4*x)/3  -8/27,0,2),taylor(x**3 - 2*x**2 + (4*x)/3  -8/27,0,3),
####         (x,-2.5,2.5),legend=True, show=False)
##p = plot(taylor(taylorParam[0], taylorParam[1], taylorParam[2]),
##         (x,-2,2),legend=True, show=False)
######p[0].line_color = 'blue'
####p[1].line_color = 'green'
##p[0].line_color = 'firebrick'
####p[3].line_color = 'black'
##p.title = 'Taylor Series Expansion'
##p.show()
