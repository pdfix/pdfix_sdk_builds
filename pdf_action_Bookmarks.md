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
