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
