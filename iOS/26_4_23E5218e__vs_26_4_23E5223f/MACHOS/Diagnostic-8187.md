## Diagnostic-8187

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187`

```diff

-1066.100.29.0.0
-  __TEXT.__text: 0xacb4
-  __TEXT.__auth_stubs: 0x620
+1066.100.31.0.0
+  __TEXT.__text: 0xac24
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__objc_methlist: 0xfe4
   __TEXT.__gcc_except_tab: 0x8bc

   __TEXT.__objc_methname: 0x3063
   __TEXT.__objc_classname: 0x1b0
   __TEXT.__objc_methtype: 0xb3d
-  __TEXT.__cstring: 0x94c
+  __TEXT.__cstring: 0x819
   __TEXT.__oslogstring: 0xce7
   __TEXT.__unwind_info: 0x458
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x7a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A789EFEF-0677-3B60-A8C4-BF7E8155945F
+  UUID: 7E854AE6-70C3-3374-8CF1-5F72B32F26BE
   Functions: 294
-  Symbols:   219
-  CStrings:  939
+  Symbols:   218
+  CStrings:  938
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_10000182c : 1256 -> 1152
~ sub_100002a54 -> sub_1000029ec : 392 -> 352
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRnugAOjA7D1ad4eKmf_RVxY1qR46fsNm_LftA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
