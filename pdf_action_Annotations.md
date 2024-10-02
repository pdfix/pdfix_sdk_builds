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
