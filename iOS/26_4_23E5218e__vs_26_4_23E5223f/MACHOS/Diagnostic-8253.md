## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x13bd8
-  __TEXT.__auth_stubs: 0x740
+  __TEXT.__text: 0x13b48
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__gcc_except_tab: 0x222c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x3dde
+  __TEXT.__cstring: 0x3cab
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methname: 0x60a
   __TEXT.__objc_methtype: 0x7d1
   __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x4f8
   __DATA_CONST.__cfstring: 0x3220

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D51BAD9-E87B-39EC-B180-6AEB72D5F293
+  UUID: CD238BB6-1435-3AC6-B27C-ED79A1C476AA
   Functions: 207
-  Symbols:   359
-  CStrings:  968
+  Symbols:   358
+  CStrings:  967
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_10000362c : 5120 -> 5016
~ sub_100004d74 -> sub_100004d0c : 2580 -> 2540
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRfugDywEzyHpDE5AqdDbfH7AdCTrLiPzJ_0fg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
