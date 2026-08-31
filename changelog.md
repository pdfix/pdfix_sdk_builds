# Changelog

## [9.3.0] - 2026-08-31

### Accessibility

 * Fixed MoveChild leaving `/Pg` on an ancestor instead of the direct parent of moved structure content (PVQ-5927)

### Actions

 * Fixed Set Annotation Contents skipping on-page link annotations with a zero-size rectangle (PVQ-5949)
 * Fixed Fix Invalid Elements treating page MCR kids as orphans and Remove Invalid MCID missing page marks
 * Updated Set PDF/UA revision year default to 2024

### Metadata and Document Information

 * Fixed parsing UTF-16/32 XMP Metadata streams so Set PDF/UA and Fix Metadata no longer wipe existing properties (PVQ-5950)
 * Fixed saving PDF/A without object streams (ObjStm) or cross-reference streams (XRefStm) (PVQ-5951)
 * Fixed preserving compact XMP attributes, writing ISO 8601 dates, and declaring the pdfuaid extension schema when setting PDF/UA (PVQ-5952)
 * Fixed Dublin Core Text properties (`dc:coverage`, `dc:identifier`, `dc:format`, `dc:source`) being wrapped as `rdf:Bag` (PVQ-5953)
 * Fixed keeping localized `dc:title` `xml:lang` when setting PDF/UA (PVQ-5973)
 * Fixed Set PDF/UA dropping custom PDF/A extension schemas from `pdfaExtension:schemas`

### WebAssembly

 * Fixed UTF-16/32 XMP conversion on WASM (ICU converter not available in the WASM ICU subset)

### SDK, API

 * Modified `PdfSaveFlags::kSaveUncompressed` — also skips XRefStm; a full save of a PDF/A document applies this flag automatically

## [9.2.0] - 2026-08-13

### Accessibility

 * Fixed continuous table tagging across pages (PVQ-5831)
 * Fixed graphic table detection (PVQ-5814)

### Actions

 * Added Merge Tags action — grouping wrappers, neighbours, nested Document, Note chains, merge target, and default join values (PVQ-5452, PVQ-5834)
 * Added Fix Fonts for Form Filling action (PVQ-5695)
 * Fixed AutoTag Preflight — shown in the action; skipped when a template is set (PVQ-5876)
 * Fixed Fix Content Marks removing valid Form XObject MCIDs with Remove Invalid MCID (PVQ-5816)

### PdfDocTemplate

 * Added `tag_neighbours` template function — pair rules for Merge Tags (cross-page, Note chains) (PVQ-5452)
 * Added `object_num` on structure tags — identify associated page objects by ID (PVQ-5860)

### Metadata and Document Information

 * Fixed Catalog XMP metadata wrapping in `xpacket` (PVQ-5751)

### General Updates

 * Fixed license device identification on Windows (PVQ-5669)
 * Improved action execution performance (PVQ-5753)

## [9.1.1] - 2026-07-16

### Accessibility

 * Fixed Make Accessible mirroring text on the page when horizontal scale is negative (PVQ-5638)

### Command-Line and Pipeline

 * Fixed PsCommand pipeline output mixed with external process stderr when memory allocation exceeds limits (PVQ-5674)

## [9.1.0] - 2026-06-17

### Accessibility

 * Fixed Move tags out of parent (PVQ-3570, PVQ-4846)
 * Fixed Delete Tags with Empty Spaces removing incorrect tags (PVQ-173)
 * Fixed Remove circular mapping (PVQ-3583)
 * Fixed Deleting a link invalidating ParentTree (PVQ-3042)
 * Fixed Sect Order — missing initial element for section tables (PVQ-5317)
 * Fixed Link tag — Annotation Contents not used for Alt text (PVQ-5343)
 * Fixed Table tool issue with span cells (PVQ-5386)
 * Fixed template Formula element ignored and not tagged in document (PVQ-5520)
 * Fixed continuous list and set list numbering — missing initial element, numbering regex
 * Improved struct element MCID page-object lookup performance
 * Improved `children_tag_type` to expose Link-OBJR

### Actions

 * Added Set Unicode for Font Charcode action (PVQ-5320)
 * Added Set Annotation Flag action (PVQ-5406)
 * Added Remove Annotation Properties action (PVQ-5407)
 * Added Remove Corrupt Elements action (PVQ-5461)
 * Fixed Fix Content Marks action behavior (PVQ-4985)
 * Fixed Set Content Color — incorrect colors, CMYK range, exceptions, and error messages (PVQ-5354)
 * Fixed Tag Annotation — Document tag not created in structure tree (PVQ-5367)
 * Fixed Delete Content — missing "All Page Objects" name (PVQ-5528)
 * Fixed Fix Fonts — embedded fonts when "Embed font" was not checked (PVQ-5501)
 * Fixed Fix List Tag — Join Captions (PVQ-5438)
 * Fixed Create Bookmarks — new bookmarks created when bookmarks already exist (PVQ-5437)

### Annotations

 * Fixed stamp annotation appearance removed on flatten annot (PVQ-5405)

### Metadata and Document Information

 * Fixed XMP metadata — missing `x:xmpmeta` namespace attribute when `dc:title` is removed (PVQ-5515)

### Fonts

 * Added template-based font selection for font actions via `font_update` hook (PVQ-5451)

### PdfDocTemplate

 * Added `font_update` template function — select and filter fonts by KB rules on `pdf_font` instead of plain name regex (PVQ-5451)

### Command-Line and Pipeline

 * Fixed batch command not reporting error when working in read-only folder (PVQ-5335)

### SDK, API

 * Added `PdfTemplateQuery` — evaluate filters (regex or template hooks `tag_update`, `font_update`, `object_update`, `annot_update`), including `TestFont()` for template-based font selection (PVQ-5451)
 * Added `PdsText.GetCharOrigin(index)` (PVQ-5475)
 * Added `PdfTextState.horizontal_scale` (PVQ-5476)
 * Added PdsText scaling factors from PdfTextState to PDF-to-JSON conversion (PVQ-5477)

### Python SDK

 * Improved Python wrapper — type hints, `Optional[]`, `str` for `char*`, MYPY compatibility, pythonic None handling, `GetPath` fix (PVQ-5466)

### PDF Core

 * Fixed UTF-8 encoded string objects and dictionary keys (PVQ-5387)
 * Fixed empty dictionary keys removed when value is empty (PVQ-5371)
 * Fixed stack overflow in `get_page_object` on deep `/P` chains (PVQ-5447)
 * Fixed XRef stream (pdfium update)

### General Updates

 * Fixed warning cleanup (num_cast, literals, C4099, CMake)

## [9.0.0] - 2026-05-04

### Accessibility

 * Added support for setting Alt, Actual Text, Lang, Extension, and Title properties on structure elements through layout templates and element property update functions
 * Added and improved Fix Parent Tree, Fix Table Tag, Fix List, Set List Numbering, Move Tags, Split Content, Delete Tags, and Make Accessible workflows
 * Added support for tagging initial elements only and improved parenting of initial elements and containers
 * Added support for artifacting untagged content and improved removal of empty content marks after MCID cleanup
 * Improved list recognition, ordered list detection, label validation, label updates, and combined label flag handling
 * Improved heading level detection based on font properties
 * Improved continuous paragraph, list, and table handling
 * Improved reading order and content order in paragraphs, table headers, table cells, and split text
 * Improved auto-tagging of background words, subscript and superscript text, and text spans with layout-specific edge cases
 * Fixed Add Tags support for embedded templates
 * Fixed Remove Tags and Remove Labels behavior and performance on larger documents
 * Fixed Element Properties Update not applying Alt Text or Actual Text
 * Fixed Alternate Text and Actual Text Unicode encoding issues
 * Fixed Delete Tags crashes and Fix Parent Tree issues
 * Fixed Split Content duplication and Split Pages issues
 * Fixed Autotag hangs with substructure XObjects

### Actions

 * Added Fix Table action 
 * Added Split Content action
 * Added Fix Metadata and Reset Metadata actions
 * Added Fix Fonts action, which replaces Embed Fonts and Add Missing Unicode with new options
 * Added Move Tags action
 * Added Set Title action option to use the document title from the Info dictionary
 * Added support for running combined external and base custom actions directly from the SDK
 * Added support for embedding external custom actions into the SDK, including APIs to save and enumerate custom actions
 * Added support for external actions in `PsCommand` 
 * Added Fix Headings parameter Assign heading levels to regenerate H1–H6 from font style and leading numbering
 * Updated Set Annotation Contents action to use previous, next, and parent tag text for annotation content
 * Updated Create Bookmarks action to correctly remove existing bookmarks when overwrite is enabled
 * Fixed Set Annotation Contents action for widget annotations with empty or missing TU values
 * Fixed Remove Annotation Properties action for widget annotations
 * Fixed Set Title action when deriving the title from the file name

