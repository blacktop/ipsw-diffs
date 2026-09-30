## DocumentManagerCore

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore`

```diff

-357.2.0.0.0
-  __TEXT.__text: 0x45690
+360.0.0.0.0
+  __TEXT.__text: 0x45a3c
   __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x39f0
+  __TEXT.__objc_methlist: 0x3a30
   __TEXT.__const: 0x708
-  __TEXT.__gcc_except_tab: 0x710
-  __TEXT.__cstring: 0x4aaa
-  __TEXT.__oslogstring: 0x38a2
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__cstring: 0x4b6a
+  __TEXT.__oslogstring: 0x3852
   __TEXT.__ustring: 0x10c
   __TEXT.__swift5_typeref: 0x3fc
   __TEXT.__constg_swiftt: 0xbc

   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x74
-  __TEXT.__unwind_info: 0x1160
+  __TEXT.__unwind_info: 0x1168
   __TEXT.__eh_frame: 0x2c0
   __TEXT.__objc_classname: 0x5bd
-  __TEXT.__objc_methname: 0x972a
-  __TEXT.__objc_methtype: 0xe28
-  __TEXT.__objc_stubs: 0x6500
-  __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__const: 0x1600
+  __TEXT.__objc_methname: 0x97a0
+  __TEXT.__objc_methtype: 0xe3d
+  __TEXT.__objc_stubs: 0x6560
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__const: 0x15e0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2620
+  __DATA_CONST.__objc_selrefs: 0x2640
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x870
-  __AUTH_CONST.__const: 0xb90
-  __AUTH_CONST.__cfstring: 0x2f20
-  __AUTH_CONST.__objc_const: 0x6098
+  __AUTH_CONST.__const: 0xbb0
+  __AUTH_CONST.__cfstring: 0x2f00
+  __AUTH_CONST.__objc_const: 0x60e0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x448
   __AUTH.__data: 0x130
   __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0xab0
-  __DATA.__bss: 0xe00
+  __DATA.__bss: 0xe10
   __DATA_DIRTY.__objc_data: 0xb18
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x108

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 727AFD8D-6E14-3B00-B70E-9DCE64F3B3AA
-  Functions: 1808
-  Symbols:   5249
-  CStrings:  3055
+  UUID: 290898D5-CC9A-30E3-9816-27C8345296D4
+  Functions: 1814
+  Symbols:   5257
+  CStrings:  3059
 
Symbols:
+ +[DOCFeature typeToFocusIsSupported]
+ +[DOCFeature typeToFocusIsSupported].cold.1
+ +[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]
+ -[FINode(DOCNode) dateAdded]
+ -[FPItem(DOCNode) dateAdded]
+ GCC_except_table134
+ GCC_except_table139
+ ___36+[DOCFeature typeToFocusIsSupported]_block_invoke
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.5
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.5.cold.1
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.8
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.8.cold.1
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke_2
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke_2.cold.1
+ ___block_literal_global.247
+ ___block_literal_global.7
+ _objc_msgSend$_spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:
+ _objc_msgSend$propertyAsDate:
+ _objc_msgSend$typeToFocus
+ _typeToFocusIsSupported.isSupported
+ _typeToFocusIsSupported.onceToken
- GCC_except_table132
- GCC_except_table137
- ___64+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:error:]_block_invoke.3
- ___64+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:error:]_block_invoke.3.cold.1
- ___64+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:error:]_block_invoke.cold.1
- ___76+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:completionHandler:]_block_invoke
- ___76+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:completionHandler:]_block_invoke.7
- ___76+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:completionHandler:]_block_invoke.7.cold.1
- ___76+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:completionHandler:]_block_invoke.cold.1
- ___block_literal_global.6
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_DocumentManagerCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DocumentManagerCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DocumentManagerCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DocumentManagerCore
CStrings:
+ "%@|"
+ "+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke"
+ "ERROR: Remote object renameDocumentAtURL: call returned bookmark data: %@ error: %@"
+ "Title for the action of sorting the items in the collection by the date the file was added to the device"
+ "Title for the action of sorting the items in the collection by the file creation date"
+ "Title for the action of sorting the items in the collection by the file modification date"
+ "_spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:"
+ "dateAdded"
+ "ipad_type_select"
+ "propertyAsDate:"
+ "typeToFocusIsSupported"
+ "v44@0:8@16@24B32@?36"
- "+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:completionHandler:]_block_invoke"
- "+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:error:]"
- "+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:error:]_block_invoke"
- "ERROR: Remote object renameDocumentAtURL: call retured bookmark data: %@ error: %@"
- "ERROR: Remote object renameDocumentAtURL: call retured bookmarkData: %@ error: %@"
- "emoji"
- "sym"

```
