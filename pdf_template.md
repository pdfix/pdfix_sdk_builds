# PDFix Template

--

## Table of Contents

- [Settings](#Settings)
- [Threshold Values](#threshold-values)
- [Regular Expressions](#regular-expressions)
- [Functions](#functions)

## General Settings
General template settings

| key | type | value |
| - | - | - |
| `retain_pdfua` | bool | True |
| `page_tag` | string | NonStruct |
| `substructure_form_XObject` | bool | True |

Example:
```
{
  "template": {
    "settings": {
      "retain_pdfua": true,
      "page_tag": "NonStruct",
      "substructure_form_XObject": true
    }
  }
}
```

## Threshold Values
--

| key | value | desciption |
| - | - | - |
| `preflight_columns` | `1` | Preflight colums druring preflight method. Set to 0 if this information is not required. |
| `preflight_column_width_distance` | `20` | Columns width detection precision. |
| `preflight_column_alignment_distance` | `4` | Columns alignment detection precision. |
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
| `bbox_expansion` | `4` | Bounding box expansion - half of kTrTextHeight. |
| `angle_deviation` | `0.015707963267949` | Maximum angle deviation for horizontal and vertical elements. |
| `header_ratio` | `0.15` | Maximum percentage of a header height. Possible values from interval [0,1]. |
| `footer_ratio` | `0.15` | Maximum percentage of a footer height. Possible values from interval [0,1]. |
| `artifact_w1` | `1` | Artifact page border distance weight. |
| `artifact_w2` | `1` | Artifact image area weight. |
| `artifact_border_distance_max` | `2` | Maximum distance of artifact to page border. |
| `artifact_font_size` | `40` | All texts with font size bigger then this is artifact. |
| `artifact_similarity` | `0.7` | Minimum similarity value when object or element is an artifact normalized to interval [0,1]. |
| `object_intersection` | `0.1` | Expansion for page objects intersection. |
| `object_isolated` | `16` | Maximum isolated object heigh and width. It's used for joining isolated objects. |
| `path_object_max` | `2000` | Maximum number of subsequence path objects that are still paths. |
| `path_object_min` | `100` | Minimum number of subsequence path objects that are still paths. |
| `isolated_text_ratio` | `10` | Maximum isolated text width ratio. Is multiplied with the font size. |
| `isolated_text` | `80` | Maximum isolated text width. |
| `isolated_element_ratio` | `6` | Maximum isolated element width/height ratio. Is multiplied with the font size. |
| `initial_element_expansion` | `0` | Initial element bounding box expansion when searching children. Size in points. If its zero, a half of default page font size is used. |
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
| `rect_image_similarity` | `0.7` | Minimum similarity value when rectangle is image normalized to interval [0,1]. |
| `image_background_text` | `1` | Text bounding box expansion. |
| `image_overlap_distance` | `1` | Maximum distance value when graphic page objects can be joined. Distance in points. |
| `image_join_distance` | `8` | Maximum distance value when graphic page objects can be joined. Distance in points. |
| `char_clip_ratio` | `0.5` | Minimal ratio of the clipping area of the character comparing to it's original size. |
| `word_space_width_ratio` | `0.6` | Default char space width ratio (percentage) based on the font size. |
| `word_space_width_min_ratio` | `0.1` | Minimal acceptable space width ratio. |
| `word_space_type` | `0` | The space's advance width detection type. If 0, font space width is calculated as average of all characters widths. If -1, maximum width is used. If -2, space character width is used. If there is a number greater then 0, font size(em) multiplied by this number is used. |
| `word_space_distance_max` | `0` | Maximum distance between chunks. If zero, word_space_distance_max_ratio is used. Size in points. |
| `word_space_distance_max_ratio` | `10` | Maximum distance between chunks. The value is multiplied by simple word spacing between words. |
| `word_space_update` | `0.1` | Maximum distance of word spacing. Size in points. |
| `word_distance` | `0` | Maximum distance value in word spacing detection. If zero, word_distance_ratio is used. Size in points. |
| `word_distance_ratio` | `0.1` | Maximum distance value in word spacing detection. The value is multiplied by word font size. |
| `word_space_splitter_ratio` | `2` | Minimum space before splitter. The value is multiplied by most used font size. |
| `word_splitter_distance` | `4` | Maximum threshold value for word splitters detections. Real distance in points. |
| `text_line_baseline_ratio` | `0.1` | Maximum baseline shift. Value multiplies minimal font. Baseline shift moves individual characters up or down in relation to other text on the same line. |
| `text_line_underline_distance` | `2.6` | Distance of the underline line and text baseline. Size in points. |
| `text_line_underline_char_distance_ratio` | `0.1` | Distance of the underline line start/end point and character bounding box. The value is multiplied by line font size. Size in points. |
| `text_line_subscript_space_ratio` | `0.5` | Subscript space multiplied with word space. |
| `text_line_subscript_font_ratio` | `1` | Mamimum subscript font size multiplied with line font size. |
| `text_line_subscript_len` | `6` | Maximum number of characters in subscript. |
| `text_line_join_font_size_distance` | `0` | Distance of two fonts in points, when two lines with different fonts can be join. |
| `text_line_distance_max` | `0` | Maximum distance between lines. If zero, text_line_distance_max_ratio is used. Size in points. |
| `text_line_distance_max_ratio` | `3.6` | Maximum distance between lines. The value is multiplied by line font size. |
| `text_line_join_distance` | `2` | Maximum threshold value in line spacing detection for specific font size. The higher value allows creating paragraph with variable line spacings. The value is multiplied by font size. |
| `text_chunk_distance_max` | `0` | Maximum distance between chunks. If zero, text_chunk_distance_max_ratio is used. Size in points. |
| `text_chunk_distance_max_ratio` | `6` | Maximum distance between chunks. The value is multiplied by simple word spacing between words. |
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
| `text_heading_h1` | `0` | Minimal font size for H1. |
| `text_heading_h2` | `0` | Minimal font size for H2. |
| `text_heading_h3` | `0` | Minimal font size for H3. |
| `text_column_similarity` | `0.7` | Minimum similarity value that text creates a column normalized to interval [0,1]. |
| `label_alignment_h` | `2` | Maximum deviation of horizontal label alignment. |
| `label_distance_ratio` | `10` | Distance of the label and text. Is multiplied with the page most used font size. |
| `label_baseline_ration` | `0.14` | Multiplies minimal font. Maximum deviation of horizontal label aligned to text. |
| `label_image_w1` | `1` | Labels alignment weight. Accepted only if labels overlap. |
| `label_image_w2` | `1` | Labels and sibling distance weight. |
| `label_image_w3` | `1` | Siblings font size difference weight. Accepted only if it's not equal. |
| `label_image_w4` | `0.25` | Labels width difference weight. |
| `label_image_w5` | `0.25` | Labels height difference weight. |
| `label_image_w6` | `1` | Label and sibling height weight. |
| `label_image_w7` | `1` | Label width weight. |
| `label_image_w8` | `0` | Labels type weight. If set to 1, accept only same type labels. |
| `label_image_w9` | `0` | Labels graphic state weight. If set to 1, labels have to have same graphics state. |
| `label_image_w10` | `0` | Siblings text state weight. If set to 1, siblings have to have same text state. |
| `label_image_width_min` | `0` | Minimal value of bbox width for label object. If zero, label_image_width_min_ratio is used. Size in points. |
| `label_image_width_min_ratio` | `1` | Minimal value of bbox width for label objec multiply with average page font size. |
| `label_image_width_max` | `0` | Maximal value of bbox width for label object. If zero, label_image_width_max_ratio is used. Size in points. |
| `label_image_width_max_ratio` | `6` | Maximal value of bbox width for label object multiply with average page font size. |
| `label_image_distance` | `8` | Minimum distance value when graphic page object is label. Distance in points. |
| `label_word_w1` | `1` | Labels alignment weight. |
| `label_word_w2` | `1` | Labels and sibling distance weight. |
| `label_word_distance` | `0` | Maximum distance value when a word is a label. Distance in points. |
| `label_word_distance_ratio` | `1` | Maximum distance value when a word is a label. The value is multiplied by avarage page font width. |
| `label_sibling_dist_ratio` | `1.2` | Minimum distance of left lebel sibling. Ratio is multiplied with right sibling distance. |
| `toc_word_w1` | `1` | Tocs words alignment weight. |
| `toc_word_distance` | `0.6` | Minimum distance value when word is a label. Distance in points. |
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
| `sect_table_row_alignment_type` | `1` | Table row alignment type [0 - strong, 1 - average, 2 - weak]. |
| `sect_table_col_alignment_type` | `1` | Table column alignment type [0 - strong, 1 - average, 2 - weak]. |
| `sect_table_col_similarity_type` | `0` | Table column similarity type [0 - column alignment distance, 1 - element distance, 2 - element size, 3 - max]. |
| `sect_table_col_distance` | `0.8` | Maximum deviation value for detection nearest distancies for table columns. Real distance in points. |
| `sect_table_col_similarity` | `0.36` | Minimum similarity value when elements create table column. |
| `sect_table_alignment_type` | `2` | Table column alignment type [0 - strong, 1 - average, 2 - weak]. Select strong for strictly aligned table elements. |
| `sect_table_alignment_distance` | `0.4` | Maximum threshold value for detection section tables.  |
| `sect_table_text_col_w1` | `1` | Text column paragraph weight. |
| `sect_table_text_col_w2` | `1` | Text column width weight. |
| `sect_table_text_col_width_min` | `0` | Minimal value of bbox width for text in table column. If zero, sect_table_text_col_width_min_ratio is used. Size in points. |
| `sect_table_text_col_width_min_ratio` | `1` | Minimal value of bbox width for text in table column multiply with average page font size. |
| `sect_table_text_col_width_max` | `0` | Maximal value of bbox width for text in table column. If zero, sect_table_text_col_width_max_ratio is used. Size in points. |
| `sect_table_text_col_width_max_ratio` | `8` | Maximal value of bbox width for text in table column multiply with average page font size. |
| `sect_table_image_col_w1` | `1` | Image column weight. |
| `sect_table_image_col_gs` | `1` | If set to 1, image column has to have same graphics state. |
| `sect_table_image_col_width_min` | `0` | Minimal value of bbox width for image in table column. If zero, sect_table_image_col_width_min_ratio is used. Size in points. |
| `sect_table_image_col_width_min_ratio` | `1` | Minimal value of bbox width for image in table column multiply with average page font size. |
| `sect_table_image_col_width_max` | `0` | Maximal value of bbox width for image in table column. If zero, sect_table_image_col_width_max_ratio is used. Size in points. |
| `sect_table_image_col_width_max_ratio` | `4` | Maximal value of bbox width for image in table column multiply with average page font size. |
| `sect_table_image_col_height_min` | `0` | Minimal value of bbox height for image in table column. If zero, sect_table_image_col_height_min_ratio is used. |
| `sect_table_image_col_height_min_ratio` | `1` | Minimal value of bbox height for image in table column multiply with average page font size. |
| `sect_table_image_col_height_max` | `0` | Maximal value of bbox height for image in table column. If zero, sect_table_image_col_height_max_ratio is used. |
| `sect_table_image_col_height_max_ratio` | `2` | Maximal value of bbox height for image in table column multiply with average page font size. |
| `sect_table_column_similarity` | `0.5` | Minimum similarity value when elements create table column. |
| `sect_table_image_similarity_w1` | `1` | Sect table image similarity area weight. |
| `sect_table_image_similarity_w2` | `1` | Sect table image similarity chart weight. |
| `sect_table_image_similarity` | `0.7` | Minimum similarity value when section table is image normalized to interval [0,1]. |
| `sect_table_paragraph_similarity` | `0.7` | Minimum similarity value when section table is paragraph normalized to interval [0,1]. |
| `table_span_col_ratio` | `0.1` | Intersection percentage of colspan element. Possible values from interval [0,1]. |
| `table_span_row_ratio` | `0.2` | Intersection percentage of rowspan element. Possible values from interval [0,1]. |
| `table_alignment_h` | `1` | Maximum deviation (in points) of horizontal table aligned elements. |
| `table_alignment_v` | `4` | Maximum deviation (in points) of vertical table aligned elements. |
| `table_line_intersection` | `1` | Expansion (in points) for lines intersection. It's used in table detection. |
| `table_detect_form` | `1` | Recognize form fields as tables. |
| `table_detect_sect` | `1` | Texts (not graphic) tables detection. Possible values: 0 | 1. If 0 is set, it prevents generating tables from isolated chunk of text. |
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
        "element_isolated_width_min": 0,
        "graphic_table_image_w1": -1,
        "sect_table_image_col_width_max": 0
      }
    ]
  }
}
```

## Regular Expressions
--

| key | value |
| - | - |
| `regex_hyphen` | `-$` |
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
        "numbering_splitter_chars": ".()[]",
        "regex_bullet_font": "(Wingdings)|(Symbol)"
      }
    ]
  }
}
```

