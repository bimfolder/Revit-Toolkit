# -*- coding: utf-8 -*-

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNCTIONS
def ScriptRun(UID):
	iLoaded = []
	from pyrevit.loader import sessioninfo
	loaded_assemblies = sessioninfo.get_loaded_pyrevit_assemblies()
	for assembly in loaded_assemblies:
		iLoaded.append(assembly.split('_')[3].lower())
	if UID.split('-')[0].lower() in iLoaded:
		from pyrevit.loader import sessionmgr
		sessionmgr.execute_command(UID)
	else:
		import webbrowser
		url = "https://bimfolder.com/DemoVP.asp?Id=24705h"
		webbrowser.open(url)


