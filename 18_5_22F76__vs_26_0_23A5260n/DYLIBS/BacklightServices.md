## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

```diff

-4.5.3.0.0
-  __TEXT.__text: 0x28320
+5.0.55.0.0
+  __TEXT.__text: 0x2872c
   __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x32d4
+  __TEXT.__objc_methlist: 0x3344
   __TEXT.__const: 0x1b8
-  __TEXT.__oslogstring: 0x2743
-  __TEXT.__cstring: 0x19d2
+  __TEXT.__oslogstring: 0x2782
+  __TEXT.__cstring: 0x19e1
   __TEXT.__ustring: 0xf4
-  __TEXT.__gcc_except_tab: 0xdcc
-  __TEXT.__unwind_info: 0xef0
+  __TEXT.__gcc_except_tab: 0xe0c
+  __TEXT.__unwind_info: 0xf48
   __TEXT.__objc_classname: 0x108e
-  __TEXT.__objc_methname: 0x5d94
-  __TEXT.__objc_methtype: 0x123b
-  __TEXT.__objc_stubs: 0x3da0
+  __TEXT.__objc_methname: 0x5f93
+  __TEXT.__objc_methtype: 0x1249
+  __TEXT.__objc_stubs: 0x3de0
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0xd80
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1480
+  __DATA_CONST.__objc_selrefs: 0x14b8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
   __AUTH_CONST.__auth_got: 0x4e8
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x21e0
-  __AUTH_CONST.__objc_const: 0x7890
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x2a0
+  __AUTH_CONST.__cfstring: 0x2200
+  __AUTH_CONST.__objc_const: 0x7958
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x2a8
   __DATA.__data: 0xba8
-  __DATA.__bss: 0xe1
-  __DATA_DIRTY.__objc_data: 0x1e00
-  __DATA_DIRTY.__bss: 0x88
+  __DATA.__bss: 0xd9
+  __DATA_DIRTY.__objc_data: 0x1db0
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2E2CD418-011F-3288-A6CB-EDE1196346B5
-  Functions: 1199
-  Symbols:   4428
-  CStrings:  2059
+  UUID: D5471FEF-52D1-32CC-AB4F-5942E1DBFBF8
+  Functions: 1214
+  Symbols:   4461
+  CStrings:  2077
 
Symbols:
+ -[BLSBacklightChangeEvent isEnvironmentTransitionAnimated]
+ -[BLSBacklightChangeEvent isTransitionForcedUnanimated]
+ -[BLSBacklightChangeEvent setTransitionForcedUnanimated:environmentTransitionAnimated:]
+ -[BLSBacklightFBSSceneEnvironment alwaysOnContentIs1hz]
+ -[BLSBacklightFBSSceneEnvironment setAlwaysOnContentIs1hz:]
+ -[BLSBacklightFBSSceneEnvironment setAlwaysOnContentIs1hz:].cold.1
+ -[FBSMutableSceneClientSettings(BacklightServices) bls_setAlwaysOnContentIs1hz:]
+ -[FBSSceneClientSettings(BacklightServices) bls_alwaysOnContentIs1hz]
+ GCC_except_table20
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table91
+ _OBJC_IVAR_$_BLSBacklightChangeEvent._environmentTransitionAnimated
+ _OBJC_IVAR_$_BLSBacklightChangeEvent._transitionForcedUnanimated
+ __ZN26BLSTimelineEntriesCombinerD2Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EclB8ne200100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EclB8ne200100Ev
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEE5clearB8ne200100Ev
+ __ZNSt3__114__split_bufferI26BLSTimelineEntryBookkeeperRNS_9allocatorIS1_EEE17__destruct_at_endB8ne200100EPS1_
+ __ZNSt3__116allocator_traitsINS_9allocatorI26BLSTimelineEntryBookkeeperEEE7destroyB8ne200100IS2_vLi0EEEvRS3_PT_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS3_EEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI26BLSTimelineEntryBookkeeperEEPS3_EEED2B8ne200100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI26BLSTimelineEntryBookkeeperEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE22__base_destruct_at_endB8ne200100EPS1_
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__19allocatorI24BLSTimelineEntryIteratorE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI26BLSTimelineEntryBookkeeperE17allocate_at_leastB8ne200100Em
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZZ115-[BLSAlwaysOnTimeline entryBookkeepersForDateInterval:shouldConstructStartEntry:framesPerSecond:previousSpecifier:]ENK3$_0clEP24BLSAlwaysOnTimelineEntryS1_
+ __ZnwmSt19__type_descriptor_t
+ ___59-[BLSBacklightFBSSceneEnvironment setAlwaysOnContentIs1hz:]_block_invoke
+ _objc_msgSend$bls_alwaysOnContentIs1hz
+ _objc_msgSend$bls_setAlwaysOnContentIs1hz:
- -[BLSAlwaysOnTimeline entryBookkeepersForDateInterval:shouldConstructStartEntry:framesPerSecond:previousSpecifier:].cold.1
- GCC_except_table16
- GCC_except_table55
- GCC_except_table64
- GCC_except_table65
- GCC_except_table70
- GCC_except_table78
- GCC_except_table82
- GCC_except_table86
- __ZN26BLSTimelineEntriesCombinerD1Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS2_EclB8ne190102Ev
- __ZNKSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112__destroy_atB8ne190102I26BLSTimelineEntryBookkeeperLi0EEEvPT_
- __ZNSt3__112construct_atB8ne190102I26BLSTimelineEntryBookkeeperJRKS1_EPS1_EEPT_S6_DpOT0_
- __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEE5clearB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEEPS3_EEED2B8ne190102Ev
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI24BLSTimelineEntryIteratorEES2_EEvRT_PT0_S7_S7_
- __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE21__push_back_slow_pathIS1_EEPS1_OT_
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE9push_backB8ne190102ERKS1_
- __ZNSt3__19allocatorI24BLSTimelineEntryIteratorE17allocate_at_leastB8ne190102Em
- __ZNSt3__19allocatorI26BLSTimelineEntryBookkeeperE17allocate_at_leastB8ne190102Em
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
CStrings:
+ "%p setAlwaysOnContentIs1hz:%{BOOL}u for environment:%{public}@"
+ "TB,N,Sbls_setAlwaysOnContentIs1hz:"
+ "TB,R,N,GisEnvironmentTransitionAnimated,V_environmentTransitionAnimated"
+ "TB,R,N,GisTransitionForcedUnanimated,V_transitionForcedUnanimated"
+ "_environmentTransitionAnimated"
+ "_transitionForcedUnanimated"
+ "alwaysOnContentIs1hz"
+ "aoContentIs1hz"
+ "bls_alwaysOnContentIs1hz"
+ "bls_setAlwaysOnContentIs1hz:"
+ "environmentTransitionAnimated"
+ "isEnvironmentTransitionAnimated"
+ "isTransitionForcedUnanimated"
+ "setAlwaysOnContentIs1hz:"
+ "setTransitionForcedUnanimated:environmentTransitionAnimated:"
+ "transitionForcedUnanimated"
+ "v24@0:8B16B20"

```
