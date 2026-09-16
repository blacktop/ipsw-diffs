## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-2109.0.22.0.0
-  __TEXT.__cstring: 0x4479
-  __TEXT.__const: 0x10180
+2109.40.15.0.0
+  __TEXT.__cstring: 0x453c
+  __TEXT.__const: 0x101e0
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x6cdf8
+  __TEXT_EXEC.__text: 0x6d240
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0x29e0
   __DATA.__common: 0x18
-  __DATA_CONST.__const: 0x3fb8
+  __DATA_CONST.__const: 0x3fd8
   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x188
-  Functions: 1949
+  Functions: 1956
   Symbols:   0
-  CStrings:  368
+  CStrings:  371
 
CStrings:
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign (rejection, ML-DSA-44): %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch rejection sig (ML-DSA-44): %d\n"
+ "fipspost_post_mldsa_sign_rejection_kat_44"
```
