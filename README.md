# File Name Replacer

A GUI-based Python tool for replacing parts of file names within a directory, with options for recursive searching, regular expressions, and case sensitivity.

## Description

This application provides a user-friendly interface for batch renaming files. It allows you to specify a directory, a search string, and a replacement string. You can then preview the changes before applying them. The tool supports recursive searching through subdirectories, using regular expressions for more complex patterns, and toggling case sensitivity for the search.

## Features

- **Graphical User Interface (GUI):** Easy-to-use interface built with `tkinter` and `ttkbootstrap` for a modern look.
- **Directory Selection:** Browse and select the target directory using a file dialog.
- **Search and Replace:** Specify the string to search for and the string to replace it with.
- **Regular Expression Support:** Use regular expressions for advanced pattern matching.
- **Case Sensitivity:** Toggle case sensitivity for the search.
- **Recursive Search:** Search for files in subdirectories as well.
- **Preview:** View the proposed file name changes before applying them.
- **Progress Bar:** Track the progress of the renaming process.
- **Status Updates:** See the current status of each file being processed.
- **Error Handling:** Displays error messages if any issues occur during renaming.

## Usage

1.  **Select Directory:** Click the "Browse" button to choose the directory containing the files you want to rename.
2.  **Enter Search String:** Type the string you want to find in the file names into the "Search String" field.
3.  **Enter Replace String:** Type the string you want to use as the replacement into the "Replace String" field.
4.  **Configure Options:**
    - **Use Regular Expression:** Check this box if your search string is a regular expression.
    - **Case Sensitive:** Check this box to perform a case-sensitive search.
    - **Recursive Search:** Check this box to search for files in subdirectories.
5.  **Preview Changes:** Click the "Preview" button to see a list of the proposed file name changes.
6.  **Replace Files:** If you are satisfied with the preview, click the "Replace Files" button to rename the files.

## Installation

1.  **Prerequisites:** Make sure you have Python 3.6 or higher installed.
2.  **Download the Source Code:** Download the source code from the GitHub repository. You can either clone the repository using Git or download the ZIP file.
3.  **Install Dependencies:**
    ```bash
    pip install tkinter ttkbootstrap
    ```
    (You might need to use `pip3` instead of `pip` depending on your Python setup.)
4.  **Run the Application:**
    ```bash
    python file_renamer.py
    ```

## Contributing

Contributions are welcome! Here's how you can contribute:

1.  **Fork the Repository:** Create your own fork of the repository.
2.  **Create a Branch:** Create a new branch for your feature or bug fix.
3.  **Make Changes:** Implement your changes and commit them with descriptive messages.
4.  **Submit a Pull Request:** Submit a pull request to the main repository.

Please follow these guidelines when contributing:

- Write clear and concise commit messages.
- Test your changes thoroughly.
- Follow the existing code style.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This project uses [tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- This project uses [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/) for the modern GUI theme.
