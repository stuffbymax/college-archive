import subprocess
import os
import shutil  # For moving the file after processing

def convert_acsm_to_pdf(acsm_file, output_pdf=None, adobecmd_path=None):
    """
    Converts an ACSM file to a PDF using Adobe Digital Editions.  Requires Adobe Digital Editions to be installed.

    Args:
        acsm_file (str): Path to the ACSM file.
        output_pdf (str, optional): Path to the output PDF file. If None, 
                                   it will be created in the same directory as the ACSM file,
                                   with the same name but the .pdf extension.
        adobecmd_path (str, optional): Path to the Adept.exe or adobeactivate.exe file (Adobe Digital Editions command-line tool).
                                   If None, it will attempt to find it in the default installation location.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """

    if not os.path.exists(acsm_file):
        print(f"Error: ACSM file not found: {acsm_file}")
        return False

    if output_pdf is None:
        output_pdf = os.path.splitext(acsm_file)[0] + ".pdf"


    # Determine the path to Adept.exe or adobeactivate.exe if not provided.
    if adobecmd_path is None:
        # Common paths where Adept.exe or adobeactivate.exe might be located.
        possible_paths = [
            "C:\\Program Files (x86)\\Adobe\\Adobe Digital Editions\\Adept.exe", # Windows 64-bit
            "C:\\Program Files\\Adobe\\Adobe Digital Editions\\Adept.exe",   # Windows 32-bit
            "C:\\Program Files (x86)\\Adobe\\Adobe Digital Editions 4.0\\adobeactivate.exe", # Win
            "C:\\Program Files\\Adobe\\Adobe Digital Editions 4.0\\adobeactivate.exe", # Win
            "/Applications/Adobe Digital Editions.app/Contents/MacOS/Adobe Digital Editions" # macOS (This isn't the command-line tool, but it should still work through subprocess)
        ]

        for path in possible_paths:
            if os.path.exists(path):
                adobecmd_path = path
                break

        if adobecmd_path is None:
            print("Error: Could not find Adept.exe/adobeactivate.exe. Please specify the path using the 'adobecmd_path' argument.")
            return False


    # Construct the command to execute.
    command = [adobecmd_path, acsm_file]

    try:
        # Execute the command.  Capture both standard output and standard error.
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Check the return code.  A return code of 0 usually indicates success.
        return_code = process.returncode

        if return_code == 0:
            print(f"Successfully converted {acsm_file} to {output_pdf}")

            # After successful conversion, Adobe Digital Editions usually places the PDF in its library folder.
            # We need to find it and move it to the desired output location.
            # This part requires some assumptions about ADE's behavior, so it might need adjustments.

            ade_library_path = os.path.expanduser("~/Documents/My Digital Editions/")
            if os.path.exists(ade_library_path):
              # Find the PDF file based on the ACSM filename in ADE library
              for filename in os.listdir(ade_library_path):
                 if filename.lower().startswith(os.path.splitext(os.path.basename(acsm_file))[0].lower()) and filename.lower().endswith(".pdf"):
                   pdf_source_path = os.path.join(ade_library_path, filename)
                   try:
                     shutil.move(pdf_source_path, output_pdf) # Move the PDF to specified location.
                     print(f"Moved PDF file from ADE library to: {output_pdf}")
                     return True
                   except FileNotFoundError:
                      print(f"Error: Conversion appeared successful, but the PDF file not found in ADE library: {pdf_source_path}")
                      return False
                   except Exception as e:
                      print(f"Error: Could not move the converted PDF file: {e}")
                      return False
              print("Error: Conversion appeared successful, but could not find corresponding PDF in ADE library.")
              return False
            else:
                print(f"Error: Could not find Adobe Digital Editions library folder: {ade_library_path}")
                return False
        else:
            print(f"Error: Conversion failed with return code {return_code}")
            print(f"Stdout: {stdout.decode()}")  # Decode bytes to string
            print(f"Stderr: {stderr.decode()}")
            return False

    except FileNotFoundError:
        print(f"Error: Adept.exe/adobeactivate.exe not found at: {adobecmd_path}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False



# Example usage:
if __name__ == "__main__":
    # Replace "your_acsm_file.acsm" with the actual path to your ACSM file.
    acsm_file_path = "your_acsm_file.acsm"  # Example: "./my_book.acsm"

    # (Optional) Specify the desired output PDF path. If None, it will be created in the same directory.
    output_pdf_path = "your_output_pdf.pdf" # Example:  "./my_book.pdf"  or None

    # (Optional) Specify the path to Adept.exe or adobeactivate.exe if it's not in the default location.
    adept_path = None # Example: "C:\\Program Files (x86)\\Adobe\\Adobe Digital Editions\\Adept.exe"

    success = convert_acsm_to_pdf(acsm_file_path, output_pdf_path, adept_path)

    if success:
        print("ACSM to PDF conversion completed successfully.")
    else:
        print("ACSM to PDF conversion failed.")
