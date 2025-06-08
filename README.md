## Instructions for Extracting Geometry from Binkies3D

1. **Create a Live 3D Project**  
   Go to [studio.binkies3d.com](https://studio.binkies3d.com) and create a **Live 3D project** with the model you want to retrieve.

2. **Open the Embed Page**  
   Navigate to the **embed page** of the project.

3. **Modify JavaScript**  
   Locate and **overwrite** the script file:  
   `842.live3d-player.js`

   Inside this script, **log the value of variable `l` to the console** at the moment it's assigned the result of `e(s, i)`.  
   Example modification:
   ```javascript
   l = e(s, i);
   console.log(l);
   ```

4. **Save JSON Output**  
   Open the browser console, **copy the printed JSON**, and **save it to a file** named:  
   `geometria.json`

5. **Run Python Scripts**  
   In the following order, execute the Python scripts:
   ```bash
   python3 FILTRUJ.py
   python3 GEOMETRUJ.py
   ```

---

📌 Make sure `geometria.json` is in the correct directory before running the scripts.

---

🧩 The final output model will appear as `output_model.stl` in the same directory.
