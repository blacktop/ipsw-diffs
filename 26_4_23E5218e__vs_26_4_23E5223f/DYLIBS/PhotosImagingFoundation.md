## PhotosImagingFoundation

> `/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation`

```diff

-840.1.250.0.0
-  __TEXT.__text: 0x220d4
-  __TEXT.__auth_stubs: 0x840
+840.2.120.0.0
+  __TEXT.__text: 0x22074
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x2564
   __TEXT.__const: 0x420
   __TEXT.__gcc_except_tab: 0xf1c
-  __TEXT.__cstring: 0x6177
+  __TEXT.__cstring: 0x5d52
   __TEXT.__oslogstring: 0x336
   __TEXT.__ustring: 0xa8
   __TEXT.__unwind_info: 0xf90

   __DATA_CONST.__objc_selrefs: 0xfe0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
-  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x218
   __AUTH_CONST.__cfstring: 0x3760
   __AUTH_CONST.__objc_const: 0x3a60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A682BE3-F212-34A1-B137-D79D29763EA8
+  UUID: 0AF595C9-F107-3D1E-B6DA-D6A6D4D748CD
   Functions: 927
-  Symbols:   3225
-  CStrings:  1993
+  Symbols:   3224
+  CStrings:  1990
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt12out_of_rangeC1B9nqe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN2PA4RectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__120__throw_out_of_rangeB9nqe210106EPKc
+ __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE11__vallocateB9nqe210106Em
+ __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE20__throw_out_of_rangeB9nqe210106Ev
+ __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___Block_byref_object_copy_.1737
+ ___Block_byref_object_copy_.2205
+ ___Block_byref_object_dispose_.1738
+ ___Block_byref_object_dispose_.2206
+ ___block_literal_global.1267
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt12out_of_rangeC1B9foe210106EPKc
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIN2PA4RectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__120__throw_out_of_rangeB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE11__vallocateB9foe210106Em
- __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE20__throw_out_of_rangeB9foe210106Ev
- __ZNSt3__16vectorIN2PA4RectENS_9allocatorIS2_EEE9push_backB9foe210106ERKS2_
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ___Block_byref_object_copy_.1740
- ___Block_byref_object_copy_.2208
- ___Block_byref_object_dispose_.1741
- ___Block_byref_object_dispose_.2209
- ___block_literal_global.1269
Functions:
~ -[IPAMutableRectArray removeRectAtIndex:] : 120 -> 84
~ -[IPAMutableRectArray insertRect:atIndex:] : 588 -> 564
~ __ZNSt3__112__hash_tableIN2PA10RegionRectENS1_8RectHashENS1_11RectEqualToENS_9allocatorIS2_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEE : 340 -> 304
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"

```
