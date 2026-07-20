## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/Versions/A/HealthKit`

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
-  __TEXT.__text: 0x40cb34
-  __TEXT.__objc_methlist: 0x30ec4
-  __TEXT.__cstring: 0x35552
-  __TEXT.__const: 0x1a9fc
-  __TEXT.__oslogstring: 0xc763
-  __TEXT.__gcc_except_tab: 0x388c
+7027.0.67.1.1
+  __TEXT.__text: 0x40e6e0
+  __TEXT.__objc_methlist: 0x30f14
+  __TEXT.__cstring: 0x356c2
+  __TEXT.__const: 0x1aa1c
+  __TEXT.__oslogstring: 0xc993
+  __TEXT.__gcc_except_tab: 0x38c4
   __TEXT.__dlopen_cstrs: 0x1a8
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
-  __TEXT.__unwind_info: 0x12d98
-  __TEXT.__eh_frame: 0x79a8
+  __TEXT.__unwind_info: 0x12e08
+  __TEXT.__eh_frame: 0x7a40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x808
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a48
+  __DATA_CONST.__objc_selrefs: 0x11a78
   __DATA_CONST.__objc_protorefs: 0x630
   __DATA_CONST.__objc_superrefs: 0x1788
   __DATA_CONST.__objc_arraydata: 0x69d0
   __DATA_CONST.__got: 0x1d30
-  __AUTH_CONST.__const: 0x1b9d1
-  __AUTH_CONST.__cfstring: 0x32f80
-  __AUTH_CONST.__objc_const: 0x52830
+  __AUTH_CONST.__const: 0x1ba19
+  __AUTH_CONST.__cfstring: 0x33260
+  __AUTH_CONST.__objc_const: 0x52898
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x43f8
   __AUTH_CONST.__objc_arrayobj: 0x768

   __AUTH_CONST.__auth_got: 0x1e10
   __AUTH.__objc_data: 0xeff8
   __AUTH.__data: 0x34f0
-  __DATA.__objc_ivar: 0x2f44
-  __DATA.__data: 0xf970
+  __DATA.__objc_ivar: 0x2f4c
+  __DATA.__data: 0xf980
   __DATA.__bss: 0x320e0
   __DATA.__common: 0x7b8
   __DATA_DIRTY.__objc_data: 0x2788

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 29368
-  Symbols:   41426
-  CStrings:  8609
+  Functions: 29400
+  Symbols:   41443
+  CStrings:  8640
 
Symbols:
+ -[HKFeatureStatusManager _dataSourceIfAvailable]
+ -[HKHealthStore _setCharacteristic:forDataType:date:error:]
+ -[HKHealthStoreImplementation _setCharacteristic:forDataType:date:error:]
+ -[HKSource _researchStudyIconData]
+ -[HKSource _setResearchStudyIconData:]
+ -[HKStatistics discrepancyDescriptionComparedTo:]
+ -[_HKFeatureFlags timeBoundedAuthorizationInLineButtons]
+ GCC_except_table283
+ GCC_except_table287
+ OBJC_IVAR_$_HKSource._researchStudyIconData
+ OBJC_IVAR_$__HKFeatureFlags._timeBoundedAuthorizationInLineButtons
+ _HKQuantityDeltaDescription
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ ___56-[_HKFeatureFlags timeBoundedAuthorizationInLineButtons]_block_invoke
+ ___73-[HKHealthStoreImplementation _setCharacteristic:forDataType:date:error:]_block_invoke
+ ___73-[HKHealthStoreImplementation _setCharacteristic:forDataType:date:error:]_block_invoke_2
+ _objc_msgSend$_setCharacteristic:forDataType:date:error:
+ _objc_msgSend$remote_setCharacteristic:forDataType:date:handler:
- -[HKFeatureStatusManager _requirementSatisfactionOverrides]
- GCC_except_table284
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
