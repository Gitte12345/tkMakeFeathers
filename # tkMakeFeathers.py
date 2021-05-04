# tkMakeFeathers.py

from functools import partial 
import maya.cmds as cmds
import maya.mel as mel


def cShrinkWin(windowToClose, *args):
    cmds.window(windowToClose, e=1, h=20, w=440)


def cBakePFX(action, *args):
	polyPfxList = []
	pfx = cmds.ls(sl=1, l=1)
	if not pfx:
		cmds.textField('tfFeedback', tx='Select a paint effect to convert', e=1)

	pfx = cmds.ls(sl=1, l=1)[0]
	start = cmds.intField('ifStart', v=1, q=1)
	end = cmds.intField('ifEnd', v=1, q=1)
	diff = end - start
	print diff



	if diff >= 0 and diff < 101:
		for f in range(start, end, 1):
			cmds.textField('tfFeedback', tx=('Baking ... ' + str(f)), e=1)
			cmds.currentTime(f)
			cmds.select(pfx)
			cmds.PaintEffectsToPoly()
			polyPfxShp = cmds.ls(sl=1, l=1)
			polyPfx = cmds.listRelatives(p=1) 
			polyPfx = cmds.rename(polyPfx, 'bakedPfx_' + str(f))
			cmds.delete(polyPfx, ch=1)
			polyPfxList.append(polyPfx)

			dag = cmds.listRelatives(polyPfx, p=1)
			cmds.parent(polyPfx, w=1)
			cmds.delete(dag) 

		cPlanarUV(polyPfxList)

		if action == 'export':
			cExportFeathers(polyPfxList)
		
		cmds.textField('tfFeedback', tx='Success', e=1)

	if diff <= 0:
		cmds.textField('tfFeedback', tx='Strange range', e=1)
	elif diff > 3:
		cmds.textField('tfFeedback', tx='Max 100 objects alllowed', e=1)
	


def cPlanarUV(polyPfxList, *args):
	for obj in polyPfxList:
		cmds.select(obj, r=1)
		v = cmds.polyEvaluate(obj, v=1)
		vertices = (str(obj) + '.f[0:' + str(v) + ']')
		cmds.polyProjection(str(vertices), ch=0, type='Planar', ibd=1, md='z')



def cExportFeathers(polyPfxList, *args):
	ws = cmds.workspace(fn=1)
	newPath = ws + '/scenes/justFeathers' 
	if os.path.isdir(newPath) == 0:
		os.mkdir(newPath)				

	if polyPfxList is 'exportSelection':
		polyPfxList = cmds.ls(sl=1, l=1)

	if len(polyPfxList) < 101:
		for obj in polyPfxList:
			obj = obj.split('|')[-1]
			file = newPath + '/' + obj + '.ma' 
			cmds.select(obj, r=1)
			# print file
			cmds.textField('tfFeedback', tx=file, e=1)
			cmds.file(file, force=1, typ='mayaAscii', pr=1, es=1)

	else:
		cmds.textField('tfFeedback', tx='more than 100 objects selected', e=1)








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
cmds.frameLayout('flMakeFeathers', l='Make Faethers From PFX', bgc=(colGreen[0], colGreen[1], colGreen[2]), cll=1, cl=0, cc=partial(cShrinkWin, 'win_tkMakefeathersHelper'))

cmds.columnLayout(adj=1)
cmds.rowColumnLayout(nc=4, cw=[(1, 140), (2, 60), (3, 60), (4, 140)])
cmds.button(l='Bake From To', c=partial(cBakePFX, 'bake'), bgc=(colGreen[0], colGreen[1], colGreen[2]))
cmds.intField('ifStart', v=30)
cmds.intField('ifEnd', v=34)
cmds.button(l='Bake And Export', c=partial(cBakePFX, 'export'), bgc=(colRed[0], colRed[1], colRed[2]))
cmds.setParent('..')

cmds.rowColumnLayout(nc=3, cw=[(1, 140), (2, 260)])
cmds.button(l='Export to .../scenes/', c=partial(cExportFeathers, 'exportSelection'), bgc=(colRed[0], colRed[1], colRed[2]))
cmds.textField('tfPath', tx='justFeathers_A', ed=1)
cmds.setParent('..')

cmds.textField('tfFeedback', tx='', ed=0, bgc=(colGreenD[0], colGreenD[1], colGreenD[2]))

cmds.showWindow(myWindow)

cmds.window(myWindow, w=400, h=50, e=1)

cmds.select('pfxHair1', r=1)
