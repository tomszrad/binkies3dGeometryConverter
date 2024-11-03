import json

# Krok 1: Wczytanie zawartości pliku `geometria.json` i przetworzenie `geometries`
with open('geometria.json', 'r') as file:
    data = json.load(file)

# Funkcja do usuwania tablic 'ambientOcclusions', 'textureCoordinates' i 'normals' z danych
def remove_unwanted_arrays(data):
    if isinstance(data, dict):
        # Przetwarzamy słownik, usuwając klucze, jeśli są tablicami
        return {k: remove_unwanted_arrays(v) for k, v in data.items() 
                if k not in ['ambientOcclusions', 'textureCoordinates', 'normals'] or not isinstance(v, list)}
    elif isinstance(data, list):
        # Przechodzimy rekurencyjnie przez elementy listy
        return [remove_unwanted_arrays(item) for item in data]
    else:
        # Jeśli to nie jest ani słownik, ani lista, zwracamy wartość bez zmian
        return data

# Przetwarzamy zawartość klucza `geometries` (jeśli istnieje) i usuwamy niechciane tablice
if 'geometries' in data:
    geometries_data = remove_unwanted_arrays(data['geometries'])
    
    # Zapisujemy przetworzone dane do pliku `geometria.geometries.json`
    with open('geometria.geometries.json', 'w') as new_file:
        json.dump(geometries_data, new_file, indent=4)
    
    print("Zawartość 'geometries' bez tablic 'ambientOcclusions', 'textureCoordinates' i 'normals' została zapisana do pliku 'geometria.geometries.json'.")
else:
    print("Brak klucza 'geometries' w pliku JSON.")

# Krok 2: Wczytanie `geometria.geometries.json`, filtrowanie i zapisanie do nowego pliku
with open('geometria.geometries.json', 'r') as file:
    geometries_data = json.load(file)

# Rekurencyjna funkcja do usuwania kluczy liczbowych większych niż 6
def remove_large_number_keys(data):
    if isinstance(data, dict):
        return {k: remove_large_number_keys(v) for k, v in data.items() if not (k.isdigit() and int(k) > 6)}
    elif isinstance(data, list):
        return [remove_large_number_keys(item) for item in data]
    else:
        return data

# Przetwarzamy `geometries_data` by usunąć wszystkie klucze liczbowe > 6
filtered_geometries = remove_large_number_keys(geometries_data)

# Zapisujemy przefiltrowane dane do nowego pliku `geometria.geometries.filtered.json`
with open('geometria.geometries.filtered.json', 'w') as filtered_file:
    json.dump(filtered_geometries, filtered_file, indent=4)

print("Zawartość została przefiltrowana i zapisana do pliku 'geometria.geometries.filtered.json'.")
