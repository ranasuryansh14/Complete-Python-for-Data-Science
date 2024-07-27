def addition(p,b):
    return p+b

def vote(a):
    if a>=18:
        return "You can vote"
    elif a>0 and a<18:
        return "You can't vote"
    else:
        return "Invalid Age"