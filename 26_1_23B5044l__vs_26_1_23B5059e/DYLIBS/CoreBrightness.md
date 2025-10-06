## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2079.40.16.0.0
-  __TEXT.__text: 0x1c4d0c
+2079.40.22.0.1
+  __TEXT.__text: 0x1c5a34
   __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x98ac
-  __TEXT.__cstring: 0xe365
-  __TEXT.__const: 0x10944
-  __TEXT.__oslogstring: 0x15759
-  __TEXT.__gcc_except_tab: 0x21dc
+  __TEXT.__objc_methlist: 0x99ac
+  __TEXT.__cstring: 0xe3be
+  __TEXT.__const: 0x1094c
+  __TEXT.__oslogstring: 0x157d4
+  __TEXT.__gcc_except_tab: 0x21d0
   __TEXT.__dlopen_cstrs: 0x1d5
-  __TEXT.__unwind_info: 0x3510
-  __TEXT.__objc_classname: 0xe88
-  __TEXT.__objc_methname: 0x14140
-  __TEXT.__objc_methtype: 0x4c4e
-  __TEXT.__objc_stubs: 0xf0a0
+  __TEXT.__unwind_info: 0x3520
+  __TEXT.__objc_classname: 0xeb1
+  __TEXT.__objc_methname: 0x14378
+  __TEXT.__objc_methtype: 0x4d0a
+  __TEXT.__objc_stubs: 0xf2c0
   __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x2380
-  __DATA_CONST.__objc_classlist: 0x500
+  __DATA_CONST.__const: 0x23d0
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47e8
+  __DATA_CONST.__objc_selrefs: 0x4870
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x4b0
-  __DATA_CONST.__objc_arraydata: 0x900
+  __DATA_CONST.__objc_superrefs: 0x4c0
+  __DATA_CONST.__objc_arraydata: 0x990
   __AUTH_CONST.__auth_got: 0xb18
   __AUTH_CONST.__const: 0xa50
-  __AUTH_CONST.__cfstring: 0xc920
-  __AUTH_CONST.__objc_const: 0x1f760
+  __AUTH_CONST.__cfstring: 0xca40
+  __AUTH_CONST.__objc_const: 0x1fdd8
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__objc_intobj: 0xb40
-  __AUTH_CONST.__objc_arrayobj: 0x2a0
+  __AUTH_CONST.__objc_intobj: 0xb88
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_floatobj: 0x140
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH.__objc_data: 0xc30
-  __DATA.__objc_ivar: 0x13f0
-  __DATA.__data: 0x2d0c0
+  __AUTH.__objc_data: 0xca8
+  __DATA.__objc_ivar: 0x142c
+  __DATA.__data: 0x2d0c8
   __DATA.__bss: 0x3b0
-  __DATA_DIRTY.__objc_data: 0x25d0
+  __DATA_DIRTY.__objc_data: 0x25f8
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x138
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FA072B7-B0CF-345E-AFF2-DD38EDD8200F
-  Functions: 5482
-  Symbols:   17340
-  CStrings:  10202
+  UUID: 2AE6432C-DF28-3EC9-8679-94787ACAC4C4
+  Functions: 5504
+  Symbols:   17436
+  CStrings:  10263
 
