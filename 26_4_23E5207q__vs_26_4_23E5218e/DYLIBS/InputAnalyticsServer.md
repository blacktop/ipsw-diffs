## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-111.4.3.0.0
-  __TEXT.__text: 0x69d20
-  __TEXT.__auth_stubs: 0x1310
-  __TEXT.__objc_methlist: 0x5134
+111.4.5.0.0
+  __TEXT.__text: 0x6aba4
+  __TEXT.__auth_stubs: 0x1320
+  __TEXT.__objc_methlist: 0x5164
   __TEXT.__const: 0x580
-  __TEXT.__cstring: 0x4957
-  __TEXT.__oslogstring: 0x6603
+  __TEXT.__cstring: 0x4a17
+  __TEXT.__oslogstring: 0x6703
   __TEXT.__gcc_except_tab: 0xc94
   __TEXT.__swift5_typeref: 0x1b7
   __TEXT.__constg_swiftt: 0xec

   __TEXT.__swift5_capture: 0x98
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x16f8
+  __TEXT.__unwind_info: 0x1718
   __TEXT.__eh_frame: 0x358
   __TEXT.__objc_classname: 0xcca
-  __TEXT.__objc_methname: 0xc340
-  __TEXT.__objc_methtype: 0x11cd
-  __TEXT.__objc_stubs: 0x9ac0
-  __DATA_CONST.__got: 0x1280
+  __TEXT.__objc_methname: 0xc450
+  __TEXT.__objc_methtype: 0x11ad
+  __TEXT.__objc_stubs: 0x9b80
+  __DATA_CONST.__got: 0x1288
   __DATA_CONST.__const: 0x1290
   __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a20
+  __DATA_CONST.__objc_selrefs: 0x2a50
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__auth_got: 0x998
+  __AUTH_CONST.__auth_got: 0x9a0
   __AUTH_CONST.__const: 0xf98
-  __AUTH_CONST.__cfstring: 0x5360
-  __AUTH_CONST.__objc_const: 0x8c78
-  __AUTH_CONST.__objc_intobj: 0xeb8
+  __AUTH_CONST.__cfstring: 0x53c0
+  __AUTH_CONST.__objc_const: 0x8ca8
+  __AUTH_CONST.__objc_intobj: 0xfc0
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x614
+  __DATA.__objc_ivar: 0x618
   __DATA.__data: 0x578
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x1608

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 67347317-493B-397A-9DD1-89E744AA7552
-  Functions: 2279
-  Symbols:   776
-  CStrings:  4178
+  UUID: D1BBA61B-2E59-3C9B-8CAD-AC0A8C0C803F
+  Functions: 2289
+  Symbols:   777
+  CStrings:  4196
 
Symbols:
+ _OBJC_CLASS_$_BMWritingToolsRequests
+ _os_transaction_create
- __swift_FORCE_LOAD_$_swiftCoreImage
CStrings:
+ "%{private}@ signal received without a bundleId"
+ "1.0"
+ "Handling a signal with nil bundleId but it should already have been filtered out."
+ "IASMissingKeyboardAnalyzer.m"
+ "Requests"
+ "T@\"NSMutableArray\",&,N,V_biomeWritingToolsComposeAndAdjust"
+ "T@\"NSMutableArray\",&,N,V_biomeWritingToolsRequests"
+ "[%{private}@] Biome: content warning detected, will skip Requests events"
+ "[%{private}@] Biome: nil prompt, will skip ComposeAndAdjust event"
+ "[%{private}@] ComposeAndAdjust Biome: %{sensitive}@"
+ "[%{private}@] Requests Biome: %{sensitive}@"
+ "_biomeWritingToolsRequests"
+ "biomeWritingToolsRequests"
+ "com.apple.inputanalyticsd.missingKeyboardAnalyzer.screenshotAndDetection"
+ "initWithTimestamp:clientBundleID:originalText:prompt:userInterfaceLanguage:userSetRegionFormat:feature:result:version:"
+ "sendBiomeAnalyticsComposeAndAdjust"
+ "sendBiomeAnalyticsRequests"
+ "setBiomeWritingToolsRequests:"
- "@\"BMWritingToolsComposeAndAdjust\""
- "T@\"BMWritingToolsComposeAndAdjust\",&,N,V_biomeWritingToolsComposeAndAdjust"
- "[%{private}@] Biome: Skip nil prompt"

```
