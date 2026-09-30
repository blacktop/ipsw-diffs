## libcorecrypto.dylib

> `/System/ExclaveKit/usr/lib/system/libcorecrypto.dylib`

```diff

-1736.60.52.0.0
-  __TEXT.__text: 0x5c424
+1736.60.66.0.0
+  __TEXT.__text: 0x5f9c4
   __TEXT.__auth_stubs: 0x130
   __TEXT.__cstring: 0x77f
   __TEXT.__const: 0x12f90
-  __TEXT.__unwind_info: 0x1188
+  __TEXT.__unwind_info: 0x12c8
   __TEXT.__eh_frame: 0x138
   __DATA.__auth_got: 0x98
   __DATA.__got: 0x10

   __DATA.__common: 0x8
   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib
-  Functions: 1599
-  Symbols:   1867
+  Functions: 1700
+  Symbols:   1972
   CStrings:  96
 
Symbols:
+ _cc_cmp_safe_internal
+ _cc_disable_dit_with_sb
+ _ccapsic_client_check_intersect_response_ws
+ _ccapsic_client_init_internal
+ _ccapsic_server_encode_element_ws
+ _cccbc_init_internal
+ _cccbc_one_shot_explicit_internal
+ _cccbc_set_iv_internal
+ _cccbc_update_internal
+ _ccccm_finalize_and_verify_tag_internal
+ _ccccm_one_shot_internal
+ _ccchacha20_update_internal
+ _ccchacha20poly1305_decrypt_internal
+ _ccchacha20poly1305_encrypt_internal
+ _ccchacha20poly1305_finalize_internal
+ _ccchacha20poly1305_init_internal
+ _ccchacha20poly1305_setnonce_internal
+ _ccchacha20poly1305_verify_internal
+ _cccmac_final_generate_internal
+ _cccmac_final_verify_internal
+ _cccmac_init_internal
+ _cccmac_one_shot_generate_internal
+ _cccmac_update_internal
+ _ccctr_init_internal
+ _ccctr_one_shot_internal
+ _ccctr_update_internal
+ _cccurve25519_assumes_dit_internal
+ _cccurve25519_make_key_pair_internal
+ _cccurve25519_make_pub_internal
+ _ccder_blob_decode_eckey_internal
+ _ccder_blob_encode_eckey_internal
+ _ccder_decode_eckey_internal
+ _ccder_decode_rsa_priv_internal
+ _ccder_encode_eckey_internal
+ _ccder_encode_rsa_priv_internal
+ _ccdigest_init_internal
+ _ccdigest_internal
+ _ccdigest_update_internal
+ _ccdrbg_df_bc_init_internal
+ _ccdrbg_init_internal
+ _ccec_export_affine_point_public_value
+ _ccecb_init_internal
+ _ccecb_one_shot_explicit_internal
+ _ccecb_update_internal
+ _ccecies_decrypt_gcm_composite_ws
+ _ccecies_encrypt_gcm_composite_ws
+ _cced25519_sign_with_rng_internal
+ _cced448_make_pub_internal
+ _ccentropy_add_entropy_internal
+ _ccentropy_get_seed_internal
+ _ccgcm_aad_internal
+ _ccgcm_finalize_internal
+ _ccgcm_inc_iv_internal
+ _ccgcm_init_internal
+ _ccgcm_one_shot_internal
+ _ccgcm_set_iv_internal
+ _ccgcm_update_internal
+ _cchkdf_expand_internal
+ _cchkdf_extract_internal
+ _cchkdf_internal
+ _cchmac_final_internal
+ _cchmac_init_internal
+ _cchmac_internal
+ _cchmac_update_internal
+ _cchpke_initiator_encrypt_internal
+ _cchpke_responder_decrypt_internal
+ _cchpke_responder_setup_internal
+ _ccmgf_internal
+ _ccn_bitlen_internal
+ _ccn_bitlen_public_value
+ _ccn_cmp_internal
+ _ccn_cmp_public_value
+ _ccn_cmpn_internal
+ _ccn_cmpn_public_value
+ _ccn_read_uint_internal
+ _ccn_read_uint_public_value
+ _ccn_write_int_public_value
+ _ccn_write_int_size_public_value
+ _ccn_write_uint_internal
+ _ccn_write_uint_padded_ct_internal
+ _ccn_write_uint_padded_internal
+ _ccn_write_uint_public_value
+ _ccn_write_uint_size_internal
+ _ccn_write_uint_size_public_value
+ _ccnistkdf_ctr_cmac_fixed_internal
+ _ccnistkdf_ctr_cmac_internal
+ _ccpad_pkcs7_decode_internal
+ _ccpbkdf2_hmac_internal
+ _ccpoly1305_final_internal
+ _ccpoly1305_init_internal
+ _ccpoly1305_update_internal
+ _ccrng_uniform_internal
+ _ccrsa_eme_pkcs1v15_encode_internal
+ _ccrsa_emsa_pkcs1v15_encode_internal
+ _ccrsa_emsa_pss_encode_internal
+ _ccrsa_oaep_encode_parameter_internal
+ _ccsae_generate_commitment_finalize_ws
+ _ccsae_lexographic_order_key_internal
+ _ccsigma_compute_mac_internal
+ _ccspake_prover_init_internal
+ _ccsrp_generate_verifier_internal
+ _ccsrp_server_compute_session_internal
+ _ccsrp_server_generate_public_key_internal
+ _ccwrap_auth_decrypt_withiv_internal
+ _ccwrap_auth_encrypt_withiv_internal
+ _timingsafe_enable_if_supported
+ _timingsafe_restore_if_supported
- _ccec_make_pub_from_priv
- _ccec_twin_mult

```
