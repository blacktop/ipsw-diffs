## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/Versions/A/InputAnalyticsServer`

```diff

-147.0.0.0.0
-  __TEXT.__text: 0x7bbd8
-  __TEXT.__objc_methlist: 0x5f8c
-  __TEXT.__const: 0x648
-  __TEXT.__gcc_except_tab: 0xc14
-  __TEXT.__cstring: 0x5bf2
-  __TEXT.__oslogstring: 0x7330
+153.500.0.0.0
+  __TEXT.__text: 0x7e8d0
+  __TEXT.__objc_methlist: 0x6194
+  __TEXT.__const: 0x6b8
+  __TEXT.__gcc_except_tab: 0xbec
+  __TEXT.__cstring: 0x5e52
+  __TEXT.__oslogstring: 0x7640
   __TEXT.__swift5_typeref: 0x1f5
   __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_fieldmd: 0x50

   __TEXT.__swift5_capture: 0x98
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x1580
+  __TEXT.__unwind_info: 0x1608
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1338
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__const: 0x13b8
+  __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ee8
+  __DATA_CONST.__objc_selrefs: 0x2fd8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x398
-  __DATA_CONST.__got: 0x17a0
-  __AUTH_CONST.__const: 0x1878
-  __AUTH_CONST.__cfstring: 0x6120
-  __AUTH_CONST.__objc_const: 0xa4f8
-  __AUTH_CONST.__objc_intobj: 0x1788
+  __DATA_CONST.__got: 0x17d0
+  __AUTH_CONST.__const: 0x18f8
+  __AUTH_CONST.__cfstring: 0x6440
+  __AUTH_CONST.__objc_const: 0xa578
+  __AUTH_CONST.__objc_intobj: 0x1848
   __AUTH_CONST.__objc_arrayobj: 0x4e0
-  __AUTH_CONST.__auth_got: 0x948
-  __AUTH.__objc_data: 0xad8
+  __AUTH_CONST.__auth_got: 0x958
+  __AUTH.__objc_data: 0xa88
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x734
+  __DATA.__objc_ivar: 0x748
   __DATA.__data: 0x420
-  __DATA.__bss: 0x140
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0x250
   __DATA_DIRTY.__bss: 0x660

   - /System/Library/PrivateFrameworks/Anvil.framework/Versions/A/Anvil
   - /System/Library/PrivateFrameworks/AudioAnalytics.framework/Versions/A/AudioAnalytics
   - /System/Library/PrivateFrameworks/AudioSession.framework/Versions/A/AudioSession
+  - /System/Library/PrivateFrameworks/BackBoardServices.framework/Versions/A/BackBoardServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams

   - /System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/Versions/A/UIIntelligenceSupport
   - /System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/Versions/A/UIIntelligenceSupportAgent
   - /usr/lib/libAccessibility.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2685
-  Symbols:   865
-  CStrings:  1378
+  Functions: 2741
+  Symbols:   871
+  CStrings:  1415
 
Symbols:
+ _IADataStoreObjectTypeCounter
+ _IAPayloadKeyImageGenerationAssetID
+ _IAPayloadKeyImageGenerationUnredactedStyle
+ _IASignalImageGenerationPCCImageGenerated
+ _IASignalImageGenerationPIRImageGenerated
+ _MGCopyAnswerWithError
CStrings:
+ "Always-on Proofreading"
+ "Assistant Enabled"
+ "Dropping AOP event: missing/unparseable GrammarUUID %{private}@"
+ "EventCount"
+ "Failed to load AOP daily event counter: %{private}@"
+ "Failed to reset AOP daily event counter: %{private}@"
+ "IASImageGenerationImageInteractionAnalyzer.m"
+ "MobileGestalt read failed for DeviceSupportsApplePencil (error=%{private}d, answer=%{private}@) - falling back to device model prefix check"
+ "PersonalizedSmartReplies"
+ "Proofread"
+ "Replaced nil bundleId with com.apple.nilBundleId."
+ "Rewrite"
+ "Rolled dedup caches and reset daily event count in periodic24HourEvents"
+ "ShownPersonalizeSmartRepliesAlert"
+ "Siri"
+ "Smart Reply"
+ "Writing Tools"
+ "[%{private}@] Biome ImageInteraction: %{sensitive}@"
+ "[%{private}@] Dropping ImageInteraction with no assetIdentifier for signal %{private}@"
+ "campoAvailability"
+ "com.apple.assistant.support"
+ "com.apple.inputAnalytics.IASAOPAnalyzer"
+ "com.apple.inputAnalytics.server.IASImageGenerationImageInteractionAnalyzer"
+ "com.apple.nilBundleId"
+ "content_dismissed"
+ "content_generated"
+ "custom_measure_type"
+ "custom_measure_value"
+ "group.com.apple.mail"
+ "isEnhancedSiriAvailable called"
+ "periodic24HourEvents: Campo available:%{private}lu"
+ "periodic24HourEvents: mail defaults initialized"
+ "periodic24HourEventsWithModelAvailability: grabbing siri settings"
+ "periodic24HourEventsWithModelAvailability: siri settings grabbed"
+ "personalizedSmartRepliesAlertShown"
+ "personalizedSmartRepliesEnabled"
+ "siriSettings"
+ "unredactedStyle"
+ "yhHcB0iH0d1XzPO/CFd3ow"
- "&"
- "Rolled dedup caches in periodic24HourEvents"
```
