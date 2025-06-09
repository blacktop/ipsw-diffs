## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1736.120.5.0.0
-  __TEXT.__text: 0x7d094
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__cstring: 0x5848
-  __TEXT.__const: 0x19028
+1922.0.1.0.0
+  __TEXT.__text: 0x84674
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__cstring: 0x585e
+  __TEXT.__const: 0x19978
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1938
+  __TEXT.__unwind_info: 0x19b8
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0xf30
-  __AUTH_CONST.__auth_got: 0x110
-  __AUTH_CONST.__const: 0x1aa0
+  __DATA_CONST.__const: 0xf50
+  __AUTH_CONST.__auth_got: 0x118
+  __AUTH_CONST.__const: 0x1ea8
   __AUTH.__data: 0xb8
-  __DATA.__data: 0x6738
+  __DATA.__data: 0x6858
   __DATA.__bss: 0xeb8
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 57D653E3-0853-3406-816B-3D6BD1DBEDFA
-  Functions: 2228
-  Symbols:   3975
-  CStrings:  499
+  UUID: 960B1CC2-2412-333D-92C9-1DD90DECB266
+  Functions: 2416
+  Symbols:   4326
+  CStrings:  502
 
Symbols:
+ _Constants
+ _InvShiftRows_RotWord
+ _S_Box_Inverse_Zero
+ _XWING_LABEL
+ ___memmove_chk
+ _ccccm_nonce_size
+ _ccdigest_parallel
+ _ccdigest_parallel_internal
+ _ccdigest_parallel_update_internal
+ _ccdrbg_generate_internal
+ _ccgcm_set_iv_legacy_internal
+ _cchpke_aead_aesgcm256
+ _cchpke_aead_aesgcm_open
+ _cchpke_aead_aesgcm_seal
+ _cchpke_kem_dhkem_x25519_hkdf_sha256
+ _cchpke_kem_xwing
+ _cchpke_kem_xwing_mlkem768x25519_decap
+ _cchpke_kem_xwing_mlkem768x25519_encap
+ _cchpke_kem_xwing_mlkem768x25519_generate_key_pair
+ _cchpke_params_x25519_AESGCM256_HKDF_SHA256
+ _cchpke_params_x25519_AESGCM256_HKDF_SHA256.params
+ _cchpke_params_xwing_AESGCM128_HKDF_SHA256
+ _cchpke_params_xwing_AESGCM128_HKDF_SHA256.params
+ _cckeccak_absorb_iovec
+ _cckeccak_get_permutation
+ _cckeccak_init_state
+ _cckeccak_oneshot
+ _cckeccak_oneshot_iovec
+ _cckem_decapsulate_internal
+ _cckem_derive_key_from_seed_internal
+ _cckem_encapsulate_internal
+ _cckem_export_privkey_internal
+ _cckem_generate_key_with_seed
+ _cckem_import_privkey_internal
+ _cckem_kyber1024_generate_key_with_seed
+ _cckem_kyber768_generate_key_with_seed
+ _cckem_mlkem1024
+ _cckem_mlkem1024_decapsulate
+ _cckem_mlkem1024_derive_key_from_seed
+ _cckem_mlkem1024_encapsulate
+ _cckem_mlkem1024_export_privkey
+ _cckem_mlkem1024_export_pubkey
+ _cckem_mlkem1024_generate_key
+ _cckem_mlkem1024_generate_key_with_seed
+ _cckem_mlkem1024_import_privkey
+ _cckem_mlkem1024_import_pubkey
+ _cckem_mlkem1024_info
+ _cckem_mlkem768
+ _cckem_mlkem768_decapsulate
+ _cckem_mlkem768_derive_key_from_seed
+ _cckem_mlkem768_encapsulate
+ _cckem_mlkem768_export_privkey
+ _cckem_mlkem768_export_pubkey
+ _cckem_mlkem768_generate_key
+ _cckem_mlkem768_generate_key_with_seed
+ _cckem_mlkem768_import_privkey
+ _cckem_mlkem768_import_pubkey
+ _cckem_mlkem768_info
+ _cckem_seed_nbytes_ctx
+ _cckem_seed_nbytes_info
+ _cckem_xwing_mlkem768x25519
+ _cckem_xwing_mlkem768x25519_combine
+ _cckem_xwing_mlkem768x25519_decapsulate
+ _cckem_xwing_mlkem768x25519_derive_key_from_seed
+ _cckem_xwing_mlkem768x25519_encapsulate
+ _cckem_xwing_mlkem768x25519_export_privkey
+ _cckem_xwing_mlkem768x25519_export_pubkey
+ _cckem_xwing_mlkem768x25519_generate_key
+ _cckem_xwing_mlkem768x25519_generate_key_with_seed
+ _cckem_xwing_mlkem768x25519_import_privkey
+ _cckem_xwing_mlkem768x25519_import_pubkey
+ _cckem_xwing_mlkem768x25519_info
+ _ccmldsa65
+ _ccmldsa65_params
+ _ccmldsa87
+ _ccmldsa87_params
+ _ccmldsa_compute_c
+ _ccmldsa_compute_mu
+ _ccmldsa_derive_key_from_seed
+ _ccmldsa_export_privkey
+ _ccmldsa_export_pubkey
+ _ccmldsa_full_ctx_init
+ _ccmldsa_generate_key
+ _ccmldsa_generate_key_with_seed
+ _ccmldsa_hash_nbytes_ctx
+ _ccmldsa_hash_nbytes_params
+ _ccmldsa_import_privkey
+ _ccmldsa_import_pubkey
+ _ccmldsa_keygen_internal
+ _ccmldsa_ntt_forward
+ _ccmldsa_ntt_forward_eta
+ _ccmldsa_ntt_inverse
+ _ccmldsa_ntt_pointwise
+ _ccmldsa_poly_add
+ _ccmldsa_poly_bitpack_eta2
+ _ccmldsa_poly_bitpack_eta4
+ _ccmldsa_poly_bitpack_t0
+ _ccmldsa_poly_bitpack_t1
+ _ccmldsa_poly_bitpack_z
+ _ccmldsa_poly_bitunpack_eta2
+ _ccmldsa_poly_bitunpack_eta4
+ _ccmldsa_poly_bitunpack_t0
+ _ccmldsa_poly_bitunpack_t1
+ _ccmldsa_poly_bitunpack_z
+ _ccmldsa_poly_caddq
+ _ccmldsa_poly_checknorm
+ _ccmldsa_poly_decompose
+ _ccmldsa_poly_make_hint
+ _ccmldsa_poly_power2round
+ _ccmldsa_poly_reduce
+ _ccmldsa_poly_shiftl
+ _ccmldsa_poly_simplebitpack_w1
+ _ccmldsa_poly_sub
+ _ccmldsa_poly_use_hint
+ _ccmldsa_polyvec_matrix_expand_ntt_pointwise
+ _ccmldsa_polyveck_add
+ _ccmldsa_polyveck_bitpack_eta
+ _ccmldsa_polyveck_bitpack_t0
+ _ccmldsa_polyveck_bitpack_t1
+ _ccmldsa_polyveck_bitunpack_eta
+ _ccmldsa_polyveck_bitunpack_t0
+ _ccmldsa_polyveck_bitunpack_t1
+ _ccmldsa_polyveck_caddq
+ _ccmldsa_polyveck_checknorm
+ _ccmldsa_polyveck_decompose
+ _ccmldsa_polyveck_make_hint
+ _ccmldsa_polyveck_ntt_forward
+ _ccmldsa_polyveck_ntt_forward_eta
+ _ccmldsa_polyveck_ntt_inverse
+ _ccmldsa_polyveck_ntt_pointwise_poly
+ _ccmldsa_polyveck_power2round
+ _ccmldsa_polyveck_reduce
+ _ccmldsa_polyveck_shiftl
+ _ccmldsa_polyveck_sub
+ _ccmldsa_polyveck_use_hint
+ _ccmldsa_polyvecl_add
+ _ccmldsa_polyvecl_bitpack_eta
+ _ccmldsa_polyvecl_bitpack_z
+ _ccmldsa_polyvecl_bitunpack_eta
+ _ccmldsa_polyvecl_bitunpack_z
+ _ccmldsa_polyvecl_checknorm
+ _ccmldsa_polyvecl_ntt_forward
+ _ccmldsa_polyvecl_ntt_forward_eta
+ _ccmldsa_polyvecl_ntt_inverse
+ _ccmldsa_polyvecl_ntt_pointwise_poly
+ _ccmldsa_polyvecl_reduce
+ _ccmldsa_prehash
+ _ccmldsa_prehash_with_context
+ _ccmldsa_privkey_nbytes_ctx
+ _ccmldsa_privkey_nbytes_params
+ _ccmldsa_pub_ctx_init
+ _ccmldsa_pubkey_nbytes_ctx
+ _ccmldsa_pubkey_nbytes_params
+ _ccmldsa_public_ctx
+ _ccmldsa_sample_in_ball
+ _ccmldsa_sample_rej_bounded_poly
+ _ccmldsa_sample_rej_coeffs_eta2
+ _ccmldsa_sample_rej_coeffs_eta4
+ _ccmldsa_sample_rej_ntt_poly
+ _ccmldsa_seed_nbytes_ctx
+ _ccmldsa_seed_nbytes_params
+ _ccmldsa_sign
+ _ccmldsa_sign_internal
+ _ccmldsa_sign_prehashed
+ _ccmldsa_sign_prehashed_internal
+ _ccmldsa_sign_with_context
+ _ccmldsa_signature_nbytes_ctx
+ _ccmldsa_signature_nbytes_params
+ _ccmldsa_sizeof_full_ctx
+ _ccmldsa_sizeof_pub_ctx
+ _ccmldsa_verify
+ _ccmldsa_verify_internal
+ _ccmldsa_verify_prehashed
+ _ccmldsa_verify_prehashed_internal
+ _ccmldsa_verify_with_context
+ _ccmldsa_zetas
+ _ccmlkem1024_params
+ _ccmlkem768_params
+ _ccmlkem_hash_g
+ _ccmlkem_hash_g_append_k
+ _ccmlkem_hash_h
+ _ccmlkem_indcpa_decrypt_ws
+ _ccmlkem_indcpa_encrypt
+ _ccmlkem_indcpa_encrypt_ws
+ _ccmlkem_indcpa_keypair
+ _ccmlkem_kem_decapsulate
+ _ccmlkem_kem_encapsulate
+ _ccmlkem_kem_encapsulate_msg
+ _ccmlkem_kem_keypair
+ _ccmlkem_kem_keypair_from_seed
+ _ccmlkem_kem_keypair_with_seed
+ _ccmlkem_ntt_basemul
+ _ccmlkem_ntt_forward
+ _ccmlkem_ntt_forward_cbd_eta2
+ _ccmlkem_ntt_inverse
+ _ccmlkem_poly_add
+ _ccmlkem_poly_compress
+ _ccmlkem_poly_compress_d1
+ _ccmlkem_poly_compress_d10
+ _ccmlkem_poly_compress_d11
+ _ccmlkem_poly_compress_d4
+ _ccmlkem_poly_compress_d5
+ _ccmlkem_poly_decode
+ _ccmlkem_poly_decompress
+ _ccmlkem_poly_decompress_d1
+ _ccmlkem_poly_decompress_d10
+ _ccmlkem_poly_decompress_d11
+ _ccmlkem_poly_decompress_d4
+ _ccmlkem_poly_decompress_d5
+ _ccmlkem_poly_encode
+ _ccmlkem_poly_getnoise
+ _ccmlkem_poly_reduce
+ _ccmlkem_poly_sub
+ _ccmlkem_poly_toplant
+ _ccmlkem_polyvec_add
+ _ccmlkem_polyvec_basemul
+ _ccmlkem_polyvec_compress
+ _ccmlkem_polyvec_decode
+ _ccmlkem_polyvec_decompress
+ _ccmlkem_polyvec_encode
+ _ccmlkem_polyvec_getnoise
+ _ccmlkem_polyvec_ntt_forward
+ _ccmlkem_polyvec_ntt_forward_cbd_eta2
+ _ccmlkem_polyvec_reduce
+ _ccmlkem_prf
+ _ccmlkem_rkprf
+ _ccmlkem_sample_cbd_eta2
+ _ccmlkem_sample_matrix
+ _ccmlkem_zetas
+ _ccpost_chacha20_poly1305
+ _ccpost_curve25519
+ _ccsae_verify_commitment_with_rejected_groups
+ _ccsae_verify_commitment_ws
+ _ccsigma_exclave_pairing_info
+ _ccspake_get_session_key
+ _ccspake_session_key_compute_internal
+ _ccxwing_mlkem768x25519_encapsulate_derand_internal
+ _ep_aead_next_iv
+ _ep_aead_open
+ _ep_aead_seal
+ _ep_clear
+ _ep_kex_ctx
+ _ep_mac_compute
+ _ep_peer_kex_ctx
+ _ep_peer_sign_ctx
+ _ep_session_keys_buffer
+ _ep_session_keys_derive
+ _ep_session_keys_sizes
+ _ep_sigma_compute_mac_and_digest
+ _ep_sign_ctx
+ _exclave_pairing_info
+ _exclave_pairing_kdf_dst
+ _exclave_pairing_kdf_salt
+ _exclave_pairing_sign_dst
+ ccaes_arm_encrypt_key128
+ ccaes_arm_encrypt_key192
+ ccaes_arm_encrypt_key256
+ ccmlkem_ntt_forward_2
+ ccmlkem_ntt_forward_3
+ ccmlkem_ntt_inverse_2
+ ccmlkem_ntt_inverse_3
+ dlCPI0_0
+ dlCPI0_1
+ dlCPI0_2
+ dlCPI0_3
+ dlCPI0_4
- _OUTLINED_FUNCTION_7
- _ccaes_arm_decrypt_key128
- _ccaes_arm_decrypt_key192
- _ccaes_arm_decrypt_key256
- _ccaes_arm_encrypt_key128
- _ccaes_arm_encrypt_key192
- _ccaes_arm_encrypt_key256
- _cchpke_aead_aesgcm128_open
- _cchpke_aead_aesgcm128_seal
- _cchpke_kem_x25519
- _cchpke_kem_x25519_deserialize
- _cchpke_kem_x25519_public_key
- _cchpke_kem_x25519_serialize
- _cckyber_hash_g
- _cckyber_hash_h
- _cckyber_indcpa_decrypt_ws
- _cckyber_indcpa_encrypt
- _cckyber_indcpa_encrypt_ws
- _cckyber_indcpa_keypair
- _cckyber_kem_decapsulate
- _cckyber_kem_encapsulate
- _cckyber_kem_encapsulate_msg
- _cckyber_kem_keypair
- _cckyber_kem_keypair_coins
- _cckyber_ntt_basemul
- _cckyber_ntt_forward
- _cckyber_ntt_inverse
- _cckyber_poly_add
- _cckyber_poly_compress
- _cckyber_poly_compress_d1
- _cckyber_poly_compress_d10
- _cckyber_poly_compress_d11
- _cckyber_poly_compress_d4
- _cckyber_poly_compress_d5
- _cckyber_poly_decode
- _cckyber_poly_decompress
- _cckyber_poly_decompress_d1
- _cckyber_poly_decompress_d10
- _cckyber_poly_decompress_d11
- _cckyber_poly_decompress_d4
- _cckyber_poly_decompress_d5
- _cckyber_poly_encode
- _cckyber_poly_from_msg
- _cckyber_poly_getnoise
- _cckyber_poly_reduce
- _cckyber_poly_sub
- _cckyber_poly_to_msg
- _cckyber_poly_toplant
- _cckyber_polyvec_add
- _cckyber_polyvec_basemul
- _cckyber_polyvec_compress
- _cckyber_polyvec_decode
- _cckyber_polyvec_decompress
- _cckyber_polyvec_encode
- _cckyber_polyvec_ntt_forward
- _cckyber_polyvec_reduce
- _cckyber_prf
- _cckyber_rkprf
- _cckyber_sample_cbd_eta2
- _cckyber_sample_ntt
- _cckyber_zetas
- _ccrsa_verify_pkcs1v15_digest_ws
- aes_dkey_expansion
- aes_key_expansion
CStrings:
+ "%zu bit rsa key\n"
+ "SHA3_C"
+ "SHA3_VNG_ARM"
+ "SHA3_VNG_ARM_HW"
+ "SHA3_VNG_INTEL"
- "%lu bit rsa key\n"
- "cchpke_kem_x25519_public_key"

```
