# Getting started with PDFix SDK

PDFix SDK is a cross-platform PDF processing tool, that offers various ways of the integration. 
A Command-line interface [PDFix CLI](#Integration-using-the-CLI) is a quick and easy way to add PDF processing functionality into various workflows without coding.

Developers can use the PDFix SDK with [programming languages](#Integration-using-the-SDK) to take advandatage of the full control over the PDF documents.

Check the [system requirements](#Prerequisites) to avoid any problems with running PDFix SDK on your system. 

## Integration using the CLI
PDFix offers straightforward, rapid, and automated PDF processing via the command-line interface. 


```console
$ ./pdfix_app make-accessible -i test.pdf -o output.pdf
```

For more CLI options please check the [PDFix SDK Command-line interface](https://pdfix.net/support/pdfix-command-line/). The CLI application is part of the downloadable package available on [website](https://pdfix.net/download/).


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
Check more github examples on [https://github.com/pdfix/pdfix_sdk_example_dotnet](https://github.com/pdfix/pdfix_sdk_example_dotnet)

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
Check more github examples on [https://github.com/pdfix/pdfix_sdk_example_cpp](https://github.com/pdfix/pdfix_sdk_example_cpp)

### java
```java
import net.pdfix.pdfixlib.*;

public static void main() {
   Pdfix pdfix = new Pdfix();   
   PdfDoc doc = pdfix.OpenDoc("Sample.pdf", "");      
   // do your stuff
   doc.Close();
}
``````
Check more github examples on [https://github.com/pdfix/pdfix_sdk_example_java](https://github.com/pdfix/pdfix_sdk_example_java)

### python
Import Python Package [pdfix-sdk](https://pypi.org/project/pdfix-sdk/)

```python
from pdfixsdk import *

pdfix  = GetPdfix()
doc = pdfix.OpenDoc("Sample.pdf", "")
// do your stuff
doc.close()
```
Check more github examples on [https://github.com/pdfix/pdfix_sdk_example_python](https://github.com/pdfix/pdfix_sdk_example_python)

## Multi-threaded environments

The SDK is designed for single-threaded processing, meaning only one API method can be executed at a time within a single process. Any methods invoked from other threads will wait until the preceding one completes.

If there's a need to handle multiple concurrent calls, it's advised to utilize separate processes instead.


## Prerequisites
- Windows 7 and newer, Windows Server 2016 and newer (_The latest [Microsoft Visual C++ Redistributable for Visual Studio
2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)_)
- macOS 10.15 and newer
- Ubuntu 16.04 and newer, Debian 10 and newer, CentOS 8 and newer

## Trial/Lite license limitations
- Methods extracting text from the PDF content randomly replace characters with "*"
- Rasterized images may contain logo watermark
- Saved PDFs may have redacted parts of the content 

## License Management
PDFix SDK can be autorized using an activation key or using the name, key pair.

### Standard License Activation
Software can be authorized using an activation key. After activating the software operates on the computer according to the license. Internet connection is necessary for occasional license updates.

#### Online Activation
Using the command line:
```
$ ./pdfix_app license --activate XXXX-XXXX-XXXX-XXXX
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseActivate.cpp), [c#](https://github.com/pdfix/pdfix_sdk_example_dotnet/blob/master/src/Initialization.cs), [Python](https://github.com/pdfix/pdfix_sdk_example_python/blob/master/src/License.py)

_Note to PHP users: Depending on the configuration the PHP may operate in a safe mode under a virtual user (e.g. www-data). In such a case the license should be activated separately with PHP._

#### Offline activation 
**Step 1:** Create activation request file
```
./pdfix_app license --activate XXXX-XXXX-XXXX-XXXX --request --license-path license.req
```
**Step 2:** Upload the `license.req` file to https://pdfix.net/offline-licensing/ to create a license activation file. You receive a `license.lic` upon submission and follow to the next step.

**Step 3:** Activate the license from file
```
./pdfix_app license --activate XXXX-XXXX-XXXX-XXXX --license-path license.lic
```

Code examples: (follow the same steps as with CLI)

[c++](https://github.com/pdfix/pdfix_sdk_example_cpp) samples StandardLicenseCreateOfflineActivationFile.cpp, StandardLicenseActivateOffline.cpp


### Deactivating the standard license
Note: When moving license to another computer the license should be deactivated.

#### Online deactivation
Command line example:
```
$ ./pdfix_app license --deactivate
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseDeactivate.cpp)

#### Offline deactivation
Command line example:
```
$ ./pdfix_app license --deactivate --license-path deactivate.req
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseDeactivateOffline.cpp), [Python](https://github.com/pdfix/pdfix_sdk_example_python/blob/master/src/License.py)


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
