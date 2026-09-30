## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2079.60.14.502.2
-  __TEXT.__text: 0x1c5d28
-  __TEXT.__auth_stubs: 0x1610
-  __TEXT.__objc_methlist: 0x99e4
-  __TEXT.__cstring: 0xe31a
+2079.60.14.0.10
+  __TEXT.__text: 0x1c6248
+  __TEXT.__auth_stubs: 0x1620
+  __TEXT.__objc_methlist: 0x9a1c
+  __TEXT.__cstring: 0xe340
   __TEXT.__const: 0x10fb4
-  __TEXT.__oslogstring: 0x1576c
+  __TEXT.__oslogstring: 0x15770
   __TEXT.__gcc_except_tab: 0x21fc
   __TEXT.__dlopen_cstrs: 0x1d5
-  __TEXT.__unwind_info: 0x3528
+  __TEXT.__unwind_info: 0x3530
   __TEXT.__objc_classname: 0xebb
-  __TEXT.__objc_methname: 0x143cf
+  __TEXT.__objc_methname: 0x14459
   __TEXT.__objc_methtype: 0x4d5b
-  __TEXT.__objc_stubs: 0xf360
+  __TEXT.__objc_stubs: 0xf400
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x23d0
   __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4888
+  __DATA_CONST.__objc_selrefs: 0x48b0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x990
-  __AUTH_CONST.__auth_got: 0xb20
+  __AUTH_CONST.__auth_got: 0xb28
   __AUTH_CONST.__const: 0xa50
-  __AUTH_CONST.__cfstring: 0xca20
+  __AUTH_CONST.__cfstring: 0xca60
   __AUTH_CONST.__objc_const: 0x1fe18
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0xb88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7035830-D1E0-3837-B89E-EE327246906E
-  Functions: 5510
-  Symbols:   17461
-  CStrings:  10262
+  UUID: 4B77E7F3-89F8-39D3-BB82-396777F83641
+  Functions: 5515
+  Symbols:   17477
+  CStrings:  10271
 
Symbols:
+ -[CBIndicatorBrightnessModule calculateJumpTargetForFastStart]
+ -[CBIndicatorBrightnessModule determineJumpTarget]
+ -[CBIndicatorBrightnessModule handleRampDecisionForTargetIB:indicatorUpdatedOutsideOfRamp:]
+ -[CBIndicatorBrightnessModule jumpTo:]
+ -[CBIndicatorBrightnessModule shouldJumpToMIB]
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._jumpOnRestart
+ _log2
+ _objc_msgSend$calculateJumpTargetForFastStart
+ _objc_msgSend$determineJumpTarget
+ _objc_msgSend$handleRampDecisionForTargetIB:indicatorUpdatedOutsideOfRamp:
+ _objc_msgSend$jumpTo:
+ _objc_msgSend$shouldJumpToMIB
- _OBJC_IVAR_$_CBIndicatorBrightnessModule._jumpToTarget
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CBbvugBGRPDMDnmjOm7ePHQujRAIbIxGt2YwyVI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "CBRingLightEnabled"
+ "CBRingLightMinNits"
+ "Jumping to target indicator brightness: %f"
+ "_jumpOnRestart"
+ "calculateJumpTargetForFastStart"
+ "determineJumpTarget"
+ "handleRampDecisionForTargetIB:indicatorUpdatedOutsideOfRamp:"
+ "jumpTo:"
+ "shouldJumpToMIB"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/comp_ref_type.h:47: assertion !__comp_(__l, __r) failed: Comparator does not induce a strict weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h:40: assertion __len > 0 failed: The heap given to pop_heap must be non-empty\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h:88: assertion __len >= 2 failed: shouldn't be called unless __len >= 2\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:499: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:591: assertion __last - __first >= difference_type(3) failed: \n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:36: assertion (std::is_sorted<_RandomAccessIterator, _Comp_ref>(__first, __last, _Comp_ref(__comp))) failed: The range is not sorted after the sort, your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:50: assertion !__comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:52: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:59: assertion __comp(*(__first + __a), *(__first + __b)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__debug_utils/strict_weak_ordering_check.h:61: assertion !__comp(*(__first + __b), *(__first + __a)) failed: Your comparator is not a valid strict-weak ordering\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__iterator/advance.h:70: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to advance(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__iterator/next.h:33: assertion __n >= 0 || __has_bidirectional_iterator_category<_InputIter>::value failed: Attempt to next(it, n) with negative n on a non-bidirectional iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:39: assertion __location != nullptr failed: null pointer given to construct_at\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:403: assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:422: assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:430: assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/array:269: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/array:273: assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/bitset:694: assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/list:1319: assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/list:1434: assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/list:786: assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/valarray:825: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CBEHugBoe2IJnIQG0z_Gpu4QunkW-k4mV2P2Tv8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/valarray:830: assertion __i < size() failed: valarray::operator[] index out of bounds\n"
- "Jumping to target compensated MIB (%f)"
- "_jumpToTarget"

```
