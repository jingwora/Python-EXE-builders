import sys
from cx_Freeze import setup, Executable
import shutil
import os

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter"],
    "excludes": [],
    "include_files": [("inputs", "inputs"), ("icon.ico", "icon.ico")]  # Ensure to include the icon file
}

# Base option for Windows GUI applications
base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options["build_exe"] = "build/exe"

setup(
    name="text_file_combiner",
    version="0.1",
    description="Combine contents of two text files",
    options={"build_exe": build_exe_options},
    executables=[Executable("run.py", base=base, icon="icon.ico")]
)

# After the build, move all files to a subdirectory and create shortcuts
def create_shortcuts():
    from win32com.client import Dispatch

    exe_dir = "build/exe"
    dist_dir = "dist"
    support_dir = os.path.join(dist_dir, "support_files")
    outputs_dir = os.path.join(support_dir, "outputs")

    # Ensure the dist, support_files, and outputs directories exist
    os.makedirs(support_dir, exist_ok=True)
    os.makedirs(outputs_dir, exist_ok=True)

    # Move all build files to the support_files directory
    for file in os.listdir(exe_dir):
        src_path = os.path.join(exe_dir, file)
        shutil.move(src_path, support_dir)

    # Create a shortcut to run.exe
    shell = Dispatch('WScript.Shell')
    shortcut_path_run = os.path.join(dist_dir, "run.lnk")
    target_path_run = os.path.join(support_dir, "run.exe")
    working_directory_run = support_dir

    shortcut_run = shell.CreateShortCut(shortcut_path_run)
    shortcut_run.TargetPath = os.path.abspath(target_path_run)
    shortcut_run.WorkingDirectory = os.path.abspath(working_directory_run)
    shortcut_run.IconLocation = os.path.abspath(os.path.join(support_dir, "icon.ico"))  # Correctly set the path to icon.ico
    shortcut_run.save()

    # Create a shortcut to the outputs folder
    shortcut_path_outputs = os.path.join(dist_dir, "outputs.lnk")
    target_path_outputs = os.path.abspath(outputs_dir)

    shortcut_outputs = shell.CreateShortCut(shortcut_path_outputs)
    shortcut_outputs.TargetPath = target_path_outputs
    shortcut_outputs.WorkingDirectory = target_path_outputs
    shortcut_outputs.IconLocation = target_path_outputs
    shortcut_outputs.save()

# Run the tidy up process
create_shortcuts()