## Functions

### test_function

This function is intended for development purposes only

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### form_object_process

The test is triggered when the page form object is parsed.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### path_object_process

The test is triggered when the page path object is parsed.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### image_object_process

The test is triggered when the page image object is parsed.

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

### word_update

Updates a word element after detecting words.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### word_spacing

Detects the spacing between two words.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_line_add_word

The test is triggered when forming text lines from words.

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

### text_line_split_filling

Splits a text line based on filling.

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

### element_create

Create user-defined elements.

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

### table_recognize

The test is triggered during the table recognition process for detecting columns and rows. This test can be called multiple times!

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### caption_join

Finds the element for text that has been marked as a caption.

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

### table_detect_header

Defines the rules for detecting table headers and tests whether the text is a header in a table.

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

### single_instance_detect

Detects handles for elements that require a single occurrence only.

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

### reading_order_detect

Detect reading order options

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

### tag_list

Handles the process of tagging lists.

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

Handles the process of tagging tables. For repurposing and accessibility purposes, a table should have headers. If no headers are detected, the default behavior is to leave the table without any `<th>` elements.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_annot

Handles the process of tagging annotations.

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

The `if` statement type of the query. According to the statement the query evaluation stops upon pass or not.

- _values:_ 
  - `['$if', '$elif', '$else']`
