def square_root(n):
    root=n**0.5
    if int(root)**2==n:
        return True
    else:
        return False
    
n=int(input())
print(square_root(n))   
    