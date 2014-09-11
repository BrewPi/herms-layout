#!/usr/bin/python
#

import PythonMagick
from PyPDF2 import PdfFileWriter, PdfFileReader

fileName = "BrewPi-HERMS-drawing"
input = PdfFileReader(file(fileName + ".pdf", "rb"))
output = PdfFileWriter()

numPages = input.getNumPages()
print "document has %s pages." % numPages

# pythonmagic gave me errors. Direct shell commands worked instead.
from subprocess import check_output
for i in range(numPages):
    print "processing page ", i
    cmd = "convert -density 300 -flatten BrewPi-HERMS-drawing.pdf[" + str(i) + "] png/" + fileName + "-%02d.png"
    print check_output(cmd, shell=True)
exit()

# Pythonmagic implementation below, didn't work for me
img = PythonMagick.Image()
img.density("300")

for i in range(numPages):
    print "processing page ", i
    # img.read(fileName + ".pdf[" + str(i) + "]") # read in at 300 dpi
    img.read('BrewPi-HERMS-drawing.pdf[0]') # read in at 300 dpi
    img.write(fileName + str(i) + ".png")
