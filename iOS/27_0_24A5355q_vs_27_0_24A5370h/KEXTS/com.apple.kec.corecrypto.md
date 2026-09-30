## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-2097.0.0.0.0
-  __TEXT.__cstring: 0x4d8c sha256:a39380a9ea6b971c2ab5a5801e404cbc27dfcdc7d0b038f85eb8d14174e593bd
+2109.0.7.0.0
+  __TEXT.__cstring: 0x4567 sha256:3944c320c26dd3463ac91220f968be0061217352311c2cbf33f2545d4f822bbf
   __TEXT.__const: 0x1b5a0 sha256:afe45cffcb87cdd72871cfbcea0e5c535b372efaca1e14845e047bf5dad84327
-  __TEXT.__fips_hmacs: 0x20 sha256:5f3530ecdaf5af79f981387313f088c6e49eb6cc542708d427a078198256e4af
-  __TEXT_EXEC.__text: 0x6db84 sha256:c79e9e3dc8a7b4e5000f667b1db272f39a024e39a3a7be6ffd3757883707b2af
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x9340 sha256:8b25a472d5b4e2a783049c69bdfc84a17a02c39656506b7e57de1155c6b0fdbd
+  __TEXT.__fips_hmacs: 0x20 sha256:f901682eecfe538c84dcd2d91e5be26a633669b6ec04744f1f8849498f2586cb
+  __TEXT_EXEC.__text: 0x6fe68 sha256:cf7297275e5fa2668ee3af6a479d56273ff8a4e9e438ebfacc60112f742b990b
+  __TEXT_EXEC.__auth_stubs: 0x250 sha256:4555c5d5bdead454be072e3241e6ce3bfb4885f0ccb8f58ed94917777dfedd6e
+  __DATA.__data: 0x9340 sha256:de1d7da37e813d350f628f855a7026f84d838b60865fa7be2943b4794509e57c
   __DATA.__bss: 0x2a00 sha256:ee0d534dd385f4c26c52ee121654897b783c0754c6512886e53578dce4b24735
   __DATA.__common: 0x140 sha256:7b6436b0c98f62380866d9432c2af0ee08ce16a171bda6951aecd95ee1307d61
-  __DATA_CONST.__const: 0x42a8 sha256:10553fb1f50151412cba3d23f6e04dd3feb4b34995b7d574dbecfe49b262de00
-  __DATA_CONST.__auth_got: 0x128 sha256:58ca5c7d6b141df3c05712f8498901bfc6ecd7c2e330798b31da492a1367c955
-  __DATA_CONST.__got: 0x10 sha256:a4bdd3fe2c1d28853456dc2136bf130c1f42622b356f393bda41bf172cf62586
-  __DATA_CONST.__auth_ptr: 0x190 sha256:1505da9d009d1c8ac5a596cfdb701625826fa2b0e0cb26371e822315e75d2ba2
-  UUID: 8A881D11-8D6A-356B-92EF-C2C6E52A4443
-  Functions: 1960
+  __DATA_CONST.__const: 0x4218 sha256:6d0933b94ddbd3a83fac2e23a0c3726808f1e6afd9cd2a639b33c7edf656c7e1
+  __DATA_CONST.__auth_got: 0x128 sha256:e5c87458b5019808e8a9129a320eaf305447650994c124d4fdead37fa2f8da0e
+  __DATA_CONST.__got: 0x10 sha256:41e5b15e06f3ab7671bb59f6ef675df9bf5b380c049793e5682a44883f9be95a
+  __DATA_CONST.__auth_ptr: 0x190 sha256:b8d1f117b7f115701206f1e1bee3d68bb877d1ff6361688ee76e725c25db98d4
+  UUID: 93E50159-261F-3608-BC37-EEBC0074037D
+  Functions: 1993
   Symbols:   0
-  CStrings:  470
+  CStrings:  443
 
CStrings:
+ "27.0"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: %s: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate_masked: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - %s\n"
+ "fipspost_post_aes_ecb"
+ "fipspost_post_ecdh"
+ "fipspost_post_ecdsa"
+ "fipspost_post_indicator"
+ "fipspost_post_rsa_sig"
+ "fipspost_run_post"
- "26.0"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_aes_cbc: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_aes_ccm: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_aes_cmac: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_aes_ecb: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_aes_gcm: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_aes_xts: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_drbg_ctr: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_drbg_hmac: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_ecdh: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_ecdsa: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_hkdf: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_hmac: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_indicator: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_integrity: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_kdf_ctr: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_kdf_ctr_cmac: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_pbkdf: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: fipspost_post_rsa_sig: %d\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_cbc\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_ccm\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_cmac\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_ecb\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_gcm\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_xts\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_drbg_ctr\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_drbg_hmac\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_ecdh\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_ecdsa\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_hkdf\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_hmac\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_indicator\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_integrity\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_kdf_ctr\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_kdf_ctr_cmac\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_pbkdf\n"
- "FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_rsa_sig\n"

```
