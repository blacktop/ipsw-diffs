## SpotlightUIShared

> `/System/Library/PrivateFrameworks/SpotlightUIShared.framework/Versions/A/SpotlightUIShared`

```diff

-120.3.2.0.0
-  __TEXT.__text: 0xdc8c
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x298
-  __TEXT.__const: 0xd68
-  __TEXT.__cstring: 0xae8
+120.4.6.0.0
+  __TEXT.__text: 0xe074
+  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__objc_methlist: 0x3dc
+  __TEXT.__const: 0xd78
+  __TEXT.__cstring: 0xaf8
   __TEXT.__ustring: 0x7d2
   __TEXT.__oslogstring: 0xa2
   __TEXT.__swift5_typeref: 0x6b0

   __TEXT.__swift5_fieldmd: 0x14c
   __TEXT.__swift5_proto: 0xb4
   __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift_as_entry: 0x60
+  __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_capture: 0xb0
-  __TEXT.__unwind_info: 0x600
-  __TEXT.__eh_frame: 0x7d4
+  __TEXT.__unwind_info: 0x620
+  __TEXT.__eh_frame: 0x878
   __TEXT.__objc_classname: 0xa9
-  __TEXT.__objc_methname: 0xfb8
+  __TEXT.__objc_methname: 0xfd7
   __TEXT.__objc_methtype: 0x23f
-  __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0x238
+  __TEXT.__objc_stubs: 0xf80
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c0
+  __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__auth_got: 0x610
   __AUTH_CONST.__const: 0x5f0
-  __AUTH_CONST.__cfstring: 0x440
-  __AUTH_CONST.__objc_const: 0x890
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0x650
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2d8
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x548
-  __DATA.__bss: 0x1748
+  __DATA.__data: 0x558
+  __DATA.__bss: 0x1758
   __DATA.__common: 0x98
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 113EE679-B2AC-387B-B7A5-C55658162FE5
-  Functions: 404
-  Symbols:   611
-  CStrings:  352
+  UUID: 928F419F-371A-34B9-A34A-7A21D1DAB7F8
+  Functions: 424
+  Symbols:   632
+  CStrings:  355
 
Symbols:
+ +[SUISRadarUtilities pathToSpotlightFiles].cold.1
+ +[SUISRadarUtilities searchResultCategoriesFilePath]
+ +[SUIUtilities visionResourcesQueue].cold.1
+ -[SUISpotlightController startQueryTaskWithSearchString:queryOptions:sourceResult:triggerEvent:languages:currentKeyboardLanguage:queryId:].cold.1
+ ___52+[SUISRadarUtilities searchResultCategoriesFilePath]_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.163
+ __block_literal_global.167
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_SpotlightUIShared
+ _objc_msgSend$searchResultCategoriesFilePath
+ searchResultCategoriesFilePath.onceToken
+ searchResultCategoriesFilePath.searchResultCategoriesFilePath
- __block_literal_global.49
- __block_literal_global.53
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_SpotlightUIShared
- _swift_bridgeObjectRelease_n
CStrings:
+ "SearchResultCategories.log"
+ "searchResultCategoriesFilePath"

```
