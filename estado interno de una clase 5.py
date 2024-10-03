class CarritoDeCompras:
    def __init__(self):
        self.productos =[] # estado inicial lista vacia
    def agregar_productos(self,producto):
        self.productos.append(producto)
    def eliminar_producto(self,producto):
        if productos in self.producto:
            self.productos.remove(producto)
        def mostrar_productos(self):
            if self.productos:
                print("productos en el carrito:",".".join(self.productos))
            else:
                print("el carrito esta vacio.")
                