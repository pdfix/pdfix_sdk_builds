# PDFix Template

--

## Table of Contents

- [General Settings](#general-settings)
- [Threshold Values](#threshold-values)
- [Regular Expressions](#regular-expressions)
- [Functions](#functions)

## General Settings
General template settings

| key | type | value |
| - | - | - |
| `rtl` | bool | False |
| `substructure_form_xobject` | bool | True |
| `page_tag` | string | NonStruct |
| `debug_pagemap_stop` | string |  |

Example:
```
{
  "template": {
    "settings": {
      "rtl": false,
      "substructure_form_xobject": true,
      "page_tag": "NonStruct",
      "debug_pagemap_stop": ""
    }
  }
}
```

## Threshold Values
--

| key | value | desciption |
| - | - | - |
| `preflight_artifact_font_size_min` | `32` | Minimum font size for artifact |
| `preflight_artifact_w1` | `1` | Horizontal alignment weight. |
| `preflight_artifact_w2` | `1` | Vertical alignment weight. |
| `preflight_artifact_w3` | `1` | Element width weight. |
| `preflight_artifact_w4` | `1` | Element height(for images) or font size(for text) weight. |
| `preflight_artifact_w5` | `1` | Page numbers weight. |
| `preflight_artifact_distance` | `0.7` | Maximum distance<0,1> when elements can be an artifact/header/footer. |
| `preflight_artifact_cluster_points` | `2` | Minimal number of points in preflight_artifact_distance radian. |
| `concurrent_threads` | `0` | The number of concurrent threads. If zero, the number of concurrent threads supported by the implementation is used. If it's set to 1, no parallel algorithms are used. |
| `text_only` | `0` | Process only texts in pagemap. |
| `rotation_detect` | `1` | Detect and correct page rotation for reading. |
| `background_color_red` | `255` | Page background color - red. |
| `background_color_green` | `255` | Page background color - green. |
| `background_color_blue` | `255` | Page background color - blue. |
| `background_color_diff` | `2` | Page background color max color component difference. |
| `bbox_expansion` | `2` | Bounding box expansion - half of kTrTextHeight. |
| `angle_deviation` | `0.015707963267949` | Maximum angle deviation for horizontal and vertical elements. |
| `header_ratio` | `0.15` | Maximum percentage of a header height. Possible values from interval [0,1]. |
| `footer_ratio` | `0.15` | Maximum percentage of a footer height. Possible values from interval [0,1]. |
| `artifact_w1` | `1` | Artifact page border distance weight. |
| `artifact_w2` | `1` | Artifact image area weight. |
| `artifact_border_distance_max` | `2` | Maximum distance of artifact to page border. |
| `artifact_similarity` | `0.7` | Minimum similarity value when object or element is an artifact normalized to interval [0,1]. |
| `path_object_max` | `2000` | Maximum number of subsequence path objects that are still paths. |
| `path_object_min` | `100` | Minimum number of subsequence path objects that are still paths. |
| `initial_element_expansion` | `1` | Initial element bounding box expansion when searching children. Size in points. If its zero, a half of default page font size is used. |
| `initial_element_overlap` | `0.5` | Minimum percentage of covered area of element by the initial element. |
| `annot_char_overlap` | `0.05` | Minimum percentage of covered area of character by the annotation. |
| `isolated_text_ratio` | `10` | Maximum isolated text width ratio. Is multiplied with the font size. |
| `isolated_text` | `80` | Maximum isolated text width. |
| `isolated_element_ratio` | `6` | Maximum isolated element width/height ratio. Is multiplied with the font size. |
| `element_isolated_w1` | `1` | Element paragraph weight. |
| `element_isolated_w2` | `1` | Element width weight. |
| `element_isolated_caption` | `1` | If set to 1 and element contains caption(table, image, chart, note) do not mark it as isolated element. |
| `element_isolated_width_min` | `0` | Minimal value of bbox width for isolated element. If zero, element_isolated_width_min_ratio is used. Size in points. |
| `element_isolated_width_min_ratio` | `4` | Minimal value of bbox width for isolated element multiply with average page font size. |
| `element_isolated_width_max` | `0` | Maximal value of bbox width for isolated element. If zero, element_isolated_width_max_ratio is used. Size in points. |
| `element_isolated_width_max_ratio` | `10` | Maximal value of bbox width for isolated element multiply with average page font size. |
| `element_isolated_similarity` | `0.7` | Minimum similarity value when element is isolated normalized to interval [0,1]. |
| `element_isolated_image_w1` | `1` | Image vs page area weight. |
| `element_isolated_image_w2` | `1` | Elements isolated similarity weight. |
| `element_isolated_image_w3` | `1` | Images area vs join image area weight. |
| `element_isolated_image_similarity` | `0.7` | Minimum similarity value when isolated elements can be added to an image. |
| `element_line_w1` | `1` | Line width weight. |
| `element_line_width_max` | `8` | Maximal value of line width. If zero, element_line_width_max_ratio is used. Size in points. |
| `element_line_width_max_ratio` | `1` | Maximal value of line width multiply with average page font size. |
| `element_line_similarity` | `0.6` | Minimum similarity value when element is recognized as line normalized to interval [0,1]. |
| `element_alignment_ratio` | `0.5` | Ration between baseline and bounding box alignments. Bounding box alignment precision is multiplied with element_alignment_ratio. |
| `rect_image_similarity` | `0.7` | Minimum similarity value when the rectangle should be an image normalized to interval [0,1]. |
| `rect_line_similarity` | `0.5` | Minimum similarity value when the rectangle should be a line normalized to interval [0,1]. |
| `image_background_text` | `1` | Text bounding box expansion. |
| `image_overlap_distance` | `1` | Maximum distance value when graphic page objects can be joined. Distance in points. |
| `image_join_distance` | `8` | Defines the maximum allowed distanc (in points) between small images for them to be considered joinable. These parameters help fine-tune the grouping of small image elements into a cohesive larger visual block based on their spatial proximity. |
| `char_clip_ratio` | `0.5` | Minimal ratio of the clipping area of the character comparing to it's original size. |
| `word_space_width_ratio` | `0.6` | The word_space_width_ratio is a multiplier that determines the threshold for identifying inter-word spaces by comparing the gap between characters to the typical width of a space character. It scales the space width so that small variations in spacing can be interpreted as either a valid word separator or a mere character gap. |
| `word_space_width_min_ratio` | `0.1` | The word_space_width_min_ratio is an additional multiplier that sets a minimum threshold for the allowed space between words. It ensures that, even when minimal character spacing is detected, the computed gap used to determine word boundaries does not fall below a baseline value relative to the font size. |
| `word_space_distance_max` | `0` | Maximum word space distance in points. |
| `word_space_distance_max_ratio` | `0` | Maximum word space distance. The value is multiplied by word font size. |
| `word_space_ratio` | `1` | Ratio that defines if the text line is simple or justify. |
| `word_space_update_min` | `0.2` | Minimum ratio of detected word spacing. |
| `word_space_update_max` | `4` | Maximum ratio of detected word spacing. If set to 0, update word spacif from lines is not applied. |
| `word_space_update_distance` | `0.04` | Distance for clustering word spaces in text line update. |
| `word_splitter_ratio` | `2` | Minimum space before splitter. The value is multiplied by most used font size. |
| `word_splitter_distance` | `4` | Maximum threshold value for word splitters detections. Real distance in points. |
| `word_overlap` | `0.9` | Minimum overlap percentage (0-1) required between bounding boxes to consider words as duplicates. A word must cover at least this percentage of another word's area to be considered overlapping. |
| `text_line_baseline_ratio` | `0.1` | Maximum baseline shift. Value multiplies minimal font. Baseline shift moves individual characters up or down in relation to other text on the same line. |
| `text_line_underline_distance` | `2.6` | Distance of the underline line and text baseline. Size in points. |
| `text_line_underline_char_distance_ratio` | `0.1` | Distance of the underline line start/end point and character bounding box. The value is multiplied by line font size. Size in points. |
| `text_line_subscript_font_ratio` | `1` | This ratio is used to calculate the maximum allowed baseline difference for joining a subscript with its main word. Specifically, multiply the word's font size by this ratio to get a threshold. |
| `text_line_join_font_size_distance` | `0` | Distance of two fonts in points, when two lines with different fonts can be join. |
| `text_line_distance_max` | `0` | Maximum distance between lines. If zero, text_line_distance_max_ratio is used. Size in points. |
| `text_line_distance_max_ratio` | `2` | Maximum distance between lines. The value is multiplied by line font size. |
| `text_line_join_distance` | `2` | Maximum threshold value in line spacing detection for specific font size. The higher value allows creating paragraph with variable line spacings. The value is multiplied by font size. |
| `text_line_chunk_distance_max` | `0` | Maximum distance between chunks. If zero, text_chunk_distance_max_ratio is used. Size in points. |
| `text_line_chunk_distance_max_ratio` | `6` | Maximum distance between chunks. The value is multiplied by simple word spacing between words. |
| `text_line_chunk_distance` | `0` | A fixed threshold parameter used by the clustering algorithm to group word spaces in a line. When set to a nonzero value, it directly defines the threshold that determines whether adjacent word spaces are similar enough to be considered part of the same cluster. If zero, word_distance_ratio is used. Size in points. |
| `text_line_chunk_distance_ratio` | `0.4` | A relative multiplier that comes into play when the fixed threshold (word_distance) is zero. It calculates the threshold by multiplying the line’s font size by the ratio, thereby adapting the clustering sensitivity to the text size. |
| `text_chunk_distance` | `0` | Maximum distance value when text chunks are vertically aligned. If zero, text_chunk_distance_ratio is used. Size in points. |
| `text_chunk_distance_ratio` | `0.42` | Maximum distance value when text chunks are vertically aligned. The value is multiplied by page font width. |
| `text_chunk_simple_distance` | `0.4` | Maximum distance value when text chunks create simple line. Normalized to interval [0,1]. |
| `text_chunk_word_distance` | `0.1` | Maximum distance value when single line text has to be split to words. Normalized to interval [0,1]. |
| `text_height` | `8` | Minimal text height on the page. |
| `text_simple_similarity` | `0.96` | Minimum similarity value when text lines create a simple paragraph normalized to interval [0,1]. |
| `text_justify_similarity` | `0.96` | Minimum similarity value when text lines create a justify paragraph normalized to interval [0,1]. |
| `text_table_similarity` | `0.65` | Minimum similarity value when text lines create a table normalized to interval [0,1]. |
| `text_paragraph_similarity` | `0.7` | Minimum similarity value when text is paragraph normalized to interval [0,1]. |
| `text_split_distance` | `0.2` | Dissimilarity boundary value when text lines creates a paragraph. |
| `text_column_similarity` | `0.7` | Minimum similarity value that text creates a column normalized to interval [0,1]. |
| `label_image_detect` | `1` | Graphic labels detection. Possible values: 0 | 1. If 0 is set, it prevents generating labels from paths. |
| `label_word_detect` | `1` | Texts labels detection. Possible values: 0 | 1. If 0 is set, it prevents generating labels from words. |
| `label_alignment_h` | `2` | Maximum deviation of horizontal label alignment. |
| `label_distance_ratio` | `10` | Distance of the label and text. Is multiplied with the page most used font size. |
| `label_baseline_ration` | `0.14` | Multiplies minimal font. Maximum deviation of horizontal label aligned to text. |
| `label_image_w1` | `1` | Controls how much vertical alignment matters when clustering labels. A higher value enforces stricter alignment, while a lower value allows more variation. |
| `label_image_w2` | `1` | Controls how much the distance between a label and its associated text influences clustering. A higher value enforces stricter proximity, ensuring labels are closely linked to their text. |
| `label_image_w3` | `1` | This weight controls how much the label's width consistency matters in clustering. A higher value enforces that labels should have the same width, while a lower value allows more variation in width between labels. |
| `label_image_w4` | `1` | This weight determines how important the height consistency of labels is when clustering. A higher value enforces that labels should have the same height, while a lower value allows more flexibility in height differences. |
| `label_image_w5` | `0.5` | This weight adjusts how important the height relationship is between the image label and its associated text. A higher value means the height alignment between the label and the text is more significant in clustering decisions. |
| `label_image_width_min` | `0` | Specifies a fixed minimum width in points. If set to zero, the label_image_width_min_ratio is used instead.. |
| `label_image_width_min_ratio` | `0` | Defines the minimum width as a multiple of the average font size. Useful when label size varies with font size. |
| `label_image_width_max` | `0` | Specifies a fixed maximum width in points. If set to zero, the label_image_width_max_ratio is used instead. |
| `label_image_width_max_ratio` | `6` | Defines the maximum width as a multiple of the average page font size. This ratio is applied when label_image_width_max is zero. |
| `label_image_distance` | `4` | Clustering threshold in points that decides when labels should be grouped together. A higher value makes clustering more flexible, allowing distant labels to merge, while a lower value keeps clusters tight and separate. |
| `label_word_w1` | `1` | Controls how much vertical alignment matters when clustering labels. A higher value enforces stricter alignment, while a lower value allows more variation. |
| `label_word_w2` | `1` | Controls how much the distance between a label and its associated text influences clustering. A higher value enforces stricter proximity, ensuring labels are closely linked to their text. |
| `label_word_dist_sibling_ratio` | `4` | This threshold, defined as a ratio multiplied by a siblings font size, sets the maximum gap allowed between a label and its sibling element to be joined together. If the distance exceeds this value, the label and its sibling remain separate. |
| `label_word_distance` | `0` | Clustering threshold in points that decides when labels should be grouped together. A higher value makes clustering more flexible, allowing distant labels to merge, while a lower value keeps clusters tight and separate. |
| `label_word_distance_ratio` | `1` | Clustering threshold value that decides when labels should be grouped together. The value is multiplied by avarage page font width. |
| `toc_detect` | `1` | TOC detection. Possible values: 0 | 1. If 0 is set, it prevents generating TOC from words. |
| `toc_word_distance` | `0` | Controls how much vertical alignment matters when clustering TOC words. A higher value enforces stricter alignment, ensuring TOC elements are well-structured. |
| `toc_word_distance_ratio` | `1` | Threshold ratio that determines when TOC entries should be clustered together. The value is multiplied by the average page font width. |
| `graphic_table_detect` | `1` | Graphic tables detection. Possible values: 0 | 1. If 0 is set, it prevents generating tables from paths. |
| `graphic_table_detect_row` | `1` | Row graphic tables  detection. |
| `graphic_table_detect_col` | `1` | Column graphic tables detection. |
| `graphic_table_alignment_distance` | `0.8` | Maximum alignment distance value when elements can create a table. Distance in points. |
| `graphic_table_split_w1` | `1` | Table texts paragraph weight. |
| `graphic_table_split_w2` | `1` | Table texts horizontal alignment weight. |
| `graphic_table_split_w3` | `1` | Columns width weight. |
| `graphic_table_split_w4` | `0.5` | Number of columns weight. |
| `graphic_table_split_w5` | `0.5` | Number of rows weight. |
| `graphic_table_split_w6` | `1` | Page area weight. |
| `graphic_table_split_col_max` | `5` | Maximal number of columns when table can be split. |
| `graphic_table_split_row_max` | `5` | Maximal number of rows when table can be split. |
| `graphic_table_split_similarity` | `0.7` | Minimum similarity value when graphic table has to be split. |
| `graphic_table_split_layout_similarity` | `0.7` | Minimum similarity value when graphic table has to be split. |
| `graphic_table_chart_similarity` | `0.3` | Minimum similarity value when graphic table is a char. |
| `graphic_table_image_w1` | `-1` | Images area weight. If -1, number of images is used. |
| `graphic_table_image_w2` | `-1` | Images  weight. If -1, number of images is used. |
| `graphic_table_image_w3` | `-1` | Chart similarity weight. If -1, number of paths is used. |
| `graphic_table_image_w4` | `1` | Texts vertical alignment weight. |
| `graphic_table_image_w5` | `1` | Table size weight. |
| `graphic_table_image_similarity` | `0.7` | Minimum similarity value when graphic table has an image. |
| `text_table_detect` | `1` | Texts (not graphic) tables detection. Possible values: 0 | 1. If 0 is set, it prevents generating tables from isolated chunk of text. |
| `text_table_detect_row` | `1` | Row texts (not graphic) tables detection. |
| `text_table_detect_col` | `1` | Column texts (not graphic) tables detection.  |
| `text_table_row_alignment_type` | `1` | Table row alignment type [0 - strong, 1 - average, 2 - weak]. |
| `text_table_col_alignment_type` | `1` | Table column alignment type [0 - strong, 1 - average, 2 - weak]. |
| `text_table_col_similarity_type` | `0` | Table column similarity type [0 - column alignment distance, 1 - element distance, 2 - element size, 3 - max]. |
| `text_table_col_distance` | `0.8` | Maximum deviation value for detection nearest distancies for table columns. Real distance in points. |
| `text_table_col_similarity` | `0.36` | Minimum similarity value when elements create table column. |
| `text_table_alignment_type` | `2` | Table column alignment type [0 - strong, 1 - average, 2 - weak]. Select strong for strictly aligned table elements. |
| `text_table_alignment_distance` | `0.4` | Maximum threshold value for detection text tables.  |
| `text_table_text_col_w1` | `1` | Text column paragraph weight. |
| `text_table_text_col_w2` | `1` | Text column width weight. |
| `text_table_text_col_width_min` | `0` | Minimal value of bbox width for text in table column. If zero, text_table_text_col_width_min_ratio is used. Size in points. |
| `text_table_text_col_width_min_ratio` | `1` | Minimal value of bbox width for text in table column multiply with average page font size. |
| `text_table_text_col_width_max` | `0` | Maximal value of bbox width for text in table column. If zero, text_table_text_col_width_max_ratio is used. Size in points. |
| `text_table_text_col_width_max_ratio` | `8` | Maximal value of bbox width for text in table column multiply with average page font size. |
| `text_table_image_col_w1` | `1` | Image column weight. |
| `text_table_image_col_gs` | `1` | If set to 1, image column has to have same graphics state. |
| `text_table_image_col_width_min` | `0` | Minimal value of bbox width for image in table column. If zero, text_table_image_col_width_min_ratio is used. Size in points. |
| `text_table_image_col_width_min_ratio` | `1` | Minimal value of bbox width for image in table column multiply with average page font size. |
| `text_table_image_col_width_max` | `0` | Maximal value of bbox width for image in table column. If zero, text_table_image_col_width_max_ratio is used. Size in points. |
| `text_table_image_col_width_max_ratio` | `4` | Maximal value of bbox width for image in table column multiply with average page font size. |
| `text_table_image_col_height_min` | `0` | Minimal value of bbox height for image in table column. If zero, text_table_image_col_height_min_ratio is used. |
| `text_table_image_col_height_min_ratio` | `1` | Minimal value of bbox height for image in table column multiply with average page font size. |
| `text_table_image_col_height_max` | `0` | Maximal value of bbox height for image in table column. If zero, text_table_image_col_height_max_ratio is used. |
| `text_table_image_col_height_max_ratio` | `2` | Maximal value of bbox height for image in table column multiply with average page font size. |
| `text_table_column_similarity` | `0.5` | Minimum similarity value when elements create table column. |
| `text_table_image_similarity_w1` | `1` | Sect table image similarity area weight. |
| `text_table_image_similarity_w2` | `1` | Sect table image similarity chart weight. |
| `text_table_image_similarity` | `0.7` | Minimum similarity value when text table is image normalized to interval [0,1]. |
| `text_table_paragraph_similarity` | `0.7` | Minimum similarity value when text table is paragraph normalized to interval [0,1]. |
| `table_update_delete_empty` | `1` | Delete empty rows and cols. |
| `table_update_split_by_cell` | `0` | Split elements that should be originally splitted, It usually happens when some paragraph is recognized instead of single lines or images(bullets) are joined together. |
| `table_update_split_by_row` | `0` | Split table texts to lines. |
| `table_update_split_label` | `0` | Split labels in tables. |
| `table_update_span_empty` | `1` | Span empty cells. |
| `table_update_span_row` | `0` | Join rows based on the maximum row span |
| `table_update_span_row_first` | `0` | If set to true, rows are merged together first using span |
| `table_update_join` | `0` | Join texts in a single cell. |
| `table_update_cell_header` | `1` | Detect headers. |
| `table_span_col_ratio` | `0.1` | Intersection percentage of colspan element. Possible values from interval [0,1]. |
| `table_span_row_ratio` | `0.2` | Intersection percentage of rowspan element. Possible values from interval [0,1]. |
| `table_alignment_h` | `1` | Maximum deviation (in points) of horizontal table aligned elements. |
| `table_alignment_v` | `4` | Maximum deviation (in points) of vertical table aligned elements. |
| `table_line_intersection` | `1` | Expansion (in points) for lines intersection. It's used in table detection. |
| `form_table_detect` | `1` | Recognize form fields as tables. |
| `caption_distance` | `80` | Distance of the caption and the image/table. |
| `caption_alignment_h` | `4` | Maximum deviation (in points) in caption and nearest element alignment. |
| `caption_alignment_v` | `4` | Maximum deviation (in points) in caption and nearest element alignment. |
| `mc_detect` | `1` | Update elements language, alternate description and actual text based on kb. Default value is set to 1 but can be turn to 0 due to optimization - when alternate description is not required. |
| `rd_sort` | `0` | Sort elements: 0 - inbuild, 1 - original content positions, 2 - by x and y coordinates. |
| `rd_sort_direction` | `0` | Sort elements: 0 - inbuild, 1 - prefere columns, 2 - prefere rows. |
| `rd_column_distance` | `0.8` | Maximum threshold value for columns detection. Real distance in points. |

Example:
```
{
  "template": {
    "pagemap": [
      {
        "text_table_similarity": 0.65,
        "text_table_text_col_w2": 1,
        "word_overlap": 0.9
      }
    ]
  }
}
```

## Regular Expressions
--

| key | value |
| - | - |
| `regex_hyphen` | `\\w+-$` |
| `regex_bullet` | `^[\\u2010\\u2011\\u2212\\u005E\\u005B\\ uF0A7\\uF097\\uF0BB\\u25CF\\u2022\\u25D8 \\u25CB\\u25D9\\u2023\\u2043\\uF0B7\\u22 12\\u204C\\u204D\\u25E6\\u29BE\\u29BF\\u 21E8\\u25BA\\u25C4\\u2219\\u25A0\\uF06C\ \u25A1\\u005D\\u25C6]$` |
| `regex_bullet_font` | `(Wingdings)\|(Symbol)` |
| `regex_label` | `^[\\[\\(]?((M{0,4}(CM\|CD\|D?C{0,3})(XC\|XL\|L?X{0,3})(IX\|IV\|V?I{0,3}))\|(\\d+)\|([a-zA-Z]))[\\)\\]\\. ]$` |
| `label_chars` | `.()[]` |
| `regex_decimal_numbering` | `^[\\[\\(]?(?:\\d{1,4}\\.){0,5}\\d{0,4}\\s?[\\)\\]\\.]?$` |
| `regex_roman_numbering` | `^[\\[\\(]?M{0,4}(CM\|CD\|D?C{0,3})(XC\|XL\|L?X{0,3})(IX\|IV\|V?I{0,3})[\\)\\]\\.]?$` |
| `regex_letter_numbering` | `^[\\[\\(]?[A-Za-z][\\)\\]\\.]$` |
| `regex_filling` | `[._]{2,}` |
| `regex_filling_chars` | `._` |
| `regex_page_number` | `(^\\d+$)\|(^M{0,4}(CM\|CD\|D?C{0,3})(XC\|XL\|L?X{0,3})(IX\|IV\|V?I{0,3})$)` |
| `regex_first_cap` | `^[A-Z]` |
| `regex_terminal` | `[\\.\\!\\?]$` |
| `regex_table_caption` | `((^table)\|(^tab\\.))` |
| `regex_image_caption` | `((^image)\|(^img\\.)\|(^figure)\|(^fig\ \.))` |
| `regex_chart_caption` | `((^chart)\|(^map))` |
| `regex_note_caption` | `((^source\\:)\|(^note\\:))` |
| `regex_toc_caption` | `((^content)\|(^toc))` |
| `regex_colon` | `:$` |
| `regex_comma` | `[,;]$` |
| `regex_letter` | `^[A-Za-z]$` |
| `number_chars` | `-+.,%\\u20AC$\\u00A5\\u00A3` |
| `numbering_splitter_chars` | `.()[]` |

Example:
```
{
  "template": {
    "pagemap_regex": [
      {
        "regex_letter_numbering": "^[\\[\\(]?[A-Za-z][\\)\\]\\.]$",
        "regex_filling": "[._]{2,}"
      }
    ]
  }
}
```

## Functions

### element_create

Create user-defined elements.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### object_update

The test is triggered when the page content object is tested.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_run_update

Updates a text run element after processing text objects.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_run_neighbours

This test is triggered when forming text lines from textrun.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### line_update

Updates a line element after detecting horizontal and vertical lines.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### rect_update

Updates a rectangle element after detecting rectangles.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_graphic_neighbours

Test if two neighbours path elements can form a single graphic table.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_graphic_update

Updates line, rects and graphic table element after detecting.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### word_update

Updates a word element after detecting words.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### word_neighbours

This test is triggered when forming text lines from words.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_line_update

Updates a text line element after detecting text lines.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_line_neighbours

Test if two neighbours text lines can form a paragraph.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_update

Updates the text element after detecting paragraphs.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### image_update

Updates an image after detecting basic images from page objects.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_update

Updates an element after detecting basic elements.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### table_update

Updates a table after the whole process od table detection is done.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### cell_update

Updates a table cell after the whole process od table detection is done.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### table_split

Updates the table after the entire table detection process is completed.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### alt_update

Sets an alternate description for the element. The alternate description is established in a specific order. To skip a step, set the default value to false for that step.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### actual_text_update

Sets the actual text for the element. The actual text is established in a specific order. To skip a step, set the default value to false for that step.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### artifact_update

Marks an element as an artifact.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### label_update

Update elements marked as labels to include them as part of the list.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### list_update

Tests if a list is correct.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_image

Handles the process of tagging images. For repurposing and accessibility purposes, a Figure element should have either an Alt entry or an ActualText entry in its structure element dictionary. If both are absent, the default behavior is to tag the Figure with an empty alt attribute.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_table

Handles the process of tagging tables. For repurposing and accessibility purposes, a table should have headers. If no headers are detected, the default behavior is to leave the table without any <th> elements.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_update

Updates the tag after it has been created..

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### annot_update

Updates the annotation tag after it has been created.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

## Schema

### statement

The if statement type of the query. According to the statement the query evaluation stops upon pass or not.

- _values:_ 
  - `['$if', '$elif', '$else']`
- _defaule value:_ $if

_keys and values:_
- "$if"
- "$elif"
- "$else"

### $if

Can by used in all functions. Applies a rule when a condition is true.

- _type:_ statement

### $elif

Can by used in all functions. Applies a rule when a condition is true.

- _type:_ statement

### $else

Can by used in all functions. Applies a rule when a condition is not true.

- _type:_ statement

### query

The query defines thresholds and operations for a pagemap detection.

- _type:_ query

_keys and values:_
- "[param](#param)"
_params:_
  - "[pds_object_params](#pds_object_params)" 
    - A parameter that represents PdsObject. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pde_element_params](#pde_element_params)" 
    - A parameter that represents PdeElement. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pds_struct_elem_params](#pds_struct_elem_params)" 
    - A parameter that represents PdsStructElem. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pdf_annot_params](#pdf_annot_params)" 
    - A parameter that represents PdfAnnots. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pdf_rect](#pdf_rect)" 

  - "[pdf_rgb](#pdf_rgb)" 

  - "[int](#int)" 
    - Parameter that represents integer.
  - "[bool](#bool)" 
    - Parameter that represents boolean value.
  - "[float](#float)" 
    - Parameter that represents floating value.
  - "[string](#string)" 
    - Parameter that represents string value.
- "[var](#var)"
_params:_
  - "0_value" 

- "[logical_operators](#logical_operators)"

### param

Define the number and type of input parameters.

- _type:_ query_param

_keys and values:_
- "[pds_object_params](#pds_object_params)"
- "[pde_element_params](#pde_element_params)"
- "[pds_struct_elem_params](#pds_struct_elem_params)"
- "[pdf_annot_params](#pdf_annot_params)"
- "[pdf_rect](#pdf_rect)"
- "[pdf_rgb](#pdf_rgb)"
- "[int](#int)"
- "[bool](#bool)"
- "[float](#float)"
- "[string](#string)"

### int

Parameter that represents integer.

- _type:_ int

### bool

Parameter that represents boolean value.

- _type:_ bool

### float

Parameter that represents floating value.

- _type:_ float

### string

Parameter that represents string value.

- _type:_ string

### var

User defined variables. Use macros to define variables

- _type:_ var

_keys and values:_
- "0_value"

### logical_operators

Available logical operators.

- _type:_ string
- _values:_ 
  - `['$and', '$or', '$not']`

_keys and values:_
- "$and"
_params:_
  - "$and" 

  - "$or" 

  - "$not" 

  - "[condition](#condition)" 

- "$or"
_params:_
  - "$and" 

  - "$or" 

  - "$not" 

  - "[condition](#condition)" 

- "$not"
_params:_
  - "$and" 

  - "$or" 

  - "$not" 

  - "[condition](#condition)" 


### $and

Logical AND. All sub-conditions must be true.

- _type:_ logical_operator

_keys and values:_
- "$and"
- "$or"
- "$not"
- "[condition](#condition)"

### $or

Logical OR. At least one sub-condition must be true.

- _type:_ logical_operator

_keys and values:_
- "$and"
- "$or"
- "$not"
- "[condition](#condition)"

### $not

Logical NOT.

- _type:_ logical_operator

_keys and values:_
- "$and"
- "$or"
- "$not"
- "[condition](#condition)"

### comparison_operators

Available comparison operators.

- _type:_ string
- _values:_ 
  - `['$eq', '$ne', '$lt', '$lte', '$gt', '$gte', '$regex', '$in', '$nin']`

_keys and values:_
- "$eq"
- "$ne"
- "$lt"
- "$lte"
- "$gt"
- "$gte"
- "$regex"
- "$in"
- "$nin"

### $eq

Equal to value.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)", "[string](#string)", "[bool](#bool)"]

### $ne

Not equal to value.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)", "[string](#string)", "[bool](#bool)"]

### $lt

Less then value.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $lte

Less or equals then value.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $gt

Greater then value

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $gte

Greater or equals then value.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $regex

Regular expression predicate.

- _type:_ comparison_operator
- _types:_ ["[string](#string)"]

### $in

Contain value operator.

- _type:_ comparison_operator
- _types:_ ["[bbox](#bbox)"]

### $nin

Not contain value operator.

- _type:_ comparison_operator
- _types:_ ["[bbox](#bbox)"]

### pds_object_params

List of all pds_object types, can be used as parameter in QUERY->PARAM.


_keys and values:_
- "[pds_text](#pds_text)"
_params:_
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[children_num](#children_num)" 

  - "[artifact](#artifact)" 

  - "[mcid](#mcid)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[text](#text)" 

- "[pds_path](#pds_path)"
- "[pds_image](#pds_image)"
- "[pds_shading](#pds_shading)"
- "[pds_form](#pds_form)"
- "[pds_object](#pds_object)"
_params:_
  - "[type](#type)" 
    - Type of PdsObject.
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[children_num](#children_num)" 

  - "[artifact](#artifact)" 

  - "[mcid](#mcid)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[text](#text)" 


### pds_text

Text page object


_keys and values:_
- "[width](#width)"
- "[height](#height)"
- "[left](#left)"
- "[right](#right)"
- "[top](#top)"
- "[bottom](#bottom)"
- "[bbox](#bbox)"
_params:_
  - "[left](#left)" 

  - "[bottom](#bottom)" 

  - "[right](#right)" 

  - "[top](#top)" 

- "[has_fill](#has_fill)"
- "[has_stroke](#has_stroke)"
- "[fill_color](#fill_color)"
- "[stroke_color](#stroke_color)"
- "[children_num](#children_num)"
- "[artifact](#artifact)"
- "[mcid](#mcid)"
- "[font_size](#font_size)"
- "[font_name](#font_name)"
- "[text](#text)"

### pds_struct_elem_params

List of all pds_tag types, can be used as parameter in QUERY->PARAM.


_keys and values:_
- "[pds_struct_elem](#pds_struct_elem)"
_params:_
  - "[type](#type)" 
    - Type of PdsTag.
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[tag_type](#tag_type)" 

  - "[role_mapped_tag_type](#role_mapped_tag_type)" 

  - "[parent_tag_type](#parent_tag_type)" 

  - "[children_tag_type](#children_tag_type)" 

  - "[id](#id)" 

  - "[title](#title)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[text](#text)" 

  - "[expansion](#expansion)" 

  - "[children_num](#children_num)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[has_content](#has_content)" 

  - "[row_num](#row_num)" 

  - "[col_num](#col_num)" 

  - "[cell_column](#cell_column)" 

  - "[cell_row](#cell_row)" 

  - "[cell_row_span](#cell_row_span)" 

  - "[cell_column_span](#cell_column_span)" 

  - "[cell_scope](#cell_scope)" 


### pdf_annot_params

List of all pdf_annot types, can be used as parameter in QUERY->PARAM.


_keys and values:_
- "[pdf_annot](#pdf_annot)"
_params:_
  - "[type](#type)" 
    - Type of PdfAnnot.
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[annot_type](#annot_type)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[contents](#contents)" 

  - "[annot_flag](#annot_flag)" 


### pde_element_params

List of all pde_element types, can be used as parameter in QUERY->PARAM.


_keys and values:_
- "[pde_text](#pde_text)"
_params:_
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[baseline_x](#baseline_x)" 

  - "[baseline_y](#baseline_y)" 

  - "[bbox](#bbox)" 

  - "[label](#label)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[text](#text)" 

  - "[angle](#angle)" 

  - "[heading](#heading)" 

  - "[name](#name)" 

- "[pde_text_line](#pde_text_line)"
- "[pde_word](#pde_word)"
- "[pde_text_run](#pde_text_run)"
- "[pde_image](#pde_image)"
_params:_
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[label](#label)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[children_num](#children_num)" 

  - "[object_num](#object_num)" 

  - "[name](#name)" 

- "[pde_container](#pde_container)"
- "[pde_list](#pde_list)"
- "[pde_rect](#pde_rect)"
- "[pde_cell](#pde_cell)"
_params:_
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[text](#text)" 

  - "[cell_column](#cell_column)" 

  - "[cell_row](#cell_row)" 

  - "[cell_row_span](#cell_row_span)" 

  - "[cell_column_span](#cell_column_span)" 

  - "[cell_scope](#cell_scope)" 

  - "[children_num](#children_num)" 

  - "[name](#name)" 

- "[pde_toc](#pde_toc)"
- "[pde_header](#pde_header)"
- "[pde_footer](#pde_footer)"
- "[pde_line](#pde_line)"
_params:_
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[label](#label)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[name](#name)" 

- "[pde_form_field](#pde_form_field)"
- "[pde_annot](#pde_annot)"
- "[pde_table](#pde_table)"
_params:_
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[label](#label)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[row_num](#row_num)" 

  - "[col_num](#col_num)" 

  - "[cell_header](#cell_header)" 

  - "[table_type](#table_type)" 

  - "[isolated_num](#isolated_num)" 
    - Number of isolated elements in the table.
  - "[name](#name)" 

- "[pde_element](#pde_element)"
_params:_
  - "[type](#type)" 

  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[baseline_x](#baseline_x)" 

  - "[baseline_y](#baseline_y)" 

  - "[bbox](#bbox)" 

  - "[label](#label)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[angle](#angle)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[flag](#flag)" 

  - "[name](#name)" 


### general_vars

General variables can be used without parameters. It represents general state during the processing. It contains information about the current page and the document and can be used in any query.

- _type:_ string

_keys and values:_
- "$page_num"
- "$page_width"
- "$page_height"
- "$page_font_size"
- "$page_min_font_size"
- "$page_max_font_size"
- "$page_rotation"
- "$page_rtl"
- "$page_anchor"
- "$doc_num_pages"
- "$doc_lang"
- "$doc_title"
- "$doc_anchor"

### $page_num

Page number.

- _type:_ int

### $page_width

Page cropbox width.

- _type:_ float

### $page_height

Page cropbox height.

- _type:_ float

### $page_font_size

Average font size on the page.

- _type:_ float

### $page_min_font_size

Minimal font size on the page.

- _type:_ float

### $page_max_font_size

Maximal font size on the page.

- _type:_ float

### $page_rotation

Page rotation.

- _type:_ int
- _values:_ 
  - `[0, 90, 180, 270]`

### $page_rtl

Page contains RTL content.

- _type:_ bool

### $page_anchor

Page already detected anchors.

- _type:_ string

### $doc_num_pages

Document number of pages.

- _type:_ int

### $doc_lang

Document language.

- _type:_ string

### $doc_title

Document title.

- _type:_ string

### $doc_anchor

Document already detected anchors.

- _type:_ string

### values

General values used in JSON default template.


_keys and values:_
- "[type](#type)"
- "[alt](#alt)"
- "[actual_text](#actual_text)"
- "[lang](#lang)"
- "[id](#id)"
- "[associated_header](#associated_header)"
- "[expansion](#expansion)"
- "[has_content](#has_content)"
- "[tag_type](#tag_type)"
- "[parent_tag_type](#parent_tag_type)"
- "[children_tag_type](#children_tag_type)"
- "[annot_type](#annot_type)"
- "[contents](#contents)"
- "[annot_flag](#annot_flag)"
- "[title](#title)"
- "[name](#name)"
- "[angle](#angle)"
- "[bbox](#bbox)"
_params:_
  - "[left](#left)" 

  - "[bottom](#bottom)" 

  - "[right](#right)" 

  - "[top](#top)" 

- "[cell_column](#cell_column)"
- "[cell_row](#cell_row)"
- "[cell_row_span](#cell_row_span)"
- "[cell_column_span](#cell_column_span)"
- "[cell_scope](#cell_scope)"
- "[col_num](#col_num)"
- "[children_num](#children_num)"
- "[object_num](#object_num)"
- "[artifact](#artifact)"
- "[mcid](#mcid)"
- "[has_fill](#has_fill)"
- "[fill_color](#fill_color)"
_params:_
  - "[red](#red)" 

  - "[green](#green)" 

  - "[blue](#blue)" 

- "[has_stroke](#has_stroke)"
- "[stroke_color](#stroke_color)"
_params:_
  - "[red](#red)" 

  - "[green](#green)" 

  - "[blue](#blue)" 

- "[flag](#flag)"
- "[numbering](#numbering)"
- "[single_instance](#single_instance)"
- "[word_space](#word_space)"
- "[font_name](#font_name)"
- "[font_size](#font_size)"
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"
- "[cell_header](#cell_header)"
- "[cell_associated_header](#cell_associated_header)"
- "[heading](#heading)"
- "[width](#width)"
- "[height](#height)"
- "[label](#label)"
- "[left](#left)"
- "[right](#right)"
- "[top](#top)"
- "[bottom](#bottom)"
- "[baseline_x](#baseline_x)"
- "[baseline_y](#baseline_y)"
- "[pdf_rect](#pdf_rect)"
_params:_
  - "[left](#left)" 

  - "[bottom](#bottom)" 

  - "[right](#right)" 

  - "[top](#top)" 

- "[pdf_rgb](#pdf_rgb)"
_params:_
  - "[red](#red)" 

  - "[green](#green)" 

  - "[blue](#blue)" 

- "[reflow](#reflow)"
- "[row_num](#row_num)"
- "[table_type](#table_type)"
- "[text](#text)"
- "[text_flag](#text_flag)"
- "[text_line_flag](#text_line_flag)"
- "[text_state_flag](#text_state_flag)"
- "[word_flag](#word_flag)"

### type

Type.

- _type:_ string
- _values:_ 
  - `['pds_object', 'pds_text', 'pds_path', 'pds_image', 'pds_shading', 'pds_form', 'pde_element', 'pde_text', 'pde_text_line', 'pde_word', 'pde_text_run', 'pde_image', 'pde_container', 'pde_list', 'pde_line', 'pde_rect', 'pde_table', 'pde_cell', 'pde_toc', 'pde_header', 'pde_footer', 'pde_form_field', 'pde_annot', 'pds_struct_elem', 'pdf_annot']`

### alt

Alternate description typically used for Figure tags.

- _type:_ string

### actual_text

Actual text.

- _type:_ string

### lang

The language identifier.

- _type:_ string

### id

The unique identifier of the tag.

- _type:_ string

### associated_header

The unique identifier of the associated header. For more associated headers use composed string a|b|c|d

- _type:_ string

### expansion

The expanded form of an abbreviation.

- _type:_ string

### has_content

A value identifying whether the object or tag has associated page content.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### tag_type

Tag type defined by a string or regular expression. Use .* to match all tags.

- _type:_ string
- _values:_ 
  - `['Annot', 'Art', 'Artifact', 'Aside', 'BibEntry', 'BlockQuote', 'Caption', 'Code', 'Div', 'Document', 'DocumentFragment', 'Em', 'FENote', 'Figure', 'Form', 'Formula', 'H', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Index', 'L', 'Lbl', 'LBody', 'LI', 'Link', 'NonStruct', 'Note', 'P', 'Part', 'Private', 'Quote', 'RB', 'Reference', 'RP', 'RT', 'Ruby', 'Sect', 'Span', 'Strong', 'Sub', 'Table', 'TBody', 'TD', 'TFoot', 'TH', 'THead', 'Title', 'TOC', 'TOCI', 'TR', 'Warichu', 'WP', 'WT']`

### annot_type

Annotation type defined by a string or regular expression. Use .* to match all annotations.

- _type:_ string
- _values:_ 
  - `['Text', 'Link', 'FreeText', 'Line', 'Square', 'Circle', 'Polygon', 'PolyLine', 'Highlight', 'Underline', 'Squiggly', 'StrikeOut', 'Stamp', 'Caret', 'Ink', 'Popup', 'FileAttachment', 'Sound', 'Movie', 'Widget', 'Screen', 'PrinterMark', 'TrapNet', 'Watermark', '3D', 'Redact', 'Projection', 'RichMedia']`

### contents

A string value specifying the annotation contents.

- _type:_ string

### annot_flag

A comma-delimited string value specifying the annotation flags.

- _type:_ string
- _values:_ 
  - `['invisible', 'hidden', 'print', 'no_zoom', 'no_rotate', 'no_view', 'read_only', 'locked', 'toggle', 'contents']`

### title

Title.

- _type:_ string

### name

Unique name to identify element later.

- _type:_ string

### angle

Angle.

- _type:_ float

### bbox

Parameter that represents the bounding box of an object, formatted as an array: [left, bottom, right, top]. Each coordinate can be defined by a float number, general variables, anchor variables, or mathematical functions with previously defined variables. Each bounding box can be associated with only one anchor.

- _type:_ bbox

_keys and values:_
- "[left](#left)"
- "[bottom](#bottom)"
- "[right](#right)"
- "[top](#top)"

### cell_column

The column number of the cell in the table.

- _type:_ int

### cell_row

The row number of the cell in the table.

- _type:_ int

### cell_row_span

The cell row span.

- _type:_ int

### cell_column_span

The cell column span.

- _type:_ int

### cell_scope

The cell scope.

- _type:_ string
- _values:_ 
  - `['row', 'column', 'both']`

### col_num

Number of columns in the table.

- _type:_ int

### children_num

Number of associated child objects.

- _type:_ int

### object_num

Number of associated page objects.

- _type:_ int

### artifact

True if object has content mark Artifact, false otherwise.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### mcid

MCID content mark number is exists, -1 otherwise.

- _type:_ int

### has_fill

True if fill color is set

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### fill_color

The fill color of an object.

- _type:_ rgb

_keys and values:_
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"

### has_stroke

True if stroke color is set

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### stroke_color

The stroke color of an object.

- _type:_ rgb

_keys and values:_
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"

### flag

The flag value defines a specific property for an object, which is essential for further processing.

- _type:_ string
- _values:_ 
  - `['no_join', 'no_split', 'artifact', 'header', 'footer', 'splitter', 'no_table', 'no_image', 'no_expand', 'continuous', 'anchor']`

### numbering

Set the list numbering attribute.

- _type:_ string
- _values:_ 
  - `['None', 'Unordered', 'Disc', 'Circle', 'Square', 'Ordered', 'Decimal', 'UpperRoman', 'LowerRoman', 'UpperAlpha', 'LowerAlpha', 'Description']`

### single_instance

Properties that are compared delimited by |. If the element with same properties already exists, only first instance is tagged.

- _type:_ string
- _values:_ 
  - `['type', 'width', 'height', 'left', 'right', 'top', 'bottom', 'bbox', 'font_size', 'font_name', 'text', 'fill_color', 'stroke_color', 'angle', 'alt', 'actual_text', 'flag', 'word_flag', 'text_line_flag', 'text_flag', 'lang', 'cell_column', 'cell_row', 'cell_column_span', 'cell_row_span', 'cell_scope', 'row_num', 'col_num']`

### word_space

Update words space for the font in points.

- _type:_ float

### font_name

The name of the font used in the text object.

- _type:_ string

### font_size

The size of the font used in the text object.

- _type:_ float

### red

The red component of an RGB color.

- _type:_ int

### green

The green component of an RGB color.

- _type:_ int

### blue

The blue component of an RGB color.

- _type:_ int

### cell_header

Marks the object as a table header.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### cell_associated_header

Cell associated headers delimited by |.

- _type:_ string

### heading

Sets the text heading style.

- _type:_ string
- _values:_ 
  - `['normal', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'note', 'title']`

### width

The object's width dimension.

- _type:_ float

### height

The object's height dimension.

- _type:_ float

### label

Marks the element as a list label.

- _type:_ string
- _values:_ 
  - `['label', 'li_1', 'li_2', 'li_3', 'li_4', 'label_no']`

### left

The left coordinate of the object.

- _type:_ float

### right

The left coordinate of the object.

- _type:_ float

### top

The top coordinate of the object.

- _type:_ float

### bottom

The bottom coordinate of the object.

- _type:_ float

### baseline_x

The baseline x coordinate of the text object.

- _type:_ float

### baseline_y

The baseline y coordinate of the text object.

- _type:_ float

### pdf_rect

Parameter that represents the bounding box of an object, formatted as an array: [left, bottom, right, top].

- _type:_ rec

_keys and values:_
- "[left](#left)"
- "[bottom](#bottom)"
- "[right](#right)"
- "[top](#top)"

### pdf_rgb

Parameter that represents the RGB color of an object, formatted as an array: [red, green, blue].

- _type:_ rgb

_keys and values:_
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"

### reflow

Text reflow. If set to false, each line is treated as a new line.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### row_num

The number of rows in the table.

- _type:_ int

### table_type

The table type represented as a value from the PdfTableType enum.

- _type:_ string
- _values:_ 
  - `['graphic', 'isolated', 'row', 'col', 'form']`

### text

The text to be used as a value.

- _type:_ string

### text_flag

The flag to be used for the text element, specifying a value similar to the regex flags.

- _type:_ string
- _values:_ 
  - `['table_caption', 'image_caption', 'chart_caption', 'note_caption', 'filling', 'uppercase', 'new_line', 'no_new_line']`

### text_line_flag

The flag to be used for the text line element, specifying a value similar to the regex flags.

- _type:_ string
- _values:_ 
  - `['hyphen', 'new_line', 'indent', 'terminal', 'drop_cap', 'filling', 'uppercase', 'no_new_line']`

### text_state_flag

The flag to be used for the text text_state_flag.

- _type:_ string
- _values:_ 
  - `['underline', 'strikeout', 'highlight', 'subscript', 'superscript', 'no_unicode', 'white_space', 'unicode']`

### word_flag

The flag to be used for the word element, specifying a value similar to the regex flags.

- _type:_ string
- _values:_ 
  - `['hyphen', 'bullet', 'colon', 'number', 'subscript', 'superscript', 'terminal', 'capital', 'image', 'decimal_num', 'roman_num', 'letter_num', 'page_num', 'filling', 'uppercase', 'comma', 'no_unicode']`

### suffix

Container holding all unique suffixes used for naming in JSON default template


_keys and values:_

### condition

Conditions types used in the query


_keys and values:_
- "[condition_value](#condition_value)"
- "[comparison](#comparison)"
_params:_
  - "$eq" 

- "[comparison_array](#comparison_array)"
_params:_
  - "$gt" 

  - "$lt" 


### condition_value

{0_width : 100}


### comparison

{0_width : {$lt : 100}


_keys and values:_
- "$eq"

### comparison_array

{0_width : [{$lt : 100}, {$gt : 100}, ...]}


_keys and values:_
- "$gt"
- "$lt"

### keywords

Container holding all unique keywords used in JSON default template


_keys and values:_
- "[general](#general)"
- "[template](#template)"
- "[query](#query)"
- "[param](#param)"
- "[statement](#statement)"
- "[disable](#disable)"
- "[purpose](#purpose)"

### general

Holding general data like: version, date, id, SDK version, ...


### template

Holding all functions.


### query

Can be used in all functions. Each QUERY must have child PARAM, which holding array of parameters to specified query objects.


### param

Child of the QUERY. Each QUERY must include a PARAM that specifies the object types used for evaluation.

- _type:_ array_param

### statement

The if statement should be used in function nodes. Based on the statement, the query evaluation stops upon pass or fail. If the if statement is not present, the condition is considered disabled.

- _type:_ string
- _values:_ 
  - `['$if', '$elif', '$else']`

### disable

Can by used in all main functions nodes. If value is true, node is not executed. Default value is false

- _type:_ bool
- _values:_
  - `['true', 'false']`

### purpose

Describes the user-defined purpose or description of the QUERY.

- _type:_ string

### insert

Values to be added as the default for the node.


_keys and values:_
- "[elements_add_value](#elements_add_value)"
- "[elements_add_cell](#elements_add_cell)"

### math_expressions

Mathemical functions to define custom variable.

- _type:_ string
- _values:_ 
  - `['SUM()', 'MINUS()', 'ABS()', 'MULTIPLY()', 'DIVIDE()', 'MIN()', 'MAX()', 'MOD()', 'FLOOR()', 'CEILING()']`

