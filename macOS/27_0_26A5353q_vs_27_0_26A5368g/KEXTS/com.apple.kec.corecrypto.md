## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-2097.0.0.0.0
-  __TEXT.__cstring: 0x4d90 sha256:5e091e2a61b442df9f268e05814934a73b7c8533a675ee028aeeabb90cd4f511
+2109.0.7.0.0
+  __TEXT.__cstring: 0x456b sha256:3baeae6ab673c6a6417b0884bc84f348795d353a8f7a5b6a9e2f2ff19fd9cd49
   __TEXT.__const: 0x1b5a0 sha256:afe45cffcb87cdd72871cfbcea0e5c535b372efaca1e14845e047bf5dad84327
-  __TEXT.__fips_hmacs: 0x20 sha256:620b64d9842ab7a5c6e5065a5977f963cb3b9e213a8ed7170c3fa0467c46d38f
-  __TEXT_EXEC.__text: 0x6d9fc sha256:84a5850af7ddee439f25049636d076d2a1d4877452e5b1c1ba17a66bbb076ce5
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x9340 sha256:51c3b791e799262d3c837e8fcdc35ca53f88cae2bacef66fb927dfdd6f64e0c8
+  __TEXT.__fips_hmacs: 0x20 sha256:f985782df798ed5e2bce0edd9a519b974fd02e023481b97a74e2648d96edc847
+  __TEXT_EXEC.__text: 0x6fd08 sha256:d811fb33833c93e157fdede13c513a56afb750a695c75ed8fa55abbe5988b193
+  __TEXT_EXEC.__auth_stubs: 0x250 sha256:24cf313399a98ff2180cccbe30d53776986ba56079c0918f26d52e632a1dfeb4
+  __DATA.__data: 0x9340 sha256:abc6b64a1a52fcc67d5074e43877dbb97989782aa439ac74da28fc579623a332
   __DATA.__bss: 0x2a00 sha256:ee0d534dd385f4c26c52ee121654897b783c0754c6512886e53578dce4b24735
   __DATA.__common: 0x140 sha256:7b6436b0c98f62380866d9432c2af0ee08ce16a171bda6951aecd95ee1307d61
-  __DATA_CONST.__const: 0x42a8 sha256:fbe29c49c87d289d8cf79527ca2f2122170f0f5bcc1444d93ceb91203036eacb
-  __DATA_CONST.__auth_got: 0x128 sha256:470fc64581036d0fe37b2b91329895ddcb11497b95dfca1c871cf7196fea7f74
-  __DATA_CONST.__got: 0x10 sha256:331466acabb828a38a3d45e678b02479ae2bd5e5ce6c5e3ed0baab03d30cc6df
-  __DATA_CONST.__auth_ptr: 0x190 sha256:7dfb5f30f53b3831454ff80a0e6d54f148bc2c6169b22d02969d07c3fd431fc8
-  UUID: 4FBEE9B4-A528-3A8E-896A-CC2381A69B96
-  Functions: 1959
-  Symbols:   2509
-  CStrings:  470
+  __DATA_CONST.__const: 0x4218 sha256:ea150453645ccd6f94e611d1062f61c14a83302938552af3693d8ac8deabab38
+  __DATA_CONST.__auth_got: 0x128 sha256:ecc43e8a24cbd3900802e6154c731d9b56e1497118bb4618e1252eab3cbd3d64
+  __DATA_CONST.__got: 0x10 sha256:6e7ed9684b8b3c4d9474aa0d12037eff039e831ad855c855e21bfbaf690cf53b
+  __DATA_CONST.__auth_ptr: 0x190 sha256:92a3ef3cfab5d66bccce92f97a0d7a3538fc109f8b1e74ad8ca2f5d8e121e0f8
+  UUID: CAD16FE3-4486-338D-B2D8-2024749BB037
+  Functions: 1992
+  Symbols:   2544
+  CStrings:  443
 
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
+ _cckeccak_absorb_and_pad_internal
+ _cckeccak_absorb_blocks_internal
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
