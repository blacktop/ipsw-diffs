## libcrypto.46.dylib

> `/usr/lib/libcrypto.46.dylib`

```diff

-111.0.2.0.0
-  __TEXT.__text: 0xd1f74
+111.0.5.0.0
+  __TEXT.__text: 0xd1fc8
   __TEXT.__const: 0x20c70
   __TEXT.__cstring: 0x1bd60
   __TEXT.__unwind_info: 0x2b88

   __DATA_CONST.__const: 0x13768
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x6180
-  __AUTH_CONST.__auth_got: 0x4a0
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH.__data: 0x7d8
   __DATA.__data: 0x45c8
   __DATA.__bss: 0xa70

   - /System/Library/PrivateFrameworks/TrustEvaluationAgent.framework/Versions/A/TrustEvaluationAgent
   - /usr/lib/libSystem.B.dylib
   Functions: 5056
-  Symbols:   6215
+  Symbols:   6216
   CStrings:  4098
 
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
