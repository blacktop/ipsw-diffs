## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-147.0.0.0.0
-  __TEXT.__text: 0x7b708
-  __TEXT.__objc_methlist: 0x609c
-  __TEXT.__const: 0xa50
-  __TEXT.__gcc_except_tab: 0xd50
-  __TEXT.__cstring: 0x6282
-  __TEXT.__oslogstring: 0x7840
+153.0.0.0.0
+  __TEXT.__text: 0x7e28c
+  __TEXT.__objc_methlist: 0x62a4
+  __TEXT.__const: 0xab0
+  __TEXT.__gcc_except_tab: 0xd28
+  __TEXT.__cstring: 0x64e2
+  __TEXT.__oslogstring: 0x7b50
   __TEXT.__swift5_typeref: 0x2aa
   __TEXT.__constg_swiftt: 0x164
   __TEXT.__swift5_fieldmd: 0x88

   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift_as_cont: 0x40
   __TEXT.__swift5_capture: 0x98
-  __TEXT.__unwind_info: 0x1778
+  __TEXT.__unwind_info: 0x1818
   __TEXT.__eh_frame: 0x5f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1740
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__const: 0x17b8
+  __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30c0
+  __DATA_CONST.__objc_selrefs: 0x31c8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0x18f0
-  __AUTH_CONST.__const: 0x14d8
-  __AUTH_CONST.__cfstring: 0x6780
-  __AUTH_CONST.__objc_const: 0xa528
-  __AUTH_CONST.__objc_intobj: 0x17b8
+  __DATA_CONST.__got: 0x1930
+  __AUTH_CONST.__const: 0x1558
+  __AUTH_CONST.__cfstring: 0x6aa0
+  __AUTH_CONST.__objc_const: 0xa5a8
+  __AUTH_CONST.__objc_intobj: 0x1878
   __AUTH_CONST.__objc_arrayobj: 0x4f8
-  __AUTH_CONST.__auth_got: 0xbf0
-  __AUTH.__objc_data: 0xad8
+  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH.__objc_data: 0xa88
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x738
+  __DATA.__objc_ivar: 0x74c
   __DATA.__data: 0x4e8
-  __DATA.__bss: 0x740
+  __DATA.__bss: 0x770
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0x240
   __DATA_DIRTY.__bss: 0x678

   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/Anvil.framework/Anvil
   - /System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics
+  - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport
   - /System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent
   - /usr/lib/libAccessibility.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2792
-  Symbols:   974
-  CStrings:  1463
+  Functions: 2848
+  Symbols:   982
+  CStrings:  1500
 
Symbols:
+ _IADataStoreObjectTypeCounter
+ _IAPayloadKeyImageGenerationAssetID
+ _IAPayloadKeyImageGenerationUnredactedStyle
+ _IAPayloadKeyPencilSystemDisplayIdentifier
+ _IASignalImageGenerationPCCImageGenerated
+ _IASignalImageGenerationPIRImageGenerated
+ _MGCopyAnswerWithError
+ _OBJC_CLASS_$_BKSDisplayService
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
