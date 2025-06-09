## vCard

> `/System/Library/PrivateFrameworks/vCard.framework/vCard`

```diff

-3770.600.1.0.0
-  __TEXT.__text: 0x238f4
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x39e8
+3793.100.1.0.0
+  __TEXT.__text: 0x24810
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x3a48
   __TEXT.__const: 0x1c4
-  __TEXT.__cstring: 0x1c65
-  __TEXT.__oslogstring: 0x51e
+  __TEXT.__cstring: 0x1c15
+  __TEXT.__oslogstring: 0x423
   __TEXT.__ustring: 0x8
-  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__gcc_except_tab: 0x1f4
+  __TEXT.__dlopen_cstrs: 0x171
   __TEXT.__constg_swiftt: 0x14c
   __TEXT.__swift5_typeref: 0x6c
   __TEXT.__swift5_fieldmd: 0x74

   __TEXT.__swift5_reflstr: 0x1e
   __TEXT.__unwind_info: 0xab8
   __TEXT.__objc_classname: 0x8b9
-  __TEXT.__objc_methname: 0x720c
+  __TEXT.__objc_methname: 0x7307
   __TEXT.__objc_methtype: 0xe12
-  __TEXT.__objc_stubs: 0x6280
-  __DATA_CONST.__got: 0x420
-  __DATA_CONST.__const: 0xd98
+  __TEXT.__objc_stubs: 0x62e0
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0xe20
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ee0
+  __DATA_CONST.__objc_selrefs: 0x1f10
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0x6700
+  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x34e0
+  __AUTH_CONST.__objc_const: 0x6788
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_ivar: 0x348
+  __DATA.__objc_ivar: 0x350
   __DATA.__data: 0x580
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x198
   __DATA_DIRTY.__objc_data: 0x1bf8
-  __DATA_DIRTY.__data: 0x130
+  __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 31D04562-6183-3E4F-98EA-CF7BEF4C67B0
-  Functions: 1192
-  Symbols:   4575
-  CStrings:  2519
+  UUID: 3AAD8177-A8D5-3C79-BF2F-4F64E6D5C372
+  Functions: 1191
+  Symbols:   4569
+  CStrings:  2535
 
Symbols:
+ +[CNVCardImage sizeOfImageData:].cold.1
+ +[CNVCardImage sizeOfImageData:].cold.2
+ +[CNVCardImage sizeOfImageData:].cold.3
+ +[CNVCardImage sizeOfImageData:].cold.4
+ +[CNVCardMutableImage CGImageCreateWithData:maxSizeValue:].cold.1
+ +[CNVCardMutableImage CGImageCreateWithData:maxSizeValue:].cold.2
+ +[CNVCardMutableImage CGImageCreateWithData:maxSizeValue:].cold.3
+ +[CNVCardMutableImage CGImageCreateWithData:maxSizeValue:].cold.4
+ +[CNVCardMutableImage CGImageCreateWithData:maxSizeValue:].cold.5
+ -[CGImageRefWithFormat dealloc]
+ -[CNVCard30CardBuilder addPosterIdentifier]
+ -[CNVCardFilteredPerson posterIdentifier]
+ -[CNVCardMutableImage nts_initCGImage].cold.1
+ -[CNVCardMutableImage nts_initCGImage].cold.2
+ -[CNVCardMutableImage renderCGImage:].cold.1
+ -[CNVCardMutableImage renderCGImage:].cold.2
+ -[CNVCardParser parse_VND_63_POSTER_IDENTIFIER]
+ -[CNVCardPerson posterIdentifier]
+ -[CNVCardPerson setPosterIdentifier:]
+ -[CNVCardWritingOptions includePosterIdentifiers]
+ -[CNVCardWritingOptions setIncludePosterIdentifiers:]
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table16
+ GCC_except_table21
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table34
+ GCC_except_table8
+ _CFRetain
+ _CNVCardKeyPosterIdentifier
+ _CoreGraphicsLibrary
+ _CoreGraphicsLibraryCore.frameworkLibrary
+ _CoreImageLibrary
+ _CoreImageLibraryCore.frameworkLibrary
+ _CoreServicesLibrary
+ _CoreServicesLibraryCore.frameworkLibrary
+ _ImageIOLibrary
+ _ImageIOLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_CNVCardPerson._posterIdentifier
+ _OBJC_IVAR_$_CNVCardWritingOptions._includePosterIdentifiers
+ __OBJC_$_PROP_LIST_CNVCardPerson.348
+ ___38-[CNVCardMutableImage hasAlphaChannel]_block_invoke.cold.1
+ ___39-[CNVCardMutableImage isSourceLossless]_block_invoke.cold.1
+ ___39-[CNVCardMutableImage isSourceLossless]_block_invoke.cold.2
+ ___CoreGraphicsLibraryCore_block_invoke
+ ___CoreImageLibraryCore_block_invoke
+ ___CoreServicesLibraryCore_block_invoke
+ ___ImageIOLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.193
+ ___block_literal_global.225
+ ___block_literal_global.393
+ ___block_literal_global.402
+ ___block_literal_global.453
+ ___block_literal_global.456
+ ___block_literal_global.459
+ ___block_literal_global.462
+ ___getCGImageGetAlphaInfoSymbolLoc_block_invoke
+ ___getCGImageGetHeightSymbolLoc_block_invoke
+ ___getCGImageGetWidthSymbolLoc_block_invoke
+ ___getCGImageSourceCopyPropertiesAtIndexSymbolLoc_block_invoke
+ ___getCGImageSourceCreateThumbnailAtIndexSymbolLoc_block_invoke
+ ___getCGImageSourceCreateWithDataSymbolLoc_block_invoke
+ ___getCGImageSourceGetTypeSymbolLoc_block_invoke
+ ___getCIContextClass_block_invoke
+ ___getCIContextClass_block_invoke.cold.1
+ ___getCIImageClass_block_invoke
+ ___getCIImageClass_block_invoke.cold.1
+ ___getUTTypeConformsToSymbolLoc_block_invoke
+ ___getkCGImageDestinationLossyCompressionQualitySymbolLoc_block_invoke
+ ___getkCGImagePropertyPixelHeightSymbolLoc_block_invoke
+ ___getkCGImagePropertyPixelWidthSymbolLoc_block_invoke
+ ___getkCGImageSourceCreateThumbnailFromImageAlwaysSymbolLoc_block_invoke
+ ___getkCGImageSourceThumbnailMaxPixelSizeSymbolLoc_block_invoke
+ ___getkCIFormatRGBA8SymbolLoc_block_invoke
+ ___getkUTTypeJPEGSymbolLoc_block_invoke
+ __sl_dlopen
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_vCard
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_vCard
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_vCard
+ _abort_report_np
+ _audit_stringCoreGraphics
+ _audit_stringCoreImage
+ _audit_stringCoreServices
+ _audit_stringImageIO
+ _dlerror
+ _free
+ _getCGImageGetAlphaInfoSymbolLoc.ptr
+ _getCGImageGetHeightSymbolLoc.ptr
+ _getCGImageGetWidthSymbolLoc.ptr
+ _getCGImageSourceCopyPropertiesAtIndexSymbolLoc.ptr
+ _getCGImageSourceCreateThumbnailAtIndexSymbolLoc.ptr
+ _getCGImageSourceCreateWithDataSymbolLoc.ptr
+ _getCGImageSourceGetTypeSymbolLoc.ptr
+ _getCIContextClass.softClass
+ _getCIImageClass.softClass
+ _getUTTypeConformsToSymbolLoc.ptr
+ _getkCGImageDestinationLossyCompressionQualitySymbolLoc.ptr
+ _getkCGImagePropertyPixelHeightSymbolLoc.ptr
+ _getkCGImagePropertyPixelWidthSymbolLoc.ptr
+ _getkCGImageSourceCreateThumbnailFromImageAlwaysSymbolLoc.ptr
+ _getkCGImageSourceThumbnailMaxPixelSizeSymbolLoc.ptr
+ _getkCIFormatRGBA8SymbolLoc.ptr
+ _getkUTTypeJPEGSymbolLoc.ptr
+ _objc_msgSend$addPosterIdentifier
+ _objc_msgSend$includePosterIdentifiers
+ _objc_msgSend$posterIdentifier
- GCC_except_table11
- GCC_except_table20
- GCC_except_table25
- _CIContextFunction
- _CIImageFunction
- _LoadCoreImage.frameworkLibrary
- _LoadCoreImage.loadPredicate
- _LoadCoreServices.frameworkLibrary
- _LoadCoreServices.loadPredicate
- _LoadImageIO.frameworkLibrary
- _LoadImageIO.loadPredicate
- __OBJC_$_PROP_LIST_CNVCardPerson.343
- ___LoadCoreImage_block_invoke
- ___LoadCoreImage_block_invoke.cold.1
- ___LoadCoreServices_block_invoke
- ___LoadCoreServices_block_invoke.cold.1
- ___LoadImageIO_block_invoke
- ___LoadImageIO_block_invoke.cold.1
- ___block_literal_global.120
- ___block_literal_global.131
- ___block_literal_global.190
- ___block_literal_global.222
- ___block_literal_global.383
- ___block_literal_global.392
- ___block_literal_global.443
- ___block_literal_global.446
- ___block_literal_global.449
- ___block_literal_global.452
- ___error
- __os_log_default
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_vCard
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_vCard
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_vCard
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_vCard
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_vCard
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_vCard
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_vCard
- _classCIContext
- _classCIImage
- _constantkCGImageDestinationLossyCompressionQuality
- _constantkCGImagePropertyPixelHeight
- _constantkCGImagePropertyPixelWidth
- _constantkCGImageSourceCreateThumbnailFromImageAlways
- _constantkCGImageSourceThumbnailMaxPixelSize
- _constantkCIFormatRGBA8
- _constantkUTTypeJPEG
- _dlopen
- _getCIContextClass
- _getCIImageClass
- _getkCGImageDestinationLossyCompressionQuality
- _getkCGImagePropertyPixelHeight
- _getkCGImagePropertyPixelWidth
- _getkCGImageSourceCreateThumbnailFromImageAlways
- _getkCGImageSourceThumbnailMaxPixelSize
- _getkCIFormatRGBA8
- _getkUTTypeJPEG
- _initCGImageGetAlphaInfo
- _initCGImageGetAlphaInfo.cold.1
- _initCGImageGetHeight
- _initCGImageGetHeight.cold.1
- _initCGImageGetWidth
- _initCGImageGetWidth.cold.1
- _initCGImageSourceCopyPropertiesAtIndex
- _initCGImageSourceCopyPropertiesAtIndex.cold.1
- _initCGImageSourceCreateThumbnailAtIndex
- _initCGImageSourceCreateThumbnailAtIndex.cold.1
- _initCGImageSourceCreateWithData
- _initCGImageSourceCreateWithData.cold.1
- _initCGImageSourceGetType
- _initCGImageSourceGetType.cold.1
- _initCIContext
- _initCIContext.cold.1
- _initCIImage
- _initCIImage.cold.1
- _initUTTypeConformsTo
- _initUTTypeConformsTo.cold.1
- _initkCGImageDestinationLossyCompressionQuality
- _initkCGImageDestinationLossyCompressionQuality.cold.1
- _initkCGImagePropertyPixelHeight
- _initkCGImagePropertyPixelHeight.cold.1
- _initkCGImagePropertyPixelWidth
- _initkCGImagePropertyPixelWidth.cold.1
- _initkCGImageSourceCreateThumbnailFromImageAlways
- _initkCGImageSourceCreateThumbnailFromImageAlways.cold.1
- _initkCGImageSourceThumbnailMaxPixelSize
- _initkCGImageSourceThumbnailMaxPixelSize.cold.1
- _initkCIFormatRGBA8
- _initkCIFormatRGBA8.cold.1
- _initkUTTypeJPEG
- _initkUTTypeJPEG.cold.1
- _kCGImageDestinationLossyCompressionQualityFunction
- _kCGImagePropertyPixelHeightFunction
- _kCGImagePropertyPixelWidthFunction
- _kCGImageSourceCreateThumbnailFromImageAlwaysFunction
- _kCGImageSourceThumbnailMaxPixelSizeFunction
- _kCIFormatRGBA8Function
- _kUTTypeJPEGFunction
- _softLinkCGImageGetAlphaInfo
- _softLinkCGImageGetHeight
- _softLinkCGImageGetWidth
- _softLinkCGImageSourceCopyPropertiesAtIndex
- _softLinkCGImageSourceCreateThumbnailAtIndex
- _softLinkCGImageSourceCreateWithData
- _softLinkCGImageSourceGetType
- _softLinkUTTypeConformsTo
- _swift_release_n
- _swift_retain
CStrings:
+ "%s"
+ "T@\"NSString\",&,V_posterIdentifier"
+ "TB,V_includePosterIdentifiers"
+ "Unable to find class %s"
+ "VND-63-POSTER-IDENTIFIER"
+ "_includePosterIdentifiers"
+ "_posterIdentifier"
+ "addPosterIdentifier"
+ "includePosterIdentifiers"
+ "parse_VND_63_POSTER_IDENTIFIER"
+ "posterIdentifier"
+ "setIncludePosterIdentifiers:"
+ "setPosterIdentifier:"
+ "softlink:r:path:/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics"
+ "softlink:r:path:/System/Library/Frameworks/CoreImage.framework/CoreImage"
+ "softlink:r:path:/System/Library/Frameworks/CoreServices.framework/CoreServices"
+ "softlink:r:path:/System/Library/Frameworks/ImageIO.framework/ImageIO"
- "/System/Library/Frameworks/CoreImage.framework/CoreImage"
- "/System/Library/Frameworks/CoreServices.framework/CoreServices"
- "/System/Library/Frameworks/ImageIO.framework/ImageIO"
- "Failed to Soft Link: /System/Library/Frameworks/CoreImage.framework/CoreImage (%d)"
- "Failed to Soft Link: /System/Library/Frameworks/CoreServices.framework/CoreServices (%d)"
- "Failed to Soft Link: /System/Library/Frameworks/ImageIO.framework/ImageIO (%d)"

```
