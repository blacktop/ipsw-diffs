## SmartReplies

> `/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies`

```diff

-116.3.0.0.0
-  __TEXT.__text: 0x67a54
-  __TEXT.__auth_stubs: 0x19c0
-  __TEXT.__objc_methlist: 0x11e4
-  __TEXT.__const: 0x2c00
-  __TEXT.__cstring: 0x279c
-  __TEXT.__constg_swiftt: 0x1494
-  __TEXT.__swift5_typeref: 0xfc4
-  __TEXT.__swift5_reflstr: 0x178e
-  __TEXT.__swift5_fieldmd: 0x1194
+116.7.3.0.0
+  __TEXT.__text: 0x6db88
+  __TEXT.__auth_stubs: 0x1a30
+  __TEXT.__objc_methlist: 0x1244
+  __TEXT.__const: 0x2c30
+  __TEXT.__cstring: 0x28fc
+  __TEXT.__constg_swiftt: 0x14ac
+  __TEXT.__swift5_typeref: 0xfd6
+  __TEXT.__swift5_reflstr: 0x17de
+  __TEXT.__swift5_fieldmd: 0x11b8
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__oslogstring: 0x232c
+  __TEXT.__oslogstring: 0x254c
   __TEXT.__swift5_proto: 0x1a4
   __TEXT.__swift5_types: 0x120
-  __TEXT.__swift5_capture: 0x42c
+  __TEXT.__swift5_capture: 0x444
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift_as_entry: 0x104
-  __TEXT.__swift_as_ret: 0x110
+  __TEXT.__swift_as_entry: 0x10c
+  __TEXT.__swift_as_ret: 0x118
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1ad0
-  __TEXT.__eh_frame: 0x2ad0
+  __TEXT.__unwind_info: 0x1b88
+  __TEXT.__eh_frame: 0x2dd0
   __TEXT.__objc_classname: 0x236
-  __TEXT.__objc_methname: 0x26a0
-  __TEXT.__objc_methtype: 0xaa2
-  __TEXT.__objc_stubs: 0xb00
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0x308
+  __TEXT.__objc_methname: 0x2741
+  __TEXT.__objc_methtype: 0xaaa
+  __TEXT.__objc_stubs: 0xb40
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xb20
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0xce8
-  __AUTH_CONST.__const: 0x2740
-  __AUTH_CONST.__objc_const: 0x2640
-  __AUTH.__objc_data: 0x7f0
+  __AUTH_CONST.__auth_got: 0xd20
+  __AUTH_CONST.__const: 0x2768
+  __AUTH_CONST.__objc_const: 0x26f0
+  __AUTH.__objc_data: 0x800
   __AUTH.__data: 0x770
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0xa08
+  __DATA.__data: 0xa38
   __DATA.__bss: 0x1f90
-  __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0xaa8
-  __DATA_DIRTY.__data: 0xb58
+  __DATA.__common: 0x68
+  __DATA_DIRTY.__objc_data: 0xac8
+  __DATA_DIRTY.__data: 0xb78
   __DATA_DIRTY.__bss: 0xd10
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions
+  - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FD9920DA-F539-34C5-8E12-C6EFB2FB875D
-  Functions: 2665
-  Symbols:   293
-  CStrings:  940
+  UUID: 19DF5F51-7F9F-36BE-9AB1-9F407AD9CE4C
+  Functions: 2733
+  Symbols:   302
+  CStrings:  963
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _DDBinderMoneyKey
+ _DDResultCurrencyExtraction
+ _DDResultHasType
+ _DDScannerCopyResultsOptionsForPassiveUse
+ _DDScannerCopyResultsWithOptions
+ _DDScannerCreateWithType
+ _DDScannerScanString
CStrings:
+ "$__lazy_storage_$_mostRecentMessage"
+ "@116@0:8Q16@24@32@40@48B56@60d68d76@84Q92d100@108"
+ "@116@0:8q16@24@32@40@48B56@60d68d76@84q92d100@108"
+ "Apple pay action triggered with no valid received message"
+ "Most recent message is not from sender, skipping checkIn action"
+ "No currency amounts found in message for Apple Pay action"
+ "No most recent message found for checkIn action"
+ "No valid currency extraction found for Apple Pay action"
+ "Td,N,R,VcurrencyAmount"
+ "Unable to create ApplePayActionMetadataProvider: scanner creation failed"
+ "Unable to extract currency amounts for Apple Pay action"
+ "Unable to instantiate apple pay metadata provider with a triggered apple pay action request"
+ "currencyAmount"
+ "currencyCode"
+ "hasValidMessages"
+ "initWithType:title:attribution:stringRepresentation:date:hasRichActionType:url:locationLatitude:locationLongitude:imageName:attributionSource:currencyAmount:currencyCode:"
+ "mostRecentMessage"
+ "retrieveActionSuggestionsFor:completionHandler:"
+ "setMostRecentMessage:"
+ "v32@0:8@\"_TtC12SmartReplies31SRSmartRepliesSuggestionRequest\"16@?<v@?@\"NSArray\">24"
+ "xCHECKININCOMINGx"
+ "xCHECKINOUTGOINGx"
+ "✓ Send a Check In"
- "@100@0:8Q16@24@32@40@48B56@60d68d76@84Q92"
- "@100@0:8q16@24@32@40@48B56@60d68d76@84q92"
- "initWithType:title:attribution:stringRepresentation:date:hasRichActionType:url:locationLatitude:locationLongitude:imageName:attributionSource:"

```
