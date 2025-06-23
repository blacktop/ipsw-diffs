## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-345.58.3.0.0
-  __TEXT.__text: 0x3a9b4
+345.64.1.0.0
+  __TEXT.__text: 0x3a98c
   __TEXT.__auth_stubs: 0x8d0
   __TEXT.__objc_methlist: 0x4b54
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x3619
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x3604
   __TEXT.__gcc_except_tab: 0x4654
   __TEXT.__oslogstring: 0x214a
   __TEXT.__dlopen_cstrs: 0x3a5
   __TEXT.__unwind_info: 0x1b08
-  __TEXT.__objc_classname: 0xe83
+  __TEXT.__objc_classname: 0xe88
   __TEXT.__objc_methname: 0x80a0
   __TEXT.__objc_methtype: 0x2299
   __TEXT.__objc_stubs: 0x2520

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F769D391-13AA-3D06-93E2-D9B4921D30BE
+  UUID: 78A58CF1-E4E5-350E-9D2E-5AB4867DA4DD
   Functions: 1607
   Symbols:   5810
   CStrings:  3033
Symbols:
+ -[MADService(Text) performRequests:text:identifier:completionHandler:]
+ -[MADService(Text) performRequests:textInputs:completionHandler:]
+ -[MADService(Text) prewarmTextRequests:completionHandler:]
+ __OBJC_$_CLASS_METHODS_MADService(Photos|Performance|ProtocolDefaults|UserSafety|VIAnalytics|Text|Spotlight|MultiModal)
+ __OBJC_$_INSTANCE_METHODS_MADService(Photos|Performance|ProtocolDefaults|UserSafety|VIAnalytics|Text|Spotlight|MultiModal)
+ __OBJC_CLASS_PROTOCOLS_$_MADService(Photos|Performance|ProtocolDefaults|UserSafety|VIAnalytics|Text|Spotlight|MultiModal)
+ ___101-[MADService(Spotlight) submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:completionHandler:]_block_invoke.354
+ ___58-[MADService(Text) prewarmTextRequests:completionHandler:]_block_invoke
+ ___58-[MADService(Text) prewarmTextRequests:completionHandler:]_block_invoke.338
+ ___58-[MADService(Text) prewarmTextRequests:completionHandler:]_block_invoke.cold.1
+ ___65-[MADService(Text) performRequests:textInputs:completionHandler:]_block_invoke
+ ___65-[MADService(Text) performRequests:textInputs:completionHandler:]_block_invoke.342
+ ___65-[MADService(Text) performRequests:textInputs:completionHandler:]_block_invoke.cold.1
+ ___70-[MADService(MultiModal) prewarmMultiModalRequests:completionHandler:]_block_invoke.360
+ ___77-[MADService(MultiModal) performRequests:multiModalInputs:completionHandler:]_block_invoke.361
- -[MADService(Spotlight) performRequests:text:identifier:completionHandler:]
- -[MADService(Spotlight) performRequests:textInputs:completionHandler:]
- -[MADService(Spotlight) prewarmTextRequests:completionHandler:]
- __OBJC_$_CLASS_METHODS_MADService(Photos|Performance|ProtocolDefaults|UserSafety|VIAnalytics|Spotlight|MultiModal)
- __OBJC_$_INSTANCE_METHODS_MADService(Photos|Performance|ProtocolDefaults|UserSafety|VIAnalytics|Spotlight|MultiModal)
- __OBJC_CLASS_PROTOCOLS_$_MADService(Photos|Performance|ProtocolDefaults|UserSafety|VIAnalytics|Spotlight|MultiModal)
- ___101-[MADService(Spotlight) submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:completionHandler:]_block_invoke.350
- ___63-[MADService(Spotlight) prewarmTextRequests:completionHandler:]_block_invoke
- ___63-[MADService(Spotlight) prewarmTextRequests:completionHandler:]_block_invoke.338
- ___63-[MADService(Spotlight) prewarmTextRequests:completionHandler:]_block_invoke.cold.1
- ___70-[MADService(MultiModal) prewarmMultiModalRequests:completionHandler:]_block_invoke.359
- ___70-[MADService(Spotlight) performRequests:textInputs:completionHandler:]_block_invoke
- ___70-[MADService(Spotlight) performRequests:textInputs:completionHandler:]_block_invoke.342
- ___70-[MADService(Spotlight) performRequests:textInputs:completionHandler:]_block_invoke.cold.1
- ___77-[MADService(MultiModal) performRequests:multiModalInputs:completionHandler:]_block_invoke.360
Functions:
~ _MADTextEmbeddingCalibrationVersionCurrent : 84 -> 52
~ -[MADImageEmbeddingRequest init] : 148 -> 144
~ -[MADTextEmbeddingRequest init] : 124 -> 120
CStrings:
+ "SearchUnifiedEmbeddingMD7"
- "MD5TextCalibrationV3"
- "SearchUnifiedEmbeddingMD6"

```
