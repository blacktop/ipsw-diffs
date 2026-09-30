## swcutil

> `/System/Library/PrivateFrameworks/SharedWebCredentials.framework/Support/swcutil`

```diff

 1021.2.0.0.0
-  __TEXT.__text: 0x1a5f4
-  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__text: 0x1a518
+  __TEXT.__auth_stubs: 0x9f0
   __TEXT.__objc_stubs: 0x2dc0
   __TEXT.__objc_methlist: 0xc14
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x35cc
-  __TEXT.__cstring: 0x2471
+  __TEXT.__cstring: 0x209a
   __TEXT.__objc_methname: 0x34fd
   __TEXT.__oslogstring: 0xf38
   __TEXT.__objc_classname: 0x178
   __TEXT.__objc_methtype: 0xc8b
   __TEXT.__unwind_info: 0xa50
-  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__auth_got: 0x508
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x918
   __DATA_CONST.__cfstring: 0x1480

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF755D0A-DCF3-3CAF-A8FD-EA110B308FEA
+  UUID: EC230BC4-479E-348D-8DA7-B40714FC4CB2
   Functions: 326
-  Symbols:   247
-  CStrings:  1241
+  Symbols:   246
+  CStrings:  1238
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_10000dec4 : 2848 -> 2668
~ sub_100014d04 -> sub_100014c50 : 720 -> 680
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlSugBy9c3pEocOD9yCdUZRFcdVtPrTeBhBWdo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlSugBy9c3pEocOD9yCdUZRFcdVtPrTeBhBWdo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlSugBy9c3pEocOD9yCdUZRFcdVtPrTeBhBWdo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"

```
