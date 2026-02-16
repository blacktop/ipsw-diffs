## Montreal

> `/System/Library/PrivateFrameworks/Montreal.framework/Montreal`

```diff

 188.0.0.0.0
-  __TEXT.__text: 0x1b3318
-  __TEXT.__auth_stubs: 0x1970
+  __TEXT.__text: 0x1cf410
+  __TEXT.__auth_stubs: 0x1930
   __TEXT.__init_offsets: 0x48
   __TEXT.__objc_methlist: 0x22bc
-  __TEXT.__gcc_except_tab: 0x1bdac
-  __TEXT.__const: 0x42e0
-  __TEXT.__cstring: 0x3415
+  __TEXT.__gcc_except_tab: 0x1bd88
+  __TEXT.__const: 0x4264
+  __TEXT.__cstring: 0x5881
   __TEXT.__oslogstring: 0x3d2
-  __TEXT.__unwind_info: 0x5c60
-  __TEXT.__eh_frame: 0xa0
+  __TEXT.__unwind_info: 0x5dc0
+  __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x393
   __TEXT.__objc_methname: 0x63a1
-  __TEXT.__objc_methtype: 0x13d4
+  __TEXT.__objc_methtype: 0x13d0
   __TEXT.__objc_stubs: 0x4a00
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__const: 0x870

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0xcd0
+  __AUTH_CONST.__auth_got: 0xcb0
   __AUTH_CONST.__const: 0x8560
   __AUTH_CONST.__cfstring: 0x2960
   __AUTH_CONST.__objc_const: 0x4518

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29516AD8-B7C9-3B6E-B7BD-D95ACC7EACA7
-  Functions: 4080
-  Symbols:   766
-  CStrings:  2189
+  UUID: 46F3F210-596E-3221-94DD-08D14FAE83C7
+  Functions: 4148
+  Symbols:   762
+  CStrings:  2215
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugDqK4pFx8tTLQtmx6D-QFlEqg09FG-fFgg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "{map<unsigned int, std::map<unsigned int, unsigned int>, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, std::map<unsigned int, unsigned int>>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, std::map<unsigned int, unsigned int>>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, std::map<unsigned int, unsigned int>>, std::less<unsigned int>>, std::allocator<std::pair<const unsigned int, std::map<unsigned int, unsigned int>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- ".mil"
- "{map<unsigned int, std::map<unsigned int, unsigned int>, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, std::map<unsigned int, unsigned int>>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, std::map<unsigned int, unsigned int>>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, std::map<unsigned int, unsigned int>>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, std::map<unsigned int, unsigned int>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"

```