### External Actions

 * Improved Create Layout Template (Docling) and AutoTag (Docling) action to support List, complex Tables, and element parenting 
 * Added a new external AutoTag (PDFix) action that utilizes layout templates and ensures backward compatibility by using the appropriate PDFix SDK version

### PdfDocTemplate

 * Added `element_nest` function to layout templates
 * Added `element_prop_detect` function to set element properties
 * Added `has_annot` and `is_standard_tag` support for structure element and template processing
 * Added title support for structure elements in layout templates
 * Added template support for Alt, Actual Text, Lang, and Extension properties
 * Fixed regular expression matching for empty strings in layout templates
 * Fixed UTF-8 to PDF string conversion from JSON templates
 * Fixed table detection crashes caused by invalid templates
 * Fixed alternate text encoding from templates
 * Improved text insertion, text-in-place handling, line sorting, baseline checks, and text run bounding box recalculation

### Annotations

 * Fixed annotation rectangles for initial elements
 * Fixed widget annotation TU handling in Set Annotation Contents
 * Fixed removal of annotation properties for widget annotations

### Metadata and Document Information

 * Added `PdfObjectInfo` and `PdfDoc.AcquireObjectInfo(string)` for veraPDF-style object identification
 * Added Export Bookmarks to JSON
 * Fixed saving PDF version 2.0 documents so they are not incorrectly saved as PDF version 1.0

### Fonts

 * Added Fix Font support for `.notdef` glyph compliance issue (clause 7.21.8)
 * Improved font name comparison in the knowledge base
 * Fixed preflight issues with font names containing unsupported characters

### Command-Line and Pipeline

 * Refactored CLI batch command output handling for JSON output to file or stderr
 * Fixed CLI batch command exit codes on exceptions
 * Fixed forwarding of subprocess stdout and stderr in `pdfix_app batch`

### WebAssembly

 * Enabled WASM memory growth with `-s ALLOW_MEMORY_GROWTH=1`

### SDK, API
* Added `PdfObjectInfo` - New object for parsed information about a PDF object identified by a string path, intended for resolving validator paths such as veraPDF object references.
* Added `PdfDoc::AcquireObjectInfo(const wchar_t* path)` - Acquires `PdfObjectInfo` for a validator-style object path so callers can resolve page, annotation, content, MCID, object-id, and bounding-box information.
* Added `PdsStructElement::HasContent()` - Checks whether the structure element is connected with page content through MCID/MCR.
* Added `PdsStructElement::HasAnnot()` - Checks whether the structure element contains an annotation reference, OBJR, directly or indirectly.
* Added `PsCommand::SaveActionsToStream(PsStream* stream, PsDataFormat format, PdfSaveFlags flags)` - Serializes all built-in PDFix action definitions to a stream for discovering actions, parameters, and options.
* Added `PsCommand::GetNumCustomActions()` - Returns the number of embedded custom action presets distributed with the SDK.
* Added `PsCommand::SaveCustomActionToStream(int index, PsStream* stream, PsDataFormat format, PdfSaveFlags flags)` - Serializes one embedded custom action preset to a stream for inspection or execution through `PsCommand`.
* Added `Pdfix::GetCommand()` - Creates a `PsCommand` object, or returns null if creation fails.
* Added `PdfObjectInfo::GetType()` - Returns the parsed object reference type.
* Added `PdfObjectInfo::GetPageNum()` - Returns the zero-based page index for a page-specific object path, or `-1` when no page is associated.
* Added `PdfObjectInfo::GetCount()` - Returns the number of parsed path entries.
* Added `PdfObjectInfo::GetBBox(int index, PdfRect* bbox)` - Returns the bounding box associated with a parsed path entry, if available.
* Added `PdfObjectInfo::GetAnnotIndex(int index)` - Returns the zero-based annotation index for a parsed entry.
* Added `PdfObjectInfo::GetContentStreamId(int index)` - Returns the content stream identifier for a parsed entry.
* Added `PdfObjectInfo::GetContentId(int index)` - Returns the content identifier for a parsed entry.
* Added `PdfObjectInfo::GetNumContentItemIds(int index)` - Returns the number of nested content item identifiers for a parsed entry.
* Added `PdfObjectInfo::GetContentItemId(int index, int index2)` - Returns one nested content item identifier from a parsed entry.
* Added `PdfObjectInfo::GetOperatorId(int index)` - Returns the content operator identifier for a parsed entry.
* Added `PdfObjectInfo::GetMcid(int index)` - Returns the MCID associated with a parsed entry.
* Added `PdfObjectInfo::GetObjectIdCount()` - Returns the number of COS object identifiers referenced by the parsed path.
* Added `PdfObjectInfo::GetObjectId(int index)` - Returns one COS object identifier extracted from the parsed path.
* Added `PdfObjectInfo::Release()` - Releases the `PdfObjectInfo` object and returns the remaining reference count.
* Modified `PdeList` - Changed inheritance from `PdeElement` to `PdeContainer`, exposing list elements as containers.
* Modified `PdsStructElement::SetActualText(const wchar_t* text)` - Parameter name changed from `alt` to `text`; the function still sets the ActualText value for the structure element.
* Modified `PdsStructElement::RecognizeTable()` - Return type changed from `bool` to `PdsStructTableError`, allowing callers to inspect detailed table recognition errors.
* Modified `PsAccountAuthorization::Authorize(const wchar_t* license_name, const wchar_t* license_key)` - Parameter names changed from `email` and `serial_number` to license name/key terminology.
* Added `PdfContainerType::kPdeContainerList` - Adds list container type.
* Added `PdfElementFlags::kElemNone` - Adds explicit no-flag value.
* Added `PdfElementFlags::kElemNoNesting` - Adds a flag that prevents nesting.
* Added `PdfLabelType::kLabelList` - Adds explicit list-label value.
* Added `PdfLabelType::kLabelLevel5` - Adds list label level 5.
* Added `PdfLabelType::kLabelLevel6` - Adds list label level 6.
* Added `PdfObjectInfoType` - Adds object identification types used by `PdfObjectInfo`, including document, metadata, structure tree, structure element, bookmark, font, annotation, content, content item, and XObject.
* Modified `PdfLabelType::kLabel` - Meaning changed to marked as label but do not create lists.
* Modified `PdfTextStyle` - Replaced separate `kTextH7` and `kTextH8` heading styles with generic `kTextH`.
* Modified `PdsStructTableError` - Reworked table errors to report invalid span, invalid tag type, and missing table headers.
* Modified `PdfCellParams` - Added `PdsStructTableError error`, initialized to `kTableErrorNone`.
* Removed `PsCommandType` - Removed typed command/action group enum for base, make accessible, autofix, and quickfix command exports.
* Removed `PsCommand::SaveCommandsToStream(PsCommandType type, PsStream* stream, PsDataFormat format, PdfSaveFlags flags)` - Removed typed command export API; replaced by `SaveActionsToStream()`, `GetNumCustomActions()`, and `SaveCustomActionToStream()`.
* Removed `PdfTextStyle::kTextH7` - Removed H7 heading style value; replaced by generic `kTextH`.
* Removed `PdfTextStyle::kTextH8` - Removed H8 heading style value; replaced by generic `kTextH`.
* Removed `PdsStructTableError::kTableErrorNoRow` - Removed missing-row table error value.
* Removed `PdsStructTableError::kTableErrorRowSpan` - Removed rowspan-specific table error value; replaced by generic span error handling.
* Removed `PdsStructTableError::kTableErrorColSpan` - Removed colspan-specific table error value; replaced by generic span error handling.

### General Updates

* Improved logging support 
* Fixed C# marshaling of `const char*` return values as `IntPtr`
* Fixed license management in concurrent processes
* Performance, stability, memory management

## [8.7.10] - 2026-01-10

### Template
- Fixed label removal behavior in pde_table.

### General
- Fixed an issue with writing clip paths inside XObjects in the content writer
- Fixed incorrect line dash handling when modifying page content
- Renamed the argument in *SetActualText* from the previous name to *text* for improved API consistency

## [8.7.9] - 2025-12-30

### Template
- Added *text_line_baseline_elem_ratio* – Maximum allowed baseline shift between a text line and its elements

### WebAssembly
- Enabled memory growth beyond 1GB in the WASM module

## [8.7.8] - 2025-12-17

### Actions
- Changed default value of Overwrite property to *AutoTag* action to *true*

## [8.7.7] - 2025-12-15

### Actions
- Added Overwrite property to *AutoTag* action
- Added support for embedded template in the *AutoTag* action
- Added Export Bookmarks option to *Convert to JSON* action
- Added secured flag to document information in *Convert to JSON* action
- Fixed regular expression for Links in *Set Annotation Contents* action

### Metadata
- Fixed updating Medatada with invalid namespaces and duplicate entries

