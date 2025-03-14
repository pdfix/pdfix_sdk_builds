# Getting Started with PDFix SDK

PDFix SDK is a cross-platform PDF processing tool that offers multiple integration options.
The Command-Line Interface ([PDFix CLI](#integration-using-the-cli)) provides a quick and easy way to add PDF processing functionality to various workflows without writing code.

Developers can leverage the SDK with different [programming languages](#integration-using-the-sdk) for full control over PDF documents.

Before getting started, check the [system requirements](#prerequisites) to ensure compatibility with your system.

## Integration Using the CLI

PDFix offers straightforward, rapid, and automated PDF processing via the command-line interface:

```console
$ ./pdfix_app make-accessible -i test.pdf -o output.pdf
```

For additional CLI options, refer to the [PDFix SDK Command-Line Interface documentation](https://pdfix.net/support/pdfix-command-line/). The CLI application is included in the downloadable package available on the [PDFix website](https://pdfix.net/download/).

## Integration the SDK programatically

To integrate the PDFix SDK programmatically, refer to the code examples on GitHub for your preferred programming language:

- [C++](https://github.com/pdfix/pdfix_sdk_example_cpp) – Native applications
- [.NET](https://github.com/pdfix/pdfix_sdk_example_dotnet) – For .NET Framework, .NET Core, and .NET 5+
- [Java](https://github.com/pdfix/pdfix_sdk_example_java) – For Maven or Gradle projects
- [Python](https://github.com/pdfix/pdfix_sdk_example_python) – Applications
- [JavaScript](https://github.com/pdfix/pdfix_sdk_example_npm) – For frameworks like Node.js, React.js, Angular, and similar

## How to

### Fix Accessibility Issues

To fix PDF/UA compliance issues in a PDF document use methods available in:

- **PDFix Actions for Accessibility** - a flexible pdf manipulation without coding 
- **SDK API methods** to access and edit
  - Structure Tree and its Elements
  - Page Objects and their Content Marks
  - Annotations
  - Document Metadata

### Extract PDF Content

To extract the data from a PDF document a conversion to JSON. The data extraction can methods can provide:

- **Raw Document Extraction** to access
  - Document Metadata, Form Fields, and classification such as tagged, signed, secured
  - Page Size, Rotation, Annotations, Content including text content, images, positions, colors
- **Layout Recognition** to access the logical content such as
  - Paragraphs, Headings, Figures, Tables, Headers, Footers
  - 
- **Document Structure Tags** to access
  - Complete document structure tree with element properties, attributes, position, and content




## Multi-Threaded Environments

PDFix SDK operates in a single-threaded manner, allowing only one API method to run at a time within a single process. Any additional method calls from other threads will be queued until the current operation finishes.

For parallel processing, use separate processes rather than threads.

## Licensing

- For volume licensing, refer to [Volume Licensing](https://github.com/pdfix/pdfix_sdk_builds/blob/main/volume-licensing.md).
- For high-volume or custom licensing, contact us at **support@pdfix.net**.

### Trial/Lite License Limitations

- Extracted text may include randomly replaced characters with "*".
- Saved PDFs may contain redacted content with watermark.

## Prerequisites

- **Windows**: Windows 7 and newer, Windows Server 2016 and newer (_Requires the latest [Microsoft Visual C++ Redistributable for Visual Studio 2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)_)  
- **macOS**: macOS 10.15 and newer  
- **Linux**: Ubuntu 16.04 and newer, Debian 10 and newer, CentOS 8 and newer  

## Support

For any questions, visit our [Support Page](https://pdfix.net/support).
