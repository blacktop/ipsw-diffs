## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

```diff

-5.2.1.0.0
-  __TEXT.__text: 0x28754
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x3344
-  __TEXT.__const: 0x1b8
-  __TEXT.__oslogstring: 0x2782
+5.4.2.0.0
+  __TEXT.__text: 0x28f3c
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0x334c
+  __TEXT.__const: 0x138
+  __TEXT.__oslogstring: 0x27ef
   __TEXT.__cstring: 0x19e1
   __TEXT.__ustring: 0xf4
-  __TEXT.__gcc_except_tab: 0xe0c
-  __TEXT.__unwind_info: 0xfd0
+  __TEXT.__gcc_except_tab: 0xde8
+  __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_classname: 0x108e
-  __TEXT.__objc_methname: 0x5f94
+  __TEXT.__objc_methname: 0x5fa4
   __TEXT.__objc_methtype: 0x1249
-  __TEXT.__objc_stubs: 0x3de0
+  __TEXT.__objc_stubs: 0x3e00
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0xd80
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14b8
+  __DATA_CONST.__objc_selrefs: 0x14c0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x4e8
+  __AUTH_CONST.__auth_got: 0x4b8
   __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__cfstring: 0x2200
   __AUTH_CONST.__objc_const: 0x7958
   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x2a8
   __DATA.__data: 0xba8
-  __DATA.__bss: 0xf9
+  __DATA.__bss: 0x109
   __DATA_DIRTY.__objc_data: 0x1860
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35661378-CADF-3ED2-A7A6-56669AD69B78
-  Functions: 1214
-  Symbols:   4465
-  CStrings:  2077
+  UUID: F3C228BA-D657-383F-B009-7AF27D0E6A66
+  Functions: 1239
+  Symbols:   4548
+  CStrings:  2079
 
Symbols:
+ +[BLSAlwaysOnTimeline timelineWithUpdateInterval:startDate:identifier:configure:].cold.1
+ -[NSDate(BacklightServices) bls_isValidDate]
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EclB9foe210106Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EclB9foe210106Ev
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEE5clearB9foe210106Ev
+ __ZNSt3__114__split_bufferI26BLSTimelineEntryBookkeeperRNS_9allocatorIS1_EEE17__destruct_at_endB9foe210106EPS1_
+ __ZNSt3__116allocator_traitsINS_9allocatorI26BLSTimelineEntryBookkeeperEEE7destroyB9foe210106IS2_Li0EEEvRS3_PT_
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS3_EEED2B9foe210106Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS3_EEED2B9foe210106Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe210106INS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe210106INS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE22__base_destruct_at_endB9foe210106EPS1_
+ __ZNSt3__19allocatorI24BLSTimelineEntryIteratorE17allocate_at_leastB9foe210106Em
+ __ZNSt3__19allocatorI26BLSTimelineEntryBookkeeperE17allocate_at_leastB9foe210106Em
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___block_literal_global.83
+ _objc_msgSend$bls_isValidDate
+ _objc_retain_x28
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EclB8ne200100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EclB8ne200100Ev
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEE5clearB8ne200100Ev
- __ZNSt3__114__split_bufferI26BLSTimelineEntryBookkeeperRNS_9allocatorIS1_EEE17__destruct_at_endB8ne200100EPS1_
- __ZNSt3__116allocator_traitsINS_9allocatorI26BLSTimelineEntryBookkeeperEEE7destroyB8ne200100IS2_vLi0EEEvRS3_PT_
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS3_EEED2B8ne200100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS3_EEED2B8ne200100Ev
- __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE22__base_destruct_at_endB8ne200100EPS1_
- __ZNSt3__19allocatorI24BLSTimelineEntryIteratorE17allocate_at_leastB8ne200100Em
- __ZNSt3__19allocatorI26BLSTimelineEntryBookkeeperE17allocate_at_leastB8ne200100Em
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___block_literal_global.81
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x8
CStrings:
+ "BLSAlwaysOnPeriodicTimeline invalid startDate (NaN or infinity) for identifier:%@ - returning empty timeline"
+ "bls_isValidDate"

```
