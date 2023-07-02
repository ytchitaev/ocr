# Image OCR with pytesseract

This project demonstrates how to use pytesseract to perform Optical Character Recognition (OCR) on images in a given directory and save the extracted text to corresponding text files.

## Prerequisites

- Python 3.x
- Tesseract OCR engine installed and accessible from the command line
  - Download Tesseract from the official GitHub repository: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
  - Make sure to add Tesseract to your system's PATH environment variable

## Use

1. Clone the repository or download the project files.
2. `create_venv.ps1` to create venv from requirements
3. Set `env.ini` to specify the arguments, if not found uses default
4. `run_venv.ps1` to run `run_ocr.exe` from venv
5. `build_exe.ps1` to build exe from `run_ocr.py`

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
