import mc

config = mc.GetApp().GetLocalConfig()
config.ResetAll()
config.SetValue("runtime", 'first')
mc.ActivateWindow(14000)