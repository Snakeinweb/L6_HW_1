# https://github.com/Snakeinweb/L6_HW_1

n = int (input ())
k = 0
for i in range (0, n):
    x = int(input ())  
    if x == 0:
        k += 1
print (k)