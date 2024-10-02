## Tags

### Delete Tags
`delete_tags`

Delete defined tags
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
### Apply Standard Tags
`apply_standard_tags`

Apply standard tag names according to their role mapping
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
### Rename Tags
`rename_tags`

Rename tag names
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
### Set Tag ID
`set_tag_id`

Generate a unique identifier for the tag
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
### Set Tag BBox
`set_tag_bbox`

Calculate the tag bbox from it's content
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
### Set Alternate Description
`set_alt`

Set alternative description to the tag
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
### Set Actual Text
`set_actual`

Set a replacement for the content, providing text that is equivalent to what a person would see when viewing the content
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
### Fix Placement
`fix_placement`

Fix placement
#### example:
```
{
    "name": "fix_placement"
}
```
### Fix Document Tag
`fix_document_tag`

Fix Document tag 
#### example:
```
{
    "name": "fix_document_tag"
}
```
### Fix List Tag
`fix_list_tag`

Fix List tag 
#### example:
```
{
    "name": "fix_list_tag"
}
```
### Remove Tag Properties
`remove_tag_data`

Remove properties from the defined tags
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
### Set Tag Attributes
`set_structure_attribute`

Set the attributes of the tag
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
### Fix Headings
`fix_headings`

Assign heading levels properly
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
