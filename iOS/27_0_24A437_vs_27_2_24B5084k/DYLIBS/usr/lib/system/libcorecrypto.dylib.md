## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-2109.0.22.0.0
-  __TEXT.__text: 0x8b468
-  __TEXT.__cstring: 0x5940
-  __TEXT.__const: 0x204a8
+2109.40.15.0.0
+  __TEXT.__text: 0x8ba0c
+  __TEXT.__cstring: 0x5a03
+  __TEXT.__const: 0x204e8
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x2420
+  __TEXT.__unwind_info: 0x2428
   __TEXT.__eh_frame: 0x3c8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2108
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x23b8
+  __AUTH_CONST.__const: 0x2488
   __AUTH_CONST.__auth_got: 0x118
   __AUTH.__data: 0x148
   __DATA.__data: 0x6858

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2638
-  Symbols:   2958
-  CStrings:  534
+  Functions: 2644
+  Symbols:   2965
+  CStrings:  537
 
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
+ _seed_kat_44
- _ccmldsa_poly_bitpack_z
- _ccmldsa_poly_bitunpack_z
- _ccmldsa_poly_simplebitpack_w1
CStrings:
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection, ML-DSA-44): %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig (ML-DSA-44): %d\n"
+ "fipspost_post_mldsa_sign_rejection_kat_44"
```
