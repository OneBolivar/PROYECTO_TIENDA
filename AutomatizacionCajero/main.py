from RegistroVentas import RegistroVentas 
SeguirComprando = input("¿Desea comprar algo?: ")
if SeguirComprando == "si":
    RegistroVentas()
elif SeguirComprando == "no":
     print("Producto:",NombreProducto,"|Precio Unitario:",PrecioProducto,"|Cantidad:",CantidadProducto,"|Total a pagar:",Total )
else:
    print("ERROR!!! Solo ingrese si o no")
    RegistroVentas()
    
