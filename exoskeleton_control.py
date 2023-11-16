def exoskeleton_control(emg_signals, emg_threshold=0.02):
    # Inicjalizacja pustej listy wyników
    results = []

    # Iteracja przez każdy punkt czasowy
    for emg_signal_value in emg_signals:
        # Sprawdzenie aktywacji na podstawie sygnału EMG
        emg_activation = emg_signal_value > emg_threshold

        # Dodanie wyniku do listy
        if emg_activation:
            results.append(1)
        else:
            results.append(0)

    return results
