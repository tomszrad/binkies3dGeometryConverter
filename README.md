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
   - In the **Sources** tab, there are several JS scripts named `[number].live3d-player.js`. Using the text search (**Ctrl+F**), locate the one that contains the phrase `l = e(s, i)`.
   - Enable *Local Overrides* for this specific file:
     1. In **Sources → Overrides**, pick a local folder to store overrides.
     2. Right-click on the identified `[number].live3d-player.js` file and choose **Save for overrides**.
   - Open the overridden script in the editor.  
   - Just below the `l = e(s, i)` line in the identified file, insert the following line:
     ```javascript
     console.log(l);
     ```
   - Reload the page. 
   - **Note:** The page will stop functioning and an error will appear in the console. This is expected behavior – the console log will still work despite the crash.

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

```text
output_model.stl
```

in the same directory.

---

Ensure all scripts and `geometry.json` are in the same catalog before starting.