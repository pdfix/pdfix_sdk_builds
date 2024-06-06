PDFix SDK CLI
```
Usage: ./pdfix_app [OPTIONS] [SUBCOMMAND]
```

_Options:_
```
  -h,--help                   Print this help message and exit
  --help-all-md               Show all help in MD format
  -v,--version                
```
## Subcommands

| name | description |
| - | - |
| [`batch`](#batch) | Run commands in a batch. The document is not saved to the output path if a command does not modify it.| 
| [`make-accessible`](#make-accessible) | Makes PDF Accessible. Converts PDF to fully compliant PDF/UA.If you have image-only PDF, please use OCR command before.| 
| [`add-tags`](#add-tags) | Add tags to PDF.| 
| [`extract-data`](#extract-data) | Extract PDF data into JSON/XML| 
| [`pdf2table`](#pdf2table) | Extracts tables detected in the PDF into CSV files.Output should point to the folder where separate CSV files will be saved.| 
| [`pdf2txt`](#pdf2txt) | Extract text from PDF| 
| [`pdf2image`](#pdf2image) | Extract images from PDF| 
| [`extract-highlighted-text`](#extract-highlighted-text) | Extract highlighted text from PDF| 
| [`pdf2html`](#pdf2html) | Converts PDF to HTML , output is the HTML file created duringconversion.  All necessary files generated during the conversion aresaved in the same folder as the output file.| 
| [`preflight`](#preflight) | Preflight document template and output the config| 
| [`ocr`](#ocr) | Converts scans or images-only PDF documents into searchable, editable PDF files.| 
| [`import-data`](#import-data) | Import form data from JSON| 
| [`acroform2json`](#acroform2json) | Extract PDF Form Fields into JSON| 
| [`json2acroform`](#json2acroform) | Import PDF Form Fields from JSON| 
| [`render-page`](#render-page) | Render Page| 
| [`digital-signature`](#digital-signature) | Sign PDF| 
| [`add-comment`](#add-comment) | Add comment to PDF| 
| [`remove-comments`](#remove-comments) | Remove comments from PDF| 
| [`flatten`](#flatten) | Flatten all annotations into the PDF content.| 
| [`embedfonts`](#embedfonts) | Embeds fonts into PDF| 
| [`watermark`](#watermark) | Add watermark to PDF| 
| [`parse-pds-objects`](#parse-pds-objects) | Tag operations on PDF| 
| [`create-document`](#create-document) | Create new PDF| 
| [`create-page`](#create-page) | Create new page in PDF| 
| [`move-page`](#move-page) | Move one page in document| 
| [`delete-pages`](#delete-pages) | Delete pages from PDF| 
| [`insert-pages`](#insert-pages) | Insert pages from PDF to another| 
| [`document-metadata`](#document-metadata) | Get and set document metadata as XML| 
| [`license`](#license) | License related commands| 
| [`pages2json`](#pages2json) | Convert PDF Pages into JSON| 
| [`bmk2json`](#bmk2json) | Convert PDF Bookmarks into JSON| 
| [`tags2json`](#tags2json) | StructTree to JSON| 
| [`content2json`](#content2json) | Page Content to JSON| 
| [`dests2json`](#dests2json) | Extract Named Destivations into JSON| 
### `[Option Group: ]`
Internal commands



_Options:_
```
  -m,--email TEXT             Registration e-mail address
  -k,--key TEXT               License key
  --settings-path TEXT        PDFix SDK settings
  -i,--input TEXT             Input file
  -o,--output TEXT            Output file or replace input file if not set
```


### `batch`
Run commands in a batch. The document is not saved to the output path if a command does not modify it.



_Options:_
```
  -p,--password TEXT          Open password
  -c,--command TEXT           Batch command JSON file
  --progress                  Print out the batch commands progress output if set
```



### `make-accessible`
Makes PDF Accessible. Converts PDF to fully compliant PDF/UA.If you have image-only PDF, please use OCR command before.



_Options:_
```
  --password TEXT             Open password
  -c,--command-path TEXT      Command file path. Default make accessible command will be used if it's empty.
```



### `add-tags`
Add tags to PDF.



_Options:_
```
  --password TEXT             Open password
  -c,--config-path TEXT       Config file path.
  --preflight                 Preflight document template before processing
```



### `extract-data`
Extract PDF data into JSON/XML



_Options:_
```
  --password TEXT             Open password
  -c,--config_path TEXT:FILE  Config file path
  --preflight                 Preflight document template before processing
  -f,--format ENUM:{0,1}      integer value defining the data file output format (0-JSON, 1-XML)
  -p,--page-number INT        the page number from which to extract data, default -1 extracts from all pages
  --doc-info                  extract document general information (metadata, num pages, etc.)
  --doc-outlines              extract document outlines (bookmarks)
  --doc-acroform              extract document forms (AcroForm)
  --doc-struct-tree           extract document structure tree (tags)
  --page-info                 extract page general information (number, crop box, rotation)
  --page-content              extract page objects (raw data)
  --page-map                  scrape page data (logical content extraction)
  --page-annots               extract page annotstions
  --text                      extract page map text elements or content text objects
  --tables                    extract page map tables structure
  --images                    extract page map image elements or page contnet images
  --bbox                      extract element or object bbox
  --text-style                extract text style of text element
  --text-state                extract text state of text object or element
  --graphic-state             extract page object's graphic state
```



### `pdf2table`
Extracts tables detected in the PDF into CSV files.Output should point to the folder where separate CSV files will be saved.





### `pdf2txt`
Extract text from PDF



_Options:_
```
  -c,--config_path TEXT:FILE  Config file path
  -p,--page INT               Page number from which text will be extracted (Default value -1 extract all pages
```



### `pdf2image`
Extract images from PDF



_Options:_
```
  -w,--page-width INT         with of the rendered page in pixels used for scaling the images
  -f,--format ENUM:{1,2}      integer value defining the image output format (0-PNG, 1-JPG)
  -q,--quality INT:INT in [0 - 100]
image quality. For JPG means the compression level otherwise it’s ignored
```



### `extract-highlighted-text`
Extract highlighted text from PDF



_Options:_
```
  -c,--config-path TEXT       path to config file
```



### `pdf2html`
Converts PDF to HTML , output is the HTML file created duringconversion.  All necessary files generated during the conversion aresaved in the same folder as the output file.



_Options:_
```
  --password TEXT             Open password
  -c,--config-path TEXT       path to config file.
  -w,--page-width INT         Page width
  -a,--append-html TEXT       Append HTML code from file
  --preflight                 Preflight document template before processing
  --export-js                 exports document JavaScript into HTML.
  --text-size                 retain original text size in created HTML.
  --text-color                page number from which image will be created.
  --no-external               use inline css, js and embeded images and fonts.
  --no-external-css           use inline css instead of the external file.
  --no-external-js            use inline javascript instead of the external file.
  --no-external-img           use embedded based encoded images.
  --no-external-font          use embedded based encoded fonts.
  --gray-background           use gray background and page padding.
  --no-page-render            do not render page.
  --responsive                creates responsive HTML, creates fixed layout if not set.
  --derivation                creates HTML derived from PDF tags.
  --export-fonts Needs: --responsive
exports embedded TrueType fonts into HTML using CSS3.
  --format ENUM:{1,2}         integer value defining the image output format (0-PNG, 1-JPG)
  --quality INT:INT in [0 - 100]
integer value defining the image output quality (0-100)
  -j,--js                     
  -s,--css                    
  -d,--doc                    
  -p,--page INT               
```



### `preflight`
Preflight document template and output the config



_Options:_
```
  -f,--format ENUM:{0,1}      integer value defining the data file output format (0-JSON, 1-XML)
```



### `ocr`
Converts scans or images-only PDF documents into searchable, editable PDF files.



_Options:_
```
  -l,--lang TEXT              OCR language
  -d,--data-path TEXT:DIR     path to Tesseract ORC data.
```



### `import-data`
Import form data from JSON



_Options:_
```
  --password TEXT             Open password
  -j,--json-path TEXT:FILE    Path to JSON file
  -f,--flatten                Flatten PDF
```



### `acroform2json`
Extract PDF Form Fields into JSON



_Options:_
```
  --password TEXT             Open password
  --widgets                   include information about the form field annotations - widgets.
```



### `json2acroform`
Import PDF Form Fields from JSON



_Options:_
```
  -j,--json-path TEXT:FILE    Path to JSON file
```



### `render-page`
Render Page



_Options:_
```
  -f,--format ENUM:{1,2}      integer value defining the image output format (0-PNG, 1-JPG)
  -r,--rotate ENUM:{0,90,180,270}
page rotation in degrees
  --password TEXT             Open password
  -p,--page-number INT        page number from which image will be created.
  -l,--left INT               integer value specifying the page left of the clipping region in device units
  -t,--top INT                integer value specifying the page top of the clipping region in device units
  -w,--width INT              integer value specifying the width of the page left clipping region in device units
  -g,--height INT             integer value specifying the height of the page left clipping region in device units
  -q,--quality INT:INT in [0 - 100]
integer value defining the image output quality (0-100)
  -z,--zoom FLOAT             floating point number of zoom level
```



### `digital-signature`
Sign PDF



_Options:_
```
  -x,--pfx-path TEXT:FILE     Path to .pfx file with signature.
  -p,--pfx-password TEXT      Password for .pfx file.
```



### `add-comment`
Add comment to PDF





### `remove-comments`
Remove comments from PDF





### `flatten`
Flatten all annotations into the PDF content.





### `embedfonts`
Embeds fonts into PDF





### `watermark`
Add watermark to PDF



_Options:_
```
  -m,--image-path TEXT:FILE   Path to image file used for watermark
  -s,--start-page INT         First page where the watermark is placed [0].
  -e,--end-page INT           Last page where the watermark is placed [last page].
  --order-top INT:NUMBER      Control watermark z-order (0-bottom, [1]-top)
  --percentage                Use percentage values instead of points
  --h-align ENUM:{1,2,3,6}:NUMBER
Horizontal alignment ([1]-left, 2-right, 3-justify, 6-center)
  --v-align ENUM:{4,5,6}:NUMBER
Vertical alignment ([4]-top, 5-bottom, 6-center)
  --h-value FLOAT:NUMBER      Horizontal image offset [0]
  --v-value FLOAT:NUMBER      Vertical image offset [0]
  --scale FLOAT:NUMBER        Image scale [1]
  --rotation FLOAT:NUMBER     Image counter-clockwise rotation in degrees [0]
  --opacity FLOAT:NUMBER      Image opacity [1]
```



### `parse-pds-objects`
Tag operations on PDF



_Options:_
```
  --password TEXT             Open password
```



### `create-document`
Create new PDF





### `create-page`
Create new page in PDF



_Options:_
```
  -p,--after-page INT         page number after which the new page will be inserted.
```



### `move-page`
Move one page in document



_Options:_
```
  -f,--from INT               page number of the page to move
  -t,--to INT                 new location of the page to move.
```



### `delete-pages`
Delete pages from PDF



_Options:_
```
  -f,--from INT               page number of first page to delete.
  -t,--to INT                 page number of the last page to delete.
```



### `insert-pages`
Insert pages from PDF to another



_Options:_
```
  -s,--src TEXT:FILE          Source file
  -a,--after INT              Page number after which pages will be inserted
  -f,--from INT               Page number of first page to insert
  -t,--to INT                 Page number of the last page to insert
```



### `document-metadata`
Get and set document metadata as XML



_Options:_
```
  -x,--xml-path TEXT          Path to .xml file with metadata.
```



### `license`
License related commands



_Options:_
```
  -a,--activate TEXT          activate license using the key online or offline if --license-path is set, or request activation if --request-path is set
  --request                   create activation request, --license-path should be set to write request to, used only in combination with --activate
  --license-path TEXT         path to a license file
  -d,--deactivate             deactivate license online, for offline deactivation --license-path should be set
  -u,--update                 update license online, for offline update --license-path should be set
  -s,--status                 print license status
  -r,--reset                  reset local license
```



### `pages2json`
Convert PDF Pages into JSON



_Options:_
```
  --password TEXT             Open password
  -p,--page-number INT        page number, [0] default all pages)
  --text                      exports page text
```



### `bmk2json`
Convert PDF Bookmarks into JSON



_Options:_
```
  --password TEXT             Open password
```



### `tags2json`
StructTree to JSON





### `content2json`
Page Content to JSON



_Options:_
```
  -p,--page-number INT        page number.
```



### `dests2json`
Extract Named Destivations into JSON



_Options:_
```
  --password TEXT             Open password
```



