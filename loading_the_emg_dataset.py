import os
import pandas as pd
import matplotlib.pyplot as plt

# Ścieżka do folderu zawierającego pliki CSV
folder_path = '/content/Normal'  # Zastąp '/content/Normal' właściwą ścieżką

# Pobranie listy plików CSV w folderze
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Iteracja przez wszystkie pliki CSV w folderze
for file in csv_files:
    file_path = os.path.join(folder_path, file)

    # Wczytanie danych z pliku CSV
    data = pd.read_csv(file_path)

    emg_columns = data.columns[:-1]  # Wszystkie kolumny, pomijając ostatnią ('Flexo-Extension')

    # Tworzenie wykresów dla każdego sygnału EMG
    for column in emg_columns:
        plt.figure(figsize=(8, 2))
        plt.plot(data[column])
        plt.title(f'Wykres Sygnału EMG - {column} - {file}')
        plt.xlabel('Indeks')
        plt.ylabel('Amplituda')
        plt.grid(True)
        plt.show()

    # Tworzenie wykresu dla kolumny 'Flexo-Extension'
   # plt.figure(figsize=(12, 8))
   # plt.plot(data['Flexo-Extension'], linestyle='--', color='black')
   # plt.title(f'Wykres Sygnału Flexo-Extension - {file}')
   # plt.xlabel('Indeks')
   # plt.ylabel('Amplituda')
   # plt.grid(True)
   # plt.show()
