## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-7027.0.64.0.0
-  __TEXT.__text: 0x3f61dc
-  __TEXT.__objc_methlist: 0x31744
-  __TEXT.__cstring: 0x37b12
-  __TEXT.__const: 0x158b3c
-  __TEXT.__oslogstring: 0xd683
-  __TEXT.__gcc_except_tab: 0x3f24
+7027.0.67.2.1
+  __TEXT.__text: 0x3f7cc8
+  __TEXT.__objc_methlist: 0x31794
+  __TEXT.__cstring: 0x37c82
+  __TEXT.__const: 0x15bc4c
+  __TEXT.__oslogstring: 0xd8b3
+  __TEXT.__gcc_except_tab: 0x3f58
   __TEXT.__dlopen_cstrs: 0x644
-  __TEXT.__ustring: 0x78
+  __TEXT.__ustring: 0x1d8
   __TEXT.__constg_swiftt: 0x569c
   __TEXT.__swift5_typeref: 0x5275
   __TEXT.__swift5_builtin: 0x53c

   __TEXT.__swift5_proto: 0x1954
   __TEXT.__swift5_types: 0x738
   __TEXT.__swift5_capture: 0xed4
-  __TEXT.__swift_as_entry: 0x1ac
-  __TEXT.__swift_as_ret: 0x1b4
-  __TEXT.__swift_as_cont: 0x348
+  __TEXT.__swift_as_entry: 0x1b0
+  __TEXT.__swift_as_ret: 0x1b8
+  __TEXT.__swift_as_cont: 0x354
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x133b8
-  __TEXT.__eh_frame: 0x7a30
+  __TEXT.__unwind_info: 0x13430
+  __TEXT.__eh_frame: 0x7ac8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x848
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12020
+  __DATA_CONST.__objc_selrefs: 0x12050
   __DATA_CONST.__objc_protorefs: 0x640
   __DATA_CONST.__objc_superrefs: 0x17a8
   __DATA_CONST.__objc_arraydata: 0x69d0
   __DATA_CONST.__got: 0x1e18
-  __AUTH_CONST.__const: 0x13d81
-  __AUTH_CONST.__cfstring: 0x33540
-  __AUTH_CONST.__objc_const: 0x53468
+  __AUTH_CONST.__const: 0x13dc9
+  __AUTH_CONST.__cfstring: 0x33820
+  __AUTH_CONST.__objc_const: 0x534d0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x4698
   __AUTH_CONST.__objc_arrayobj: 0x768

   __AUTH_CONST.__auth_got: 0x2028
   __AUTH.__objc_data: 0xf2c8
   __AUTH.__data: 0x34e8
-  __DATA.__objc_ivar: 0x2f7c
-  __DATA.__data: 0xfda0
+  __DATA.__objc_ivar: 0x2f84
+  __DATA.__data: 0xfdb0
   __DATA.__bss: 0x32370
   __DATA.__common: 0xa00
   __DATA_DIRTY.__objc_data: 0x2738

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 29622
-  Symbols:   41709
-  CStrings:  9160
+  Functions: 29654
+  Symbols:   41723
+  CStrings:  9191
 
Symbols:
+ -[HKFeatureStatusManager _dataSourceIfAvailable]
+ -[HKHealthStore _setCharacteristic:forDataType:date:error:]
+ -[HKHealthStoreImplementation _setCharacteristic:forDataType:date:error:]
+ -[HKSource _researchStudyIconData]
+ -[HKSource _setResearchStudyIconData:]
+ -[HKStatistics discrepancyDescriptionComparedTo:]
+ -[_HKFeatureFlags timeBoundedAuthorizationInLineButtons]
+ GCC_except_table253
+ GCC_except_table257
+ _HKQuantityDeltaDescription
+ _OBJC_IVAR_$_HKSource._researchStudyIconData
+ _OBJC_IVAR_$__HKFeatureFlags._timeBoundedAuthorizationInLineButtons
+ ___56-[_HKFeatureFlags timeBoundedAuthorizationInLineButtons]_block_invoke
+ ___73-[HKHealthStoreImplementation _setCharacteristic:forDataType:date:error:]_block_invoke
+ ___73-[HKHealthStoreImplementation _setCharacteristic:forDataType:date:error:]_block_invoke_2
+ _objc_msgSend$_setCharacteristic:forDataType:date:error:
+ _objc_msgSend$remote_setCharacteristic:forDataType:date:handler:
- -[HKFeatureStatusManager _requirementSatisfactionOverrides]
- GCC_except_table254
- GCC_except_table93
CStrings:
+ "#### (180749116) 01. (HKLiveWorkoutBuilder *)associatedWorkoutBuilder"
+ "#### (180749116) 02. - (HKLiveWorkoutBuilder *)associatedWorkoutBuilderWithDevice:(nullable HKDevice *)device..."
+ "#### (180749116) 03. - (void)_setupTaskServerWithCompletion:(void (^)(BOOL success, NSError * _Nullable error))completion"
+ "#### (180749116) 15. - (void)clientRemote_didUpdateStatistics:(HKWorkoutBuilderStatistics *)builderStatistics"
+ "%@: %@→%@"
+ "%@: %g→%g %@ (Δ=%g, %.4f%%)"
+ "%@: date may not be nil in %@"
+ "<no differences>"
+ "Feature status data source is unavailable"
+ "TimeBoundedAuthorizationInLineButtons"
+ "VitalsDaySummaryDemoMode"
+ "[%{public}@] Data source unavailable; skipping feature status update"
+ "[%{public}@] Data source unavailable; skipping observation-driven update"
+ "avg"
+ "avgBySource differs"
+ "categoryValue: %@→%@"
+ "dataCount: %lu→%lu"
+ "dataCountBySource differs"
+ "dataType: %@→%@"
+ "durationBySource differs"
+ "earliestInterval: %@→%@"
+ "endDate: %@→%@"
+ "maxBySource differs"
+ "minBySource differs"
+ "mostRecentBySource differs"
+ "mostRecentInterval: %@→%@"
+ "other=nil"
+ "researchStudyIconData"
+ "sources differ"
+ "startDate: %@→%@"
+ "sumBySource differs"
```
