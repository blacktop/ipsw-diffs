## gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

-2.0.21.0.0
-  __TEXT.__text: 0x24848
+2.0.23.0.0
+  __TEXT.__text: 0x27d9c
   __TEXT.__auth_stubs: 0x1070
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0xf94
+  __TEXT.__const: 0xf64
   __TEXT.__objc_methname: 0xc84
   __TEXT.__objc_classname: 0xd5
   __TEXT.__objc_methtype: 0x2ed
-  __TEXT.__cstring: 0x267b
-  __TEXT.__swift5_typeref: 0x8b1
+  __TEXT.__cstring: 0x26bb
+  __TEXT.__swift5_typeref: 0x8b7
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x12a0
-  __TEXT.__swift5_reflstr: 0xcec
-  __TEXT.__swift5_fieldmd: 0x8e0
+  __TEXT.__constg_swiftt: 0x11ec
+  __TEXT.__swift5_reflstr: 0xd5c
+  __TEXT.__swift5_fieldmd: 0x92c
   __TEXT.__swift5_proto: 0x8c
-  __TEXT.__swift5_types: 0x74
+  __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_capture: 0x330
-  __TEXT.__oslogstring: 0x8c8
+  __TEXT.__oslogstring: 0x948
   __TEXT.__info_plist: 0x528
-  __TEXT.__unwind_info: 0x750
-  __TEXT.__eh_frame: 0x5f0
+  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__eh_frame: 0x700
   __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x268
-  __DATA_CONST.__const: 0xdd8
+  __DATA_CONST.__const: 0xe70
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0x2690
+  __DATA.__objc_const: 0x2630
   __DATA.__objc_selrefs: 0x3c0
-  __DATA.__objc_data: 0x840
-  __DATA.__data: 0x2010
+  __DATA.__objc_data: 0x868
+  __DATA.__data: 0x1f10
   __DATA.__common: 0x70
   __DATA.__bss: 0xe00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 639
-  Symbols:   403
-  CStrings:  491
+  Functions: 674
+  Symbols:   404
+  CStrings:  492
 
Symbols:
+ _$s10GamePolicy0A10ModeStatusC08previousA17BundleIdentifiersSaySSGvpWvd
+ _$s10GamePolicy0A10ModeStatusC6ConfigV7enabled14enablementDate011disablementH015deviceSupported17jettisonCameraS2R21gameBundleIdentifiers08previousapQ008impactedpQ0018previouslyImpactedpQ00G8StrategyAESb_10Foundation0H0VSgASS2bSaySSGA3tA0c10EnablementV0OtcfC
- _$s10GamePolicy0A10ModeStatusC6ConfigV7enabled14enablementDate011disablementH015deviceSupported21gameBundleIdentifiers08impactedmN0018previouslyImpactedmN00G8StrategyAESb_10Foundation0H0VSgAQSbSaySSGA2rA0c10EnablementR0OtcfC
CStrings:
+ "Bundle ID = %!{(MISSING)public, name=bundleId}%!s(MISSING)\n\nRequires Performance Gaming Tier = %!{(MISSING)public, name=requiresPerformanceGamingTier}%!d(MISSING)\n\nRequires Increased Memory Limit = %!{(MISSING)public, name=requiresIncreasedMemoryLimit}d\n\nRequires Increased Debug Memory Limit = %!{(MISSING)public, name=requiresIncreasedDebugMemoryLimit}d\n\nSupports SEM = %!{(MISSING)public, name=supportsSEM}d\n\nSupports Model Manager Assertion = %!{(MISSING)public, name=supportsModelManagerAssertion}d\n\nRequires Model Manager Assertion %!{(MISSING)public, name=requiresModelManagerAssertion}d\n\nSupports Camera Jettison S2R %!{(MISSING)public, name=supportsCameraJettisonS2R}d"
+ "Jettison Camera S2R %!{(MISSING)public}s."
+ "JettisonCameraS2R: Disabled"
+ "JettisonCameraS2R: Enabled"
+ "Unable to post game mode camera jettison S2R darwin notification - token is invalid!"
+ "_observers"
+ "_onqueue_modelManagerAssertion"
+ "_state"
+ "com.apple.system.console_mode_changed_camera_jettison_s2r"
+ "gameModeCameraJettisonS2RNotification"
+ "gameModeCameraJettisonS2RNotifyToken"
+ "supportsCameraJettisonS2R"
- "Bundle ID = %!{(MISSING)public, name=bundleId}%!s(MISSING)\n\nRequires Performance Gaming Tier = %!{(MISSING)public, name=requiresPerformanceGamingTier}%!d(MISSING)\n\nRequires Increased Memory Limit = %!{(MISSING)public, name=requiresIncreasedMemoryLimit}d\n\nRequires Increased Debug Memory Limit = %!{(MISSING)public, name=requiresIncreasedDebugMemoryLimit}d\n\nSupports SEM = %!{(MISSING)public, name=supportsSEM}d\n\nSupports Model Manager Assertion = %!{(MISSING)public, name=supportsModelManagerAssertion}d\n\nRequires Model Manager Assertion %!{(MISSING)public, name=requiresModelManagerAssertion}d"
- "_dynamicSplitterEnablementStrategy"
- "_gameModeEnablementStrategy"
- "_modelManagerGameAssertionPolicyStrategy"
- "_sustainedExecutionEnablementStrategy"
- "dynamicSplitterStatus"
- "gameModeStatus"
- "modelManagerAssertion"
- "modelManagerGameAssertionStatus"
- "observers"
- "sustainedExecutionStatus"

```
