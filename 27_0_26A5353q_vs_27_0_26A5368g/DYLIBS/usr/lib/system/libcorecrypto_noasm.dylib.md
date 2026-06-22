## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-2097.0.0.0.0
-  __TEXT.__text: 0x86658 sha256:a6a25f6ff255cd9edef4d7d72cfd319307379785426a8e349d105722c6b80d27
-  __TEXT.__const: 0x201e8 sha256:5e0d6b309cfa4a2c23e58d5381817e808950b4243e316975e3b59cdb0edd0c51
-  __TEXT.__cstring: 0x5fa1 sha256:ff03fdf3573bea4d70047460483b0d7c0474df4a3f211afed04043aa14da91b2
-  __TEXT.__fips_hmacs: 0x20 sha256:30a15a972e4cfcff00d9c4122b13416083aac902de0aec2fcf39ffe26565ff27
+2109.0.7.0.0
+  __TEXT.__text: 0x88b5c sha256:4775e19efd81feea1d7016f5efb46d7293e9aa3c571fca148828d05d15dff360
+  __TEXT.__const: 0x201e8 sha256:df4c9075c0f0b7256583026d9009828f3e6386204c884c8ce872212145cddb44
+  __TEXT.__cstring: 0x5534 sha256:ff3de113e0afe09a9efde373c86734089f73bd0b719bc3f0a9863e02e2b8c40c
+  __TEXT.__fips_hmacs: 0x20 sha256:a088dfc29655811c1d4496bdb288489f361f4ace32461df56bfffaab8d39b50c
   __TEXT.__oslogstring: 0x60 sha256:78e974179b007217d55508910e62a9486547baf68b8e3aea9812d2437b46e85a
-  __TEXT.__unwind_info: 0x1c08 sha256:a2065ad6ffbf83d852ef715b431a3add9be2760bf64ab31561ae4767a7303a2a
-  __TEXT.__eh_frame: 0x3d8 sha256:3f3c240617d5cb95ef1b8b0c9e87d547135ee43e589792c7e3e1b1612f2e76bf
+  __TEXT.__unwind_info: 0x1c30 sha256:b943e1980d4c0079ff0f925074405f695a6818edc985c0cbc54bf2aa28e027f2
+  __TEXT.__eh_frame: 0x490 sha256:59967c29806437624a18a254edda0cf7fd0eb991e827934f5d7a70c86c0559b7
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x21b0 sha256:f933c1210ae7a0ccc425f93022ca6b7e9237e5291c15cd1e1dfa7e8914b9b124
+  __DATA_CONST.__const: 0x1ec8 sha256:1232ea8de5bfdd1e3dad463bef6b91f1f86cab2e96d11cd52bf9473ee8146464
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1980 sha256:698bcec5b1d6f041ce04bd4e4ce618fcce092f7b9ccbe0c0ded2ee0d63847c55
+  __AUTH_CONST.__const: 0x1a70 sha256:e0a711495aad91e28ea470a43f299e34d438699510b93cdafb2d74e442f59b40
   __AUTH_CONST.__auth_got: 0x118 sha256:1f6c9de2e555d5d589e1149fed58f9cbcc101739df97d4a4d694a13f1242c5b9
-  __AUTH.__data: 0x118 sha256:12be7717dfce68547c053efff35d5234adc989e08ada60da1713d50f78d5e1df
-  __DATA.__data: 0x6860 sha256:3aa76b2bf6b4925fc92d8bb125fdb417b2bf5d2773f332c2a8c47679bb87ddbc
+  __AUTH.__data: 0x148 sha256:3461be9b077f2063cdf8253161f8dbdc5c0131153d8f2346f33714e7ebdf9098
+  __DATA.__data: 0x6860 sha256:4d5e5ea1e70f64c6cf92179413ab0841c53f60514d532209b64645351dbd71bd
   __DATA.__bss: 0x1a38 sha256:054249310193267110a4519d47f46913a45ba0ff248832e8ee86ba2a3697e713
   __DATA.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 1B860849-A15D-3E75-8E4F-38B5364154AC
-  Functions: 2458
-  Symbols:   2964
-  CStrings:  553
+  UUID: EEA560B1-13CA-39D4-954A-39A51D9DB9F5
+  Functions: 2483
+  Symbols:   2993
+  CStrings:  519
 
