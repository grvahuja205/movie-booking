from .. import db

def get_model_id_model_object_mapping(model_name):

    model_id_model_object_mapping = dict(db.session.query(
        model_name.id, model_name).all())

    return model_id_model_object_mapping