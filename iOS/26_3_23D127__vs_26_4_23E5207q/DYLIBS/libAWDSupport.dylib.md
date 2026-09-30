## libAWDSupport.dylib

> `/usr/lib/libAWDSupport.dylib`

```diff

 998.0.0.0.0
-  __TEXT.__text: 0x381a0
-  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__text: 0x384cc
+  __TEXT.__auth_stubs: 0xc30
   __TEXT.__init_offsets: 0x4
-  __TEXT.__gcc_except_tab: 0x4758
-  __TEXT.__cstring: 0xad4
+  __TEXT.__gcc_except_tab: 0x4768
+  __TEXT.__cstring: 0x2bbe
   __TEXT.__const: 0xf98
   __TEXT.__oslogstring: 0x7a
-  __TEXT.__unwind_info: 0x1808
+  __TEXT.__unwind_info: 0x1868
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x198
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x1800
   __AUTH_CONST.__cfstring: 0x40
   __AUTH.__data: 0x30
-  __DATA.__bss: 0x58
-  __DATA_DIRTY.__bss: 0x38
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: A11E760D-35D3-369D-ADC1-4BD7936E20D1
-  Functions: 1094
-  Symbols:   371
-  CStrings:  188
+  UUID: EC7A5100-A673-3D89-9E88-8D6DEFD8094D
+  Functions: 1123
+  Symbols:   372
+  CStrings:  213
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3352: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZOugB_qFtr53vVVShCKyGHAEYgWbfqm2dg41k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3352: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"

```
