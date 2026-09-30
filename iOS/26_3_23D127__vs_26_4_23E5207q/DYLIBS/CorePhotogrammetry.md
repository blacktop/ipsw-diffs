## CorePhotogrammetry

> `/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry`

```diff

 3.9.4.0.0
-  __TEXT.__text: 0xf48f44
-  __TEXT.__auth_stubs: 0x3860
+  __TEXT.__text: 0xfdb024
+  __TEXT.__auth_stubs: 0x3850
   __TEXT.__init_offsets: 0xc
-  __TEXT.__gcc_except_tab: 0xaaf30
-  __TEXT.__const: 0x5763c
-  __TEXT.__cstring: 0x7c87a
+  __TEXT.__gcc_except_tab: 0xaa74c
+  __TEXT.__const: 0x56e3c
+  __TEXT.__cstring: 0x8123a
   __TEXT.__oslogstring: 0x487
-  __TEXT.__unwind_info: 0x315d0
-  __TEXT.__eh_frame: 0xf60
+  __TEXT.__unwind_info: 0x31768
+  __TEXT.__eh_frame: 0xe88
   __TEXT.__objc_methname: 0x18f6
   __TEXT.__objc_stubs: 0x1d60
   __DATA_CONST.__got: 0x6f8
   __DATA_CONST.__const: 0x12b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x758
-  __AUTH_CONST.__auth_got: 0x1c40
+  __AUTH_CONST.__auth_got: 0x1c38
   __AUTH_CONST.__const: 0x31310
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_intobj: 0x60

   __AUTH.__thread_bss: 0x8038
   __DATA.__data: 0x4084
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x77c8
-  __DATA.__common: 0x1a0
-  __DATA_DIRTY.__common: 0x208
+  __DATA.__bss: 0x77d8
+  __DATA.__common: 0x190
+  __DATA_DIRTY.__common: 0x218
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  UUID: F531FA0B-3343-39D7-B4A9-85342B53EAC0
-  Functions: 33692
-  Symbols:   3240
-  CStrings:  5220
+  UUID: 0BD888F0-6623-31DF-9398-A87804F2731A
+  Functions: 33919
+  Symbols:   3239
+  CStrings:  5276
 
Symbols:
+ __ZNSt3__117__assoc_sub_state12__make_readyEv
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _wmemchr
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_storeStrong
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:831: libc++ Hardening assertion __ns >= 0 failed: invalid range specified\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1572: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:840: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/valarray:825: libc++ Hardening assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/valarray:830: libc++ Hardening assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/base/tf/refPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/usd/sdf/declareHandles.h"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBVt5d2ABWXz_0RnZzRuKppbL3CNWRGELU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/usd/usd/object.h"
+ "/Library/Caches/com.apple.xbs/CD38D22B-9830-454E-9712-1904A547AEF5/TemporaryDirectory.vprQYU/Binaries/CorePhotogrammetry/install/TempContent/Objects/3rd-party/MLXWrapper/mlx/mlx/backend/metal/kernels//mlx.metallib"
+ "/Library/Caches/com.apple.xbs/CD38D22B-9830-454E-9712-1904A547AEF5/TemporaryDirectory.vprQYU/Sources/CorePhotogrammetry/3rd-party/CGAL/include/CGAL/Small_unordered_map.h"
+ "/Library/Caches/com.apple.xbs/CD38D22B-9830-454E-9712-1904A547AEF5/TemporaryDirectory.vprQYU/Sources/CorePhotogrammetry/aspenbase/third-party/cpg-applecmake/src/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h:216"
+ "/Library/Caches/com.apple.xbs/CD38D22B-9830-454E-9712-1904A547AEF5/TemporaryDirectory.vprQYU/Sources/CorePhotogrammetry/aspenbase/third-party/cpg-applecmake/src/Kit/CoreVideo/src/CVImage.cpp:51"
- "/AppleInternal/Library/BuildRoots/4~CH0JugAFiCZHi3Z-5uvUOOg6WhXEzdYfdsTBbkg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/base/tf/refPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CH0JugAFiCZHi3Z-5uvUOOg6WhXEzdYfdsTBbkg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/usd/sdf/declareHandles.h"
- "/AppleInternal/Library/BuildRoots/4~CH0JugAFiCZHi3Z-5uvUOOg6WhXEzdYfdsTBbkg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/usd/usd/object.h"
- "/Library/Caches/com.apple.xbs/Binaries/CorePhotogrammetry/install/TempContent/Objects/3rd-party/MLXWrapper/mlx/mlx/backend/metal/kernels//mlx.metallib"
- "/Library/Caches/com.apple.xbs/Sources/CorePhotogrammetry/3rd-party/CGAL/include/CGAL/Small_unordered_map.h"
- "/Library/Caches/com.apple.xbs/Sources/CorePhotogrammetry/aspenbase/third-party/cpg-applecmake/src/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h:216"
- "/Library/Caches/com.apple.xbs/Sources/CorePhotogrammetry/aspenbase/third-party/cpg-applecmake/src/Kit/CoreVideo/src/CVImage.cpp:51"

```
