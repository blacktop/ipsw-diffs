## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

### Sections with Same Size but Changed Content

- `__TEXT.__fips_hmacs`
- `__DATA.__data`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-2109.0.11.0.0
-  __TEXT.__cstring: 0x3f2c
+2109.0.17.0.0
+  __TEXT.__cstring: 0x4214
   __TEXT.__const: 0x10140
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x69da4
+  __TEXT_EXEC.__text: 0x6a0fc
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0x29e0
   __DATA.__bss: 0x27c0

   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x188
-  Functions: 1944
+  Functions: 1942
   Symbols:   0
-  CStrings:  337
+  CStrings:  347
 
CStrings:
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected FAILURE: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected SUCCESS\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected FAILURE: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected SUCCESS\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: FORCEFAIL\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: expected SUCCESS\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: FORCEFAIL\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: expected SUCCESS\n"
+ "fipspost_post_mldsa_pairwise"
+ "fipspost_post_mlkem_pairwise"
```
