## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport`

```diff

-3864.200.33.2.2
-  __TEXT.__text: 0x18e84
+3864.200.63.0.0
+  __TEXT.__text: 0x18e74
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x17f0
-  __TEXT.__gcc_except_tab: 0x26b4
-  __TEXT.__cstring: 0x481e
-  __TEXT.__const: 0x37c
+  __TEXT.__gcc_except_tab: 0x26a8
+  __TEXT.__cstring: 0x483e
+  __TEXT.__const: 0x38c
   __TEXT.__oslogstring: 0x4a6
   __TEXT.__dlopen_cstrs: 0xd4
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x242
   __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_reflstr: 0xb2
-  __TEXT.__swift5_fieldmd: 0x8c
+  __TEXT.__swift5_reflstr: 0xc8
+  __TEXT.__swift5_fieldmd: 0x98
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x48
-  __TEXT.__unwind_info: 0xd50
+  __TEXT.__unwind_info: 0xd58
   __TEXT.__objc_classname: 0x650
-  __TEXT.__objc_methname: 0x5583
+  __TEXT.__objc_methname: 0x5584
   __TEXT.__objc_methtype: 0x865
-  __TEXT.__objc_stubs: 0x3880
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x1288
+  __TEXT.__objc_stubs: 0x3860
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0x1290
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1450
+  __DATA_CONST.__objc_selrefs: 0x1448
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x20

   __AUTH_CONST.__objc_const: 0x3fe0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1d0
+  __AUTH.__objc_data: 0x180
   __DATA.__objc_ivar: 0x1a4
-  __DATA.__data: 0x610
+  __DATA.__data: 0x5c8
   __DATA.__bss: 0x468
-  __DATA_DIRTY.__objc_data: 0xeb0
-  __DATA_DIRTY.__data: 0x168
+  __DATA_DIRTY.__objc_data: 0xf00
+  __DATA_DIRTY.__data: 0x1b0
   __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D181D742-97EB-36AD-9956-8DAADE535223
+  UUID: C420BCB3-156F-3A88-8410-3E8B1202C859
   Functions: 655
   Symbols:   3030
   CStrings:  2287
Symbols:
+ -[MSParsecSearchSession reportMessageResultsVisible:latencyMs:]
+ -[MSParsecSearchSession reportSuggestionsVisible:latencyMs:]
+ ___block_literal_global.34
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_MailSupport
+ _objc_msgSend$setInputToResultShownMs:
- -[MSParsecSearchSession reportMessageResultsVisible:]
- -[MSParsecSearchSession reportSuggestionsVisible:]
- _OBJC_CLASS_$_WKWebsiteDataStore
- ___block_literal_global.32
- _objc_msgSend$nonPersistentDataStore
- _objc_msgSend$setWebsiteDataStore:
Functions:
~ -[MSParsecSearchSession reportSuggestionsVisible:] -> -[MSParsecSearchSession reportSuggestionsVisible:latencyMs:] : 640 -> 720
~ -[MSParsecSearchSession reportMessageResultsVisible:] -> -[MSParsecSearchSession reportMessageResultsVisible:latencyMs:] : 164 -> 244
~ +[MSWebKitWebViewConfigurationFactory commonWebViewConfiguration] : 372 -> 332
~ sub_2572969c0 -> sub_257209a80 : 192 -> 220
~ sub_257296d50 -> sub_257209e2c : 192 -> 28
CStrings:
+ "IMAPSyncMoreMessages"
+ "reportMessageResultsVisible:latencyMs:"
+ "reportSuggestionsVisible:latencyMs:"
+ "setInputToResultShownMs:"
- "nonPersistentDataStore"
- "reportMessageResultsVisible:"
- "reportSuggestionsVisible:"
- "setWebsiteDataStore:"

```
