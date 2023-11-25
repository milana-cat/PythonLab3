import math
import numpy as np

def LinearList(input:[float]):
    #result = np.array([0],dtype=float)
    a=input[0]
    b=input[1]
    step=input[2]
    parameterM=input[3]
    result = []

    for x in np.arange(a,b+step,step):
        #np.append(result,LinearFunction([parameterM,x,parameterM])[0])
        result.append(LinearFunction([parameterM,x]))

    return result



def LinearFunction(parameters:[float]):
    m = parameters[0]
    x = parameters[1]
    k= x**3+m*math.sin(x)
    return k #тут функция
    