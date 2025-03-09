import clr, System
clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')
clr.AddReference('System')
from System.Windows import Window, WindowStartupLocation
from System.Windows.Controls import StackPanel, TextBlock, Button, Image, Border, WrapPanel
from System.Windows.Media import Brushes, FontFamily
from System.Windows.Input import Cursors
from System.Windows.Media.Imaging import BitmapImage
from System import Uri
from System.Diagnostics import Process
from System.Windows.Clipboard import SetText
from System.Windows import FontWeights, Thickness, HorizontalAlignment
from System.Windows.Documents import Hyperlink, Run, LineBreak
from System.Windows import CornerRadius
from pyrevit import HOST_APP
import requests
def check_file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD to only fetch headers
        if response.status_code == 200:
            return True  # File exists
        elif response.status_code == 404:
            return False  # File not found
        else:
            print("Error: " + response.status_code)
            return False
    except requests.RequestException as e:
        print("Request error:" + e)
        return False

autodesk_id = __revit__.Application.Username.lower() + "-" + HOST_APP.uiapp.Application.LoginUserId
userfolder = HOST_APP.uiapp.Application.LoginUserId
account_status = "NA"
if check_file_exists("https://www.bimfolder.com/Dropbox/Apps/pyRevit-3/pyUser/"+ userfolder + "/.active.py"):
    account_status = "Active"
if check_file_exists("https://www.bimfolder.com/Dropbox/Apps/pyRevit-3/pyUser/"+ userfolder + "/.inactive.py"):
    account_status = "Inactive"
if check_file_exists("https://www.bimfolder.com/Dropbox/Apps/pyRevit-3/pyUser/"+ userfolder + "/.trial.py"):
    account_status = "Trail"
    url = "https://www.bimfolder.com/Dropbox/Apps/pyRevit-3/pyUser/" + userfolder + "/.trial.py"
    response = requests.head(url)
    creation_time = response.headers.get("Last-Modified")
    from datetime import datetime
    cre_time = datetime.strptime(creation_time, "%a, %d %b %Y %H:%M:%S GMT")
    day_left = 30 - (datetime.utcnow() - cre_time).days

def show_message_with_link():
    stack_panel = StackPanel()
    stack_panel.Margin = Thickness(20)
    # First line: Username + Autodesk Id
    first_text_block = TextBlock()
    first_text_block.Margin = Thickness(100, 0, 20, 0)
    first_text_block.FontSize = 16
    first_text_block.FontFamily = FontFamily("Segoe UI")
    first_text_block.Foreground = Brushes.DarkBlue
    first_text_block.FontWeight = FontWeights.Normal
    first_text_block.Inlines.Add(Run("Autodesk ID:  " + autodesk_id))
    stack_panel.Children.Add(first_text_block)
    # Second line: Copy to clipboard button
    copyclip_button = Button()
    copyclip_button.Margin = Thickness(200, 5, 20, 0)
    copyclip_button.Content = "Copy To Clipboard"
    copyclip_button.FontSize = 14
    copyclip_button.FontFamily = FontFamily("Segoe UI")
    copyclip_button.Width = 250
    copyclip_button.Height = 25
    copyclip_button.HorizontalAlignment = HorizontalAlignment.Left
    def copy_to_clipboard(sender, args):
        SetText(autodesk_id)
    copyclip_button.Click += copy_to_clipboard
    stack_panel.Children.Add(copyclip_button)
    # Third line: Type of accout
    second_text_block = TextBlock()
    second_text_block.Margin = Thickness(100, 5, 5, 5)
    second_text_block.FontSize = 16
    second_text_block.FontFamily = FontFamily("Segoe UI")
    second_text_block.Foreground = Brushes.Red
    second_text_block.FontWeight = FontWeights.Normal
    if account_status == "Trail":
        second_text_block.Inlines.Add(Run("Account Status: Trial (" + str(day_left) + " Days left)"))
    stack_panel.Children.Add(second_text_block)
    # Image setup in a horizontal row using a WrapPanel
    image_panel = WrapPanel()
    image_panel.Margin = Thickness(0, 15, 0, 1)
    image1 = Image()
    image1.Source = BitmapImage(Uri("https://www.bimfolder.com/lib/plan_01r.png"))
    image1.Width = 256
    image1.Height = 440
    image1.Margin = Thickness(2)
    image1.Cursor = Cursors.Hand
    def open_image1_link(sender, args):
        Process.Start("https://www.bimfolder.com/pySubs_new.asp?pid=1")
    image1.MouseLeftButtonUp += open_image1_link
    image2 = Image()
    image2.Source = BitmapImage(Uri("https://www.bimfolder.com/lib/plan_10r.png"))
    image2.Width = 256
    image2.Height = 440
    image2.Margin = Thickness(2)
    image2.Cursor = Cursors.Hand
    def open_image2_link(sender, args):
        Process.Start("https://www.bimfolder.com/pySubs_new.asp?pid=2")
    image2.MouseLeftButtonUp += open_image2_link
    image3 = Image()
    image3.Source = BitmapImage(Uri("https://www.bimfolder.com/lib/plan_30r.png"))
    image3.Width = 256
    image3.Height = 440
    image3.Margin = Thickness(2)
    image3.Cursor = Cursors.Hand
    def open_image3_link(sender, args):
        Process.Start("https://www.bimfolder.com/pySubs_new.asp?pid=3")
    image3.MouseLeftButtonUp += open_image3_link
    image_panel.Children.Add(image1)
    image_panel.Children.Add(image2)
    image_panel.Children.Add(image3)
    stack_panel.Children.Add(image_panel)
    # Window setup
    window = Window()
    window.Title = "My Account"
    window.Width = 850
    window.Height = 650
    window.Content = stack_panel
    window.WindowStartupLocation = WindowStartupLocation.CenterScreen
    window.ShowDialog()

show_message_with_link()