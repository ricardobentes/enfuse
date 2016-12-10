#!/usr/bin/env python

from gimpfu import *
import subprocess
import os

def enfuse(image, drawable, tempPath): 
        #    blend180, verbose, levels, tiff_compression, jpg_compression,
        #    fus_exp, fus_cont, fus_sat, fus_mu, fus_sigma, force_hard_blend,
        #    use_CIECAM02, associated_alpha_hack, block_size, cache_size):
    

    enfusePath = "C:\\enfuse\\bin\\enfuse.exe"

# Save Layers in temp files
    pdb.gimp_progress_set_text ("Exporting layers to temp files")

    tempFiles = []

    for layer in image.layers:
        layer.visible = 1
        pdb.gimp_edit_copy(layer)
        newImage = pdb.gimp_edit_paste_as_new()
        fileName = layer.name.decode('utf-8')+ ".tiff"
        fullName = tempPath+fileName
        newdrawable = newImage.layers[0]
        pdb.file_tiff_save(newImage, newdrawable, fullName, fileName, 0)
        tempFiles.append(fullName)
        

# Create Enfuse command
    pdb.gimp_progress_set_text ("Creating Enfuse command")

    inputFiles = ""
    for inputFile in tempFiles:
        inputFiles = inputFiles + " " + inputFile
        pdb.gimp_message(inputFiles)

    outputFile = tempPath + "hdr.tiff"

    appPath = enfusePath + " --output " + outputFile + " " + inputFiles

# call Enfuse
    pdb.gimp_progress_set_text ("Enfusing...")

    child = subprocess.Popen(appPath, shell=False)
    child.communicate()

# Import result as new layer
    pdb.gimp_progress_set_text ("Importing Enfused image into new layer")

    resultFile = pdb.file_tiff_load(outputFile, outputFile)
    pdb.gimp_edit_copy(resultFile.layers[0])
    newLayer = pdb.gimp_layer_new(image, image.width, image.height, RGB, "Enfused", 100, 0)
    image.add_layer(newLayer)
    floatingSel = pdb.gimp_edit_paste(newLayer, FALSE)
    pdb.gimp_floating_sel_anchor(floatingSel)

# Clean up
    pdb.gimp_progress_set_text ("Cleaning up")

    for tempFile in tempFiles:
        os.remove(tempFile)

    os.remove(outputFile)
    #pdb.gimp_message("Ding!")

register(
    "python-fu-enfuse",
    "Enfuse",
    "Create an HDR image from several exposures",
    "Ricardo Bentes", #Author
    "Ricardo Bentes", #Copyright  
    "2016", #Copyright year
    "Enfuse", #Name of the Gimp menu
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_DIRNAME, "tempPath", "Temp files path", "D:\\")
        # (PF_BOOL,   "blend180", "Blend accros -180/+180 boundary", False),
        # (PF_BOOL,   "verbose", "Verbose", False),
        # (PF_SPINNER, "levels", "Levels (0 - Auto)", 0, (0, 29, 1)),
        # (PF_OPTION, "tiff_compression", "TIFF Compression", 0,
        #     ("None", "Packbits", "LZW", "Deflate")
        #  ),
        # (PF_SPINNER, "jpg_compression", "JPEG Compression (0 - Default)", 0, (0, 100, 1)),

        # (PF_SLIDER, "fus_exp",  "Fusion Exp.", 1.000, (0.000, 1.000, 0.001)),
        # (PF_SLIDER, "fus_cont",  "Fusion Cont.", 0.000, (0.000, 1.000, 0.001)),
        # (PF_SLIDER, "fus_sat",  "Fusion Sat.", 0.200, (0.000, 1.000, 0.001)),
        # (PF_SLIDER, "fus_mu",  "Fusion Mu", 0.500, (0.000, 1.000, 0.001)),
        # (PF_SLIDER, "fus_sigma",  "Fusion Sigma", 0.200, (0.000, 1.000, 0.001)),
        # (PF_BOOL,   "force_hard_blend", "Force hard blend masks", False),

        # (PF_BOOL,   "use_CIECAM02", "User CIECAM02 to blend colors", False),
        # (PF_BOOL,   "associated_alpha_hack", "Associated-alpha hack", False),
        # (PF_INT, "block_size", "Block size (KB)", 2048),
        # (PF_INT, "cache_size", "Cache size (MB)", 1024)
    ],
    [],
    enfuse, menu="<Image>/Filters/Combine")  # second item is menu location

main()