## libcrypto.55.dylib

> `/usr/lib/libcrypto.55.dylib`

```diff

-111.0.2.0.0
-  __TEXT.__text: 0xc5a14
+111.0.5.0.0
+  __TEXT.__text: 0xc5a68
   __TEXT.__cstring: 0x1991b
   __TEXT.__const: 0x190a8
   __TEXT.__unwind_info: 0x28d8

   __DATA_CONST.__const: 0x17fd8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x7348
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH.__data: 0x38
   __DATA.__data: 0xff4
   __DATA.__bss: 0x1eb0

   - /System/Library/PrivateFrameworks/TrustEvaluationAgent.framework/Versions/A/TrustEvaluationAgent
   - /usr/lib/libSystem.B.dylib
   Functions: 4771
-  Symbols:   5773
+  Symbols:   5774
   CStrings:  4062
 
Symbols:
+ _cc_cmp_safe
Functions:
~ _ECDSA_do_sign_new : 488 -> 500
~ _ECDSA_do_verify_new : 372 -> 380
~ _aes_gcm_cleanup : 144 -> 152
~ _HMAC_Init_ex : 720 -> 748
~ _HMAC_CTX_copy : 240 -> 304
~ _libressl_timingsafe_memcmp : 68 -> 32
```
