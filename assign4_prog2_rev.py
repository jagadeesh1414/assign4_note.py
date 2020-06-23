def reverse(string): 
    string = "".join(reversed(string)) 
    return string   
s = "Gitam"  
print("The original string is : ",end="") 
print(s) 
print("The reversed string is : ",end="") 
print(reverse(s)) 