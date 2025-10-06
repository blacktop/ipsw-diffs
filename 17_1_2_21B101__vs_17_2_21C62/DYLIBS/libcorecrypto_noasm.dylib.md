## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1608.40.12.0.0
-  __TEXT.__text: 0x73d20
+1608.60.11.0.0
+  __TEXT.__text: 0x74e1c
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x189d4
-  __TEXT.__cstring: 0x51d6
+  __TEXT.__const: 0x18b74
+  __TEXT.__cstring: 0x5397
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x16e0
+  __TEXT.__unwind_info: 0x1700
   __TEXT.__eh_frame: 0x270
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf00
-  __AUTH_CONST.__const: 0x12e8
+  __AUTH_CONST.__const: 0x13a0
   __AUTH_CONST.__auth_got: 0x110
-  __AUTH.__data: 0xc0
+  __AUTH.__data: 0xa0
   __DATA.__data: 0x6b68
   __DATA.__bss: 0x19d0
   __DATA.__common: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 4021EBE1-C34B-343D-AC3D-176DF8629DDD
-  Functions: 1827
-  Symbols:   3106
-  CStrings:  610
+  UUID: D1565DC6-F2AB-3C81-9AED-A116EA122A60
+  Functions: 1847
+  Symbols:   3147
+  CStrings:  618
 
