# from functools import reduce
# from typing import Dict


# def Ventas(Categoria,Valor,Cantidad) : 
#    Factura = list(map(lambda x= 0,y=0: x * y ,Valor,Cantidad))
#    Descuento = list(map(lambda x=0, y=0 : 0.1 * y if x > 10 else 0.0* y   ,Cantidad,Factura))
#    TotalFact = reduce(lambda x=0, y=0 : x+y , Factura)
#    TotalDesc = reduce(lambda x=0, y=0 : x+y , Descuento)
#    VentaTotal = int(TotalFact - TotalDesc)
#    MejorVenta = max(Factura)
   
#    print(f'Factura = {Factura}')
#    print(f'Descuento = {Descuento}')   
#    dic = {'Venta Total':VentaTotal, 'Mayor venta':MejorVenta}
   
#    return dic

import pandas as pd

elementos = { 
    "Numero atómico":[1, 6, 47, 88],
    "Masa atómica":[1.008, 12.011, 107.87, 226],
    "Familia":["No metal", "No metal", "Metal", "Metal"]
}
elementos

tabla_periodica = pd.DataFrame(elementos)
print(tabla_periodica)