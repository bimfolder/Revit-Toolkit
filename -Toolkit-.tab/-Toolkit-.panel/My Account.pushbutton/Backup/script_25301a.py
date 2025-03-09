import wpf
from System import Windows
from System.Windows import Window
from System.Windows.Controls import TextBlock
from System.Windows.Documents import Hyperlink, Run
from System.Windows.TextWrapping import Wrap
from System.Windows.WindowStartupLocation import CenterScreen
from System.Diagnostics import Process
from pyrevit import script


# Alternative approach without XAML
def show_message_with_link():
    # Create text block with hyperlink
    text_block = TextBlock()
    text_block.TextWrapping = Wrap

    # Add regular text
    text_block.Inlines.Add(Run("Your message here. "))

    # Add hyperlink
    hyperlink = Hyperlink()
    hyperlink.Inlines.Add(Run("Click here to visit our website"))

    def open_link(sender, args):
        url = "https://example.com"  # Replace with your URL
        Process.Start(url)

    hyperlink.Click += open_link
    text_block.Inlines.Add(hyperlink)

    # Add more text if needed
    text_block.Inlines.Add(Run(" for more information."))

    # Create and show window
    window = Window()
    window.Title = "Message"
    window.Width = 400
    window.Height = 200
    window.Content = text_block
    window.WindowStartupLocation = CenterScreen
    window.ShowDialog()


# Run the code-only approach
show_message_with_link()