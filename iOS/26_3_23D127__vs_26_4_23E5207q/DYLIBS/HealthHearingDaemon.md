## HealthHearingDaemon

> `/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x21b08
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x1af4
+6200.5.77.2.6
+  __TEXT.__text: 0x2268c
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0x1b14
   __TEXT.__const: 0x3f2
-  __TEXT.__cstring: 0x2302
+  __TEXT.__cstring: 0x21a4
   __TEXT.__oslogstring: 0x2a2b
-  __TEXT.__gcc_except_tab: 0x284
+  __TEXT.__gcc_except_tab: 0x28c
   __TEXT.__constg_swiftt: 0xd8
   __TEXT.__swift5_typeref: 0xbc
   __TEXT.__swift5_reflstr: 0xbd

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x788
+  __TEXT.__unwind_info: 0x798
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x6d0
-  __TEXT.__objc_methname: 0x7116
-  __TEXT.__objc_methtype: 0x11a4
-  __TEXT.__objc_stubs: 0x4aa0
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x650
+  __TEXT.__objc_classname: 0x711
+  __TEXT.__objc_methname: 0x72ca
+  __TEXT.__objc_methtype: 0x11cd
+  __TEXT.__objc_stubs: 0x4d00
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0x648
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17b8
+  __DATA_CONST.__objc_selrefs: 0x17c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x690
-  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__auth_got: 0x5e0
   __AUTH_CONST.__const: 0x310
   __AUTH_CONST.__cfstring: 0x1d20
-  __AUTH_CONST.__objc_const: 0x3058
+  __AUTH_CONST.__objc_const: 0x3060
   __AUTH_CONST.__objc_intobj: 0xe10
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x1b0
-  __DATA.__data: 0x910
+  __DATA.__data: 0x920
   __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x918
-  __DATA_DIRTY.__data: 0xc8
+  __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
+  - /System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures
   - /System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing
   - /System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E87F65BE-4119-372C-8D58-CD875380252E
-  Functions: 686
-  Symbols:   2695
-  CStrings:  1845
+  UUID: 68246BA3-0F96-36BB-BE2D-1B40E395D121
+  Functions: 702
+  Symbols:   2770
+  CStrings:  1839
 
Symbols:
+ +[HDAudioAnalyticsUtilities unboundedIntegerForLEQ:]
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ __OBJC_$_CATEGORY_HKCountrySet_$_HearingAid
+ __OBJC_$_CLASS_METHODS_HKCountrySet(HearingAid|HearingAidV2|HearingProtection|HearingProtectionPPE|HearingTest)
+ __PROTOCOLS__TtC19HealthHearingDaemon32HDHearingTestDailyAnalyticsEvent.2
+ ___87-[HDHeadphoneDoseManager _lock_updateCurrentDoseUsingStatisticsResult:assertion:error:]_block_invoke.452
+ ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.366
+ ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.366.cold.1
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.357
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.369
+ ___block_literal_global.371
+ ___block_literal_global.455
+ ___block_literal_global.510
+ ___block_literal_global.543
+ ___block_literal_global.568
+ ___block_literal_global.579
+ ___block_literal_global.608
+ _objc_msgSend$_creationDate
+ _objc_msgSend$activePairedDeviceProductType
+ _objc_msgSend$ageWithCurrentDate:error:
+ _objc_msgSend$areAllRequirementsSatisfied
+ _objc_msgSend$audiogramSampleType
+ _objc_msgSend$biologicalSexWithError:
+ _objc_msgSend$currentDate
+ _objc_msgSend$environmentDataSource
+ _objc_msgSend$featureStatusProviderForIdentifier:
+ _objc_msgSend$hardwareVersion
+ _objc_msgSend$healthDataSource
+ _objc_msgSend$highestPriorityUnsatisfiedRequirement
+ _objc_msgSend$isHearingTestCapable
+ _objc_msgSend$leftEarDiagnostic
+ _objc_msgSend$oldestSampleWithType:profile:encodingOptions:predicate:error:
+ _objc_msgSend$pairedDevicesWithError:
+ _objc_msgSend$predicateWithMetadataKey:exists:
+ _objc_msgSend$rightEarDiagnostic
+ _objc_msgSend$unboundedIntegerForLEQ:
+ _objc_retain_x9
- __OBJC_$_CATEGORY_HKCountrySet_$_HearingAidV2
- __OBJC_$_CLASS_METHODS_HKCountrySet(HearingAidV2|HearingProtectionPPE|HearingProtection|HearingTest|HearingAid)
- __PROTOCOLS__TtC19HealthHearingDaemon32HDHearingTestDailyAnalyticsEvent.5
- ___87-[HDHeadphoneDoseManager _lock_updateCurrentDoseUsingStatisticsResult:assertion:error:]_block_invoke.413
- ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.327
- ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.327.cold.1
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.318
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.338
- ___block_literal_global.471
- ___block_literal_global.504
- ___block_literal_global.529
- ___block_literal_global.540
- ___block_literal_global.569
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "F5C2DAD0-332F-481C-B7DE-7E80973B07BF"
+ "samplesMapWereRemoved:anchor:"
+ "unboundedIntegerForLEQ:"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "F5C2DAD0-38FB-4B3B-86D3-B264F4F8CBDA"

```