Symbols:
+ +[CBAnalytics alsSelectionLuxTimeHistogram:forALSIndex:]
+ -[ALSSelectionStats calculateIndexForOrientation:placement:]
+ -[ALSSelectionStats dealloc]
+ -[ALSSelectionStats init]
+ -[ALSSelectionStats recordALSSwapWithOrientation:andPlacement:andLux:]
+ -[ALSSelectionStats recordTimeForCurrentALS]
+ -[ALSSelectionStats recordTime]
+ -[ALSSelectionStats resetStats]
+ -[ALSSelectionStats submit]
+ -[ALSSelectionStats updateStatsDisplayOff]
+ -[ALSSelectionStats updateStatsWithOrientation:andLux:andPlacement:]
+ -[ALSSelectionStats updateTimeWithOrientation:andPlacement:andLux:]
+ -[ALSSelectionStats validateOrientation:]
+ -[ALSSelectionStats validatePlacement:]
+ -[CBAppliedCompensations blrComp]
+ -[CBAppliedCompensations blrEnabled]
+ -[CBAppliedCompensations compensationFor:andMax:]
+ -[CBAppliedCompensations copyStatusInfo]
+ -[CBAppliedCompensations dealloc]
+ -[CBAppliedCompensations harmonyComp]
+ -[CBAppliedCompensations harmonyEnabled]
+ -[CBAppliedCompensations initWithRampManager:maxHarmony:maxBLR:]
+ -[CBAppliedCompensations setBlrEnabled:]
+ -[CBAppliedCompensations setHarmonyEnabled:]
+ GCC_except_table135
+ GCC_except_table263
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table306
+ GCC_except_table312
+ GCC_except_table321
+ GCC_except_table339
+ GCC_except_table351
+ GCC_except_table353
+ GCC_except_table371
+ GCC_except_table375
+ GCC_except_table388
+ GCC_except_table392
+ GCC_except_table395
+ GCC_except_table405
+ GCC_except_table411
+ GCC_except_table455
+ GCC_except_table470
+ GCC_except_table476
+ GCC_except_table490
+ GCC_except_table515
+ GCC_except_table528
+ GCC_except_table75
+ _BLR_COMPENSATION_RAMP
+ _HARMONY_COMPENSATION_RAMP
+ _OBJC_CLASS_$_ALSSelectionStats
+ _OBJC_CLASS_$_CBAppliedCompensations
+ _OBJC_IVAR_$_ALSSelectionStats.currentALSOrientation
+ _OBJC_IVAR_$_ALSSelectionStats.currentALSPlacement
+ _OBJC_IVAR_$_ALSSelectionStats.currentLux
+ _OBJC_IVAR_$_ALSSelectionStats.deltas
+ _OBJC_IVAR_$_ALSSelectionStats.lastEvalTime
+ _OBJC_IVAR_$_ALSSelectionStats.luxTimeHistograms
+ _OBJC_IVAR_$_ALSSelectionStats.nSwaps
+ _OBJC_IVAR_$_ALSSelectionStats.samples
+ _OBJC_IVAR_$_ALSSelectionStats.startTime
+ _OBJC_IVAR_$_ALSSelectionStats.time
+ _OBJC_IVAR_$_CBAppliedCompensations._blrComp
+ _OBJC_IVAR_$_CBAppliedCompensations._blrEnabled
+ _OBJC_IVAR_$_CBAppliedCompensations._harmonyComp
+ _OBJC_IVAR_$_CBAppliedCompensations._harmonyEnabled
+ _OBJC_IVAR_$_CBAppliedCompensations._maxBLR
+ _OBJC_IVAR_$_CBAppliedCompensations._maxHarmony
+ _OBJC_IVAR_$_CBAppliedCompensations._rampManager
+ _OBJC_IVAR_$_CBDisplayContaineriOS._cachedABPref
+ _OBJC_IVAR_$_CBDisplayModuleiOS._appliedCompensations
+ _OBJC_METACLASS_$_ALSSelectionStats
+ _OBJC_METACLASS_$_CBAppliedCompensations
+ __OBJC_$_INSTANCE_METHODS_ALSSelectionStats
+ __OBJC_$_INSTANCE_METHODS_CBAppliedCompensations
+ __OBJC_$_INSTANCE_VARIABLES_ALSSelectionStats
+ __OBJC_$_INSTANCE_VARIABLES_CBAppliedCompensations
+ __OBJC_$_PROP_LIST_CBAppliedCompensations
+ __OBJC_$_PROTOCOL_REFS_CBRampManagerI
+ __OBJC_CLASS_RO_$_ALSSelectionStats
+ __OBJC_CLASS_RO_$_CBAppliedCompensations
+ __OBJC_METACLASS_RO_$_ALSSelectionStats
+ __OBJC_METACLASS_RO_$_CBAppliedCompensations
+ ___40-[CBAppliedCompensations setBlrEnabled:]_block_invoke
+ ___44-[CBAppliedCompensations setHarmonyEnabled:]_block_invoke
+ ___51-[CBDisplayModuleiOS initWithBacklight:andContext:]_block_invoke.26
+ ___51-[CBDisplayModuleiOS initWithBacklight:andContext:]_block_invoke.32
+ ___51-[CBDisplayModuleiOS initWithBacklight:andContext:]_block_invoke_2.33
+ ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.371
+ ___56+[CBAnalytics alsSelectionLuxTimeHistogram:forALSIndex:]_block_invoke
+ ___56+[CBAnalytics alsSelectionLuxTimeHistogram:forALSIndex:]_block_invoke_2
+ ___68-[ALSSelectionStats updateStatsWithOrientation:andLux:andPlacement:]_block_invoke
+ ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.742
+ ___block_descriptor_48_e8_32o_e34_v32?0Q8"NSString"16"NSNumber"24ls32l8
+ ___block_descriptor_64_e8_32o40o_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_literal_global.1043
+ ___block_literal_global.478
+ ___block_literal_global.574
+ ___block_literal_global.723
+ ___block_literal_global.92
+ _kCBBrightnessCapToCA
+ _objc_msgSend$alsSelectionLuxTimeHistogram:forALSIndex:
+ _objc_msgSend$blrComp
+ _objc_msgSend$blrEnabled
+ _objc_msgSend$calculateIndexForOrientation:placement:
+ _objc_msgSend$compensationFor:andMax:
+ _objc_msgSend$harmonyComp
+ _objc_msgSend$harmonyEnabled
+ _objc_msgSend$initWithRampManager:maxHarmony:maxBLR:
+ _objc_msgSend$recordALSSwapWithOrientation:andPlacement:andLux:
+ _objc_msgSend$recordTime
+ _objc_msgSend$recordTimeForCurrentALS
+ _objc_msgSend$resetStats
+ _objc_msgSend$setBlrEnabled:
+ _objc_msgSend$setHarmonyEnabled:
+ _objc_msgSend$updateStatsDisplayOff
+ _objc_msgSend$updateStatsWithOrientation:andLux:andPlacement:
+ _objc_msgSend$updateTimeWithOrientation:andPlacement:andLux:
+ _objc_msgSend$validateOrientation:
+ _objc_msgSend$validatePlacement:
- -[CBDisplayModuleiOS computeBrightnessCompensation]
- -[CBDisplayModuleiOS setAppliedCompensation:]
- -[CBEDR appliedCompensation]
- -[CBEDR setAppliedCompensation:]
- GCC_except_table221
- GCC_except_table264
- GCC_except_table301
- GCC_except_table303
- GCC_except_table313
- GCC_except_table322
- GCC_except_table340
- GCC_except_table352
- GCC_except_table354
- GCC_except_table372
- GCC_except_table376
- GCC_except_table389
- GCC_except_table393
- GCC_except_table396
- GCC_except_table400
- GCC_except_table407
- GCC_except_table456
- GCC_except_table471
- GCC_except_table478
- GCC_except_table491
- GCC_except_table516
- GCC_except_table529
- _DEFAULT_COMPENSATION
- _OBJC_IVAR_$_CBDisplayModuleiOS._appliedBLRComp
- _OBJC_IVAR_$_CBDisplayModuleiOS._appliedComp
- _OBJC_IVAR_$_CBDisplayModuleiOS._appliedHarmonyComp
- _OBJC_IVAR_$_CBEDR._appliedCompensation
- __ZL21BLR_COMPENSATION_RAMP
- __ZL25HARMONY_COMPENSATION_RAMP
- ___51-[CBDisplayModuleiOS initWithBacklight:andContext:]_block_invoke.22
- ___51-[CBDisplayModuleiOS initWithBacklight:andContext:]_block_invoke.28
- ___51-[CBDisplayModuleiOS initWithBacklight:andContext:]_block_invoke_2.29
- ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.370
- ___60-[CBDisplayModuleiOS handleNotificationForKey:withProperty:]_block_invoke
- ___60-[CBDisplayModuleiOS handleNotificationForKey:withProperty:]_block_invoke.177
- ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.741
- ____ZN4AABC24_UpdateAggregateFunctionEP20__IOHIDServiceClientPNS_3ALSE_block_invoke
- ___block_literal_global.1042
- ___block_literal_global.464
- ___block_literal_global.560
- ___block_literal_global.709
- ___block_literal_global.88
- _objc_msgSend$computeBrightnessCompensation
- _objc_msgSend$setAppliedCompensation:
CStrings:
+ "%s: r.policy: %lu | h.max: %f | h.ref=%f | h.req: %f | SDR: %f | cap: %f | p.max: %f | sec.per.stop: %f | sec.per.stop.exit: %f"
+ ".ALS.LuxTime"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B-3qugC1FzNUesOJcGaFomg9uCGrwZJQBGE1k2c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "@\"<CBRampManagerI>\""
+ "@\"CBAppliedCompensations\""
+ "@40@0:8@16d24d32"
+ "ALS is not supported on this device or not yet registered-> re-apply the DisplayBrightnessAuto property when the ALS service comes up"
+ "ALS service is now ready - re-applying cached DisplayBrightnessAuto property"
+ "ALSSelectionStats"
+ "BLRComp"
+ "BLREnabled"
+ "CBAppliedCompensations"
+ "HarmonyComp"
+ "HarmonyEnabled"
+ "MaxBLRComp"
+ "MaxHarmonyComp"
+ "TB,N,V_blrEnabled"
+ "TB,N,V_harmonyEnabled"
+ "Td,R,V_blrComp"
+ "Td,R,V_harmonyComp"
+ "[12d]"
+ "[18@\"CBHistogramBuilder\"]"
+ "[18d]"
+ "_appliedCompensations"
+ "_blrComp"
+ "_cachedABPref"
+ "_harmonyComp"
+ "_maxBLR"
+ "_maxHarmony"
+ "alsIndex"
+ "alsSelectionLuxTimeHistogram:forALSIndex:"
+ "blrComp"
+ "blrEnabled"
+ "calculateIndexForOrientation:placement:"
+ "compensationFor:andMax:"
+ "currentALSOrientation"
+ "currentALSPlacement"
+ "d32@0:8d16d24"
+ "deltas"
+ "harmonyComp"
+ "harmonyEnabled"
+ "i20@0:8i16"
+ "i24@0:8i16i20"
+ "initWithRampManager:maxHarmony:maxBLR:"
+ "kCBBrightnessCapToCA"
+ "lastEvalTime"
+ "luxBin"
+ "luxTimeHistograms"
+ "nSwaps"
+ "recordALSSwapWithOrientation:andPlacement:andLux:"
+ "recordTime"
+ "recordTimeForCurrentALS"
+ "resetStats"
+ "setBlrEnabled:"
+ "setHarmonyEnabled:"
+ "updateStatsDisplayOff"
+ "updateStatsWithOrientation:andLux:andPlacement:"
+ "updateTimeWithOrientation:andPlacement:andLux:"
+ "v28@0:8i16f20i24"
+ "v28@0:8i16i20f24"
+ "v32@0:8@16q24"
+ "validateOrientation:"
+ "validatePlacement:"
- "%s: r.policy: %lu | h.max: %f | h.ref=%f | h.req: %f | SDR: %f | cap: %f | p.max: %f | a.comp: %f | sec.per.stop: %f | sec.per.stop.exit: %f"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B9sPugClFQ8-BwpXNzydTm7PXvLYXZt31CRMEnM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "ALS is not supported on this device -> ignore setting of DisplayBrightnessAuto property"
- "AppliedCompensation"
- "Tf,N"
- "Tf,V_appliedCompensation"
- "_appliedBLRComp"
- "_appliedComp"
- "_appliedCompensation"
- "_appliedHarmonyComp"
- "computeBrightnessCompensation"
- "setAppliedCompensation:"

```
