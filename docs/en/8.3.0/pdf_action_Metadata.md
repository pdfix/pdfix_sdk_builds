## Metadata

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