### Template
- Fixed encoding of Unicode characters in the Alt or Actual Text in the auto-tagging layout template

### General
- Fixed error handling in failures when loading template JSON files

## [8.7.6] - 2025-10-16

### Accessibility
- Fixed Set Alternate Description action errors when used with layout templates
- Fixed issue preventing dc:title metadata field updates during metadata repair

## Actions
- Fixed Delete Tags action behavior after auto-tagging

## [8.7.5] - 2025-10-09

**Accessibility**
- Added support for reading order definition in the *create_element* function within the auto-tagging template
- Added support for table associated headers in layout template

**Actions**
- Added *Fix Link Tag* action to correct errors in Link tags, setting the destination and zoom factor
- Added *Set Content Language*, *Set Document Language*, and *Set Tag Language* actions
- Fixed *Set Content Color* action to support page objects

**Command-Line**
- Added new parameter `--no-sequential-headings` to the *add-tags* command

**General**
- Added method `PdsStructElementValidChild`
- Fixed writing of document XMP metadata 
- Stability and performance updates

## [8.7.4] - 2025-09-05

**Accessibility**
- Added action *Set Language* for Tag and the Content
- Fixed untagged elements remaining when tagging tables
- Fixed duplicate Metadata entries being created in rdf:Description
- Fixed *Remove Content Marks* action when removing invalid MCIDs
- Updated *Fix Link Tag* action to fix link destinations
- Improved contionuous tables tagging
- Improved *Add Associated Headers* support in layout template


**PdfDocTemplate**
- Added `has_fill` and `has_stroke` properties to identify objects by graphical appearance
- Added support for ECMAScript regular expression case-insensitivity switch `/i` 
- Fixed parsing of RGB color values from templates

**Command Line**
- Added render-pages command to export document pages as images (PNG, JPEG)

**General Updates**
- Improved performance, memory management, and overall stability

## [8.7.3] - 2025-08-11

**Accessibility**
- New action Set Content Color
- New action Fix Page Orientation
- Add a missing URL prefix support in Create Web Links 
- Associated headers support in the layout template
- Fixed Create Bookmarks from Headings with nested tags
- Fixed Create Alternate description for Widget annotations

**General Updates**
- Performance, memory allocation, and stability updates

## [8.7.2] - 2025-07-18

**Accessibility**
- Fixed circular role mapping errors
- Fixed tagging of inline images in paragraphs
- Added action Remove Annotation Properties
- Removed generic annotation contents during autotagging
  
**PdfDocTemplate**
- Fixed evaluation of `$child_tag_type` of the struct element object

**General Updates**
- Performance, memory allocation, and stability updates

## [8.7.1] - 2025-07-10

**PdfDocTemplate**
- Always create a List tag if the list label is set
- Fixed math functions in the query

**Annotations**
- Create Web Links support for user-defined URI address

**General Updates**
- Performance, memory allocation, and stability updates

## [8.7.0] - 2025-06-23

**Accessibility**
- Added AddAssociatedFile, GetAssociatedFile to manage the structure element's associated files

**PdfDocTemplate**
- Layout recognition reading order updates
- Hyphen detection regular expression update

**General Updates**
- Added PdsFileSpec object to manage embedded files
- Performance and stability updates

## [8.6.1] - 2025-06-16

**Accessibility**
- Set Actual text, Language, ID, and Alt to structure elements when auto-tagging text content

**PdfDocTemplate**
- Updated thresholds for word and line detection

**General Updates**
- Fixed processing files with special characters in the Command-Line application
- Performance and stability updates

## [8.6.0] - 2025-06-05

**Accessibility**
- Support for re-tagging content defined by template with `add_tags` action

**PdfDocTemplate**
- Added support for dynamic element definition using anchors and start/end positions
- Added support for nested templates for pre-defined elements
- Added MATH expressions support in values

**Document Assembly**
- Support for `split_pages` based on the template

**Annotations**
- Added support to create web links from emails

**General Updates**
- Debugging support for the template creation process
- Performance and stability updates

## [8.5.4] - 2025-05-16

### Added 
- Added creating mailto: links in the Create Web Links Action

### Fixed
- Fixed Fix Spaces Action sometimes does not process all tags in the PDF
- Fixed path content writer issues causing content loss

## [8.5.3] - 2025-04-15

### Fixed
- Font Embedding of base 14 fonts

## [8.5.2] - 2025-04-14

### Fixed
- Fixed tagging overlapping annotations over text content
- Fixed embedding TrueType fonts containing non-ansi characters

## [8.5.1] - 2025-03-28

### Fixed
- Fixed duplicate MCID generated in content with nested content marks
- Fixed missing tag name in BDC content mark in text content

### Changed
- Enhanced precision in matching annotations with text content

## [8.5.0] - 2025-03-16

### Added
- Added `PdfDoc.SetPath` and `PdfDoc.GetPath` to control the document path when loading from memory or a custom stream
- Added support for updating invalid document metadata

### Fixed
- Fixed failure to load on macOS Intel in Java
- Fixed PDF-to-JSON export of text from structure elements, Base64 images, and annotations
- Fixed updating of the document modified flag after running the set_pdf_version action
- Fixed reloading of `PdePageMap` after a change in `PdfDocTemplate`
- Fixed `xmp:ModifyDate` format in metadata
- Fixed `remove_content_marks` action when removing invalid MCID in MCR structure elements
- Fixed soft/hard hyphenation tagging
- Fixed auto-tagging of text spans with annotations

### Changed
- Updated subscript/superscript detection in layout recognition

## [8.4.3] - 2024-12-17

### General
- Java 8 support, library built with JDK version 1.8.0

### Fixed
- Fixed python module initialization on Windows

## [8.4.2] - 2024-12-12

### Fixed
- Fixed python module initialization on Windows

## [8.4.1] - 2024-12-02

### General
- Integration udpate for PDFix Pipeline
- Performance and stability improvements

## [8.4.0] - 2024-11-20

### Added 
- Added command Clone tagged and non-tagged XObjects

### Fixed
- Fixed duplicit MCID error when auto-tagging
- Fixed reversed flags for marking headers/footers in template

### General
- Performance and stability improvements

## [8.3.1] - 2024-11-05
### Fixed
- Fixed PsProgressControl raises an exception if initiating with zero steps
- Fixed Modification Date format in document Metadata

### General
- Performance and stability improvements

## [8.3.0] - 2024-10-31
### Added
- New Actions (previously Commands)
  - __Add Table Summary__ action
  - __Set PDF Version__ action
  - __Set Actual Text__ action
  - __Set Associated Headers__ action
  - __Rename Tags__ action
  - Add extended Tag properties support to PSCommand
- Added methods `PdfDoc.SetFlags`, `PdfPage.SetFlags`
- Added `PdsStructTable` class for handling Table structure elements

### Changed
- Updated __PDF to HTML__ and __PDF to JSON__ conversion for pipeline-runner
- __Set PDF modification date__ when saving
- __Create Bookmarks Action__ now allows defining multiple tags for bookmark levels
- __Deleted rolemap__ after applying standard tags
- __Set Annotation Contents Action__ changed default value to "text in bbox"
- Added `--lang` and `--title` parameters to the `make-accessible` CLI command

### Fixed
- Issues with Artifact and Set Content Marks in Form XObjects
- Incorrect order in list and table elements after autotagging
- `PdsStructElement.MoveChild` now correctly updates the StructElement page number

### General
- Performance and stability improvements

## [8.2.0] - 2024-08-25
### Added 
- Added PdsStructElement.GetBBox the union bounding boxes on the page number on which the content items designated by the K entry are rendered

### Changed
- Changed Java JAR package contains native libraries
- Renamed kCommand... contants to kAction...

### Fixed
- Fixed default MakeAccessible action does not specify bookmark levels

## [8.1.11] - 2024-08-24
### Fixed 
- Fixed dependencies on linux platforms

## [8.1.10] - 2024-08-16
### Fixed 
- Fixed Docker compatibility for linux/amd64 and linux/arm64 platforms

## [8.1.9] - 2024-08-07
### Added 
- Added option for Delete Tags command to move childs to parent structure element

### Fixed
- Fixed ToUnicode formatting issues


## [8.1.8] - 2024-08-06
### Added 
- Added Quick Fix command for fixing common accessibility issues

### Fixed
- Fixed flattening XObject with text inside causes text to hide
- Fixed Python function signatures returning string values

### Added 
- Linux aarch64 support

## [8.1.7] - 2024-08-01

### Added 
- Linux aarch64 support

### Fixed
- PDF File saves invalid XRefStm in some linux distributions
- Could not load Windows dll due to missing system dependencies
- PdfDoc.AddMissingUnicode invalidates font PDF/UA compliance
- PdfDoc.AddTags may create diplicate MCID entry on non-text objects
- PdfDoc.CreateXObjectFrom page from another document

## [8.1.1] - 2024-06-18

