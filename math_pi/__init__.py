version = "0.0.1"
name = "math_pi"

def pi(a = 1, b = 1000000):
    if b > 1000000:
        raise Exception("b cannot be more than 1000000")
    full = open("pi_1m.txt").read()
    full = full[2:]
    b = int(b)
    if a != 1:
        return full[a - 1:b]
    return "3." + full[a - 1:b]
    


    
