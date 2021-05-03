# tkMakeFeathers.py

from functools import partial 
import maya.cmds as cmds
import maya.mel as mel


def cShrinkWin(windowToClose, *args):
    cmds.window(windowToClose, e=1, h=20, w=440)












''' window '''
ver = 'v0.1';
windowStartHeight = 150;
windowStartWidth = 440;
bh1 = 18;
bh2 = 22;
colRed              = [0.44, 0.2, 0.2]
colBlue             = [0.18, 0.28, 0.44]
colGreen            = [0.28, 0.44, 0.28]
colGreenL           = [0.38, 0.5, 0.38]
colGreenD           = [0.1, 0.22, 0.12]
colDark             = [0.08, 0.09, 0.10]
colDark2            = [0.02, 0.21, 0.22]
colYellow           = [0.50, 0.45, 0.00]
colYellow2          = [0.42, 0.37, 0.00]
colYellow3          = [0.39, 0.34, 0.00]
colYellow4          = [0.49, 0.44, 0.00]
colYellow5          = [0.33, 0.27, 0.00]
colBlk              = [0.00, 0.00, 0.00]

if cmds.window('win_tkMakefeathersHelper', exists=1):
    cmds.deleteUI('win_tkMakefeathersHelper')

myWindow = cmds.window('win_tkMakefeathersHelper', t=('xGen Helper ' + ver), s=1, wh=(windowStartHeight, windowStartWidth ))
cmds.columnLayout(adj=1, bgc=(colGreenD[0], colGreenD[1], colGreenD[2]))
cmds.frameLayout('flStitchHeadUtils', l='Prep Work', bgc=(colGreen[0], colGreen[1], colGreen[2]), cll=1, cl=0, cc=partial(cShrinkWin, 'win_tkMakefeathersHelper'))

cmds.rowColumnLayout(nc=3, cw=[(1, 180), (2, 180), (3, 80)])
cmds.button(l='1. Import Guides', c=cImportGuides, bgc=(colGreen[0], colGreen[1], colGreen[2]))
cmds.button(l='2. Build Gear Rig', bgc=(colGreenD[0], colGreenD[1], colGreenD[2]))
cmds.button(l='3. Add Locs', c=cAddStitchLocs, bgc=(colGreen[0], colGreen[1], colGreen[2]))
# cmds.button(l='3. Rename: GRP CTRL JOIN', c=cRenameNodes, bgc=(colGreen[0], colGreen[1], colGreen[2]))
# cmds.button(l='4. Add "GRUP" at the end', c=cFindEmptyTransforms, bgc=(colGreen[0], colGreen[1], colGreen[2]))
# cmds.button(l='5. Add Attributes', c=cAddAttributes)
# cmds.setParent(top=1)
