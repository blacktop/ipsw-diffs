## libtls.20.dylib

> `/usr/lib/libtls.20.dylib`

```diff

-111.0.2.0.0
-  __TEXT.__text: 0x107350
+111.0.5.0.0
+  __TEXT.__text: 0x1073a4
   __TEXT.__cstring: 0x21921
   __TEXT.__const: 0x213ee
   __TEXT.__unwind_info: 0x3460

   __DATA_CONST.__const: 0x16440
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x7280
-  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__auth_got: 0x500
   __AUTH.__data: 0x828
   __DATA.__data: 0x6ec8
   __DATA.__bss: 0x22b0

   - /System/Library/PrivateFrameworks/TrustEvaluationAgent.framework/Versions/A/TrustEvaluationAgent
   - /usr/lib/libSystem.B.dylib
   Functions: 5814
-  Symbols:   7420
+  Symbols:   7421
   CStrings:  5003
 
Symbols:
+ _cc_cmp_safe
Functions:
~ _ECDSA_do_sign_new : 488 -> 500
~ _ECDSA_do_verify_new : 372 -> 380
~ _aes_gcm_cleanup : 144 -> 152
~ _HMAC_Init_ex : 700 -> 728
~ _HMAC_CTX_copy : 232 -> 296
~ _timingsafe_memcmp : 68 -> 32
```
