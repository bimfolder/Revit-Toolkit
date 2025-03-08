# -*- coding: utf-8 -*-
from pyrevit import forms, script
class AboutWindow(forms.WPFWindow):
    def __init__(self, xaml_file_name):
        forms.WPFWindow.__init__(self, xaml_file_name)
        self.short_version_info.Text = '1.0.1'
        self.pyrevit_subtitle.Text = '(Organizes and manages pyRevit Plugins)'
        self.pyrevit_engine.Text = 'Running on pyRevit v4.8.13 and Above'
        self.copyright_tb.Text = '© 2024 BIMFolder Services'
    def openwiki(self, sender, args):
        script.open_url('https://www.bimfolder.com')
    def openyoutubechannel(self, sender, args):
        script.open_url ('https://www.youtube.com/channel/UC5ORVWjUKiMf2qQ9RgYzVyQ')
    def handleclick(self, sender, args):
        self.Close()
AboutWindow('AboutWindow.xaml').show_dialog()
