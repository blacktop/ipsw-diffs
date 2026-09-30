## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2079.0.34.0.0
-  __TEXT.__text: 0x1c3e0c
+2079.0.39.0.0
+  __TEXT.__text: 0x1c4768
   __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x9854
-  __TEXT.__cstring: 0xe2ee
-  __TEXT.__const: 0x104dc
-  __TEXT.__oslogstring: 0x156e1
+  __TEXT.__objc_methlist: 0x98ac
+  __TEXT.__cstring: 0xe31e
+  __TEXT.__const: 0x102fc
+  __TEXT.__oslogstring: 0x15708
   __TEXT.__gcc_except_tab: 0x21dc
   __TEXT.__dlopen_cstrs: 0x1d5
-  __TEXT.__unwind_info: 0x3508
+  __TEXT.__unwind_info: 0x3510
   __TEXT.__objc_classname: 0xe88
-  __TEXT.__objc_methname: 0x1407e
+  __TEXT.__objc_methname: 0x14120
   __TEXT.__objc_methtype: 0x4c4e
-  __TEXT.__objc_stubs: 0xf000
+  __TEXT.__objc_stubs: 0xf0a0
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x2380
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47c0
+  __DATA_CONST.__objc_selrefs: 0x47e8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x900
   __AUTH_CONST.__auth_got: 0xb18
   __AUTH_CONST.__const: 0xa50
-  __AUTH_CONST.__cfstring: 0xc880
-  __AUTH_CONST.__objc_const: 0x1f6b0
+  __AUTH_CONST.__cfstring: 0xc8c0
+  __AUTH_CONST.__objc_const: 0x1f720
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_floatobj: 0x140
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x13e0
-  __DATA.__data: 0x2d0b0
+  __AUTH.__objc_data: 0xc30
+  __DATA.__objc_ivar: 0x13e8
+  __DATA.__data: 0x2d0c0
   __DATA.__bss: 0x3b0
-  __DATA_DIRTY.__objc_data: 0x2670
+  __DATA_DIRTY.__objc_data: 0x25d0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x138
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C326868F-0C1A-32E2-9C3C-76A7DB7F9870
-  Functions: 5472
-  Symbols:   17308
-  CStrings:  10178
+  UUID: 5202D2A5-13F3-3C85-9EBF-0A7D1DCF7551
+  Functions: 5482
+  Symbols:   17337
+  CStrings:  10192
 
Symbols:
+ -[CBALSNode getReportInterval]
+ -[CBColorFilter acknowledgeHIDEvent:from:]
+ -[CBColorFilter allValidALSEventsArrived]
+ -[CBColorFilter resetEvents]
+ -[CBDisplayModuleiOS appliedCompensation]
+ -[CBDisplayModuleiOS compensatedSDRNits]
+ -[CBDisplayModuleiOS setAppliedCompensation:]
+ GCC_except_table55
+ GCC_except_table78
+ _OBJC_IVAR_$_CBDisplayModuleiOS._appliedBLRComp
+ _OBJC_IVAR_$_CBDisplayModuleiOS._appliedHarmonyComp
+ __ZL21BLR_COMPENSATION_RAMP
+ __ZL25HARMONY_COMPENSATION_RAMP
+ ___42-[CBColorFilter acknowledgeHIDEvent:from:]_block_invoke
+ ___45-[CBDisplayContaineriOS setupInternalModules]_block_invoke.225
+ ___45-[CBDisplayContaineriOS setupInternalModules]_block_invoke_2.226
+ ___51-[CBDisplayContaineriOS setupInternalBrtCtlModules]_block_invoke.255
+ ___51-[CBDisplayContaineriOS setupInternalBrtCtlModules]_block_invoke_2.256
+ ___60-[CBDisplayContaineriOS handleCBBrtCtlDisplayContainerStart]_block_invoke.175
+ ___60-[CBDisplayContaineriOS handleCBBrtCtlDisplayContainerStart]_block_invoke_2.179
+ ___60-[CBDisplayModuleiOS handleNotificationForKey:withProperty:]_block_invoke
+ ___60-[CBDisplayModuleiOS handleNotificationForKey:withProperty:]_block_invoke.181
+ ___os_log_helper_16_0_13_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_4_0
+ ___os_log_helper_16_2_4_4_0_4_0_8_32_4_0
+ _objc_msgSend$acknowledgeHIDEvent:from:
+ _objc_msgSend$allValidALSEventsArrived
+ _objc_msgSend$appliedCompensation
+ _objc_msgSend$compensatedSDRNits
+ _objc_msgSend$resetEvents
- GCC_except_table47
- GCC_except_table49
- GCC_except_table75
- ___45-[CBDisplayContaineriOS setupInternalModules]_block_invoke.223
- ___45-[CBDisplayContaineriOS setupInternalModules]_block_invoke_2.225
- ___51-[CBDisplayContaineriOS setupInternalBrtCtlModules]_block_invoke.253
- ___51-[CBDisplayContaineriOS setupInternalBrtCtlModules]_block_invoke_2.255
- ___60-[CBDisplayContaineriOS handleCBBrtCtlDisplayContainerStart]_block_invoke.174
- ___60-[CBDisplayContaineriOS handleCBBrtCtlDisplayContainerStart]_block_invoke_2.178
- ___os_log_helper_16_0_14_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_4_0
- ___os_log_helper_16_2_3_4_0_4_0_8_32
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugAvzxv7IcdGc8G2SYbFVXSoM0LX2JB6i_Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "BLR_COMPENSATION_RAMP"
+ "CBEDR statusInfo | AvailableHeadroom=%.3f | BrightnessCap=%.3f | HDRMax=%.3f | Headroom=%.3f | MaxHeadroom=%.3f | PanelMax=%.3f | RampPolicy=%lu | ReferenceHeadroom=%.3f | RequestedHeadroom=%.3f | Compensated.SDR=%.3f | SecPerStop=%.3f | SecPerStopExit=%.3f | ModulatorEnabled=%d"
+ "HARMONY_COMPENSATION_RAMP"
+ "Reset color matrix for display id: %d"
+ "TI,R,N,V_orientation"
+ "TI,R,N,V_placement"
+ "Tf,N"
+ "_appliedBLRComp"
+ "_appliedHarmonyComp"
+ "acknowledgeHIDEvent:from:"
+ "allValidALSEventsArrived"
+ "compensatedSDRNits"
+ "getReportInterval"
+ "harmony available: %d (clamshell: %d | color ALS %s | overriden: %d)"
+ "resetEvents"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B5UAugATyt3H9EpWv9fXCFqH5sCsWWQRD4yZuH4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "CBEDR statusInfo | AppliedCompensation=%.3f | AvailableHeadroom=%.3f | BrightnessCap=%.3f | HDRMax=%.3f | Headroom=%.3f | MaxHeadroom=%.3f | PanelMax=%.3f | RampPolicy=%lu | ReferenceHeadroom=%.3f | RequestedHeadroom=%.3f | SDR=%.3f | SecPerStop=%.3f | SecPerStopExit=%.3f | ModulatorEnabled=%d"
- "Ti,R,N,V_placement"
- "harmony available: %d (clamshell: %d | color ALS %s)"

```
