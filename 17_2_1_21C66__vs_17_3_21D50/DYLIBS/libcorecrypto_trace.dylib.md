## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1608.60.11.0.0
-  __TEXT.__text: 0x7e91c
+1608.80.10.0.0
+  __TEXT.__text: 0x7ee5c
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x18e94
-  __TEXT.__cstring: 0x5697
+  __TEXT.__const: 0x18e74
+  __TEXT.__cstring: 0x56aa
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1794
+  __TEXT.__unwind_info: 0x17a8
   __TEXT.__eh_frame: 0x220
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf00
-  __AUTH_CONST.__const: 0x18e0
+  __AUTH_CONST.__const: 0x1940
   __AUTH_CONST.__auth_got: 0x110
   __AUTH.__data: 0xb8
   __DATA.__data: 0x6b70

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 2F68D539-BAD2-3154-89BB-E106AD575CA1
-  Functions: 1962
-  Symbols:   3395
+  UUID: 2D6CED64-5FD5-3AEC-A311-127842D8DE7D
+  Functions: 1969
+  Symbols:   3408
   CStrings:  649
 
Symbols:
+ _CCBFV_DECRYPT_CTX_INIT_WORKSPACE_N
+ _CCBFV_PARAM_CTX_INIT_WORKSPACE_N
+ _PQCLEAN_KYBER_CLEAN_crypto_kem_enc_msg
+ _PQCLEAN_KYBER_CLEAN_crypto_kem_keypair_coins
+ _cc_xor_safe
+ _ccrsa_eme_pkcs1v15_decode_safe
+ _ccrsa_eme_pkcs1v15_decode_safe_ws
CStrings:
+ "ccrsa_eme_pkcs1v15_decode_generate_random"
- "Bogus Kyber parameter."

```
