## CoreSceneUnderstanding

> `/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding`

```diff

 87.0.0.0.0
-  __TEXT.__text: 0xc8be8
-  __TEXT.__auth_stubs: 0x15a0
+  __TEXT.__text: 0xc8004
+  __TEXT.__auth_stubs: 0x15b0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x393c
   __TEXT.__const: 0x1ef0
-  __TEXT.__gcc_except_tab: 0xf058
-  __TEXT.__cstring: 0xbdee
+  __TEXT.__gcc_except_tab: 0xf0ec
+  __TEXT.__cstring: 0xa40e
   __TEXT.__oslogstring: 0xed8
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__constg_swiftt: 0xe8

   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x45c0
+  __TEXT.__unwind_info: 0x4610
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xb94
   __TEXT.__objc_methname: 0xb2ad

   __DATA_CONST.__objc_selrefs: 0x1bc8
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x380
-  __AUTH_CONST.__auth_got: 0xae8
+  __AUTH_CONST.__auth_got: 0xaf0
   __AUTH_CONST.__const: 0x2778
   __AUTH_CONST.__cfstring: 0x3780
   __AUTH_CONST.__objc_const: 0x8e28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F71370D3-F976-3AF4-8073-9DE22CDC1BD7
-  Functions: 3119
-  Symbols:   590
-  CStrings:  3363
+  UUID: 9B6B7CC2-2755-3CF0-BC69-F1569A9FFD02
+  Functions: 3131
+  Symbols:   591
+  CStrings:  3344
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__ranges/view_interface.h:140: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.back()` called on an empty view.\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"

```
