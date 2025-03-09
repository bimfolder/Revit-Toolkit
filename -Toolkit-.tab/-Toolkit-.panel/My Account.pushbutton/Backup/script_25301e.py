import clr
clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')

from System.Windows import Window, WindowStartupLocation
from System.Windows.Controls import StackPanel, TextBlock, Button, Image
from System.Windows.Media import Brushes, FontFamily
from System.Windows.Input import Cursors
from System.Windows.Media.Imaging import BitmapImage
from System import Uri
from System.Diagnostics import Process
from System.Windows.Clipboard import SetText
from System.Windows import FontWeights, Thickness, HorizontalAlignment
from System.Windows.Documents import Hyperlink, Run, LineBreak

def show_message_with_link():
    # StackPanel setup
    stack_panel = StackPanel()
    stack_panel.Margin = Thickness(20)

    # TextBlock setup
    text_block = TextBlock()
    text_block.Margin = Thickness(0, 0, 0, 20)
    text_block.FontSize = 16
    text_block.FontFamily = FontFamily("Segoe UI")
    text_block.Foreground = Brushes.DarkBlue
    text_block.FontWeight = FontWeights.Normal
    text_block.Inlines.Add(Run("First line of your message here."))
    text_block.Inlines.Add(LineBreak())
    text_block.Inlines.Add(Run("Second line with "))

    # Hyperlink setup
    hyperlink = Hyperlink()
    hyperlink_text = Run("clickable link")
    hyperlink.Inlines.Add(hyperlink_text)
    hyperlink.Foreground = Brushes.Blue

    def open_link(sender, args):
        url = "https://example.com"
        Process.Start(url)

    hyperlink.Click += open_link
    text_block.Inlines.Add(hyperlink)
    text_block.Inlines.Add(Run(" in the middle."))
    text_block.Inlines.Add(LineBreak())
    text_block.Inlines.Add(Run("Third line of your message."))
    stack_panel.Children.Add(text_block)

    # Image setup
    image = Image()
    image.Source = BitmapImage(Uri("https://www.bimfolder.com/lib/plan_01.png"))
    image.Width = 200
    image.Height = 150
    image.Margin = Thickness(0, 10, 0, 10)
    image.Cursor = Cursors.Hand

    def open_image_link(sender, args):
        Process.Start("https://www.bimfolder.com/pySubs_new.asp?pid=1")

    image.MouseLeftButtonUp += open_image_link
    stack_panel.Children.Add(image)

    # Copy button setup
    copy_button = Button()
    copy_button.Content = "Copy 'aaa'"
    copy_button.Width = 100
    copy_button.Height = 30
    copy_button.HorizontalAlignment = HorizontalAlignment.Center

    def copy_to_clipboard(sender, args):
        SetText("aaa")

    copy_button.Click += copy_to_clipboard
    stack_panel.Children.Add(copy_button)

    # Close button setup
    close_button = Button()
    close_button.Content = "Close"
    close_button.Width = 100
    close_button.Height = 30
    close_button.HorizontalAlignment = HorizontalAlignment.Center

    def close_window(sender, args):
        window.Close()

    close_button.Click += close_window
    stack_panel.Children.Add(close_button)

    # Window setup
    window = Window()
    window.Title = "Message"
    window.Width = 400
    window.Height = 400
    window.Content = stack_panel
    window.WindowStartupLocation = WindowStartupLocation.CenterScreen
    window.AllowsTransparency = True  # Transparency
    window.BorderBrush = Brushes.Gray  # Shaded border color
    window.BorderThickness = Thickness(2)  # Border thickness
    window.WindowStyle = 0  # No title bar
    window.ShowDialog()

show_message_with_link()
