## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-2109.0.17.0.0
-  __TEXT.__cstring: 0x4214
-  __TEXT.__const: 0x10140
+2109.0.22.0.0
+  __TEXT.__cstring: 0x4479
+  __TEXT.__const: 0x10180
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x6a0fc
+  __TEXT_EXEC.__text: 0x6db98
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0x29e0
   __DATA.__bss: 0x27c0

   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x188
-  Functions: 1942
+  Functions: 1949
   Symbols:   0
-  CStrings:  347
+  CStrings:  368
 
CStrings:
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_import_privkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_import_pubkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign (rejection): %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch rejection sig: %d\n"
+ "cckem_decapsulate"
+ "cckem_encapsulate"
+ "cckem_generate_key"
+ "cckem_generate_key_with_seed"
+ "cckem_mlkem1024"
+ "cckem_mlkem768"
+ "ccmldsa65"
+ "ccmldsa87"
+ "ccmldsa_generate_key"
+ "ccmldsa_generate_key_with_seed"
+ "ccmldsa_sign"
+ "ccmldsa_sign_prehashed"
+ "ccmldsa_sign_with_context"
+ "ccmldsa_verify"
+ "ccmldsa_verify_prehashed"
+ "ccmldsa_verify_with_context"
+ "fipspost_post_mldsa_sign_rejection_kat"
```
