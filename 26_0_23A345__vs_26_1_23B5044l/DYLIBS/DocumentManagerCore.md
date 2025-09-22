## DocumentManagerCore

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore`

```diff

-367.0.3.0.0
-  __TEXT.__text: 0x476cc
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x3ac8
+367.1.2.1.0
+  __TEXT.__text: 0x47b24
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_methlist: 0x3ad8
   __TEXT.__const: 0x6e8
-  __TEXT.__gcc_except_tab: 0x698
-  __TEXT.__cstring: 0x4e6a
+  __TEXT.__gcc_except_tab: 0x74c
+  __TEXT.__cstring: 0x4e8a
   __TEXT.__oslogstring: 0x3922
   __TEXT.__ustring: 0x10c
   __TEXT.__swift5_typeref: 0x438

   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x84
-  __TEXT.__unwind_info: 0x12c0
+  __TEXT.__unwind_info: 0x12d8
   __TEXT.__eh_frame: 0x2c0
   __TEXT.__objc_classname: 0x5bd
-  __TEXT.__objc_methname: 0x98bf
+  __TEXT.__objc_methname: 0x98e1
   __TEXT.__objc_methtype: 0xe48
-  __TEXT.__objc_stubs: 0x65c0
-  __DATA_CONST.__got: 0x5f0
-  __DATA_CONST.__const: 0x15e0
+  __TEXT.__objc_stubs: 0x65e0
+  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__const: 0x15d8
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2690
+  __DATA_CONST.__objc_selrefs: 0x26a0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x870
-  __AUTH_CONST.__const: 0xc20
-  __AUTH_CONST.__cfstring: 0x2f60
-  __AUTH_CONST.__objc_const: 0x6178
+  __AUTH_CONST.__auth_got: 0x880
+  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__cfstring: 0x2fa0
+  __AUTH_CONST.__objc_const: 0x6188
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x448

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D1372322-D03C-3115-9C60-86863F03CD81
-  Functions: 1834
-  Symbols:   5270
-  CStrings:  3096
+  UUID: F5F107C3-9A03-39D3-A921-D629A344BABA
+  Functions: 1835
+  Symbols:   5273
+  CStrings:  3102
 
Symbols:
+ +[DOCAXIdentifier pickerFilenameTextField]
+ _CFStringGetTypeID
+ __DS_CFURLGetPropertyForKey
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.6
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.6.cold.1
+ ___92+[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:]_block_invoke.4
+ ___92+[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:]_block_invoke.4.cold.1
+ ___block_descriptor_57_e8_32s40bs48r_e27_v24?0"NSURL"8"NSError"16lr48l8s40l8s32l8
+ __kCFURLIconEmojiKey
+ __kCFURLIconSymbolNameKey
+ _objc_msgSend$setEmoji:
+ _objc_msgSend$symbolName
- ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.8
- ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.8.cold.1
- ___92+[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:]_block_invoke.6
- ___92+[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:]_block_invoke.6.cold.1
- ___block_descriptor_49_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16ls40l8s32l8
- ___block_literal_global.5
- ___block_literal_global.7
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_DocumentManagerCore
- _objc_msgSend$fiNodeFromURL:
Functions:
~ -[FPItem(DOCNode) folderIcon] : 468 -> 884
~ +[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:] : 576 -> 800
~ ___92+[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:]_block_invoke : 92 -> 152
~ ___92+[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:]_block_invoke_2 : 108 -> 136
~ ___92+[DOCImportToDefaultLocationSupport _spi_importDocumentAtURL:synchronous:completionHandler:]_block_invoke.3 : 108 -> 136
+ +[DOCAXIdentifier pickerFilenameTextField]
~ +[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:] : 640 -> 860
~ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke : 92 -> 152
~ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke_2 : 108 -> 136
~ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.5 : 108 -> 136
CStrings:
+ "DOCPicker"
+ "filenameTextField"
+ "pickerFilenameTextField"
+ "setEmoji:"

```
