"""Simple date picker calendar using PySide6. Multiple dates can be selected and
stored in a set. The clear button removes all selected dates from the set and
clears all highlights from the calendar."""

# Import necessary modules
from PySide6.QtWidgets import (
   QApplication,
   QWidget,
   QCalendarWidget,
   QPushButton,
   QVBoxLayout,
)
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QTextCharFormat


# Create a custom widget for date selection
class DatePickerWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize variables to store selected dates and formatting
        self.selected_dates = set()  # Use set to hold selected dates
        self.selected_date_format = QTextCharFormat()  # Format for highlighting selected dates
        self.selected_date_format.setBackground(Qt.gray)  # Set background color for selected dates

        # Create the calendar widget and clear button
        self.calendar = QCalendarWidget()
        self.clear_button = QPushButton("Clear")

        # Set up the user interface
        self.init_ui()

    def init_ui(self):
        # Create a vertical layout to hold the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)  # Add the calendar to the layout
        layout.addWidget(self.clear_button)  # Add the clear button to the layout
        self.setLayout(layout)  # Set the layout for the widget

        # Connect signals and slots for button clicks and calendar interactions
        self.clear_button.clicked.connect(self.clear_calendar)  # Connect clear button to clear_calendar function
        self.calendar.clicked.connect(self.update_selected_dates)  # Connect calendar clicks to update_selected_dates

    def update_selected_dates(self):
        # Get the currently selected date
        clicked_date = self.calendar.selectedDate()

        # If the date is already selected, deselect it
        if clicked_date in self.selected_dates:
            self.selected_dates.remove(clicked_date)  # Remove from the list
            self.calendar.setDateTextFormat(clicked_date, QTextCharFormat())  # Remove highlight
        else:
            # Otherwise, select it and highlight it
            self.selected_dates.add(clicked_date)  # Add to the set
            self.calendar.setDateTextFormat(clicked_date, self.selected_date_format)  # Apply highlight

        # Print the list of selected dates for debugging
        print(self.selected_dates)

    def clear_calendar(self):
        # Iterate through the select_dates set to clear the calendar and empty the set
        for date in self.selected_dates:  # Iterate through the set directly
            self.calendar.setDateTextFormat(date, QTextCharFormat())  # Remove highlight
        self.selected_dates.clear()  # Clear the set

        # Print the updated list of selected dates for debugging
        print(self.selected_dates)


# Run the application if this module is executed directly
if __name__ == "__main__":
    app = QApplication([])
    widget = DatePickerWidget()
    widget.show()
    app.exec()

