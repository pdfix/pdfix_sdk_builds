# Getting started with PDFix SDK

PDFix SDK is a cross-platform PDF processing tool, that offers various ways of the integration. 
A Command-line interface [PDFix CLI](#Integration-using-the-CLI) is a quick and easy way to add PDF processing functionality into various workflows without coding.

Developers can use the PDFix SDK with [programming languages](#Integration-using-the-SDK) to take advandatage of the full control over the PDF documents.

Check the [system requirements](#Prerequisites) to avoid any problems with running PDFix SDK on your system. 

## Integration using the CLI
PDFix provides simple, fast and automated PDF processing through the
command-line. PDFix CLI is the easiest way to integrate the PDFix SDK
functionality into your solutions.

```console
$ ./pdfix_app make-accessible -i test.pdf -o output.pdf --preflight
```

For more CLI options please check the [PDFix SDK Command-line interface](https://pdfix.net/support/pdfix-command-line/).

## Integration using the SDK

### c&#35; 
Import NuGet package [PDFix.SDK](https://www.nuget.org/packages/PDFix.SDK/)
```cs
using PDFixSDK.Pdfix;

static void Main() {
   var pdfix = new Pdfix();
   var doc = pdfix.OpenDoc("Sample.pdf", "");
   // do your stuff
   doc.Close();                                       
}
```
Check the full github sample [https://github.com/pdfix/pdfix_sdk_example_dotnet](https://github.com/pdfix/pdfix_sdk_example_dotnet)

### c++
```cpp

#include "Pdfix.h"

Pdfix_statics;

int main() {
   if (Pdfix_init(Pdfix_MODULE_NAME))) {
      auto pdfix = GetPdfix();
      auto doc = pdfix->OpenDoc(L"Sample.pdf", L"");
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
   System.loadLibrary("pdfix");                       
   Pdfix pdfix = new Pdfix();   
   PdfDoc doc = pdfix.OpenDoc("Sample.pdf", "");      
   // do your stuff
   doc.Close();
}
``````
Check the full github sample [https://github.com/pdfix/pdfix_sdk_example_java](https://github.com/pdfix/pdfix_sdk_example_java)

### python
Import Python Package [pdfix-sdk](https://pypi.org/project/pdfix-sdk/)

```python
from pdfixsdk.Pdfix import *

pdfix  = GetPdfix()
doc = pdfix.OpenDoc("Sample.pdf", "")
// do your stuff
doc.close()
```
Check the full github sample [https://github.com/pdfix/pdfix_sdk_example_python](https://github.com/pdfix/pdfix_sdk_example_python)


## Prerequisites
- Windows 7, Windows Server 2016 (_The latest [Microsoft Visual C++ Redistributable for Visual Studio
2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)_)
- macOS 10.15+
- Ubuntu 16.04+, CentOS 8+

## Trial/Lite license limitations
- Methods extracting text from the PDF content randomly replace characters with "*"
- Rasterized images may contain logo watermark
- Saved PDFs may have redacted parts of the content 

## License Management
PDFix SDK can be autorized using an activation key or using the name, key pair.

### Standard License Activation
Software can be authorized using an activation key. After activating the software operates on the computer according to the license. Internet connection is necessary for occasional license updates.

Command line example:
```
$ ./pdfix_app license --activate XXXX-XXXX-XXXX-XXXX
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseActivate.cpp), [c#](https://github.com/pdfix/pdfix_sdk_example_dotnet/blob/master/src/Initialization.cs)

_Note to PHP users: Depending on the configuration the PHP may operate in a safe mode under a virtual user (e.g. www-data). In such a case the license should be activated separately with PHP._

### Deactivating the standard license
When moving license to another computer the license should be deactivated.

Command line example:
```
$ ./pdfix_app license --deactivate
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseDeactivate.cpp)


### License file local storage
The activated license information is stored on computer under the current user account. The default local license storage is in the following directories:

- Windows: `<user>\AppData\Local\.pdfixsdk`
- MacOS: `<user>/Library/Application Support/.pdfixsdk`
- Linux: `<user>/.pdfixsdk`

Custom location can be set by setting the license data path and file name in the settings JSON as follows:

```
{
    "user": {
        "license_data_path" : "<local_folder>",
        "license_file_name" : "MyLicenseLey.txt"
    }
}
```
Command-line use:
```
$ ./pdfix_app [SUBCOMMAND] [OPTIONS] --settings-path <path_to_json>
```

### Updating the standard license
The license is updated automatically when running the software. When an instant update is needed the following command should be executed:

Command line example:
```
$ ./pdfix_app license --update
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseUpdate.cpp)

### Account license authorization
Software can be authorized using a name and key. The name key pair should be used every time the PDFix SDK is used. 

Command line example:
```
$ ./pdfix_app extract-data --input test.pdf --email your@email --key XXXXXXXXXXXXXX
```
Code example: [c#](https://github.com/pdfix/pdfix_sdk_example_dotnet/blob/master/src/Initialization.cs)

### License Status
The current license status can be saved into JSON.

Command line example:
```
$ ./pdfix_app license --status 
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/LicenseStatus.cpp)

Satus output:
```
{
    "product": {
        "name": "PDFix SDK",
        "option": "Enterprise",
        "version": "6.4.0"
    },
    "status": {
        "authorized": "true"
    },
    "license": {
        "type": "standard",
        "active": "true",
        "key": "XXXX-XXXX-XXXX-XXXX",
        "max_activations": "5",
        "total_activations": "2",
        "days_remaining": "51",
        "expired": "false",
        "expiration_date": "2021-01-09",
        "days_since_last_check": "1",
        "pages": {
            "type": "2",
            "max_consumption": "300000",
            "total_consumption": "37024",
            "local_consumption": "5"
        },
        "enterprise": {
            "type": "1"
        }
    }
}
```

## Support
In case of any questions please [contact support](https://pdfix.net/support).
