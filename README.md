# Getting started with PDFix SDK
The build contain the libraries with headers and the command line
application(pdfix_app).

## Integration through the CLI
PDFix provides simple, fast and automated PDF processing through the
command-line. PDFix CLI is the easiest way to integrate the PDFix SDK
functionality into your solutions.

Technically the CLI is a an application created with our SDK.  It’s suitable
for system integrators without developer experience who want to integrate PDFix
technology.

## Integration through the SDK
PDFix SDK allows full control of integration and processing. It gives you
access to all SDK features and you have power to fully customise our extraction
and conversion engine.

Have a look at our functional examples to see how easy it is to integrate PDFix
SDK into your project. Speed up development by using our code examples!
Download examples from PDFix GitHub.

## Prerequisites
The latest [Microsoft Visual C++ Redistributable for Visual Studio
2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)
is required for the Windows version.

## Download
- [PDFix SDK with CLI application](https://pdfix.net/download)

## Quick start guide for PDFix CLI (Make Accessible PDF Example)

<img src="http://pdfix.net/img/terminal.gif" width="600">

1. Download the build for your operating system.
2. Extract the content of the .zip file.
3. Go to the folder containing the pdfix_app:

- Linux:  
   `pdfix_sdk_x.x.x_linux/bin/linux`
- MacOS:  
   `pdfix_sdk_x.x.x_linux/bin/darwin`
- Windows 32-bit:  
   `pdfix_sdk_x.x.x_linux/bin/x86`
- Windows 64-bit:  
   `pdfix_sdk_x.x.x_linux/bin/x64`

4. Make accessible PDF with pdfix_app

- Linux:  
   `./pdfix_app make-accessible -i input.pdf -o output.pdf`
- MacOS:  
   `./pdfix_app make-accessible -i input.pdf -o output.pdf`
- Windows:  
   `pdfix_app.exe make-accesible -i input.pdf -o output.pdf`

## Example projects
- [C++](https://github.com/pdfix/pdfix_sdk_example_cpp)
- [.net](https://github.com/pdfix/pdfix_sdk_example_dotnet)
- [Java](https://github.com/pdfix/pdfix_sdk_example_java)
- [Python](https://github.com/pdfix/pdfix_sdk_example_python)

## Documentation
The [changelog](changelog.md) tracks changes in the SDK and the pdfix_app.

- [PDFix CLI documentation](https://pdfix.net/support/pdfix-command-line/) 
