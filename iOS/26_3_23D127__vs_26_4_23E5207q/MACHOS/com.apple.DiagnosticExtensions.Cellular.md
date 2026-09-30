## com.apple.DiagnosticExtensions.Cellular

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular`

```diff

-1399.9.0.0.0
-  __TEXT.__text: 0x25938
-  __TEXT.__auth_stubs: 0xbd0
+1416.1.0.0.0
+  __TEXT.__text: 0x26ad4
+  __TEXT.__auth_stubs: 0xbf0
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x1a8
   __TEXT.__const: 0x4b8
-  __TEXT.__gcc_except_tab: 0x35c4
-  __TEXT.__cstring: 0x4a0
+  __TEXT.__gcc_except_tab: 0x3618
+  __TEXT.__cstring: 0x1baf
   __TEXT.__oslogstring: 0xb38
   __TEXT.__objc_methname: 0x47e
   __TEXT.__objc_classname: 0x46
   __TEXT.__objc_methtype: 0x288
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0x5f8
+  __TEXT.__unwind_info: 0x788
+  __DATA_CONST.__auth_got: 0x608
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__cfstring: 0x2a0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2BC57A0-7D33-3CB8-AA2A-834D0FF7851D
-  Functions: 288
-  Symbols:   377
-  CStrings:  268
+  UUID: BBFEC3E3-8857-316F-8D70-47BEE90A5B80
+  Functions: 292
+  Symbols:   380
+  CStrings:  286
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x22
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "Watchdog timed out"

```
