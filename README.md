## Simple Date Picker Calendar with PySide6

This project provides a simple **date picker calendar** built with PySide6, allowing you to select and manage multiple dates.

**Key Features:**

- Select and highlight multiple dates on the calendar.
- Store selected dates efficiently in a set to prevent duplicates.
- Clear all selected dates and highlights with a dedicated button.
- Visually distinguish selected dates with a gray background.

**Getting Started:**

1. **Install the required dependencies:**

```bash
pip install pyside6
```

2. **Run the application:**

```bash
python Date Picker PySide6.py
```

3. **Interact with the calendar:**

- Click on dates to select or deselect them.
- Click the "Clear" button to reset the selection.

**Technical Details:**

- The code uses PySide6 for creating the GUI elements.
- Selected dates are stored in a set to ensure no duplicates.
- Custom QTextCharFormat is used to highlight selected dates visually.

**Note:**

- The `print` statements in the `update_selected_dates` and `clear_calendar` functions are for debugging purposes and should be removed before deploying the application.

**Contributing:**

Feel free to contribute to this project by creating pull requests with suggested improvements or new features. We welcome your feedback!

**Additional Notes:**

- You can customize the appearance of the calendar by modifying the QTextCharFormat used for highlighting.
- Consider adding more features such as date range selection or saving/loading selected dates.
