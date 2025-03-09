import wpf
from System import Windows
from System.Windows import Window
from System.Windows.Controls import TextBlock, StackPanel, Button
from System.Windows.Documents import Hyperlink, Run, LineBreak
from System.Windows.TextWrapping import Wrap
from System.Windows.WindowStartupLocation import CenterScreen
from System.Windows.Media import Brushes, FontFamily
from System.Windows import FontWeights, Thickness, HorizontalAlignment
from System.Diagnostics import Process
from pyrevit import script


# Alternative approach without XAML
def show_message_with_link():
    # Create a stack panel to hold multiple text blocks if needed
    stack_panel = StackPanel()
    stack_panel.Margin = Thickness(20)

    # Create text block with hyperlink
    text_block = TextBlock()
    text_block.TextWrapping = Wrap
    text_block.Margin = Thickness(0, 0, 0, 20)  # Add bottom margin for spacing

    # Set font properties for the entire TextBlock
    text_block.FontSize = 16
    text_block.FontFamily = FontFamily("Segoe UI")
    text_block.Foreground = Brushes.DarkBlue
    text_block.FontWeight = FontWeights.Normal

    # First line of text
    text_block.Inlines.Add(Run("First line of your message here."))

    # Add a line break
    text_block.Inlines.Add(LineBreak())

    # Second line of text
    text_block.Inlines.Add(Run("Second line with "))

    # Add hyperlink
    hyperlink = Hyperlink()
    hyperlink_text = Run("clickable link")
    hyperlink.Inlines.Add(hyperlink_text)
    hyperlink.Foreground = Brushes.Blue
    hyperlink.TextDecorations = Windows.TextDecorations.Underline

    def open_link(sender, args):
        url = "https://example.com"
        Process.Start(url)

    hyperlink.Click += open_link
    text_block.Inlines.Add(hyperlink)
    text_block.Inlines.Add(Run(" in the middle."))

    # Add another line break
    text_block.Inlines.Add(LineBreak())

    # Third line of text
    text_block.Inlines.Add(Run("Third line of your message."))

    # Add the text block to the stack panel
    stack_panel.Children.Add(text_block)

    # Create close button
    close_button = Button()
    close_button.Content = "Close"
    close_button.Width = 100
    close_button.Height = 30
    close_button.HorizontalAlignment = HorizontalAlignment.Center

    # Define the close button event handler
    def close_window(sender, args):
        window.Close()

    close_button.Click += close_window

    # Add the button to the stack panel
    stack_panel.Children.Add(close_button)

    # Create and show window
    window = Window()
    window.Title = "Message"
    window.Width = 400
    window.Height = 250
    window.Content = stack_panel
    window.WindowStartupLocation = CenterScreen
    window.ShowDialog()


# Run the code-only approach
show_message_with_link()