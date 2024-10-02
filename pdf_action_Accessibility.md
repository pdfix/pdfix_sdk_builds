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
