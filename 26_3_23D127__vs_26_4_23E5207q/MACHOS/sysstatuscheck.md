## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

-210.0.0.0.0
-  __TEXT.__text: 0xc338
-  __TEXT.__auth_stubs: 0x4f0
+211.100.4.0.0
+  __TEXT.__text: 0xcbb4
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__init_offsets: 0x4
+  __TEXT.__cstring: 0x1143
   __TEXT.__gcc_except_tab: 0x538
-  __TEXT.__cstring: 0x8e7
   __TEXT.__const: 0x498
-  __TEXT.__unwind_info: 0x518
-  __DATA_CONST.__auth_got: 0x280
+  __TEXT.__unwind_info: 0x510
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x728
   __DATA_CONST.__cfstring: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 82F44036-8173-3966-B9EA-83D3F5174E65
-  Functions: 248
+  UUID: 8E8C6CC1-2C73-3573-8A09-8C37DAD55D4E
+  Functions: 247
   Symbols:   129
-  CStrings:  66
+  CStrings:  73
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIVIugAV4HKt_NML8Ve-bthUwiIqRIgPOvyLrDY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVIugAV4HKt_NML8Ve-bthUwiIqRIgPOvyLrDY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVIugAV4HKt_NML8Ve-bthUwiIqRIgPOvyLrDY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVIugAV4HKt_NML8Ve-bthUwiIqRIgPOvyLrDY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVIugAV4HKt_NML8Ve-bthUwiIqRIgPOvyLrDY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVIugAV4HKt_NML8Ve-bthUwiIqRIgPOvyLrDY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVIugAV4HKt_NML8Ve-bthUwiIqRIgPOvyLrDY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
