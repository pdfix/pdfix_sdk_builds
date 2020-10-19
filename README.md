# Getting started with PDFix SDK

PDFix SDK is a cross-platform PDF processing tool, that offers various ways of the integration. 
A Command-line interface [PDFix CLI](#Integration-using-the-CLI) is a quick and easy way to add PDF processing functionality into various workflows without coding.

Developers can use the PDFix SDK in various [programming languages](#Integration-using-the-SDK) to take advandatage of the full control over the PDF documents.

Check the [system requirements](#Prerequisites) to avoid any problems.

## Integration using the CLI
PDFix provides simple, fast and automated PDF processing through the
command-line. PDFix CLI is the easiest way to integrate the PDFix SDK
functionality into your solutions.

```console
$ ./pdfix_app make-accessible -i test.pdf -o output.pdf
```

For more CLI options please check the [PDFix SDK Command-line interface](https://pdfix.net/support/pdfix-command-line/).

## Integration using the SDK
PDFix SDK allows full control of integration and processing. It gives you
access to all SDK features and you have power to fully customise our extraction
and conversion engine.

### c#
Import NuGet package [PDFix.SDK](https://www.nuget.org/packages/PDFix.SDK/)
```cs
using PDFixSDK.Pdfix;

static void Main() {
   var pdfix = new Pdfix();                           // load the library
   var doc = pdfix.OpenDoc("Sample.pdf", "");         // open document
   // do your stuff
   doc.Close();                                       
}
```
Check the full github sample [https://github.com/pdfix/pdfix_sdk_example_dotnet](https://github.com/pdfix/pdfix_sdk_example_dotnet)

### c++
```cpp

#include "Pdfix.h"

Pdfix_statics;                                        // static members

int main() {
   if (Pdfix_init(Pdfix_MODULE_NAME))) {              // load the library
      auto pdfix = GetPdfix();
      auto doc = pdfix->OpenDoc(L"Sample.pdf", L"");  // open document
      // do your stuff
      doc->Close();                                   
   }
}
``````
Check the full github sample [https://github.com/pdfix/pdfix_sdk_example_cpp](https://github.com/pdfix/pdfix_sdk_example_cpp)

### java
```java
import net.pdfix.pdfixlib.*;

public static void main() {
   System.loadLibrary("pdfix");                       // load the library
   Pdfix pdfix = new Pdfix();   
   PdfDoc doc = pdfix.OpenDoc("Sample.pdf", "");      // open document
   // do your stuff
   doc.Close();
}
``````
Check the full github sample [https://github.com/pdfix/pdfix_sdk_example_java](https://github.com/pdfix/pdfix_sdk_example_java)

### python
Check the full github sample [https://github.com/pdfix/pdfix_sdk_example_python](https://github.com/pdfix/pdfix_sdk_example_python)


## Prerequisites
Windows 10, Windows Server 2016 (_The latest [Microsoft Visual C++ Redistributable for Visual Studio
2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)_)

macOS 10.15+

Ubuntu 16.04+

## Support
In case of any questions please [contact support](https://pdfix.net/support).
