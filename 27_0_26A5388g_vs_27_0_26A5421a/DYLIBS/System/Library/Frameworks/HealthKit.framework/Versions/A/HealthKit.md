## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/Versions/A/HealthKit`

```diff

-7027.0.67.1.1
-  __TEXT.__text: 0x40e6e0
-  __TEXT.__objc_methlist: 0x30f14
-  __TEXT.__cstring: 0x356c2
+7027.0.72.1.1
+  __TEXT.__text: 0x40ed50
+  __TEXT.__objc_methlist: 0x30f44
+  __TEXT.__cstring: 0x35752
   __TEXT.__const: 0x1aa1c
-  __TEXT.__oslogstring: 0xc993
-  __TEXT.__gcc_except_tab: 0x38c4
+  __TEXT.__oslogstring: 0xc9e3
+  __TEXT.__gcc_except_tab: 0x38ec
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__ustring: 0x1d8
   __TEXT.__constg_swiftt: 0x569c
   __TEXT.__swift5_typeref: 0x5275
   __TEXT.__swift5_builtin: 0x53c
   __TEXT.__swift5_reflstr: 0x36bb
-  __TEXT.__swift5_fieldmd: 0x5314
+  __TEXT.__swift5_fieldmd: 0x5320
   __TEXT.__swift5_assocty: 0x1578
   __TEXT.__swift5_proto: 0x1954
   __TEXT.__swift5_types: 0x738

   __TEXT.__swift_as_cont: 0x354
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12e08
-  __TEXT.__eh_frame: 0x7a40
+  __TEXT.__unwind_info: 0x12e20
+  __TEXT.__eh_frame: 0x7a78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8738
+  __DATA_CONST.__const: 0x8748
   __DATA_CONST.__objc_classlist: 0x1b90
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x808
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a78
+  __DATA_CONST.__objc_selrefs: 0x11a98
   __DATA_CONST.__objc_protorefs: 0x630
   __DATA_CONST.__objc_superrefs: 0x1788
-  __DATA_CONST.__objc_arraydata: 0x69d0
-  __DATA_CONST.__got: 0x1d30
-  __AUTH_CONST.__const: 0x1ba19
-  __AUTH_CONST.__cfstring: 0x33260
-  __AUTH_CONST.__objc_const: 0x52898
+  __DATA_CONST.__objc_arraydata: 0x69e0
+  __DATA_CONST.__got: 0x1d20
+  __AUTH_CONST.__const: 0x1ba39
+  __AUTH_CONST.__cfstring: 0x332c0
+  __AUTH_CONST.__objc_const: 0x528f0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x43f8
+  __AUTH_CONST.__objc_intobj: 0x4410
   __AUTH_CONST.__objc_arrayobj: 0x768
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__auth_got: 0x1e10
   __AUTH.__objc_data: 0xeff8
   __AUTH.__data: 0x34f0
-  __DATA.__objc_ivar: 0x2f4c
+  __DATA.__objc_ivar: 0x2f50
   __DATA.__data: 0xf980
   __DATA.__bss: 0x320e0
   __DATA.__common: 0x7b8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 29400
-  Symbols:   41443
-  CStrings:  8640
+  Functions: 29407
+  Symbols:   41454
+  CStrings:  8644
 
Symbols:
+ -[HKMCPregnancyModel initWithState:pregnancyStartDate:pregnancyEndDate:estimatedDueDate:pregnancyDuration:physiologicalWashoutEndDate:behavioralWashoutEndDate:trimesters:sample:educationalStepsCompletedDate:staleOngoingPregnancySample:]
+ -[HKMCPregnancyModel staleOngoingPregnancySample]
+ GCC_except_table189
+ GCC_except_table282
+ GCC_except_table285
+ GCC_except_table288
+ GCC_except_table292
+ OBJC_IVAR_$_HKMCPregnancyModel._staleOngoingPregnancySample
+ _HKCategoryTypeIdentifierFitzpatrickSkinType
+ __93-[HKHealthStoreImplementation clientRemote_presentAuthorizationWithRequestRecord:completion:]_block_invoke_4
+ __HKDaemonPreferencesTCCReportUseThrottleDayOverrideKey
+ __OBJC_$_PROP_LIST__HKAuthorizationPresentationController
+ ___93-[HKHealthStoreImplementation clientRemote_presentAuthorizationWithRequestRecord:completion:]_block_invoke_2
+ ___93-[HKHealthStoreImplementation clientRemote_presentAuthorizationWithRequestRecord:completion:]_block_invoke_3
+ ___93-[HKHealthStoreImplementation clientRemote_presentAuthorizationWithRequestRecord:completion:]_block_invoke_4
+ _objc_msgSend$initWithState:pregnancyStartDate:pregnancyEndDate:estimatedDueDate:pregnancyDuration:physiologicalWashoutEndDate:behavioralWashoutEndDate:trimesters:sample:educationalStepsCompletedDate:staleOngoingPregnancySample:
+ _objc_msgSend$setPresentationDidFailHandler:
- GCC_except_table272
- GCC_except_table280
- GCC_except_table283
- GCC_except_table287
- _NSLocaleMeasurementSystem
- _NSLocaleMeasurementSystemMetric
CStrings:
+ "<%@:%p state:%@ | startDate:%@ | endDate:%@ | estimatedDueDate:%@ | duration:%@ | physiologicalWashoutEndDate:%@ | behavioralWashoutEndDate:%@ | trimesters:%@ | educationalStepsCompletedDate:%@ | sample:%@ | staleOngoingPregnancySample:%@ "
+ "Failed to end authorization session after presentation failure: %{public}@"
+ "HKCategoryTypeIdentifierFitzpatrickSkinType"
+ "HKTCCReportUseThrottleDayOverride"
+ "StaleOngoingPregnancySample"
- "<%@:%p state:%@ | startDate:%@ | endDate:%@ | estimatedDueDate:%@ | duration:%@ | physiologicalWashoutEndDate:%@ | behavioralWashoutEndDate:%@ | trimesters:%@ | educationalStepsCompletedDate:%@ | sample:%@ "
```
