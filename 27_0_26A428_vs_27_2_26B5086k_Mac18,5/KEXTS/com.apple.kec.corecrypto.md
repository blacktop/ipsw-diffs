## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-2109.0.22.0.0
-  __TEXT.__cstring: 0x447d
-  __TEXT.__const: 0x10180
+2109.40.15.0.0
+  __TEXT.__cstring: 0x4540
+  __TEXT.__const: 0x101e0
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x6cc24
+  __TEXT_EXEC.__text: 0x6d0ac
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0x29e0
   __DATA.__common: 0x18
-  __DATA_CONST.__const: 0x3fb8
+  __DATA_CONST.__const: 0x3fd8
   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x188
-  Functions: 1948
-  Symbols:   2116
-  CStrings:  368
+  Functions: 1955
+  Symbols:   2122
+  CStrings:  371
 
Symbols:
+ _ccmldsa44
+ _ccmldsa44_params
+ _ccmldsa_poly_bitpack_z_g1_17
+ _ccmldsa_poly_bitpack_z_g1_19
+ _ccmldsa_poly_bitunpack_z_g1_17
+ _ccmldsa_poly_bitunpack_z_g1_19
+ _ccmldsa_poly_simplebitpack_w1_4bit
+ _ccmldsa_poly_simplebitpack_w1_6bit
+ _rej_rnd_kat_44
+ _rej_sig_sha256_kat_44
+ _seed_kat_44
- _ccmldsa65_draft_params
- _ccmldsa87_draft_params
- _ccmldsa_poly_bitpack_z
- _ccmldsa_poly_bitunpack_z
- _ccmldsa_poly_simplebitpack_w1
CStrings:
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign (rejection, ML-DSA-44): %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch rejection sig (ML-DSA-44): %d\n"
+ "fipspost_post_mldsa_sign_rejection_kat_44"
```
