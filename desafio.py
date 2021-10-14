#n = int(input('quantos termos você quer mostrar: '))
n = 5
u_1 = 1
u_2 = -1
#n = n - 1
i = 0
fib_list = []
for vic in range(0,n):
    i= u_1 + u_2
    u_1=i
    u_2 = (i- u_2) 
    fib_list.append(i)
    

#fib_string = ' '.join(fib_string)
print(fib_list)