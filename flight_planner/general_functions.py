"""
These functions are general, and they are reused in other functions in another file-storage.py for more
abstraction and to simplify the project.
"""


def generate_new_id(entity_dict):
    return max(entity_dict.keys(), default=0) + 1


def create_entity(entity_dict, entity_data):
    new_id = generate_new_id(entity_dict)
    entity = {'id': new_id, **entity_data}
    entity_dict[new_id] = entity
    return entity


def get_entity(entity_dict, entity_id):
    return entity_dict.get(entity_id)


def delete_entity(entity_dict, entity_id):
    if entity_id in entity_dict:
        del entity_dict[entity_id]


def delete_all_entities(entity_dict):
    entity_dict.clear()