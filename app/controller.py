def setup(app):
    @app.get("/test/hello")
    def hello():
        return "¡Hola, mundo!"
