import flask

from .usecase import contactoperations

mock_embalse = {
    "nombre": "Pepito",
    "ccaa": "Andalucía",
    "provincia": "Málaga",
    "coordenadas": {"x": 36.7178, "y": -4.4256},
    "demarcacion": "Demacración",
    "agua_total": 100
}
mock_embalse2 = {
    "nombre": "Jorgito",
    "ccaa": "Andalucía",
    "provincia": "Málaga",
    "coordenadas": {"x": 36.7178, "y": -4.4256},
    "demarcacion": "Demacración",
    "agua_total": 100
}

def setup(app):
    @app.get("/")
    def index():
        return flask.render_template("index.html")
    
    @app.get("/map")
    def map():
        return flask.render_template("map.html")

    @app.get("/embalse/")
    def lista_embalse():
        return flask.render_template("lista_embalse.html", embalses=[mock_embalse, mock_embalse2])
    
    @app.get("/embalse/<int:embalse_id>")
    def detalle_embalse(embalse_id: int):
        
        return flask.render_template("detalle_embalse.html", embalse=mock_embalse)

    @app.get("/data/contacts")
    def get_contacts():
        return flask.jsonify(
            contactoperations.get_all_contacts()
        )

    @app.get("/data/contacts/<int:contact_id>")
    def get_contact(contact_id: int):
        return flask.jsonify(
            contactoperations.get_contact(contact_id)
        )

    @app.post("/data/contacts")
    def create_contact():
        body = flask.request.form
        return flask.jsonify(
            contactoperations.create_new_contact(body)
        )

    @app.put("/data/contacts")
    def modify_contact():
        body = flask.request.form
        return flask.jsonify(
            contactoperations.update_contact(body)
        )

    @app.delete("/data/contacts/<int:contact_id>")
    def delete_contact(contact_id: int):
        return flask.jsonify(
            contactoperations.delete_contact(contact_id)
        )
