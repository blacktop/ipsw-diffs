## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1608.60.11.0.0
-  __TEXT.__text: 0x74e1c
+1608.80.10.0.0
+  __TEXT.__text: 0x752cc
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x18b74
-  __TEXT.__cstring: 0x5397
+  __TEXT.__const: 0x18b54
+  __TEXT.__cstring: 0x53aa
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1700
+  __TEXT.__unwind_info: 0x1714
   __TEXT.__eh_frame: 0x270
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf00
   __AUTH_CONST.__auth_ptr: 0x1c8
-  __AUTH_CONST.__const: 0x13a0
+  __AUTH_CONST.__const: 0x1400
   __AUTH_CONST.__auth_got: 0x110
   __AUTH.__data: 0xa0
   __DATA.__data: 0x6b68

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 1847
-  Symbols:   3147
+  Functions: 1854
+  Symbols:   3160
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
