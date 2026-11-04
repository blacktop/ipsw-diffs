## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-154.1.8.0.0
-  __TEXT.__text: 0x84260
-  __TEXT.__objc_methlist: 0x6714
-  __TEXT.__const: 0xb10
-  __TEXT.__gcc_except_tab: 0xe0c
-  __TEXT.__cstring: 0x6b92
-  __TEXT.__oslogstring: 0x8700
+154.2.4.0.0
+  __TEXT.__text: 0x88254
+  __TEXT.__objc_methlist: 0x69cc
+  __TEXT.__const: 0xba0
+  __TEXT.__gcc_except_tab: 0xe3c
+  __TEXT.__cstring: 0x6ee2
+  __TEXT.__oslogstring: 0x8aa0
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x2aa
   __TEXT.__constg_swiftt: 0x164

   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift_as_cont: 0x40
   __TEXT.__swift5_capture: 0x98
-  __TEXT.__unwind_info: 0x21a0
+  __TEXT.__unwind_info: 0x22c0
   __TEXT.__eh_frame: 0x658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1988
-  __DATA_CONST.__objc_classlist: 0x3f8
+  __DATA_CONST.__const: 0x1ab0
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34b8
+  __DATA_CONST.__objc_selrefs: 0x3698
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x230
-  __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0x1b48
-  __AUTH_CONST.__const: 0x1758
-  __AUTH_CONST.__cfstring: 0x7220
-  __AUTH_CONST.__objc_const: 0xab78
-  __AUTH_CONST.__objc_intobj: 0x1bc0
-  __AUTH_CONST.__objc_arrayobj: 0x4f8
-  __AUTH_CONST.__auth_got: 0xc48
-  __AUTH.__objc_data: 0xad8
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_arraydata: 0x400
+  __DATA_CONST.__got: 0x1ba8
+  __AUTH_CONST.__const: 0x17f8
+  __AUTH_CONST.__cfstring: 0x74e0
+  __AUTH_CONST.__objc_const: 0xae80
+  __AUTH_CONST.__objc_intobj: 0x1c50
+  __AUTH_CONST.__objc_arrayobj: 0x5a0
+  __AUTH_CONST.__auth_got: 0xc90
+  __AUTH.__objc_data: 0xb28
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x774
+  __DATA.__objc_ivar: 0x7a8
   __DATA.__data: 0x540
   __DATA_DIRTY.__objc_data: 0x1ea0
   __DATA_DIRTY.__data: 0x248

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3012
-  Symbols:   1057
-  CStrings:  1600
+  Functions: 3104
+  Symbols:   1078
+  CStrings:  1638
 
Symbols:
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _IAChannelPencilVisualIntelligence
+ _IAPayloadKeyPencilVisualIntelligenceUnderlyingBundleId
+ _IASignalPencilVisualIntelligenceEnterHighlightDoubleTap
+ _IASignalPencilVisualIntelligenceEnterHighlightSqueezePalette
+ _IASignalPencilVisualIntelligenceEnterHighlightUnspecified
+ _IASignalPencilVisualIntelligenceExitHighlight
+ _IASignalPencilVisualIntelligenceLassoSelection
+ _IASignalPencilVisualIntelligenceSiriRequestSent
+ _IASignalPencilVisualIntelligenceSuggestionSelected
+ _OBJC_CLASS_$_CMMagicPoseManager
+ _OBJC_CLASS_$_GMAvailabilityWrapper
+ _OBJC_CLASS_$_NSOperationQueue
+ _gettimeofday
+ _localtime_r
+ _mach_continuous_time
+ _mach_timebase_info
+ _objc_retain_x7
+ _strlen
CStrings:
+ "BEGIN TRANSACTION;DROP TABLE IF EXISTS %1$@;CREATE TABLE %1$@ (date TEXT NOT NULL, pencilVersion INTEGER NOT NULL, usageType INTEGER NOT NULL, appInfo TEXT NOT NULL, inUseDisplay INTEGER NOT NULL, devicePose INTEGER NOT NULL, activeMinutes INTEGER, activeSeconds INTEGER, lastActivityTimestamp INTEGER, PRIMARY KEY (date, pencilVersion, usageType, appInfo, inUseDisplay, devicePose));COMMIT;"
+ "CoreMotion did not return a device pose: %{private}@"
+ "Device pose changed: hingeState=%lu, outerOrientation=%lu, innerOrientation=%lu, timestamp=%f"
+ "DevicePoseChanged"
+ "Failed to load AOP daily event counter for %{private}@: %{private}@"
+ "Failed to migrate the pencil usage table to v3 with error %{private}s"
+ "Failed to reset AOP daily event counter for %{private}@: %{private}@"
+ "Migrated the pencil usage table to v3 (dropped the old table, added the devicePose column)."
+ "Not publishing pencil VI signal: %{private}@"
+ "Pencil VI signal %{private}@ carries no underlying bundle id."
+ "Pencil VI signal %{private}@ from CampoUI carries no session id."
+ "Pencil VI signal %{private}@ received outside a VI session."
+ "SuggestionCategoryEventCount"
+ "Unexpected AOP event name %@"
+ "[%{private}@] Biome: availability = %{private}ld, additional policy options = %{private}d"
+ "actionType=%@"
+ "analyzer"
+ "analyzerId"
+ "analyzers"
+ "class"
+ "com.apple.engineering-test"
+ "com.apple.inputAnalytics.pencilIntelligence"
+ "devicePose"
+ "dumpStateWithReply: %{private}@ returned a nil stateDictionary, skipping"
+ "dumpStateWithReply: JSON serialization failed: %{private}@"
+ "dumpStateWithReply: state dictionary is not JSON-serializable"
+ "hingeState"
+ "innerOrientation"
+ "inputanalyticsd"
+ "linkedSessionIds"
+ "onDiskVersionForTable should be exhaustive but wasn't. Returning Unknown."
+ "outerOrientation"
+ "pccRequestType"
+ "sessionManagers"
+ "sessions"
+ "state"
+ "timestamp"
+ "v24@?0@\"CMMagicPoseEvent\"8@\"NSError\"16"
+ "v32@?0@\"NSNumber\"8@\"IASCandidateBarAnalyzer\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
- "Failed to load AOP daily event counter: %{private}@"
- "Failed to reset AOP daily event counter: %{private}@"
```
