## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x1d684
-  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__text: 0x1d460
+  __TEXT.__auth_stubs: 0xb40
   __TEXT.__objc_stubs: 0x1d60
   __TEXT.__objc_methlist: 0x8e4
   __TEXT.__gcc_except_tab: 0x3010
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x23bf
-  __TEXT.__cstring: 0x4758
+  __TEXT.__cstring: 0x4625
   __TEXT.__objc_classname: 0xc0
   __TEXT.__objc_methtype: 0xa81
   __TEXT.__oslogstring: 0x26
   __TEXT.__unwind_info: 0x8a8
-  __DATA_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__auth_got: 0x5b8
   __DATA_CONST.__got: 0x428
   __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__cfstring: 0x3600

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBAE6410-B808-3433-A057-5360C121657A
+  UUID: DF299AEB-6F42-3CC8-ABE8-F8FF58A174CD
   Functions: 352
-  Symbols:   466
-  CStrings:  1537
+  Symbols:   465
+  CStrings:  1536
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_1000164a8 : 1488 -> 1136
~ sub_100016ae8 -> sub_100016988 : 12160 -> 11964
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRfugDywEzyHpDE5AqdDbfH7AdCTrLiPzJ_0fg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
