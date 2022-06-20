import aspose.slides as slides
import aspose.pydrawing as drawing


with slides.Presentation("m1.pptx") as presentation:
    presentation.save("pres1.pdf ",slides.export.SaveFormat.PDF)

    

