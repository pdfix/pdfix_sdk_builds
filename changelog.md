# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [6.1.0] - 2020-10-02
### Added
- Document template preflight for headers and footers (#30)
- Document template preflight for headings (#50)
- CLI: Use preflight option in CLI commands make-accessible, add-tags, pdf2html – responsive (#127)

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
- CLI: Document template preflight for headers and footers (#30)

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
