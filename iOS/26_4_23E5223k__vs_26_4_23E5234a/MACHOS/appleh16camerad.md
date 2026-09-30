## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-5.403.0.0.0
-  __TEXT.__text: 0x7f698
-  __TEXT.__auth_stubs: 0x1f70
+5.408.0.0.0
+  __TEXT.__text: 0x7f5f4
+  __TEXT.__auth_stubs: 0x1f60
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0x268
   __TEXT.__gcc_except_tab: 0x2198
   __TEXT.__const: 0x2db0
-  __TEXT.__cstring: 0x8e71
+  __TEXT.__cstring: 0x8acd
   __TEXT.__objc_classname: 0x89
   __TEXT.__oslogstring: 0x5dfe
   __TEXT.__objc_methname: 0x1582
   __TEXT.__objc_methtype: 0x10b3
   __TEXT.__unwind_info: 0x15b0
-  __DATA_CONST.__auth_got: 0xfc8
+  __DATA_CONST.__auth_got: 0xfc0
   __DATA_CONST.__got: 0xbc8
   __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0xb710

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CDB77D2E-0125-38B6-9600-3EB61CA159F1
+  UUID: 434ED948-ED49-35F0-BBDE-156A82CDDD6E
   Functions: 1694
-  Symbols:   906
-  CStrings:  2446
+  Symbols:   905
+  CStrings:  2443
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_1000247c0 : 596 -> 488
~ sub_10005f13c -> sub_10005f0d0 : 1684 -> 1628
CStrings:
+ "5.408"
- "/AppleInternal/Library/BuildRoots/4~CJlbugAz5lQ_lqjyo6HUuqrlFzFIYhzc2ygJrXs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlbugAz5lQ_lqjyo6HUuqrlFzFIYhzc2ygJrXs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlbugAz5lQ_lqjyo6HUuqrlFzFIYhzc2ygJrXs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "5.403"

```
