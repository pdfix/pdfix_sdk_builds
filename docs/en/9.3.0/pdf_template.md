# PDFix Template

--

## Table of Contents

- [General Settings](#general-settings)
- [Threshold Values](#threshold-values)
- [Regular Expressions](#regular-expressions)
- [Functions](#functions)

## General Settings
Global switches that apply across tagging and pagemap (RTL, Form XObject handling, optional page struct type, debug breakpoints).

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
| `preflight_artifact_w1` | `1` | Weight of horizontal bbox alignment differences when comparing two header/footer samples across pages. |
| `preflight_artifact_w2` | `1` | Weight of vertical bbox alignment differences in the same preflight comparison. |
| `preflight_artifact_w3` | `1` | For non-text objects, weight of width mismatch; for text pairs this term is unused (font checks apply instead). |
| `preflight_artifact_w4` | `1` | For text, weight of font-size difference; for graphics, weight of height mismatch between samples. |
| `preflight_artifact_w5` | `1` | Weight of numeric token / page-index stride consistency when matching running heads that include page numbers. |
| `preflight_artifact_distance` | `0.7` | DBSCAN epsilon on the weighted preflight distance between header/footer or artifact samples across pages (same units as multivariate_distance output from alignment, size, and page-number terms). |
| `preflight_artifact_cluster_points` | `2` | Minimum DBSCAN cluster size (number of page samples) to accept a repeating header, footer, or artifact stripe. If 0, the engine uses about num_pages/10 as the default minimum. |
| `concurrent_threads` | `0` | Worker thread count for parallel pagemap steps (e.g. distance-matrix fills in image/label/section clustering). 0 lets the runtime pick an implementation default; 1 disables parallelism. |
| `text_only` | `0` | If 1, pagemap skips vector line/rect extension and graphic-object layout passes; only text extraction and text-driven structure run. |
| `rotation_detect` | `1` | If 1 (or during preflight), logical page rotation is detected from content and the working page rotation may be adjusted for reading order. |
| `background_color_red` | `255` | Assumed page background RGB red component (0–255) for matching filled rectangles to the paper color. |
| `background_color_green` | `255` | Assumed page background RGB green component (0–255). |
| `background_color_blue` | `255` | Assumed page background RGB blue component (0–255). |
| `background_color_diff` | `2` | Maximum per-channel difference from the assumed background RGB still treated as background when classifying rects (tolerance for off-white). |
| `bbox_expansion` | `2` | Extra padding in points (half-width inflate/deflate) for overlap tests: reading-order bands (e.g. TOC), nesting content into table cells, multi-line text split across cells, and table vs. image overlap. |
| `angle_deviation` | `0.015707963267949` | Maximum angular deviation (radians) allowed when treating two elements (e.g. text runs) as parallel on the same line, and for stroke/alignment classification. |
| `header_ratio` | `0.15` | Upper bound as a fraction of page height [0,1] for the band considered when detecting header regions. |
| `footer_ratio` | `0.15` | Upper bound as a fraction of page height [0,1] for the band considered when detecting footer regions. |
| `artifact_w1` | `1` | Weight of the border-distance term in automatic artifact similarity (how much proximity to the page edge counts). |
| `artifact_w2` | `1` | Weight of image area relative to the page when scoring images as artifacts. |
| `artifact_font_size` | `40` | Preflight only (preflight_elements): font size in points. Horizontal text with size less than or equal to this value is not added to the artifact sample set; any non-horizontal text is always added, and horizontal text strictly larger than this value is added. |
| `artifact_border_distance_max` | `2` | Distance in points from the page edge within which border proximity still contributes to artifact similarity. |
| `artifact_similarity` | `0.7` | Similarity threshold [0,1] above which an element is treated as an artifact in automatic artifact detection passes. |
| `artifact_untagged` | `0` | If set to 1, elements without an initial parent are automatically classified as artifacts. |
| `path_object_max` | `2000` | Maximum number of sub-paths in a compound path before it may be split into separate paths. If exceeded, the path is kept intact (processed as a complex/non-simple path). |
| `path_object_min` | `100` | Sub-path count threshold that enables an “isolation” check before splitting. If a path object has more than path_object_min sub-paths, it is split only when it is not considered isolated (based on bbox size vs isolated_text). |
| `initial_element_only` | `0` | If set to 1, pagemap processes only elements explicitly marked/detected as “initial elements”; all other detected elements are ignored. |
| `initial_elements_keep_empty` | `0` | Specifies whether to preserve initial elements that remain empty (i.e., contain no detected objects) after processing. |
| `initial_element_expansion` | `2` | Bounding box expansion (in points) applied to an initial element when searching for its children. Used when element flag contains no_expand. |
| `initial_element_overlap` | `0` | Minimum required overlap ratio (0–1) between a candidate bbox and the initial element bbox to accept the candidate as a child. Used when the initial element uses **no expand** (fixed bounds). If set to 0, `initial_element_expansion` is used instead (inflate parent bbox, then require full containment). |
| `initial_element_expand_overlap` | `0.5` | Minimum required overlap ratio (0–1): intersection area divided by the **candidate** bbox area must exceed this value. Used when the initial element **may expand** (flag doesn't contain no_expand). |
| `annot_char_overlap` | `0.05` | Minimum fraction (0–1) of a character’s area that must lie under an annotation to associate that annotation with the character during tagging. |
| `isolated_text_ratio` | `10` | Upper bound on text bbox width as a multiple of typical font size when classifying a region as “isolated” for path splitting and graphic guards. |
| `isolated_text` | `80` | Upper bound in points on text bbox width for the same isolated-region tests when the ratio-based path is not used. |
| `isolated_element_ratio` | `6` | Upper bound on element bbox width and height as a multiple of font size when deciding if a graphic element is isolated. |
| `element_isolated_w1` | `1` | Weight of paragraph-like layout evidence when scoring whether a floating element is isolated. |
| `element_isolated_w2` | `1` | Weight of horizontal span / width cues in the same isolated-element score. |
| `element_isolated_caption` | `1` | If 1, elements that already carry a detected caption (table, figure, chart, note) are not treated as isolated layout islands. |
| `element_isolated_width_min` | `0` | Minimal value of bbox width for isolated element. If zero, element_isolated_width_min_ratio is used. Size in points. |
| `element_isolated_width_min_ratio` | `4` | Minimal value of bbox width for isolated element multiply with average page font size. |
| `element_isolated_width_max` | `0` | Maximal value of bbox width for isolated element. If zero, element_isolated_width_max_ratio is used. Size in points. |
| `element_isolated_width_max_ratio` | `10` | Maximal value of bbox width for isolated element multiply with average page font size. |
| `element_isolated_similarity` | `0.7` | Isolation score threshold [0,1]: in preflight, text is only collected as a column candidate when its isolation score is below this value; debug builds also use it to highlight highly isolated elements. |
| `element_line_w1` | `1` | Weight for stroke-thickness similarity when classifying paths as lines; if 0, width-based line detection is disabled. |
| `element_line_width_max` | `8` | Maximal value of line width. If zero, element_line_width_max_ratio is used. Size in points. |
| `element_line_width_max_ratio` | `1` | When element_line_width_max is 0, maximum stroke thickness is element_line_width_max_ratio times the page’s reference font size (the same scale used when comparing strokes for line detection). |
| `element_line_similarity` | `0.6` | Line-likeness score threshold [0,1] (width vs. thickness style metric). Used when classifying thin rectangles and images as stroke-like lines, and when rejecting a table candidate as corrupted if the region looks too much like a single rule instead of a grid. |
| `element_alignment_ratio` | `0.5` | Blend between baseline-based and bbox-based alignment checks. Bbox alignment is weighted by element_alignment_ratio relative to baseline alignment. |
| `rect_image_similarity` | `0.7` | Minimum image similarity [0,1] for converting a plain rectangle into an image element (when line classification does not win). |
| `rect_line_similarity` | `0.5` | Minimum line similarity [0,1] for converting a rectangle into a line element (evaluated before the image branch). |
| `image_background_text` | `1` | Expands text bounding boxes when testing whether a graphic is a text background highlight. |
| `image_overlap_distance` | `1` | Maximum distance value when graphic page objects can be joined. Distance in points. |
| `image_join_distance` | `8` | Defines the maximum allowed distance (in points) between small images for them to be considered joinable. These parameters help fine-tune the grouping of small image elements into a cohesive larger visual block based on their spatial proximity. |
| `char_clip_ratio` | `0.5` | Minimum ratio of visible (unclipped) character area to the character’s full glyph box. |
| `word_space_width_ratio` | `0.6` | The word_space_width_ratio is a multiplier that determines the threshold for identifying inter-word spaces by comparing the gap between characters to the typical width of a space character. It scales the space width so that small variations in spacing can be interpreted as either a valid word separator or a mere character gap. |
| `word_space_width_min_ratio` | `0.1` | The word_space_width_min_ratio is an additional multiplier that sets a minimum threshold for the allowed space between words. It ensures that, even when minimal character spacing is detected, the computed gap used to determine word boundaries does not fall below a baseline value relative to the font size. |
| `word_space_distance_max` | `0` | The maximum fixed distance (in points) allowed between two words to consider them part of the same text line. |
| `word_space_distance_max_ratio` | `0` | The maximum distance allowed between words to join them into a line, calculated as a multiple of the font size. |
| `word_space_ratio` | `1` | Scale factor applied when estimating default word spacing from the font’s space character (simple vs justified-like lines). |
| `word_space_update_min` | `0.2` | Minimum ratio of detected word spacing. |
| `word_space_update_max` | `4` | Maximum ratio of detected word spacing. If set to 0, automatic word-spacing updates from lines are not applied. |
| `word_space_update_distance` | `0.04` | DBSCAN epsilon scale for clustering measured word gaps: effective eps = font size × this factor. |
| `word_overlap` | `0.9` | Minimum overlap percentage (0-1) required between bounding boxes to consider words as duplicates. A word must cover at least this percentage of another word's area to be considered overlapping. |
| `text_line_baseline_ratio` | `0.1` | Maximum baseline shift. Value multiplies minimal font. Baseline shift moves individual characters up or down in relation to other text on the same line. |
| `text_line_insert_elem_ratio` | `0.5` | Maximum vertical shift/overlap ratio allowed when inserting an element into a text line. The value is multiplied by the minimum font size. |
| `text_line_underline_distance` | `2.6` | Distance of the underline line and text baseline. Size in points. |
| `text_line_underline_char_distance_ratio` | `0.1` | Distance of the underline line start/end point and character bounding box. The value is multiplied by line font size. Size in points. |
| `text_line_superscript_detect` | `1` | If 1, the engine attempts to detect and merge superscript words into the same line when they are close enough to the baseline and horizontally near their main word. If 0, no special handling for superscripts is applied; all words are treated as part of the same line based on regular spacing rules. |
| `text_line_superscript_shift_ratio` | `0.5` | Maximum vertical baseline shift allowed for a word to be considered a superscript, defined as a ratio of the maximum font size. |
| `text_line_subscript_shift_ratio` | `0.4` | Maximum vertical baseline shift allowed for a word to be considered a subscript, defined as a ratio of the maximum font size. |
| `text_line_superscript_dist_ratio` | `0.3` | Maximum horizontal distance (gap or overlap) allowed between a word and its superscript, defined as a ratio of the maximum font size. |
| `text_line_subscript_dist_ratio` | `0.3` | Maximum horizontal distance (gap or overlap) allowed between a word and its subscript, defined as a ratio of the maximum font size. |
| `text_line_join_font_size_distance` | `0.1` | Maximum font-size difference (points) allowed when merging two lines that use different fonts into one paragraph line. |
| `text_line_distance_max` | `0` | Maximum distance between lines. If zero, text_line_distance_max_ratio is used. Size in points. |
| `text_line_distance_max_ratio` | `2` | Maximum distance between lines. The value is multiplied by line font size. |
| `text_line_join_distance` | `2` | Maximum threshold value in line spacing detection for specific font size. The higher value allows creating paragraph with variable line spacings. The value is multiplied by font size. |
| `text_line_chunk_distance_max` | `0` | Maximum word-to-word gap inside a line chunk before forcing a split. If zero, text_line_chunk_distance_max_ratio scales simple word spacing instead. Size in points. |
| `text_line_chunk_distance_max_ratio` | `6` | Maximum distance between chunks. The value is multiplied by simple word spacing between words. |
| `text_line_chunk_distance` | `0` | DBSCAN epsilon (points) for clustering measured word gaps within a chunk. If nonzero, it is used directly; if zero, text_line_chunk_distance_ratio times line font size is used instead. |
| `text_line_chunk_distance_ratio` | `0.4` | When text_line_chunk_distance is zero, DBSCAN epsilon is line font size × this ratio. |
| `text_chunk_distance` | `0` | Maximum distance value when text chunks are vertically aligned. If zero, text_chunk_distance_ratio is used. Size in points. |
| `text_chunk_distance_ratio` | `0.42` | Maximum distance value when text chunks are vertically aligned. The value is multiplied by page font width. |
| `text_chunk_simple_distance` | `0.4` | Maximum distance value when text chunks create simple line. Normalized to interval [0,1]. |
| `text_chunk_word_distance` | `0.1` | Similarity threshold [0,1] for splitting a single-line text chunk into words when internal spacing is ambiguous. |
| `text_height` | `8` | Typical text height in points used as a scale reference: minimum table cell sizing, graphic-table span caps (with table span ratios), line spacing, and other distance heuristics. |
| `text_simple_similarity` | `0.96` | Minimum similarity value when text lines create a simple paragraph normalized to interval [0,1]. |
| `text_justify_similarity` | `0.96` | Minimum similarity value when text lines create a justify paragraph normalized to interval [0,1]. |
| `text_table_similarity` | `0.65` | Minimum similarity value when text lines create a table normalized to interval [0,1]. |
| `text_split_distance` | `0.2` | Dissimilarity cutoff when adjacent text lines are evaluated for splitting one paragraph into two. |
| `label_image_detect` | `1` | If 1, list/label markers drawn as vector paths can be detected; if 0, path-based label candidates are skipped. |
| `label_word_detect` | `1` | If 1, list/label markers from extracted words are detected; if 0, word-based label detection is disabled. |
| `label_distance_ratio` | `10` | Maximum label-to-text gap as a multiple of the dominant page font size for pairing markers with body text. |
| `label_image_w1` | `1` | Controls how much vertical alignment matters when clustering labels. A higher value enforces stricter alignment, while a lower value allows more variation. |
| `label_image_w2` | `1` | Weight for how closely two vector markers agree on horizontal offset from their paired sibling words (start, end, and center gaps to the sibling edge). This compares candidate A vs B, not a single absolute gap. |
| `label_image_w3` | `1` | This weight controls how much the label's width consistency matters in clustering. A higher value enforces that labels should have the same width, while a lower value allows more variation in width between labels. |
| `label_image_w4` | `1` | This weight determines how important the height consistency of labels is when clustering. A higher value enforces that labels should have the same height, while a lower value allows more flexibility in height differences. |
| `label_image_w5` | `0.5` | This weight adjusts how important the height relationship is between the image label and its associated text. A higher value means the height alignment between the label and the text is more significant in clustering decisions. |
| `label_image_width_min` | `0` | Specifies a fixed minimum width in points. If set to zero, label_image_width_min_ratio is used instead. |
| `label_image_width_min_ratio` | `0` | When label_image_width_min is 0: minimum marker width as a multiple of the paired sibling word’s font size (the body word next to the marker). |
| `label_image_width_max` | `0` | Specifies a fixed maximum width in points. If set to zero, the label_image_width_max_ratio is used instead. |
| `label_image_width_max_ratio` | `6` | When label_image_width_max is 0: maximum marker width as a multiple of the paired sibling word’s font size. |
| `label_image_distance` | `4` | Clustering threshold in points that decides when labels should be grouped together. A higher value makes clustering more flexible, allowing distant labels to merge, while a lower value keeps clusters tight and separate. |
| `label_word_w1` | `1` | Controls how much vertical alignment matters when clustering labels. A higher value enforces stricter alignment, while a lower value allows more variation. |
| `label_word_w2` | `1` | Weight for agreement between two word-based markers on horizontal offset from their sibling text (same start/end/center gaps as for image labels; LTR adds an extra horizontal position consistency term between the two candidates). |
| `label_word_dist_sibling_ratio` | `4` | This threshold, defined as a ratio multiplied by a siblings font size, sets the maximum gap allowed between a label and its sibling element to be joined together. If the distance exceeds this value, the label and its sibling remain separate. |
| `label_sibling_distance_ratio` | `1.2` | Multiplier applied to the label–true-sibling gap when a competing “false” sibling word exists: if the false sibling sits within end_dist × this ratio of the label, the singleton geometry is rejected (label_singleton_geometry_rejected in label and image pairing). |
| `label_word_distance` | `0` | Clustering threshold in points that decides when labels should be grouped together. A higher value makes clustering more flexible, allowing distant labels to merge, while a lower value keeps clusters tight and separate. |
| `label_word_distance_ratio` | `1` | Used only when label_word_distance is 0: hierarchical clustering cutoff equals this ratio times the page font width. |
| `label_order_detect` | `1` | If 1, the engine ignores list that do not have a consistent label order (e.g. 1., 2., 3. or a), b), c)); if 0, no label-order checks are applied and any cluster of markers can form a list style. |
| `toc_detect` | `1` | TOC detection. Possible values: 0 | 1. If 0 is set, it prevents generating TOC from words. |
| `toc_word_distance` | `0` | Clustering cutoff in points when splitting the TOC candidate tree into clusters (epsilon passed to the hierarchical cut). If set to 0, the cutoff is toc_word_distance_ratio × page font width instead. |
| `toc_word_distance_ratio` | `1` | Used only when toc_word_distance is 0: multiplied by page font width to obtain the same tree-cut epsilon as a non-zero toc_word_distance. |
| `graphic_table_detect` | `1` | Master switch for automatically creating path-based (graphic) tables from vector lines and rectangles. It does not disable path-based row or column recognition inside an initial pde_table declared through element_create. |
| `graphic_table_detect_row` | `1` | If 0, y-coordinates from path lines and rectangle edges are not used to build row bands for path-based (graphic) tables; if 1, horizontal rules contribute row structure. Together with text_table_detect_row: when graphic_table_detect_row is on and text_table_detect_row is off, adjacent cells with no graphic border (line or rectangle edge) between them are spanned into a rowspan. |
| `graphic_table_detect_col` | `1` | If 0, x-coordinates from path lines and rectangle edges are not used to build column guides for path-based (graphic) tables; if 1, vertical rules contribute column structure. Together with text_table_detect_col: when graphic_table_detect_col is on and text_table_detect_col is off, adjacent cells with no graphic border (line or rectangle edge) between them are spanned into a colspan. |
| `graphic_table_alignment_distance` | `0.8` | Maximum alignment slack in points when path-derived table elements are scored as belonging to the same row or column grid. |
| `graphic_table_split_w1` | `1` | Weight of paragraph-like text layout when deciding whether a graphic region should stay one table or be split. |
| `graphic_table_split_w2` | `1` | Weight of horizontal alignment consistency in the same split-or-keep score. |
| `graphic_table_split_w3` | `1` | Weight of column width regularity in the split-or-keep score. |
| `graphic_table_split_w4` | `0.5` | Weight of the inferred column count in the split-or-keep score. |
| `graphic_table_split_w5` | `0.5` | Weight of the inferred row count in the split-or-keep score. |
| `graphic_table_split_w6` | `1` | Weight of how much page area the candidate occupies when balancing table vs. non-table layout. |
| `graphic_table_split_col_max` | `5` | Upper limit on column count considered when evaluating a graphic split. |
| `graphic_table_split_row_max` | `5` | Upper limit on row count considered when evaluating a graphic split. |
| `graphic_table_split_similarity` | `0.7` | Blended split score [0,1] (paragraph-likeness, horizontal alignment, optional width boost via multivariate_distance). If this score is strictly greater than the threshold, the graphic table candidate is split—either into layout containers or into flat elements depending on graphic_table_split_layout_similarity. |
| `graphic_table_split_layout_similarity` | `0.7` | When a split is triggered, split_to_containers_similarity (column/row count vs caps plus table area vs container) is compared with >= to this threshold: if true, split_table_to_containers; else split_table_to_elements. Also used when nested graphic tables are merged or split. |
| `graphic_table_chart_similarity` | `0.3` | Similarity threshold [0,1] used when classifying a graphic region as chart-like versus tabular. |
| `graphic_table_image_w1` | `-1` | Images area weight. If -1, number of images is used. |
| `graphic_table_image_w2` | `-1` | Image-count weight in the chart-or-table score. If -1, raw image count is used instead of a fixed weight. |
| `graphic_table_image_w3` | `-1` | Chart similarity weight. If -1, number of paths is used. |
| `graphic_table_image_w4` | `1` | Texts vertical alignment weight. |
| `graphic_table_image_w5` | `1` | Table size weight. |
| `graphic_table_image_similarity` | `0.7` | Minimum similarity value when graphic table has an image. |
| `text_table_detect` | `1` | Master switch for automatically creating text-based section tables (columns built from text/image chunks, not from vector grid paths). It does not disable text-based row or column recognition inside an initial pde_table declared through element_create. |
| `text_table_detect_row` | `1` | If 0, isolated text and images are not grouped into horizontal row bands for borderless (text-based) table hypotheses; if 1, row clustering runs. Also paired with graphic_table_detect_row for rowspan: when text_table_detect_row is 0 and graphic_table_detect_row is 1, cells without a graphic border between them are spanned (no text-overlap heuristic). |
| `text_table_detect_col` | `1` | If 0, isolated elements are not clustered into vertical column bands for text-only table hypotheses; if 1, column alignment is evaluated. Also paired with graphic_table_detect_col for colspan: when text_table_detect_col is 0 and graphic_table_detect_col is 1, cells without a graphic border between them are spanned (no text-overlap heuristic). |
| `text_table_row_alignment_type` | `1` | Table row alignment type [0 - strong, 1 - average, 2 - weak]. |
| `text_table_col_alignment_type` | `1` | Table column alignment type [0 - strong, 1 - average, 2 - weak]. |
| `text_table_col_similarity_type` | `0` | Table column similarity type [0 - column alignment distance, 1 - element distance, 2 - element size, 3 - max]. |
| `text_table_col_distance` | `0.8` | Maximum deviation (points) when pairing nearest-neighbor elements into the same text-table column. |
| `text_table_col_similarity` | `0.36` | Minimum weighted column table-likeness score [0,1]; below this the candidate region is rejected as not a text table. |
| `text_table_alignment_type` | `2` | Table column alignment type [0 - strong, 1 - average, 2 - weak]. Select strong for strictly aligned table elements. |
| `text_table_alignment_distance` | `0.4` | Maximum alignment deviation (points) when scoring text regions as a single table. |
| `text_table_text_col_w1` | `1` | Weight of the text-vs-paragraph similarity term when scoring a candidate text-table column. |
| `text_table_text_col_w2` | `1` | Weight of the column-width similarity term in the same text-column distance blend. |
| `text_table_text_col_width_min` | `0` | Minimum text-column width in points; if 0, effective min is text_table_text_col_width_min_ratio × page font size. |
| `text_table_text_col_width_min_ratio` | `1` | Used only when text_table_text_col_width_min is 0: scales the minimum column width from page font size. |
| `text_table_text_col_width_max` | `0` | Maximum text-column width in points; if 0, effective max is text_table_text_col_width_max_ratio × page font size. |
| `text_table_text_col_width_max_ratio` | `8` | Used only when text_table_text_col_width_max is 0: scales the maximum column width from page font size. |
| `text_table_image_col_w1` | `1` | Weight for the blended image-column distance (size spread and optional graphics-state check). |
| `text_table_image_col_gs` | `1` | If non-zero, images in the same column candidate must share compatible graphics state (line width, fill/stroke type and opacity). |
| `text_table_image_col_width_min` | `0` | Minimum image-column width in points; if 0, use text_table_image_col_width_min_ratio × page font size. |
| `text_table_image_col_width_min_ratio` | `1` | Used when text_table_image_col_width_min is 0. |
| `text_table_image_col_width_max` | `0` | Maximum image-column width in points; if 0, use text_table_image_col_width_max_ratio × page font size. |
| `text_table_image_col_width_max_ratio` | `4` | Used when text_table_image_col_width_max is 0. |
| `text_table_image_col_height_min` | `0` | Minimum image-column height in points; if 0, use text_table_image_col_height_min_ratio × page font size. |
| `text_table_image_col_height_min_ratio` | `1` | Used when text_table_image_col_height_min is 0. |
| `text_table_image_col_height_max` | `0` | Maximum image-column height in points; if 0, use text_table_image_col_height_max_ratio × page font size. |
| `text_table_image_col_height_max_ratio` | `2` | Used when text_table_image_col_height_max is 0. |
| `text_table_image_similarity_w1` | `1` | Weight for image-area similarity in the section image score. |
| `text_table_image_similarity_w2` | `1` | Weight applied when chart similarity overrides the area term in that blend. |
| `text_table_image_similarity` | `0.7` | If section image similarity is at or above this value [0,1], the overlap is rejected as not a text table (too figure-like). |
| `text_table_paragraph_similarity` | `0.7` | If section paragraph similarity is at or above this value [0,1], the overlap is rejected as not a text table (too prose-like). |
| `table_update_delete_empty` | `1` | Default preference for post-detection cleanup: when enabled in templates, empty rows and columns are dropped so hollow grids do not linger. |
| `table_update_split_by_cell` | `0` | When enabled, oversized merged cells are subdivided—e.g. a paragraph mistaken for one cell, or bullets and body text glued in one cell. |
| `table_update_split_by_row` | `0` | When enabled, multi-line cell content is broken into one line per row for downstream table semantics. |
| `table_update_split_label` | `0` | When enabled, label markers inside table cells are separated from body text where the detector fused them. |
| `table_update_span_empty` | `1` | When enabled, visually empty cells are merged using row/column span metadata instead of leaving many blank boxes. |
| `table_update_span_row` | `0` | When enabled, rows are coalesced according to the largest consistent row span detected in the grid. |
| `table_update_span_row_first` | `0` | Default order for span repair: when enabled, row-span style merging is preferred before column-span merging; when disabled, column direction runs first. Applies to post-process span_empty-style passes and to the graphic-table isolated-element span pass (same meaning as template span_row_first on table_update). |
| `table_update_join` | `0` | When enabled, all text fragments inside one cell are concatenated into a single paragraph element. |
| `table_update_cell_header` | `1` | When enabled, header rows/cells are inferred during table post-processing for accessibility and layout roles. |
| `table_span_col_ratio` | `0.1` | Fraction [0,1] of cell span width: isolated content intersecting adjacent graphic cells must cover at least this much of each cell’s span bbox horizontally before colspan-style merging is allowed (path-based tables with floating text). |
| `table_span_row_ratio` | `0.2` | Fraction [0,1] of cell span height: same idea as table_span_col_ratio but for rowspan decisions; combined with text_height caps when measuring how much of an isolated element intersects stacked cells. |
| `table_alignment_h` | `1` | Maximum slack in points when comparing vertical positions (top, bottom, or vertical center) of content in adjacent cells on the same row to infer row-wise alignment. |
| `table_alignment_v` | `4` | Maximum slack in points when comparing horizontal positions (left, right, or horizontal center) of content in adjacent cells in the same column to infer column-wise alignment. |
| `table_line_intersection` | `1` | Padding in points around strokes when testing intersections: graphic table construction from paths, and assigning text lines to the correct graphic cell during nesting. |
| `form_table_detect` | `1` | If 1, widget/form field layouts may be interpreted as tabular structure where applicable. |
| `element_prop_detect` | `1` | Update elements alternate description, actual text, expansion and annotation Contents key. Default is 1; set to 0 to skip for performance when alternate text is not required. |
| `rd_sort` | `0` | Reading-order sort mode: 0 built-in heuristic, 1 PDF content stream order, 2 geometric (xy), 3 explicit rd_index from template. |
| `rd_sort_direction` | `0` | When using built-in or xy geometric sort: 0 default, 1 favor column-major traversal, 2 favor row-major traversal. |
| `rd_column_distance` | `0.8` | Maximum horizontal gap in points between elements tentatively placed in the same column during reading-order grouping. |
| `rd_overlap_min_ratio` | `0.02` | For reading-order overlap tests, require the shared span on the overlap axis to be at least this fraction of the smaller box width (horizontal) or smaller height (vertical). 0 keeps the legacy rule where any positive overlap counts. |

Example:
```
{
  "template": {
    "pagemap": [
      {
        "graphic_table_image_w2": -1,
        "graphic_table_split_similarity": 0.7,
        "text_chunk_simple_distance": 0.4
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
| `regex_bullet` | `^[\\u2010\\u2011\\u2212\\u005E\\u005B\\ uF0A7\\uF097\\uF0BB\\u25CF\\u2022\\u25D8 \\u25CB\\u25D9\\u2023\\u2043\\uF0B7\\u22 12\\u204C\\u204D\\u25E6\\u29BE\\u29BF\\u 21E8\\u25BA\\u25C4\\u2219\\u25A0\\uF06C\ \u25A1\\u005D\\u25C6\\u006F]$` |
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
        "regex_table_caption": "((^table)|(^tab\\.))"
      }
    ]
  }
}
```

## Functions

### element_create

Define initial regions (anchors) such as pde_text, pde_list, or pde_table and optional template fields (flag, label, numbering, parent, and others) applied when those regions are recognized.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### object_update

Runs while each low-level PDF content object (pds_text, pds_path, pds_image, pds_form, …) is classified before it becomes pde_* layout elements.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_run_update

Runs per pde_text_run after PDF text objects are parsed: adjust text_state_flag and other run-level keys before words are built.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_run_neighbours

Binary rule on adjacent pde_text_run segments (left then right) while runs are merged into words or lines.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### line_update

Runs once per detected text line after path-based line detection. Matching rules here can set header, footer, artifact, parent, tag, alt, and related template keys on that line.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### rect_update

Runs per pde_rect still stored in the line-elements list after rect detection and extension: same promotion path as line_update (header/footer/artifact).

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_graphic_neighbours

Binary rule on two neighbouring graphic candidates (line, rect, table fragment, or generic pde_element) during graphic-table merging.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_graphic_update

Runs on graphic layout nodes (pde_line, pde_rect, pde_table) after graphic detection: shared update keys (flag, parent, tag, single_instance, id, …).

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### word_update

Invoked for each extracted word during layout. (1) While words are collected, matching rules can set flags (header, footer, artifact, no_join, …), language, numbering, labels, and related keys; when header, footer, or artifact is set, the word may be moved into the corresponding band or region. (2) During font preparation the engine may evaluate this hook again so word_space can lock the space width for that font before lines are built. Global word_space_ratio in the main pagemap block still scales those widths afterward; this hook does not replace that multiplier.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### word_neighbours

Binary rule on adjacent pde_word tokens (left then right) while the engine merges words into a text line.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_line_update

Runs per pde_text_line after line assembly: same keys as other *_update steps (flag, heading, label, word_space, split, splitter, …).

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_line_neighbours

Binary rule on an upper and lower pde_text_line: decide whether they may belong to one paragraph or must split.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### text_update

Runs per pde_text after paragraph/chunk grouping: set tag, heading, lang, flags, numbering, label fields, id, and other text-level template keys.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### image_update

Runs per pde_image after raster/vector image objects are recognized: alt, actual_text, expansion, lang, tag, flag, single_instance, id, etc.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_update

Generic template hook for any element type listed in the query (text, image, line, rect, table, and other layout types). Use it to set tag, parent, flag, dimensions, contents, and related keys on the matched element.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_nest

Binary template: the query matches two elements by structural kind. The first `param` operand is the candidate parent; the second is the candidate child. When a row matches, the optional `join` value can force nesting (first becomes parent of the second) or forbid it; if `join` is omitted after a match, default nesting logic still runs.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### table_update

Runs while the engine is building each detected table, after the grid is recognized. Matching rules here load values for the table_update step and apply them to the current table. The boolean fields below, when set in this block, override the document’s default pagemap table thresholds for that table only: delete_empty, split_by_row, split_label, split_by_cell, span_empty, span_row_first, span_row, join, cell_header, and the optional flag. Note: split_by_cell usually behaves as intended only when text-based row detection (text_table_detect_row) is also enabled in pagemap, unless your template explicitly changes that relationship.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### cell_update

Runs for each table cell after the table’s global passes, when the cell is a span and not only an initial placeholder. Matching rules can set name (anchor), language, flag, column/row span, scope, cell_header, id, heading, single_instance, associated_header, join (merge text in that cell), and join_row (steer row merges with borders in later passes).

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### table_split

Binary template on pde_table plus one child element: the engine scans rows from the bottom upward; if the rule matches and row is true, that row index becomes a table split boundary. Children with a table splitter flag can also force a split row.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### element_prop_update

Updates a specific property (Alt, ActualText, Expansion, or Contents) of an element. The value is determined by a step-by-step fallback process. The engine checks each step in order (1 to 7); if a step is enabled (true) and yields a value, that value is used, and subsequent steps are skipped.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### artifact_update

Runs while post-processing the artifact candidate list: the template can keep an item as artifact (artifact true) or clear the artifact flag so the element moves back to header, footer, page body, or its initial-element parent.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### label_update

Refine words or elements already marked as list markers (label levels, patterns) before lists are assembled.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### list_update

After list_detect builds pde_list containers, refine each list: set flag (e.g. continuous), numbering style, or split back to plain texts.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_image

Runs while emitting structure for a pde_image: supplies Alt / ActualText, optional artifact escape hatch, and (PDF 2.0+) whether child widgets or annotations live under the Figure.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_table

Emits Table structure for a pde_table: borders/isolated chrome as artifacts, optional split into per-cell traversal when headers are missing, and continuous tables that reuse one Table node across pages when the element continuous flag is set.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_update

Template hook on an existing pds_struct_elem during tagging commands: lets regex or programmatic filters accept or reject structure nodes by running KB rules against the live struct element.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### tag_neighbours

Binary rule on two neighbouring structure tags in reading order, evaluated by the Merge Tags action: the first parameter is the upper tag, the second is the lower tag.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### annot_update

Runs when associating structure with a pdf_annot: adjust alt and Contents (and linked schema values) after the annotation is tied to content.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

### font_update

Template hook on a pdf_font during font commands: lets regex or programmatic filters accept or reject fonts by running KB rules against the live font dictionary.

_keys and values:_
- "[disable](#disable)" : false
- "[statement](#statement)" : "$if"
- "[query](#query)" :
  - "[param](#param)" : [["[pds_form](#pds_form)"]]
- "[flag](#flag)" : ""

## Schema

### statement

Controls conditional evaluation: $if / $elif / $else branches decide which template nodes run against the current query.

- _values:_ 
  - `['$if', '$elif', '$else']`
- _defaule value:_ $if

_keys and values:_
- "$if"
- "$elif"
- "$else"

### $if

Primary branch: the following query is evaluated when no earlier branch matched.

- _type:_ statement

### $elif

Secondary branch evaluated only if previous $if/$elif queries did not match.

- _type:_ statement

### $else

Fallback branch when no $if or $elif matched.

- _type:_ statement

### query

Predicate and context for a template node: parameters, logical operators, and optional variables that must pass before values are applied.

- _type:_ query

_keys and values:_
- "[param](#param)"
_params:_
  - "[pds_object_params](#pds_object_params)" 
    - A parameter that represents PdsObject. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pde_element_params](#pde_element_params)" 
    - A parameter that represents PdeElement. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pds_struct_elem_params](#pds_struct_elem_params)" 
    - A parameter that represents a structure-tree element. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pdf_annot_params](#pdf_annot_params)" 
    - A parameter that represents a PDF annotation. The value starts with the character $, followed by a number (e.g., $0_width). The number represents the index of the parameter in the param array.
  - "[pdf_font_params](#pdf_font_params)" 
    - A parameter that represents a PDF font. The value starts with the character $, followed by a number (e.g., $0_font_name). The number represents the index of the parameter in the param array.
  - "[pdf_rect](#pdf_rect)" 

  - "[pdf_rgb](#pdf_rgb)" 

  - "[int](#int)" 
    - Integer operand in a condition (no fractional part).
  - "[bool](#bool)" 
    - Boolean true/false operand in a condition.
  - "[float](#float)" 
    - Floating-point operand (geometry, font size, ratios).
  - "[string](#string)" 
    - String operand (text, names, regex targets).
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
- "[pdf_font_params](#pdf_font_params)"
- "[pdf_rect](#pdf_rect)"
- "[pdf_rgb](#pdf_rgb)"
- "[int](#int)"
- "[bool](#bool)"
- "[float](#float)"
- "[string](#string)"

### int

Integer operand in a condition (no fractional part).

- _type:_ int

### bool

Boolean true/false operand in a condition.

- _type:_ bool

### float

Floating-point operand (geometry, font size, ratios).

- _type:_ float

### string

String operand (text, names, regex targets).

- _type:_ string

### var

User-defined variables; reference bbox macros such as left, width, or top in conditions.

- _type:_ var

_keys and values:_
- "0_value"

### logical_operators

Combine multiple query conditions: $and requires all branches, $or any branch, $not inverts one branch.

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

Scalar comparisons ($eq, $ne, $lt, …), regex match ($regex), and bbox containment ($in / $nin).

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

Field equals the given literal (string, number, or bool).

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)", "[string](#string)", "[bool](#bool)"]

### $ne

Field differs from the given literal.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)", "[string](#string)", "[bool](#bool)"]

### $lt

Numeric field strictly less than the operand.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $lte

Numeric field less than or equal to the operand.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $gt

Numeric field strictly greater than the operand.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $gte

Numeric field greater than or equal to the operand.

- _type:_ comparison_operator
- _types:_ ["[int](#int)", "[float](#float)"]

### $regex

String field must match the given regular expression pattern.

- _type:_ comparison_operator
- _types:_ ["[string](#string)"]

### $in

True when the parameter’s bbox lies inside the comparison bbox (spatial containment).

- _type:_ comparison_operator
- _types:_ ["[bbox](#bbox)"]

### $nin

True when the parameter’s bbox does not lie inside the comparison bbox.

- _type:_ comparison_operator
- _types:_ ["[bbox](#bbox)"]

### pds_object_params

Catalog of low-level PDF content object shapes (pds_text, pds_path, …) usable as QUERY param types for object_update.


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

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[children_num](#children_num)" 

  - "[artifact](#artifact)" 

  - "[mcid](#mcid)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[text](#text)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 

- "[pds_path](#pds_path)"
- "[pds_image](#pds_image)"
- "[pds_shading](#pds_shading)"
- "[pds_form](#pds_form)"
- "[pds_object](#pds_object)"
_params:_
  - "[type](#type)" 
    - Concrete pds_* subtype for this object instance.
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

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[children_num](#children_num)" 

  - "[artifact](#artifact)" 

  - "[mcid](#mcid)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[text](#text)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 


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
- "[fill_alpha](#fill_alpha)"
- "[stroke_alpha](#stroke_alpha)"
- "[has_transparency](#has_transparency)"
- "[children_num](#children_num)"
- "[artifact](#artifact)"
- "[mcid](#mcid)"
- "[font_size](#font_size)"
- "[font_name](#font_name)"
- "[text](#text)"
- "[lang](#lang)"
- "[alt](#alt)"
- "[actual_text](#actual_text)"
- "[expansion](#expansion)"

### pdf_font_params

Font dictionary fields available when pdf_font is a query parameter (font_update, font filters).


_keys and values:_
- "[pdf_font](#pdf_font)"
_params:_
  - "[font_name](#font_name)" 

  - "[cos_obj](#cos_obj)" 

  - "[font_type](#font_type)" 

  - "[embedded](#embedded)" 

  - "[bold](#bold)" 

  - "[italic](#italic)" 

  - "[fixed_width](#fixed_width)" 

  - "[vertical](#vertical)" 

  - "[missing_unicode](#missing_unicode)" 


### pds_struct_elem_params

Structure-tree element parameters for tag_update and similar hooks (pds_struct_elem).


_keys and values:_
- "[pds_struct_elem](#pds_struct_elem)"
_params:_
  - "[type](#type)" 
    - Structure element role/type name as in the PDF structure tree.
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

  - "[is_standard_tag](#is_standard_tag)" 
    - A value identifying whether the tag is a standard tag for detected PDF.
  - "[id](#id)" 

  - "[title](#title)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 

  - "[text](#text)" 

  - "[children_num](#children_num)" 

  - "[object_num](#object_num)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[font_size](#font_size)" 

  - "[font_name](#font_name)" 

  - "[has_content](#has_content)" 

  - "[has_annot](#has_annot)" 

  - "[row_num](#row_num)" 

  - "[col_num](#col_num)" 

  - "[numbering](#numbering)" 

  - "[cell_column](#cell_column)" 

  - "[cell_row](#cell_row)" 

  - "[cell_row_span](#cell_row_span)" 

  - "[cell_column_span](#cell_column_span)" 

  - "[cell_scope](#cell_scope)" 

  - "[page_num](#page_num)" 
    - 1-based index of the structure element page

### pdf_annot_params

Annotation fields available when pdf_annot is a query parameter (annot_update, linking).


_keys and values:_
- "[pdf_annot](#pdf_annot)"
_params:_
  - "[type](#type)" 
    - Annotation subtype (link, text, highlight, …) exposed to the template.
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

  - "[tag_type](#tag_type)" 


### pde_element_params

Layout element field catalog (pde_text, pde_image, …) referenced from QUERY param arrays.


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

  - "[toc](#toc)" 

  - "[has_fill](#has_fill)" 

  - "[has_stroke](#has_stroke)" 

  - "[fill_color](#fill_color)" 

  - "[stroke_color](#stroke_color)" 

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 

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

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 

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

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

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

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 

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

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 

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

  - "[fill_alpha](#fill_alpha)" 

  - "[stroke_alpha](#stroke_alpha)" 

  - "[has_transparency](#has_transparency)" 

  - "[angle](#angle)" 

  - "[lang](#lang)" 

  - "[alt](#alt)" 

  - "[actual_text](#actual_text)" 

  - "[expansion](#expansion)" 

  - "[flag](#flag)" 

  - "[name](#name)" 


### general_vars

Built-in read-only variables ($page_*, $doc_*) usable in query conditions without declaring parameters.

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

1-based index of the page being processed.

- _type:_ int

### $page_width

Crop box width in default user space units (same basis as layout bboxes).

- _type:_ float

### $page_height

Crop box height in default user space units (same basis as layout bboxes).

- _type:_ float

### $page_font_size

Dominant body font size estimated for the page.

- _type:_ float

### $page_min_font_size

Smallest font size observed on the page.

- _type:_ float

### $page_max_font_size

Largest font size observed on the page.

- _type:_ float

### $page_rotation

PDF /Rotate value in degrees for the page (typically 0, 90, 180, or 270).

- _type:_ int
- _values:_ 
  - `[0, 90, 180, 270]`

### $page_rtl

True when the page is treated as right-to-left for layout. Set during page-content parsing when the knowledge base enables RTL handling and a text object contains a character classified as right-to-left; if RTL is disabled in the knowledge base, this flag is usually not set that way and stays false.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### $page_anchor

Comma-joined names of anchors already registered on this page during template application.

- _type:_ string

### $doc_num_pages

Total page count in the PDF document.

- _type:_ int

### $doc_lang

Document-level language hint from metadata or detection.

- _type:_ string

### $doc_title

Title string from document metadata when available.

- _type:_ string

### $doc_anchor

Comma-joined anchor names resolved anywhere in the document so far.

- _type:_ string

### values

Reusable field definitions (alt, flag, bbox, …) linked from template nodes via schema:values:*.


_keys and values:_
- "[type](#type)"
- "[alt](#alt)"
- "[actual_text](#actual_text)"
- "[expansion](#expansion)"
- "[lang](#lang)"
- "[id](#id)"
- "[associated_header](#associated_header)"
- "[has_content](#has_content)"
- "[has_annot](#has_annot)"
- "[tag_type](#tag_type)"
- "[parent_tag_type](#parent_tag_type)"
- "[children_tag_type](#children_tag_type)"
- "[annot_type](#annot_type)"
- "[contents](#contents)"
- "[annot_flag](#annot_flag)"
- "[title](#title)"
- "[name](#name)"
- "[parent](#parent)"
- "[caption](#caption)"
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

- "[fill_alpha](#fill_alpha)"
- "[stroke_alpha](#stroke_alpha)"
- "[has_transparency](#has_transparency)"
- "[flag](#flag)"
- "[numbering](#numbering)"
- "[single_instance](#single_instance)"
- "[word_space](#word_space)"
- "[font_name](#font_name)"
- "[cos_obj](#cos_obj)"
- "[font_type](#font_type)"
- "[embedded](#embedded)"
- "[bold](#bold)"
- "[italic](#italic)"
- "[fixed_width](#fixed_width)"
- "[vertical](#vertical)"
- "[missing_unicode](#missing_unicode)"
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
- "[label_text](#label_text)"
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

Discriminator string for the object or element in a query param slot.

- _type:_ string
- _values:_ 
  - `['pds_object', 'pds_text', 'pds_path', 'pds_image', 'pds_shading', 'pds_form', 'pde_element', 'pde_text', 'pde_text_line', 'pde_word', 'pde_text_run', 'pde_image', 'pde_container', 'pde_list', 'pde_line', 'pde_rect', 'pde_table', 'pde_cell', 'pde_toc', 'pde_header', 'pde_footer', 'pde_form_field', 'pde_annot', 'pds_struct_elem', 'pdf_annot']`

### alt

Alternate description for figures, images, and other structure elements (PDF/UA).

- _type:_ string

### actual_text

Replacement Unicode string for structure or content when true text is not encoded as glyphs (or for accessibility overrides).

- _type:_ string

### expansion

Spoken or spelled-out form of an abbreviation or acronym (E for expanded form in tagged PDF).

- _type:_ string

### lang

BCP 47 / ISO language tag applied to the element (e.g. en-US).

- _type:_ string

### id

Stable structure-element identifier string carried into the tag tree when set from the template.

- _type:_ string

### associated_header

Header cell id(s) this data cell relates to; use | to list multiple associations.

- _type:_ string

### has_content

True when the structure node has real page-marked content (text, paths, images) under it in the tag tree—not counting OBJR-only annotation references.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### has_annot

True when the structure element references annotations via OBJR entries (links, widgets, markup) even if no direct text path is attached.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### tag_type

PDF structure type name or regex (e.g. Figure, P, .*).

- _type:_ string
- _values:_ 
  - `['Annot', 'Art', 'Artifact', 'Aside', 'BibEntry', 'BlockQuote', 'Caption', 'Code', 'Div', 'Document', 'DocumentFragment', 'Em', 'FENote', 'Figure', 'Form', 'Formula', 'H', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Index', 'L', 'Lbl', 'LBody', 'LI', 'Link', 'NonStruct', 'Note', 'P', 'Part', 'Private', 'Quote', 'RB', 'Reference', 'RP', 'RT', 'Ruby', 'Sect', 'Span', 'Strong', 'Sub', 'Table', 'TBody', 'TD', 'TFoot', 'TH', 'THead', 'Title', 'TOC', 'TOCI', 'TR', 'Warichu', 'WP', 'WT']`

### annot_type

PDF annotation subtype name (Link, Widget, Highlight, …) or regex; use .* to match all.

- _type:_ string
- _values:_ 
  - `['Text', 'Link', 'FreeText', 'Line', 'Square', 'Circle', 'Polygon', 'PolyLine', 'Highlight', 'Underline', 'Squiggly', 'StrikeOut', 'Stamp', 'Caret', 'Ink', 'Popup', 'FileAttachment', 'Sound', 'Movie', 'Widget', 'Screen', 'PrinterMark', 'TrapNet', 'Watermark', '3D', 'Redact', 'Projection', 'RichMedia']`

### contents

Human-readable string written to the annotation Contents entry, or TU for widget tooltips when mapping to accessibility.

- _type:_ string

### annot_flag

Comma-separated list of PDF annotation flag keywords (invisible, print, read_only, …). The token contents refers to the flag bit, not this string property.

- _type:_ string
- _values:_ 
  - `['invisible', 'hidden', 'print', 'no_zoom', 'no_rotate', 'no_view', 'read_only', 'locked', 'toggle', 'contents']`

### title

Human-readable title string on annotations or widgets when exposed by the PDF.

- _type:_ string

### name

Template element `name` for this element (letters, digits, hyphen; no $ or _).

- _type:_ string

### parent

Optional parent override by element `name`; changes default element nesting.

- _type:_ string

### caption

Element `name` of an element that should be attached as this element's caption/title child.

- _type:_ string

### angle

Rotation of the text or element in radians (positive = counter-clockwise in user space).

- _type:_ float

### bbox

Axis-aligned bounds in default user space: left, bottom, right, top. Coordinates may be literals, $page_* macros, anchor offsets, or simple math. One bbox ties to one anchor for variable expansion.

- _type:_ bbox

_keys and values:_
- "[left](#left)"
- "[bottom](#bottom)"
- "[right](#right)"
- "[top](#top)"

### cell_column

The specific column index (1-based) of the cell within the table.

- _type:_ int

### cell_row

The specific row index (1-based) of the cell within the table.

- _type:_ int

### cell_row_span

The number of vertical rows this cell merges or covers.

- _type:_ int

### cell_column_span

The number of horizontal columns this cell merges or covers.

- _type:_ int

### cell_scope

Defines the accessibility scope of a header cell (Row, Column, or Both).

- _type:_ string
- _values:_ 
  - `['row', 'column', 'both']`

### col_num

Logical column count of the parent pde_table after recognition (grid width, not visual guides).

- _type:_ int

### children_num

Direct child count: layout children for pde_*, or tag-tree children including OBJR for structure nodes.

- _type:_ int

### object_num

Number of low-level PDF objects (paths, text runs, images): merged into a layout element, or associated with a structure tag via MCID.

- _type:_ int

### artifact

Indicates if the page content object is explicitly marked as an Artifact via a Marked Content Sequence (BMC/BDC tag with /Artifact property).

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### mcid

The Marked Content Identifier (MCID) assigned to this content stream object.

- _type:_ int

### has_fill

Indicates whether the object has a fill color applied.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### fill_color

The RGB components of the object's fill (interior) color.

- _type:_ rgb

_keys and values:_
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"

### has_stroke

Indicates whether the object has a stroke (border/outline) applied.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### stroke_color

The RGB components of the object's stroke (border) color.

- _type:_ rgb

_keys and values:_
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"

### fill_alpha

The opacity level of the fill color, ranging from 0 (invisible) to 255 (fully opaque).

- _type:_ int

### stroke_alpha

The opacity level of the stroke color, ranging from 0 (invisible) to 255 (fully opaque).

- _type:_ int

### has_transparency

Indicates if the element or object contains any transparency features.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### flag

Template-driven behavior on an element: for example no_join and no_split control merging; continuous keeps one structure tag across pages for tables, lists, or text when tagging; splitter ends continuous chains for the types listed in splitter; artifact, header, and footer move content out of the main reading flow.

- _type:_ string
- _values:_ 
  - `['none', 'no_join', 'no_split', 'artifact', 'header', 'footer', 'splitter', 'no_table', 'no_image', 'no_expand', 'continuous', 'anchor']`

### numbering

List numbering style for the element (None, Unordered, Decimal, UpperRoman, LowerRoman, and other schema values). Drives list attributes and ordered-marker continuation when ordinals are detected.

- _type:_ string
- _values:_ 
  - `['None', 'Unordered', 'Disc', 'Circle', 'Square', 'Ordered', 'Decimal', 'UpperRoman', 'LowerRoman', 'UpperAlpha', 'LowerAlpha', 'Description']`

### single_instance

Pipe-separated property keys; duplicates sharing those keys collapse so only the first instance is kept for tagging or layout.

- _type:_ string
- _values:_ 
  - `['type', 'width', 'height', 'left', 'right', 'top', 'bottom', 'bbox', 'font_size', 'font_name', 'text', 'fill_color', 'stroke_color', 'angle', 'alt', 'actual_text', 'flag', 'word_flag', 'text_line_flag', 'text_flag', 'lang', 'cell_column', 'cell_row', 'cell_column_span', 'cell_row_span', 'cell_scope', 'row_num', 'col_num']`

### word_space

When word_update matches and sets this float, the engine stores it as that font’s fixed space width before lines are built, so later layout uses that spacing for the font.

- _type:_ float

### font_name

PDF font base name for the text object or run.

- _type:_ string

### cos_obj

Indirect object number of the object dictionary in the PDF file.

- _type:_ int

### font_type

PDF font type from GetFontState (Type1, TrueType, Type3, CIDFont, Unknown).

- _type:_ string
- _values:_ 
  - `['Unknown', 'Type1', 'TrueType', 'Type3', 'CIDFont']`

### embedded

True when the font program is embedded in the PDF.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### bold

True when the font is treated as bold (font metrics or BaseFont name heuristic).

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### italic

True when the font has a non-zero italic angle.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### fixed_width

True for fixed-pitch (monospace) fonts.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### vertical

True when the font uses vertical writing mode.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### missing_unicode

True when the font has charcodes without a Unicode mapping.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### font_size

Font size in points (text height scale) for the object or run.

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

True when this table cell should be emitted or treated as a header (TH) for accessibility.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### cell_associated_header

Pipe-separated list of header cell ids associated with this cell (see associated_header).

- _type:_ string

### heading

Logical heading level for structure output (normal, h1–h6, h, note, title).

- _type:_ string
- _values:_ 
  - `['normal', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h', 'note', 'title']`

### width

Width of the bbox in default user space units (points).

- _type:_ float

### height

Height of the bbox in default user space units (points).

- _type:_ float

### label

List-marker classification: label_no (not a marker), label (generic), label_list (list body), or li_1–li_6 for outline depth used by list_detect.

- _type:_ string
- _values:_ 
  - `['label_no', 'label', 'label_list', 'li_1', 'li_2', 'li_3', 'li_4', 'li_5', 'li_6']`

### label_text

String or regex for the visible marker token (digits, bullets, roman numerals) consistent with pagemap_regex numbering and bullet patterns.

- _type:_ string

### left

Left edge x of the bbox in default user space.

- _type:_ float

### right

Right edge x of the bbox in default user space.

- _type:_ float

### top

Top edge y of the bbox in default user space.

- _type:_ float

### bottom

Bottom edge y of the bbox in default user space.

- _type:_ float

### baseline_x

Horizontal position of the text baseline origin for this text object.

- _type:_ float

### baseline_y

Vertical position of the text baseline for this text object.

- _type:_ float

### pdf_rect

Rectangle in default user space as left, bottom, right, top (same meaning as bbox for query macros).

- _type:_ rec

_keys and values:_
- "[left](#left)"
- "[bottom](#bottom)"
- "[right](#right)"
- "[top](#top)"

### pdf_rgb

Device RGB triplet 0–255 per channel for comparisons against fill_color or stroke_color.

- _type:_ rgb

_keys and values:_
- "[red](#red)"
- "[green](#green)"
- "[blue](#blue)"

### reflow

When false, hard line breaks in the PDF are preserved in logical text; when true, softer wrapping may be applied depending on export path.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### row_num

Detected row count for the parent table element.

- _type:_ int

### table_type

Classifier label for how the table was formed: graphic (paths), isolated, row/column text layout, or form-derived.

- _type:_ string
- _values:_ 
  - `['graphic', 'isolated', 'row', 'col', 'form']`

### text

Unicode string extracted for the object or tag: prefers marked-content text (MCID), then related annotation strings; length may be capped by max_char in tooling.

- _type:_ string

### text_flag

Paragraph-level caption and line-break hints set from detection or template (table_caption, filling, …).

- _type:_ string
- _values:_ 
  - `['none', 'table_caption', 'image_caption', 'chart_caption', 'note_caption', 'filling', 'uppercase', 'new_line']`

### text_line_flag

Line-level layout hints: hyphenation, indent, terminal punctuation, drop cap, filling, etc.

- _type:_ string
- _values:_ 
  - `['hyphen', 'new_line', 'indent', 'terminal', 'drop_cap', 'filling', 'uppercase', 'no_new_line']`

### text_state_flag

Graphics-state text attributes on a text run: underline, strikeout, highlight, sub/superscript, unicode hints.

- _type:_ string
- _values:_ 
  - `['underline', 'strikeout', 'highlight', 'subscript', 'superscript', 'no_unicode', 'white_space', 'unicode']`

### word_flag

Word-level classification flag (hyphen, bullet, numbering family, etc.) aligned with pagemap_regex-driven markers.

- _type:_ string
- _values:_ 
  - `['hyphen', 'bullet', 'colon', 'number', 'subscript', 'superscript', 'terminal', 'capital', 'image', 'decimal_num', 'roman_num', 'letter_num', 'page_num', 'filling', 'uppercase', 'comma', 'no_unicode']`

### suffix

Meta-keys (<desc>, <type>, <link>, …) that annotate schema entries for editors and docs, not runtime JSON children.


_keys and values:_

### condition

How a field is compared: fixed value (condition_value), one operator object (comparison), or an array of operators (comparison_array).


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

Example: {"0_width": 100} — parameter 0 width must equal 100.


### comparison

Example: {"0_width": {"$lt": 100}} — one comparison operator per field.


_keys and values:_
- "$eq"

### comparison_array

Example: {"0_width": [{"$lt": 10}, {"$gt": 5}]} — multiple operator objects chained on the same indexed field.


_keys and values:_
- "$gt"
- "$lt"

### keywords

Reserved template keywords: query, param, statement, disable, and related control fields shared by function nodes.


_keys and values:_
- "[general](#general)"
- "[template](#template)"
- "[query](#query)"
- "[param](#param)"
- "[statement](#statement)"
- "[disable](#disable)"
- "[purpose](#purpose)"

### general

Metadata bucket (version, dates, id, SDK) at template root.


### template

Root object that holds pagemap, element_create, *_update functions, and tagging hooks.


### query

Present on every function node: declares which object types are evaluated and optional $and/$or condition trees.


### param

Nested arrays of type names (e.g. pde_text, pde_table) aligned with the function’s insert signature.

- _type:_ array_param

### statement

$if / $elif / $else on a function node: evaluation stops at the first matching branch with a passing query.

- _type:_ string
- _values:_ 
  - `['$if', '$elif', '$else']`

### disable

If true, the entire function node is skipped. Default false.

- _type:_ bool
- _values:_ 
  - `['true', 'false']`

### purpose

Optional free-text note for authors; not interpreted by the engine.

- _type:_ string

### insert

Factory snippets the schema UI uses when inserting new template fragments.


_keys and values:_
- "[elements_add_value](#elements_add_value)"
- "[elements_add_cell](#elements_add_cell)"

### elements_add_value

Minimal pde_text initial element with zero bbox (replace with real coordinates).


### elements_add_cell

Starter pde_cell with unit span and default scope for table shells.


### math_expressions

Built-in math helpers (SUM, MIN, MAX, …) for macro or variable definitions in advanced templates.

- _type:_ string
- _values:_ 
  - `['SUM()', 'MINUS()', 'ABS()', 'MULTIPLY()', 'DIVIDE()', 'MIN()', 'MAX()', 'MOD()', 'FLOOR()', 'CEILING()']`

