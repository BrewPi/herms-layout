#!/usr/bin/python
#

from PyPDF2 import PdfFileWriter, PdfFileReader

input1 = PdfFileReader(file("BrewPi-HERMS-drawing-uncropped.pdf", "rb"))
output = PdfFileWriter()

numPages = input1.getNumPages()
print "document has %s pages." % numPages

for i in range(numPages):
    page = input1.getPage(i)
    print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
    page.mediaBox.upperRight = (
        page.mediaBox.getUpperRight_x(),
        page.mediaBox.getUpperRight_y() - 100
    )
    print page.mediaBox.getLowerLeft_x(), page.mediaBox.getLowerLeft_y()
    if i == 0:
        upperLeft = page.mediaBox.getUpperLeft_y()/4*3-60
    else:
        upperLeft = page.mediaBox.getUpperLeft_y()/4*3+60
    page.mediaBox.lowerLeft = (
        page.mediaBox.getLowerLeft_x(),
        upperLeft
    )
    output.addPage(page)

outputStream = file("BrewPi-HERMS-drawing.pdf", "wb")
output.write(outputStream)
outputStream.close()