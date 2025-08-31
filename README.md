# Extracting 3D Geometry from Binkies3D

Follow these steps to extract a 3D model from a Live 3D project on studio.binkies3d.com.

## Steps

1. **Create Project**
   - Go to [studio.binkies3d.com](https://studio.binkies3d.com).
   - Create a *Live 3D project* with the desired model.

2. **Access Embed Page**
   - Open the project's *Embed* page.

3. **Edit JavaScript**
   - Locate the file: `842.live3d-player.js`.
   - Find where `l = e(s, i)` is defined and insert:
     ```javascript
     console.log(l);
     ```
   - This logs the geometry JSON to the browser console.

4. **Export Geometry**
   - Copy the logged JSON from the console.
   - Save it as `geometria.json` in your working directory.

5. **Install Dependencies**
   - Make sure you have Python 3 and pip installed.
   - Install required packages:
     ```bash
     pip install numpy numpy-stl
     ```

6. **Run Conversion Scripts**
   - In terminal, run:
     ```bash
     python3 FILTR.py
     python3 GEOMETRUJ.py
     ```

## Output
The final model will be saved as:

```
output_model.stl
```

in the same directory.

---

Ensure all scripts and `geometria.json` are in the same folder before starting.
