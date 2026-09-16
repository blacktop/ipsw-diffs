## PrivacyDisclosureCore

> `/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore`

```diff

-49.0.1.0.0
-  __TEXT.__text: 0x3c40
+53.0.0.0.0
+  __TEXT.__text: 0x3d38
   __TEXT.__objc_methlist: 0x704
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x444
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x43a
   __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__oslogstring: 0x244
+  __TEXT.__oslogstring: 0x2d0
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__unwind_info: 0x278
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x1e10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libCTGreenTeaLogger.dylib
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 133
+  Functions: 134
   Symbols:   510
-  CStrings:  55
+  CStrings:  56
 
Symbols:
+ ___isTennessineEligible_block_invoke
+ _isTennessineEligible.once
+ _isTennessineEligible.result
+ _os_eligibility_get_domain_answer
- _MGGetBoolAnswer
- ___isGreenTea_block_invoke
- _isGreenTea.once
- _isGreenTea.result
Functions:
- ___isGreenTea_block_invoke
+ ___isTennessineEligible_block_invoke
+ ___isTennessineEligible_block_invoke.cold.1
CStrings:
+ "Failed to query OS_ELIGIBILITY_DOMAIN_TENNESSINE: %{darwin.errno}d"
+ "OS_ELIGIBILITY_DOMAIN_TENNESSINE answered %llu, treating as not eligible"
- "green-tea"
```