Symbols:
+ _OUTLINED_FUNCTION_8
+ _cc_free
+ _cckeccak_absorb_and_pad_internal
+ _cckeccak_f1600_masked_c
+ _cckeccak_oneshot_masked
+ _cckeccak_squeeze_internal
+ _cckeccak_theta
+ _cckem_mlkem1024_decapsulate_unmasked
+ _cckem_mlkem1024_unmasked
+ _cckem_mlkem1024_unmasked_info
+ _cckem_mlkem768_decapsulate_unmasked
+ _cckem_mlkem768_unmasked
+ _cckem_mlkem768_unmasked_info
+ _ccmlkem_decompress_coefficient
+ _ccmlkem_hash_g_masked
+ _ccmlkem_indcpa_decrypt_masked_ws
+ _ccmlkem_indcpa_encrypt_masked_ws
+ _ccmlkem_kem_decapsulate_masked
+ _ccmlkem_poly_compress_encode
+ _ccmlkem_poly_compress_encode_d1
+ _ccmlkem_poly_compress_encode_d10
+ _ccmlkem_poly_compress_encode_d11
+ _ccmlkem_poly_compress_encode_d1_masked
+ _ccmlkem_poly_compress_encode_d4
+ _ccmlkem_poly_compress_encode_d5
+ _ccmlkem_poly_decode_d12
+ _ccmlkem_poly_decode_decompress
+ _ccmlkem_poly_decode_decompress_d1
+ _ccmlkem_poly_decode_decompress_d10
+ _ccmlkem_poly_decode_decompress_d11
+ _ccmlkem_poly_decode_decompress_d1_masked
+ _ccmlkem_poly_decode_decompress_d4
+ _ccmlkem_poly_decode_decompress_d5
+ _ccmlkem_poly_encode_d12
+ _ccmlkem_polyvec_compress_encode
+ _ccmlkem_polyvec_decode_d12
+ _ccmlkem_polyvec_decode_decompress
+ _ccmlkem_polyvec_encode_d12
+ _ccspake_mac_nistkdf_cmac_aes128_sha256
+ _ccspake_mac_nistkdf_cmac_aes128_sha256_decl
+ _ccspake_mac_nistkdf_cmac_compute
+ _ccspake_mac_nistkdf_derive
+ _fipspost_post_run_all
+ _fipspost_run_post
- _ccmlkem_poly_compress
- _ccmlkem_poly_compress_d1
- _ccmlkem_poly_compress_d10
- _ccmlkem_poly_compress_d11
- _ccmlkem_poly_compress_d4
- _ccmlkem_poly_compress_d5
- _ccmlkem_poly_decode
- _ccmlkem_poly_decompress
- _ccmlkem_poly_decompress_d1
- _ccmlkem_poly_decompress_d10
- _ccmlkem_poly_decompress_d11
- _ccmlkem_poly_decompress_d4
- _ccmlkem_poly_decompress_d5
- _ccmlkem_poly_encode
- _ccmlkem_polyvec_compress
- _ccmlkem_polyvec_decode
- _ccmlkem_polyvec_decompress
- _ccmlkem_polyvec_encode
CStrings:
+ "27.0"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: %s: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate_masked: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - %s\n"
+ "fipspost_post_aes_ecb"
+ "fipspost_post_ecdh"
+ "fipspost_post_ecdsa"
+ "fipspost_post_indicator"
+ "fipspost_post_mldsa"
+ "fipspost_post_mlkem"
+ "fipspost_post_rsa_enc_dec"
+ "fipspost_post_rsa_sig"
+ "fipspost_run_post"
- "26.0"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_aes_cbc: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_aes_ccm: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_aes_cmac: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_aes_ecb: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_aes_gcm: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_aes_xts: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_drbg_ctr: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_drbg_hmac: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_ecdh: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_ecdsa: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_ffdh: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_hkdf: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_hmac: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_indicator: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_integrity: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_kdf_ctr: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_kdf_ctr_cmac: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_mldsa: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_mlkem: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_pbkdf: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_enc_dec: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_sig: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_shake: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_cbc\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_ccm\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_cmac\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_ecb\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_gcm\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_aes_xts\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_drbg_ctr\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_drbg_hmac\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_ecdh\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_ecdsa\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_ffdh\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_hkdf\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_hmac\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_indicator\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_integrity\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_kdf_ctr\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_kdf_ctr_cmac\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_mldsa\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_mlkem\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_pbkdf\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_rsa_enc_dec\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_rsa_sig\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_shake\n"

```
