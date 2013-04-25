#MenuTitle: Distribute Nodes vertically
"""Distributes the selected nodes vertically."""

import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayer = Doc.selectedLayers()[0]

try:
	selection = selectedLayer.selection()
	selectionYList = [ n.y for n in selection ]
	lowestY, highestY = min( selectionYList ), max( selectionYList )
	diffY = abs(lowestY-highestY)
	
	Font.disableUpdateInterface()

	increment = diffY // ( len( selection ) - 1 )
	sortedSelection = sorted( selection, key=lambda n: n.y)
	for thisNodeIndex in range( len( selection ) ):
		sortedSelection[thisNodeIndex].y = lowestY + ( thisNodeIndex * increment )
			
	Font.enableUpdateInterface()
	
except Exception, e:
	if selection == ():
		print "Cannot distribute nodes: nothing selected in frontmost layer."
	else:
		print "Error. Cannot distribute nodes:", selection
		print e
