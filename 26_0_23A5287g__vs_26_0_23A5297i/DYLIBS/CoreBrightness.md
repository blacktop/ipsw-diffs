## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2079.0.27.0.0
-  __TEXT.__text: 0x1c255c
+2079.0.34.0.0
+  __TEXT.__text: 0x1c3e0c
   __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x982c
-  __TEXT.__cstring: 0xe288
+  __TEXT.__objc_methlist: 0x9854
+  __TEXT.__cstring: 0xe2ee
   __TEXT.__const: 0x104dc
-  __TEXT.__oslogstring: 0x15494
-  __TEXT.__gcc_except_tab: 0x21e0
+  __TEXT.__oslogstring: 0x156e1
+  __TEXT.__gcc_except_tab: 0x21dc
   __TEXT.__dlopen_cstrs: 0x1d5
-  __TEXT.__unwind_info: 0x34f0
+  __TEXT.__unwind_info: 0x3508
   __TEXT.__objc_classname: 0xe88
-  __TEXT.__objc_methname: 0x13fce
-  __TEXT.__objc_methtype: 0x4bdd
-  __TEXT.__objc_stubs: 0xefe0
+  __TEXT.__objc_methname: 0x1407e
+  __TEXT.__objc_methtype: 0x4c4e
+  __TEXT.__objc_stubs: 0xf000
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x2380
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47a8
+  __DATA_CONST.__objc_selrefs: 0x47c0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x900
   __AUTH_CONST.__auth_got: 0xb18
   __AUTH_CONST.__const: 0xa50
-  __AUTH_CONST.__cfstring: 0xc820
-  __AUTH_CONST.__objc_const: 0x1f650
+  __AUTH_CONST.__cfstring: 0xc880
+  __AUTH_CONST.__objc_const: 0x1f6b0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_floatobj: 0x140
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x13d4
+  __DATA.__objc_ivar: 0x13e0
   __DATA.__data: 0x2d0b0
   __DATA.__bss: 0x3b0
   __DATA_DIRTY.__objc_data: 0x2670

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 897080FC-C365-3E6F-949F-1464CB5820D2
-  Functions: 5458
-  Symbols:   17276
-  CStrings:  10158
+  UUID: C326868F-0C1A-32E2-9C3C-76A7DB7F9870
+  Functions: 5472
+  Symbols:   17308
+  CStrings:  10178
 
