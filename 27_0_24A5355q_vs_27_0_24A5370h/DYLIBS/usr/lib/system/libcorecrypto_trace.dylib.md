## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-2097.0.0.0.0
-  __TEXT.__text: 0x8bb48 sha256:f60d43e6b43d5ed9ac30a666794bc2841ffc6367da47a24a0ea2bd3250a34944
-  __TEXT.__cstring: 0x62bd sha256:57f1ac2be47c3cba9cc5fcba837d8e5aafcc38509ee146812d7c6506aa0d8502
-  __TEXT.__const: 0x20498 sha256:517cc32235806d0c8a2c5bdb0a7dd187d7fcb56eabc9ca6252d4d5162ecd00d2
-  __TEXT.__fips_hmacs: 0x20 sha256:c598aaeed29087600a15535a0f6b0930858ef19cb5b3513c89d14b834509ba47
+2109.0.7.0.0
+  __TEXT.__text: 0x8cfec sha256:5f344678389bdd96057f63e0058cb6241ad5e29c6b8cc9b686a76761465bcd87
+  __TEXT.__cstring: 0x57a3 sha256:5cec1e59d8c0038ff846bdd146053a37b9f8f6440013bb12659879ec71bffd29
+  __TEXT.__const: 0x20498 sha256:5b427ca1ce0463f6458a7a83ade41ab5921b34f23e2fe2593112ae7aaf91d496
+  __TEXT.__fips_hmacs: 0x20 sha256:eebe92f919d618f5925eb8e71b475990e746df2f144b07f4b5f75e42bf826e49
   __TEXT.__oslogstring: 0x60 sha256:78e974179b007217d55508910e62a9486547baf68b8e3aea9812d2437b46e85a
-  __TEXT.__unwind_info: 0x1d38 sha256:6a5a163811f3db87c4ccab5f4768f6c9d592f2abacb113195834ddc56d1d44c8
-  __TEXT.__eh_frame: 0x3a0 sha256:0b2574f3c1575abbf8cf376096f2cb799f7da398315dccf2b6fda300f63df0e8
+  __TEXT.__unwind_info: 0x1d60 sha256:b5c4aed90d155ae71f12954d40df2e1fc23538dbe101f2edb15f514aa675a2cd
+  __TEXT.__eh_frame: 0x3a0 sha256:c0fb07cdebc2ff934d8d8926f8fb64e8789c1b9ca425b1430529351d65219136
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x21b0 sha256:87a1c96d2683ea6e98e6cf651ec560308945eaecface5ab65986ebf7c4dac9c6
+  __DATA_CONST.__const: 0x1ec8 sha256:2d3c306229cd92cee0344f5695d3ddd7e0fd179304036a017a8c5067e5ddb958
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x22c8 sha256:f30be4691517640cbcf23e93fd650b3f86cadb4221010ea8187269d164f977bd
+  __AUTH_CONST.__const: 0x23b8 sha256:015c00312ac3a9d25b6748e0d12e749a4d2b1dfee4bc0b01b0a9ef771981720c
   __AUTH_CONST.__auth_got: 0x118 sha256:1f6c9de2e555d5d589e1149fed58f9cbcc101739df97d4a4d694a13f1242c5b9
-  __AUTH.__data: 0x130 sha256:008e396a4dcc0e5c31df4afc1cba3a1b6a3ad9ae17cbc51113cd9847dfc7a0d0
-  __DATA.__data: 0x6868 sha256:a76e899119f73728ae98c72409ba0730fa71948aa7c9cdbd675b1b46cc79de25
+  __AUTH.__data: 0x160 sha256:ae06d45101db56b05f5f0ed8a9d489861775a7f7ca5b9a1998e8b43938fec8a7
+  __DATA.__data: 0x6868 sha256:b81058ee8b0ffafd30b88bc686b06d93e1aca58036eeee21fc6b0e856f8b17a3
   __DATA.__bss: 0x20d0 sha256:8d2230968bb2dbe1a7b9a4e594a7c4ac1dc07cafa8733d85a55e2d7630ee3b80
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 1C28C7D6-0ADC-38D1-B6DB-98C07FC43A04
-  Functions: 2603
-  Symbols:   4722
-  CStrings:  585
+  UUID: 2A0D4045-B8D3-318A-9D43-3DD78500425A
+  Functions: 2647
+  Symbols:   4810
+  CStrings:  543
 
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
