# PDFix Batch Commands

Custom PDF commands are engineered to automate the editing of PDFs and resolve various accessibility issues, thereby streamlining the processes of document editing and remediation. This approach enhances efficiency and simplifies tasks, eliminating the need for programming skills. By utilizing a bespoke sequence of commands, it is possible to process PDF documents tailored to specific requirements.

```
{
    "title": "PDFix Batch Command Example",
    "desc": "Custom command sequence to re-tag the PDF document and set PDF/UA-1 identifier",
    "commands": [
        {
            "name": "clear_structure",
            "params": [
                {
                    "name": "clear_tags",
                    "value": true
                },
                {
                    "name": "clear_struct_tree",
                    "value": true
                },
                {
                    "name": "clear_bookmarks",
                    "value": false
                }
            ]
        },
        {
            "name": "add_tags",
            "params": [
                {
                    "name": "standard_attrs",
                    "value": false
                },
                {
                    "name": "sequential_headings",
                    "value": true
                }
            ]
        },
        {
            "name": "set_pdf_ua_standard",
            "params": [
                {
                    "name": "part_number",
                    "value": 1
                }
            ]
        }
    ]
}
```
## Index


__Accesibility__: [set_pdf_ua_standard](#set_pdf_ua_standard), [set_suspect_value](#set_suspect_value), [fix_oc_name](#fix_oc_name), [set_display_doc_title](#set_display_doc_title), [remove_standard_tags_mapping](#remove_standard_tags_mapping), [set_language](#set_language), [set_title](#set_title), [add_tags](#add_tags), [clear_structure](#clear_structure), [fix_id_tree](#fix_id_tree), [fix_parent_tree](#fix_parent_tree)

__Annotations__: [fix_media_clip_keys](#fix_media_clip_keys), [set_tabs_key](#set_tabs_key), [tag_annot](#tag_annot), [set_annot_contents](#set_annot_contents), [flatten_annot](#flatten_annot), [create_web_links](#create_web_links), [delete_annot](#delete_annot)

__Bookmarks__: [create_bookmarks](#create_bookmarks)

__Content__: [artifact_content](#artifact_content), [flatten_xobject](#flatten_xobject), [remove_content_marks](#remove_content_marks)

__Conversion__: [pdf_to_html](#pdf_to_html), [pdf_to_json](#pdf_to_json)

__Fonts__: [embed_font](#embed_font), [replace_font](#replace_font), [add_missing_unicode](#add_missing_unicode)

__Metadata__: [get_doc_info](#get_doc_info), [set_doc_info](#set_doc_info)

__Pages__: [rotate_pages](#rotate_pages)

__Tags__: [delete_tags](#delete_tags), [apply_standard_tags](#apply_standard_tags), [set_tag_id](#set_tag_id), [set_tag_bbox](#set_tag_bbox), [set_alt](#set_alt), [fix_placement](#fix_placement), [remove_tag_data](#remove_tag_data), [set_structure_attribute](#set_structure_attribute), [fix_structure_spaces](#fix_structure_spaces), [fix_headings](#fix_headings)

__Template__: [preflight](#preflight), [load_template](#load_template), [reset_template](#reset_template)

__Validation__: [validation](#validation), [validation_report](#validation_report)


## Accesibility

### `set_pdf_ua_standard`
__Set PDF/UA Standard__ - Set the PDF/UA part number
#### params:

- `part_number` (string) __Part Identifier__ - The part number of the International Standard that the file conforms to.

  - __1__ - PDF/UA-1
  - __2__ - PDF/UA-2


- `rev_number` (string) __Rev Number__ - Four-digit year of the date of publication or revision. Ignored for part 1.

#### example:
```
{
    "name": "set_pdf_ua_standard",
    "params": [
        {
            "name": "part_number",
            "value": "1"
        },
        {
            "name": "rev_number",
            "value": "2023"
        }
    ]
}
```
### `set_suspect_value`
__Set Suspect Value__ - Fix the document Suspects entry
#### example:
```
{
    "name": "set_suspect_value"
}
```
### `fix_oc_name`
__Fix Optional Content__ - Fix optional content configuration dictionary
#### example:
```
{
    "name": "fix_oc_name"
}
```
### `set_display_doc_title`
__Fix Display Document Title__ - Fix ViewerPreferences dictionary
#### example:
```
{
    "name": "set_display_doc_title"
}
```
### `remove_standard_tags_mapping`
__Remove Standard Tags Mapping__ - Remove standard tags mapping
#### example:
```
{
    "name": "remove_standard_tags_mapping"
}
```
### `set_language`
__Set Language__ - Define the document language
#### params:

- `lang` (lang) __Language__ - Document language

- `apply_lang_to` (int) __Apply Language to__ - Select the objects to which you intend to apply the defined language

  - __0__ - Document
  - __1__ - Tag
  - __2__ - Marked Content


- `overwrite` (bool) __Overwrite__ - Replace the current language if it already exists

#### example:
```
{
    "name": "set_language",
    "params": [
        {
            "name": "lang",
            "value": "en-US"
        },
        {
            "name": "apply_lang_to",
            "value": 0
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### `set_title`
__Set Title__ - Set document title
#### params:

- `title_type` (int) __Title__ - Define a source for detecting the document title

  - __0__ - Define the Custom Title
  - __1__ - Use the first Description Tag
  - __2__ - Retrieve the title from the file name


- `custom_text` (string) __Custom Title__ - Custom title

- `description_tag` (string) __Description Tag__ - Define the tags which content is used for title text

- `overwrite` (bool) __Overwrite__ - Replace the current title if it already exists

#### example:
```
{
    "name": "set_title",
    "params": [
        {
            "name": "title_type",
            "value": 2
        },
        {
            "name": "custom_text",
            "value": ""
        },
        {
            "name": "description_tag",
            "value": "Caption"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### `add_tags`
__Autotag__ - Autotag document
#### params:

- `standard_attrs` (bool) __Add Layout Attributes__ - Add all detected layout attributes

- `sequential_headings` (bool) __Sequential Heading Levels__ - Keep headings in sequentially-descending order

#### example:
```
{
    "name": "add_tags",
    "params": [
        {
            "name": "standard_attrs",
            "value": false
        },
        {
            "name": "sequential_headings",
            "value": true
        }
    ]
}
```
### `clear_structure`
__Clear Document Structure__ - Clear document structure
#### params:

- `clear_tags` (bool) __Clear Content Marks__ - Clear content marks

- `clear_struct_tree` (bool) __Clear Structure Tree__ - Clear structure tree

- `clear_bookmarks` (bool) __Clear Bookmarks__ - Clear bookmarks

#### example:
```
{
    "name": "clear_structure",
    "params": [
        {
            "name": "clear_tags",
            "value": true
        },
        {
            "name": "clear_struct_tree",
            "value": true
        },
        {
            "name": "clear_bookmarks",
            "value": true
        }
    ]
}
```
### `fix_id_tree`
__Fix ID Tree__ - Fix ID tree
#### example:
```
{
    "name": "fix_id_tree"
}
```
### `fix_parent_tree`
__Fix Parent Tree__ - Fix parent tree
#### example:
```
{
    "name": "fix_parent_tree"
}
```
## Annotations

### `fix_media_clip_keys`
__Fix Media Clip__ - Define a MIME type of the media clip annotations file
#### params:

- `ct_key` (string) __Media Clip__ - CT key

  - __text/plain__ - text/plain
  - __text/html__ - text/html
  - __image/jpeg__ - image/jpeg
  - __audio/mp3__ - audio/mp3
  - __video/mp4__ - video/mp4


#### example:
```
{
    "name": "fix_media_clip_keys",
    "params": [
        {
            "name": "ct_key",
            "value": "text/plain"
        }
    ]
}
```
### `set_tabs_key`
__Set Tab Order__ - Sets the tab order key for every page
#### params:

- `tabs_key` (string) __Tabs Key__ - Tabs key

- `overwrite` (bool) __Overwrite__ - Replace the current Tabs Key if it already exists

#### example:
```
{
    "name": "set_tabs_key",
    "params": [
        {
            "name": "tabs_key",
            "value": "S"
        },
        {
            "name": "overwrite",
            "value": true
        }
    ]
}
```
### `tag_annot`
__Tag Annotations__ - Tag the untagged annotations
#### params:

- `annot_types` (string) __Annotation Types__ - Annotation types delimited by comma

- `exclude_annot_types` (bool) __Exclude__ - Exclude annotation types if checked

- `flags` (flag) __Flags__ - Skip annotations with specific characteristics

  - __1__ - Skip Invisible
  - __2__ - Skip Hidden


#### example:
```
{
    "name": "tag_annot",
    "params": [
        {
            "name": "annot_types",
            "value": "Popup"
        },
        {
            "name": "exclude_annot_types",
            "value": true
        },
        {
            "name": "flags",
            "value": 3
        }
    ]
}
```
### `set_annot_contents`
__Set Annotation Contents__ - Set alternative description for an annotation
#### params:

- `annot_types` (string) __Annotation Types__ - Annotation types delimited by comma

- `exclude_annot_types` (bool) __Exclude__ - Exclude annotation types if checked

- `flags` (flag) __Flags__ - Skip annotations with specific characteristics

  - __1__ - Skip Invisible
  - __2__ - Skip Hidden


- `alt_type` (int) __Contents__ - Define a source for detecting the alternative text

  - __0__ - Define the Custom Contents text
  - __1__ - Use the text from annotation bounding box
  - __2__ - Use the action destination


- `custom_text` (string) __Custom Contents__ - Enter custom text to serve as an alternative description

- `bbox_padding_x` (float) __BBox X padding__ - Bounding box padding in horizontal direction

- `bbox_padding_y` (float) __BBox Y padding__ - Bounding box padding in vertical direction

- `overwrite` (bool) __Overwrite__ - Replace the current alternative description if it already exists

#### example:
```
{
    "name": "set_annot_contents",
    "params": [
        {
            "name": "annot_types",
            "value": "Link,Highlight,Underline,Squiggly,StrikeOut"
        },
        {
            "name": "exclude_annot_types",
            "value": false
        },
        {
            "name": "flags",
            "value": 3
        },
        {
            "name": "alt_type",
            "value": 0
        },
        {
            "name": "custom_text",
            "value": "Decorative"
        },
        {
            "name": "bbox_padding_x",
            "value": 4
        },
        {
            "name": "bbox_padding_y",
            "value": 4
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### `flatten_annot`
__Flatten Annotations__ - Flatten the visual representation of annotations directly into the content layer
#### params:

- `annot_types` (string) __Annotation Types__ - Annotation types delimited by comma

- `exclude_annot_types` (bool) __Exclude__ - Exclude annotation types if checked

- `flags` (flag) __Flags__ - Skip annotations with specific characteristics

  - __1__ - Skip Invisible
  - __2__ - Skip Hidden


#### example:
```
{
    "name": "flatten_annot",
    "params": [
        {
            "name": "annot_types",
            "value": "Widget,Popup,Link"
        },
        {
            "name": "exclude_annot_types",
            "value": true
        },
        {
            "name": "flags",
            "value": 3
        }
    ]
}
```
### `create_web_links`
__Create Web Links__ - Create link annotations from web links in the page content
#### params:

- `url_regex` (string) __URL search regex__ - Regular expression for searching web links

#### example:
```
{
    "name": "create_web_links",
    "params": [
        {
            "name": "url_regex",
            "value": "^(((http(s)?|ftp):\\/\\/)|(mailto:)|www.)[^\\s\\/$.?#].[^\\s]*"
        }
    ]
}
```
### `delete_annot`
__Delete Annotations__ - Delete annotations from the document
#### params:

- `annot_types` (string) __Annotation Types__ - Annotation types delimited by comma

- `exclude_annot_types` (bool) __Exclude__ - Exclude annotation types if checked

- `flags` (flag) __Flags__ - Satisfy the characteristics of the annotation

  - __1__ - Delete Invisible
  - __2__ - Delete Hidden
  - __255__ - Delete All


#### example:
```
{
    "name": "delete_annot",
    "params": [
        {
            "name": "annot_types",
            "value": "TrapNet"
        },
        {
            "name": "exclude_annot_types",
            "value": false
        },
        {
            "name": "flags",
            "value": 255
        }
    ]
}
```
## Bookmarks

### `create_bookmarks`
__Create Bookmarks__ - Create bookmarks from the tag tree hierarchy
#### params:

- `tag_1` (string) __Level 1__ - Define the tag that represents top level

- `tag_2` (string) __Level 2__ - Define the tag that represents second level

- `tag_3` (string) __Level 3__ - Define the tag that represents third level

- `tag_4` (string) __Level 4__ - Define the tag that represents fourth level

- `tag_5` (string) __Level 5__ - Define the tag that represents fifth level

- `tag_6` (string) __Level 6__ - Define the tag that represents sixth level

- `overwrite` (bool) __Overwrite__ - Replace the current bookmarks it already exist

#### example:
```
{
    "name": "create_bookmarks",
    "params": [
        {
            "name": "tag_1",
            "value": "H1"
        },
        {
            "name": "tag_2",
            "value": "H2"
        },
        {
            "name": "tag_3",
            "value": "H3"
        },
        {
            "name": "tag_4",
            "value": "H4"
        },
        {
            "name": "tag_5",
            "value": "H5"
        },
        {
            "name": "tag_6",
            "value": "H6"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
## Content

### `artifact_content`
__Artifact Content__ - Mark defined content as an artifact
#### params:

- `artifact_untagged` (bool) __Untagged content only__ - Mark the content as Artifact only if it's untagged

- `artifact_type` (int) __Mark as__ - Mark the content as an Artifact, Header or Footer

  - __0__ - Artifact
  - __1__ - Header
  - __2__ - Footer


#### example:
```
{
    "name": "artifact_content",
    "params": [
        {
            "name": "artifact_untagged",
            "value": true
        },
        {
            "name": "artifact_type",
            "value": 0
        }
    ]
}
```
### `flatten_xobject`
__Flatten Form XObjects__ - Flatten Form XObjects
#### example:
```
{
    "name": "flatten_xobject"
}
```
### `remove_content_marks`
__Remove Content Marks__ - Remove atrifact, mcid or any custom tag from page content objects
#### params:

- `flags` (flag) __Remove__ - Types of content marks to be removed

  - __1__ - MCID
  - __2__ - Artifact
  - __4__ - Custom Content Marks
  - __8__ - Invalid Content Marks
  - __16__ - Artifact, if MCID is presented
  - __32__ - MCID, if Artifact is presented


#### example:
```
{
    "name": "remove_content_marks",
    "params": [
        {
            "name": "flags",
            "value": 8
        }
    ]
}
```
## Conversion

### `pdf_to_html`
__Convert To HTML__ - Convert PDF to HTML
#### params:

- `html_type` (int) __Conversion Type__ - HTML layout type

  - __0__ - Original layout
  - __1__ - Responsive layout
  - __2__ - Layout defined by PDF Tags


- `output` (folder_path) __Output Folder__ - The destination folder for the output

- `width` (int) __Width__ - The width of the rendered page in pixels. Width controls the quality of rendered images.

- `flags` (flag) __Conversion Flags__ - HTML conversion flags

  - __0__ - Basic html
  - __1__ - Export document JavaScripts
  - __2__ - Export embedded font files
  - __4__ - Ignore font sizes and use standard
  - __8__ - Retain text color
  - __32__ - Use inline css
  - __64__ - Use inline JavaScript
  - __128__ - Use embedded base64 encoded images
  - __256__ - Use embedded base64 encoded fonts
  - __512__ - Display pages on the gray background with margin
  - __1024__ - Do not render the page. Original layout only.
  - __2048__ - Exclude head and body html nodes
  - __4096__ - Exclude pdf-document div element
  - __8192__ - Exclude pdf-page div elements


#### example:
```
{
    "name": "pdf_to_html",
    "params": [
        {
            "name": "html_type",
            "value": 0
        },
        {
            "name": "output",
            "value": ""
        },
        {
            "name": "width",
            "value": 1200
        },
        {
            "name": "flags",
            "value": false
        }
    ]
}
```
### `pdf_to_json`
__Convert To JSON__ - Convert PDF to JSON
#### params:

- `output` (folder_path) __Output Folder__ - The destination folder for the output

- `struct_tree` (bool) __Structure Tree__ - Structure tree

- `page_map` (bool) __PageMap Objects__ - PageMap objects

- `page_content` (bool) __Page Content Objects__ - Page content objects

- `text` (bool) __Export Texts__ - Export texts

- `text_style` (bool) __Export Text Styles__ - Export text styles

- `text_state` (bool) __Export Text States__ - Export text states

- `images` (bool) __Export Images__ - Export images

- `bbox` (bool) __Export Bounding Box__ - Export object bounding box

- `graphics_state` (bool) __Export Graphics States__ - Export graphics states

- `content_marks` (bool) __Export Content Marks__ - Export object content marks

#### example:
```
{
    "name": "pdf_to_json",
    "params": [
        {
            "name": "output",
            "value": ""
        },
        {
            "name": "struct_tree",
            "value": false
        },
        {
            "name": "page_map",
            "value": true
        },
        {
            "name": "page_content",
            "value": true
        },
        {
            "name": "text",
            "value": true
        },
        {
            "name": "text_style",
            "value": true
        },
        {
            "name": "text_state",
            "value": false
        },
        {
            "name": "images",
            "value": false
        },
        {
            "name": "bbox",
            "value": false
        },
        {
            "name": "graphics_state",
            "value": false
        },
        {
            "name": "content_marks",
            "value": false
        }
    ]
}
```
## Fonts

### `embed_font`
__Embed Fonts__ - Embed font
#### example:
```
{
    "name": "embed_font"
}
```
### `replace_font`
__Replace Font__ - Replace font
#### params:

- `font_name` (string) __Font Name__ - The PDF font name that will replaced. Regular expression is supported.

- `font_family` (system_font) __Font Family__ - The font family name that will be used for replacement

#### example:
```
{
    "name": "replace_font",
    "params": [
        {
            "name": "font_name",
            "value": ""
        },
        {
            "name": "font_family",
            "value": ""
        }
    ]
}
```
### `add_missing_unicode`
__Add Missing Unicodes__ - Add missing unicode mapping
#### example:
```
{
    "name": "add_missing_unicode"
}
```
## Metadata

### `get_doc_info`
__Get Document Properties__ - Get document metadata and properties
#### example:
```
{
    "name": "get_doc_info"
}
```
### `set_doc_info`
__Set Document Properties__ - Set document metadata and properties
#### params:

- `set_author` (bool) __Set Author__ - Set the document author

- `author` (string) __Author__ - Author

- `set_title` (bool) __Set Title__ - Set the document title

- `title` (string) __Title__ - Title

- `set_subject` (bool) __Set Subject__ - Set the document subject

- `subject` (string) __Subject__ - Subject

- `set_keywords` (bool) __Set Keywords__ - Set the document keywords

- `keywords` (string) __Keywords__ - Keywords

- `set_producer` (bool) __Set Producer__ - Set the document producer

- `producer` (string) __Producer__ - Producer name

- `set_creator` (bool) __Set Creator__ - Set the document creator

- `creator` (string) __Creator__ - Creator

#### example:
```
{
    "name": "set_doc_info",
    "params": [
        {
            "name": "set_author",
            "value": true
        },
        {
            "name": "author",
            "value": ""
        },
        {
            "name": "set_title",
            "value": true
        },
        {
            "name": "title",
            "value": ""
        },
        {
            "name": "set_subject",
            "value": true
        },
        {
            "name": "subject",
            "value": ""
        },
        {
            "name": "set_keywords",
            "value": true
        },
        {
            "name": "keywords",
            "value": ""
        },
        {
            "name": "set_producer",
            "value": true
        },
        {
            "name": "producer",
            "value": ""
        },
        {
            "name": "set_creator",
            "value": true
        },
        {
            "name": "creator",
            "value": ""
        }
    ]
}
```
## Pages

### `rotate_pages`
__Rotate Page__ - Rotate pages
#### params:

- `rotation_type` (int) __Rotation Type__ - Type of rotation

  - __0__ - Set rotation angle
  - __1__ - Rotate by angle


- `rotation_angle` (int) __Rotation Angle__ - Rotation angle

  - __0__ - 0 degrees
  - __90__ - 90 degrees
  - __180__ - 180 degrees
  - __270__ - 270 degrees


- `page_rotation` (int) __Pages With Rotation__ - Pages with defined rotation

  - __0__ - 0 degrees
  - __90__ - 90 degrees
  - __180__ - 180 degrees
  - __270__ - 270 degrees


- `page_orientation` (int) __Pages With Orientation__ - Pages with defined orientation

  - __0__ - Pages With Any Orientation
  - __1__ - Landscape Pages
  - __2__ - Portrait Pages


#### example:
```
{
    "name": "rotate_pages",
    "params": [
        {
            "name": "rotation_type",
            "value": 1
        },
        {
            "name": "rotation_angle",
            "value": 0
        },
        {
            "name": "page_rotation",
            "value": 0
        },
        {
            "name": "page_orientation",
            "value": 0
        }
    ]
}
```
## Tags

### `delete_tags`
__Delete Tags__ - Delete defined tags
#### params:

- `tag_names` (string) __Tags__ - Define the tags, separated by commas, that shall be deleted

- `exclude_tag_names` (bool) __Exclude__ - If checked, If checked, all tags except those explicitly defined will be deleted

- `skip_tag_names` (string) __Ignore Tags__ - Define the tags, separated by commas, that should be skipped

- `flags` (flag) __Delete__ - If checked, delete only defined tags

  - __1__ - Empty (no children)
  - __2__ - Invalid (no associated page content)
  - __4__ - Even when Actual Text exists
  - __8__ - Even when Alternate Description exists
  - __255__ - Delete All


#### example:
```
{
    "name": "delete_tags",
    "params": [
        {
            "name": "tag_names",
            "value": "H,H1,H2,H3,H4,H5,H6"
        },
        {
            "name": "exclude_tag_names",
            "value": true
        },
        {
            "name": "skip_tag_names",
            "value": "TH,TD,TR,LI,Lbl,LBody"
        },
        {
            "name": "flags",
            "value": 1
        }
    ]
}
```
### `apply_standard_tags`
__Apply Standard Tags__ - Apply standard tag names according to their role mapping
#### example:
```
{
    "name": "apply_standard_tags"
}
```
### `set_tag_id`
__Set Tag ID__ - Generate a unique identifier for the tag
#### params:

- `tag_names` (string) __Tags__ - Define the tags, separated by commas, from which properties should be removed

- `exclude_tag_names` (bool) __Exclude__ - If checked, all tags except those explicitly defined will be processed

- `overwrite` (bool) __Overwrite__ - Replace the current Tag ID if it already exists

#### example:
```
{
    "name": "set_tag_id",
    "params": [
        {
            "name": "tag_names",
            "value": "Note,TH"
        },
        {
            "name": "exclude_tag_names",
            "value": false
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### `set_tag_bbox`
__Set Tag BBox__ - Calculate the tag bbox from it's content
#### params:

- `tag_names` (string) __Tags__ - Define the tags, separated by commas, from which properties should be removed

- `exclude_tag_names` (bool) __Exclude__ - If checked, all tags except those explicitly defined will be processed

- `overwrite` (bool) __Overwrite__ - Replace the current Tag ID if it already exists

#### example:
```
{
    "name": "set_tag_bbox",
    "params": [
        {
            "name": "tag_names",
            "value": "Figure, Formula, Form, Table"
        },
        {
            "name": "exclude_tag_names",
            "value": false
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### `set_alt`
__Set Alternate Description__ - Set alternative description to the tag
#### params:

- `tag_names` (string) __Tags__ - Define the tags, separated by commas, to set alternative descriptions

- `exclude_tag_names` (bool) __Exclude__ - If checked, all tags except those explicitly defined will be processed

- `alt_type` (int) __Alternative Text__ - Define a source for detecting the alternative text

  - __0__ - Define the Custom Alternative text
  - __1__ - Use the first Description Tag above
  - __2__ - Use the first Description Tag below
  - __3__ - Use the first Description Tag from children
  - __4__ - Use the associated tag content


- `custom_text` (string) __Custom Alternative__ - Enter custom text to serve as an alternative description

- `description_tag` (string) __Description Tag__ - Define the tags which content is used for alternative text

- `overwrite` (bool) __Overwrite__ - Replace the alternative text if it already exists

#### example:
```
{
    "name": "set_alt",
    "params": [
        {
            "name": "tag_names",
            "value": "Figure,Formula"
        },
        {
            "name": "exclude_tag_names",
            "value": false
        },
        {
            "name": "alt_type",
            "value": 0
        },
        {
            "name": "custom_text",
            "value": "Decorative"
        },
        {
            "name": "description_tag",
            "value": "Caption"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### `fix_placement`
__Fix Placement__ - Fix placement
#### example:
```
{
    "name": "fix_placement"
}
```
### `remove_tag_data`
__Remove Tag Properties__ - Remove properties from the defined tags
#### params:

- `tag_names` (string) __Tags__ - Define the tags, separated by commas, from which properties should be removed

- `exclude_tag_names` (bool) __Exclude__ - If checked, all tags except those explicitly defined will be processed

- `accept_alternate_desc` (bool) __Remove Alternate__ - Remove Alt key

- `accept_actual_text` (bool) __Remove Actual Text__ - Remove ActualText key

- `accept_id` (bool) __Remove ID__ - Remove ID key

- `accept_lang` (bool) __Remove Language__ - Remove Lang key

- `accept_title` (bool) __Remove Title__ - Remove T key

#### example:
```
{
    "name": "remove_tag_data",
    "params": [
        {
            "name": "tag_names",
            "value": ""
        },
        {
            "name": "exclude_tag_names",
            "value": true
        },
        {
            "name": "accept_alternate_desc",
            "value": false
        },
        {
            "name": "accept_actual_text",
            "value": false
        },
        {
            "name": "accept_id",
            "value": false
        },
        {
            "name": "accept_lang",
            "value": false
        },
        {
            "name": "accept_title",
            "value": false
        }
    ]
}
```
### `set_structure_attribute`
__Set Tag Attributes__ - Set the attributes of the tag
#### params:

- `tag_names` (string) __Tags__ - Define the tags, separated by commas, from which properties should be removed

- `exclude_tag_names` (bool) __Exclude__ - If checked, all tags except those explicitly defined will be processed

- `overwrite` (bool) __Overwrite__ - Replace the current Tag ID if it already exists

- `owner` (string) __Owner__ - Standard attribute owner

  - __Layout__ - Layout
  - __List__ - List
  - __PrintField__ - PrintField
  - __Table__ - Table


- `name` (string) __Name__ - Attribute name

- `value` (string) __Value__ - Arrtibute value

  - ____ - 


- `value_type` (string) __Value Type__ - Attribute value type

  - __string__ - string
  - __name__ - name
  - __array__ - array
  - __number__ - number


- `overwrite` (bool) __Overwrite__ - Replace the current attribute if it already exists

#### example:
```
{
    "name": "set_structure_attribute",
    "params": [
        {
            "name": "tag_names",
            "value": ""
        },
        {
            "name": "exclude_tag_names",
            "value": true
        },
        {
            "name": "overwrite",
            "value": false
        },
        {
            "name": "owner",
            "value": ""
        },
        {
            "name": "name",
            "value": ""
        },
        {
            "name": "value",
            "value": ""
        },
        {
            "name": "value_type",
            "value": ""
        },
        {
            "name": "overwrite",
            "value": "false"
        }
    ]
}
```
### `fix_structure_spaces`
__Fix Spaces__ - Add missing or resolve duplicate white spaces within a structure element
#### params:

- `add_missing_spaces` (bool) __Add Missing Spaces__ - Identify words in the structure and add missing spaces

- `remove_unnecessary_spaces` (bool) __Remove Unnecessary Spaces__ - Remove duplicite spaces after each word

- `artifact_unnecessary_spaces` (bool) __Artifact Unnecessary Spaces__ - Mark duplicite spaces after each word as an Artifact

#### example:
```
{
    "name": "fix_structure_spaces",
    "params": [
        {
            "name": "add_missing_spaces",
            "value": true
        },
        {
            "name": "remove_unnecessary_spaces",
            "value": false
        },
        {
            "name": "artifact_unnecessary_spaces",
            "value": true
        }
    ]
}
```
### `fix_headings`
__Fix Headings__ - Assign heading levels properly
#### params:

- `renumber_headings` (bool) __Renumber Headings__ - Renumber all headings

- `change_headings_to` (string) __Change Headings to__ - Change Headings to

  - __H__ - H
  - __H1__ - H1
  - __H2__ - H2
  - __H3__ - H3
  - __H4__ - H4
  - __H5__ - H5
  - __H6__ - H6


#### example:
```
{
    "name": "fix_headings",
    "params": [
        {
            "name": "renumber_headings",
            "value": true
        },
        {
            "name": "change_headings_to",
            "value": "H"
        }
    ]
}
```
## Template

### `preflight`
__Preflight__ - Preflight document
#### params:

- `merge_preflight` (bool) __Merge__ - Combine the preflight settings with the existing ones

#### example:
```
{
    "name": "preflight",
    "params": [
        {
            "name": "merge_preflight",
            "value": false
        }
    ]
}
```
### `load_template`
__Load Template__ - Load template from file and merge with the current template
#### params:

- `template` (file_path) __Template__ - Template file path

#### example:
```
{
    "name": "load_template",
    "params": [
        {
            "name": "template",
            "value": ""
        }
    ]
}
```
### `reset_template`
__Reset Template__ - Reset template
#### example:
```
{
    "name": "reset_template"
}
```
## Validation

### `validation`
__Validation__ - Validation
#### params:

- `profile` (validation_profile) __Profile__ - Validation profile

#### example:
```
{
    "name": "validation",
    "params": [
        {
            "name": "profile",
            "value": "PDFUA-1"
        }
    ]
}
```
### `validation_report`
__Validation Report__ - Save the validation report into a file
#### params:

- `output` (folder_path) __Output Folder__ - Choose a folder to save the validation report, or save it in the same folder as the source file if no folder is specified.

- `profile` (validation_profile) __Profile__ - Validation profile

- `file_format` (string) __File Format__ - Validation report format

  - __html__ - html
  - __xml__ - xml
  - __json__ - json
  - __text__ - text
  - __raw__ - raw


#### example:
```
{
    "name": "validation_report",
    "params": [
        {
            "name": "output",
            "value": ""
        },
        {
            "name": "profile",
            "value": "PDFUA-1"
        },
        {
            "name": "file_format",
            "value": "html"
        }
    ]
}
```
