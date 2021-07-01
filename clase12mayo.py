# Cobro por llamada

valor=int(input("Ingresa los minutos de la llamada: "))
dia=input("Ingrese el dia: ")
if valor <= 5:
    t1=valor*100
    if dia=="domingo":
        dom=t1*0.03
        total1=t1+dom
        print("El valor de la llamada es $",total1)
    else:
        turno=input("Ingrese el turno ...mañana o tarde: ")
        if turno=="mañana":
            man=t1*0.15
            total2=t1+man

            print("El valor de la llamada es $",total2)
        else:
            tar=t1*0.10
            total3=t1+tar
            print("El valor de la llamada es $",total3)
else:
    if valor <= 8: 
        t2=valor*80
        if dia=="domingo":
            dom=t2*0.03
            total1=t2+dom
            print("El valor de la llamada es $",total1)
        else:
            turno=input("Ingrese el turno ...mañana o tarde: ")
            if turno=="mañana":
                mana=t2*0.15
                total2=t2+mana

                print("El valor de la llamada es $",total2)
            else:
                tard=t2*0.10
                total3=t2+tard
                print("El valor de la llamada es $",total3)
    else:
        if valor <= 10: 
            t3= valor*70
            if dia=="domingo":
                dom=t3*0.03
                total1=t3+dom
                print("El valor de la llamada es $",total1)
            else:
                turno=input("Ingrese el turno ...mañana o tarde: ")
                if turno=="mañana":
                    man=t3*0.15
                    total2=t3+man

                    print("El valor de la llamada es $",total2)
                else:
                    tar=t3*0.10
                    total3=t3+tar
                    print("El valor de la llamada es $",total3)
        else:
            if valor > 10: 
                t4= valor*50
                if dia=="domingo":
                    dom=t4*0.03
                    total1=t4+dom
                    print("El valor de la llamada es $",total1)
                else:
                    turno=input("Ingrese el turno ...mañana o tarde: ")
                    if turno=="mañana":
                        man=t4*0.15
                        total2=t4+man

                        print("El valor de la llamada es $",total2)
                    else:
                        tar=t4*0.10
                        total3=t4+tar
                        print("El valor de la llamada es $",total3)

#Año bisiesto o no

