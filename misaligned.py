def get_index(i, j) -> str:
    return str((i * 5 + j) + 1)


def get_color_map_length(major_color_length, minor_color_length) -> int:
    return major_color_length * minor_color_length


def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    try:
        for i in range(len(major_colors)):
            for j in range(len(minor_colors)):
                print("{} | {} | {}".format(get_index(i, j).ljust(2), major_colors[i].ljust(6), minor_colors[j].ljust(6)))
    except Exception:
        return False
    return True
