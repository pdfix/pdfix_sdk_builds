# Changelog

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
