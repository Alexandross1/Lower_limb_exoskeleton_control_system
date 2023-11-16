import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import numpy as np

# Funkcja do aplikowania filtru górnoprzepustowego Butterworth
def highpass_filter(data, cutoff_frequency, sampling_rate, order=4):
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    y = filtfilt(b, a, data)
    return y

# Funkcja do zastosowania filtru ruchomej średniej
def moving_average(signal, window_size):
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')

# Ścieżka do folderu zawierającego pliki CSV
folder_path = '/content/Normal'  

# Pobranie listy plików CSV w folderze
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Iteracja przez wszystkie pliki CSV w folderze
for file in csv_files:
    file_path = os.path.join(folder_path, file)

    # Wczytanie danych z pliku CSV
    data = pd.read_csv(file_path)

    emg_columns = data.columns[:-1] 

    # Normalizacja i zastosowanie filtru górnoprzepustowego dla każdej kolumny sygnałów EMG
    for column in emg_columns:
        # Normalizacja dla zakresu [0, 1]
        normalized_signal = (data[column] - data[column].min()) / (data[column].max() - data[column].min())

        # Zastosowanie filtru górnoprzepustowego
        cutoff_frequency = 1  # Przykładowa wartość, dostosuj do potrzeb
        sampling_rate = 120  # Przykładowa wartość, dostosuj do faktycznej częstotliwości próbkowania
        highpass_filtered_signal = highpass_filter(normalized_signal, cutoff_frequency, sampling_rate)

        # Odcinanie amplitud poniżej zera
        highpass_filtered_signal[highpass_filtered_signal < 0] = 0

        # Zastosowanie filtru ruchomej średniej
        window_size = 90  # Przykładowa szerokość okna dla filtru ruchomej średniej
        moving_avg_filtered_signal = moving_average(highpass_filtered_signal, window_size)

         # Symulacja algorytmu sterowania egzoszkieletem
        angles_data = data['Flexo-Extension']
        activity_results = exoskeleton_control(moving_avg_filtered_signal)
        extracted_angles = extract_flexo_extension(angles_data, activity_results)
        
        
        # Tworzenie wykresu dla activity
        plt.figure(figsize=(25, 2))
        plt.plot(activity_results, label=f'Aktywacja Egzoszkieletem - {column} - {file}')
        plt.title(f'Aktywacja Egzoszkieletem - {column} - {file}')
        plt.xlabel('Indeks')
        plt.axhline()
        plt.xlim(0, 8000)
        plt.axhline(y=0, color='g', linestyle='--')
        plt.axhline(y=1, color='r', linestyle='--')
        plt.ylabel('Aktywacja')
        plt.grid(True)
        plt.legend()
        plt.show()

        # Tworzenie wykresu dla extracted_angles
        plt.figure(figsize=(25, 4))
        plt.plot(extracted_angles, color='m')
        plt.title(f'ścieżka ruchu egzoszkieletu - {column} - {file}')
        plt.xlim(0, 8000)
        plt.ylim(-150, 150)
        plt.xlabel('Indeks')
        plt.ylabel('Wartości dla Aktywacji')
        plt.grid(True)
        plt.legend()
        plt.show()
        print(extracted_angles)

        # Tworzenie wykresu dla flexo extension
        plt.figure(figsize=(25, 4))
        plt.plot(angles_data, color='c', label='Wartości dla Aktywacji')
        plt.title(f'Flexo-Extension - {column} - {file}')
        plt.xlim(0, 8000)
        plt.ylim(-150, 150)
        plt.xlabel('Indeks')
        plt.ylabel('Wartości dla Aktywacji')
        plt.grid(True)
        plt.legend()
        plt.show()
