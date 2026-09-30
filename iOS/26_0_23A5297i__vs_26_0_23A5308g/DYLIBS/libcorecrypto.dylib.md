## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1922.0.17.0.0
-  __TEXT.__text: 0x84f90
+1922.0.25.0.0
+  __TEXT.__text: 0x851f0
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__cstring: 0x5862
-  __TEXT.__const: 0x19a38
+  __TEXT.__cstring: 0x5f4d
+  __TEXT.__const: 0x1e328
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
   __TEXT.__unwind_info: 0x1988
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0xf50
+  __DATA_CONST.__const: 0x2208
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x1ea8
   __AUTH.__data: 0xb8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 48763905-B8AF-33CE-902B-2CFC0DC9E9CB
-  Functions: 2429
-  Symbols:   4363
-  CStrings:  502
+  UUID: 57CBC909-23D5-3FB0-89EA-7E87F8D8507B
+  Functions: 2432
+  Symbols:   4384
+  CStrings:  545
 
Symbols:
+ _d_kat
+ _ek_kat
+ _fips_allowed_algs
+ _fips_allowed_drbgs
+ _fips_allowed_modes
+ _fipspost_post_mldsa
+ _fipspost_post_mlkem
+ _fipspost_post_mlkem_decapsulate
+ _msg_kat
+ _privkey_kat
+ _pubkey_kat
+ _seed_kat
+ _sig_kat
+ _sig_rng_kat
+ _sk_kat
+ _sk_rej_kat
+ _z_kat
CStrings:
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid ek_kat: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid privkey_kat: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid pubkey_kat: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid sk_kat: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_derive_key_from_seed: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_privkey: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_pubkey: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_verify: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_encapsulate_msg: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_keypair_from_seed: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_mldsa: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_mlkem: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch ek: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch privkey: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch pubkey: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sig: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sk: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_mldsa\n"
+ "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_mlkem\n"
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
+ "fipspost_post_mldsa_keygen"
+ "fipspost_post_mldsa_sign_kat"
+ "fipspost_post_mldsa_verify_kat"
+ "fipspost_post_mlkem_decapsulate"
+ "fipspost_post_mlkem_encapsulate"
+ "fipspost_post_mlkem_keygen"

```
