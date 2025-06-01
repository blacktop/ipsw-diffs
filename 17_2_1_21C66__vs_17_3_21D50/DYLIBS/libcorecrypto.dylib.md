## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1608.60.11.0.0
-  __TEXT.__text: 0x7dd84
+1608.80.10.0.0
+  __TEXT.__text: 0x7e284
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x18e84
-  __TEXT.__cstring: 0x5397
+  __TEXT.__const: 0x18e74
+  __TEXT.__cstring: 0x53aa
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__unwind_info: 0x179c
   __TEXT.__eh_frame: 0x220
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf00
-  __AUTH_CONST.__const: 0x18e0
+  __AUTH_CONST.__const: 0x1940
   __AUTH_CONST.__auth_got: 0x110
   __AUTH.__data: 0xa0
   __DATA.__data: 0x6c90

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: DEBF5E16-5BD7-36B2-855F-38A18B167D81
-  Functions: 1955
-  Symbols:   3375
+  UUID: 92CB071F-AE05-3671-84A5-853F205956C5
+  Functions: 1962
+  Symbols:   3388
   CStrings:  618
 
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