Symbols:
+ -[CBColorModuleShared absoluteDifferenceForCurrentColor:andDeltaError:]
+ -[CBColorModuleShared setColorSensitivity:forALS:]
+ -[CBColorModuleShared updateSensorSensitivity:forValue:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table125
+ GCC_except_table137
+ GCC_except_table221
+ GCC_except_table264
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table309
+ GCC_except_table313
+ GCC_except_table322
+ GCC_except_table328
+ GCC_except_table340
+ GCC_except_table352
+ GCC_except_table354
+ GCC_except_table372
+ GCC_except_table376
+ GCC_except_table389
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table456
+ GCC_except_table471
+ GCC_except_table477
+ GCC_except_table478
+ GCC_except_table491
+ GCC_except_table516
+ GCC_except_table529
+ GCC_except_table75
+ _DisplaySetSliderScaler
+ _OBJC_IVAR_$_CBAODTransitionController._currentIndicatorBrightness
+ _OBJC_IVAR_$_CBAODTransitionController._currentIndicatorBrightnessLimit
+ _OBJC_IVAR_$_CBColorModuleShared._currentChromaticitySensitivity
+ __ZN4AABC20UpdateAmbrosiaFactorEf
+ __ZN4AABC29AmbrosiaReductionToUserSliderEf
+ __ZN4AABC29UserSliderToAmbrosiaReductionEf
+ ___104-[CBAODTransitionController startTransition:transitionParameters:rampDoneCallback:rampCanceledCallback:]_block_invoke.189
+ ___104-[CBAODTransitionController startTransition:transitionParameters:rampDoneCallback:rampCanceledCallback:]_block_invoke_2.202
+ ___104-[CBAODTransitionController startTransition:transitionParameters:rampDoneCallback:rampCanceledCallback:]_block_invoke_3.206
+ ___37-[CBColorModuleShared updateActivity]_block_invoke.233
+ ___51-[CBDisplayContaineriOS copyPreferenceForKey:user:]_block_invoke
+ ___51-[CBDisplayContaineriOS setPreference:forKey:user:]_block_invoke
+ ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.367
+ ___54-[CBIndicatorBrightnessModule startMonitoringForRTPLC]_block_invoke.65
+ ___55-[CBDisplayContaineriOS setNightShiftFactorDictionary:]_block_invoke
+ ___60-[CBSliderCommitTelemetry sendNotificationForKey:withValue:]_block_invoke
+ ___DisplaySetSliderScaler_block_invoke
+ ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.741
+ ___block_literal_global.1042
+ ___block_literal_global.189
+ ___block_literal_global.243
+ ___os_log_helper_16_0_14_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_4_0
+ _objc_msgSend$updateSensorSensitivity:forValue:
- GCC_except_table101
- GCC_except_table136
- GCC_except_table218
- GCC_except_table261
- GCC_except_table298
- GCC_except_table300
- GCC_except_table304
- GCC_except_table305
- GCC_except_table310
- GCC_except_table326
- GCC_except_table337
- GCC_except_table349
- GCC_except_table351
- GCC_except_table369
- GCC_except_table390
- GCC_except_table397
- GCC_except_table403
- GCC_except_table404
- GCC_except_table409
- GCC_except_table474
- GCC_except_table475
- GCC_except_table488
- GCC_except_table513
- GCC_except_table70
- GCC_except_table72
- GCC_except_table74
- ___104-[CBAODTransitionController startTransition:transitionParameters:rampDoneCallback:rampCanceledCallback:]_block_invoke.183
- ___104-[CBAODTransitionController startTransition:transitionParameters:rampDoneCallback:rampCanceledCallback:]_block_invoke_2.196
- ___104-[CBAODTransitionController startTransition:transitionParameters:rampDoneCallback:rampCanceledCallback:]_block_invoke_3.200
- ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.328
- ___54-[CBIndicatorBrightnessModule startMonitoringForRTPLC]_block_invoke.61
- ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.740
- ___block_literal_global.1041
- ___block_literal_global.188
- ___block_literal_global.234
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "B28@0:8f16^{__IOHIDServiceClient=}20"
+ "CBEDR statusInfo | AppliedCompensation=%.3f | AvailableHeadroom=%.3f | BrightnessCap=%.3f | HDRMax=%.3f | Headroom=%.3f | MaxHeadroom=%.3f | PanelMax=%.3f | RampPolicy=%lu | ReferenceHeadroom=%.3f | RequestedHeadroom=%.3f | SDR=%.3f | SecPerStop=%.3f | SecPerStopExit=%.3f | ModulatorEnabled=%d"
+ "IndicatorBrightness.Limit"
+ "MinimumIndicatorBrightnessCompensationFactor"
+ "RTPLC Cap (%f) < MIB (%f), this should never happen!"
+ "Scaling user slider. slider_value=%f ambrosia_factor=%f scaled=%f"
+ "SensorAbsoluteColorSensitivity"
+ "Updating Ambrosia reduction. ambrosia_factor=%f slider_value=%f"
+ "Updating MIB compensation factor: %f"
+ "_currentChromaticitySensitivity"
+ "_currentIndicatorBrightnessLimit"
+ "absoluteDifferenceForCurrentColor:andDeltaError:"
+ "difference in sensitivity too small (%f)"
+ "f32@0:8{?=ff}16{?=ff}24"
+ "invalid registry ID"
+ "sensor 0x%lX | current %f | new %f | diff %f"
+ "setColorSensitivity:forALS:"
+ "updateSensorSensitivity:forValue:"
+ "updating sensor sensitivity to %{public}@"
+ "v32@0:8^{__IOHIDServiceClient=}16^{__IOHIDEvent=}24"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B4AFugBUHDq4hoKXUyotBdvDzJNhnOc1qTg7Kxo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "CBEDR statusInfo: %@"
- "lux is 0, leave the values zeroed out"
- "update: lux=%f"

```
