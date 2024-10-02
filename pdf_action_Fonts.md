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
