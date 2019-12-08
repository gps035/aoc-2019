def split_into_layers(image_data, image_height, image_width):
    pixels = image_height * image_width
    return [image_data[i:i + pixels] for i in range(0, len(image_data), pixels)]


def calculate_checksum(image_data: str, image_height: int, image_width: int):
    def get_count_of_character(image_layer: str, character: str):
        return len(image_layer) - len(image_layer.replace(character, ""))

    image_layers = split_into_layers(image_data, image_height, image_width)

    lowest = min(image_layers, key=lambda layer: get_count_of_character(layer, "0"))
    return get_count_of_character(lowest, "1") * get_count_of_character(lowest, "2")


def flatten_layers(image_data: str, image_height: int, image_width: int):
    image_layers = split_into_layers(image_data, image_height, image_width)
    image = ""
    for index in range(len(image_layers[0])):
        added = False
        for layer in image_layers:
            pixel_in_layer = layer[index]
            if pixel_in_layer == "2":
                continue
            image += pixel_in_layer
            added = True
            break
        if not added:
            image += "2"
    return image
