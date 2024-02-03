# En tu_app/middleware.py
class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código que se ejecuta en cada solicitud antes de llegar a la vista
        print(f"Solicitud recibida en la URL: {request.path}")
        response = self.get_response(request)
        # Código que se ejecuta en cada respuesta después de salir de la vista
        return response
