#MenuTitle: Baseline Wiggle
"""Create pseudorandom baseline shift for all selected glyphs."""

import random
random.seed()

wiggleMax  =  50
wiggleMin  = -50
linelength =  70

Font = Glyphs.orderedDocuments()[0].font
Doc  = Glyphs.currentDocument

def create_otclass( classname   = "@default", 
                    classglyphs = [ x.parent.name for x in Doc.selectedLayers() ], 
                    targetfont  = Glyphs.orderedDocuments()[0].font ):
	"""
	Creates an OpenType class in the font.
	Default: class @default with currently selected glyphs in the current font.
	Returns a status message in form of a string.
	"""
	
	if not classname[0] == "@":
		classname = "@"+classname
		
	newClass = GSClass()
	newClass.name = classname
	newClass.code = " ".join( classglyphs )
	targetfont.classes.append( newClass )
	
	return "Created OT class: %s" % classname

def create_otfeature( featurename = "calt", 
                      featurecode = "sub a' a by a.alt;", 
                      targetfont  = Glyphs.orderedDocuments()[0].font ):
	"""
	Creates an OpenType feature in the font.
	Default: calt with "sub a' a by a.alt;" in the current font.
	Returns a status message in form of a string.
	"""
	
	newFeature = GSFeature()
	newFeature.name = featurename
	newFeature.code = featurecode
	targetfont.features.append( newFeature )
	
	return "Created OT feature: %s" % featurename

featuretext = ""
for j in range( linelength, 0, -1 ):
	newline = "pos @wiggle' " + "@wiggle "*j + "<0 " + str( random.randint( wiggleMin, wiggleMax ) ) + " 0 0>;\n"
	featuretext = featuretext + newline

print create_otclass( classname="@wiggle" )
print create_otfeature( featurename="calt", featurecode=featuretext )