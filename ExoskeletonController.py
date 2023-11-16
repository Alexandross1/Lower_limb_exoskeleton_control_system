class ExoskeletonController:
    def __init__(self, joint_angle, target_angle):
        self.joint_angle = joint_angle
        self.target_angle = target_angle

    def control_algorithm(self):
        # algorytm, który dąży do ustawienia joint_angle na target_angle
        self.joint_angle += 0.1 * (self.target_angle - self.joint_angle)
        
def extract_flexo_extension(angles_data, activity_results):
    extracted_angles = []
    prev_angle = None  # Ustawienie wartości poprzedzającej na None

    # Pobierz kąty z extract_angle jako dane wejściowe dla kąta docelowego
    target_angles = extract_angle(angles_data, activity_results)

    # Algorytm sterowania
    controller = ExoskeletonController(angles_data.iloc[0], None)  # Początkowy docelowy kąt ustawiony na None

    for index, (angle, activity, target_angle) in enumerate(zip(angles_data, activity_results, target_angles)):
        if activity == 1:
            # Ustaw docelowy kąt na wartość z extract_angle dla danego indeksu
            controller.target_angle = target_angle

            # Wywołaj algorytm sterowania, aby dostosować kąt stawu
            controller.control_algorithm()

            # Pobierz nowy kąt stawu po dostosowaniu
            adjusted_angle = controller.joint_angle

            # Dodaj dostosowany kąt do listy
            extracted_angles.append(adjusted_angle)
            prev_angle = adjusted_angle
        elif prev_angle is not None:
            extracted_angles.append(prev_angle)
        else:
            extracted_angles.append(angle)

    return extracted_angles
