## Conversion

### PDF to HTML
`pdf_to_html`

Convert PDF to HTML
#### params:

- `input_pdf` (file_path) __Input PDF__ - Input PDF file path

- `output_html` (file_path) __Ouput HTML file path__ - Define the output HTML Index file

- `html_type` (int) __HTML Layout__ - HTML layout type

  - __0__ - Original layout
  - __1__ - Responsive layout
  - __2__ - Layout defined by PDF Tags


- `template` (file_path) __Template__ - Load the template from the file as the current template. If the file is empty, the default template will be used

- `preflight` (bool) __Preflight__ - Preflight the document and combine the preflight values with the current template

- `flags` (flag) __Conversion Flags__ - Define conversion flags

  - __1__ - Export JavaScripts
  - __2__ - Export fonts
  - __4__ - Default font sizes
  - __8__ - Retain text color
  - __32__ - Inline CSS
  - __64__ - Inline JavaScript
  - __128__ - Embed images
  - __256__ - Embed fonts
  - __512__ - Gray padding


#### example:
```
{
    "name": "pdf_to_html"
}
```
### PDF to JSON
`pdf_to_json`

Convert PDF to JSON
#### params:

- `input_pdf` (file_path) __Input PDF__ - Input PDF file path

- `output_json` (file_path) __Output JSON file path__ - Define the output JSON file

- `flags` (flags) __Conversion Flags__ - Flags specifying the extracted content

  - __1__ - Export Basic Document Information
  - __2__ - Export Basic Page Information
  - __16__ - Export page content
  - __32__ - Export document structure tree
  - __64__ - Export document layout recognition PageMap
  - __256__ - Export object bounding box
  - __512__ - Export page object marks when available
  - __4096__ - Export text for all exported text objects
  - __8192__ - Export text style when available
  - __16384__ - Export text state from  the page content
  - __65536__ - Export base64 encoded images


#### example:
```
{
    "name": "pdf_to_json"
}
```
