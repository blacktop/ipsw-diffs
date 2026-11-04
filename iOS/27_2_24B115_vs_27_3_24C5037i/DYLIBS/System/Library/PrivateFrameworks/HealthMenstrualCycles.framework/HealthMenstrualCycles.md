## HealthMenstrualCycles

> `/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x2e514
-  __TEXT.__objc_methlist: 0x380c
+7027.2.13.0.0
+  __TEXT.__text: 0x2eacc
+  __TEXT.__objc_methlist: 0x383c
   __TEXT.__const: 0x898
   __TEXT.__gcc_except_tab: 0x1c0
   __TEXT.__cstring: 0x4056
-  __TEXT.__oslogstring: 0x259d
+  __TEXT.__oslogstring: 0x25eb
   __TEXT.__ustring: 0x166
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x100

   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1100
+  __TEXT.__unwind_info: 0x1118
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xfc0
+  __DATA_CONST.__const: 0xfe8
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2178
+  __DATA_CONST.__objc_selrefs: 0x21a0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x5f0
   __AUTH_CONST.__const: 0x5e3
   __AUTH_CONST.__cfstring: 0x3440
-  __AUTH_CONST.__objc_const: 0x6920
+  __AUTH_CONST.__objc_const: 0x6988
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x470
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x490
+  __DATA.__objc_ivar: 0x49c
   __DATA.__data: 0xbe8
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1400
-  Symbols:   2633
-  CStrings:  610
+  Functions: 1409
+  Symbols:   2641
+  CStrings:  611
 
Symbols:
+ -[HKMCMenopauseModelProvider _handleQuery:updateWithError:]
+ -[HKMCMenopauseModelProvider _restartQueryIfPreviousQueryFailed]
+ -[HKMCViewModelProvider refetchDaySummariesIfPreviousFetchFailed]
+ -[HKMCViewModelProvider viewModelProviderDataSource:didFailToFetchDaySummariesInDayIndexRange:]
+ _HKMCMaximumMenstruationLengthDays
+ _OBJC_IVAR_$_HKMCMenopauseModelProvider._queryFailed
+ _OBJC_IVAR_$_HKMCViewModelProvider._dayIndexesToRefetchAfterRecovery
+ _OBJC_IVAR_$_HKMCViewModelProvider._failedDayIndexes
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- -[HKMCMenopauseModelProvider _handleQueryUpdateWithError:]
CStrings:
+ "[%{public}@:%p] Refetching summaries in range %{public}@ after a failed fetch"
```
