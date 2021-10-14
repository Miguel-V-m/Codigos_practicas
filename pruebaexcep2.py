def divide():
    try:

        op1=(float(input('introdice el primer numero: ')))

        op2=(float(input('introduce el segundo numero: ')))

        print('ladivision es: '+ str(op1/op2))
    except ValueError:
        print('el valor introduzido es erróneo')

    except ZeroDivisionError:
        print('mo se puede dividir entre cero!')        

    print('calculo finalizado') # esta linea se lee normal en alguno caso se usa el finally

divide()    