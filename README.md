# The Fractal Pi Matrix

This repository contains code to generate a massive, interactive "fractal graph" or radial tree that visually maps out the digits of Pi. 

The graph uses a counter-clockwise spiral structure where the number of nodes doubles with every outward ring (4, 8, 16, 32, etc.), allowing for the linear analysis of number patterns.

## Files Included

* **`index.html`**: The standard version. This features a locked-in 8-ring matrix pre-loaded with the first 1,021 digits of Pi.
* **`custom-matrix.html`**: The dynamic version. This allows the user to upload a custom plain text file of Pi and define how many rings they want to generate, making it capable of visualizing tens of thousands of digits with zoom and pan capabilities.
* **`extreme_matrix.html`**: The high-performance version built with viewport culling to handle 15+ rings (130,000+ digits).
* **`pi.txt`**: A plain text data file containing the first 100,000 digits of Pi, used to feed the custom matrix files.

## How to Use

1. Download or clone this repository to your local computer.
2. Double-click on any of the `.html` files to open them directly in your web browser. 
3. For the custom matrices, click the "Choose File" button in the top left corner and select the `pi.txt` file to instantly generate the graph.
4. **Controls:** Use your mouse wheel to zoom in and out, and click and drag to pan around the matrix.

## Author
* **Erin Fulks**
