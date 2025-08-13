<div id="md-title">

# PDFix Batch Actions

Custom PDF actions automate the editing of PDFs and resolve various accessibility issues, streamlining document editing and remediation. This approach enhances efficiency and simplifies tasks by eliminating the need for programming skills. By utilizing a bespoke sequence of actions, you can process PDF documents tailored to your specific requirements

```
{
    "title": "PDFix Batch Action Example",
    "desc": "Custom action sequence to re-tag the PDF document and set the PDF/UA-1 identifier",
    "actions": [
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

</div>

<div id="md-toc">

## Index

<div id="md-toc-accessibility">

__Accessibility__: [Set PDF/UA Standard](#set-pdf/ua-standard), [Set Suspect Value](#set-suspect-value), [Fix Optional Content](#fix-optional-content), [Fix Display Document Title](#fix-display-document-title), [AutoTag](#autotag), [Clear Document Structure](#clear-document-structure), [Fix ID Tree](#fix-id-tree), [Fix Parent Tree](#fix-parent-tree)

</div>

<div id="md-toc-annotations">

__Annotations__: [Fix Media Clip](#fix-media-clip), [Set Tab Order](#set-tab-order), [Tag Annotations](#tag-annotations), [Set Annotation Contents](#set-annotation-contents), [Remove Annotation Properties](#remove-annotation-properties), [Flatten Annotations](#flatten-annotations), [Create Web Links](#create-web-links), [Delete Annotations](#delete-annotations)

</div>

<div id="md-toc-bookmarks">

__Bookmarks__: [Create Bookmarks](#create-bookmarks)

</div>

<div id="md-toc-content">

__Content__: [Delete Content](#delete-content), [Artifact Content](#artifact-content), [Flatten Form XObjects](#flatten-form-xobjects), [Clone Form XObjects](#clone-form-xobjects), [Remove Content Marks](#remove-content-marks), [Set Content Color](#set-content-color)

</div>

<div id="md-toc-conversion">

__Conversion__: [PDF to HTML](#pdf-to-html), [PDF to JSON](#pdf-to-json)

</div>

<div id="md-toc-fonts">

__Fonts__: [Embed Fonts](#embed-fonts), [Replace Font](#replace-font), [Add Missing Unicodes](#add-missing-unicodes)

</div>

<div id="md-toc-metadata">

__Metadata__: [Set Document Properties](#set-document-properties), [Set PDF Version](#set-pdf-version), [Set Language](#set-language), [Set Title](#set-title)

</div>

<div id="md-toc-pages">

__Pages__: [Rotate Page](#rotate-page), [Fix Page Orientation](#fix-page-orientation), [Split Pages](#split-pages)

</div>

<div id="md-toc-role map">

__Role Map__: [Apply Standard Tags](#apply-standard-tags), [Fix Role Mapping](#fix-role-mapping), [Set Role Mapping](#set-role-mapping)

</div>

<div id="md-toc-table">

__Table__: [Fix Table Cells](#fix-table-cells), [Set Table Summary](#set-table-summary)

</div>

<div id="md-toc-tags">

__Tags__: [Import Tags](#import-tags), [Delete Tags](#delete-tags), [Rename Tags](#rename-tags), [Clone Tag XObjects](#clone-tag-xobjects), [Set Tag ID](#set-tag-id), [Set Tag BBox](#set-tag-bbox), [Set Alternate Description](#set-alternate-description), [Set Actual Text](#set-actual-text), [Fix Placement](#fix-placement), [Fix Document Tag](#fix-document-tag), [Fix List Tag](#fix-list-tag), [Remove Tag Properties](#remove-tag-properties), [Set Tag Attributes](#set-tag-attributes), [Fix Spaces](#fix-spaces), [Fix Headings](#fix-headings)

</div>

</div>

<div id="md-accessibility">

## Accessibility

### Set PDF/UA Standard

`set_pdf_ua_standard`

Set the PDF/UA part number

#### params:

- `part_number` (string) __Part Identifier__ - Specify the part number of the International Standard to which the file conforms

  - ____  - Remove PDF/UA Part Number
  - __1__  - PDF/UA-1
  - __2__  - PDF/UA-2


- `rev_number` (string) __Rev Number__ - Specify the four-digit year of publication or revision (ignored for part 1)

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
### Set Suspect Value

`set_suspect_value`

Fix the document’s MarkInfo dictionary and Suspects entry

#### example:
```
{
    "name": "set_suspect_value"
}
```
### Fix Optional Content

`fix_oc_name`

Fix the optional content configuration dictionary

#### example:
```
{
    "name": "fix_oc_name"
}
```
### Fix Display Document Title

`set_display_doc_title`

Fix the ViewerPreferences dictionary

#### example:
```
{
    "name": "set_display_doc_title"
}
```
### AutoTag

`add_tags`

Automatically add accessibility tags to an untagged document

#### params:

- `template` (file_path) __Template__ - Load the template from the file as the current template. If the file is empty, the default template will be applied

- `preflight` (bool) __Preflight__ - Preflight the document and combine the preflight values with the current template

- `standard_attrs` (bool) __Add Layout Attributes__ - Add all detected layout attributes

- `sequential_headings` (bool) __Sequential Heading Levels__ - Keep headings in sequentially descending order

#### example:
```
{
    "name": "add_tags",
    "params": [
        {
            "name": "template",
            "value": ""
        },
        {
            "name": "preflight",
            "value": false
        },
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
### Clear Document Structure

`clear_structure`

Clear the document structure

#### params:

- `clear_tags` (bool) __Clear Content Marks__ - Clear content marks

- `clear_struct_tree` (bool) __Clear Structure Tree__ - Clear the structure tree

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
### Fix ID Tree

`fix_id_tree`

Fix the ID tree

#### example:
```
{
    "name": "fix_id_tree"
}
```
### Fix Parent Tree

`fix_parent_tree`

Fix the parent tree

#### example:
```
{
    "name": "fix_parent_tree"
}
```
</div>

<div id="md-annotations">

## Annotations

### Fix Media Clip

`fix_media_clip_keys`

Define a MIME type for the media clip annotation file

#### params:

- `ct_key` (string) __Media Clip__ - CT key

  - __text/plain__  - text/plain
  - __text/html__  - text/html
  - __image/jpeg__  - image/jpeg
  - __audio/mp3__  - audio/mp3
  - __video/mp4__  - video/mp4


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
### Set Tab Order

`set_tabs_key`

Set the tab order key for every page. Every page containing an annotation must have the Tabs key set to S

#### params:

- `tabs_key` (string) __Tabs Key__ - Specify the tab order key

- `overwrite` (bool) __Overwrite__ - Replace the current tab order key if it already exists

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
### Tag Annotations

`tag_annot`

Tag untagged annotations by placing them in the closest matching tag

#### params:

- `annot_types` (annot) __Annotations__ - Specify annotation types using a regular expression format or define them by template annot_update

#### example:
```
{
    "name": "tag_annot",
    "params": [
        {
            "name": "annot_types",
            "value": "^(?!.*Popup).*$"
        }
    ]
}
```
### Set Annotation Contents

`set_annot_contents`

Set an alternative description for an annotation using the Contents key or TU key for widget annotations

#### params:

- `annot_types` (annot) __Annotations__ - Specify annotation types using a regular expression format or define them by template annot_update

- `alt_type` (int) __Contents__ - Define the source for detecting alternative text

  - __0__  - Custom text
  - __1__  - Text from annotation bounding box
  - __2__  - Action destination
  - __3__  - Auto generated text


- `custom_text` (string) __Custom__ - Enter custom text for the Contents key

- `bbox_padding_x` (float) __Left BBox Padding__ - Adjust horizontal padding (X axis) for the left edge of the BBox

- `bbox_padding_x_right` (float) __ Right BBox Padding__ - Adjust horizontal padding (X axis) for the right edge of the BBox

- `bbox_padding_y_top` (float) __Top BBox Padding__ - Adjust vertical padding (Y axis) for the top edge of the BBox

- `bbox_padding_y` (float) __Bottom BBox Padding__ - Adjust vertical padding (Y axis) for the bottom edge of the BBox

- `overwrite` (bool) __Overwrite__ - eplace the current alternative description if it already exists

#### example:
```
{
    "name": "set_annot_contents",
    "params": [
        {
            "name": "annot_types",
            "value": ".*"
        },
        {
            "name": "alt_type",
            "value": 1
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
            "name": "bbox_padding_x_right",
            "value": 4
        },
        {
            "name": "bbox_padding_y_top",
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
### Remove Annotation Properties

`remove_annot_data`

Remove properties from the annotations

#### params:

- `annot_types` (annot) __Annotations__ - Specify annotation types using a regular expression format or define them by template annot_update

- `remove_contents` (bool) __Remove Contents__ - Remove the Contents key

#### example:
```
{
    "name": "remove_annot_data",
    "params": [
        {
            "name": "annot_types",
            "value": ".*"
        },
        {
            "name": "remove_contents",
            "value": true
        }
    ]
}
```
### Flatten Annotations

`flatten_annot`

Flatten the visual representation of annotations into the content layer. This prevents issues with annotation tagging when interactivity is not needed in a PDF/UA-compliant document

#### params:

- `annot_types` (annot) __Annotations__ - Specify annotation types using a regular expression format or define them by template annot_update

#### example:
```
{
    "name": "flatten_annot",
    "params": [
        {
            "name": "annot_types",
            "value": "^(?!.*Link|.*Widget|.*Popup).*$"
        }
    ]
}
```
### Create Web Links

`create_web_links`

Create link annotations from web addresses and email patterns found in the page content

#### params:

- `url_regex` (string) __URL Pattern__ - Specify a regular expression to identify web or email links in the content. The matched text will be used as the link target unless overridden by the URL Address or modified by adding the URL Prefix

  - __^(((http(s)?|ftp):\/\/)|(mailto:)|www.)[^\s\/$.?#].[^\s]*__ 
  - __^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}__ 


- `url_prefix` (string) __URL Prefix__ - Prepend this prefix to the detected URL or email if it does not already begin with a known scheme (e.g., http, mailto). This is useful for ensuring that URLs are correctly formatted

  - ____ 
  - __http://__ 
  - __https://__ 
  - __ftp://__ 
  - __file://__ 
  - __mailto:__ 
  - __tel:__ 
  - __data:__ 
  - __ws://__ 
  - __wss://__ 


- `url` (string) __URL Address__ - Set the destination URL. If this is set, it overrides the matched text and any prefix added by the URL Prefix

#### example:
```
{
    "name": "create_web_links",
    "params": [
        {
            "name": "url_regex",
            "value": "^(((http(s)?|ftp):\\/\\/)|(mailto:)|www.)[^\\s\\/$.?#].[^\\s]*"
        },
        {
            "name": "url_prefix",
            "value": "ws://"
        },
        {
            "name": "url",
            "value": ""
        }
    ]
}
```
### Delete Annotations

`delete_annot`

Completely remove an annotation from the PDF. Use this action when certain annotation types (e.g., TrapNet) are not permitted in a PDF/UA-compliant document

#### params:

- `annot_types` (annot) __Annotations__ - Specify annotation types using a regular expression format or define them by template annot_update

#### example:
```
{
    "name": "delete_annot",
    "params": [
        {
            "name": "annot_types",
            "value": "^TrapNet$"
        }
    ]
}
```
</div>

<div id="md-bookmarks">

## Bookmarks

### Create Bookmarks

`create_bookmarks`

Create bookmarks from the tag tree hierarchy

#### params:

- `tag_1` (tag) __Level 1__ - Define tag types using a regular expression format or specify them by template

- `tag_2` (tag) __Level 2__ - Define the tag that represents second level

- `tag_3` (tag) __Level 3__ - Define the tag that represents third level

- `tag_4` (tag) __Level 4__ - Define the tag that represents fourth level

- `tag_5` (tag) __Level 5__ - Define the tag that represents fifth level

- `tag_6` (tag) __Level 6__ - Define the tag that represents sixth level

- `overwrite` (bool) __Overwrite__ - Replace existing bookmarks if they already exist

#### example:
```
{
    "name": "create_bookmarks",
    "params": [
        {
            "name": "tag_1",
            "value": "^H1$"
        },
        {
            "name": "tag_2",
            "value": "^H2$"
        },
        {
            "name": "tag_3",
            "value": "^H3$"
        },
        {
            "name": "tag_4",
            "value": "^H4$"
        },
        {
            "name": "tag_5",
            "value": "^H5$"
        },
        {
            "name": "tag_6",
            "value": "^H6$"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
</div>

<div id="md-content">

## Content

### Delete Content

`delete_content`

Completely remove a content from the PDF

#### params:

- `object_types` (object) __Objects__ - Define the page content objects to be deleted

#### example:
```
{
    "name": "delete_content",
    "params": [
        {
            "name": "object_types",
            "value": ""
        }
    ]
}
```
### Artifact Content

`artifact_content`

Mark defined content as an artifact

#### params:

- `object_types` (object) __Objects__ - Specify the objects using the object_update template

- `artifact_type` (int) __Mark as__ - Mark the content as an artifact, header, or footer

  - __0__  - Artifact
  - __1__  - Header
  - __2__  - Footer


#### example:
```
{
    "name": "artifact_content",
    "params": [
        {
            "name": "object_types",
            "value": {
                "template": {
                    "object_update": [
                        {
                            "query": {
                                "$and": [
                                    {
                                        "$0_artifact": "false"
                                    },
                                    {
                                        "$0_mcid": "-1"
                                    }
                                ],
                                "param": [
                                    "pds_object"
                                ]
                            },
                            "statement": "$if"
                        }
                    ]
                }
            }
        },
        {
            "name": "artifact_type",
            "value": 0
        }
    ]
}
```
### Flatten Form XObjects

`flatten_xobject`

Flatten Form XObjects

#### params:

- `object_types` (object) __Objects__ - Define the objects by the template object_update

#### example:
```
{
    "name": "flatten_xobject",
    "params": [
        {
            "name": "object_types",
            "value": "^pds_form$"
        }
    ]
}
```
### Clone Form XObjects

`clone_xobject`

Clone Form XObjects

#### params:

- `object_types` (object) __Objects__ - Define the objects by the template object_update

#### example:
```
{
    "name": "clone_xobject",
    "params": [
        {
            "name": "object_types",
            "value": "^pds_form$"
        }
    ]
}
```
### Remove Content Marks

`remove_content_marks`

Remove artifact, MCID, or any custom tag from page content objects

#### params:

- `object_types` (object) __Objects__ - Define the objects by the template object_update

- `flags` (flag) __Remove__ - Specify types of content marks to be removed

  - __8__  - Invalid MCID
  - __4__  - Custom Content Marks
  - __1__  - MCID
  - __2__  - Artifact


#### example:
```
{
    "name": "remove_content_marks",
    "params": [
        {
            "name": "object_types",
            "value": ".*"
        },
        {
            "name": "flags",
            "value": 8
        }
    ]
}
```
### Set Content Color

`set_content_color`

Change the fill and/or stroke color of specified content objects

#### params:

- `object_types` (object) __Objects__ - Define the page objects using the object_update template

- `fill_color` (string) __Fill Color__ - Specify a new fill color using the format RGB(127,255,0) or CMYK(25,84,50,100). Leave empty to keep the current color unchanged

- `stroke_color` (string) __Stroke Color__ - Specify a new stroke color using the format RGB(127,255,0) or CMYK(25,84,50,100). Leave empty to keep the current color unchanged

#### example:
```
{
    "name": "set_content_color",
    "params": [
        {
            "name": "object_types",
            "value": ".*"
        },
        {
            "name": "fill_color",
            "value": "RGB(0,0,0)"
        },
        {
            "name": "stroke_color",
            "value": "RGB(0,0,0)"
        }
    ]
}
```
</div>

<div id="md-conversion">

## Conversion

### PDF to HTML

`pdf_to_html`

Convert a PDF to HTML

#### params:

- `input_pdf` (file_path) __Input PDF__ - Specify the input PDF file path

- `output_html` (file_path) __Ouput HTML__ - Specify the output HTML file

- `html_type` (int) __HTML Layout__ - Choose the HTML layout type

  - __0__ - Original layout
  - __1__ - Responsive layout
  - __2__ - Layout defined by PDF Tags


- `template` (file_path) __Template__ - Load the template from a file as the current template. If the file is empty, the default template will be applied

- `preflight` (bool) __Preflight__ - Preflight the document and merge its preflight values with the current template

- `flags` (flag) __Conversion Flags__ - Define conversion flags

  - __1__ - Export JavaScript
  - __2__ - Export fonts
  - __4__ - Use default font sizes
  - __8__ - Retain text color
  - __32__ - Inline CSS styles
  - __64__ - Inline JavaScript code
  - __128__ - Embed images within the document
  - __256__ - Embed fonts within the document
  - __512__ - Apply gray padding


#### example:
```
{
    "name": "pdf_to_html"
}
```
### PDF to JSON

`pdf_to_json`

Convert a PDF to JSON

#### params:

- `input_pdf` (file_path) __Input PDF__ - Specify the input PDF file path

- `output_json` (file_path) __Output JSON__ - Specify the output JSON file path

- `flags` (flag) __Conversion Flags__ - Specify flags for the extracted content

  - __1__ - Include document metadata
  - __2__ - Include page information
  - __16__ - Extract page content
  - __32__ - Extract document structure tree
  - __64__ - Extract layout recognition
  - __256__ - Include bounding box data
  - __512__ - Include content marks
  - __4096__ - Include text content
  - __8192__ - Include text style
  - __16384__ - Include text state
  - __65536__ - Extract images as base64
  - __131072__ - Extract annotations


#### example:
```
{
    "name": "pdf_to_json"
}
```
</div>

<div id="md-fonts">

## Fonts

### Embed Fonts

`embed_font`

Embed fonts in the document

#### example:
```
{
    "name": "embed_font"
}
```
### Replace Font

`replace_font`

Replace a font

#### params:

- `font_name` (string) __Font Name__ - Specify the PDF font name to be replaced. Regular expressions are supported

- `font_family` (system_font) __Font Family__ - Specify the font family name to be used as a replacement

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
### Add Missing Unicodes

`add_missing_unicode`

Add missing Unicode mappings

#### example:
```
{
    "name": "add_missing_unicode"
}
```
</div>

<div id="md-metadata">

## Metadata

### Set Document Properties

`set_doc_info`

Set document metadata and properties

#### params:

- `set_author` (bool) __Set Author__ - Set the document author

- `author` (string) __Author__ - Specify the author

- `set_title` (bool) __Set Title__ - Set the document title

- `title` (string) __Title__ - Specify the title

- `set_subject` (bool) __Set Subject__ - Set the document subject

- `subject` (string) __Subject__ - Specify the subject

- `set_keywords` (bool) __Set Keywords__ - Set the document keywords

- `keywords` (string) __Keywords__ - Specify the keywords

- `set_producer` (bool) __Set Producer__ - Set the document producer

- `producer` (string) __Producer__ - Specify the producer name

- `set_creator` (bool) __Set Creator__ - Set the document creator

- `creator` (string) __Creator__ - Specify the creator

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
### Set PDF Version

`set_pdf_version`

Set the PDF version

#### params:

- `version_number` (int) __PDF Version__ - Choose the PDF version designation

  - __14__  - PDF 1.4
  - __15__  - PDF 1.5
  - __16__  - PDF 1.6
  - __17__  - PDF 1.7
  - __20__  - PDF 2.0


#### example:
```
{
    "name": "set_pdf_version",
    "params": [
        {
            "name": "version_number",
            "value": 17
        }
    ]
}
```
### Set Language

`set_language`

Set the document language

#### params:

- `lang` (lang) __Language__ - Document language

- `apply_lang_to` (int) __Apply Language to__ - Select the objects to which the defined language will be applied

  - __0__  - Document
  - __1__  - Tag
  - __2__  - Marked Content


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
### Set Title

`set_title`

Set the document title

#### params:

- `title_type` (int) __Title__ - Define a source for detecting the document title

  - __0__  - Define a custom title
  - __1__  - Use the first description tag
  - __2__  - Retrieve the title from the file name


- `custom_text` (string) __Custom Title__ - Custom title

- `description_tag` (string) __Description Tag__ - Define the tags whose content is used for the title text

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
</div>

<div id="md-pages">

## Pages

### Rotate Page

`rotate_pages`

Rotate pages

#### params:

- `object_types` (object) __Pages__ - Select pages using regular expressions or by defining anchors in a template

- `rotation_type` (int) __Rotation Type__ - Specify the type of rotation

  - __0__  - Set rotation angle
  - __1__  - Rotate by angle


- `rotation_angle` (int) __Rotation Angle__ - Specify the rotation angle

  - __0__  - 0 degrees
  - __90__  - 90 degrees
  - __180__  - 180 degrees
  - __270__  - 270 degrees


#### example:
```
{
    "name": "rotate_pages",
    "params": [
        {
            "name": "object_types",
            "value": ".*"
        },
        {
            "name": "rotation_type",
            "value": 1
        },
        {
            "name": "rotation_angle",
            "value": 0
        }
    ]
}
```
### Fix Page Orientation

`fix_page_orientation`

Correct the orientation of selected pages and normalize their transformation matrix and bounding box

#### params:

- `object_types` (object) __Pages__ - Select pages using regular expressions or by defining anchors in a template

#### example:
```
{
    "name": "fix_page_orientation",
    "params": [
        {
            "name": "object_types",
            "value": ".*"
        }
    ]
}
```
### Split Pages

`split_pages`

Split a PDF into multiple documents based on defined page rules or template anchors

#### params:

- `base_pdf` (file_path) __Output Path__ - Specify the output folder based on the input file pathh

- `object_types` (object) __Splitters__ - Specify split rules using regular expressions for page numbers or template-defined anchors

#### example:
```
{
    "name": "split_pages",
    "params": [
        {
            "name": "base_pdf",
            "value": ""
        },
        {
            "name": "object_types",
            "value": ".*"
        }
    ]
}
```
</div>

<div id="md-role map">

## Role Map

### Apply Standard Tags

`apply_standard_tags`

Changes all non-standard tags to standard tags according to their role mapping

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

#### example:
```
{
    "name": "apply_standard_tags",
    "params": [
        {
            "name": "tag_names",
            "value": ".*"
        }
    ]
}
```
### Fix Role Mapping

`remove_standard_tags_mapping`

Resolve issues in the document's Role Map to ensure correct structure type mappings

#### params:

- `standard_role_mapping` (bool) __Remove standard tags mapping__ - Remove role mapping of standard structure types

- `circular_role_mapping` (bool) __Remove circular role mapping__ - Detect and remove circular role mappings that is explicitly permitted

- `clear_rolemap` (bool) __Clear Role Map__ - Clear the role map specified in the structure tree root

#### example:
```
{
    "name": "remove_standard_tags_mapping",
    "params": [
        {
            "name": "standard_role_mapping",
            "value": true
        },
        {
            "name": "circular_role_mapping",
            "value": true
        },
        {
            "name": "clear_rolemap",
            "value": true
        }
    ]
}
```
### Set Role Mapping

`set_role_mapping`

Map the name of structure types used in the document to the selected standard structure types

#### params:

- `tag_names` (tag) __Tags__ - Specify the tag types using a regular expression format or define them by template tag_update

- `standard_tag_name` (string) __Standard tag type__ - Specify the standard tag name to which the selected tag will be role-mapped

- `overwrite` (bool) __Overwrite__ - Replace the current tag mapping

#### example:
```
{
    "name": "set_role_mapping",
    "params": [
        {
            "name": "tag_names",
            "value": ""
        },
        {
            "name": "standard_tag_name",
            "value": "P"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
</div>

<div id="md-table">

## Table

### Fix Table Cells

`set_table_header`

Fix table header and data cells

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `scope` (string) __Scope__ - Specify whether the header cell applies to a row, column, or both

  - __None__  - None
  - __Row__  - Row
  - __Column__  - Column
  - __Both__  - Both


- `row_span` (int) __RowSpan__ - Set the row span for the cell. Use -1 to keep the existing RowSpan

- `col_span` (int) __ColSpan__ - Set the column span for the cell. Use -1 to keep the existing ColSpan

- `tag_name` (string) __Change to__ - Specify a new tag type (TD or TH) for the cell. Leave empty to retain the existing type

- `overwrite` (bool) __Overwrite__ - Replace current properties if they already exist

#### example:
```
{
    "name": "set_table_header",
    "params": [
        {
            "name": "tag_names",
            "value": "^TD$"
        },
        {
            "name": "scope",
            "value": "None"
        },
        {
            "name": "row_span",
            "value": -1
        },
        {
            "name": "col_span",
            "value": -1
        },
        {
            "name": "tag_name",
            "value": "TH"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### Set Table Summary

`set_table_summary`

Provide a summary of the table’s purpose and structure. Only applicable to Table tags

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `summary_type` (int) __Summary__ - Define a source for detecting the summary

  - __0__  - Define the Custom Summary
  - __1__  - Use the associated TH content
  - __2__  - Use the associated tag content


- `custom_text` (string) __Custom Summary__ - Enter custom text as the table summary

- `overwrite` (bool) __Overwrite__ - Replace the table summary if it already exists

#### example:
```
{
    "name": "set_table_summary",
    "params": [
        {
            "name": "tag_names",
            "value": "^Table$"
        },
        {
            "name": "summary_type",
            "value": 2
        },
        {
            "name": "custom_text",
            "value": "Summary"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
</div>

<div id="md-tags">

## Tags

### Import Tags

`import_tags`

Import a tag tree with predefined values and templates

#### params:

- `json_path` (file_path) __Json__ - Load a JSON file that represents the tag tree in an expected formatt

#### example:
```
{
    "name": "import_tags",
    "params": [
        {
            "name": "json_path",
            "value": ""
        }
    ]
}
```
### Delete Tags

`delete_tags`

Delete defined tags

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `tag_content` (string) __Content__ - Handle the content of deleted tags

  - __none__  - Leave content untagged
  - __move__  - Move nested tags to the parent tag
  - __artifact__  - Mark content as an artifact


#### example:
```
{
    "name": "delete_tags",
    "params": [
        {
            "name": "tag_names",
            "value": {
                "template": {
                    "tag_update": [
                        {
                            "query": {
                                "$and": [
                                    {
                                        "$0_tag_type": {
                                            "$regex": "^(?!H$|H\\d$|TH$|TD$|TR$|LBody$).*"
                                        }
                                    },
                                    {
                                        "$0_has_content": "false"
                                    }
                                ],
                                "param": [
                                    "pds_struct_elem"
                                ]
                            },
                            "statement": "$if"
                        }
                    ]
                }
            }
        },
        {
            "name": "tag_content",
            "value": "none"
        }
    ]
}
```
### Rename Tags

`rename_tags`

Rename tags

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `tag_name` (string) __Replace with__ - Specify a new tag name

#### example:
```
{
    "name": "rename_tags",
    "params": [
        {
            "name": "tag_names",
            "value": "^P$"
        },
        {
            "name": "tag_name",
            "value": "P"
        }
    ]
}
```
### Clone Tag XObjects

`clone_tag_xobject`

Clone Form XObjects in tags

#### example:
```
{
    "name": "clone_tag_xobject"
}
```
### Set Tag ID

`set_tag_id`

Generate a unique ID key for specific tags, such as Note tags required in PDF/UA-1

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `overwrite` (bool) __Overwrite__ - Replace the current tag ID if it already exists

#### example:
```
{
    "name": "set_tag_id",
    "params": [
        {
            "name": "tag_names",
            "value": "^Note$|^TH$"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### Set Tag BBox

`set_tag_bbox`

Calculate the bounding box from the tag content and set it in the Layout attributes

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `overwrite` (bool) __Overwrite__ - Replace the current bounding box if it already exists

#### example:
```
{
    "name": "set_tag_bbox",
    "params": [
        {
            "name": "tag_names",
            "value": "^Figure$|^Formula$|^Form$|^Table$"
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### Set Alternate Description

`set_alt`

Set an alternative description for the tag. These text alternatives are crucial for accessibility, helping users with vision impairments understand the content

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `alt_type` (int) __Alternative Description__ - Define a source for detecting the alternative text

  - __0__  - Define the Custom Alternative text
  - __1__  - Use the first Description Tag above
  - __2__  - Use the first Description Tag below
  - __3__  - Use the first Description Tag from children
  - __4__  - Use the associated tag content. If there is an Annotation among the children, its Contents key is used


- `custom_text` (string) __Custom Alternative__ - Enter custom text for the alternative description

- `description_tag` (string) __Description Tag__ - Define tags whose content is used for the alternative description

- `overwrite` (bool) __Overwrite__ - Replace the alternative description if it already exists

#### example:
```
{
    "name": "set_alt",
    "params": [
        {
            "name": "tag_names",
            "value": "^Figure$|^Formula$"
        },
        {
            "name": "alt_type",
            "value": 4
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
### Set Actual Text

`set_actual`

Set a replacement text for the content, providing an equivalent text representation

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `actual_type` (int) __Actual Text__ - Define a source for detecting the replacement text

  - __0__  - Custom actual text
  - __1__  - Use the associated tag content


- `custom_text` (string) __Custom__ - Enter custom actual text as the replacement text

- `overwrite` (bool) __Overwrite__ - Replace the actual text if it already exists

#### example:
```
{
    "name": "set_actual",
    "params": [
        {
            "name": "tag_names",
            "value": "^Span$"
        },
        {
            "name": "actual_type",
            "value": 0
        },
        {
            "name": "custom_text",
            "value": ""
        },
        {
            "name": "overwrite",
            "value": false
        }
    ]
}
```
### Fix Placement

`fix_placement`

Fix incorrect placement attributes for specified tags

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

#### example:
```
{
    "name": "fix_placement",
    "params": [
        {
            "name": "tag_names",
            "value": "^Figure$|^Formula$|^Form$|^Note$"
        }
    ]
}
```
### Fix Document Tag

`fix_document_tag`

Fix the document tag

#### example:
```
{
    "name": "fix_document_tag"
}
```
### Fix List Tag

`fix_list_tag`

Fix list(L) tag errors

#### params:

- `tag_names` (tag) __Tags__ - Define the tags by the template tag_update

#### example:
```
{
    "name": "fix_list_tag",
    "params": [
        {
            "name": "tag_names",
            "value": "^L$"
        }
    ]
}
```
### Remove Tag Properties

`remove_tag_data`

Remove properties from the defined tags

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `accept_alternate_desc` (bool) __Remove Alternate__ - Remove the Alt key

- `accept_actual_text` (bool) __Remove Actual Text__ - Remove the ActualText key

- `accept_id` (bool) __Remove ID__ - Remove the ID key

- `accept_lang` (bool) __Remove Language__ - Remove the Lang key

- `accept_title` (bool) __Remove Title__ - Remove the T key

- `owner` (string) __Remove Attribute Owner__ - Remove standard attribute owners. If no attribute name is specified, all attributes in the group will be removed

  - __None__  - None
  - __Layout__  - Layout Attributes governing the layout of content
  - __List__  - List Attributes governing the numbering of lists
  - __PrintField__  - PrintField Attributes governing Form structure elements for non-interactive form fields
  - __Table__  - Table Attributes governing the organisation of cells in tables


- `name` (string) __Remove Attribute Name__ - Remove a specific attribute by name. For example Headers from the previously defined Attribute Owner

#### example:
```
{
    "name": "remove_tag_data",
    "params": [
        {
            "name": "tag_names",
            "value": ".*"
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
        },
        {
            "name": "owner",
            "value": "None"
        },
        {
            "name": "name",
            "value": ""
        }
    ]
}
```
### Set Tag Attributes

`set_structure_attribute`

Set standard structure attributes for tags. Each attribute object has an owner

#### params:

- `tag_names` (tag) __Tags__ - Specify the tags using a regular expression format or define them by template tag_update

- `overwrite` (bool) __Overwrite__ - Replace the current attribute if it already exists

- `owner` (string) __Owner__ - Specify the standard attribute owner

  - __Layout__  - Layout Attributes governing the layout of content
  - __List__  - List Attributes governing the numbering of lists
  - __PrintField__  - PrintField Attributes governing Form structure elements for non-interactive form fields
  - __Table__  - Table Attributes governing the organisation of cells in tables


- `name` (string) __Name__ - Specify the attribute name

- `value` (string) __Value__ - Specify the attribute value

- `value_type` (string) __Value Type__ - Specify the attribute value type

  - __string__  - string
  - __name__  - name
  - __array__  - array
  - __number__  - number


- `overwrite` (bool) __Overwrite__ - Replace the current attribute if it already exists

#### example:
```
{
    "name": "set_structure_attribute",
    "params": [
        {
            "name": "tag_names",
            "value": ".*"
        },
        {
            "name": "overwrite",
            "value": false
        },
        {
            "name": "owner",
            "value": "Layout"
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
            "value": "array"
        },
        {
            "name": "overwrite",
            "value": "false"
        }
    ]
}
```
### Fix Spaces

`fix_structure_spaces`

Add missing or resolve duplicate white spaces within a structure element

#### params:

- `add_missing_spaces` (bool) __Add Missing Spaces__ - Identify words in the structure and add missing spaces

- `remove_unnecessary_spaces` (bool) __Remove Unnecessary Spaces__ - Remove duplicate spaces after each word

- `artifact_unnecessary_spaces` (bool) __Artifact Unnecessary Spaces__ - Mark duplicate spaces as artifacts

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
### Fix Headings

`fix_headings`

Correct an invalid heading structure to maintain sequentially descending order

#### params:

- `renumber_headings` (int) __Renumber Headings__ - Renumber all headings

  - __0__  - Change headings to
  - __1__  - Move headings up a level
  - __2__  - Add empty headings


- `change_headings_to` (string) __Change Headings to__ - Change all headings to a specified level

  - __H__  - H
  - __H1__  - H1
  - __H2__  - H2
  - __H3__  - H3
  - __H4__  - H4


#### example:
```
{
    "name": "fix_headings",
    "params": [
        {
            "name": "renumber_headings",
            "value": 2
        },
        {
            "name": "change_headings_to",
            "value": "H"
        }
    ]
}
```
</div>

