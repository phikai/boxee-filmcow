import mc

def setMenu():
	config = mc.GetApp().GetLocalConfig()
	show = config.GetValue("show")
	
	if (show == 'recentuploads'):
		mc.GetWindow(14000).GetToggleButton(1200).SetSelected(False)
		mc.GetWindow(14000).GetToggleButton(1201).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1202).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1203).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1204).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1205).SetSelected(True)
	elif (show == 'charlietheunicorn'):
		mc.GetWindow(14000).GetToggleButton(1200).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1201).SetSelected(False)
		mc.GetWindow(14000).GetToggleButton(1202).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1203).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1204).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1205).SetSelected(True)
	elif (show == 'charlietehunicron'):
		mc.GetWindow(14000).GetToggleButton(1200).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1201).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1202).SetSelected(False)
		mc.GetWindow(14000).GetToggleButton(1203).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1204).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1205).SetSelected(True)
	elif (show == 'llamaswithhats'):
		mc.GetWindow(14000).GetToggleButton(1200).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1201).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1202).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1203).SetSelected(False)
		mc.GetWindow(14000).GetToggleButton(1204).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1205).SetSelected(True)
	elif (show == 'animatedshorts'):
		mc.GetWindow(14000).GetToggleButton(1200).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1201).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1202).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1203).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1204).SetSelected(False)
		mc.GetWindow(14000).GetToggleButton(1205).SetSelected(True)
	elif (show == 'liveactionshorts'):
		mc.GetWindow(14000).GetToggleButton(1200).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1201).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1202).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1203).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1204).SetSelected(True)
		mc.GetWindow(14000).GetToggleButton(1205).SetSelected(False)
	else:
		pass
		
def setFocus(items):
	mc.GetActiveWindow().GetList(100).SetItems(items)
	mc.GetActiveWindow().GetList(100).SetFocusedItem(0)
	mc.GetActiveWindow().GetControl(100).SetFocus()
	mc.GetActiveWindow().GetControl(100).SetVisible(True)

def thumbReplace(items):
	for item in items:
		item.SetThumbnail(item.GetThumbnail().replace('3.jpg','0.jpg'))
		mc.GetActiveWindow().GetList(100).SetItems(items)

	mc.GetActiveWindow().GetControl(100).SetFocus()
	mc.GetActiveWindow().GetControl(100).SetVisible(True)