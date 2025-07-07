## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

```diff

-3.2.4.0.0
-  __TEXT.__text: 0x24ac8
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x28e8
-  __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x24fc
-  __TEXT.__cstring: 0x1823
+3.4.9.0.0
+  __TEXT.__text: 0x26944
+  __TEXT.__auth_stubs: 0x990
+  __TEXT.__objc_methlist: 0x28e0
+  __TEXT.__const: 0x98
+  __TEXT.__oslogstring: 0x24ec
+  __TEXT.__cstring: 0x1852
   __TEXT.__ustring: 0xac
-  __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__unwind_info: 0xbd4
-  __TEXT.__objc_classname: 0xf89
-  __TEXT.__objc_methname: 0x5d28
-  __TEXT.__objc_methtype: 0x1255
-  __TEXT.__objc_stubs: 0x3e00
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xbc0
+  __TEXT.__gcc_except_tab: 0x9e8
+  __TEXT.__unwind_info: 0xde8
+  __TEXT.__eh_frame: 0x38
+  __TEXT.__objc_classname: 0xf8d
+  __TEXT.__objc_methname: 0x5bf4
+  __TEXT.__objc_methtype: 0x1230
+  __TEXT.__objc_stubs: 0x3d00
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0xc18
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5758
-  __DATA_CONST.__objc_selrefs: 0x13b0
+  __DATA_CONST.__objc_selrefs: 0x1388
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x380
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __AUTH_CONST.__objc_const: 0x2b40
   __AUTH_CONST.__cfstring: 0x1f00
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__auth_got: 0x488
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__auth_got: 0x4e0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x388
-  __DATA.__objc_superrefs: 0x1a8
   __DATA.__objc_ivar: 0x284
   __DATA.__data: 0xc08
-  __DATA.__bss: 0x8c
+  __DATA.__bss: 0x94
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DA21E81-E322-3712-A57E-061C02CEB7A4
-  Functions: 1104
-  Symbols:   4079
-  CStrings:  1997
+  UUID: F51239B7-BF35-33EE-B868-BDFAC04E12F8
+  Functions: 1146
+  Symbols:   4213
+  CStrings:  1996
 
Symbols:
+ +[BLSAlwaysOnTimeline entriesCombinerForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:]
+ +[BLSAlwaysOnTimeline requestedFidelityForTimelines:inDateInterval:]
+ -[BLSAlwaysOnTimeline configureEntries:previousEntry:]
+ -[BLSAlwaysOnTimeline description]
+ -[BLSAlwaysOnTimeline entryBookkeepersForDateInterval:shouldConstructStartEntry:framesPerSecond:previousSpecifier:]
+ -[BLSAlwaysOnTimeline estimatedFidelityForPresentationTime:nextPresentationTime:]
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table14
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table81
+ GCC_except_table9
+ __ZN24BLSTimelineEntryIterator14entrySpecifierEv
+ __ZN24BLSTimelineEntryIterator20nextPresentationTimeEv
+ __ZN24BLSTimelineEntryIterator7advanceEv
+ __ZN26BLSTimelineEntriesCombiner13nextSpecifierEv
+ __ZN26BLSTimelineEntriesCombiner15entrySpecifiersEv
+ __ZN26BLSTimelineEntriesCombiner16computeNextEntryEv
+ __ZN26BLSTimelineEntriesCombiner24constructFrameSpecifiersEv
+ __ZN26BLSTimelineEntriesCombinerC2EONSt3__16vectorI24BLSTimelineEntryIteratorNS0_9allocatorIS2_EEEEP14NSDateIntervald
+ __ZN26BLSTimelineEntriesCombinerD1Ev
+ __ZN26BLSTimelineEntryBookkeeper24presentationTimeForIndexEm
+ __ZN26BLSTimelineEntryBookkeeper31entryFirstFramePresentationTimeEP24BLSAlwaysOnTimelineEntryd
+ __ZN26BLSTimelineEntryBookkeeper7advanceEv
+ __ZN26BLSTimelineEntryBookkeeperC2EP24BLSAlwaysOnTimelineEntryS1_d
+ __ZN26BLSTimelineEntryBookkeeperC2EP33BLSAlwaysOnTimelineEntrySpecifier
+ __ZN26BLSTimelineEntryBookkeeperD1Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEENS_16reverse_iteratorIPS2_EEEclB8ue170006Ev
+ __ZNKSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__112__destroy_atB8ue170006I26BLSTimelineEntryBookkeeperLi0EEEvPT_
+ __ZNSt3__112construct_atB8ue170006I26BLSTimelineEntryBookkeeperJRKS1_EPS1_EEPT_S6_DpOT0_
+ __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEE5clearB8ue170006Ev
+ __ZNSt3__114__split_bufferI24BLSTimelineEntryIteratorRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferI26BLSTimelineEntryBookkeeperRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI24BLSTimelineEntryIteratorEENS_16reverse_iteratorIPS3_EEEEED2B8ue170006Ev
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorI24BLSTimelineEntryIteratorEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorI26BLSTimelineEntryBookkeeperEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE21__push_back_slow_pathIS1_EEvOT_
+ __ZNSt3__16vectorI24BLSTimelineEntryIteratorNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE21__push_back_slow_pathIS1_EEvOT_
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
+ __ZNSt3__16vectorI26BLSTimelineEntryBookkeeperNS_9allocatorIS1_EEE9push_backB8ue170006ERKS1_
+ __ZNSt3__19allocatorI24BLSTimelineEntryIteratorE17allocate_at_leastB8ue170006Em
+ __ZNSt3__19allocatorI26BLSTimelineEntryBookkeeperE17allocate_at_leastB8ue170006Em
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ __ZSt9terminatev
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZZ115-[BLSAlwaysOnTimeline entryBookkeepersForDateInterval:shouldConstructStartEntry:framesPerSecond:previousSpecifier:]ENK3$_1clEP36BLSAlwaysOnTimelineUnconfiguredEntryU13block_pointerFP6NSDatevE
+ __ZZ115-[BLSAlwaysOnTimeline entryBookkeepersForDateInterval:shouldConstructStartEntry:framesPerSecond:previousSpecifier:]ENK3$_2clEP36BLSAlwaysOnTimelineUnconfiguredEntry
+ __ZZ86-[BLSAlwaysOnTimeline requestedFidelityForStartEntryInDateInterval:withPreviousEntry:]E12didFaultOnce
+ __ZdlPv
+ __Znwm
+ ___34-[BLSAlwaysOnTimeline description]_block_invoke
+ ___90-[BLSAlwaysOnFrequencyPerMinuteTimeline unconfiguredEntriesForDateInterval:previousEntry:]_block_invoke.54
+ ____ZZ115-[BLSAlwaysOnTimeline entryBookkeepersForDateInterval:shouldConstructStartEntry:framesPerSecond:previousSpecifier:]ENK3$_2clEP36BLSAlwaysOnTimelineUnconfiguredEntry_block_invoke
+ ____ZZ115-[BLSAlwaysOnTimeline entryBookkeepersForDateInterval:shouldConstructStartEntry:framesPerSecond:previousSpecifier:]ENK3$_2clEP36BLSAlwaysOnTimelineUnconfiguredEntry_block_invoke_2
+ ___assert_rtn
+ ___block_descriptor_40_ea8_32bs_e23_v28?0"NSDate"8B16^B20ls32l8
+ ___block_descriptor_40_ea8_32s_e13_"NSDate"8?0ls32l8
+ ___block_descriptor_40_ea8_32s_e23_B32?0"NSDate"8Q16^B24ls32l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s_e20_v24?0"NSDate"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s_e13_"NSDate"8?0ls32l8s56l8s40l8
+ ___block_literal_global.187
+ ___block_literal_global.95
+ ___clang_call_terminate
+ ___cxa_allocate_exception
+ ___cxa_begin_catch
+ ___cxa_free_exception
+ ___cxa_throw
+ ___gxx_personality_v0
+ _objc_msgSend$estimatedFidelityForPresentationTime:nextPresentationTime:
+ _objc_msgSend$isAfterDate:
+ _objc_msgSend$isBeforeDate:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$previousTimelineEntry
+ _objc_msgSend$requestedFidelityForTimelines:inDateInterval:
- +[BLSAlwaysOnTimeline coalesceSpecifiers:forDateInterval:framesPerSecond:previousSpecifier:]
- +[BLSAlwaysOnTimeline coalescedSpecifierFromEnumerator:forDateInterval:framesPerSecond:previousSpecifier:]
- +[BLSAlwaysOnTimeline uncoalescedFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:]
- -[BLSAlwaysOnFrameSpecifier initWithTimelineEntry:previousTimelineEntry:]
- -[BLSAlwaysOnTimeline configuredEntriesForDateInterval:previousEntry:shouldConstructStartEntry:]
- -[BLSAlwaysOnTimeline guessFidelityWhenUnspecifiedForUnconfiguredEntries:previousEntry:]
- _OBJC_CLASS_$_NSMutableDictionary
- ___139+[BLSAlwaysOnTimeline uncoalescedFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:]_block_invoke
- ___90-[BLSAlwaysOnFrequencyPerMinuteTimeline unconfiguredEntriesForDateInterval:previousEntry:]_block_invoke.56
- ___block_descriptor_32_e65_q24?0"BLSAlwaysOnFrameSpecifier"8"BLSAlwaysOnFrameSpecifier"16l
- ___block_descriptor_40_e8_32bs_e23_v28?0"NSDate"8B16^B20ls32l8
- ___block_descriptor_40_e8_32s_e23_B32?0"NSDate"8Q16^B24ls32l8
- ___block_descriptor_64_e8_32s40s48s_e20_v24?0"NSDate"8^B16ls32l8s40l8s48l8
- ___block_literal_global.186
- ___block_literal_global.82
- ___block_literal_global.96
- _objc_msgSend$allValues
- _objc_msgSend$coalesceSpecifiers:forDateInterval:framesPerSecond:previousSpecifier:
- _objc_msgSend$coalescedSpecifierFromEnumerator:forDateInterval:framesPerSecond:previousSpecifier:
- _objc_msgSend$configuredEntriesForDateInterval:previousEntry:shouldConstructStartEntry:
- _objc_msgSend$dictionary
- _objc_msgSend$initWithTimelineEntry:previousTimelineEntry:
- _objc_msgSend$mutableCopy
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$peekNextObject
- _objc_msgSend$peekingEnumerator
- _objc_msgSend$replaceObjectAtIndex:withObject:
- _objc_msgSend$setDidChange:
- _objc_msgSend$setObject:forKeyedSubscript:
- _objc_msgSend$uncoalescedFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:
CStrings:
+ "%p class:%{public}@ should override requestedFidelityForStartEntryInDateInterval:withPreviousEntry: to avoid brute force method for timeline:%{public}@"
+ "1 0"
+ "@\"NSDate\"8@?0"
+ "BLSTimelineEntriesCombiner_Project.hpp"
+ "T@\"NSString\",?,R,C"
+ "[specifiers count] > 0"
+ "configureEntries:previousEntry:"
+ "estimatedFidelityForPresentationTime:nextPresentationTime:"
+ "isAfterDate:"
+ "isBeforeDate:"
+ "nextSpecifier"
+ "objectAtIndexedSubscript:"
+ "performDesiredFidelityRequest desiredFidelity:%{public}@ for timelines:%{public}@"
+ "requestedFidelityForTimelines:inDateInterval:"
+ "success == true"
+ "vector"
- "%p nil timelineIdentifier for entrySpecifier:%{public}@ frameSpecifier:%{public}@"
- "@36@0:8@16@24B32"
- "@48@0:8@16@24d32@40"
- "allValues"
- "coalesceSpecifiers:forDateInterval:framesPerSecond:previousSpecifier:"
- "coalescedSpecifierFromEnumerator:forDateInterval:framesPerSecond:previousSpecifier:"
- "configuredEntriesForDateInterval:previousEntry:shouldConstructStartEntry:"
- "dictionary"
- "initWithTimelineEntry:previousTimelineEntry:"
- "mutableCopy"
- "objectForKeyedSubscript:"
- "performDesiredFidelityRequest desiredFidelity:%{public}@ for frameSpecifiers:%{public}@"
- "performDesiredFidelityRequest desiredFidelity:Minutes for empty frameSpecifiers"
- "q24@?0@\"BLSAlwaysOnFrameSpecifier\"8@\"BLSAlwaysOnFrameSpecifier\"16"
- "replaceObjectAtIndex:withObject:"
- "setObject:forKeyedSubscript:"
- "uncoalescedFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:"

```
