
# Text File Combiner

This application combines the contents of two text files. It is built using Tkinter for the GUI and cx_Freeze for creating an executable.

## Developer Guide

### Prerequisites

- Python 3.x
- pip

### Setup

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Building the Executable

1. **Ensure cx_Freeze is installed:**
    ```bash
    pip install cx-Freeze
    ```

2. **Run the setup script to build the executable:**
    ```bash
    python setup.py build
    ```

3. **Find the executable in the `build` directory.**

### Project Structure

```
sample_project/
├── functions.py       # Logic for checking and combining text files
├── icon.ico           # Icon image
├── run.py             # Tkinter GUI
├── setup.py           # Configuration for cx_Freeze
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
├── build/
│   └── exe/           # Temporary build directory
│       └── ...        # Intermediate files
├── dist/
│   ├── run.lnk        # Shortcut to the executable
│   ├── outputs.lnk    # Shortcut to the outputs folder
│   └── support_files/ # Directory for all required files
│       ├── run.exe
│       ├── python3.dll
│       ├── python311.dll
│       └── outputs/
│           └── output.txt


```

## User Guide

### Using the Text File Combiner

1. **Run the executable:**
    Navigate to the `build` directory and double-click the executable file.

2. **Combine Text Files:**
    - Click the "Combine Text Files" button.
    - Select the first text file in the file dialog.
    - Select the second text file in the file dialog.
    - The combined content of the two files will be displayed in a message box.

### Requirements

- Windows operating system
- No additional software needed as all dependencies are included in the executable

---

This application provides a simple and user-friendly way to combine the contents of two text files. If you encounter any issues or have any questions, please refer to the documentation or contact the developer.
