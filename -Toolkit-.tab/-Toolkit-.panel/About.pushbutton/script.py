# -*- coding: utf-8 -*-
from pyrevit import forms, script
class AboutWindow(forms.WPFWindow):
    def __init__(self, xaml_file_name):
        forms.WPFWindow.__init__(self, xaml_file_name)
        self.short_version_info.Text = '1.1.0'
        self.pyrevit_subtitle.Text = '(Organizes and manages pyRevit Plugins)'
        self.pyrevit_engine.Text = 'Running on pyRevit v5.0.0 and Above'
        self.copyright_tb.Text = '© 2024 BIMFolder Services'
    def openwiki(self, sender, args):
        script.open_url('https://www.bimfolder.com')
    def openupd(self, sender, args):
        import time, random, requests, re, os, sys, shutil
        self.Close()
        timestamp = str(int(time.time()) + random.randint(0, 1000))
        S_curr = "https://raw.githubusercontent.com/bimfolder/Revit-Toolkit/main/-Toolkit-.tab/-Toolkit-.panel/About.pushbutton/script.py?timestamp=" + timestamp
        V_curr = requests.get(S_curr)
        if V_curr.status_code == 200:
            lines = V_curr.text.splitlines()
            line_6 = lines[5] if len(lines) >= 6 else None
            match = re.search(r"'([^']+)'", line_6)
            if match:
                V_cur = match.group(1)
        else:
            print("Error")
        V_local = (os.path.join(os.getenv('APPDATA'), 'pyRevit', 'Extensions', 'BIMFolder.extension', '-Toolkit-.tab', '-Toolkit-.panel', 'About.pushbutton',
                                'script.py'))
        with open(V_local, 'r') as file:
            lines = file.readlines()
            line_6 = lines[5] if len(lines) >= 6 else None
            match = re.search(r"'([^']+)'", line_6)
            if match:
                V_loc = match.group(1)
        if V_loc == V_cur:
            forms.alert("You have the latest version installed.", exitscript=False)
        else:
            response = forms.alert(
                "               A new version (" + V_cur +") is available. \n       The currently installed  version is (" + V_loc +").",
                exitscript=False,
                options=["Upgrade App Only", "Upgrade App and Refresh Installed Tools", "Exit Without Action"],
                warn_icon=False
            )
            if response == "Upgrade App Only":
                Upgrade_App(V_loc, V_cur)
            elif response == "Upgrade App and Refresh Installed Tools":
                Upgrade_App(V_loc, V_cur)
                Folder_Tools = os.environ.get("USERPROFILE") + "\\AppData\\Roaming\\pyRevit\\Extensions\\BIMFolder.extension\\Tools"
                if os.path.exists(Folder_Tools) and os.path.isdir(Folder_Tools):
                    shutil.rmtree(Folder_Tools)
                os.makedirs(Folder_Tools)
                Refresh_Tools()
            elif response == "Exit Without Action":
                sys.exit()
    def handleclick(self, sender, args):
        self.Close()
AboutWindow('AboutWindow.xaml').show_dialog()