### Changed
- Licensing - page counter updates local consumption upon sucessfull save/export only

### Fixed
- Support for View Destination defined as a object reference
- Fixed update of Structure element attributes defined in indirect object
- Fixed Template alt_text top-bottom reversed position 
- Support for multiple same owner structure element attributes

## [8.1.0] - 2024-06-06

### Added
- Added Create URL link from content command
- Added Replace font by regex command

### Changed
- CLI pdfix_app overwrites input file if output is not set

### Fixed
- Fixed Nuget package runtime native libraries load

## [8.0.1] - 2024-05-03

### Changed
- New simplified and customizable command line make-accessible command 

## [8.0.0] - 2024-05-02

### Added
- Added PsProgressControl class to control long processes (replaces cancelProc parameter)
- Added new PdfDoc enumeration interfaces with custom selection for bookmarks, pages, page objects, fonts, structure elements
- Added PsCommand.Run function (replaces individual PsCommand methods)
- Added Batch Commands
  - Save validation report into file
  - Remove standard tags mapping
  - Set PDF/UA Standard
  - Set Suspect Value
  - Fix Optional Content
  - Remove Standard Tags Mapping
  - Fix Media Clip
  - Tag Annotations
  - Set Tag BBox
  - Set Alternate Description
- Added Batch Command Parameters
  - Set Document Properties
    - Set Producer
    - Set Keywords
  - Set Title
    - Use the first Description Tag
    - Retrieve the title from the file name
  - Set Language
    - Apply Language to Document, Tag, Marked Content
  - Delete Tags
    - Invalid Tags

### Changed
- CancelProc for cancelling processes moved to PsProgressControl, all API functions affected

### Fixed 
- Editing tags and content marks of for XObjects

## [7.3.3] - 2024-03-13

### Fixed
- Embed fonts fails when called multiple times
- Dot filling text marked as artifact when tagging as Table or other tag
- Multiple MCID assigned for page objects split by artifact when tagging

## [7.3.2] - 2024-02-27

### Added
- Append HTML support for PDF to HTML batch command

### Fixed
- Fixed generation of ToUnicode CMap stream in character unicode mapping

## [7.3.1] - 2024-02-16

### Added
- Added PdfHtmlConversion.AddHtml method to append HTML code into converted document
- Added CLI parameter for `pdf2html` command `-a`|`--append-html` 
- Added offline license activation support 

### Fixed
- UFT-8 encoding issue in PDF to HTML conversion using the derivation algorithm

## [7.3.0] - 2024-01-22

### Added
- Set Doc Info command includes set PDF/UA standard
- Set PDF/UA Standard command

### Fixed
- Progress control in commands MakeAccessible, ConvertToHtml
- Untagged content after Make Accessible
- Virtual Windows server license activation
- Create Bookmarks from Headings creates empty bookmarks for nested tags
- Error messages from CLI

## [7.2.0] - 2023-11-29

### Added
- Added Docker support
- Added Nuget package support for  Linux (amd64), MacOS(amd64, arm64)
- Added NPM package 
- Added modulus operator mod(a,b) in template
- Progress monitoring in CLI
- Export to JSON including content marks

### Fixed
- Fixed creating XObject from 1 BPC Image JPG images
- Fixed adding missing spaces while tagging
- Autotag breaks transparency in PDF object


## [7.1.0] - 2023-09-21

### Added

- Delete empty tags after TagAs 
- Fix placement for Note
- Rotate pages PsCommand

### Fixed 
- Adding spaces when tagging generates too many mcids
- Fix spaces does not embed font correctly on Linux
- Delete Tags support for tables and rows
- MoveTag removes the reference to parent object P
- Add Objects to Tag does not assign direct MCID
- Fixed Set Suspect Value
- Remove annot from tag tree if re-taging if UA support is on
- Flattening form fields causes appearance offset 
- Page.SetContent skews the content
- Tag Annotation Error
- Unicode character converted incorrectly into HTML in derivation
- Convert to HTML invalid annotation raises an exception


## [7.0.1] - 2023-07-28

### Changed
- Delete Tags command uses regular expression to define tag names
- Set Contents command uses regular expression to define annotation types

### Fixed
- Fixed Conversion to HTML when invalid annotation appears
- Content writer issues

## [7.0.0] - 2023-06-28
### Added
- Added PsCommand FixWhitespaces, SetStructureAttribute, RemoveContentMarks
- Added CLI batch command
- Added PdsPageObject.TransformCTM
- Added flags support for WordFinder
- Added PdfDoc.CreateXObjectFromPage
- Added support for macOS M1 chips

### Changed
- Convert Structure Tree to JSON includes type and attributes
- Embed Font command failed
- Get Document Properties output unreadable
- Layout and content recognition updates

### Fixed
- Fixed flatten annots issue
- Fixed adding char spaces in autotag
- Fixed flatten form XObject invalid matrix
- Fixed word geometry calculation on rotated pages
- Fixed handling marked content sequences in derivation
- Fixed autotag table colspan issue
- Fixed required flag support to the HTML form field

### Removed
- Removed PdsPageObject.SetMatrix 

## [6.20.0] - 2023-02-15
### Added
- Added PdfDoc.SetTagId to add required tag IDs
- Added PsCommand.RepairIdTree and PdsStructTree.RepairIdTree
- Added PdeCell.GetNumAssiciatedHeaders, GetAssociatedHedder, AddAssociatedHeader, RemoveAssociatedHeader
- Added PdeElement.GetTagId, SetTagId
- Added PdeCell.GetColNum, SetColNum, GetRowNum, SetRowNum
- Added PdfDocJsonConversion extract page content

### Fixed
- PdePageMap.AddTags support for tag ID
- PdeCell Associated headers manipulation support
- Fixed PageMap initial table element not created if no children were found
- Fixed PdfLinkAnnot.AddQuad invalid order of quad points
- PDF to HTML font size optimization

### Removed
- Removed PdfDoc.AddTagId

## [6.19.0] - 2022-11-11
### Added
- Added PdsString.IsHexValue method to check if string is hex or literal object (1072)

### Fixed
- Fixed AddTags does not remove mcid childs from struct tree (1085)
- Fixed PdfToHtml conversion text color flag (1083)

## [6.18.0] - 2022-09-07
### Added
- Added option to change the license file path (322)
- Added struct element rect attribute in derivation (395)
- Added method PdsObject.Clone (1035)
- Added PdsPageObject::GetContentStreamIndex (1049)
- Added method PdfPage.CloneFormXObjects (1064)
- Added PdfDoc.HasPassword method (1018)
- Added option to change the page struct element from nonStruct to custom tag (1002)
- Added method PdeElement.GetTag, SetTag (1001)
- Added PdfJsonConversion class (1000)
- Added PsCommand for batch processing
- Added batch command into pdfix_app (942)
- Added PdfDocUtils.EnumAnnots, EnumPageObjects, EnumStructElements (956)
- Added PdfAnnot.GetPageObject method (951)
- Added PdfDocUtils class to handle document maintenance and fixing (952)
- Added PdfPage.CreateFomFromObject (899)

### Changed
- Changed pdf_config to contain document settings, rename general to matedata (1051)
- Changed PdfTemplate "statement" node mandatory

### Fixed
- Fixed writing encrypted object streams (1022)
- Fixed form xobject not marked as artifact after autogagging (1063)
- Fixed CreateParent tree causes exception if Nums array is missing (1062)
- Fixed PdsContentUndoEntry on form object optimization (1059)
- Fixed PdePageMap.AddTags does not clear previous object structure on all objects (1044)
- Fixed Invalid ptr in C# wrapper if the function returning Struct that not filled (1039)
- Fixed setting document title in metadata (931)
- Fixed PDF/UA support when removing annotation (923)
- Fixed update parent tree after removing OBJR child from struct tree (921)
- Fixed PdsStrucTree.AddAnnot (912)
- Fixed CPdsStructElement.GetChildPageNumber (898)
- Fixed not rendering widget annotations even with renderAnnot flag (896)

