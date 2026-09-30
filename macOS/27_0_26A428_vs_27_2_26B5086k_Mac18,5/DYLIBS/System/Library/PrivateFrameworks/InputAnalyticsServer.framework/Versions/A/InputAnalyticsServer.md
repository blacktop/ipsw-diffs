## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/Versions/A/InputAnalyticsServer`

```diff

-153.500.0.0.0
-  __TEXT.__text: 0x7c918
-  __TEXT.__objc_methlist: 0x6194
-  __TEXT.__const: 0x6b8
-  __TEXT.__gcc_except_tab: 0xbec
-  __TEXT.__cstring: 0x5e52
-  __TEXT.__oslogstring: 0x7640
-  __TEXT.__swift5_typeref: 0x1f5
+154.1.4.0.0
+  __TEXT.__text: 0x7fd88
+  __TEXT.__objc_methlist: 0x630c
+  __TEXT.__const: 0x6d0
+  __TEXT.__gcc_except_tab: 0xcd0
+  __TEXT.__cstring: 0x6162
+  __TEXT.__oslogstring: 0x7a10
+  __TEXT.__swift5_typeref: 0x1f6
   __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_capture: 0x98
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x1d50
-  __TEXT.__eh_frame: 0x378
+  __TEXT.__unwind_info: 0x1e40
+  __TEXT.__eh_frame: 0x3d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x13b8
-  __DATA_CONST.__objc_classlist: 0x3c8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__const: 0x1488
+  __DATA_CONST.__objc_classlist: 0x3e0
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fd8
+  __DATA_CONST.__objc_selrefs: 0x30f0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x398
-  __DATA_CONST.__got: 0x17d0
-  __AUTH_CONST.__const: 0x18f8
-  __AUTH_CONST.__cfstring: 0x6440
-  __AUTH_CONST.__objc_const: 0xa578
-  __AUTH_CONST.__objc_intobj: 0x1848
+  __DATA_CONST.__got: 0x17f8
+  __AUTH_CONST.__const: 0x1998
+  __AUTH_CONST.__cfstring: 0x6840
+  __AUTH_CONST.__objc_const: 0xa780
+  __AUTH_CONST.__objc_intobj: 0x18c0
   __AUTH_CONST.__objc_arrayobj: 0x4e0
-  __AUTH_CONST.__auth_got: 0x958
-  __AUTH.__objc_data: 0xa88
+  __AUTH_CONST.__auth_got: 0x950
+  __AUTH.__objc_data: 0xb78
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x748
-  __DATA.__data: 0x420
+  __DATA.__data: 0x480
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0x250
-  __DATA_DIRTY.__bss: 0x660
+  __DATA_DIRTY.__bss: 0x638
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/PrivateFrameworks/AudioSession.framework/Versions/A/AudioSession
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/Versions/A/BackBoardServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/BatteryCenter.framework/Versions/A/BatteryCenter
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/FeedbackService.framework/Versions/A/FeedbackService

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2741
-  Symbols:   871
-  CStrings:  1415
+  Functions: 2796
+  Symbols:   875
+  CStrings:  1457
 
Symbols:
+ _IAPayloadKeyImageGenerationNumInputImages
+ _IAPayloadValueSidecarInteractionModalitySidecar
+ _IOHIDManagerRegisterDeviceRemovalCallback
+ _OBJC_CLASS_$_BCBatteryDeviceController
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
- _IOHIDDeviceGetProperty
CStrings:
+ "!!"
+ "3!"
+ "ChargingStateChanged"
+ "Concise Rewrite"
+ "Failed to initialize the pencil data store. Will retry on the next call to sharedInstance."
+ "Failed to initialize the sidecar data store. Will retry on the next call to sharedInstance."
+ "Failed to initialize the system table. Will retry on the next call to sharedInstance."
+ "Failed to open the pencil data store tables (usageTable ok: %d, errorTable ok: %d). Will retry on the next call to sharedInstance."
+ "Failed to open the sidecar data store tables (usageTable ok: %d, lifecycleTable ok: %d). Will retry on the next call to sharedInstance."
+ "Friendly Rewrite"
+ "IASImageGenerationDirectManipulationAnalyzer.m"
+ "IASPencilAnalyzerDataStoreBatteryTable"
+ "Key Points"
+ "List"
+ "NSUserDefaults returns value: %@; for key: %@"
+ "PKPencilDoubleTapVisualIntelligenceHighlightEnabledKey"
+ "PKUIPencilHoverPreviewEnabledKey"
+ "Professional Rewrite"
+ "Restored charging state from the data store: state = %lu, battery = %ld, time = %f, identifier=%{private}@, pencilVersion = %lu"
+ "Summary"
+ "Table"
+ "The battery table has %lu rows but should only ever have one. Using the one with the newest timeAtPeriodStart."
+ "This analyzer does not and should not emit CoreAnalytics event."
+ "XCTestCase"
+ "[%{private}@] Biome UserInteraction: %{sensitive}@"
+ "accessoryIdentifier"
+ "batteryChange"
+ "batteryEnd"
+ "batteryPercentage"
+ "batteryPercentageAtPeriodStart"
+ "batteryStart"
+ "chargingState"
+ "com.apple.inputAnalytics.pencilBattery"
+ "com.apple.inputAnalytics.server.IASImageGenerationDirectManipulationAnalyzer"
+ "com.apple.preferences.sounds"
+ "connectedDevicesDidChange pencil productIdentifier=%ld, version=%lu"
+ "effects-pencil-haptic"
+ "hapticsEnablement"
+ "identifierAtPeriodStart"
+ "just published a pencilBattery event with state=Unspecified. This shouldn't happen."
+ "numInputImages"
+ "pencilState"
+ "secondsInState"
+ "shadowEnablement"
+ "singleRowKey"
+ "timeAtPeriodStart"
+ "viAcceleratorState"
- "!"
- "#"
- "C!"
- "ProductID"
- "stylusDeviceAddedCallback pencil productID=%lu"
```
