import json
import numpy as np
from stl import mesh

def create_stl_from_json(json_file, stl_file, scale=1000.0, mirror_axis=None):
    """
    Creates an STL file from geometry data stored in JSON.

    :param json_file: path to input JSON file
    :param stl_file: path to output STL file
    :param scale: scale factor (default 1000.0)
    :param mirror_axis: mirror axis ("x", "y", "z" or None)
    """
    # Load JSON
    with open(json_file, 'r') as file:
        data = json.load(file)

    all_vertices = []
    all_faces = []
    vertex_offset = 0

    # Process objects
    for obj in data:
        positions = obj['positions'][0]
        indices = obj['indices']

        vertices = []
        position_keys = sorted(positions.keys(), key=int)
        for i in range(len(position_keys) // 3):
            x = float(positions[position_keys[i * 3]]) * scale
            y = float(positions[position_keys[i * 3 + 1]]) * scale
            z = float(positions[position_keys[i * 3 + 2]]) * scale
            vertices.append([x, y, z])

        faces = []
        for i in range(0, len(indices), 3):
            face_indices = [indices[str(j)] + vertex_offset for j in range(i, i + 3)]
            faces.append(face_indices)

        all_vertices.extend(vertices)
        all_faces.extend(faces)
        vertex_offset += len(vertices)

    vertices = np.array(all_vertices)
    faces = np.array(all_faces)

    # Mirror if needed
    if mirror_axis is not None:
        if mirror_axis.lower() == "x":
            vertices[:, 0] *= -1
        elif mirror_axis.lower() == "y":
            vertices[:, 1] *= -1
        elif mirror_axis.lower() == "z":
            vertices[:, 2] *= -1
        else:
            raise ValueError("mirror_axis must be one of: 'x', 'y', 'z'")

        # Fix normals by swapping indices
        faces[:, [0, 1]] = faces[:, [1, 0]]

    # Build mesh
    stl_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            stl_mesh.vectors[i][j] = vertices[f[j], :]

    # Save to STL
    stl_mesh.save(stl_file)

    # ✅ Success message
    print(f"STL file successfully created: {stl_file}")


json_file = 'geometry.geometries.json'
stl_file = 'output_model.stl'

create_stl_from_json(json_file, stl_file, scale=1000.0, mirror_axis="x")
