def remove_overlapping_entities(entities):
    """
    Remove overlapping entities from a list, giving priority to entities that appear earlier in the list.

    :param entities: List of entities, where each entity is represented as a tuple (start_pos, end_pos).
    :return: A new list of entities with no overlaps.
    """
    non_overlapping = []

    for current_entity in entities:
        overlap = False
        for added_entity in non_overlapping:
            # Check if the current entity overlaps with any already added entity
            if not (current_entity[1] <= added_entity[0] or current_entity[0] >= added_entity[1]):
                overlap = True
                break
        
        if not overlap:
            non_overlapping.append(current_entity)

    return non_overlapping

# Example usage
entities = [(0, 10), (5, 15), (16, 20), (18, 25)]
non_overlapping_entities = remove_overlapping_entities(entities)
print(non_overlapping_entities)
