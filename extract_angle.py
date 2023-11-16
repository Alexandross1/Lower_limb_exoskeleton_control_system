def extract_angle(angles_data, activity_results):
    angles = []
    prev_angle = None  # Ustawienie wartości poprzedzającej na None

    for angle, activity in zip(angles_data, activity_results):
        if activity == 1:
            angles.append(angle)
            prev_angle = angle
        elif prev_angle is not None:
            angles.append(prev_angle)
        else:
            angles.append(angle)

    return angles
