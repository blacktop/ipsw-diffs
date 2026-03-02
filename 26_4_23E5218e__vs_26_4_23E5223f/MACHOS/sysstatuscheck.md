## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

 211.100.4.0.0
-  __TEXT.__text: 0xcbb4
-  __TEXT.__auth_stubs: 0x500
+  __TEXT.__text: 0xc090
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1143
+  __TEXT.__cstring: 0x8e7
   __TEXT.__gcc_except_tab: 0x538
   __TEXT.__const: 0x498
-  __TEXT.__unwind_info: 0x510
-  __DATA_CONST.__auth_got: 0x288
+  __TEXT.__unwind_info: 0x508
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x728
   __DATA_CONST.__cfstring: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 9BE3973A-E9F7-33E5-9640-A7EDBA85C72F
-  Functions: 247
-  Symbols:   129
-  CStrings:  73
+  UUID: 2DA3C98A-2B56-308B-BC35-EA9C7E955D2B
+  Functions: 246
+  Symbols:   128
+  CStrings:  66
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJJDugDImN35kU5FfnYZ3RO1CzanTtZTQzRwY3g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJJDugDImN35kU5FfnYZ3RO1CzanTtZTQzRwY3g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJJDugDImN35kU5FfnYZ3RO1CzanTtZTQzRwY3g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJJDugDImN35kU5FfnYZ3RO1CzanTtZTQzRwY3g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJJDugDImN35kU5FfnYZ3RO1CzanTtZTQzRwY3g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJJDugDImN35kU5FfnYZ3RO1CzanTtZTQzRwY3g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJJDugDImN35kU5FfnYZ3RO1CzanTtZTQzRwY3g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
