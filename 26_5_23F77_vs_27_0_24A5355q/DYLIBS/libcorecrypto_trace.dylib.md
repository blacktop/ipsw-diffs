## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1922.122.1.0.0
-  __TEXT.__text: 0x88008
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__cstring: 0x61ae
-  __TEXT.__const: 0x1e4e8
+2097.0.0.0.0
+  __TEXT.__text: 0x8bb48
+  __TEXT.__cstring: 0x62bd
+  __TEXT.__const: 0x20498
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1b28
-  __TEXT.__eh_frame: 0x350
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x21a8
+  __TEXT.__unwind_info: 0x1d38
+  __TEXT.__eh_frame: 0x3a0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x21b0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x22c8
   __AUTH_CONST.__auth_got: 0x118
-  __AUTH_CONST.__const: 0x1ea8
   __AUTH.__data: 0x130
   __DATA.__data: 0x6868
-  __DATA.__bss: 0x20a0
+  __DATA.__bss: 0x20d0
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 0D83A982-6BF6-33BB-85A7-1E8DD00B8D5A
-  Functions: 2478
-  Symbols:   4488
-  CStrings:  578
+  UUID: 1C28C7D6-0ADC-38D1-B6DB-98C07FC43A04
+  Functions: 2603
+  Symbols:   4722
+  CStrings:  585
 
