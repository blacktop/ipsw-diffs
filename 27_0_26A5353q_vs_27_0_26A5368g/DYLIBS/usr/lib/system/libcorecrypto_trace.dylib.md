## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-2097.0.0.0.0
-  __TEXT.__text: 0x8bf24 sha256:ead1b7ce6de5f78b7f6fafdef39dc7b3e2ef904b045c56a489d9cb004c51b895
-  __TEXT.__cstring: 0x62c1 sha256:c10545cfc3414d126b5d52e9096467b156d01f11634186654bce690364525f83
-  __TEXT.__const: 0x20498 sha256:517cc32235806d0c8a2c5bdb0a7dd187d7fcb56eabc9ca6252d4d5162ecd00d2
-  __TEXT.__fips_hmacs: 0x20 sha256:eeb4d41ec707b159b08819a2a29b19fc59e961792af1fdb17c8a7e768e77159c
+2109.0.7.0.0
+  __TEXT.__text: 0x8d564 sha256:6bbf65b9c56391f3824767879966be8d1d780547ef9dac1df119e823a1d46075
+  __TEXT.__cstring: 0x57a7 sha256:69f44fbfe628da87bf0656ffb6c4c3f361dc4275d8052a42ec61c4a24eb35b71
+  __TEXT.__const: 0x20498 sha256:5b427ca1ce0463f6458a7a83ade41ab5921b34f23e2fe2593112ae7aaf91d496
+  __TEXT.__fips_hmacs: 0x20 sha256:8e6fff4fa95a63d27033f7423cc260512dea6ee7c245f9d21dc4cc01fca7cb28
   __TEXT.__oslogstring: 0x60 sha256:78e974179b007217d55508910e62a9486547baf68b8e3aea9812d2437b46e85a
-  __TEXT.__unwind_info: 0x1d38 sha256:6b709f3d96a16777d3cf60fc17c4c03622eff7eaba0ece17a910e0b9ccc7c15f
-  __TEXT.__eh_frame: 0x3d8 sha256:2e7b1a03f183a863f663b883a2cfafc5ad42ea7c4dbc1042a8ece2f7c5fdb491
+  __TEXT.__unwind_info: 0x1d68 sha256:761e13e91886fd07503c87793f08a962483779d51b15e5315c72c0084a3c402a
+  __TEXT.__eh_frame: 0x3d8 sha256:e9e23fd2643042918597f8e42d0911b499bce5ea73491a495fe6a028d85aec5b
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x21b0 sha256:4a1b635087e2eff677be9a84f3c4413c8f41aef9e24ea89215c294d85c9c1e2a
+  __DATA_CONST.__const: 0x1ec8 sha256:b0596cee59f97f2c2754c6a6ca65d9b771902fbf7679f71cf6d264e33809642e
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x22c8 sha256:52cd05af62522fc8bfdef099130e2f72463f6f078e994112d9e2df8627e3332c
+  __AUTH_CONST.__const: 0x23b8 sha256:8cb9fd591a7669ec67ef557767daf9f6862924c51fa27c5a67c3d519982d64c3
   __AUTH_CONST.__auth_got: 0x118 sha256:1f6c9de2e555d5d589e1149fed58f9cbcc101739df97d4a4d694a13f1242c5b9
-  __AUTH.__data: 0x130 sha256:19038e80df01f5c968fce7b7a9116c7e758220b974c6bb58a83179baaf860b5e
-  __DATA.__data: 0x6868 sha256:bc0a8c93d4faaa516c16efd6f75707a16ab4a39178b42efe8e995d6dffc63e46
+  __AUTH.__data: 0x160 sha256:ed30f5005f7f23dbab238a90aa1c0fee12be2638ae949285a394ada4bfa75b9a
+  __DATA.__data: 0x6868 sha256:f949539ec64b4e2bb6066459e90267855de9be6a69973aff55c7f451408644d3
   __DATA.__bss: 0x20d0 sha256:8d2230968bb2dbe1a7b9a4e594a7c4ac1dc07cafa8733d85a55e2d7630ee3b80
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 8AA643EF-74A6-3C17-83CF-F16435899E2C
-  Functions: 2601
-  Symbols:   3147
-  CStrings:  585
+  UUID: DA41DBEB-1A4E-34CC-ACA9-9AD70FD6612B
+  Functions: 2642
+  Symbols:   3193
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
