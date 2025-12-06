#Ex2 - Page 33 - AIVN
#Input: x, sigmoid, relu, elu
#Output: f(x)
import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1/(1+math.exp(-x))

def relu(x):
    return x if x>0 else 0.0

def elu(x):
    alpha = 0.01
    return x if x>0 else alpha*(math.exp(x)-1)

def activation(x,activation_name):
    if not is_number(x):
        print("x must be a number")
        return 
    if activation_name not in ["sigmoid","relu","elu"]:
        print(f"{activation_name} is not supportted")
        return
    x = float(x)

    if activation_name == "sigmoid":
        y = sigmoid(x)
    elif activation_name == "relu":
        y = relu(x)
    else: 
        y = elu(x)
    print(f"f({x}) = {y}")

def main():
    activation(1.5,"sigmoid")
    activation("abc","sigmoid")
    activation(1.5,"belu")

if __name__ == "__main__":
    main()