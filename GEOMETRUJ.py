import json
import numpy as np
from stl import mesh

def create_stl_from_json(json_file, stl_file):
    # Wczytanie danych z pliku JSON
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Lista do przechowywania wierzchołków i indeksów
    all_vertices = []
    all_faces = []
    vertex_offset = 0

    # Przetwarzanie każdego obiektu w danych
    for obj in data:
        positions = obj['positions'][0]  # Zakładamy, że jest tylko jeden zestaw pozycji
        indices = obj['indices']

        # Dodanie wierzchołków
        vertices = []
        position_keys = sorted(positions.keys(), key=int)  # Sortowanie kluczy
        for i in range(len(position_keys) // 3):  # Zakładamy, że wierzchołki są w zestawach po 3
            x = float(positions[position_keys[i * 3]])
            y = float(positions[position_keys[i * 3 + 1]])
            z = float(positions[position_keys[i * 3 + 2]])
            vertices.append([x, y, z])

        # Dodanie twarzy (trójkątów)
        faces = []
        for i in range(0, len(indices), 3):
            face_indices = [indices[str(j)] + vertex_offset for j in range(i, i + 3)]
            faces.append(face_indices)

        all_vertices.extend(vertices)
        all_faces.extend(faces)
        vertex_offset += len(vertices)

    # Konwersja do numpy array
    vertices = np.array(all_vertices)
    faces = np.array(all_faces)

    # Tworzenie obiektu mesh
    stl_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

    for i, f in enumerate(faces):
        for j in range(3):
            stl_mesh.vectors[i][j] = vertices[f[j], :]

    # Zapis do pliku STL
    stl_mesh.save(stl_file)

# Użycie funkcji
json_file = 'geometria.geometries.json'  # Ścieżka do pliku JSON
stl_file = 'output_model.stl'             # Ścieżka do pliku wyjściowego STL
create_stl_from_json(json_file, stl_file)