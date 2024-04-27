a = lambda i : i+10
x = lambda a,b : a%b
y = lambda a,b,c : a+b+c
str = lambda s : s.upper()
str2 = lambda s : s.lower()
large_num = lambda a,b : a if a>b else b
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
 
# print("Int formatting:", format_numeric(1000000))
# print("float formatting:", format_numeric(999999.789541235))


# print(a(8))
# print(x(8,3))
# print(y(8,3,5))
# print(str2('Test stRIng uPPer '))
print(large_num(3,7))
