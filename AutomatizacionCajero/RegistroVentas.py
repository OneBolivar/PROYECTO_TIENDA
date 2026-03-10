

def RegistroVentas():
    VALIDADOR = True
    while VALIDADOR:  
        
        try:
            NombreProducto = input("Ingrese el nombre del producto: ")  
            PrecioProducto = float(input("Ingrese el precio del producto: "))
            CantidadProducto = int(input("¿Cuantos productos desea comprar?: "))
            SeguirComprando = input("¿Desea seguir comprando?: ")
            Total = PrecioProducto*CantidadProducto  
            
            VALIDADOR = False
        except ValueError:   
            print("¡ERROR! Debe ingresar un número")