## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-2097.0.0.0.0
-  __TEXT.__text: 0x8b42c sha256:fea95d5f693377cce0302ae4686f9cae6974ef2a32900aa2a4fdb5829e60ed7c
-  __TEXT.__cstring: 0x5fa1 sha256:79d1aaf283061b684c4661f722b90a57dbb209f308adc6fb606749d2b99e906b
-  __TEXT.__const: 0x20488 sha256:c3144516dedc8411737e1bc3d0337e31ff206e7ab67307ce45a0a0544b56dedb
-  __TEXT.__fips_hmacs: 0x20 sha256:6c3610e23989c56fd1b2f6ebeb7f32ccad6c39cecf55dfb8e80635f656f7dace
+2109.0.7.0.0
+  __TEXT.__text: 0x8cd6c sha256:9c48074f1239113b9fa840b57d2b4b25274f8a3bce595122121830a4cc3e9ca0
+  __TEXT.__cstring: 0x5534 sha256:e6e3396eee24396d73ad608c389b1e11a38363d1653ae92cd021ef3ee9f0588e
+  __TEXT.__const: 0x20488 sha256:e1c6f5ca3432ec6ec1a2df8aa532d938fd9dd5cc82e2b5210213e1044ef5c7d0
+  __TEXT.__fips_hmacs: 0x20 sha256:2d2f67593e71e182cc088a5466ff8acb00e2f711cfecdb07661cd183b2e1a408
   __TEXT.__oslogstring: 0x60 sha256:78e974179b007217d55508910e62a9486547baf68b8e3aea9812d2437b46e85a
-  __TEXT.__unwind_info: 0x1cd0 sha256:101fb003dab5d56e7c8ffc9231fecc1fd61672f7b8ca5f04c17fa588adb5c624
-  __TEXT.__eh_frame: 0x3d8 sha256:440ae5160a9dc62a83bf2e135cdb4bd8eb255b7e37ceeaf3d39d35a5fc66900c
+  __TEXT.__unwind_info: 0x1ce8 sha256:5db7e0788662967a3598d6b652303be6d66bfa24a0821397126e0127a438dc00
+  __TEXT.__eh_frame: 0x3d8 sha256:c8cbb99eeb2cd533b0daf4e554f839c947d590dd05067b58e6aa7c149b845941
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x21b0 sha256:e3319ea6a98daeeaee50038e6c25e693331834e0de5e3cd1a20f8d2776138633
+  __DATA_CONST.__const: 0x1ec8 sha256:7cf1d97554e2b122865203014e2f351abdf946f3dec0b8fb98385eafaa31cf59
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x22c8 sha256:3738c90217dfce3524f9d247281d6b87c0577f0ea528524b1446005e21978429
+  __AUTH_CONST.__const: 0x23b8 sha256:2a499b5382244b0cf1e86bb7aec26f03b017ee16d6c490051b51522ee035130d
   __AUTH_CONST.__auth_got: 0x118 sha256:1f6c9de2e555d5d589e1149fed58f9cbcc101739df97d4a4d694a13f1242c5b9
-  __AUTH.__data: 0x118 sha256:39aafe3fa8fd0d1f46713cdd28c062af1e2d08850dcff62143c66ce282b7d9da
-  __DATA.__data: 0x6858 sha256:fad3390eaad902857a37355f553972dc9322d6143f9c04e2dbb8fe3108695e6a
+  __AUTH.__data: 0x148 sha256:bc4703e96dde3ae09afb551c76f077002ea7828de665a2c7f9289dafbbc9edcf
+  __DATA.__data: 0x6858 sha256:22ff5ac22c8527b0d396ebab0ba5f74d53706c346638e237f2af28b0f40476b9
   __DATA.__bss: 0xef0 sha256:6fb704e5fcf552d284809d537774b3677c2cbc1b7f845efd72eccce9203f3510
   __DATA.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   __DATA_DIRTY.__data: 0x8 sha256:7c9fa136d4413fa6173637e883b6998d32e1d675f88cddff9dcbcf331820f4b8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 08F864CD-E96A-3789-BF1A-AD0101E4FEB3
-  Functions: 2597
-  Symbols:   3134
-  CStrings:  553
+  UUID: 4444A888-FF62-30E1-9378-EE4E70E6A89C
+  Functions: 2639
+  Symbols:   3180
+  CStrings:  519
 
Symbols:
+ AccelerateCrypto_ccmlkem_ntt_inverse_2
+ AccelerateCrypto_ccmlkem_ntt_inverse_3
+ _AccelerateCrypto_ccmlkem_ntt_forward
+ _AccelerateCrypto_ccmlkem_ntt_forward_cbd_eta2
+ _AccelerateCrypto_ccmlkem_ntt_inverse
+ _AccelerateCrypto_ccmlkem_poly_add
+ _AccelerateCrypto_ccmlkem_poly_compress_encode_d1
+ _AccelerateCrypto_ccmlkem_poly_compress_encode_d10
+ _AccelerateCrypto_ccmlkem_poly_compress_encode_d11
+ _AccelerateCrypto_ccmlkem_poly_compress_encode_d4
+ _AccelerateCrypto_ccmlkem_poly_compress_encode_d5
+ _AccelerateCrypto_ccmlkem_poly_decode_d12
+ _AccelerateCrypto_ccmlkem_poly_decode_decompress_d1
+ _AccelerateCrypto_ccmlkem_poly_decode_decompress_d10
+ _AccelerateCrypto_ccmlkem_poly_decode_decompress_d11
+ _AccelerateCrypto_ccmlkem_poly_decode_decompress_d4
+ _AccelerateCrypto_ccmlkem_poly_decode_decompress_d5
+ _AccelerateCrypto_ccmlkem_poly_encode_d12
+ _AccelerateCrypto_ccmlkem_poly_reduce
+ _AccelerateCrypto_ccmlkem_poly_sub
+ _AccelerateCrypto_ccmlkem_poly_toplant
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
- ccmlkem_ntt_forward_2
- ccmlkem_ntt_forward_3
- ccmlkem_ntt_inverse_2
- ccmlkem_ntt_inverse_3
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