Symbols:
+ _CCHYBRIDSIG_FAULT_CANARY
+ _LAMPS13_MLDSA87_RSA3072_LABEL
+ _LAMPS7_15_DOMAIN
+ _ccaes_arm_decrypt_key_with_key_length_check_aligned
+ _ccaes_arm_ecb_aligned_decrypt_mode
+ _ccaes_arm_ecb_aligned_encrypt_mode
+ _ccaes_arm_encrypt_key_with_key_length_check_aligned
+ _ccaes_arm_xts_aligned_decrypt_mode
+ _ccaes_arm_xts_aligned_encrypt_mode
+ _ccckg2_contributor_finish_with_domain
+ _ccckg2_owner_finish_with_domain
+ _ccdigest_managed_dit
+ _ccdigest_managed_dit_final
+ _ccdigest_managed_dit_init
+ _ccdigest_managed_dit_update
+ _ccdit_managed_context_begin
+ _ccdit_managed_context_end
+ _ccdit_managed_context_is_enabled
+ _ccec_compute_pubkey
+ _ccec_make_pub_from_priv
+ _cche_predefined_encryption_params_n_4096_logq_27_28_28_logt_7
+ _cchybridsig_export_privkey
+ _cchybridsig_export_pubkey
+ _cchybridsig_full_ctx_prehash
+ _cchybridsig_full_ctx_sig_nbytes
+ _cchybridsig_generate_key
+ _cchybridsig_import_privkey
+ _cchybridsig_import_pubkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_export_privkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_export_pubkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_full_ctx_init
+ _cchybridsig_lamps13_mldsa87_rsa3072_generate_key
+ _cchybridsig_lamps13_mldsa87_rsa3072_import_privkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_import_pubkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_mprime
+ _cchybridsig_lamps13_mldsa87_rsa3072_privkey_nbytes
+ _cchybridsig_lamps13_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_lamps13_mldsa87_rsa3072_pubkey_nbytes
+ _cchybridsig_lamps13_mldsa87_rsa3072_public_ctx
+ _cchybridsig_lamps13_mldsa87_rsa3072_sign
+ _cchybridsig_lamps13_mldsa87_rsa3072_sign_prehashed_with_context
+ _cchybridsig_lamps13_mldsa87_rsa3072_sign_with_context
+ _cchybridsig_lamps13_mldsa87_rsa3072_verify
+ _cchybridsig_lamps13_mldsa87_rsa3072_verify_prehashed_with_context
+ _cchybridsig_lamps13_mldsa87_rsa3072_verify_prehashed_with_context_and_canary
+ _cchybridsig_lamps13_mldsa87_rsa3072_verify_with_canary
+ _cchybridsig_lamps13_mldsa87_rsa3072_verify_with_context
+ _cchybridsig_lamps13_mldsa87_rsa3072_verify_with_context_and_canary
+ _cchybridsig_mldsa87_rsa3072_export_privkey
+ _cchybridsig_mldsa87_rsa3072_export_pubkey
+ _cchybridsig_mldsa87_rsa3072_full_ctx_init
+ _cchybridsig_mldsa87_rsa3072_generate_key
+ _cchybridsig_mldsa87_rsa3072_import_privkey
+ _cchybridsig_mldsa87_rsa3072_import_pubkey
+ _cchybridsig_mldsa87_rsa3072_mprime
+ _cchybridsig_mldsa87_rsa3072_privkey_nbytes
+ _cchybridsig_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_mldsa87_rsa3072_pubkey_nbytes
+ _cchybridsig_mldsa87_rsa3072_public_ctx
+ _cchybridsig_mldsa87_rsa3072_sign
+ _cchybridsig_mldsa87_rsa3072_sign_prehashed_with_context
+ _cchybridsig_mldsa87_rsa3072_sign_with_context
+ _cchybridsig_mldsa87_rsa3072_verify
+ _cchybridsig_mldsa87_rsa3072_verify_prehashed_with_context
+ _cchybridsig_mldsa87_rsa3072_verify_prehashed_with_context_and_canary
+ _cchybridsig_mldsa87_rsa3072_verify_with_canary
+ _cchybridsig_mldsa87_rsa3072_verify_with_context
+ _cchybridsig_mldsa87_rsa3072_verify_with_context_and_canary
+ _cchybridsig_privkey_nbytes
+ _cchybridsig_pub_ctx_prehash
+ _cchybridsig_pub_ctx_sig_nbytes
+ _cchybridsig_pubkey_nbytes
+ _cchybridsig_public_ctx
+ _cchybridsig_sha512_prehash
+ _cchybridsig_sign
+ _cchybridsig_sign_prehashed_with_context
+ _cchybridsig_sign_with_context
+ _cchybridsig_verify
+ _cchybridsig_verify_prehashed_with_context
+ _cchybridsig_verify_prehashed_with_context_and_canary
+ _cchybridsig_verify_with_canary
+ _cchybridsig_verify_with_context
+ _cchybridsig_verify_with_context_and_canary
+ _cckeccak_f1600_c
+ _cckmac256_info
+ _cckmac256_vng_absorb
+ _cckmac256_vng_absorb_last
+ _cckmac256_vng_hwassist_absorb
+ _cckmac256_vng_hwassist_absorb_last
+ _cckmac256_vng_hwassist_info
+ _cckmac256_vng_hwassist_squeeze
+ _cckmac256_vng_info
+ _cckmac256_vng_squeeze
+ _cckmac_finalize
+ _cckmac_init
+ _cckmac_update
+ _ccsha256_vng_arm_aligned_di
+ _ccsha256_vng_arm_compress_aligned
+ _ccsha3_224_c_compress
+ _ccsha3_224_c_di
+ _ccsha3_224_c_final
+ _ccsha3_256_c_compress
+ _ccsha3_256_c_di
+ _ccsha3_256_c_final
+ _ccsha3_384_c_compress
+ _ccsha3_384_c_di
+ _ccsha3_384_c_final
+ _ccsha3_512_c_compress
+ _ccsha3_512_c_di
+ _ccsha3_512_c_final
+ _ccxts_managed_dit_init
+ _ccxts_managed_dit_set_tweak
+ _ccxts_managed_dit_update
+ _generate_key_mldsa
+ _keccak_round_constants
+ _lamps13_mldsa87_rsa3072_priv_info
+ _lamps13_mldsa87_rsa3072_pub_info
+ _left_encode_and_update_ctx_buffer_nbytes
+ _mldsa87_rsa3072_priv_info
+ _mldsa87_rsa3072_pub_info
+ _sign_mldsa_with_context
+ _sign_rsa_with_context
+ _verify_mldsa_with_context
+ _verify_rsa_with_context
CStrings:
+ "AES_ECB_ARM_ALIGNED"
+ "AES_XTS_ARM_ALIGNED"
+ "SHA256_VNG_ARM_ALIGNED"
+ "ccdit_managed_context_begin MUST have been called"
+ "ccrng failed assert cbc_info->block_size = %lu\n"
+ "ccrng failed assert key_nbytes = %lu\n"
+ "ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n"

```
