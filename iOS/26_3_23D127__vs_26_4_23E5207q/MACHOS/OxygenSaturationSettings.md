## OxygenSaturationSettings

> `/System/Library/NanoPreferenceBundles/Applications/OxygenSaturationSettings.bundle/OxygenSaturationSettings`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x4348
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__cstring: 0x6c8
-  __TEXT.__const: 0x94
-  __TEXT.__constg_swiftt: 0x1f8
-  __TEXT.__swift5_typeref: 0xd6
-  __TEXT.__swift5_fieldmd: 0x84
+6200.5.77.2.6
+  __TEXT.__text: 0x3190
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x224
+  __TEXT.__objc_classname: 0x158
+  __TEXT.__const: 0x84
+  __TEXT.__constg_swiftt: 0x130
+  __TEXT.__swift5_typeref: 0x76
+  __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_types: 0xc
-  __TEXT.__objc_methname: 0xac5
-  __TEXT.__swift5_reflstr: 0xb2
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methtype: 0x10d
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x188
+  __TEXT.__objc_methname: 0x971
+  __TEXT.__objc_methtype: 0x178
+  __TEXT.__swift5_reflstr: 0x22
+  __TEXT.__cstring: 0x346
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x3b8
-  __DATA.__objc_selrefs: 0x370
-  __DATA.__objc_data: 0x218
-  __DATA.__data: 0x338
+  __DATA.__objc_const: 0x308
+  __DATA.__objc_selrefs: 0x2a8
+  __DATA.__objc_data: 0x128
+  __DATA.__data: 0x308
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
   - /System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience
   - /System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI
-  - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
-  - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth
   - /System/Library/PrivateFrameworks/RespiratoryHealthUI.framework/RespiratoryHealthUI

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 488D3449-51CC-30F4-95DA-5C35186D211A
-  Functions: 75
-  Symbols:   132
-  CStrings:  179
+  UUID: 511C8FF3-D9A1-31C4-9E52-B2825BB0B5D8
+  Functions: 55
+  Symbols:   121
+  CStrings:  139
 
Symbols:
+ _HKLogRespiratory
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ _objc_retain_x24
+ _objc_retain_x28
- _HKFeatureIdentifierOxygenSaturationRecording
- _HKLogRespiratoryCategory
- _OBJC_CLASS_$_HKFeatureAvailabilityStore
- _OBJC_CLASS_$_HKHealthStore
- _OBJC_CLASS_$_HKRPOnboardingViewControllerFactory
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_UIViewPropertyAnimator
- _UIApplicationWillEnterForegroundNotification
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain_x26
- _swift_deallocObject
- _swift_errorRelease
- _swift_getErrorValue
- _swift_willThrow
CStrings:
+ "BLOOD_OXYGEN_DEVICE_NOT_SUPPORTED"
+ "HKRPOxygenSaturationOnboardingManagerObserver"
+ "deliverFeatureWithCompletion:"
+ "deviceIsSupported"
+ "initWithBool:"
+ "oxygenSaturationFeatureStatusDidChange:"
+ "regionIsSupported"
+ "settingsInteractionEnabled"
+ "shouldDeliverFeature"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"HKRPOxygenSaturationOnboardingManager\"16"
- "$__lazy_storage_$_featureAvailabilityStore"
- "$__lazy_storage_$_healthStore"
- "HKRPOnboardingDelegate"
- "[%{public}@] Couldn't get Region supported. Not Onboarded"
- "[%{public}@] Couldn't get Region supported. Remote Disabled"
- "[%{public}@] Couldn't get Region supported. Seed Expired"
- "[%{public}@] Couldn't get Region supported. Unknown state value"
- "[%{public}@] Couldn't get Region supported. error: %@"
- "[%{public}@] Couldn't get onboardedCountryCodeSupportedState with error: %{public}@"
- "addChildViewController:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "contentOffset"
- "defaultCenter"
- "didMoveToParentViewController:"
- "enablePressedWithAppropriateRegion:"
- "hideBarWithTransition:"
- "ineligibilityReasons"
- "initWithFeatureIdentifier:healthStore:"
- "integerValue"
- "isRegionSupported"
- "navigationController"
- "onboardedCountryCodeSupportedStateWithError:"
- "onboardingEligibilityForCountryCode:error:"
- "onboardingScrollViewDidScroll:"
- "onboardingShouldAppear"
- "onboardingViewControllerWithStyle:settings:onboardingManager:onboardingDelegate:"
- "popViewControllerAnimated:"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeObserver:name:object:"
- "runningPropertyAnimatorWithDuration:delay:options:animations:completion:"
- "setAlpha:"
- "setContentOffset:"
- "setName:"
- "setupLaterPressed"
- "showBarWithTransition:"
- "showStartingControllerIfNeeded"
- "startingController"
- "tabBarController"
- "tabBarHidden"
- "table"
- "v16@?0q8"
- "v24@0:8@\"UIScrollView\"16"
- "v8@?0"
- "view"
- "willMoveToParentViewController:"

```
