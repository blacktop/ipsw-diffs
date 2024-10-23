## MetricsFramework

> `/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework`

```diff

-3401.12.1.0.0
-  __TEXT.__text: 0x87d74
+3402.18.1.0.0
+  __TEXT.__text: 0x8915c
   __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__const: 0x5090
-  __TEXT.__cstring: 0x32bb
-  __TEXT.__constg_swiftt: 0x2658
-  __TEXT.__swift5_typeref: 0x1608
+  __TEXT.__const: 0x51c0
+  __TEXT.__cstring: 0x359b
+  __TEXT.__constg_swiftt: 0x26d0
+  __TEXT.__swift5_typeref: 0x1634
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x2026
-  __TEXT.__swift5_assocty: 0x5b0
-  __TEXT.__swift5_proto: 0x3ac
-  __TEXT.__swift5_types: 0x22c
-  __TEXT.__swift5_fieldmd: 0x20ec
-  __TEXT.__oslogstring: 0x1d2a
+  __TEXT.__swift5_reflstr: 0x2336
+  __TEXT.__swift5_assocty: 0x5e0
+  __TEXT.__swift5_proto: 0x3bc
+  __TEXT.__swift5_types: 0x238
+  __TEXT.__swift5_fieldmd: 0x2224
+  __TEXT.__oslogstring: 0x1d26
   __TEXT.__swift5_capture: 0x2cc
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x1e58
-  __TEXT.__eh_frame: 0x3620
+  __TEXT.__unwind_info: 0x1e90
+  __TEXT.__eh_frame: 0x3660
   __TEXT.__objc_methname: 0x1659
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x198
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5d0
   __AUTH_CONST.__auth_got: 0xa78
   __AUTH_CONST.__auth_ptr: 0x708
-  __AUTH_CONST.__const: 0x3778
-  __AUTH_CONST.__cfstring: 0x1c40
-  __AUTH_CONST.__objc_const: 0x2718
+  __AUTH_CONST.__const: 0x3918
+  __AUTH_CONST.__cfstring: 0x1ca0
+  __AUTH_CONST.__objc_const: 0x27a8
   __AUTH.__objc_data: 0xaf0
-  __AUTH.__data: 0x3248
-  __DATA.__data: 0x1a58
-  __DATA.__bss: 0x7180
+  __AUTH.__data: 0x3370
+  __DATA.__data: 0x1a88
+  __DATA.__bss: 0x7380
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2353
-  Symbols:   280
-  CStrings:  861
+  Functions: 2373
+  Symbols:   282
+  CStrings:  881
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "AssetMetricsPluginLastRunDate"
+ "AssetMetricsWorker-MLHost"
+ "BootToAssetCalculator query yielded %!l(MISSING)d results"
+ "BootToAssetMetrics"
+ "BootToAssetSelfReporter reporting results for %!l(MISSING)d days"
+ "IEROUTING_GENERATIVE_AI"
+ "IEROUTING_QUERY_REWRITE"
+ "IEROUTING_SIRI_X"
+ "MetricsFramework/BootToAssetReporter.swift"
+ "RequestWithNoAssetsCalculator query yielded %!l(MISSING)d results"
+ "SQL calculator invoked: AssetPenetrationCalculator %!s(MISSING)"
+ "SQL calculator invoked: BootToAssetCalculator %!s(MISSING)"
+ "SQL calculator invoked: RequestWithNoAssetsCalculator %!s(MISSING)"
+ "_TtC16MetricsFramework18BootToAssetMetrics"
+ "_TtC16MetricsFramework19BootToAssetReporter"
+ "_TtC16MetricsFramework20AssetMetricsExecutor"
+ "_TtC16MetricsFramework21BootToAssetCalculator"
+ "_TtC16MetricsFramework23BootToAssetDataProvider"
+ "_TtC16MetricsFramework23BootToAssetSELFReporter"
+ "_TtC16MetricsFramework29RequestWithNoAssetsCalculator"
+ "com.apple.AssetMetricsWorker"
+ "disablePersistentIDLoggingClassic"
+ "disablePersistentIDLoggingClassicOptOut"
+ "disablePersistentIDLoggingGM"
+ "disablePersistentIDLoggingIOS"
+ "disablePersistentIDLoggingIOSOptOut"
+ "disablePersistentIDLoggingMacOS"
+ "disablePersistentIDLoggingMacOSOptOut"
+ "disablePersistentIDLoggingOptIn"
+ "disablePersistentIDLoggingSiriXHybrid"
+ "disablePersistentIDLoggingSiriXHybridOptOut"
+ "disablePersistentIDLoggingSiriXUOD"
+ "disablePersistentIDLoggingSiriXUODOptOut"
+ "disablePersistentIDLoggingVisionOS"
+ "disablePersistentIDLoggingVisionOSOptOut"
- "MetricsFramework/SiriBootToAssetReporter.swift"
- "SQL calculator invoked: SiriAssetPenetrationCalculator %!s(MISSING)"
- "SQL calculator invoked: SiriBootToAssetCalculator %!s(MISSING)"
- "SQL calculator invoked: SiriRequestWithNoAssetsCalculator %!s(MISSING)"
- "SiriBootToAssetCalculator query yielded %!l(MISSING)d results"
- "SiriBootToAssetSelfReporter reporting results for %!l(MISSING)d days"
- "SiriRequestWithNoAssetsCalculator query yielded %!l(MISSING)d results"
- "_TtC16MetricsFramework22SiriBootToAssetMetrics"
- "_TtC16MetricsFramework23SiriBootToAssetReporter"
- "_TtC16MetricsFramework25SiriBootToAssetCalculator"
- "_TtC16MetricsFramework27SiriBootToAssetDataProvider"
- "_TtC16MetricsFramework27SiriBootToAssetSELFReporter"
- "_TtC16MetricsFramework33SiriRequestWithNoAssetsCalculator"
- "asset_penetration"
- "siriBootToAssetMetrics"

```
