## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1922.60.4.0.0
-  __TEXT.__text: 0x86254
+1922.60.11.0.0
+  __TEXT.__text: 0x86688
   __TEXT.__auth_stubs: 0x230
   __TEXT.__cstring: 0x6284
   __TEXT.__const: 0x1e338

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 95E1C085-13CC-38BF-B937-1F7299960EE3
+  UUID: 8F60B40D-956E-30F4-BFD2-EEB1A96AB8B8
   Functions: 2441
   Symbols:   4402
   CStrings:  578
Functions:
~ _AccelerateCrypto_SHA3_keccak : 780 -> 892
~ ccmlkem_ntt_forward_3 : 204 -> 268
~ ccmlkem_ntt_inverse_3 : 268 -> 356
~ _ccmlkem_poly_encode : 248 -> 312
~ _ccmlkem_poly_decode : 216 -> 292
~ _ccmlkem_poly_add : 60 -> 92
~ _ccmlkem_poly_sub : 60 -> 92
~ _ccmlkem_poly_reduce : 136 -> 168
~ _ccmlkem_poly_toplant : 136 -> 168
~ _ccmlkem_poly_compress_d1 : 128 -> 168
~ _ccmlkem_poly_compress_d4 : 192 -> 240
~ _ccmlkem_poly_compress_d5 : 140 -> 180
~ _ccmlkem_poly_compress_d10 : 140 -> 180
~ _ccmlkem_poly_compress_d11 : 148 -> 192
~ _ccmlkem_poly_decompress_d1 : 56 -> 72
~ _ccmlkem_poly_decompress_d4 : 68 -> 84
~ _ccmlkem_poly_decompress_d5 : 104 -> 132
~ _ccmlkem_poly_decompress_d10 : 104 -> 128
~ _ccmlkem_poly_decompress_d11 : 112 -> 140
~ _ccmlkem_ntt_basemul : 204 -> 244
~ _AccelerateCrypto_SHA3_keccak_2x_hwassist : 656 -> 804
~ _AccelerateCrypto_SHA3_keccak_hwassist : 452 -> 600
~ _ccrsa_decrypt_oaep_blinded_ws : 304 -> 312
~ _cczp_sub : 260 -> 276
~ _generate : 240 -> 228
~ _ccpolyzp_po2cyc_random_cbd_ws : 340 -> 336
~ _ccsigma_compute_mac_internal : 184 -> 200
~ _cckem_xwing_mlkem768x25519_export_privkey : 116 -> 112
~ _cckem_xwing_mlkem768x25519_import_privkey : 92 -> 100
~ _ccmode_ccm_finalize : 176 -> 172
~ _ccrns_mul_modulus_init_ws : 68 -> 64
~ _ccrns_mul_modulus_init_var_time_ws : 88 -> 84
~ _ep_mac_compute : 64 -> 60
~ _ccmldsa_export_pubkey : 72 -> 68
~ _ccmode_gcm_aad : 308 -> 304
~ _ccec_compact_generate_key_checksign_ws : 104 -> 100
~ _cche_ciphertext_coeff_plaintext_mul_ws : 228 -> 216
~ _cche_ciphertext_eval_dcrt_plaintext_mul_internal : 232 -> 220
~ _cche_ciphertext_eval_plaintext_mul_ws : 228 -> 216
~ _ccgcm_inc_iv_internal : 160 -> 148
~ _ccsae_generate_h2c_commit_finalize_ws : 116 -> 112
~ _ccpolyzp_po2cyc_coeff_apply_galois : 368 -> 356
~ _ccpolyzp_po2cyc_eval_apply_galois : 372 -> 360
~ _init : 236 -> 224
~ _reseed : 132 -> 120
~ _ccec_x963_import_priv_ws : 292 -> 280
~ _ccmode_ccm_cbcmac : 68 -> 64

```
