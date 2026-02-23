## HealthMenstrualCycles

> `/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles`

```diff

-6200.5.77.2.6
-  __TEXT.__text: 0x2b648
+6200.5.81.2.2
+  __TEXT.__text: 0x2b748
   __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0x3314
   __TEXT.__const: 0x2b8
   __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__cstring: 0x3be9
+  __TEXT.__cstring: 0x3c25
   __TEXT.__oslogstring: 0x2223
   __TEXT.__ustring: 0x166
-  __TEXT.__unwind_info: 0xc08
-  __TEXT.__objc_classname: 0x7fc
-  __TEXT.__objc_methname: 0xb82d
+  __TEXT.__unwind_info: 0xc10
+  __TEXT.__objc_classname: 0x7fd
+  __TEXT.__objc_methname: 0xb853
   __TEXT.__objc_methtype: 0x1529
-  __TEXT.__objc_stubs: 0x54e0
-  __DATA_CONST.__got: 0x518
+  __TEXT.__objc_stubs: 0x5500
+  __DATA_CONST.__got: 0x520
   __DATA_CONST.__const: 0xe08
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f40
+  __DATA_CONST.__objc_selrefs: 0x1f48
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3200
-  __AUTH_CONST.__objc_const: 0x6040
+  __AUTH_CONST.__cfstring: 0x3220
+  __AUTH_CONST.__objc_const: 0x6060
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3e4
+  __DATA.__objc_ivar: 0x3e8
   __DATA.__data: 0xa88
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x960

   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE8CF188-3648-3E54-B69F-5BBC13B9F79A
-  Functions: 1182
-  Symbols:   4271
-  CStrings:  2673
+  UUID: 3546DE15-9E4D-32CD-932C-74FE549BC73B
+  Functions: 1184
+  Symbols:   4280
+  CStrings:  2677
 
Symbols:
+ -[HKMCViewModelProvider setActiveDayRange:].cold.2
+ _HKDayIndexRangeZero
+ _OBJC_IVAR_$_HKMCViewModelProvider._hasPerformedInitialFetch
+ _objc_msgSend$addIndexes:
Functions:
~ -[HKMCViewModelProvider _initWithDataSource:cycleFactorsDataSource:analysisProvider:maximumActiveDuration:minimumBufferDuration:prefetchDuration:shouldFetchCycleFactors:calendarCache:queue:] : 700 -> 720
~ -[HKMCViewModelProvider _copyWithDataSource:cycleFactorsDataSource:minimumBufferDuration:] : 424 -> 432
~ -[HKMCViewModelProvider setActiveDayRange:] : 420 -> 472
~ -[HKMCViewModelProvider _updateManagedDayRangeIfNeeded] : 792 -> 876
+ _OUTLINED_FUNCTION_1
~ -[HKMCViewModelProvider _initWithDataSource:cycleFactorsDataSource:analysisProvider:maximumActiveDuration:minimumBufferDuration:prefetchDuration:shouldFetchCycleFactors:calendarCache:queue:].cold.1 : 124 -> 92
~ -[HKMCViewModelProvider setActiveDayRange:].cold.1 : 224 -> 96
+ -[HKMCViewModelProvider setActiveDayRange:].cold.2
CStrings:
+ "!HKEqualDayIndexRanges(activeDayRange, HKDayIndexRangeZero)"
+ "_hasPerformedInitialFetch"
+ "addIndexes:"

```
