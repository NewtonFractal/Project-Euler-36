import time
start = time.time()

def Double_base_palindromes(upper_bound,x):
    while int(x) < upper_bound:
        if str(x) == str(x[::-1]):
            y = str(x)
        x = str(int(x)+1)

Double_base_palindromes(1000000,str(10))

end = time.time()
print(end - start)