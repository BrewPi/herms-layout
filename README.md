herms-layout
============

Sketches for an automated HERMS setup.

Drawings are made with Edraw max (trial version).

Feel free to fork the design and modify it under the Creative Commons Attribution-ShareAlike 4.0 International License, found at http://creativecommons.org/licenses/by-sa/4.0/

GitHub issues and pull requests are very welcome.


Drawing guidelines used:
------------------------

* Active elements (open valves, active pumps, active pipes) have bold lines, 3pt. 
* Lines and elements keep the color of the last fluid that went through them.
* Copy-paste keeps the position when used from one page to another page. Use this to your advantage.


Dealing with the trial watermark:
---------------------------------
The page layout is set to much bigger than needed. The trial version prints a watermark in the middle of the page. By setting the page really big, it does not overlap with the drawing.

A python script is included to crop the PDF to normal size and trim off all watermarks.

Python dependency: PyPDF2


Converting PDF to PNGs:
-----------------------
Another python script is included to convert the PDF into separate PNG's.

It has 3 dependencies: ImageMagick, PythonMagick and Ghostscript. Windows installers can be found here:
http://www.imagemagick.org/script/binary-releases.php
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pythonmagick
http://www.ghostscript.com/download/gsdnld.html