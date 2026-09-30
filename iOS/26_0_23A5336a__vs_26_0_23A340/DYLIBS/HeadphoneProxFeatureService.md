## HeadphoneProxFeatureService

> `/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService`

```diff

 30.59.1.9.0
-  __TEXT.__text: 0x153f0
-  __TEXT.__auth_stubs: 0x970
+  __TEXT.__text: 0x16918
+  __TEXT.__auth_stubs: 0x9f0
   __TEXT.__objc_methlist: 0x9c
-  __TEXT.__const: 0x590
-  __TEXT.__cstring: 0x6e6
-  __TEXT.__swift5_typeref: 0x3fa
-  __TEXT.__swift5_reflstr: 0x2c7
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__constg_swiftt: 0x390
-  __TEXT.__swift5_fieldmd: 0x1d8
+  __TEXT.__const: 0x6a0
+  __TEXT.__cstring: 0x796
+  __TEXT.__swift5_typeref: 0x408
+  __TEXT.__swift5_reflstr: 0x317
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__constg_swiftt: 0x3ac
+  __TEXT.__swift5_fieldmd: 0x20c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__oslogstring: 0x2256
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__oslogstring: 0x25c6
   __TEXT.__swift5_capture: 0x114
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3c8
+  __TEXT.__unwind_info: 0x3f0
   __TEXT.__eh_frame: 0x180
-  __TEXT.__objc_methname: 0x5b2
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__objc_methname: 0x622
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x4b8
-  __AUTH_CONST.__const: 0x818
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__const: 0x948
   __AUTH_CONST.__objc_const: 0x550
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x188
-  __DATA.__data: 0xb8
-  __DATA.__bss: 0x5a0
+  __DATA.__data: 0xc8
+  __DATA.__bss: 0x7a0
   __DATA_DIRTY.__data: 0x2c0
   __DATA_DIRTY.__bss: 0x80
   __DATA_DIRTY.__common: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
+  - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager
   - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0FE4353-0DE6-3D55-81B6-ECBB11EDD227
-  Functions: 380
-  Symbols:   338
-  CStrings:  221
+  UUID: CF2A10DD-7296-33A9-BF42-38F2B88AC3E6
+  Functions: 407
+  Symbols:   345
+  CStrings:  240
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsPersonalTranslator
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_memcpy0_1
+ _associated conformance 27HeadphoneProxFeatureService17TranslateFeaturesOSHAASQ
+ _symbolic _____ 27HeadphoneProxFeatureService17TranslateFeaturesO
- _swift_setDeallocating
CStrings:
+ ", Live Translation: "
+ "HeadphoneProxFeatureService: %s: Invalid Device, Return false address: %s %s"
+ "HeadphoneProxFeatureService: %s: device does not support track workout, Return false %s"
+ "HeadphoneProxFeatureService: [%s] setProxCardShowedFeatures: Live Translation: %s -> %s"
+ "HeadphoneProxFeatureService: [%s] setProxCardShowedFeatures: PersonalTranslator: %s -> %s"
+ "HeadphoneProxFeatureService: [%s] shouldShowLiveTranslationCard: %s, Current Version: %s, Target Version: %s"
+ "HeadphoneProxFeatureService: [%s] shouldShowLiveTranslationCard: Force Show!"
+ "HeadphoneProxFeatureService: [%s] shouldShowLiveTranslationCard: No Apple Intelligence Prerequisite Not Met!"
+ "HeadphoneProxFeatureService: isAppleIntelligencePrerequisiteMet %{bool}d %{bool}d"
+ "HeadphoneProxFeatureService: shouldShowLiveTranslationCard: Feature Enabled:  %s, Device Supported: %s"
+ "Translate"
+ "forceShowLiveTranslation"
+ "heartRateMonitorCapability"
+ "liveTranslation"
+ "personalTranslator"
+ "personalTranslatorCapability"
+ "personalTranslatorVersion"
+ "setPersonalTranslatorVersion:"
+ "shouldShowTrackWorkoutCard(deviceAddress:)"

```
