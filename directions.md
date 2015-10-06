## Project Outline
Write a well-documented python package called “Image Doctor” that handles the following task efficiently:
### Task
You are given as input two sets: a set of template images (e.g. scenes containing bottles and cans) and a set of logo images (Heineken, Budweiser, etc..). Generate N unique realistic images containing one logo using the template images. For each template image, you are given a bounding box with the location of the object (i.e. bottle or can). 
### Constraints(software)
Use python v2 (latest)
For image processing use opencv 2.4.11 or Pillow
For docstrings see http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html
### Hints:
Use homographies to transform the logo and insert it into the template with image blending in various ways.
Background subtraction and replacement 
Add variations with transformations and ingenuity
Resize, translate, rotate, warp, noise, etc..
### Bonuses:
Speedups with parallelism (use python’s multiprocessing library)
Add unit and functional testing (use python’s pytest library)
Creative use of image manipulation functions (e.g. inpainting…)
Other efficiency boosts (e.g. speedups via cython type hinting, etc..)
