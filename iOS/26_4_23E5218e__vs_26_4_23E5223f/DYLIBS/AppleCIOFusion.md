## AppleCIOFusion

> `/System/Library/PrivateFrameworks/AppleCIOFusion.framework/AppleCIOFusion`

```diff

 3.0.0.0.0
-  __TEXT.__text: 0x5ed8
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__cstring: 0x576
+  __TEXT.__text: 0x5dc8
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__cstring: 0x2a7
   __TEXT.__const: 0x4a
   __TEXT.__oslogstring: 0xb51
-  __TEXT.__gcc_except_tab: 0x39c
+  __TEXT.__gcc_except_tab: 0x398
   __TEXT.__unwind_info: 0x2b8
   __DATA_CONST.__got: 0x50
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x1c8
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: ACF252CE-03A4-356E-8C1F-E61ABB100076
+  UUID: A6E635F9-1FCE-315A-9D13-8FD6C27D1DD4
   Functions: 154
-  Symbols:   77
-  CStrings:  80
+  Symbols:   76
+  CStrings:  77
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_2ab57d22c -> sub_2a8b0322c : 2688 -> 2512
~ sub_2ab57dcac -> sub_2a8b03bfc : 1392 -> 1012
~ sub_2ab57e21c -> sub_2a8b03ff0 : 1288 -> 1572
CStrings:
- "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"

```