- _defaule value:_ $if

_keys and values:_
- "$if"
- "$elif"
- "$else"

### $if

Can by used in all functions. General logic of IF statement.

- _type:_ statement

### $elif

Can by used in all functions. General logic of ELSE IF statement.

- _type:_ statement

### $else

Can by used in all functions. General logic of ELSE statement.

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
  - "[arithmetic_operator](#arithmetic_operator)" 

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

User defined variables. Use scheme:arithmetic_operators to define variables

- _type:_ var

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
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

Logical AND.

- _type:_ logical_operator

_keys and values:_
- "$and"
- "$or"
- "$not"
- "[condition](#condition)"

### $or

Logical OR.

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

Equality comparison operator.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)", "[string](#string)"]

### $ne

Nequality comparator operator.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)", "[string](#string)"]

### $lt

Less than comparison operator.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $lte

Less than or equals operator.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $gt

Greater than operator.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $gte

Greater than or equals operator.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $regex

Regular expression predicate.

- _type:_ comparison_operator
- _types:_ ["[string](#string)"]

### $in

Contain value operator.

- _type:_ comparison_operator
- _types:_ []

### $nin

Not contain value operator.

- _type:_ comparison_operator
- _types:_ []

### arithmetic_operators

Available arithmetic_operators.

- _type:_ string
- _values:_ 
  - `['$sum', '$diff', '$abs', '$mul', '$div', '$min', '$max', '$mod']`

_keys and values:_
- "$sum"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

  - "[1]" 

- "$diff"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

  - "[1]" 

- "$abs"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

- "$mul"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

  - "[1]" 

- "$div"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

  - "[1]" 

- "$min"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

  - "[1]" 

- "$max"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

  - "[1]" 

- "$mod"
_params:_
  - "[arithmetic_operator](#arithmetic_operator)" 

  - "[0]" 

  - "[1]" 


### $sum

Sum of two numbers.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[float](#float)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"
- "[1]"

### $diff

Difference of two numbers.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[float](#float)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"
- "[1]"

### $abs

Absolute value of a single number.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[float](#float)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"

### $mul

Multiply two numbers.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[float](#float)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"
- "[1]"

### $div

division two numbers.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[float](#float)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"
- "[1]"

### $min

Get minimal value from any number of values.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[float](#float)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"
- "[1]"

### $max

Get maximal value from any number of values.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[float](#float)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"
- "[1]"

### $mod

Get the modulus from a division of values.

- _type:_ arithmetic_operator
- _types:_ ["[int](#int)", "[int](#int)"]

_keys and values:_
- "[arithmetic_operator](#arithmetic_operator)"
- "[0]"
- "[1]"

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

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

- "[pds_path](#pds_path)"
- "[pds_image](#pds_image)"
- "[pds_shading](#pds_shading)"
- "[pds_form](#pds_form)"
_params:_
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[children_num](#children_num)" 

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

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[children_num](#children_num)" 


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
- "[fill_color](#fill_color)"
- "[stroke_color](#stroke_color)"

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

  - "[parent_tag_type](#parent_tag_type)" 

  - "[id](#id)" 

  - "[title](#title)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[text](#text)" 

  - "[expansion](#expansion)" 

  - "[children_num](#children_num)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[has_content](#has_content)" 


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

  - "[bbox](#bbox)" 

  - "[label](#label)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[text](#text)" 

  - "[angle](#angle)" 

  - "[heading](#heading)" 

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

  - "[label](#label)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[children_num](#children_num)" 

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

  - "[cell_column](#cell_column)" 

  - "[cell_row](#cell_row)" 

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

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

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

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[row_num](#row_num)" 

  - "[col_num](#col_num)" 

  - "[header](#header)" 

  - "[table_type](#table_type)" 

  - "[isolated_num](#isolated_num)" 
    - Number of isolated elements in the table.
- "[pde_element](#pde_element)"
_params:_
  - "[type](#type)" 
    - Type of PdeElement.
  - "[width](#width)" 

  - "[height](#height)" 

  - "[left](#left)" 

  - "[right](#right)" 

  - "[top](#top)" 

  - "[bottom](#bottom)" 

  - "[bbox](#bbox)" 

  - "[label](#label)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[angle](#angle)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[flag](#flag)" 


### general_vars

General variables can be used without parameters. It represents general state during the processing. It contains information about the current page and the document and can be used in any query.

- _type:_ string

_keys and values:_
- "$page_num"
- "$page_width"
- "$page_height"
- "$page_rotation"
- "$doc_num_pages"
- "$doc_lang"
- "$doc_title"

### $page_num

Page number.

- _type:_ int

### $page_width

Page cropbox width.

- _type:_ float

### $page_height

Page cropbox height.

- _type:_ float

### $page_rotation

Page rotation.

- _type:_ int
- _values:_ 
  - `[0, 90, 180, 270]`

### $doc_num_pages

Document number of pages.

- _type:_ int

### $doc_lang

Document language.

- _type:_ string

### $doc_title

Document title.

- _type:_ string

### values

General values used in JSON default template.


_keys and values:_
- "[actual_text](#actual_text)"
- "[alt](#alt)"
- "[lang](#lang)"
- "[id](#id)"
- "[expansion](#expansion)"
- "[has_content](#has_content)"
- "[tag_type](#tag_type)"
- "[annot_type](#annot_type)"
- "[contents](#contents)"
- "[annot_flag](#annot_flag)"
- "[title](#title)"
- "[angle](#angle)"
- "[bbox](#bbox)"
_params:_
  - "[left](#left)" 

  - "[bottom](#bottom)" 

  - "[right](#right)" 

  - "[top](#top)" 

- "[cell_column](#cell_column)"
- "[cell_row](#cell_row)"
- "[col_num](#col_num)"
- "[children_num](#children_num)"
- "[fill_color](#fill_color)"
_params:_
  - "[red](#red)" 

  - "[green](#green)" 

  - "[blue](#blue)" 

- "[stroke_color](#stroke_color)"
_params:_
  - "[red](#red)" 

  - "[green](#green)" 

  - "[blue](#blue)" 

- "[flag](#flag)"
- "[font_name](#font_name)"
- "[font_size](#font_size)"
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"
- "[header](#header)"
- "[heading](#heading)"
- "[width](#width)"
- "[height](#height)"
- "[label](#label)"
- "[left](#left)"
- "[right](#right)"
- "[top](#top)"
- "[bottom](#bottom)"
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
- "[tag](#tag)"
- "[text](#text)"
- "[text_flag](#text_flag)"
- "[text_line_flag](#text_line_flag)"
- "[type](#type)"
- "[word_flag](#word_flag)"

### actual_text

Actual text.

- _type:_ string

### alt

Alternate description typically used for Figure tags.

- _type:_ string

### lang

The language identifier of the document or tag.

- _type:_ string

### id

The unique identifier of the tag.

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

Tag type defined by a string or regular expression. Use `.*` to match all tags.

- _type:_ string
- _values:_ 
  - `['Annot', 'Art', 'Artifact', 'Aside', 'BibEntry', 'BlockQuote', 'Caption', 'Code', 'Div', 'Document', 'DocumentFragment', 'Em', 'FENote', 'Figure', 'Form', 'Formula', 'H', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Index', 'L', 'Lbl', 'LBody', 'LI', 'Link', 'NonStruct', 'Note', 'P', 'Part', 'Private', 'Quote', 'RB', 'Reference', 'RP', 'RT', 'Ruby', 'Sect', 'Span', 'Strong', 'Sub', 'Table', 'TBody', 'TD', 'TFoot', 'TH', 'THead', 'Title', 'TOC', 'TOCI', 'TR', 'Warichu', 'WP', 'WT']`

### annot_type

Annotation type defined by a string or regular expression. Use `.*` to match all annotations.

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

### angle

Angle.

- _type:_ float

### bbox

Parameter that represents the bounding box of an object, formatted as an array: `[left, bottom, right, top]`.

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

### col_num

Number of columns in the table.

- _type:_ int

### children_num

Number of associated child page objects.

- _type:_ int

### fill_color

The fill color of an object.

- _type:_ rgb

_keys and values:_
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"

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
  - `['no_join', 'no_split', 'artifact', 'header', 'footer', 'splitter', 'no_table', 'table']`

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

### header

Marks the object as a table header.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

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
  - `['', 'label', 'li_1', 'li_2', 'li_3', 'li_4', 'label_no']`

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

### pdf_rect

Parameter that represents the bounding box of an object, formatted as an array: `[left, bottom, right, top]`.

- _type:_ rec

_keys and values:_
- "[left](#left)"
- "[bottom](#bottom)"
- "[right](#right)"
- "[top](#top)"

### pdf_rgb

Parameter that represents the RGB color of an object, formatted as an array: `[red, green, blue]`.

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

The table type represented as a value from the `PdfTableType` enum.

- _type:_ string
- _values:_ 
  - `['graphic', 'isolated', 'row', 'col', 'form']`

### tag

The tag name to be used.

- _type:_ string

### text

The text to be used as a value.

- _type:_ string

### text_flag

The flag to be used for the text element, specifying a value similar to the regex flags.

- _type:_ string
- _values:_ 
  - `['table_caption', 'image_caption', 'chart_caption', 'note_caption', 'filling', 'uppercase']`

### text_line_flag

The flag to be used for the text line element, specifying a value similar to the regex flags.

- _type:_ string
- _values:_ 
  - `['hyphen', 'new_line', 'indent', 'terminal', 'drop_cap', 'filling', 'uppercase']`

### type

Marks the object or element with a type, aiding in the recognition of the correct element type.

- _type:_ string
- _values:_ 
  - `['pds_object', 'pds_text', 'pds_path', 'pds_image', 'pds_shading', 'pds_form', 'pde_element', 'pde_text', 'pde_text_line', 'pde_word', 'pde_text_run', 'pde_image', 'pde_container', 'pde_list', 'pde_line', 'pde_rect', 'pde_table', 'pde_cell', 'pde_toc', 'pde_header', 'pde_footer', 'pde_form_field', 'pde_annot']`

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

The `if` statement should be used in function nodes. Based on the statement, the query evaluation stops upon pass or fail. If the `if` statement is not present, the condition is considered disabled.

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

