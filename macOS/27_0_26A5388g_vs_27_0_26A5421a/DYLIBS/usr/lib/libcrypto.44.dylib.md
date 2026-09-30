## libcrypto.44.dylib

> `/usr/lib/libcrypto.44.dylib`

```diff

-111.0.2.0.0
-  __TEXT.__text: 0xbf190
+111.0.5.0.0
+  __TEXT.__text: 0xbf1e4
   __TEXT.__const: 0x22ffc
   __TEXT.__cstring: 0x1a8e8
   __TEXT.__unwind_info: 0x2868

   __DATA_CONST.__const: 0x11460
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x5ac0
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x448
   __AUTH.__data: 0x7d8
   __DATA.__data: 0x4d28
   __DATA.__bss: 0x22b8

   - /System/Library/PrivateFrameworks/TrustEvaluationAgent.framework/Versions/A/TrustEvaluationAgent
   - /usr/lib/libSystem.B.dylib
   Functions: 4690
-  Symbols:   5735
+  Symbols:   5736
   CStrings:  3967
 
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
