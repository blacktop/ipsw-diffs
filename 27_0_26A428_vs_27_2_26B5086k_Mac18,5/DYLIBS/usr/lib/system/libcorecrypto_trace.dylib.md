## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-2109.0.22.0.0
-  __TEXT.__text: 0x8c25c
-  __TEXT.__cstring: 0x5bb7
-  __TEXT.__const: 0x204b8
+2109.40.15.0.0
+  __TEXT.__text: 0x8c7e8
+  __TEXT.__cstring: 0x5c7a
+  __TEXT.__const: 0x204f8
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x24b0
+  __TEXT.__unwind_info: 0x24b8
   __TEXT.__eh_frame: 0x400
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2108
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x23b8
+  __AUTH_CONST.__const: 0x2488
   __AUTH_CONST.__auth_got: 0x118
   __AUTH.__data: 0x160
   __DATA.__data: 0x6868

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2643
-  Symbols:   2980
-  CStrings:  558
+  Functions: 2648
+  Symbols:   2987
+  CStrings:  561
 
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
