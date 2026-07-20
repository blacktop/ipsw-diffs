## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__fips_hmacs`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-2109.0.11.0.0
-  __TEXT.__text: 0x87290
+2109.0.17.0.0
+  __TEXT.__text: 0x875bc
   __TEXT.__const: 0x201e8
-  __TEXT.__cstring: 0x5530
+  __TEXT.__cstring: 0x5818
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
   __TEXT.__unwind_info: 0x1c38

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2487
-  Symbols:   2786
-  CStrings:  519
+  Functions: 2486
+  Symbols:   2788
+  CStrings:  529
 
Symbols:
+ _ccmldsa_keygen_pairwise_check
+ _ccmlkem_kem_pairwise_check
CStrings:
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected FAILURE: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected SUCCESS\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected FAILURE: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected SUCCESS\n"
+ "FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: FORCEFAIL\n"
+ "FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: expected SUCCESS\n"
+ "FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: FORCEFAIL\n"
+ "FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: expected SUCCESS\n"
+ "fipspost_post_mldsa_pairwise"
+ "fipspost_post_mlkem_pairwise"
```
