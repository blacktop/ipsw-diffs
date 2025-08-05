## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-1922.0.17.0.0
-  __TEXT.__cstring: 0x48a8
-  __TEXT.__const: 0x14e70
+1922.0.25.0.0
+  __TEXT.__cstring: 0x4d56
+  __TEXT.__const: 0x19760
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x6a5d0
+  __TEXT_EXEC.__text: 0x6a720
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x9340
   __DATA.__bss: 0x29e0
   __DATA.__common: 0x140
   __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__auth_ptr: 0x168
-  __DATA_CONST.__const: 0x3388
-  UUID: FAD1E9FE-7559-3172-9B5A-F8DCAEB46A2C
-  Functions: 1817
+  __DATA_CONST.__auth_ptr: 0x178
+  __DATA_CONST.__const: 0x3f38
+  UUID: 38B27D30-6B6B-392D-B8AB-EED407291878
+  Functions: 1820
   Symbols:   0
-  CStrings:  441
+  CStrings:  464
 
CStrings:
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid ek_kat: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid privkey_kat: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid pubkey_kat: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid sk_kat: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_derive_key_from_seed: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_export_privkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_export_pubkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_verify: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_encapsulate_msg: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_keypair_from_seed: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch ek: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch privkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch pubkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch sig: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch sk: %d\n"
+ "fipspost_post_mldsa_keygen"
+ "fipspost_post_mldsa_sign_kat"
+ "fipspost_post_mldsa_verify_kat"
+ "fipspost_post_mlkem_decapsulate"
+ "fipspost_post_mlkem_encapsulate"
+ "fipspost_post_mlkem_keygen"

```
