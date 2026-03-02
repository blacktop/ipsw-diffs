## CollectionViewCore

> `/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore`

```diff

-9126.4.24.1.101
-  __TEXT.__text: 0x14db4
-  __TEXT.__auth_stubs: 0x420
+9126.4.26.1.101
+  __TEXT.__text: 0x14c54
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0x1d44
   __TEXT.__const: 0x128
   __TEXT.__gcc_except_tab: 0x55c
-  __TEXT.__cstring: 0x3716
+  __TEXT.__cstring: 0x3320
   __TEXT.__oslogstring: 0xe1c
   __TEXT.__unwind_info: 0x7b8
   __TEXT.__objc_classname: 0x30b

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xea8
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1860
   __AUTH_CONST.__objc_const: 0x2900

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CAF666E9-96EA-31C0-A728-6633CB94D67A
+  UUID: D97C47E1-A1D3-391F-90B2-561BA407C903
   Functions: 598
-  Symbols:   1940
-  CStrings:  1255
+  Symbols:   1939
+  CStrings:  1252
 
Symbols:
+ __ZNSt3__119__allocate_at_leastB9nqn210106INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE18__assign_with_sizeB9nqn210106IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE9push_backB9nqn210106ERKS1_
+ __ZSt28__throw_bad_array_new_lengthB9nqn210106v
- __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE18__assign_with_sizeB9fon210106IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
- __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE9push_backB9fon210106ERKS1_
- __ZSt28__throw_bad_array_new_lengthB9fon210106v
Functions:
~ -[_UIDataSourceSnapshotter _insertSection:withInitialCount:] : 560 -> 536
~ -[_UIDataSourceSnapshotter _incrementSectionCount:byCount:] : 128 -> 80
~ -[_UIDataSourceSnapshotter numberOfItemsInSection:] : 104 -> 36
~ -[_UIDataSourceSnapshotter globalIndexForIndexPath:] : 208 -> 176
~ -[_UIDataSourceSnapshotter _decrementSectionCount:byCount:] : 148 -> 76
~ -[_UIDataSourceSnapshotter numberOfItemsBeforeSection:] : 104 -> 36
~ -[_UIDataSourceSnapshotter _deleteSection:] : 160 -> 120
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJV8ugC2eHTl0g0YrYBRsil1VCE3HGrDnLam9DI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJV8ugC2eHTl0g0YrYBRsil1VCE3HGrDnLam9DI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJV8ugC2eHTl0g0YrYBRsil1VCE3HGrDnLam9DI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
