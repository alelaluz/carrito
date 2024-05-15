class Carrito:
    def __init__(self, request):
        # nuestro request sea igual al que recibimos
        self.request = request
        # nuestra sesion sea igual a lasesion que tiene el request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            # self.session["carrito"] va a ser igual a un diccionario carrito
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    # agregar un nuevo producto
    def agregar(self, producto):
        # sacamos el id para que nos quede mas prolijo
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        # si el producto ya existe
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    # esta  funcion va a pedir un producto
    def elimninar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.elimninar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
