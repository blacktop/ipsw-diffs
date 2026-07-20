## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

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
-  __TEXT.__text: 0x8cd58
-  __TEXT.__cstring: 0x57a3
+2109.0.17.0.0
+  __TEXT.__text: 0x8d054
+  __TEXT.__cstring: 0x5a8b
   __TEXT.__const: 0x20498
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2646
-  Symbols:   2979
-  CStrings:  543
+  Functions: 2645
+  Symbols:   2981
+  CStrings:  553
 
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