Symbols:
+ _PQCLEAN_KYBER_CLEAN_crypto_kem_dec
+ _PQCLEAN_KYBER_CLEAN_crypto_kem_enc
+ _PQCLEAN_KYBER_CLEAN_crypto_kem_keypair
+ _PQCLEAN_KYBER_CLEAN_gen_matrix
+ _PQCLEAN_KYBER_CLEAN_indcpa_dec_ws
+ _PQCLEAN_KYBER_CLEAN_indcpa_enc
+ _PQCLEAN_KYBER_CLEAN_indcpa_enc_ws
+ _PQCLEAN_KYBER_CLEAN_indcpa_keypair
+ _PQCLEAN_KYBER_CLEAN_kyber_shake256_prf
+ _PQCLEAN_KYBER_CLEAN_kyber_shake256_rkprf
+ _ccentropy_digest_reset
+ _ccentropy_list_get_seed
+ _ccentropy_list_init
+ _ccentropy_lock_add_entropy
+ _ccentropy_lock_get_seed
+ _ccentropy_lock_init
+ _ccentropy_lock_reset
+ _ccentropy_reset
+ _cckem_kyber1024
+ _cckem_kyber1024_decapsulate
+ _cckem_kyber1024_encapsulate
+ _cckem_kyber1024_export_privkey
+ _cckem_kyber1024_export_pubkey
+ _cckem_kyber1024_generate_key
+ _cckem_kyber1024_import_privkey
+ _cckem_kyber1024_import_pubkey
+ _cckem_kyber1024_info
+ _cckem_kyber768_export_privkey
+ _cckem_kyber768_export_pubkey
+ _cckem_kyber768_import_privkey
+ _cckem_kyber768_import_pubkey
+ _cckyber1024_params
+ _cckyber768_params
+ _cckyber_ntt_basemul
+ _cckyber_ntt_forward
+ _cckyber_ntt_inverse
+ _cckyber_poly_add
+ _cckyber_poly_compress
+ _cckyber_poly_compress_d1
+ _cckyber_poly_compress_d10
+ _cckyber_poly_compress_d11
+ _cckyber_poly_compress_d4
+ _cckyber_poly_compress_d5
+ _cckyber_poly_decode
+ _cckyber_poly_decompress
+ _cckyber_poly_decompress_d1
+ _cckyber_poly_decompress_d10
+ _cckyber_poly_decompress_d11
+ _cckyber_poly_decompress_d4
+ _cckyber_poly_decompress_d5
+ _cckyber_poly_encode
+ _cckyber_poly_from_msg
+ _cckyber_poly_getnoise
+ _cckyber_poly_reduce
+ _cckyber_poly_sub
+ _cckyber_poly_to_msg
+ _cckyber_poly_toplant
+ _cckyber_polyvec_add
+ _cckyber_polyvec_basemul
+ _cckyber_polyvec_compress
+ _cckyber_polyvec_decode
+ _cckyber_polyvec_decompress
+ _cckyber_polyvec_encode
+ _cckyber_polyvec_ntt_forward
+ _cckyber_polyvec_reduce
+ _cckyber_sample_cbd_eta2
+ _cckyber_sample_uniform
+ _cckyber_zetas
+ _ccm_decrypt_info
+ _ccm_encrypt_info
+ _ccshake128
+ _entropy_list_info
+ _entropy_lock_info
+ _fipspost_post_shake
- _PQCLEAN_KYBER768_CLEAN_barrett_reduce
- _PQCLEAN_KYBER768_CLEAN_basemul
- _PQCLEAN_KYBER768_CLEAN_crypto_kem_dec
- _PQCLEAN_KYBER768_CLEAN_crypto_kem_enc
- _PQCLEAN_KYBER768_CLEAN_crypto_kem_keypair
- _PQCLEAN_KYBER768_CLEAN_gen_matrix
- _PQCLEAN_KYBER768_CLEAN_indcpa_dec
- _PQCLEAN_KYBER768_CLEAN_indcpa_enc
- _PQCLEAN_KYBER768_CLEAN_indcpa_keypair
- _PQCLEAN_KYBER768_CLEAN_invntt
- _PQCLEAN_KYBER768_CLEAN_kyber_shake256_prf
- _PQCLEAN_KYBER768_CLEAN_kyber_shake256_rkprf
- _PQCLEAN_KYBER768_CLEAN_montgomery_reduce
- _PQCLEAN_KYBER768_CLEAN_ntt
- _PQCLEAN_KYBER768_CLEAN_poly_add
- _PQCLEAN_KYBER768_CLEAN_poly_basemul_montgomery
- _PQCLEAN_KYBER768_CLEAN_poly_cbd_eta1
- _PQCLEAN_KYBER768_CLEAN_poly_cbd_eta2
- _PQCLEAN_KYBER768_CLEAN_poly_compress
- _PQCLEAN_KYBER768_CLEAN_poly_decompress
- _PQCLEAN_KYBER768_CLEAN_poly_frombytes
- _PQCLEAN_KYBER768_CLEAN_poly_frommsg
- _PQCLEAN_KYBER768_CLEAN_poly_getnoise_eta1
- _PQCLEAN_KYBER768_CLEAN_poly_getnoise_eta2
- _PQCLEAN_KYBER768_CLEAN_poly_invntt_tomont
- _PQCLEAN_KYBER768_CLEAN_poly_ntt
- _PQCLEAN_KYBER768_CLEAN_poly_reduce
- _PQCLEAN_KYBER768_CLEAN_poly_sub
- _PQCLEAN_KYBER768_CLEAN_poly_tobytes
- _PQCLEAN_KYBER768_CLEAN_poly_tomont
- _PQCLEAN_KYBER768_CLEAN_poly_tomsg
- _PQCLEAN_KYBER768_CLEAN_polyvec_add
- _PQCLEAN_KYBER768_CLEAN_polyvec_basemul_acc_montgomery
- _PQCLEAN_KYBER768_CLEAN_polyvec_compress
- _PQCLEAN_KYBER768_CLEAN_polyvec_decompress
- _PQCLEAN_KYBER768_CLEAN_polyvec_frombytes
- _PQCLEAN_KYBER768_CLEAN_polyvec_invntt_tomont
- _PQCLEAN_KYBER768_CLEAN_polyvec_ntt
- _PQCLEAN_KYBER768_CLEAN_polyvec_reduce
- _PQCLEAN_KYBER768_CLEAN_polyvec_tobytes
- _PQCLEAN_KYBER768_CLEAN_zetas
- _cbd2
- _cckem_kyber_export_privkey
- _cckem_kyber_export_pubkey
- _cckem_kyber_import_privkey
- _cckem_kyber_import_pubkey
- _ccm_decrypt
- _ccm_encrypt
- _rej_uniform
CStrings:
+ "Bogus Kyber parameter."
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 0-bit message failed\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 1600-bit message failed\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 0-bit message failed\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 1600-bit message failed\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_shake: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_shake\n"
+ "fipspost_post_shake"

```
