## SpotlightUIShared

> `/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared`

```diff

-163.1.0.0.0
-  __TEXT.__text: 0xa444c
-  __TEXT.__auth_stubs: 0x3060
-  __TEXT.__objc_methlist: 0x890
-  __TEXT.__const: 0x6a4c
-  __TEXT.__cstring: 0x2d58
+168.1.0.0.0
+  __TEXT.__text: 0xa64e8
+  __TEXT.__auth_stubs: 0x30d0
+  __TEXT.__objc_methlist: 0x8b8
+  __TEXT.__const: 0x6bfc
+  __TEXT.__cstring: 0x2df8
   __TEXT.__ustring: 0x7d2
-  __TEXT.__oslogstring: 0x79f
-  __TEXT.__swift5_typeref: 0x2d06
-  __TEXT.__swift5_reflstr: 0x12f5
-  __TEXT.__swift5_assocty: 0x7f0
-  __TEXT.__constg_swiftt: 0x2d2c
-  __TEXT.__swift5_fieldmd: 0x17d0
-  __TEXT.__swift5_proto: 0x560
-  __TEXT.__swift5_types: 0x264
-  __TEXT.__swift_as_entry: 0x4c8
-  __TEXT.__swift_as_ret: 0x440
+  __TEXT.__oslogstring: 0x82f
+  __TEXT.__swift5_typeref: 0x2d46
+  __TEXT.__swift5_reflstr: 0x1305
+  __TEXT.__swift5_assocty: 0x820
+  __TEXT.__constg_swiftt: 0x2d64
+  __TEXT.__swift5_fieldmd: 0x17ec
+  __TEXT.__swift5_proto: 0x578
+  __TEXT.__swift5_types: 0x268
+  __TEXT.__swift_as_entry: 0x4d0
+  __TEXT.__swift_as_ret: 0x448
   __TEXT.__swift5_protos: 0x84
-  __TEXT.__swift5_capture: 0x4dc
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3348
-  __TEXT.__eh_frame: 0x77a8
+  __TEXT.__swift5_capture: 0x4f0
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__unwind_info: 0x3370
+  __TEXT.__eh_frame: 0x7848
   __TEXT.__objc_classname: 0x1d6
-  __TEXT.__objc_methname: 0x2970
-  __TEXT.__objc_methtype: 0x402
-  __TEXT.__objc_stubs: 0x15c0
-  __DATA_CONST.__got: 0xc70
+  __TEXT.__objc_methname: 0x2b70
+  __TEXT.__objc_methtype: 0x414
+  __TEXT.__objc_stubs: 0x1780
+  __DATA_CONST.__got: 0xcd8
   __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe20
+  __DATA_CONST.__objc_selrefs: 0xee0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x1838
-  __AUTH_CONST.__const: 0x4318
+  __AUTH_CONST.__auth_got: 0x1870
+  __AUTH_CONST.__const: 0x43a8
   __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0x27e0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x11f0
   __AUTH.__data: 0x3010
   __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x1540
+  __DATA.__data: 0x15b0
   __DATA.__objc_stublist: 0x10
-  __DATA.__bss: 0xa258
+  __DATA.__bss: 0xa568
   __DATA.__common: 0x158
   __DATA_DIRTY.__objc_data: 0x158
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x490
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Combine.framework/Combine
+  - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ECFEBD96-18E9-3832-A7B6-E0334DC86386
-  Functions: 3688
-  Symbols:   2194
-  CStrings:  975
+  UUID: 014457B5-B4E6-3200-A48F-B4FF1293ABB7
+  Functions: 3714
+  Symbols:   2228
+  CStrings:  1005
 
Symbols:
+ +[SUISPasteboardManager collectExpiredItemsFromItems:expirationThresholdInSeconds:outputNextExpirationDate:]
+ +[SUISPasteboardManager collectExpiredItemsFromItems:expirationThresholdInSeconds:outputNextExpirationDate:].cold.1
+ -[SUISPasteboardManager _deleteExpiredItemsAndDispatchForNextExpiration:]
+ -[SUISPasteboardManager registerPasteboardExpirationWatchdog]
+ _NSTextCheckingCityKey
+ _NSTextCheckingCountryKey
+ _NSTextCheckingStateKey
+ _NSTextCheckingStreetKey
+ _NSTextCheckingZIPKey
+ _OBJC_CLASS_$_CNMutablePostalAddress
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDataDetector
+ _OBJC_CLASS_$_NSTextCheckingResult
+ ___108+[SUISPasteboardManager collectExpiredItemsFromItems:expirationThresholdInSeconds:outputNextExpirationDate:]_block_invoke
+ ___block_descriptor_32_e47_q24?0"CSSearchableItem"8"CSSearchableItem"16l
+ ___block_literal_global.134
+ _associated conformance So17NSTextCheckingKeyaSHSCSQ
+ _associated conformance So17NSTextCheckingKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So17NSTextCheckingKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_deleteExpiredItemsAndDispatchForNextExpiration:
+ _objc_msgSend$attachmentPaths
+ _objc_msgSend$attributeSet
+ _objc_msgSend$compare:
+ _objc_msgSend$containsString:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$isDate:equalToDate:toUnitGranularity:
+ _objc_msgSend$laterDate:
+ _objc_msgSend$now
+ _objc_msgSend$registerPasteboardExpirationWatchdog
+ _objc_msgSend$setItemIdentifiers:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _symbolic Sb14fromCollection_t
+ _symbolic Sny_____G SS5IndexV
+ _symbolic _____ So17NSTextCheckingKeya
+ _type_layout_string So17NSTextCheckingKeya
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SpotlightUIShared
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SpotlightUIShared
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SpotlightUIShared
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SpotlightUIShared
CStrings:
+ "@40@0:8@16d24^@32"
+ "Found expired items %lu, files %lu"
+ "Quiescing session pool and resigning focus if needed"
+ "URLWithString:"
+ "_deleteExpiredItemsAndDispatchForNextExpiration:"
+ "addressComponents"
+ "attachmentPaths"
+ "collectExpiredItemsFromItems:expirationThresholdInSeconds:outputNextExpirationDate:"
+ "compare:"
+ "components"
+ "containsString:"
+ "currentCalendar"
+ "dateByAddingTimeInterval:"
+ "initWithTypes:error:"
+ "isDate:equalToDate:toUnitGranularity:"
+ "laterDate:"
+ "matchesInString:options:range:"
+ "name"
+ "now"
+ "q24@?0@\"CSSearchableItem\"8@\"CSSearchableItem\"16"
+ "registerPasteboardExpirationWatchdog"
+ "setCity:"
+ "setCountry:"
+ "setItemIdentifiers:"
+ "setPostalCode:"
+ "setState:"
+ "setStreet:"
+ "sortedArrayUsingComparator:"
+ "title for recent files section in files browse"
+ "title for suggestion section in files and apps browse"
+ "we're missing the lastuseddate when checking for expirationdate"
+ "we're missing the lastuseddate when indexing. Skip indexing."
- "Quiescing session pool"
- "we're missing the lastuseddate when indexing"

```
