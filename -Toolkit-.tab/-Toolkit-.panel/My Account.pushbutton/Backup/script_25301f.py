import clr

clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')

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


def show_message_with_link():
    # StackPanel setup for message content
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

    # Image setup in a horizontal row using a WrapPanel
    image_panel = WrapPanel()
    image_panel.Margin = Thickness(0, 10, 0, 10)

    # Image 1
    image1 = Image()
    image1.Source = BitmapImage(Uri("https://www.bimfolder.com/lib/plan_01.png"))
    image1.Width = 100
    image1.Height = 100
    image1.Margin = Thickness(5)
    image1.Cursor = Cursors.Hand

    # Image 2
    image2 = Image()
    image2.Source = BitmapImage(Uri("https://www.bimfolder.com/lib/plan_10.png"))
    image2.Width = 100
    image2.Height = 100
    image2.Margin = Thickness(5)
    image2.Cursor = Cursors.Hand

    # Image 3
    image3 = Image()
    image3.Source = BitmapImage(Uri("https://www.bimfolder.com/lib/plan_30.png"))
    image3.Width = 100
    image3.Height = 100
    image3.Margin = Thickness(5)
    image3.Cursor = Cursors.Hand

    # Add images to the WrapPanel
    image_panel.Children.Add(image1)
    image_panel.Children.Add(image2)
    image_panel.Children.Add(image3)

    stack_panel.Children.Add(image_panel)

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

    # Border with rounded corners setup
    border = Border()
    border.Background = Brushes.White
    border.BorderBrush = Brushes.Gray
    border.BorderThickness = Thickness(2)
    border.CornerRadius = CornerRadius(15)
    border.Child = stack_panel

    # Window setup
    window = Window()
    window.Title = "Message"
    window.Width = 400
    window.Height = 400
    window.Content = border
    window.WindowStartupLocation = WindowStartupLocation.CenterScreen
    window.AllowsTransparency = True  # Transparency
    window.WindowStyle = 0  # No title bar
    window.ShowDialog()


show_message_with_link()