## [6.17.0] - 2022-02-11
### Added
- Added Pdfix.LoadSettingsFromStream to load SDK settings (#863)
- Added PdfFont.GetObject method (#860)
- Added PdfDoc.SetPdfStandard method (#843)
- Added support for freetext annotation appearance (#840)
- Added PdfDoc.SetVersion to set the document PDF version (#835)
- Added PdsContentMark.SetTagName, SetTagObject (#829)
- Added PdsStructElement.MoveChild method to move child object to another struct element (#828)
- Added PdfDocConversion, PdfHtmlDocConversion, PdfTiffDocConversion class for handling document conversion (#822)
- Added PdsPageObject.RemoveTags method to remove object's content marks (#816)
- Added PdfFont.GetEmbedded, GetUnicodeFromCharCode, SetUnicodeFromCharCode (#815)
- Added PdsPageObject.GetMcid (#812)
- Added PdfPage.DrawContent support for subpixel rendering (#810, #809)
- Added PdsContentMark.RemoveTags to remove tags by type (#808)
- Added PdfDocTemplate support for fill/stroke color of PdsPageObject (#804)

### Changed
- Changed PdfDoc.RemoveSecurity method to return bool (#877)
- Changed PdsStructElement.AddTag, InsertTag methods argument (#869)
- Changed PdsPageObject.GetBBox to return transformed rect according to page coordinate system (#854)
- Changed PdfToHtml plugin to be a part of the PDFix SDK core library (#851)
- Changed PdfDocTemplate.SetDefaults to clear document preflight data (#850)
- Changed PdsStructElement.SetParent to remove element from its previous parent (#803)
- Changed PdsStructElement.RemoveChild to remove mcid from page object content mark dictionary (#788)

### Fixed
- Fixed memory management issues (#875, #874, #872, #870, #801)
- Fixed saving the PDF file with object stream (#866)
- Fixed changed path fill color creating page map (#846)
- Fixed reading unicode keys in the PdsDictionary (#845)
- Fixed table recognition when empty cells are present (#844)
- Fixed PdfDoc.RemoveBookmarks does not remove Outlines in document root (#834)
- Fixed writing content mark name with space character (#833)
- Fixed PdfDoc.InsertPages to copy also inheritable page keys (#831)
- Fixed PdfPage.GetRotate on document with multi-level pagetree (#830)
- Fixed ArcTo, when arc is half-circle (#827)
- Fixed conversion of combobox export values into HTML (#879)
- Fixed conversion of hidden form field into HTML (#880)


## [6.16.0] - 2021-10-29
### Added
- Added .NET API support for Disposable objects
- Added PsRenderDeviceContext class to handle different types of devices for rendering (#740)
- Added PdsStructTree.RemoveRoleMap, CreateClassMap, RemoveClassMap (#766)
- Added PdfDoc.GetVersion (#767)
- Added PdsContentMark.InsertTag, GetNumEqualTags (#770, #780)
- Added PdsClassMap.GetObject method (#772)
- Added PdsObject.RegisterEvent, UnregisterEvent with notification kEventWillChange, kEventDidChange, kEventWillDestroy (#779)
- Added PdsContent.RegisterEvent, UnregisterEvent with notification kEventWillChange, kEventDidChange (#785)
- Added PdsPageObject.RegisterEvent, UnregisterEvent with notification kEventWillDestroy (#786)

### Changed
- Changed do not allow delete page when it's acquired (#777)
- Changed PdfDoc.Close to force closing document even if refcount not zero (#791)

### Fixed
- Fixed setting unicode string values in PdsStructElement and PdfBookmark (#764)
- Fixed content writer when saving nested BDC .. EMC operators (#765)
- Fixed nested content marks in the page content (#771)
- Fixed PdePageMap autorotate reverts to original after elements are created (#774)
- Fixed PdfBookmark.Unlink method (#775)
- Fixed PdePageMap.CreateElements returns false when template is invalid (#787)

## [6.15.0] - 2021-10-04
### Added
- Added PdfPage.RemoveArtifact SDK-758 
- Added PdfPage.ArtifactNonTaggedContent (#757)
- Added method PdfDoc.CreateRoleMap (#753)
- Added method PdsRoleMap.GetObject (#754)
- Added method PdfDoc.CreateBookmarkRoot (#752)

### Fixed
- Fixed saving page content with too large transformation (#756)

## [6.14.0] - 2021-09-14
### Added
- Added PdfAnnotHandler class (#547, #580, #590, #594, #605, #648)
- Added PdfActionHandler class (#629, #647, #681)
- Added PdfAnnot.Copy, Paste (#646, #676, #677)
- Added PdfAction.GetNumChildren, GetChild, RemoveChild to support next action (#684, #685)
- Added PdfBookmark.RemoveChild, AddChild (#698)
- Added PdePageMap.HasElements to check if the elements were created (#710)
- Added PdsStructTree.AddKid & PdsStructElement.AddKid (#720)
- Added PdfDoc.GetUserPermissions to read document's user permissions #735
- Added PdsPageObject.GetContent to get reference to parent PdsContent (#736)
- Added PdfDocUndoDidCreate, PdfDocUndoWillDestroy notifications (#746)

### Changed
- Changed AcquireAction and AcquireViewDestination to GetAction, GetViewDestination (#695)
- Changed PdfBookmark.RemoveChild returns removed PdfBookmark (#698)
- Changed PdfStructElement.AcquireStructElement to GetStructElementFromObject (#702)
- Renamed PdfStructElemen.CreateStructElement to AddNewKid (#722, #723)
- Changed PdsContentMark method GetTagArtifact returns PdsDictionary (#725)
- Changed method Close returns number of references (#729)
- Renamed PdfDocAddNewUndo to PdfDoc.CreateUndo (#747)

### Fixed
- Fixed auto-rotated page after running page map (#674)
- Fixed saving style outside of head element when converting PDF to HTML (#680)
- Fixed setting a color of a bookmark in SetAppearance method (#691)
- Fixed redaction of image masks (#692)
- Fixed crash when reading struct tree (#697)
- Fixed crash when processing page content (#703, #704, #734, #749)
- Fixed adding bookmark children on invalid index (#707)
- Fixed html plugin throws exception when pagemap elements were already created (#710)
- Fixed output path determination in conversion to html (#713)
- Fixed GetParent on bookmark. Functioned returned null when the bookmark was removed & added to the bookmark tree again (#714)
- Fixed PdfDocTemplate::LoadFromStream - does not duplicate already existing entries in JSON (#727)
- Fixed Missing PDF pages failed to load in the HTML output without error (#728)

### Removed
- Removed AddNewAnnot methods, and Added PdfAction SetViewDestination for action (#700, #688)


## [6.13.0] - 2021-06-28
### Added
- Added PdfBookmark methods GetNext, GetPrev, GetParent (#671, #668)
- Added method PdfDoc.GetBookmarkFromObject (#650)
- Added method PdsPageObject.GetDoc (#659)
- Added SetAction method to PdfWidgetAnnot, PdfLinkAnnot (#654, #653)

### Changed
- Changed method PdsText::GetTextState not to require PdfDoc reference (#660)

### Fixed
- Fixed method PdfDoc::GetInfo modifies the document (#620)
- Fixed content writer when page object has zero transformation matrix (#649)

### Removed
- Removed method PsMetadata.LoadFromStream (#655)
- Removed GetStructElement from PdsStructTree (#666)

## [6.12.0] - 2021-06-09
### Added
- Added methods IsOpen, SetOpen to read write bookmark open state (#643)
- Added notifications will/did add/remove/change to PdfDocTemplate, PdsObject, StructTree, StructElement, PdePageMap (#635, #639, #633, #634, #609)
- Added method PdfDoc.ClearFlags (#630)
- Added PdfPage.GetRefNum method (#611)
- Added conversion of button field style to HTML (#607)

### Changed
- Changed PdePageMap acquisition, object creation and manipulation (#602, #608, #610, #600)
- Changed add watermark CLI parameters (#572)

### Fixed
- Fixed missing objects when saving document multiple times (#631)
- Fixed charcode from unicode conversion (606)
- Fixed structures with default value None in python API (#601)
- Fixed memory management, object reference count control acquire/release  (#571, #570)

## [6.11.0] - 2021-05-13
### Added
- Added method PdsObject.GetDoc (#522)
- Added kEventDocDidChangeFlags notification when document flags did change (#552)
- Added PdsWord.GetQuad method (#558)
- Added PdfStandardSecurityHandler and PdfCustomSecurityHandler interface (#530, #537)
- Added PdfDoc methods Authorize, IsSecured to enable opening document without password (#525, #528, #529, #536, #541)
- Added PdfWordList object to access words on the page (#560, #569)

### Changed
- Changed c++ API PdfPoint, PdfDevPoint default constructor (#557)
- Changed PdfPage::AcquirePageMap to improve performance (#562)
- Changed PdfPage::FlattenAnnot, FlattenFormXObjects do not save new page content directly (#564, #567)
- Changed PdfPage::Release method returns the number of remaining references (#555)

### Fixed
- Fixed FlattenAnnots when appearance object is missing form XObject Type and Subtype key (#578)
- Fixed scrolling effect of converted PDF form to HTML (#554)
- Fixed application of trialstamp after content redaction (#545)

### Removed
- Removed CPdfDoc::AddWatermarkFromImage and structures PdfPageRange, PdfWatermarkParams (#572)
- Removed PdfWordFinder object (#560, #569)
  
## [6.10.0] - 2021-04-21
### Added
- Added method PdfAnnot.SetFlags (#540)
- Added const to exported functions (#506)
- Added PdsText.GetCharStateFlags, SetCharStateFlags method to set the flag on text run character (#518)
- Added PdeWord.GetCharStateFlags method to get the flag on character (#519)
- Added support for kStateExclude flag for method PdeWord.GetCharStateFlags when converting to HTML (#520)
- Added PdsTextRun & PdeTextRun interfaces and methods that allow us to iterate over textruns in words (#507)
- Added PdsContentMark.Equals method to compare two content marks (#509)
- Added PdfUndo object to support undo, redo for PdsObject manipulation (#501)
- Added PdsDictionary.RemoveKey method (#499)
- Added cancel proc and progress control to PdfDoc.EmbedFonts, ApplyRedaction, AddFontMissingUnicode, PdfPageMap.AcquireElements, PdfHtmlDoc.Save, PdfHtmlDoc.SaveDocHtml, PdfHtmlDoc.SavePageHtml (#493, #478, #479, #480)
- Added PdfStateFlags.kStateDefault enum value (#486)
- Added PdfWordFinder class to access page words (#465)
- Added method PdfDoc.CreateBooleanObject (#484)
- Added method PdfDoc.GetFlags to identify the document state (#517)

### Changed
- Changed doubles to floats in the API (#471)
- Changed PdfPage method FlattenAnnot to add annotation appearance into page content as a FormXObject through PdsContent (#495)
- Renamed PdsPageObject methods MoveTo, CopyTo to MoveToContent, CopyToContent (#491)

### Fixed
- Fixed loading multiple config jsons into PdfDocTemplate (#539)
- Fixed bullets not exported into json when calling extract-data (#496)
- Fixed artifact_update config processing when "artifact" value is set or not (#535)
- Fixed method PdfDocTemplate.SetDefaults does not clean the config (#534)
- Fixed document being held after closing in .net (#532)
- Fixed getting the font name from PdeObject (#531)
- Fixed PDF version update to minimum 1.4 when adding tags into the document (#502)
- Fixed missing form field appearance after updating the field value (#511)
- Fixed creation of form field appearance shared with multiple form fields (#503)
- Fixed BBox calculation in SetAppearanceFromXObject when XObejct is form (#497)
- Fixed handling zero default values in structures in .NET (#492)
- Fixed document template config merge after preflight (#485)
- Fixed conversion of launch action in PDF to HTML conversion (#482)

### Removed
- Removed PdfDoc.FlattenAnnots, use PdfPage.FlattenAnnot instead (#494)



## [6.9.0] - 2021-03-08
### Added
- Added support for converting partial content into HTML using object state flags (#477)
- Added form field event emitter upon register_widget (#476)
- Added python internal samples and OpenFromStream example (#472)

### Changed
- Changed python github examples (#469)

### Fixed
- Fixed content2json CLI example page number default value (#481)
- Fixed PDF to HTML JavaScript conversion of a form field with ' or " in the name (#475)
- Fixed targets for nuget packages (#474)
- Fixed Wasm sdk.CreateImage/Destroy memory leaks (#473)
- Fixed python interface methods with passed structure as parameter (#467)

## [6.8.0] - 2021-02-25
### Added
- Added mothods for creation of text object with font (#91)
- Added Java Maven sdk sample into github (#164)
- Added PdsText methods SetText, SplitAtChar, GetCharQuad (#91 #391 #388 #390 )
- Added PdeElement method GetQuad (#392)
- Added PdfDoc methods AcquireAction, AcquireViewDestination (#396 #454)
- Added Release methods to PdfAction and PdfViewDestination
- Added PdfPageObject method CopyTo, MoveTo, GetQuad (#399 #392)
- Added flags to save preflight config with comments and compressed (#406)
- Added PsSysFont class for handling system fonts (#409)
- Added progress control to the library (#415)
- Added PdfAnnot.IsMarkup method (#419)
- Added flag for render border of the page (#420)
- Added support to open document from custom stream (#422)
- Added method PdsPath.ArcTo (#427)
- Added support for comb property of the widget conversion to HTML (#431)
- Added PdfBookmark methods SetAction, GetAppearance, SetAppearance (#439 #442)
- Added methods for creating of PdfActions (#440)
- Added parameter to extract text style of the text element in extract-data CLI command (#444)
- Added method for creating PdfViewDestination (#446)
- Added Remove method to the PdfBookmark class (#447)
- Added GetGenId method to the PdsObject (#452)
- Added SetTitle method to PdfBookmark interface (#453 #455)
- Added kInsertAfterLast & kInsertBeforFirst constants (#459)

### Changed
- Changed PdsContent interfaces, to create objects at specified index (#402)
- Changed output in the extract highlighted text command to application output and add line breaks (#430)
- Changed PdfBookmark.AddNewChild method with 'index' input parameter specifying the position of the bookmark (#459)

### Fixed
- Fixed PdfDoc.SetInfo when updating document author (#413)
- Fixed PdfToHtml saving style and script nodes outside the html node (#421)
- Fixed PdfDocTemplate.SetDefaults method to properly cleanup config (#423)
- Fixed object positioning in html (#429)
- Fixed PDF to HTML conversion of a form field name or values containing ' or " (#436)
- Fixed performance of the AcquireStructElement methods (#437)
- Fixed save file performance (#443)
- Fixed merging preflight with the current template (#449)
- Fixed performace issues in MacOS and Linux (#448)

## [6.7.0] - 2021-01-14
### Fixed
- Fixed page object caching in PdfDocTemplate while running preflight (#412)

## [6.6.0] - 2021-01-13
### Added
- Added objects PdfColorSpace, PdfColor for color space manipulation (#343)
- Added $if statement evaluation for the configuration query (#355)
- Added methods PdsText.GetNumChars, GetCharText, GetCharBBox, GetCharAdvanceWidth, GetTextMatrix (#364)
- Added methods PdePageMap.GetNumArtifacts, GetArtifact to extract artifacts for the page map (#384)
- Added methods PdfBookmark.AddNewChild, GetObject (#365, #374)
- Added methods PdfFormField.NotifyWillChange, NotifyDidChange (#385)
- Added method PdfDoc.FlattenAnnot (#388)
- Added methods PdsPageObject.GetStateFlag/SetStateFlag, PdeElement::GetStateFlag/SetStateFlag (#407)
- Added method PdsArray.PutString (#410)

### Fixed
- Fixed form xobject redaction (#316)
- Fixed license activation check exception during initializing (#331)
- Fixed linking of libstdc++ to support older linux distributions (#360)
- Fixed page cache handling after page insertion (#361)
- Fixed rendering of text elements after conversion to html (#367)

### Removed
- Removed method PdeElement.SetRender (#407)

## [6.5.0] - 2020-12-07
### Added
- Added support for creating PdsPath and PdsImage objects PdsContent (#89 #90 #118)
- Added method PdsPageObject.SetGState (#115)
- Added method PdfAnnot.IsValid()
- Added word spacing detection thresholds into the configuration template (#302)
- Added support for "pde_element" and "pde_object" type in the configuration template (#299)
- Added no_label option into configuration template (#298)
- Added CLI option --page-annots support to extract-data command (#327)
- Added support for password protected documents for CLI commands bmk2json, pages2json, dests2json (#323)
- Added graphic state and text state extraction to extract-data CLI command (#312)

### Changed
- Changed vertical splitters detection for words (#308) 
- Changed paragraphs detection to allow joining lines with different font size (#297)

### Fixed
- Fixed generating random id for PdsStructElement on CentOS7 (#332)
- Fixed image margin in pdf to html responsive layout (#320)
- Fixed colon text spliter position (#304)

## [6.4.1] - 2020-11-24
### Fixed
- Fixed initialization of Pdfix on windows when running under php/jvm (#319)

## [6.4.0] - 2020-11-16
### Fixed
- Fixed initialization on linux when running under php/jvm (#292)
- Fixed PdsStructElement::SetTitle does not modify the element title (#293)
- Fixed a bug in filling words detection (#295)
- Fixed extract-data CLI command saving PageMapData into "page_map" node (#303)

## [6.3.0] - 2020-11-11
### Added
- Added get primary font method for PdeWord this info instead of word max font (#272)
- Added text_line_join_distance threshold into the template JSON (#277)
- Added CLI --password parameter to the command line to support password protected files (#281)
- Added pdf open exception for password protected documents kErrorPdfInvalidPassword, kErrorPdfEncryptionFilter	(#282)

### Changed
- Updated PDF to HTML to export form field registration JavaScript even if --export-js flag is not set (#279)

### Fixed
- Fixed fail when splitting text during the page map recognition (#278)

## [6.2.0] - 2020-11-05
### Added
- Added option to prefere rows in reading order detection (#271)
- Added word splitters to split columns (#240)
- Added template threshold for object label detection (#256)
- Added template threshold for word label detection (#257)
- Added method PdfPageMap::GetPage (#251)
- Added method PdeElement::GetPageMap (#250)
- Added methods for PdsStructElement::SetID, GetLang, SetLang SetActualText (#243, #244, #245)
- Added redact CLI command and samples (#190)
- Added template word slitters for column detection (#240)
- Added extract-data CLI command and samples (#167)

### Fixed
- Fixed PdePageMap::GetBBox method interface (#250)
- Fixed PdfBookmark::GetNumChildren fail then bookmark has no kids (#273)
- Fixed fail in detection of PdeList when wmpty string is present (#269)
- Fixed fail when creating PdfAction (#253, #254)
- Fixed underline detection and comparison of wrong coordinates (#209)
- Fixed wrong naming in pdf_config.json, rename elements_values node to elements node (#219)
- Fixed support for float values in PdfDocTemplate "bbox" property (#238)
- Fixed pdfix_app pdf2txt does not support -1 as a default value for -p parameter (#239)

### Removed
- Removed method PdfDoc::CreateFormFromObject (#255)

## [6.1.1] - 2020-10-16
### Fixed
- Fixed crashes when processing pdf with the PDFix SDK Basic license (#197)
- Fixed licensing management fail to identify Windows system home directory in PHP application (#193)

## [6.1.0] - 2020-10-02
### Added
- Document template preflight for headers and footers (#30)
- Document template preflight for headings (#50)
- (CLI) Use preflight option in CLI commands make-accessible, add-tags, pdf2html – responsive (#127)

### Changed
- Merge text objects with the same text state into single BT/ET in content writer (#130)
- Rename classes PdfDocPreflight to PdfDocTemplate, PdfPagePreflight to PdfPageTemplate
- Rename method PdfDoc.GetDocTemplate to PdfDoc.GetTemplate (#154)
- PdfDocTemplage.AddPage methods extended cancel proc callback paramater

### Fixed
- Duplicated “/Type /XRef” key in a cross-reference entry when saving the document (#121)
- Bad Font /BBox when opening this output file in PdfDoc.MakeAccessible (#123)

## [6.0.0] - 2020-09-22
PDFix SDK now supports Redaction, low-level object editing, Unicode support for
form filling, and page manipulation support.  This release improves the logical
content extraction and tagging using a document preflight, which automatically
identifies headers, footers, and headings. Redesigned table, and list
detection, reading order detection. Better control using the configuration file
allows per-template adjustments to generate better results.  
PDFix SDK Integration is now possible using a NuGet package listed on nuget.org with the
support of .NET Framework and .NET Core for Windows operating systems.

### Added
- PdfDocTemplate preflight
- PdfDoc.ApplyRedaction
- Class PdsContent, method PdfPage.GetContent
- PdfAnnot.GetAppearanceXObject
- PdfArray.Put, PdfDictionary.Add
- PdfAnnot notifications WillChange / DidChange
- PdeText.GetText
- PdfPage.SetRotate
- PdfDoc.Save added kSaveUncompressed, kSaveCompressedStructureOnly flags
- PdfDoc.InserPages, DeletePage, CreatePage
- (CLI) Document template preflight for headers and footers (#30)

### Changed 
- Renamed method PdfPage.AddTextAnnot
- Error codes update
- Form filling unicode support
- Bullets and labels detection
- Template configuration update
- Reading order detection update

### Fixed
- PdfDoc.GetObjectById

## [5.8.0] - 2020-09-14
### Added
- PdsCotnent class
- PdsPath, PdsImage, PdsText, PdsPathPoint
- PdfPage.GetContent
- PdfAnnot.GetAppearanceXObject
- PdsArray.PutNumber
- PdsArray.PutName
- PdsArray.InsertArray
- PdsDictionary.InsertArray

### Changed
- PdfPage.AddTextAddAnnot renamed to AddNewTextAddAnnot

### Fixed
- PdfDoc.FlatenAnnots - flattening widget annotation (dropdown arrow)

## [5.7.0] - 2020-08-23
### Added
- PdfDoc.ApplyRedaction
- PdfAnnot.NotifyWillChange
- PdfAnnot.NotifyDidChange

### Fixed
- PdfDoc.FlatenAnnots - flattening markup annot makes document unreadable

## [5.6.4] - 2020-08-4
### Added
- PdfPage.SetRotate

### Changed
- PdfPage.AddAnnot was renamed to AddNewAnnot
- PdfPage.AddLinkAnnot was renamed to AddNewLinkAnnot
- PdfPage.AddTextAnnot was renamed to AddNewTextAnnot
- PdfPage.AddTextMarkupAnnot was renamed to AddNewTextMarkupAnnot
- PdePageMap table and reading order detection update

### Fixed
- PdfFormField.SetValue - appearance not created when filling-in the form with non-asci characters
- PdfDoc.GetObjectById returns nullptr for existing object

## [5.6.0] - 2020-06-20
### Added
- PdfDoc.CreateXObjectFromImage
- PdfAnnot.SetAppearanceFromXObject
- PdfDocTemplate.SavePreflightToStream

### Changed
- PdfDoc.AddWatermark

### Fixed
- Performance and stability improvements

## [5.5.3] - 2020-06-03
### Fixed
- Form field appearance not created correctly when filling-in the form on Windows OS

## [5.5.2] - 2020-05-29
### Fixed
- PdfDoc.Save flags kSaveUncompressed, kSaveCompressedStructureOnly

## [5.5.1] - 2020-05-28
### Added
- PdfDoc.GetTrailerObject api method
- PdfDoc.Save flags kSaveUncompressed, kSaveCompressedStructureOnly

### Changed
- Extended configuration options for extraction and tagging

### Fixed
- Form field appearance not created when filling-in the form
- Setting PDF Producer in metadata
- Performance and stability improvements

## [5.0.44] - 2020-03-15
### Changed
- PdfDoc.AddWatermarkFromImage - fixed z-order placement

### Fixed
- Stability improvements

## [5.0.40] - 2019-12-13
### Fixed
- URI Link conversion fix

## [5.0.39] - 2019-11-22
### Fixed
- PdfPage.FlattenFormXObjects

## [5.0.36] - 2020-10-10
### Changed
- PdfAccessibleParams - create_bookmarks parameter to control bokmark creation in MakeAccessible method
- PdfDoc.AddTags -Images tagged by default with an AltText "Figure" unless defined by the config file
- PdfDoc.AddTags - Tables tagged with table headers by default

### Fixed
- AcroForm SubmitForm method

## [5.0.34] - 2020-03-15
### Fixed
- Stability and memory management improvements.

## [5.0.0] - 2019-06-06
The major release focused on accessibility, PDF/UA compliance and custom configurations.
A new PDFix SDK Enterprise version brings the ability to customize layout detection, data extraction, and tagging.
New functions allow developers to programmatically create content structure (PdsStructTree, PdsStructElement) and 
also manipulate and edit existing structure elements, marked content, properties, and attributes.
With manual adjustments, you will have full control over the process of creating PDF/UA compliant files.
The automated data extraction process is now fully customizable via the configuration file. 
In addition to the general set of thresholds, a developer can use special query language to dramatically improve the quality of data extraction.
These two major features in combination can streamline your remediation workflows.

### Added
- Pdfix.RegisterPlugin, GetPluginByName,  GetEvent
- PdfixPlugin.GetPdfixVersionMajor, GetPdfixVersionMinor, GetPdfixVersionPatch
- PsEvent.GetType, GetDoc, GetPage, GetAnnot
- PdsStructTree.GetObject, RemoveKid, CreateStructElement, GetDoc, UpdateParentTree
- PdsStructElement.SetAlt, AddAttrObj, RemoveAttrObj, RemoveKid, CreateStructElement, SetParent, AddPageObject, AddAnnot, GetStructTree, SetType
- PdfPageView.Release
- PdePageMap.Release, AcquireElements, CreateElement,  AddTags
- PdfPage.Release, GetLogicalRotate, CreatePageMap, GetNumPageObjects, GetPageObject, GetResources, GetObject, FlattenFormXObjects, GetContentFlags, SetContent, GetDoc
- PdfDocTemplate.GetProperty, SetProperty, GetRegex, SetRegex
- PdfDoc.RemoveTags, CreateDictObject, CreateArrayObject, CreateNameObject, CreateStringObject, CreateIntObject, CreateNumberObject, CreateStreamObject, GetObjectById, CreateStructTree, RemoveStructTree, RemoveBookmarks, CreateBookmarks, AddFontMissingUnicode
- PdfAnnot.GetStructObject
- PdfAction.GetDestPageNum
- PdeText.GetTextFlags, GetLabelLevel, SetLabelLevel
- PdeTextLine.GetTextLineFlags
- PdeWord.GetWordFlags
- PdeElement.SetBBox, SetRender, SetData, GetData, SetAlt, SetActualText, GetFlags, SetFlags, PdsContentMark, GetNumTags, GetTagName, GetTagObject, GetTagMcid, GetTagArtifact, AddTag, RemoveTag
- PdsForm.GetNumPageObjects, GetPageObject
- PdsText.GetTextState
- PdsPageObject.GetId, SetRender, GetStructObject, GetContentMark, GetPage
- PdsStream.IsEof, GetSize, Read, GetPos
- PdsDictionary.Put, GetDictionary, GetArray, GetStream, GetString, GetText, GetNumber, GetInteger, GetBoolean
- PdsArray.Put, Insert, GetDictionary, GetArray, GetStream, GetString, GetText, GetNumber, GetInteger
- PdsName.GetText, 
- PdsString.GetText
- PdsObject.GetId
- (OCR) OcrTesseract.SetDataPath, SetEngine
- (OCR) TesseractDoc.OcrImageToPage

### Changed
- PdsStructElement.GetType, PdsStructElement.GetID
- PdfDoc.GetRootObject, PdfDoc.GetInfoObject

### Removed
- Pdfix.SetRegex
- PdsStructTree.ReleaseStructElement
- PdfPage.ReleasePageMap, PdfPage.ReleasePageView, PdfPage.GetNumMcidPageObjects, PdfPage.GetMcidPageObject
- PdfDoc.ReleasePage, PdfPage.RemoveStructTree
- PdeTextLine.GetFlags
- PdeWord.GetFlags
- PdeElement.SetRenderMode
- PdsReference.GetObjectNumber
- (OCR) OcrTesseract.SetData
- (OCR) TesseractDoc.Save

## [4.1.0] - 2018-10-03
### Added
- PdsObject - access to PDF low level objects
- PdsStructTree - access to PDF document structure tree (Tags)
- PDF to XML conversion
- PdfDocTemplate.kTrDetectRotation - automatic detection of page rotation flag
- PdfDocTemplate.kMinCharClipRatio - clipping area intersection threshold
- PdfDocTemplate.kTrMaxLineSpacing - maximum line spacing in paragraph threshold
- (HTML) Text decoration under text markup annotations (highlight, underline, cross-out, squiggly)

### Changed 
- PdfDoc.GetInfo returns empty string if Info dict not present
- PdfPage.GetMediaBox returns bounding box 0,0,612,792 if not present
- PdeContentWriter - content stream optimization for TJ and Tj operators
- PdeContentWriter - type3 font support
- PdeContentWriter - inline image support
- PdfFlattenAnnotsParams - flat_annot member to select annotation type to flatten
- PdfPageMap - applied kTextFlagStrikeout flag on text when Cross-Out annotation is in place
- PdfPageMap - text outside of clip area treated as artifact
- PdfPageMap - split filling words into separate PdeTexts
- AddTags - set generic Form Field tooltip when missing TU key
- AddTags - extra spaces in text handling
- Metadata support of in dc:title update
- ErrorCode renamed kErrorPdfCosObjInvalid to kErrorPdsObjectInvalid
- Xref stream support when saving files
- (HTML) changed < input > defaultValue property to data-default-value

### Fixed
- (HTML) .pdf-page h1 h2 h3 h4 to .pdf-page h1, ,pdf-page h2, … to apply style on .pdf-page only, same with .pdf-page.responsive table h1 .. h4
- (HTML) < input > maxLength property – missing quotes
- (HTML) CSS & HTML validation fixes
- (HTML) Unwanted “)” in html output
- (HTML) PdfToHtmlDoc.SaveDocHtml, PdfToHtmlDoc.SavePageHtml memory allocation fix
- (HTML) Textarea CSS - scrollbar was missing in case of long text

### Removed
- kTemplateFlatAnnots - use flat_annot in PdfFlattenAnnotsParams instead
- kTrLineSpacingTextSplit - use kTrMaxLineSpacing instead
- kTrLineSpacing - use kTrMaxLineSpacing instead
- kTemplateAcceptTags
- (HTML) Removed css white-space: -pre-wrap, -o-pre-wrap, -moz-pre-wrap as unsupported properties

## [4.0.5] - 2018-08-20
### Fixed
- Text tagging fix
- Text content writer fix

## [4.0.1] - 2018-06-20
### Changed 
- Updated c# wrapper
- Stability improvements
- New sample on Github for c# 
- Font subsetting update
- (OCR) OcrTesseract.SetLanguage parameters update

### Fixed
- Table recognition fix

## [4.0.0] - 2018-05-07
### Added
- Make PDF Accessible - allows you to convert PDF to PDF/UA
- EmbedFonts - allows you to embed/subset fonts in PDF document
- (OCR) OCR module - allows you to convert scanned PDF into searchable PDF

### Changed 
- Github repository samples
- Online documentation
- Trial key authorization update
- PdfixPlugin.GetID was removed
- PsImage.Save renamed to SaveToStream, new PsImage.Save()
- PsMetadata object
- PdfDoc.SetLang, PdfDoc.GetLang
- Read/write document metadata (title, author, creator, description) and sync. with Info dict
- PdfDoc.GetMetadata,
- PdsStructElement renamed to PdfStructElement

### Fixed
- File size issue after saving file
- Incremental save fix
- Digital signature fix
- Content writer - double, float value format - no exponent
- PdePageMap android crash fix
- (HTML) Link annotations with URI action in a fixed view

## [3.2.5] - 2018-08-01
### Changed
- (HTML) Changed defaultValue property to data-default-value in input element

### Fixed
- (HTML) Bug fixes in PDF to HTML conversion
- (HTML) css .pdf-page h1 h2 h3 h4 to .pdf-page h1, ,pdf-page h2, … not to apply style outside .pdf-page (same with .pdf-page.responsive table h1 .. h4)
- (HTML) Missing quotes in maxLength property in input element

### Removed
- (HTML) css properties white-space: -pre-wrap, -o-pre-wrap, -moz-pre-wrap

## [3.2.4] - 2018-05-18
### Changed
- PdfFormField.GetFontName returns user friendly font name

### Fixed
- (HTML) Form field font style support (font family, size)
- (HTML) Form field NoScroll flag support for textarea
- (HTML) Form field MaxLen support

## [3.2.3] - 2018-05-08
### Added
- Thread-safe support for jni interface

## [3.2.2] - 2018-02-22
### Changed
- Ability to reset previously modified Document templates
- PdePageMap bullet detection
- PdePageMap rotated text handling
- (CLI) Support for relative path names for input and output files

### Fixed
- (HTML) Table column alignment
- (HTML) Duplicate form field elements in fixed layout
- (HTML) Incorrect url data format in embedded image streams

## [3.2.0] - 2018-02-08
### Added
- (HTML) Support for JPEG image format and image quality
- (HTML) Simplified CSS in the output

### Changed
- Improved content extraction algorithms
- Tables, charts, bullets, lists, TOC, headers/footers recognition update
- Reading order detection improvements
- Customizable document templates
- Ability to configure content extraction and Autotag process for specific document type or document set

### Fixed
- (HTML) Table column alignment
- (HTML) Duplicate form field elements in fixed layout
- (HTML) Incorrect url data format in embedded image streams

## [3.0.0] - 2017-10-03
### Added
- PDF to PDF/UA conversion
- PdfDoc.MakeAccessible,  Make PDF accessible functionality
- PdfDoc.AddTags,  Add tags into PDF automatically

### Changed
- Streams support
- Improved Table detection
- Improved Paragraph recognition
- Improved List detection
- Table of contents detection
- Customizable document templates
- (HTML) New PDF to HTML conversions
- (HTML) PDF conversion to embeddable <div> html element
- (HTML) Embedded resources

### Fixed
- (HTML) Table column alignment
- (HTML) Duplicate form field elements in fixed layout
- (HTML) Incorrect url data format in embedded image streams

## [2.0.0] - 2017-02-15
### Changed
- More accurate elements detection
- Text Tables detection improvement
- Colspan and Rowspan bug fixies
- Text Paragraphs detection improvement
- Bullets recognition
- Repeated pattern detection (patterns of characters, such as a series of dots or dashes, between a tab and the following text)
- Background image separation
- Drop Cap text detection
- Form Field flattening
- (HTML) PDF to HTML conversion SDK released
- (HTML) Fixed or Responsive layout output
- (HTML) Multiple HTML files output or one continuous HTML page
- (HTML) TrueType Font Extraction
- (HTML) Text size output control
- (HTML) AcroForm support

## [1.0.2] - 2017-01-10
### Changed
- Text tables detection
- Lists and Table of contents detection
- Image intersection improvement
- Words detection improvement
- Elements clipping improvement
- Reading order detection improvement
- Header/Footer detection

## [1.0.1] - 2016-05-20
### Changed
- Discrete elements detection
- Text tables detection (output as an image)
- Table cell background color detection
- Words detection improvement
- Headers/Footers detection
- XForm object handling

## [1.0.0] - 2016-05-01
### Added
- Initial release
