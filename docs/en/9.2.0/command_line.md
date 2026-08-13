PDFix SDK CLI 
```

./pdfix_app [OPTIONS] [SUBCOMMAND]

```

_OPTIONS:_
```
  -h,--help                   Print this help message and exit
  --help-all-html             Show all help in HTML format
  --help-all-md               Show all help in MD format
  -m,--email TEXT             License name or registered e-mail address.
                              
                                Identifies the PDFix SDK license holder.
                                Required when activating the license via command line.
  -k,--key TEXT               License key.
                              
                              Activation key associated with the provided license name or e-mail.
                              Required for license activation.
  --settings-path TEXT:FILE   Path to PDFix SDK settings file (JSON).
                              
                              The settings file configures SDK behavior including:
                                • user options (font paths, tagging behavior, license data path)
                                • developer options (log level, profiler path, max processes)
                              
                              If not specified, default SDK settings are used.
  --log_level INT:{nothing->0,critical->1,error->2,warning->3,info->4,debug->5} [nothing] 
Logging level
  --log_path TEXT [Default: auto-generated in system temp directory] 
Path to log file
  -v,--version                
```
## SUBCOMMANDS

| name | description |
| - | - |
| [`batch`](#batch) | Process a PDF document using a configuration file and execute a sequence of actions.| 
| [`make-accessible`](#make-accessible) | Makes PDF Accessible. Converts PDF to fully compliant PDF/UA.If you have image-only PDF, please use OCR command before.| 
| [`add-tags`](#add-tags) | Add tags to PDF.| 
| [`extract-data`](#extract-data) | Extract PDF data into JSON/XML| 
| [`pdf2table`](#pdf2table) | Extracts tables detected in the PDF into CSV files.Output should point to the folder where separate CSV files will be saved.| 
| [`pdf2txt`](#pdf2txt) | Extract text from PDF| 
| [`pdf2image`](#pdf2image) | Extract images from PDF| 
| [`extract-highlighted-text`](#extract-highlighted-text) | Extract highlighted text from PDF| 
| [`pdf2html`](#pdf2html) | Converts PDF to HTML , output is the HTML file created during conversion.  All necessary files generated during the conversion are saved in the same folder as the output file.| 
| [`pdf2json`](#pdf2json) | Extract PDF data into JSON| 
| [`preflight`](#preflight) | Preflight document template and output the config| 
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
| [`test`](#test) | test commands| 
| [`test-open-document`](#test-open-document) | test open document commands| 
| [`test-incremental-save`](#test-incremental-save) | test incremental save| 
| [`test-imposition`](#test-imposition) | test imposition| 
| [`render-pages`](#render-pages) | Render PDF pages into images. Expects the path to a PDF file as input and the path to an output folder where the rendered pages will be saved.| 
| [`open-save`](#open-save) | Opens and saves the PDF.| 
| [`add-tags-repeat`](#add-tags-repeat) | Opens and saves the PDF.| 
| [`create-documents`](#create-documents) | Create new PDF files| 
| [`redact`](#redact) | Redact content using all redaction annotations.| 
| [`pocess-control`](#pocess-control) | test commands| 
| [`undo-redo`](#undo-redo) | undo-redo test command| 
| [`tag`](#tag) | Tag operations on PDF| 
| [`remove-security`](#remove-security) | Add tags to PDF.| 
| [`test-edit-page-object-mcid`](#test-edit-page-object-mcid) | Edit page object mcid.| 
batch
  Process a PDF document using a configuration file and execute a sequence of 
  actions. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config TEXT REQUIRED 
                              Path to the JSON configuration file defining the batch actions. 
          --progress          Print progress information to stdout. 

DESCRIPTION: 
The 'batch' command processes a PDF document according to the instructions 
defined in the provided JSON configuration file. 

The configuration file specifies a sequence of actions that are executed in 
order. Each action produces an individual result, 
and the entire batch produces a final summary result. 

OUTPUT BEHAVIOR: 
Standard Output (stdout): 
Displays progress information, warnings, and informational messages during 
processing. 

Standard Error (stderr): 
Outputs a complete JSON report containing: 
- Results of all executed actions 
- Overall batch result 
- Detailed error information (if any) 

The JSON written to stderr is intended for automated processing, logging, or 
integration with external systems. 

EXIT CODES: 
0 Processing completed successfully. 
1 Processing failed (invalid arguments, file errors, or action failure when 
--fail-on-action-failure is enabled). 
>1 Internal or runtime error. 

EXAMPLES: 
Basic usage: 
pdfix_app batch -i input.pdf -o output.pdf -c config.json 

Stop on first failed action: 
pdfix_app batch -i input.pdf -o output.pdf -c config.json 
--fail-on-action-failure 

Redirect output and JSON result separately: 
pdfix_app batch -i input.pdf -o output.pdf -c config.json > progress.log 2> 
result.json 




make-accessible
  Makes PDF Accessible. Converts PDF to fully compliant PDF/UA.If you have 
  image-only PDF, please use OCR command before. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --command-path TEXT Command file path. Default make accessible command will be used 
                              if it's empty. 
  -l,     --lang TEXT         The language to assign to the PDF document 
  -t,     --title TEXT        The title to assign to the PDF document 


add-tags
  Add tags to PDF. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config-path TEXT  Layout template configuration file path. 
          --preflight         Preflight document template before processing 
          --no-sequential-headings 
                              Disable sequential headings checks 


extract-data
  Extract PDF data into JSON/XML 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config_path TEXT:FILE 
                              Config file path 
          --preflight         Preflight document template before processing 
  -f,     --format ENUM:{0,1} integer value defining the data file output format (0-JSON, 
                              1-XML) 
          --page-number INT   the page number from which to extract data, default -1 extracts 
                              from all pages 
          --doc-info          extract document general information (metadata, num pages, etc.) 
          --doc-outlines      extract document outlines (bookmarks) 
          --doc-acroform      extract document forms (AcroForm) 
          --doc-struct-tree   extract document structure tree (tags) 
          --page-info         extract page general information (number, crop box, rotation) 
          --page-content      extract page objects (raw data) 
          --page-map          scrape page data (logical content extraction) 
          --page-annots       extract page annotstions 
          --text              extract page map text elements or content text objects 
          --tables            extract page map tables structure 
          --images            extract page map image elements or page contnet images 
          --bbox              extract element or object bbox 
          --text-style        extract text style of text element 
          --text-state        extract text state of text object or element 
          --graphic-state     extract page object's graphic state 


pdf2table
  Extracts tables detected in the PDF into CSV files.Output should point to the 
  folder where separate CSV files will be saved. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


pdf2txt
  Extract text from PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config_path TEXT:FILE 
                              Config file path 
          --page INT          Page number from which text will be extracted (Default value -1 
                              extract all pages 


pdf2image
  Extract images from PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -w,     --page-width INT    with of the rendered page in pixels used for scaling the images 
  -f,     --format ENUM:{1,2} integer value defining the image output format (1-PNG, 2-JPG) 
  -q,     --quality INT:INT in [0 - 100] 
                              image quality. For JPG means the compression level otherwise 
                              it’s ignored 


extract-highlighted-text
  Extract highlighted text from PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config-path TEXT  path to config file 


pdf2html
  Converts PDF to HTML , output is the HTML file created during conversion. All 
  necessary files generated during the conversion are saved in the same folder as 
  the output file. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config-path TEXT  Path to config file 
  -w,     --page-width INT    Page width 
  -a,     --append-html TEXT  Append HTML code from file 
          --page INT          Convert specific page 
  -f,     --flags INT         Conversion flags 
          --export-js         exports document JavaScript into HTML. 
          --text-size         retain original text size in created HTML. 
          --text-color        page number from which image will be created. 
          --no-external       use inline css, js and embeded images and fonts. 
          --no-external-css   use inline css instead of the external file. 
          --no-external-js    use inline javascript instead of the external file. 
          --no-external-img   use embedded based encoded images. 
          --no-external-font  use embedded based encoded fonts. 
          --gray-background   use gray background and page padding. 
          --no-page-render    do not render page. 
          --export-fonts      exports embedded TrueType fonts into HTML using CSS3. 
          --preflight         Preflight document template before processing 
          --type ENUM:{0,1,2} integer value defining the conversion type (0-Original content 
                              layout type, 1-Responsive content layout type, 2-Derivation) 
          --format ENUM:{1,2} integer value defining the image output format (1-PNG, 2-JPG) 


pdf2json
  Extract PDF data into JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config_path TEXT:FILE 
                              Config file path 
          --preflight         Preflight document template before processing 
  -f,     --flags INT         Conversion flags 


preflight
  Preflight document template and output the config 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -f,     --format ENUM:{0,1} integer value defining the data file output format (0-JSON, 
                              1-XML) 


import-data
  Import form data from JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -j,     --json-path TEXT:FILE 
                              Path to JSON file 
  -f,     --flatten           Flatten PDF 


acroform2json
  Extract PDF Form Fields into JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
          --widgets           include information about the form field annotations - widgets. 


json2acroform
  Import PDF Form Fields from JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -j,     --json-path TEXT:FILE 
                              Path to JSON file 


render-page
  Render Page 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -f,     --format ENUM:{1,2} integer value defining the image output format (1-PNG, 2-JPG) 
  -r,     --rotate ENUM:{0,90,180,270} 
                              page rotation in degrees 
          --page-number INT   page number from which image will be created. 
  -l,     --left INT          integer value specifying the page left of the clipping region in 
                              device units 
  -t,     --top INT           integer value specifying the page top of the clipping region in 
                              device units 
  -w,     --width INT         integer value specifying the width of the page left clipping 
                              region in device units 
  -g,     --height INT        integer value specifying the height of the page left clipping 
                              region in device units 
  -q,     --quality INT:INT in [0 - 100] 
                              integer value defining the image output quality (0-100) 
  -z,     --zoom FLOAT        floating point number of zoom level 


digital-signature
  Sign PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -x,     --pfx-path TEXT:FILE 
                              Path to .pfx file with signature. 
          --pfx-password TEXT Password for .pfx file. 


add-comment
  Add comment to PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


remove-comments
  Remove comments from PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


flatten
  Flatten all annotations into the PDF content. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


embedfonts
  Embeds fonts into PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


watermark
  Add watermark to PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -m,     --image-path TEXT:FILE 
                              Path to image file used for watermark 
  -s,     --start-page INT    First page where the watermark is placed [0]. 
  -e,     --end-page INT      Last page where the watermark is placed [last page]. 
          --order-top INT:NUMBER 
                              Control watermark z-order (0-bottom, [1]-top) 
          --percentage        Use percentage values instead of points 
          --h-align ENUM:NUMBER 
                              Horizontal alignment ([1]-left, 2-right, 3-justify, 6-center) 
          --v-align ENUM:NUMBER 
                              Vertical alignment ([4]-top, 5-bottom, 6-center) 
          --h-value FLOAT:{1,2,3,6} 
                              Horizontal image offset [0] 
          --v-value FLOAT:{4,5,6} 
                              Vertical image offset [0] 
          --scale FLOAT:NUMBER 
                              Image scale [1] 
          --rotation FLOAT:NUMBER 
                              Image counter-clockwise rotation in degrees [0] 
          --opacity FLOAT:NUMBER 
                              Image opacity [1] 


parse-pds-objects
  Tag operations on PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


create-document
  Create new PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


create-page
  Create new page in PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
          --after-page INT    page number after which the new page will be inserted. 


move-page
  Move one page in document 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -f,     --from INT          page number of the page to move 
  -t,     --to INT            new location of the page to move. 


delete-pages
  Delete pages from PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -f,     --from INT          page number of first page to delete. 
  -t,     --to INT            page number of the last page to delete. 


insert-pages
  Insert pages from PDF to another 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -s,     --src TEXT:FILE     Source file 
  -a,     --after INT         Page number after which pages will be inserted 
  -f,     --from INT          Page number of first page to insert 
  -t,     --to INT            Page number of the last page to insert 


document-metadata
  Get and set document metadata as XML 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -x,     --xml-path TEXT     Path to .xml file with metadata. 


license
  License related commands 
  
  
OPTIONS:
  -a,     --activate TEXT     activate license using the key online or offline if 
                              --license-path is set, or request activation if --request-path is 
                              set 
          --request           create activation request, --license-path should be set to write 
                              request to, used only in combination with --activate 
          --license-path TEXT path to a license file 
  -d,     --deactivate        deactivate license online, for offline deactivation 
                              --license-path should be set 
  -u,     --update            update license online, for offline update --license-path should 
                              be set 
  -s,     --status            print license status 
  -r,     --reset             reset local license 


pages2json
  Convert PDF Pages into JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
          --page-number INT   page number, [0] default all pages) 
          --text              exports page text 


bmk2json
  Convert PDF Bookmarks into JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


tags2json
  StructTree to JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


content2json
  Page Content to JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
          --page-number INT   page number. 


dests2json
  Extract Named Destivations into JSON 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


test
  test commands 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -m,     --image-path TEXT   Path to image file used for watermark 


test-open-document
  test open document commands 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


test-incremental-save
  test incremental save 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


test-imposition
  test imposition 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


render-pages
  Render PDF pages into images. Expects the path to a PDF file as input and the 
  path to an output folder where the rendered pages will be saved. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -f,     --format ENUM:{1,2} integer value defining the image output format (1-PNG, 2-JPG) 
  -r,     --rotate ENUM:{0,90,180,270} 
                              page rotation in degrees 
          --page-from INT     page number from which to render (default page 1) 
          --page-to INT       page number to which to render (default -1 last page) 
  -l,     --left INT          integer value specifying the page left of the clipping region in 
                              device units 
  -t,     --top INT           integer value specifying the page top of the clipping region in 
                              device units 
  -w,     --width INT         integer value specifying the width of the page left clipping 
                              region in device units 
  -g,     --height INT        integer value specifying the height of the page left clipping 
                              region in device units 
  -q,     --quality INT:INT in [0 - 100] 
                              integer value defining the image output quality (0-100) 
  -z,     --zoom FLOAT        floating point number of zoom level 
          --thread-count UINT maximal number of threads to be used 


open-save
  Opens and saves the PDF. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -c,     --config-path TEXT  Config file path. 
  -r,     --repeat TEXT       Repeat. 


add-tags-repeat
  Opens and saves the PDF. 
  
  
OPTIONS:
  -c,     --config-path TEXT  Config file path. 
  -r,     --repeat TEXT       Repeat. 
          --preflight         Preflight document template before processing 


create-documents
  Create new PDF files 
  
  
POSITIONALS:
  count UINT                  Document count 
  thread-count UINT           Thread count 

OPTIONS:
  -c,     --count UINT        Document count 
  -t,     --thread-count UINT Thread count 


redact
  Redact content using all redaction annotations. 
  
  
OPTIONS:
  -p,     --page-number INT   page number where redaction mark will be created. 
  -l,     --left INT          integer value specifying the top of the redaction mark on page 
  -b,     --bottom INT        integer value specifying the bottom of the redaction mark on page 
  -w,     --width INT         integer value specifying the width of the redaction mark on page 
  -g,     --height INT        integer value specifying the height of the redaction mark on page 


pocess-control
  test commands 
  
  

undo-redo
  undo-redo test command 
  
  

tag
  Tag operations on PDF 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 
  -r,     --remove            
  -a,     --annotation        
  -f,     --artefact          
  -g,     --heading           
  -d,     --reading-order     
  -s,     --read-struct-tree  
  -e,     --edit-struct-tree  
  -t,     --table-as-figure   


remove-security
  Add tags to PDF. 
  
  
OPTIONS:
          --password TEXT     Open password 


test-edit-page-object-mcid
  Edit page object mcid. 
  
  
OPTIONS:
  -i,     --input TEXT        Path to the input PDF file to be processed. 
  -o,     --output TEXT       Path to the output PDF file that will be generated. 
  -p,     --password TEXT     Password used to open the input PDF (if encrypted). 


