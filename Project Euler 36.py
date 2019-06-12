import time
start = time.time()

def Double_base_palindromes(upper_bound,x):
    while int(x) < upper_bound:
        if str(x) == str(x[::-1]):
            if str(bin(x)[2:].zfill(8)) == str(bin(x)[2:].zfill(8)[::-1]):
                print(x)
        x = str(int(x)+1)

Double_base_palindromes(1000000,str(10))

end = time.time()
print(end - start)
