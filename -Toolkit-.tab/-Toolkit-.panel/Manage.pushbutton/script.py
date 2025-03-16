# -*- coding: utf-8 -*-
__title__ = "Tool\nManager"
import sys, clr, os, subprocess, shutil, requests, re
clr.AddReference('System.Windows.Forms')
clr.AddReference('PresentationFramework')
clr.AddReference('PresentationCore')
clr.AddReference('WindowsBase')
from pyrevit import forms, revit, script
from pyrevit.loader import sessionmgr

def Update_Toolkit_Panel():
    Local_panel = os.environ.get("USERPROFILE") + "\\AppData\\Roaming\\pyRevit\\Extensions\\BIMFolder.extension\\-Toolkit-.tab\\-Toolkit-.panel"
    shutil.rmtree(Local_panel)
    args_c = [UID + "-c"]
    process_c = subprocess.Popen([exe_path] + args_c, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000)
    stdout_c, stderr_c = process_c.communicate()  # stdout_a (Output from print), error message (error message)
    if process_c.returncode == 0:
        return 0
    else:
        forms.alert(stderr_c, ok=True, yes=False, no=False)
        sys.exit()
def Update_BFD_Json():
    Local_Bupd = os.environ.get("USERPROFILE") + "\\AppData\\Roaming\\pyRevit\\Extensions\\BIMFolder.extension\\BfdUpdate.pak"
    Local_Json = os.environ.get("USERPROFILE") + "\\AppData\\Roaming\\pyRevit\\Extensions\\BIMFolder.extension\\extension.json"
    os.remove(Local_Bupd)
    os.remove(Local_Json)
    Cloud_Bupd = "https://bimfolder.com/Dropbox/Apps/pyRevit-3/Toolkit/ToolkitforRevitPlugins/BIMFolder.extension/BFDupdate.pak"
    response = requests.get(Cloud_Bupd, stream=True)
    with open(Local_Bupd, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    Cloud_Json = "https://bimfolder.com/Dropbox/Apps/pyRevit-3/Toolkit/ToolkitforRevitPlugins/BIMFolder.extension/extension.json"
    response = requests.get(Cloud_Json, stream=True)
    with open(Local_Json, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
def Update_Lib():
    Local_lib = os.environ.get("USERPROFILE") + "\\AppData\\Roaming\\pyRevit\\Extensions\\BIMFolder.extension\\lib"
    shutil.rmtree(Local_lib)
    args_a = [UID + "-d"]
    process_d = subprocess.Popen([exe_path] + args_a, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000)
    stdout_d, stderr_d = process_d.communicate()  # stdout_d (Output from print), error message (error message)
    if process_d.returncode == 0:
        return 0
    else:
        forms.alert(stderr_d, ok=True, yes=False, no=False)
        sys.exit()
def Upgrade_App(V_loc,V_cur):
    V_locc = list(map(int, V_loc.split('.')))
    V_curr = list(map(int, V_cur.split('.')))
    Upd_Act = 0
    if V_locc[0] == V_curr[0] and V_locc[1] == V_curr[1]:
        Upd_Act = 1  # Update <-Toolkit-.panel>
    else:
        if V_locc[0] == V_curr[0]:
            Upd_Act = 2  # Update <-Toolkit-.panel>+BFDUpdate.pak+extension.json
        else:
            Upd_Act = 3  # Update <-Toolkit-.panel>+BFDUpdate.pak+extension.json+<lib>
    if Upd_Act == 1:
        pb_count = 0
        pb_len = 2
        with forms.ProgressBar(step=1, cancellable=False) as pb:
            pb_count += 1
            pb.title = "Download Toolkit Panel ... ... ..."
            pb.update_progress(pb_count, pb_len)
            run1 = Update_Toolkit_Panel()
            if run1 == 0:
                pb_count += 1
                pb.title = "Reloading Ribbon ... ... ..."
                pb.update_progress(pb_count, pb_len)
                sessionmgr.reload_pyrevit()
                # sessionmgr.execute_command('pyrevitcore-pyrevit-pyrevit-tools-reload')
    if Upd_Act == 2:
        pb_count = 0
        pb_len = 3
        with forms.ProgressBar(step=1, cancellable=False) as pb:
            pb_count += 1
            pb.title = "Download Toolkit Panel ... ... ..."
            pb.update_progress(pb_count, pb_len)
            run1 = Update_Toolkit_Panel()
            if run1 == 0:
                pb_count += 1
                pb.title = "Update Main App ... ... ..."
                pb.update_progress(pb_count, pb_len)
                Update_BFD_Json()
                pb_count += 1
                pb.title = "Reloading Ribbon ... ... ..."
                pb.update_progress(pb_count, pb_len)
                sessionmgr.reload_pyrevit()
                # sessionmgr.execute_command('pyrevitcore-pyrevit-pyrevit-tools-reload')
    if Upd_Act == 3:
        pb_count = 0
        pb_len = 4
        with forms.ProgressBar(step=1, cancellable=False) as pb:
            pb_count += 1
            pb.title = "Download Toolkit Panel ... ... ..."
            pb.update_progress(pb_count, pb_len)
            run1 = Update_Toolkit_Panel()
            if run1 == 0:
                pb_count += 1
                pb.title = "Update Main App ... ... ..."
                pb.update_progress(pb_count, pb_len)
                Update_BFD_Json()
                pb_count += 1
                pb.title = "Download latest library  ... ... ..."
                pb.update_progress(pb_count, pb_len)
                run2 = Update_Lib()
                if run2 == 0:
                    pb_count += 1
                    pb.title = "Reloading Ribbon ... ... ..."
                    pb.update_progress(pb_count, pb_len)
                    sessionmgr.reload_pyrevit()
                    # sessionmgr.execute_command('pyrevitcore-pyrevit-pyrevit-tools-reload')
def Refresh_Tools():
    pb_count = 0
    pb_len = 3
    with forms.ProgressBar(step=1, cancellable=False) as pb:
        # ----- a: Downloading newly tools
        pb_count += 1
        pb.title = "Downlading New Tools ... ... ..."
        pb.update_progress(pb_count, pb_len)
        args_a = [UID + "-a"]
        process_a = subprocess.Popen([exe_path] + args_a, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000)
        stdout_a, stderr_a = process_a.communicate()  # stdout_a (Output from print), error message (error message)
        if process_a.returncode == 0:
            ## ----- b. Update folder structure
            pb_count += 1
            pb.title = "Updating Folder Structure ... ... ..."
            pb.update_progress(pb_count, pb_len)
            args_b = [UID + "-b"]
            process_b = subprocess.Popen([exe_path] + args_b, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000)
            stdout_b, stderr_b = process_b.communicate()  # stdout_a (Output from print), error message (error message)
            if process_b.returncode == 0:
                ## ----- c. Reload
                pb_count += 1
                pb.title = "Reloading Ribbon ... ... ..."
                pb.update_progress(pb_count, pb_len)
                sessionmgr.reload_pyrevit()
                # sessionmgr.execute_command('pyrevitcore-pyrevit-pyrevit-tools-reload')
            else:
                forms.alert(stderr_b, ok=True, yes=False, no=False)
                sys.exit()
        else:
            forms.alert(stderr_a, ok=True, yes=False, no=False)
            sys.exit()

script_folder = os.path.dirname(os.path.realpath(__file__))
xaml_folder = os.path.join(script_folder, "WebBrowserWindow.xaml")
UID = __revit__.Application.Username.lower()

if UID != "":
    exe_path = os.environ.get("USERPROFILE") + "\\AppData\\Roaming\\pyRevit\\Extensions\\BIMFolder.extension\\BfdUpdate.pak"
    class WebBrowserWindow(forms.WPFWindow):
        def __init__(self, xaml_file):
            forms.WPFWindow.__init__(self, xaml_file)
            self.webBrowser.Navigate("https://www.bimfolder.com/pyBIM/Tab.asp?UID=" + UID)
            self.Button1.Click += self.run_Button1
            self.Button2.Click += self.run_Button2
            self.Button3.Click += self.run_Button3
        def run_Button1(self, sender, args):
            window.Close()
            res = forms.alert("      The ribbon will be updated.\n(Restart Revit if icons appear misaligned)", ok=False, yes=True, no=True)
            if not res:
                sys.exit()
            url = "https://bimfolder.com/pybim/Tab_Build_C.asp?UID=" + UID
            requests.get(url)
            Refresh_Tools()
        def run_Button2(self, sender, args):
            window.Close ()
            S_curr = "https://raw.githubusercontent.com/bimfolder/Revit-Toolkit/main/-Toolkit-.tab/-Toolkit-.panel/About.pushbutton/script.py"
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
                response = forms.alert(
                    "You're running the latest version of App (" + V_cur + ")",
                    exitscript=False,
                    options=["Refresh All Installed Tools", "Exit Without Action"],
                    warn_icon=False
                )
                if response == "Refresh All Installed Tools":
                    Folder_Tools = os.environ.get("USERPROFILE") + "\\AppData\\Roaming\\pyRevit\\Extensions\\BIMFolder.extension\\Tools"
                    if os.path.exists(Folder_Tools) and os.path.isdir(Folder_Tools):
                        shutil.rmtree(Folder_Tools)
                    os.makedirs(Folder_Tools)
                    Refresh_Tools()
                elif response == "Exit Without Action":
                    sys.exit()
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
        def run_Button3(self, sender, args):
            window.Close ()
    window = WebBrowserWindow (xaml_folder)
    window.ShowDialog()