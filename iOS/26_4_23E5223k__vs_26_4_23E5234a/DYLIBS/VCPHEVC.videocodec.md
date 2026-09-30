## VCPHEVC.videocodec

> `/System/Library/VideoCodecs/VCPHEVC.videocodec`

```diff

 350.1.0.0.0
-  __TEXT.__text: 0x136bc4
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__const: 0x31620
-  __TEXT.__cstring: 0x228b
+  __TEXT.__text: 0x12fab4
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__const: 0x31640
+  __TEXT.__cstring: 0x92f
   __TEXT.__gcc_except_tab: 0xff0
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x1920
+  __TEXT.__unwind_info: 0x1908
   __TEXT.__eh_frame: 0x470
   __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__const: 0xd0
-  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__const: 0x1188
   __AUTH_CONST.__cfstring: 0x9a0
   __DATA.__bss: 0x1a0

   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6E6D140F-3B30-3067-B234-6565A32FCEB8
-  Functions: 2433
-  Symbols:   412
-  CStrings:  267
+  UUID: 8FC552DF-C08F-363E-9E21-541085776D10
+  Functions: 2426
+  Symbols:   411
+  CStrings:  248
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:692: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:697: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlRugBp6IKjfPn5sF4hTIUyTSCdyAyBqj2WwU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"

```
