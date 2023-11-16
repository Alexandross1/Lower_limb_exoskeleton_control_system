import os
import pandas as pd
import matplotlib.pyplot as plt

# Ścieżka do folderu zawierającego pliki CSV
folder_path = '/content/Normal' # Zastąp 'ścieżka/do/twojego/folderu' właściwą ścieżką

# Pobranie listy plików CSV w folderze
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Iteracja przez wszystkie pliki CSV w folderze
for file in csv_files:
    file_path = os.path.join(folder_path, file)

    # Wczytanie danych z pliku CSV
    data = pd.read_csv(file_path)

    emg_columns = data.columns[0:]

    # Sprawdzenie czy kolumna 'Flexo-Extension' istnieje w danych
    flexo_extension_column = 'Flexo-Extension'
    if flexo_extension_column in data.columns:
        # Tworzenie wykresów dla każdego sygnału EMG
        plt.figure(figsize=(12, 8))
        for column in emg_columns:
            plt.plot(data[column], label=column)

        # Wykres Flexo-Extension
        plt.plot( data[flexo_extension_column], label=flexo_extension_column, linestyle='--', color='black')

        plt.title(f'Wykresy Sygnałów EMG i Flexo-Extension - {file}')
        plt.ylabel('Czas (s)')
        plt.xlabel('Amplituda')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print(f"Warning: {flexo_extension_column} not found in {file}")
