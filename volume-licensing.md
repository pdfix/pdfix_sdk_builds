# PDFix SDK Volume Licensing

- [PDFix SDK Volume Licensing](#pdfix-sdk-volume-licensing)
  - [Volume Licensing Plans](#volume-licensing-plans)
  - [License Deployment](#license-deployment)
    - [Deployment to Computers with Internet Connection](#deployment-to-computers-with-internet-connection)
    - [Deployment to Computers without Internet Connection](#deployment-to-computers-without-internet-connection)
  - [Page Counting](#page-counting)
  - [Which Functions Count Pages](#which-functions-count-pages)
    - [List of Functions Using Layout Analysis:](#list-of-functions-using-layout-analysis)
    - [List of CLI Commands Using Layout Analysis:](#list-of-cli-commands-using-layout-analysis)
  - [Using the license with PDFix SDK](#using-the-license-with-pdfix-sdk)
    - [Standard License Activation](#standard-license-activation)
      - [Online Activation](#online-activation)
      - [Offline activation](#offline-activation)
    - [Deactivating the standard license](#deactivating-the-standard-license)
      - [Online deactivation](#online-deactivation)
      - [Offline deactivation](#offline-deactivation)
    - [Updating the standard license](#updating-the-standard-license)
    - [Reading the license status](#reading-the-license-status)
    - [Local License File Storage](#local-license-file-storage)

## Volume Licensing Plans

Volume licensing allows users to set up flexible plans based on the number of processed pages. Volume licensing is applicable to PDFix SDK Professional and Enterprise.

The default plans offered are 2,000, 5,000, 10,000, 30,000 or more pages per month. For higher volumes, a custom or flat-rate license can be arranged upon request.

- Once the page limit is hit, the the SDK returns error 428, "Consupmtion limit reached."
- Page counter resets to zero every month
- Exceeding the limits is not allowed by default, but can be set upon request

For any inquiries, please contact us at support@pdfix.net.

## License Deployment

The deployment of the SDK affects the available license types.

### Deployment to Computers with Internet Connection

- Unlimited number of activated devices
- Allows operation on multiple computers simultaneously
- The total page count is aggregated from all computers
- Remote license updates (e.g., when changing the plan)

### Deployment to Computers without Internet Connection

- Allows one license to run on a single computer
- License activation and updates require exchanging an activation file

*Note: Deployment of the software in offline environments can be managed using a license management server within your local network. Such deployment may involve additional charges.*

## Page Counting

The SDK counts only pages processed with layout recognition. The total number of processed pages increases when saving the document. Once the document is closed, the counters reset.

**Example for an 8-page document:**
- Auto-tagging the whole document and saving increases the counter by 8 pages. Re-tagging the same opened document does not count additional pages.
- Auto-tagging, saving, and closing the document increases the counter by 8 pages. Re-opening and re-tagging the document counts another 8 pages.

- Document editing that does not involve functions below has no affect on page counting. 

## Which Functions Count Pages

Layout analysis is executed using the object `PdePageMap`. Any process operating with this object counts pages.

### List of Functions Using Layout Analysis:
- `PdePageMap.CreateElements()`
- `PdfPage.AddTags()`             *enterprise only*
- `PdfDoc.AddTags()`              *enterprise only*
- `PdfHtmlConversion.Save()`      *when converting to a responsive HTML layout*
- `PdfJsonConversion.Save()`      *when converting a page map*
- `PsCommand.Run()`               *when the action `add_tags` is used*

### List of CLI Commands Using Layout Analysis:
- `pdfix_app add-tags`
- `pdfix_app batch` *when the actions `add_tags`, `tag_as` is used*

## Using the license with PDFix SDK

Volume licensing, also known as a standard license, is handled by the SDK using a `PsStandardAuthorization` object.

### Standard License Activation
Software can be authorized using an activation key. After activating the software operates on the computer according to the license. 

#### Online Activation

Software can be activated using an activation key. Once activated, the software operates under the assigned license on the respective computer.

Command-line usage:
```
$ ./pdfix_app license --activate XXXX-XXXX-XXXX-XXXX
```

Using the code:
```python
GetPdfix().GetStandardAuthorization().Activate("XXXX-XXXX-XXXX-XXXX")
```

Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseActivate.cpp), [c#](https://github.com/pdfix/pdfix_sdk_example_dotnet/blob/master/src/Initialization.cs), [Python](https://github.com/pdfix/pdfix_sdk_example_python/blob/master/src/License.py)

_Note to PHP users: Depending on the configuration the PHP may operate in a safe mode under a virtual user (e.g. www-data). In such a case the license should be activated separately with PHP._

#### Offline activation 
**Step 1:** Create activation request file

Command-line usage:
```
./pdfix_app license --activate XXXX-XXXX-XXXX-XXXX --request --license-path license.req
```

Using the code:
```python
GetPdfix().GetStandardAuthorization().CreateOfflineActivationFile("XXXX-XXXX-XXXX-XXXX", "path/to/license.req")
```

Code examples: 
- c++ [request activation file](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseCreateOfflineActivationFile.cpp)

**Step 2:** Upload the `license.req` file to [PDFix Offline Licensing](https://pdfix.net/offline-licensing/) to generate a license activation file. You receive a `license.lic` upon submission and follow to the next step.

**Step 3:** Activate the license from file
Command-line usage:
```
./pdfix_app license --activate XXXX-XXXX-XXXX-XXXX --license-path license.lic
```
Using the code:
```python
GetPdfix().GetStandardAuthorization().ActivateOffline("path/to/license.response")
```

Code examples: 
- c++ [activate offline](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseActivateOffline.cpp)

### Deactivating the standard license
Note: When transferring a license to another computer, it must first be deactivated.

#### Online deactivation
Command-line usage:
```
$ ./pdfix_app license --deactivate
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseDeactivate.cpp)

#### Offline deactivation
Using the CLI:
```
$ ./pdfix_app license --deactivate --license-path deactivate.req
```

Using the code:
```python
GetPdfix().GetStandardAuthorization().Deactivate()
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseDeactivateOffline.cpp), [Python](https://github.com/pdfix/pdfix_sdk_example_python/blob/master/src/License.py)

### Updating the standard license
The license is updated automatically when running the software. When an instant update is needed the following command should be executed:

Command-line usage:
```
$ ./pdfix_app license --update
```

Using the code:
```python
GetPdfix().GetStandardAuthorization().Update()
```
Code example: [c++](https://github.com/pdfix/pdfix_sdk_example_cpp/blob/master/src/StandardLicenseUpdate.cpp)

### Reading the license status
Users can read the license status anytime using special commands. The license status is provided as a JSON file.

Command-line usage:
```
$ ./pdfix_app license --status
```

Using the code:
```python
GetPdfix().GetStandardAuthorization().SaveToStream(mem_stm, kDataFormatJson)
```
Code example: [Python](https://github.com/pdfix/pdfix_sdk_example_python/blob/master/src/License.py)

The example status:
```
{
    "product": {
        "name": "PDFix SDK",
        "option": "Enterprise",
        "version": "8.4.0"
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
        "expiration_date": "2024-01-09",
        "days_since_last_check": "1",
        "pages": {
            "type": "2",
            "max_consumption": "30000",
            "total_consumption": "3024",
            "local_consumption": "5"
        },
        "enterprise": {
            "type": "1"
        }
    }
}
```

### Local License File Storage
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
Command-line usage:
```
$ ./pdfix_app [SUBCOMMAND] [OPTIONS] --settings-path <path_to_json>
```

