import flask

from .usecase import contactoperations


def setup(app):
    @app.get("/")
    def index():
        return flask.render_template("index.html")
    
    @app.get("/map")
    def map():
        return flask.render_template("map.html")

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
