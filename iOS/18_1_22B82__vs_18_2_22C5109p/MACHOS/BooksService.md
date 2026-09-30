## BooksService

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/BooksService.xpc/BooksService`

```diff

-110.6.0.0.0
-  __TEXT.__text: 0x13b8
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x680
-  __TEXT.__objc_methlist: 0x128
-  __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x5d9
-  __TEXT.__cstring: 0xef
-  __TEXT.__objc_classname: 0x8c
-  __TEXT.__objc_methtype: 0x268
-  __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__oslogstring: 0x4b
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x158
-  __DATA_CONST.__cfstring: 0x80
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x18
+112.2.1.0.0
+  __TEXT.__text: 0x42e8
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x5d8
+  __TEXT.__const: 0x60
+  __TEXT.__objc_methname: 0x138d
+  __TEXT.__cstring: 0x263
+  __TEXT.__objc_classname: 0x198
+  __TEXT.__objc_methtype: 0x56d
+  __TEXT.__oslogstring: 0x56
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x770
-  __DATA.__objc_selrefs: 0x1e0
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x120
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0x1710
+  __DATA.__objc_selrefs: 0x478
+  __DATA.__objc_ivar: 0xc8
+  __DATA.__objc_data: 0x3c0
+  __DATA.__data: 0x180
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary
   - /System/Library/PrivateFrameworks/Catalyst.framework/Catalyst
   - /System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 34
-  Symbols:   75
-  CStrings:  139
+  Functions: 123
+  Symbols:   128
+  CStrings:  366
 
