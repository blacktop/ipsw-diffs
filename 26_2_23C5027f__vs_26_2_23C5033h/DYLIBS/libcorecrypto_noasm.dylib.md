## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1922.60.4.0.0
-  __TEXT.__text: 0x7b6e4
+1922.60.11.0.0
+  __TEXT.__text: 0x7b7e8
   __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0x1df88
   __TEXT.__cstring: 0x5f4d

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 24CE12F6-DA3D-3DB2-B816-7B17D9576C3A
+  UUID: 8567883C-E021-3099-A5E2-5A1BF07ED0DB
   Functions: 2313
   Symbols:   4120
   CStrings:  545
Functions:
~ _AccelerateCrypto_SHA3_keccak : 780 -> 892
~ _AccelerateCrypto_SHA3_keccak_2x_hwassist : 656 -> 804
~ _AccelerateCrypto_SHA3_keccak_hwassist : 452 -> 600
~ _ccrsa_decrypt_oaep_blinded_ws : 312 -> 304
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
~ _ccmode_gcm_aad : 336 -> 332
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
