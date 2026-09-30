## AGXCompilerCore-S2A8

> `/System/Library/PrivateFrameworks/AGXCompilerCore-S2A8.framework/AGXCompilerCore-S2A8`

```diff

 30.5.0.0.0
-  __TEXT.__text: 0x9631c
-  __TEXT.__auth_stubs: 0x1a90
+  __TEXT.__text: 0x954d0
+  __TEXT.__auth_stubs: 0x1a80
   __TEXT.__const: 0x5b73
-  __TEXT.__cstring: 0xa1f6
+  __TEXT.__cstring: 0x895c
   __TEXT.__oslogstring: 0x195
-  __TEXT.__unwind_info: 0x11c8
+  __TEXT.__unwind_info: 0x11d8
   __TEXT.__objc_methname: 0xa2
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0xc30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0xd50
+  __AUTH_CONST.__auth_got: 0xd48
   __AUTH_CONST.__const: 0x16618
   __AUTH_CONST.__cfstring: 0xc0
   __DATA.__bss: 0xea1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 012EB951-D85D-3929-96EC-8DF40ADF6976
+  UUID: BE8A6CD5-2EFA-3F57-AA25-119125701531
   Functions: 1809
-  Symbols:   481
-  CStrings:  1692
+  Symbols:   480
+  CStrings:  1674
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:582: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAm9zGd1E--Sbm6Kyt6U26rOZbUDFe6FjE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"

```
