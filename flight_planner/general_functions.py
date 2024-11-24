"""
These functions are general, and they are reused in other functions in another file-storage.py for more
abstraction, readability and to simplify the project.
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


def search_entities(entity_dict, entity_criteria, data):
    for key, value in entity_dict.items():
        for m_key, m_value in value.items():
            if entity_criteria == m_key:
                if data == m_value:
                    return entity_dict[key]


def update_entity(entity_dict, entity_id, entity_data):
    if entity_id in entity_dict:
        entity_dict[entity_id].update(entity_data)
        return entity_dict[entity_id]


def update_all_entities(entity_dict, entity_criteria):
    for key in entity_dict.keys():
        entity_dict[key].update(entity_criteria)
    return entity_dict
