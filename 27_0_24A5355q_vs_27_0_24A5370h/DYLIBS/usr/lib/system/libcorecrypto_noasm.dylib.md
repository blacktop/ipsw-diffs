## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-2097.0.0.0.0
-  __TEXT.__text: 0x85464 sha256:cbf066f788a38f0ef61d81b14dd00b29676bfe6ae84fded3285151f56c7c66ea
-  __TEXT.__const: 0x201e8 sha256:5e0d6b309cfa4a2c23e58d5381817e808950b4243e316975e3b59cdb0edd0c51
-  __TEXT.__cstring: 0x5f9d sha256:8bd4bc847230b4478a5fe1264569d6bf0ff1231b5192be4e846d370120778ece
-  __TEXT.__fips_hmacs: 0x20 sha256:53cdd95f37fc9106230e42770bdaa885aebffb7a49332fa9759fd860a325e7b6
+2109.0.7.0.0
+  __TEXT.__text: 0x8743c sha256:a78525fc315ac084499e8d7c9501fb0e80a4adc900ce5e198a882fe5bed47943
+  __TEXT.__const: 0x201e8 sha256:12eab47955062725f611bcabec5def9a55aed1a00732c76de62eb47b259314d4
+  __TEXT.__cstring: 0x5530 sha256:95d744d9d6538d4052c0c85c540defd3846c6b984e61dd2407b0449a5070a684
+  __TEXT.__fips_hmacs: 0x20 sha256:b1a861d0246ea988f1b9a3047045cb4f7ac56ae4f4b371eeae167e90bf6baa09
   __TEXT.__oslogstring: 0x60 sha256:78e974179b007217d55508910e62a9486547baf68b8e3aea9812d2437b46e85a
-  __TEXT.__unwind_info: 0x1c20 sha256:57943afeb6106c75d98d116505973113a8a80618600321086b59ef9b7f2cb7dd
-  __TEXT.__eh_frame: 0x3a0 sha256:1721c9c9f0bbf925cf34f4464576e2feaa7b257f0ed53112593b36d6b8adb0af
+  __TEXT.__unwind_info: 0x1c40 sha256:da3ab24bed2a3f8beaf42141a40bf5d559170b1f2180c24332d8d89e81278199
+  __TEXT.__eh_frame: 0x488 sha256:c3c18c3b2998e928ceb601b628f1f53cb39eae2f47ce45f4ff7c68f2e62745ce
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x21b0 sha256:bd3b978d847c5ccaf22a1496d8b41934006550559af312e3c5b1f58da1a6958a
+  __DATA_CONST.__const: 0x1ec8 sha256:2eebf6578182e1321d312e25c31212350009828de663ab7577e57a553cb077b7
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1980 sha256:961618358690e8ed8d3ae42e8f69cd28b2ab6eb18aa8843f6b9f98a6155ba054
+  __AUTH_CONST.__const: 0x1a70 sha256:533f8c67acf629f18c3c15a8ee234c005759205a356ac52d476f61f4c9ee2f41
   __AUTH_CONST.__auth_got: 0x118 sha256:1f6c9de2e555d5d589e1149fed58f9cbcc101739df97d4a4d694a13f1242c5b9
-  __AUTH.__data: 0x118 sha256:cf9dd9e46fbd7b39c39ea81f4b0ce4f6a8ad1bca0f49a318714b5c0ac586792e
-  __DATA.__data: 0x6860 sha256:a801434b0e85177167d0bd249f625f0a434caccc46a971f68a4fa6ba742f2a61
+  __AUTH.__data: 0x148 sha256:c1f34c49ae915c8e9913d6f12755edeb0ad1eb936735b3d8bb52a6e6ce92ae0d
+  __DATA.__data: 0x6860 sha256:cb9fef049e3668f244159d6c4533a2cf146e6f4f2198d0b4d9b77ac2a3c6974e
   __DATA.__bss: 0x1a38 sha256:054249310193267110a4519d47f46913a45ba0ff248832e8ee86ba2a3697e713
   __DATA.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: E7239B92-8B89-32E8-B740-15468E3839E5
-  Functions: 2460
-  Symbols:   4400
-  CStrings:  553
+  UUID: F4933154-5C39-3556-8BCE-12B1233B0A3E
+  Functions: 2487
+  Symbols:   4454
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
