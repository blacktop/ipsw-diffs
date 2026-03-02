## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x1c750
-  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__text: 0x1c52c
+  __TEXT.__auth_stubs: 0xb20
   __TEXT.__objc_stubs: 0x1bc0
   __TEXT.__objc_methlist: 0x8a4
   __TEXT.__gcc_except_tab: 0x2d1c
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x225d
-  __TEXT.__cstring: 0x449f
+  __TEXT.__cstring: 0x436c
   __TEXT.__objc_classname: 0xca
   __TEXT.__objc_methtype: 0xa12
   __TEXT.__oslogstring: 0x11d
   __TEXT.__unwind_info: 0x878
-  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__cfstring: 0x3480

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D49A0955-AC6C-394B-AF64-F83A7A1BAD5C
+  UUID: 703CCA62-E94A-387F-893A-2C9A342AC30B
   Functions: 347
-  Symbols:   462
-  CStrings:  1498
+  Symbols:   461
+  CStrings:  1497
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_100014984 : 1488 -> 1136
~ sub_100014fc4 -> sub_100014e64 : 12160 -> 11964
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRfugDywEzyHpDE5AqdDbfH7AdCTrLiPzJ_0fg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
