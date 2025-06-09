## RespiratoryHealth

> `/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x6418
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_methlist: 0xa9c
+6074.1.2.4.0
+  __TEXT.__text: 0x5894
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x93c
   __TEXT.__const: 0x72
-  __TEXT.__oslogstring: 0x9ee
-  __TEXT.__cstring: 0x754
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0x33b
-  __TEXT.__objc_methname: 0x1e4b
-  __TEXT.__objc_methtype: 0x55a
-  __TEXT.__objc_stubs: 0x1300
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x2b0
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__oslogstring: 0x8c0
+  __TEXT.__cstring: 0x734
+  __TEXT.__gcc_except_tab: 0xbc
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__objc_classname: 0x2c9
+  __TEXT.__objc_methname: 0x1b45
+  __TEXT.__objc_methtype: 0x470
+  __TEXT.__objc_stubs: 0x1120
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x288
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x768
+  __DATA_CONST.__objc_selrefs: 0x6d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x208
-  __AUTH_CONST.__cfstring: 0x700
-  __AUTH_CONST.__objc_const: 0x1620
+  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x12f8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x74
-  __DATA.__data: 0x360
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x54
+  __DATA.__data: 0x300
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 99B8FCCD-F0A6-3353-A928-CFA509B2657A
-  Functions: 198
-  Symbols:   896
-  CStrings:  531
+  UUID: 9C086D89-2675-35DC-9394-46BDC1A342B6
+  Functions: 192
+  Symbols:   827
+  CStrings:  490
 
Symbols:
+ -[HKRPOxygenSaturationSettings activateDefaultValuesIfNeeded].cold.1
+ -[HKRPOxygenSaturationSettings activateDefaultValuesIfNeeded].cold.2
+ -[HKRPOxygenSaturationSettings activateDefaultValuesIfNeeded].cold.3
+ GCC_except_table46
+ _HKLogRespiratoryCategory
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.291
+ ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.297
+ ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.308
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_RespiratoryHealth
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_RespiratoryHealth
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_RespiratoryHealth
- -[HKRPOxygenSaturationOnboardingCache .cxx_destruct]
- -[HKRPOxygenSaturationOnboardingCache hasCompletedOnboarding]
- -[HKRPOxygenSaturationOnboardingCache initWithUserDefaults:userDefaultsSyncProvider:]
- -[HKRPOxygenSaturationOnboardingCache setHasCompletedOnboarding:]
- -[HKRPOxygenSaturationOnboardingCacher .cxx_destruct]
- -[HKRPOxygenSaturationOnboardingCacher _queue_featureAvailabilityDidChange]
- -[HKRPOxygenSaturationOnboardingCacher _queue_featureAvailabilityDidChange].cold.1
- -[HKRPOxygenSaturationOnboardingCacher dealloc]
- -[HKRPOxygenSaturationOnboardingCacher featureAvailabilityProvidingDidUpdateOnboardingCompletion:]
- -[HKRPOxygenSaturationOnboardingCacher featureAvailabilityProvidingDidUpdatePairedDeviceCapability:]
- -[HKRPOxygenSaturationOnboardingCacher initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:]
- -[HKRPOxygenSaturationOnboardingCacher initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:didStart:]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource onboardingCache]
- -[_HKRPWatchAppInstallabilityDataSource hasCompletedOnboarding]
- GCC_except_table48
- _HKCreateSerialDispatchQueue
- _HKRPUserDefaultsHasCompletedOnboardingKey
- _OBJC_CLASS_$_HKRPOxygenSaturationOnboardingCache
- _OBJC_CLASS_$_HKRPOxygenSaturationOnboardingCacher
- _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingCache._userDefaults
- _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingCache._userDefaultsSyncProvider
- _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingCacher._featureAvailabilityProvider
- _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingCacher._queue
- _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingCacher._userDefaults
- _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingCacher._userDefaultsSyncProvider
- _OBJC_IVAR_$__HKRPOxygenSaturationOnboardingManagerDataSource._onboardingCache
- _OBJC_IVAR_$__HKRPWatchAppInstallabilityDataSource._onboardingCache
- _OBJC_METACLASS_$_HKRPOxygenSaturationOnboardingCache
- _OBJC_METACLASS_$_HKRPOxygenSaturationOnboardingCacher
- __OBJC_$_INSTANCE_METHODS_HKRPOxygenSaturationOnboardingCache
- __OBJC_$_INSTANCE_METHODS_HKRPOxygenSaturationOnboardingCacher
- __OBJC_$_INSTANCE_VARIABLES_HKRPOxygenSaturationOnboardingCache
- __OBJC_$_INSTANCE_VARIABLES_HKRPOxygenSaturationOnboardingCacher
- __OBJC_$_PROP_LIST_HKRPOxygenSaturationOnboardingCache
- __OBJC_$_PROP_LIST_HKRPOxygenSaturationOnboardingCacher
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKFeatureAvailabilityProvidingObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HKFeatureAvailabilityProvidingObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_HKFeatureAvailabilityProvidingObserver
- __OBJC_$_PROTOCOL_REFS_HKFeatureAvailabilityProvidingObserver
- __OBJC_CLASS_PROTOCOLS_$_HKRPOxygenSaturationOnboardingCacher
- __OBJC_CLASS_RO_$_HKRPOxygenSaturationOnboardingCache
- __OBJC_CLASS_RO_$_HKRPOxygenSaturationOnboardingCacher
- __OBJC_LABEL_PROTOCOL_$_HKFeatureAvailabilityProvidingObserver
- __OBJC_METACLASS_RO_$_HKRPOxygenSaturationOnboardingCache
- __OBJC_METACLASS_RO_$_HKRPOxygenSaturationOnboardingCacher
- __OBJC_PROTOCOL_$_HKFeatureAvailabilityProvidingObserver
- ___124-[HKRPOxygenSaturationOnboardingCacher initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:didStart:]_block_invoke
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.288
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.294
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.305
- ___67-[_HKRPOxygenSaturationOnboardingManagerDataSource onboardingCache]_block_invoke
- ___kCFBooleanTrue
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_RespiratoryHealth
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_RespiratoryHealth
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_RespiratoryHealth
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_RespiratoryHealth
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_RespiratoryHealth
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_RespiratoryHealth
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_RespiratoryHealth
- _objc_msgSend$_notifySettingsDidChange
- _objc_msgSend$_queue_featureAvailabilityDidChange
- _objc_msgSend$_setBackgroundRecordingsDuringSleepMode:
- _objc_msgSend$_setBackgroundRecordingsDuringTheaterMode:
- _objc_msgSend$_setBackgroundRecordingsEnabled:
- _objc_msgSend$_setOxygenSaturationDisabled:
- _objc_msgSend$_settingsToObserve
- _objc_msgSend$_startObservingDefaults
- _objc_msgSend$_stopObservingAllDefaults
- _objc_msgSend$hasCompletedOnboarding
- _objc_msgSend$init
- _objc_msgSend$initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:didStart:
- _objc_msgSend$onboardingCache
- _objc_msgSend$setHasCompletedOnboarding:
- _objc_msgSend$setObject:forKey:
- _objc_opt_isKindOfClass
- _objc_retain_x25
- _objc_retain_x27
CStrings:
- "@\"<HKFeatureAvailabilityProviding>\""
- "@\"HKRPOxygenSaturationOnboardingCache\""
- "@\"HKRPOxygenSaturationOnboardingCache\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@?40"
- "HKFeatureAvailabilityProvidingObserver"
- "HKRPOxygenSaturationOnboardingCache"
- "HKRPOxygenSaturationOnboardingCacher"
- "HasCompletedOnboarding"
- "T@\"HKRPOxygenSaturationOnboardingCache\",R,N"
- "T@\"NSNumber\",C,N"
- "[%{public}@] Can't determine if the current onboarding version is compatible: %{public}@"
- "[%{public}@] Checking for updated feature availability information."
- "[%{public}@] Registered for feature availability changes"
- "[%{public}@] Setting has completed onboarding: %{public}@"
- "[%{public}@] We've onboarded."
- "_notifySettingsDidChange"
- "_onboardingCache"
- "_queue"
- "_queue_featureAvailabilityDidChange"
- "_setBackgroundRecordingsDuringSleepMode:"
- "_setBackgroundRecordingsDuringTheaterMode:"
- "_setBackgroundRecordingsEnabled:"
- "_setOxygenSaturationDisabled:"
- "_settingsToObserve"
- "_startObservingDefaults"
- "_stopObservingAllDefaults"
- "featureAvailabilityProvidingDidUpdateOnboardingCompletion:"
- "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
- "featureAvailabilityProvidingDidUpdateSettings:"
- "hasCompletedOnboarding"
- "initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:"
- "initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:didStart:"
- "onboardingCache"
- "queue"
- "setHasCompletedOnboarding:"
- "setObject:forKey:"
- "v24@0:8@\"<HKFeatureAvailabilityProviding>\"16"

```
