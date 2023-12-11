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



        paragraph = text.text
        modified_text = paragraph

        offset = 0

        text_patches = []
        if len(tags.find_all()) > 0:
            for i in tags.find_all():
                tag = i.get('TYPE')
                start = int(i.get('start'))
                end = int(i.get('end'))
                text_patch = (modified_text[offset: start], tag)
                text_patches.append(text_patch)
                offset = end

        text_patches.append((modified_text[offset:], ''))

def get_redacted_text(text_patches):
    redacted_text = ''
    for patch_tuple in text_patches:
        text = patch_tuple[0]
        text_label = patch_tuple[1]
        if text_label != '':
            temp_text = text+'['+text_label+']'
        else:
            temp_text = text
        redacted_text += temp_text

    return redacted_text
