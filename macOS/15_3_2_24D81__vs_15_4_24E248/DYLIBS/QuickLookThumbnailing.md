## QuickLookThumbnailing

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/Versions/A/QuickLookThumbnailing`

```diff

-199.4.3.0.0
-  __TEXT.__text: 0x30d2c
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_methlist: 0x2a04
+199.5.3.0.0
+  __TEXT.__text: 0x30ca4
+  __TEXT.__auth_stubs: 0x1170
+  __TEXT.__objc_methlist: 0x2d48
   __TEXT.__const: 0x7ba
-  __TEXT.__cstring: 0x1ef4
-  __TEXT.__gcc_except_tab: 0x9fc
+  __TEXT.__cstring: 0x1e8d
+  __TEXT.__gcc_except_tab: 0xa04
   __TEXT.__oslogstring: 0x21b5
   __TEXT.__dlopen_cstrs: 0x9f
-  __TEXT.__swift5_typeref: 0x3c1
-  __TEXT.__swift5_capture: 0xe4
+  __TEXT.__swift5_typeref: 0x3b9
+  __TEXT.__swift5_capture: 0xd4
   __TEXT.__swift5_fieldmd: 0x1e8
   __TEXT.__constg_swiftt: 0x330
   __TEXT.__swift5_reflstr: 0x18a

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__unwind_info: 0xe58
-  __TEXT.__eh_frame: 0x418
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__unwind_info: 0xe88
+  __TEXT.__eh_frame: 0x408
   __TEXT.__objc_classname: 0x4b7
   __TEXT.__objc_methname: 0x7b5b
   __TEXT.__objc_methtype: 0x1257
   __TEXT.__objc_stubs: 0x4f60
   __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x420
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19a8
+  __DATA_CONST.__objc_selrefs: 0x1a78
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x8f0
-  __AUTH_CONST.__const: 0x14a0
+  __AUTH_CONST.__auth_got: 0x8c8
+  __AUTH_CONST.__const: 0x1450
   __AUTH_CONST.__cfstring: 0x1800
-  __AUTH_CONST.__objc_const: 0x5638
+  __AUTH_CONST.__objc_const: 0x5078
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x318
-  __DATA.__data: 0x668
+  __DATA.__data: 0x660
   __DATA.__bss: 0xa30
   __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0xa00

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B682A6DA-C42D-3E00-A515-17E255CDDF59
-  Functions: 1447
-  Symbols:   3247
-  CStrings:  2113
+  UUID: 9989B133-1E3D-31FC-929A-A99292222A1B
+  Functions: 1460
+  Symbols:   3259
+  CStrings:  2108
 
Symbols:
+ +[QLCacheFileProviderFileIdentifier knownFileProviderIdentifiersSoFar].cold.1
+ +[QLThumbnailAddition thumbnailsDictionaryForURL:error:].cold.2
+ +[QLThumbnailAddition thumbnailsDictionaryForURL:error:].cold.3
+ +[QLThumbnailConnectionHandler hostXPCInterface].cold.1
+ +[QLThumbnailConnectionHandler serviceXPCInterface].cold.1
+ +[QLThumbnailGenerationRequest customExtensionCommunicationEncodedClasses].cold.1
+ -[QLServiceThumbnailRenderer _thumbnailDataDestructionConcurrenQueue].cold.1
+ -[QLThumbnailAddition _initWithXattrsPresentOnURL:error:].cold.1
+ -[QLThumbnailRequestOperation sharedSerialResponseQueue].cold.1
+ -[QLThumbnailVersion initWithFileURL:generatorID:generatorVersion:].cold.3
+ GCC_except_table173
+ QLIconAutoDisplayExtension.cold.1
+ QLTCreateCGContext.cold.1
+ QLTCreateCGContext.cold.2
+ QLTCreateCGContext.cold.3
+ QLTCreateCGContextWithSize.cold.2
+ QLTCreateCGContextWithSize.cold.3
+ QLTCreateCGContextWithSize.cold.4
+ QLTImageClassWithError.cold.1
+ QLTInitLogging.cold.1
+ QLTPrefersExtendedRange.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ block_copy_helper.19
+ block_descriptor.21
+ block_destroy_helper.20
+ get_witness_table 21QuickLookThumbnailing18ThumbnailExtensionRzlAA0dE13Configuration33_E136596B361DD65834506CE1AB77646FLLCyxG0E10Foundation03AppeF0HPyHC.34
- GCC_except_table172
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_QuickLookThumbnailing
- _swift_bridgeObjectRelease_n
- _symbolic _____Sg 10Foundation3URLV
- block_copy_helper.20
- block_copy_helper.26
- block_descriptor.22
- block_descriptor.28
- block_destroy_helper.21
- block_destroy_helper.27
- get_witness_table 21QuickLookThumbnailing18ThumbnailExtensionRzlAA0dE13Configuration33_E136596B361DD65834506CE1AB77646FLLCyxG0E10Foundation03AppeF0HPyHC.41
CStrings:
+ "/System/AppleInternal/Library/Frameworks/AVFoundation.framework/AVFoundation"
+ "/System/AppleInternal/Library/Frameworks/FileProvider.framework/FileProvider"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Swift/IntegerTypes.swift"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"

```
