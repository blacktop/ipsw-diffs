## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1608.80.10.0.0
-  __TEXT.__text: 0x752cc
+1638.100.62.0.0
+  __TEXT.__text: 0x7e9a0
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x18b54
+  __TEXT.__const: 0x18f54
   __TEXT.__cstring: 0x53aa
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1714
+  __TEXT.__unwind_info: 0x18a4
   __TEXT.__eh_frame: 0x270
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0xf00
+  __DATA_CONST.__const: 0xf90
   __AUTH_CONST.__auth_ptr: 0x1c8
   __AUTH_CONST.__const: 0x1400
   __AUTH_CONST.__auth_got: 0x110

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 1854
-  Symbols:   3160
+  Functions: 2001
+  Symbols:   3398
   CStrings:  618
 
Symbols:
+ _CCHE_CIPHERTEXT_GALOIS_KEY_SWITCH_WORKSPACE_N
+ _CCHE_CIPHERTEXT_MOD_SWITCH_DOWN_WORKSPACE_N
+ _CCHE_CIPHERTEXT_PLAINTEXT_ADD_WORKSPACE_N
+ _CCHE_CIPHER_PLAIN_CTX_INIT_WORKSPACE_N
+ _CCHE_DECRYPT_CTX_INIT_WORKSPACE_N
+ _CCHE_DECRYPT_WORKSPACE_N
+ _CCHE_DESERIALIZE_SEEDED_CIPHERTEXT_EVAL_WORKSPACE_N
+ _CCHE_ENCRYPT_ZERO_SYMMETRIC_EVAL_WORKSPACE_N
+ _CCHE_ENCRYPT_ZERO_SYMMETRIC_HELPER_WORKSPACE_N
+ _CCHE_PARAM_CTX_INIT_WORKSPACE_N
+ _CCPOLYZP_PO2CYC_BASE_CONVERT_EXACT_POLY_WORKSPACE_N
+ _CCPOLYZP_PO2CYC_BASE_CONVERT_MOD_T_DIVIDE_AND_ROUND_Q_LAST_WORKSPACE_N
+ _CCPOLYZP_PO2CYC_CTX_WORKSPACE_N
+ _ccbfv_ciphertext_coeff_compose_skip_lsbs
+ _ccbfv_ciphertext_coeff_decompose_nptexts_skip_lsbs
+ _ccbfv_ciphertext_coeff_decompose_skip_lsbs
+ _ccbfv_predefined_encryption_params_n_4096_logq_27_28_28_logt_6
+ _ccec_add_normalized_ws
+ _ccec_full_sub
+ _ccec_map_to_homogeneous_ws
+ _cche_bytes_to_coeffs
+ _cche_cipher_plain_ctx_init_ws
+ _cche_ciphertext_apply_galois
+ _cche_ciphertext_apply_galois_ws
+ _cche_ciphertext_coeff_compose
+ _cche_ciphertext_coeff_dcrt_plaintext_mul
+ _cche_ciphertext_coeff_decompose
+ _cche_ciphertext_coeff_decompose_nptexts
+ _cche_ciphertext_coeff_decompose_nptexts_rns
+ _cche_ciphertext_coeff_plaintext_mul
+ _cche_ciphertext_coeff_plaintext_mul_ws
+ _cche_ciphertext_correction_factor
+ _cche_ciphertext_eval_dcrt_plaintext_mul
+ _cche_ciphertext_eval_plaintext_mul
+ _cche_ciphertext_eval_plaintext_mul_ws
+ _cche_ciphertext_fresh_correction_factor
+ _cche_ciphertext_fresh_npolys
+ _cche_ciphertext_fwd_ntt
+ _cche_ciphertext_galois_elt_rotate_rows_left
+ _cche_ciphertext_galois_elt_rotate_rows_right
+ _cche_ciphertext_galois_elt_swap_columns
+ _cche_ciphertext_galois_key_switch_ws
+ _cche_ciphertext_inv_ntt
+ _cche_ciphertext_mod_switch_down_ws
+ _cche_ciphertext_plaintext_add
+ _cche_ciphertext_plaintext_add_ws
+ _cche_ciphertext_sizeof
+ _cche_coeffs_to_bytes
+ _cche_dcrt_plaintext_encode
+ _cche_dcrt_plaintext_encode_ws
+ _cche_dcrt_plaintext_sizeof
+ _cche_decode_poly_uint64
+ _cche_decode_simd_int64
+ _cche_decode_simd_int64_ws
+ _cche_decode_simd_uint64
+ _cche_decode_simd_uint64_ws
+ _cche_decrypt
+ _cche_decrypt_ctx_init_ws
+ _cche_decrypt_ctx_nof_n
+ _cche_decrypt_ws
+ _cche_deserialize_ciphertext_coeff
+ _cche_deserialize_ciphertext_coeff_ws
+ _cche_deserialize_ciphertext_eval
+ _cche_deserialize_seeded_ciphertext_coeff
+ _cche_deserialize_seeded_ciphertext_coeff_ws
+ _cche_deserialize_seeded_ciphertext_eval
+ _cche_deserialize_seeded_ciphertext_eval_ws
+ _cche_encode_poly_uint64
+ _cche_encode_simd_int64
+ _cche_encode_simd_uint64
+ _cche_encoding_generator_column
+ _cche_encrypt_params_eq
+ _cche_encrypt_params_get
+ _cche_encrypt_symmetric
+ _cche_encrypt_symmetric_ws
+ _cche_encrypt_zero_symmetric_eval_ws
+ _cche_encrypt_zero_symmetric_helper_ws
+ _cche_encryption_params_coefficient_moduli
+ _cche_encryption_params_coefficient_nmoduli
+ _cche_encryption_params_plaintext_modulus
+ _cche_encryption_params_polynomial_degree
+ _cche_galois_elt_from_step
+ _cche_galois_key_ciphertext
+ _cche_galois_key_ciphertext_const
+ _cche_galois_key_generate
+ _cche_galois_key_generate_ws
+ _cche_galois_key_load
+ _cche_galois_key_load_ws
+ _cche_galois_key_nof_n
+ _cche_galois_key_save
+ _cche_galois_key_save_ws
+ _cche_galois_key_sizeof
+ _cche_mul_poly_sk
+ _cche_param_ctx_chain_const
+ _cche_param_ctx_cipher_plain_ctx_const
+ _cche_param_ctx_ciphertext_ctx_nmoduli
+ _cche_param_ctx_coefficient_moduli
+ _cche_param_ctx_eq
+ _cche_param_ctx_he_scheme
+ _cche_param_ctx_init
+ _cche_param_ctx_init_ws
+ _cche_param_ctx_key_ctx_nmoduli
+ _cche_param_ctx_key_ctx_poly_nbytes
+ _cche_param_ctx_nof_n
+ _cche_param_ctx_plaintext_ctx
+ _cche_param_ctx_plaintext_ctx_const
+ _cche_param_ctx_plaintext_modulus
+ _cche_param_ctx_plaintext_modulus_inverse
+ _cche_param_ctx_plaintext_modulus_inverse_ws
+ _cche_param_ctx_polynomial_degree
+ _cche_param_ctx_sizeof
+ _cche_param_ctx_supports_simd_encoding
+ _cche_plaintext_sizeof
+ _cche_predefined_encryption_params_insecure_n_16_logq_60_logt_15
+ _cche_predefined_encryption_params_insecure_n_512_logq_4x60_logt_20
+ _cche_predefined_encryption_params_insecure_n_8_logq_5x18_logt_5
+ _cche_predefined_encryption_params_n_4096_logq_16_33_33_logt_4
+ _cche_predefined_encryption_params_n_4096_logq_27_28_28_logt_13
+ _cche_predefined_encryption_params_n_4096_logq_27_28_28_logt_16
+ _cche_predefined_encryption_params_n_4096_logq_27_28_28_logt_17
+ _cche_predefined_encryption_params_n_4096_logq_27_28_28_logt_4
+ _cche_predefined_encryption_params_n_4096_logq_27_28_28_logt_5
+ _cche_predefined_encryption_params_n_4096_logq_27_28_28_logt_6
+ _cche_predefined_encryption_params_n_8192_logq_28_60_60_logt_20
+ _cche_predefined_encryption_params_n_8192_logq_29_60_60_logt_15
+ _cche_predefined_encryption_params_n_8192_logq_3x55_logt_24
+ _cche_predefined_encryption_params_n_8192_logq_3x55_logt_29
+ _cche_predefined_encryption_params_n_8192_logq_3x55_logt_30
+ _cche_predefined_encryption_params_n_8192_logq_3x55_logt_42
+ _cche_predefined_encryption_params_n_8192_logq_40_60_60_logt_26
+ _cche_relin_key_ciphertext
+ _cche_relin_key_ciphertext_const
+ _cche_relin_key_generate
+ _cche_relin_key_generate_ws
+ _cche_relin_key_load
+ _cche_relin_key_load_ws
+ _cche_relin_key_nof_n
+ _cche_relin_key_save
+ _cche_relin_key_save_ws
+ _cche_relin_key_sizeof
+ _cche_rng_seed_sizeof
+ _cche_secret_key_generate
+ _cche_secret_key_generate_from_seed
+ _cche_secret_key_generate_from_seed_ws
+ _cche_secret_key_generate_ws
+ _cche_secret_key_sizeof
+ _cche_serialize_ciphertext_coeff
+ _cche_serialize_ciphertext_coeff_max_nskip_lsbs
+ _cche_serialize_ciphertext_coeff_nbytes
+ _cche_serialize_ciphertext_coeff_ws
+ _cche_serialize_ciphertext_eval
+ _cche_serialize_ciphertext_eval_nbytes
+ _cche_serialize_seeded_ciphertext_coeff
+ _cche_serialize_seeded_ciphertext_coeff_nbytes
+ _cche_serialize_seeded_ciphertext_eval
+ _cche_serialize_seeded_ciphertext_eval_nbytes
+ _cckyber_hash_g
+ _cckyber_hash_h
+ _cckyber_indcpa_decrypt_ws
+ _cckyber_indcpa_encrypt
+ _cckyber_indcpa_encrypt_ws
+ _cckyber_indcpa_keypair
+ _cckyber_kem_decapsulate
+ _cckyber_kem_encapsulate
+ _cckyber_kem_encapsulate_msg
+ _cckyber_kem_keypair
+ _cckyber_kem_keypair_coins
+ _cckyber_prf
+ _cckyber_rkprf
+ _cckyber_sample_ntt
+ _ccpolyzp_po2cyc_base_convert_exact_poly_ws
+ _ccpolyzp_po2cyc_base_convert_mod_t_divide_and_round_q_last_ws
+ _ccpolyzp_po2cyc_base_convert_neg_q_inv_mod_t_ws
+ _ccpolyzp_po2cyc_init
+ _ccrsa_xor_varlen
+ _cczp_mm_init_copy
+ _sizeof_struct_cche_cipher_plain_ctx
+ _sizeof_struct_cche_ciphertext
+ _sizeof_struct_cche_decrypt_ctx
+ _sizeof_struct_cche_encrypt_params
+ _sizeof_struct_cche_galois_key
+ _sizeof_struct_cche_relin_key
- _PQCLEAN_KYBER_CLEAN_crypto_kem_dec
- _PQCLEAN_KYBER_CLEAN_crypto_kem_enc
- _PQCLEAN_KYBER_CLEAN_crypto_kem_enc_msg
- _PQCLEAN_KYBER_CLEAN_crypto_kem_keypair
- _PQCLEAN_KYBER_CLEAN_crypto_kem_keypair_coins
- _PQCLEAN_KYBER_CLEAN_gen_matrix
- _PQCLEAN_KYBER_CLEAN_indcpa_dec_ws
- _PQCLEAN_KYBER_CLEAN_indcpa_enc
- _PQCLEAN_KYBER_CLEAN_indcpa_enc_ws
- _PQCLEAN_KYBER_CLEAN_indcpa_keypair
- _PQCLEAN_KYBER_CLEAN_kyber_shake256_prf
- _PQCLEAN_KYBER_CLEAN_kyber_shake256_rkprf
- _cc_xor_safe
- _ccec_add_ws
- _cckyber_sample_uniform
- _ccpolyzp_po2cyc_base_convert_q_inv_mod_t_ws

```
