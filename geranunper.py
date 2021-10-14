def generapares(limite):

    num = 1

    while num<limite:

        yield num*2 #com este comando no usamo el return
        num=num+1
devuelvepares= generapares(10)        
    
for i in devuelvepares:
    print(i)  



