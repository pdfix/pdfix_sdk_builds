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

## Integration Using the SDK

### C&#35;
To integrate PDFix with C#, install the NuGet package [PDFix.SDK](https://www.nuget.org/packages/PDFix.SDK/):

```cs
using PDFixSDK.Pdfix;

static void Main() {
   var pdfix = new Pdfix();
   var doc = pdfix.OpenDoc("Sample.pdf", "");
   // Perform PDF operations
   doc.Close();                                       
}
```
Find more examples on [GitHub](https://github.com/pdfix/pdfix_sdk_example_dotnet).

### C++

```cpp
#include "Pdfix.h"

Pdfix_statics;

int main() {
   if (Pdfix_init(Pdfix_MODULE_NAME)) {
      auto pdfix = GetPdfix();
      auto doc = pdfix->OpenDoc(L"Sample.pdf", L"");
      // Perform PDF operations
      doc->Close();                                   
   }
}
```
Find more examples on [GitHub](https://github.com/pdfix/pdfix_sdk_example_cpp).

### Java

```java
import net.pdfix.pdfixlib.*;

public static void main() {
   Pdfix pdfix = new Pdfix();   
   PdfDoc doc = pdfix.OpenDoc("Sample.pdf", "");      
   // Perform PDF operations
   doc.Close();
}
```
Find more examples on [GitHub](https://github.com/pdfix/pdfix_sdk_example_java).

### Python
To integrate PDFix with Python, install the package [pdfix-sdk](https://pypi.org/project/pdfix-sdk/):

```python
from pdfixsdk import *

pdfix  = GetPdfix()
doc = pdfix.OpenDoc("Sample.pdf", "")
# Perform PDF operations
doc.close()
```
Find more examples on [GitHub](https://github.com/pdfix/pdfix_sdk_example_python).

## Multi-Threaded Environments

PDFix SDK is designed for single-threaded processing, meaning only one API method can be executed at a time within a single process. Any method calls from other threads will wait until the preceding one completes.

For concurrent processing, use separate processes instead of threads.

## Prerequisites

- **Windows**: Windows 7 and newer, Windows Server 2016 and newer (_Requires the latest [Microsoft Visual C++ Redistributable for Visual Studio 2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)_)  
- **macOS**: macOS 10.15 and newer  
- **Linux**: Ubuntu 16.04 and newer, Debian 10 and newer, CentOS 8 and newer  

## Trial/Lite License Limitations

- Extracted text may have randomly replaced characters with "*".
- Rasterized images may contain a watermark.
- Saved PDFs may have redacted content.

## License Management

For volume licensing, refer to [Volume Licensing](https://github.com/pdfix/pdfix_sdk_builds/blob/main/volume-licensing.md).
For high-volume or custom licensing, contact us at **support@pdfix.net**.

## Support

For any questions, visit our [Support Page](https://pdfix.net/support).

