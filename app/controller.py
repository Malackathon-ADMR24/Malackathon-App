import flask

from .usecase import contactoperations
from .usecase.embalseoperations import get_embalse_list, get_embalse


def setup(app):
    @app.get("/")
    def index():
        return flask.render_template("index.html")

    @app.get("/map")
    def map():
        return flask.render_template("map.html")

    @app.get("/embalse/")
    def lista_embalse():
        return flask.render_template("lista_embalse.html", embalses=[vars(e) for e in get_embalse_list()])

    @app.get("/embalse/<int:embalse_id>")
    def detalle_embalse(embalse_id: int):
        obj = vars(get_embalse(embalse_id))
        print(obj)
        return flask.render_template("detalle_embalse.html", embalse=obj)

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
