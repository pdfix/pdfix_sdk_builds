# PDFix Command-Line

## Usage: `./pdfix_app [OPTIONS] [SUBCOMMAND]`

_Options:_
```
  -h,--help                   Print this help message and exit
  --help-all-md               Show all help in MD format
  -l,--log-level              
  -v,--version                
```
## Subcommands

name | description
--- | ---
[`render-page`](#render-page) | Render Page
[`watermark`](#watermark) | Add watermark to PDF
[`embedfonts`](#embedfonts) | Embeds fonts into PDF
[`extract-highlighted-text`](#extract-highlighted-text) | Extract highlighted text from PDF
[`add-comment`](#add-comment) | Add comment to PDF
[`remove-comments`](#remove-comments) | Remove comments from PDF
[`document-metadata`](#document-metadata) | Get and set document metadata as XML
[`digital-signature`](#digital-signature) | Sign PDF
[`create-page`](#create-page) | Create new page in PDF
[`create-document`](#create-document) | Create new PDF
[`move-page`](#move-page) | Move one page in document
[`delete-pages`](#delete-pages) | Delete pages from PDF
[`pages2json`](#pages2json) | Convert PDF Pages into JSON
[`pdf2json`](#pdf2json) | Convert PDF into JSON
[`bmk2json`](#bmk2json) | Convert PDF Bookmarks into JSON
[`acroform2json`](#acroform2json) | Extract PDF Form Fields into JSON
[`json2acroform`](#json2acroform) | Import PDF Form Fields from JSON
[`pdf2xml`](#pdf2xml) | Convert PDF into XML
[`flatten`](#flatten) | Flatten all annotations into the PDF content.
[`make-accessible`](#make-accessible) | Makes PDF Accessible. Converts PDF to fully compliant PDF/UA.If you have image-only PDF, please use OCR command before.
[`add-tags`](#add-tags) | Add tags to PDF.
[`pdf2table`](#pdf2table) | Extracts tables detected in the PDF into CSV files.Output should point to the folder where separate CSV files will be saved.
[`pdf2txt`](#pdf2txt) | Extract text from PDF
[`pdf2image`](#pdf2image) | Extract images from PDF
[`ocr`](#ocr) | Converts scans or images-only PDF documents into searchable, editable PDF files.
[`pdf2html`](#pdf2html) | Converts PDF to HTML , output is the HTML file created duringconversion.  All necessary files generated during the conversion aresaved in the same folder as the output file.
[`license`](#license) | License related commands
[`tagged-pdf`](#tagged-pdf) | Convert Tagged PDF
[`tags2json`](#tags2json) | StructTree to JSON
[`import-data`](#import-data) | Import form data from JSON
[`content2json`](#content2json) | Page Content to JSON
[`parse-pds-objects`](#parse-pds-objects) | Tag operations on PDF
[`dests2json`](#dests2json) | Extract Named Destivations into JSON
[`test`](#test) | test commands
[`create-documents`](#create-documents) | Create new PDF files
[`render-pages`](#render-pages) | Render Pages
[`redact`](#redact) | Redact content using all redaction annotations.

### `[Common Options: ]`

Internal commands



_Options:_
```
  -m,--email TEXT             Registration e-mail address
  -k,--key TEXT               License key
```


### `render-page`
Render Page


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -f,--format ENUM:{0,1}      integer value defining the image output format (0-PNG, 1-JPG)
  -r,--rotate ENUM:{0,90,180,270}
page rotation in degrees
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -p,--page-number INT        page number from which image will be created.
  -l,--left INT               integer value specifying the page left of the clipping region in device units
  -t,--top INT                integer value specifying the page top of the clipping region in device units
  -w,--width INT              integer value specifying the width of the page left clipping region in device units
  -g,--height INT             integer value specifying the height of the page left clipping region in device units
  -q,--quality INT:INT in [0 - 100]
integer value defining the image output quality (0-100)
  -z,--zoom FLOAT             floating point number of zoom level
```



### `watermark`
Add watermark to PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -s,--start-page INT         First page where the watermark is placed [0].
  -e,--end-page INT           Last page where the watermark is placed [last page].
  -p,--pages ENUM:{0,1,2}:NUMBER
Page range type ([0]-All pages, 1-Even, 2-Odd)
  -m,--image-path TEXT:FILE   Path to image file used for watermark
  --order-top INT:NUMBER      Control watermark z-order (0-bottom, [1]-top)
  --percentage                Use percentage values instead of points
  --h-align ENUM:{1,2,3,6}:NUMBER
Horizontal alignment ([1]-left, 2-right, 3-justify, 6-center)
  --v-align ENUM:{4,5,6}:NUMBER
Vertical alignment ([4]-top, 5-bottom, 6-center)
  --h-value FLOAT:NUMBER      Horizontal image offset
  --v-value FLOAT:NUMBER      Vertical image offset
  --scale FLOAT:NUMBER        Image scale [1]
  --rotation FLOAT:NUMBER     Image rotation in degrees [0]
  --opacity FLOAT:NUMBER      Image opacity [1]
```



### `embedfonts`
Embeds fonts into PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `extract-highlighted-text`
Extract highlighted text from PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -c,--config-path TEXT       path to config file
```



### `add-comment`
Add comment to PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `remove-comments`
Remove comments from PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `document-metadata`
Get and set document metadata as XML


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -x,--xml-path TEXT          Path to .xml file with metadata.
```



### `digital-signature`
Sign PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -x,--pfx-path TEXT:FILE     Path to .pfx file with signature.
  -p,--pfx-password TEXT      Password for .pfx file.
```



### `create-page`
Create new page in PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -p,--after-page INT         page number after which the new page will be inserted.
```



### `create-document`
Create new PDF


_Positionals:_
```
  output TEXT                 Output file
```


_Options:_
```
  -o,--output TEXT            Output file
```



### `move-page`
Move one page in document


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -f,--from INT               page number of the page to move
  -t,--to INT                 new location of the page to move.
```



### `delete-pages`
Delete pages from PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -f,--from INT               page number of first page to delete.
  -t,--to INT                 page number of the last page to delete.
```



### `pages2json`
Convert PDF Pages into JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file or application output
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file or application output
  -p,--page-number INT        page number, [0] default all pages)
  --text                      exports page text
```



### `pdf2json`
Convert PDF into JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -c,--config_path TEXT:FILE  Config file path
```



### `bmk2json`
Convert PDF Bookmarks into JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file or stream
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file or stream
```



### `acroform2json`
Extract PDF Form Fields into JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  --widgets                   include information about the form field annotations - widgets.
```



### `json2acroform`
Import PDF Form Fields from JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output PDF file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output PDF file
  -j,--json-path TEXT:FILE    Path to JSON file
```



### `pdf2xml`
Convert PDF into XML


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -c,--config_path TEXT:FILE  Config file path
```



### `flatten`
Flatten all annotations into the PDF content.


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `make-accessible`
Makes PDF Accessible. Converts PDF to fully compliant PDF/UA.If you have image-only PDF, please use OCR command before.


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -c,--config-path TEXT       Config file path.
  -l,--lang TEXT              Language
  -t,--title TEXT             Title
  --preflight                 Preflight document template before processing
```



### `add-tags`
Add tags to PDF.


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -c,--config-path TEXT       Config file path.
  --preflight                 Preflight document template before processing
```



### `pdf2table`
Extracts tables detected in the PDF into CSV files.Output should point to the folder where separate CSV files will be saved.


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `pdf2txt`
Extract text from PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -c,--config_path TEXT:FILE  Config file path
  -p,--page INT               Page number from which text will be extracted (Default value -1 extract all pages
```



### `pdf2image`
Extract images from PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -w,--page-width INT         with of the rendered page in pixels used for scaling the images
  -f,--format ENUM:{0,1}      integer value defining the image output format (0-PNG, 1-JPG)
  -q,--quality INT:INT in [0 - 100]
image quality. For JPG means the compression level otherwise it’s ignored
```



### `ocr`
Converts scans or images-only PDF documents into searchable, editable PDF files.


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -l,--lang TEXT              OCR language
  -d,--data-path TEXT:DIR     path to Tesseract ORC data.
```



### `pdf2html`
Converts PDF to HTML , output is the HTML file created duringconversion.  All necessary files generated during the conversion aresaved in the same folder as the output file.


_Positionals:_
```
  input TEXT:FILE REQUIRED    Input file
  output TEXT REQUIRED        Output file
```


_Options:_
```
  -i,--input TEXT:FILE REQUIRED
Input file
  -o,--output TEXT REQUIRED   Output file
  -c,--config-path TEXT       path to config file.
  -w,--page-width INT         Page width
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
  --export-fonts Needs: --responsive
exports embedded TrueType fonts into HTML using CSS3.
  --format ENUM:{0,1}         integer value defining the image output format (0-PNG, 1-JPG)
  --quality INT:INT in [0 - 100]
integer value defining the image output quality (0-100)
  -j,--js                     
  -s,--css                    
  -d,--doc                    
  -p,--page INT               
```



### `license`
License related commands



_Options:_
```
  -a,--activate <License Key> 
  -d,--deactivate             
  -u,--update                 
  -s,--status                 
  -r,--reset                  
```



### `tagged-pdf`
Convert Tagged PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `tags2json`
StructTree to JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `import-data`
Import form data from JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -j,--json-path TEXT:FILE    Path to JSON file
  -f,--flatten                Flatten PDF
```



### `content2json`
Page Content to JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -p,--page-number INT        page number.
```



### `parse-pds-objects`
Tag operations on PDF


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



### `dests2json`
Extract Named Destivations into JSON


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file or stream
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file or stream
```



### `test`
test commands


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
  -m,--image-path TEXT        Path to image file used for watermark
```



### `create-documents`
Create new PDF files


_Positionals:_
```
  output TEXT                 Output directory
  count UINT                  Document count
  thread-count UINT           Thread count
```


_Options:_
```
  -o,--output TEXT            Output directory
  -c,--count UINT             Document count
  -t,--thread-count UINT      Thread count
```



### `render-pages`
Render Pages


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output directory
```


_Options:_
```
  -f,--format ENUM:{0,1}      integer value defining the image output format (0-PNG, 1-JPG)
  -r,--rotate ENUM:{0,90,180,270}
page rotation in degrees
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output directory
  --page-from INT             page number from which rendering will be exectuted
  --page-to INT               page number to which rendering will be exectuted
  -l,--left INT               integer value specifying the page left of the clipping region in device units
  -t,--top INT                integer value specifying the page top of the clipping region in device units
  -w,--width INT              integer value specifying the width of the page left clipping region in device units
  -g,--height INT             integer value specifying the height of the page left clipping region in device units
  -q,--quality INT:INT in [0 - 100]
integer value defining the image output quality (0-100)
  -z,--zoom FLOAT             floating point number of zoom level
  --thread-count UINT         maximal number of threads to be used
```



### `redact`
Redact content using all redaction annotations.


_Positionals:_
```
  input TEXT:FILE             Input file
  output TEXT                 Output file
```


_Options:_
```
  -i,--input TEXT:FILE        Input file
  -o,--output TEXT            Output file
```