Symbols:
+ _CFRelease
+ _CGBitmapContextCreateImage
+ _CGContextConcatCTM
+ _CGContextDrawPDFPage
+ _CGContextFillRect
+ _CGContextRelease
+ _CGContextScaleCTM
+ _CGContextSetRGBFillColor
+ _CGContextTranslateCTM
+ _CGImageRelease
+ _CGPDFDictionaryGetString
+ _CGPDFDocumentCreateWithURL
+ _CGPDFDocumentGetInfo
+ _CGPDFDocumentGetPage
+ _CGPDFPageGetBoxRect
+ _CGPDFPageGetDrawingTransform
+ _CGPDFStringCopyTextString
+ _CRKErrorWithCodeAndUserInfo
+ _NSStringFromCRKBookType
+ _OBJC_CLASS_$_BLLibrary
+ _OBJC_CLASS_$_CBSBLBookItem
+ _OBJC_CLASS_$_CBSOPFPackageContents
+ _OBJC_CLASS_$_CBSParseBookMetadataOperation
+ _OBJC_CLASS_$_CBSParseHTMLTableOfContentsOperation
+ _OBJC_CLASS_$_CBSParseNCXTableOfContentsOperation
+ _OBJC_CLASS_$_CBSParseOPFFilePathOperation
+ _OBJC_CLASS_$_CBSParseOPFPackageContentsOperation
+ _OBJC_CLASS_$_CBSParsePDFMetadataOperation
+ _OBJC_CLASS_$_CRKBook
+ _OBJC_CLASS_$_CRKChapter
+ _OBJC_CLASS_$_CRKCoreGraphicsUtilities
+ _OBJC_CLASS_$_CRKDevice
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSXMLParser
+ _OBJC_METACLASS_$_CBSBLBookItem
+ _OBJC_METACLASS_$_CBSOPFPackageContents
+ _OBJC_METACLASS_$_CBSParseBookMetadataOperation
+ _OBJC_METACLASS_$_CBSParseHTMLTableOfContentsOperation
+ _OBJC_METACLASS_$_CBSParseNCXTableOfContentsOperation
+ _OBJC_METACLASS_$_CBSParseOPFFilePathOperation
+ _OBJC_METACLASS_$_CBSParseOPFPackageContentsOperation
+ _OBJC_METACLASS_$_CBSParsePDFMetadataOperation
+ ___NSArray0__struct
+ __os_log_debug_impl
+ _objc_autorelease
+ _objc_opt_class
+ _objc_release_x23
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_setProperty_nonatomic_copy
- _OBJC_CLASS_$_CRKBLBookItem
- _OBJC_CLASS_$_CRKFetchBooksOperation
- _OBJC_CLASS_$_CRKFetchChaptersOperation
- _OBJC_CLASS_$_NSAssertionHandler
- __Block_object_dispose
- __Unwind_Resume
- ___objc_personality_v0
- __sl_dlopen
- _free
- _objc_getClass
- _objc_retainAutorelease
CStrings:
+ "\x02"
+ "\x05"
+ "\x06"
+ "\a"
+ "\b"
+ "\t"
+ "\x11"
+ "\x12"
+ "%!{(MISSING)public}@"
+ "@\"CBSOPFPackageContents\""
+ "@\"CRKBook\""
+ "@\"CRKChapter\""
+ "@\"NSData\"40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
+ "@\"NSMutableArray\""
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableString\""
+ "@\"NSString\""
+ "@\"NSXMLParser\""
+ "@24@0:8^{CGPDFDictionary=}16"
+ "@28@0:8@16B24"
+ "@32@0:8@16@24"
+ "@32@0:8@16^@24"
+ "@36@0:8@16@24B32"
+ "@40@0:8@16@24@32"
+ "Author"
+ "B"
+ "CBSBLBookItem"
+ "CBSOPFPackageContents"
+ "CBSParseBookMetadataOperation"
+ "CBSParseHTMLTableOfContentsOperation"
+ "CBSParseNCXTableOfContentsOperation"
+ "CBSParseOPFFilePathOperation"
+ "CBSParseOPFPackageContentsOperation"
+ "CBSParsePDFMetadataOperation"
+ "META-INF/container.xml"
+ "NSXMLParserDelegate"
+ "T@\"CRKBook\",R,N,V_book"
+ "T@\"NSMutableArray\",R,N,V_spineItemIdentifiers"
+ "T@\"NSMutableDictionary\",R,N,V_itemPathsByIdentifier"
+ "T@\"NSString\",C,N,V_author"
+ "T@\"NSString\",C,N,V_bookIdentifier"
+ "T@\"NSString\",C,N,V_bookIdentifierType"
+ "T@\"NSString\",C,N,V_coverImagePath"
+ "T@\"NSString\",C,N,V_identifier"
+ "T@\"NSString\",C,N,V_legacyUniqueIdentifier"
+ "T@\"NSString\",C,N,V_path"
+ "T@\"NSString\",C,N,V_storeIdentifier"
+ "T@\"NSString\",C,N,V_tableOfContentsFilePath"
+ "T@\"NSString\",C,N,V_tableOfContentsMediaType"
+ "T@\"NSString\",C,N,V_title"
+ "T@\"NSString\",R,N,V_filePath"
+ "TB,R,N,V_parseImage"
+ "Title"
+ "Title: %!@(MISSING)\nAuthor: %!@(MISSING)\nPath: %!@(MISSING)\nStore Identifier: %!@(MISSING)\n Identifier: %!@(MISSING)\nLegacy Identifier: %!@(MISSING)\nType: %!@(MISSING)"
+ "Tq,N,V_type"
+ "URLPathAllowedCharacterSet"
+ "URLWithString:"
+ "Untitled"
+ "_author"
+ "_book"
+ "_bookIdentifier"
+ "_bookIdentifierType"
+ "_coverImagePath"
+ "_filePath"
+ "_identifier"
+ "_itemPathsByIdentifier"
+ "_legacyUniqueIdentifier"
+ "_parseImage"
+ "_path"
+ "_spineItemIdentifiers"
+ "_storeIdentifier"
+ "_tableOfContentsFilePath"
+ "_tableOfContentsMediaType"
+ "_title"
+ "_type"
+ "a"
+ "abortParsing"
+ "appendString:"
+ "application/oebps-package+xml"
+ "application/x-dtbncx+xml"
+ "arrayByAddingObject:"
+ "book"
+ "bookIdentifier"
+ "bookIdentifierType"
+ "bundleForClass:"
+ "cfiWithItemIdentifier:fragment:"
+ "content"
+ "count"
+ "cover"
+ "coverImagePath"
+ "createImageContextForSize:"
+ "dataWithContentsOfFile:"
+ "dc:creator"
+ "dc:title"
+ "defaultManager"
+ "epubcfi(/6/%!@(MISSING)[%!@(MISSING)]!/4)"
+ "epubcfi(/6/%!@(MISSING)[%!@(MISSING)]!/4[%!@(MISSING)])"
+ "fileExistsAtPath:isDirectory:"
+ "fileName"
+ "filePath"
+ "fileURLWithPath:"
+ "finishOperation"
+ "finishOperation:"
+ "fragment"
+ "full-path"
+ "host"
+ "href"
+ "iTunesArtwork"
+ "ibooks://%!@(MISSING)/%!@(MISSING)"
+ "ibooks://%!@(MISSING)/%!@(MISSING)#%!@(MISSING)"
+ "ibooks://assetid/%!@(MISSING)"
+ "ibooks://filename/%!@(MISSING)"
+ "ibooks://storeid/%!@(MISSING)"
+ "id"
+ "identifierType"
+ "idref"
+ "image"
+ "imageDataFromImage:"
+ "includeImages"
+ "indexOfObject:"
+ "initWithBook:parseImage:"
+ "initWithBookFilePath:"
+ "initWithContentsOfURL:"
+ "initWithFilePath:packageContents:"
+ "initWithIdentifierType:identifier:"
+ "initWithOPFFilePath:identifierType:identifier:"
+ "initWithPDFBook:filePath:parseImage:"
+ "isEqualToString:"
+ "isExecuting"
+ "isValidWithError:"
+ "item"
+ "itemIdentifierForHref:fragment:"
+ "itemPathsByIdentifier"
+ "itemref"
+ "kCRKInvalidParameterErrorKey"
+ "lastObject"
+ "lastPathComponent"
+ "length"
+ "li"
+ "localizedStringForKey:value:table:"
+ "mBookFilePath"
+ "mBooks"
+ "mChapters"
+ "mContainerParser"
+ "mCoverItemID"
+ "mCurrentChapter"
+ "mCurrentElementName"
+ "mCurrentText"
+ "mHTMLFilePath"
+ "mHTMLParser"
+ "mIsInNav"
+ "mNCXFilePath"
+ "mNCXParser"
+ "mOPFFilePath"
+ "mOPFParser"
+ "mPackageContents"
+ "mParentChapters"
+ "mParseImage"
+ "media-type"
+ "meta"
+ "name"
+ "nav"
+ "navLabel"
+ "navPoint"
+ "ncx"
+ "numberWithInteger:"
+ "objectForKeyedSubscript:"
+ "parse"
+ "parseBookContentsOperationDidFinish:"
+ "parseBookMetadataOperationDidFail:"
+ "parseContentsFilePathOperationDidFinish:"
+ "parseImage"
+ "parseOFPPackageContentsOperationDidFinish:"
+ "parseOPFFilePathOperationDidFinish:"
+ "parsePDFMetadataOperationDidFail:"
+ "parseTableOfContentsOperationDidFinish:"
+ "parser:didEndElement:namespaceURI:qualifiedName:"
+ "parser:didEndMappingPrefix:"
+ "parser:didStartElement:namespaceURI:qualifiedName:attributes:"
+ "parser:didStartMappingPrefix:toURI:"
+ "parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:"
+ "parser:foundCDATA:"
+ "parser:foundCharacters:"
+ "parser:foundComment:"
+ "parser:foundElementDeclarationWithName:model:"
+ "parser:foundExternalEntityDeclarationWithName:publicID:systemID:"
+ "parser:foundIgnorableWhitespace:"
+ "parser:foundInternalEntityDeclarationWithName:value:"
+ "parser:foundNotationDeclarationWithName:publicID:systemID:"
+ "parser:foundProcessingInstructionWithTarget:data:"
+ "parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:"
+ "parser:parseErrorOccurred:"
+ "parser:resolveExternalEntityName:systemID:"
+ "parser:validationErrorOccurred:"
+ "parserDidEndDocument:"
+ "parserDidStartDocument:"
+ "q"
+ "q16@0:8"
+ "removeLastObject"
+ "removeObject:"
+ "rootfile"
+ "setBookIdentifier:"
+ "setBookIdentifierType:"
+ "setCoverImagePath:"
+ "setHasChapters:"
+ "setImage:"
+ "setObject:forKeyedSubscript:"
+ "setSubchapters:"
+ "setTableOfContentsFilePath:"
+ "setTableOfContentsMediaType:"
+ "setWebURL:"
+ "spineItemIdentifiers"
+ "src"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "stringByAppendingPathComponent:"
+ "stringByDeletingLastPathComponent"
+ "stringByDeletingPathExtension"
+ "stringByTrimmingCharactersInSet:"
+ "stringWithFormat:"
+ "subchapters"
+ "tableOfContentsFilePath"
+ "tableOfContentsMediaType"
+ "text"
+ "titleFromDictionaryRef:"
+ "updateAuthor:"
+ "updateTitle:"
+ "updateTitleWithDictionaryRef:"
+ "urlWithItemIdentifier:fragment:"
+ "v24@0:8@\"NSXMLParser\"16"
+ "v24@0:8^{CGPDFDictionary=}16"
+ "v24@0:8q16"
+ "v32@0:8@\"NSXMLParser\"16@\"NSData\"24"
+ "v32@0:8@\"NSXMLParser\"16@\"NSError\"24"
+ "v32@0:8@\"NSXMLParser\"16@\"NSString\"24"
+ "v32@0:8@16@24"
+ "v40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@16@24@32"
+ "v48@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@16@24@32@40"
+ "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
+ "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
+ "v56@0:8@16@24@32@40@48"
+ "webURL"
+ "whitespaceAndNewlineCharacterSet"
- "%!s(MISSING)"
- "@\"CRKFetchBooksOperation\""
- "@\"CRKFetchChaptersOperation\""
- "@\"NSMutableArray\"8@?0"
- "BLLibrary"
- "CRKDefaultBookLibraryProxy.h"
- "Class getBLLibraryClass(void)_block_invoke"
- "Unable to find class %!s(MISSING)"
- "cancel"
- "currentHandler"
- "handleFailureInFunction:file:lineNumber:description:"
- "initWithBookLibraryProxy:request:error:"
- "initWithRequest:error:"
- "internalFetchOperationDidFinish:"
- "mInternalFetchOperation"
- "softlink:r:path:/System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary"
- "stringWithUTF8String:"
- "void *BookLibraryLibrary(void)"

```
