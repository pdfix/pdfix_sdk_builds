# PDFix Batch Actions

Custom PDF actions are engineered to automate the editing of PDFs and resolve various accessibility issues, thereby streamlining the processes of document editing and remediation. This approach enhances efficiency and simplifies tasks, eliminating the need for programming skills. By utilizing a bespoke sequence of actions, it is possible to process PDF documents tailored to specific requirements

```
{
    "title": "PDFix Batch Action Example",
    "desc": "Custom action sequence to re-tag the PDF document and set PDF/UA-1 identifier",
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
## Index


__Accessibility__: [set_pdf_ua_standard](#set_pdf_ua_standard), [set_suspect_value](#set_suspect_value), [fix_oc_name](#fix_oc_name), [set_display_doc_title](#set_display_doc_title), [remove_standard_tags_mapping](#remove_standard_tags_mapping), [set_language](#set_language), [set_title](#set_title), [add_tags](#add_tags), [clear_structure](#clear_structure), [fix_id_tree](#fix_id_tree), [fix_parent_tree](#fix_parent_tree)

__Annotations__: [fix_media_clip_keys](#fix_media_clip_keys), [set_tabs_key](#set_tabs_key), [tag_annot](#tag_annot), [set_annot_contents](#set_annot_contents), [flatten_annot](#flatten_annot), [create_web_links](#create_web_links), [delete_annot](#delete_annot)

__Bookmarks__: [create_bookmarks](#create_bookmarks)

__Content__: [artifact_content](#artifact_content), [flatten_xobject](#flatten_xobject), [remove_content_marks](#remove_content_marks), [fix_structure_spaces](#fix_structure_spaces)

__Conversion__: [pdf_to_html](#pdf_to_html), [pdf_to_json](#pdf_to_json)

__Fonts__: [embed_font](#embed_font), [replace_font](#replace_font), [add_missing_unicode](#add_missing_unicode)

__Metadata__: [get_doc_info](#get_doc_info), [set_doc_info](#set_doc_info), [set_pdf_version](#set_pdf_version)

__Pages__: [rotate_pages](#rotate_pages)

__Tags__: [delete_tags](#delete_tags), [apply_standard_tags](#apply_standard_tags), [rename_tags](#rename_tags), [set_tag_id](#set_tag_id), [set_tag_bbox](#set_tag_bbox), [set_alt](#set_alt), [set_actual](#set_actual), [fix_placement](#fix_placement), [fix_document_tag](#fix_document_tag), [fix_list_tag](#fix_list_tag), [remove_tag_data](#remove_tag_data), [set_structure_attribute](#set_structure_attribute), [fix_headings](#fix_headings)


## Accessibility

### `set_pdf_ua_standard`
__Set PDF/UA Standard__ - Set the PDF/UA part number
#### params:

- `part_number` (string) __Part Identifier__ - The part number of the International Standard that the file conforms to

  - __1__ - PDF/UA-1
  - __2__ - PDF/UA-2


- `rev_number` (string) __Rev Number__ - Four-digit year of the date of publication or revision. Ignored for part 1

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

- `template` (file_path) __Template__ - Load the template from the file as the current template. If the file is empty, the default template will be used

- `preflight` (bool) __Preflight__ - Preflight the document and combine the preflight values with the current template

- `standard_attrs` (bool) __Add Layout Attributes__ - Add all detected layout attributes

- `sequential_headings` (bool) __Sequential Heading Levels__ - Keep headings in sequentially-descending order

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

- `annot_types` (annot) __Annotations__ - Define the annotations types using a regular expression format (https://regex101.com/) or define by the template update_annot

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
### `set_annot_contents`
__Set Contents__ - Set alternative description for an annotation to Contents key
#### params:

- `annot_types` (annot) __Annotations__ - Define the annotations types using a regular expression format (https://regex101.com/) or define by the template update_annot

- `alt_type` (int) __Contents__ - Define a source for detecting the alternative text

  - __0__ - Define the Custom Text
  - __1__ - Use the text from annotation bounding box
  - __2__ - Use the action destination


- `custom_text` (string) __Custom Text__ - Enter custom text to Contents key

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
            "value": "^Link$|^Highlight$|^Underline$|^Squiggly$|^StrikeOut$"
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

- `annot_types` (annot) __Annotations__ - Define the annotations types using a regular expression format (https://regex101.com/) or define by the template update_annot

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
### `create_web_links`
__Create Web Links__ - Create link annotations from web links in the page content
#### params:

- `url_regex` (string) __URL__ - Regular expression used for searching web links

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

- `annot_types` (annot) __Annotations__ - Define the annotations types using a regular expression format (https://regex101.com/) or define by the template update_annot

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
## Bookmarks

### `create_bookmarks`
__Create Bookmarks__ - Create bookmarks from the tag tree hierarchy
#### params:

- `tag_1` (tag) __Level 1__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `tag_2` (tag) __Level 2__ - Define the tag that represents second level

- `tag_3` (tag) __Level 3__ - Define the tag that represents third level

- `tag_4` (tag) __Level 4__ - Define the tag that represents fourth level

- `tag_5` (tag) __Level 5__ - Define the tag that represents fifth level

- `tag_6` (tag) __Level 6__ - Define the tag that represents sixth level

- `overwrite` (bool) __Overwrite__ - Replace the current bookmarks it already exist

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
## Conversion

### `pdf_to_html`
__PDF To HTML__ - Convert PDF to HTML
#### example:
```
{
    "name": "pdf_to_html"
}
```
### `pdf_to_json`
__Convert To JSON__ - Convert PDF to JSON
#### params:

- `output` (folder_path) __Output Folder__ - The destination folder for the output

- `struct_tree` (bool) __Structure Tree__ - Structure tree

- `page_map` (bool) __PageMap Objects__ - PageMap objects

- `page_content` (bool) __Page Content Objects__ - Page content objects

- `template` (file_path) __Template__ - Load the template from the file as the current template. If the file is empty, the default template will be used

- `preflight` (bool) __Preflight__ - Preflight the document and combine the preflight values with the current template

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
            "name": "template",
            "value": ""
        },
        {
            "name": "preflight",
            "value": false
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

- `font_name` (string) __Font Name__ - The PDF font name that will replaced. Regular expression is supported

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
### `set_pdf_version`
__Set PDF Version__ - Set the PDF version
#### params:

- `version_number` (int) __PDF Version__ - Version designations

  - __14__ - PDF 1.4
  - __15__ - PDF 1.5
  - __16__ - PDF 1.6
  - __17__ - PDF 1.7
  - __20__ - PDF 2.0


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

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `tag_content` (string) __Content__ - Handle the content of the tag

  - __none__ - Leave untagged
  - __move__ - Move to parent tag


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
                                            "$regex": "^(?!H$|H1$|H2$|H3$|H4$|H5$|H6$|TH$|TD$|TR$|LI$|Lbl$|LBody$).*"
                                        }
                                    },
                                    {
                                        "$0_children_num": "0"
                                    },
                                    {
                                        "$0_actual_text": ""
                                    },
                                    {
                                        "$0_expansion": ""
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
### `apply_standard_tags`
__Apply Standard Tags__ - Apply standard tag names according to their role mapping
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `rolemap` (bool) __Clear Role Map__ - Clear the role map specified in the structure tree root

#### example:
```
{
    "name": "apply_standard_tags",
    "params": [
        {
            "name": "tag_names",
            "value": ".*"
        },
        {
            "name": "rolemap",
            "value": true
        }
    ]
}
```
### `rename_tags`
__Rename Tags__ - Rename tag names
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `tag_name` (string) __Replace with__ - Type a new tag name

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
### `set_tag_id`
__Set Tag ID__ - Generate a unique identifier for the tag
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `overwrite` (bool) __Overwrite__ - Replace the current Tag ID if it already exists

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
### `set_tag_bbox`
__Set Tag BBox__ - Calculate the tag bbox from it's content
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `overwrite` (bool) __Overwrite__ - Replace the current Tag ID if it already exists

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
### `set_alt`
__Set Alternate Description__ - Set alternative description to the tag
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `alt_type` (int) __Alternative Description__ - Define a source for detecting the alternative text

  - __0__ - Define the Custom Alternative text
  - __1__ - Use the first Description Tag above
  - __2__ - Use the first Description Tag below
  - __3__ - Use the first Description Tag from children
  - __4__ - Use the associated tag content


- `custom_text` (string) __Custom Alternative__ - Enter custom text to serve as an alternative description

- `description_tag` (string) __Description Tag__ - Define the tags which content is used for alternative description

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
### `set_actual`
__Set Actual Text__ - Set a replacement for the content, providing text that is equivalent to what a person would see when viewing the content
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

- `actual_type` (int) __Actual Text__ - Define a source for detecting the replacement text

  - __0__ - Define the Custom Actual text
  - __1__ - Use the associated tag content


- `custom_text` (string) __Custom Actual__ - Enter custom text to serve as a replacement text

- `overwrite` (bool) __Overwrite__ - Replace the actual text if it already exists

#### example:
```
{
    "name": "set_actual",
    "params": [
        {
            "name": "tag_names",
            "value": "^Figure$|^Formula$"
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
### `fix_placement`
__Fix Placement__ - Fix placement
#### example:
```
{
    "name": "fix_placement"
}
```
### `fix_document_tag`
__Fix Document Tag__ - Fix Document tag 
#### example:
```
{
    "name": "fix_document_tag"
}
```
### `fix_list_tag`
__Fix List Tag__ - Fix List tag 
#### example:
```
{
    "name": "fix_list_tag"
}
```
### `remove_tag_data`
__Remove Tag Properties__ - Remove properties from the defined tags
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

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
        }
    ]
}
```
### `set_structure_attribute`
__Set Tag Attributes__ - Set the attributes of the tag
#### params:

- `tag_names` (tag) __Tags__ - Define the tags types using a regular expression format (https://regex101.com/) or define by the template update_tag

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
            "value": ".*"
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
### `fix_headings`
__Fix Headings__ - Assign heading levels properly
#### params:

- `renumber_headings` (int) __Renumber Headings__ - Renumber all headings

  - __0__ - Change headings to
  - __1__ - Move headings up a level
  - __2__ - Add empty headings


- `change_headings_to` (string) __Change Headings to__ - Change Headings to

  - __H__ - H
  - __H1__ - H1
  - __H2__ - H2
  - __H3__ - H3
  - __H4__ - H4


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
