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
