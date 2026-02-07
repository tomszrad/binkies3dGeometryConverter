# Extracting 3D Geometry from Binkies3D

Follow these steps to extract a 3D model from a Live 3D project on studio.binkies3d.com.

## Steps

1. **Create Project**
   - Go to [studio.binkies3d.com](https://studio.binkies3d.com).
   - Create a *Live 3D project* with the desired model.

2. **Access Embed Page**
   - Open the project's *Embed* page.

3. **Override JavaScript in Browser**
   - Open the page in Chrome/Chromium.
   - Press **F12** to open *Developer Tools*.
   - Go to the **Sources** tab.
   - Locate the file `225.live3d-player.js` (it will load from the page).
   - Enable *Local Overrides*:
     1. In **Sources → Overrides**, pick a local folder to store overrides.
     2. Right-click on `225.live3d-player.js` and choose **Save for overrides**.
   - Open the overridden script in the editor.  
     Use **Ctrl+F** in the editor to search for:
     ```
     l = e(s, i)
     ```
   - When you find it, insert a line just after it:
     ```javascript
     console.log(l);
     ```
   - Reload the page. Now the geometry JSON will be printed in the browser console.

4. **Export Geometry**
   - Open the *Console* tab.
   - Copy the logged JSON.
   - Save it as `geometry.json` in your working directory.

5. **Install Dependencies**
   - Make sure you have Python 3 and pip installed.
   - Install required packages:
     ```bash
     pip install numpy numpy-stl
     ```

6. **Run Conversion Scripts**
   - In terminal, run:
     ```bash
      python3 filtr.py && python3 convert.py
     ```

## Output
The final model will be saved as:

```
output_model.stl
```

in the same directory.

---

Ensure all scripts and `geometry.json` are in the same catalog before starting.
