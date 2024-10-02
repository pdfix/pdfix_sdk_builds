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
