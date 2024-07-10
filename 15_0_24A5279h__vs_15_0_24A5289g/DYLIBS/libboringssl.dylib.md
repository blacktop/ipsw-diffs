## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.0.2.0.0
-  __TEXT.__text: 0x99e08
-  __TEXT.__auth_stubs: 0x15c0
+486.0.8.0.0
+  __TEXT.__text: 0x98514
+  __TEXT.__auth_stubs: 0x15e0
   __TEXT.__objc_methlist: 0xd8
-  __TEXT.__cstring: 0x113a5
-  __TEXT.__const: 0x10c48
-  __TEXT.__oslogstring: 0x5271
-  __TEXT.__gcc_except_tab: 0x28cc
-  __TEXT.__unwind_info: 0x2158
+  __TEXT.__cstring: 0x115a3
+  __TEXT.__const: 0x10078
+  __TEXT.__oslogstring: 0x52be
+  __TEXT.__gcc_except_tab: 0x27ac
+  __TEXT.__unwind_info: 0x20f8
   __TEXT.__eh_frame: 0xe8
   __TEXT.__objc_classname: 0x245
   __TEXT.__objc_methname: 0xe17
   __TEXT.__objc_methtype: 0x6f7
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xadb0
+  __DATA_CONST.__const: 0xae18
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xaf0
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1ff0
+  __AUTH_CONST.__auth_got: 0xb00
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x1f78
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x2318
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0xac0
-  __DATA.__bss: 0x128
+  __DATA.__data: 0xc08
+  __DATA.__bss: 0x9a8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x2b0
-  __DATA_DIRTY.__bss: 0xa90
+  __DATA_DIRTY.__data: 0x1e0
+  __DATA_DIRTY.__bss: 0x948
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2971
-  Symbols:   4238
-  CStrings:  2863
+  Functions: 2972
+  Symbols:   4262
+  CStrings:  2876
 
Symbols:
+ BORINGSSL_keccak_absorb.cold.1
+ CRYPTO_get_ex_new_index_ex.cold.1
+ CRYPTO_tls13_hkdf_expand_label.kProtocolLabel
+ GCC_except_table149
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table30
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table32
+ GCC_except_table349
+ GCC_except_table350
+ GCC_except_table352
+ GCC_except_table354
+ GCC_except_table355
+ GCC_except_table361
+ GCC_except_table363
+ GCC_except_table368
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table50
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table97
+ OPENSSL_sk_find.cold.1
+ OPENSSL_sk_find.cold.2
+ OPENSSL_sk_find.cold.3
+ RSA_padding_add_PKCS1_OAEP_mgf1.cold.1
+ RSA_padding_check_PKCS1_OAEP_mgf1.cold.1
+ SSL_CIPHER_get_handshake_digest.cold.1
+ _BORINGSSL_keccak
+ _BORINGSSL_keccak_absorb
+ _BORINGSSL_keccak_init
+ _BORINGSSL_keccak_squeeze
+ _CRYPTO_get_ex_new_index_ex
+ _CRYPTO_tls13_hkdf_expand_label
+ _EC_GROUP_get0_generator
+ _EC_GROUP_order_bits
+ _EC_group_p224
+ _EC_group_p224_init
+ _EC_group_p224_once
+ _EC_group_p224_storage
+ _EC_group_p256
+ _EC_group_p256_init
+ _EC_group_p256_once
+ _EC_group_p256_storage
+ _EC_group_p384
+ _EC_group_p384_init
+ _EC_group_p384_once
+ _EC_group_p384_storage
+ _EC_group_p521
+ _EC_group_p521_init
+ _EC_group_p521_once
+ _EC_group_p521_storage
+ _EVP_MD_nid
+ _KYBER_decap
+ _KYBER_encap
+ _KYBER_encap_external_entropy
+ _KYBER_generate_key
+ _KYBER_generate_key_external_entropy
+ _KYBER_parse_public_key
+ _OBJ_cmp
+ _OPENSSL_calloc
+ _OPENSSL_sk_deep_copy
+ _OPENSSL_sk_dup
+ _OPENSSL_sk_find
+ _OPENSSL_sk_free
+ _OPENSSL_sk_insert
+ _OPENSSL_sk_new
+ _OPENSSL_sk_new_null
+ _OPENSSL_sk_num
+ _OPENSSL_sk_pop_free_ex
+ _OPENSSL_sk_push
+ _OPENSSL_sk_set
+ _OPENSSL_sk_value
+ _OPENSSL_zalloc
+ _SSL_CIPHER_get_handshake_digest
+ _SSL_CTX_set_strict_cipher_list
+ _SSL_get_group_name
+ _ZN4bssl12_GLOBAL__N_110ECKeyShare5DecapEPNS_5ArrayIhEEPhNS_4SpanIKhEE.cold.1
+ _ZN4bssl12_GLOBAL__N_110ECKeyShare5DecapEPNS_5ArrayIhEEPhNS_4SpanIKhEE.cold.2
+ _ZN4bssl12_GLOBAL__N_110ECKeyShare8GenerateEP6cbb_st.cold.1
+ _ZN4bssl20ssl_client_handshakeEPNS_13SSL_HANDSHAKEE.cold.11
+ _ZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcb.cold.1
+ _ZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcb.cold.2
+ _ZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcb.cold.3
+ _ZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcb.cold.4
+ _ZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcb.cold.5
+ _ZN4bssl29ssl_tls13_cipher_meets_policyEt23ssl_compliance_policy_t.cold.1
+ _ZN4bssl29ssl_tls13_cipher_meets_policyEt23ssl_compliance_policy_t.cold.2
+ _ZN4bssl29ssl_tls13_cipher_meets_policyEt23ssl_compliance_policy_t.cold.3
+ _ZN4bsslL31ext_alps_parse_serverhello_implEPNS_13SSL_HANDSHAKEEPhP6cbs_stb.cold.1
+ _ZN4bsslL31ext_alps_parse_serverhello_implEPNS_13SSL_HANDSHAKEEPhP6cbs_stb.cold.2
+ _ZN4bsslL31ext_alps_parse_serverhello_implEPNS_13SSL_HANDSHAKEEPhP6cbs_stb.cold.3
+ _ZN4bsslL31ext_alps_parse_serverhello_implEPNS_13SSL_HANDSHAKEEPhP6cbs_stb.cold.4
+ __ZL14kUnknownCipher
+ __ZL20ssl_str_to_group_idsPN4bssl5ArrayItEEPKc
+ __ZN4bssl10RefCountedI10ssl_ctx_stE14DecRefInternalEv
+ __ZN4bssl10RefCountedI14ssl_session_stE14DecRefInternalEv
+ __ZN4bssl10RefCountedI15ssl_ech_keys_stE14DecRefInternalEv
+ __ZN4bssl12_GLOBAL__N_110ECKeyShare5DecapEPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_110ECKeyShare5EncapEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_110ECKeyShare8GenerateEP6cbb_st
+ __ZN4bssl12_GLOBAL__N_114X25519KeyShare5DecapEPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_114X25519KeyShare5EncapEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_114X25519KeyShare8GenerateEP6cbb_st
+ __ZN4bssl12_GLOBAL__N_122X25519Kyber768KeyShare5DecapEPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_122X25519Kyber768KeyShare5EncapEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_122X25519Kyber768KeyShare8GenerateEP6cbb_st
+ __ZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcb
+ __ZN4bssl23ssl_choose_tls13_cipherE6cbs_stbt23ssl_compliance_policy_t
+ __ZN4bssl26ssl_send_tls12_certificateEPNS_13SSL_HANDSHAKEE
+ __ZN4bssl28ssl_cipher_auth_mask_for_keyEPK11evp_pkey_stb
+ __ZN4bssl29ssl_tls13_cipher_meets_policyEt23ssl_compliance_policy_t
+ __ZN4bsslL13kVersionNamesE
+ __ZN4bsslL21ssl_cipher_apply_ruleEjPKNS_15cipher_alias_stEiibPPNS_15cipher_order_stES5_
+ __ZN4bsslL28ext_alps_add_clienthello_oldEPKNS_13SSL_HANDSHAKEEP6cbb_stS4_NS_23ssl_client_hello_type_tE
+ __ZN4bsslL28ext_alps_add_serverhello_oldEPNS_13SSL_HANDSHAKEEP6cbb_st
+ __ZN4bsslL29ext_alps_add_clienthello_implEPKNS_13SSL_HANDSHAKEEP6cbb_stS4_NS_23ssl_client_hello_type_tEb
+ __ZN4bsslL29ext_alps_add_serverhello_implEPNS_13SSL_HANDSHAKEEP6cbb_stb
+ __ZN4bsslL30ext_alps_parse_serverhello_oldEPNS_13SSL_HANDSHAKEEPhP6cbs_st
+ __ZN4bsslL31ext_alps_parse_serverhello_implEPNS_13SSL_HANDSHAKEEPhP6cbs_stb
+ __ZNSt3__110unique_ptrIhN4bssl8internal7DeleterEE5resetB8ne180100EPh
+ __ZZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcbE11kAESCiphers
+ __ZZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcbE14kChaChaCiphers
+ __ZZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEbPKcbE14kLegacyCiphers
+ __ZdlPvSt19__type_descriptor_t
+ _bio_errno_should_retry
+ _bio_socket_should_retry
+ _bn_mont_ctx_cleanup
+ _bn_mont_ctx_init
+ _bn_mont_ctx_set_RR_consttime
+ _bn_set_static_words
+ _ec_felem_one
+ _ec_group_set_a_minus3
+ _encrypt_cpa
+ _kAllGroups
+ _kInverseNTTRoots
+ _kMasks
+ _kModRoots
+ _kNTTRoots
+ _kP224B
+ _kP224Field
+ _kP224FieldRR
+ _kP224GX
+ _kP224GY
+ _kP224Order
+ _kP224OrderRR
+ _kP256Field
+ _kP256FieldR
+ _kP256FieldRR
+ _kP256MontB
+ _kP256MontGX
+ _kP256MontGY
+ _kP256Order
+ _kP256OrderRR
+ _kP384Field
+ _kP384FieldR
+ _kP384FieldRR
+ _kP384MontB
+ _kP384MontGX
+ _kP384MontGY
+ _kP384Order
+ _kP384OrderRR
+ _kP521Field
+ _kP521FieldR
+ _kP521FieldRR
+ _kP521MontB
+ _kP521MontGX
+ _kP521MontGY
+ _kP521Order
+ _kP521OrderRR
+ _keccak_f
+ _keccak_init
+ _kyber_marshal_public_key
+ _kyber_parse_public_key_no_hash
+ _matrix_expand
+ _reduce
+ _reduce_once
+ _scalar_centered_binomial_distribution_eta_2_with_prf
+ _scalar_compress
+ _scalar_decode
+ _scalar_encode
+ _scalar_inner_product
+ _scalar_inverse_ntt
+ _scalar_mult
+ _snprintf
+ _vector_ntt
+ _x25519_auth_decap
+ _x25519_auth_encap_with_seed
+ arbitrary_bignum_to_scalar.cold.1
+ bn_mont_ctx_set_RR_consttime.cold.1
+ bn_mont_ctx_set_RR_consttime.cold.2
+ bn_mont_ctx_set_RR_consttime.cold.3
+ bn_mont_ctx_set_RR_consttime.cold.4
+ bn_mont_ctx_set_RR_consttime.cold.5
+ bn_mont_ctx_set_RR_consttime.cold.6
+ bn_mont_ctx_set_RR_consttime.cold.7
+ bn_set_static_words.cold.1
+ bn_sub_part_words.cold.2
+ bn_sub_part_words.cold.3
+ bn_uadd_consttime.cold.1
+ bn_usub_consttime.cold.1
+ ec_get_x_coordinate_as_scalar.cold.1
+ keccak_f.kRoundConstants
+ matrix_expand.cold.1
+ matrix_expand.cold.2
+ reduce.cold.1
+ reduce_once.cold.1
+ scalar_compress.cold.1
+ table_select.cold.1
- GCC_except_table146
- GCC_except_table150
- GCC_except_table152
- GCC_except_table156
- GCC_except_table26
- GCC_except_table27
- GCC_except_table331
- GCC_except_table332
- GCC_except_table334
- GCC_except_table336
- GCC_except_table337
- GCC_except_table34
- GCC_except_table343
- GCC_except_table346
- GCC_except_table351
- GCC_except_table42
- GCC_except_table42
- GCC_except_table44
- GCC_except_table47
- GCC_except_table47
- GCC_except_table51
- GCC_except_table60
- GCC_except_table60
- HRSS_decap.cold.1
- HRSS_encap.cold.1
- HRSS_generate_key.cold.1
- HRSS_generate_key.cold.2
- HRSS_generate_key.cold.3
- HRSS_generate_key.cold.4
- HRSS_marshal_public_key.cold.1
- HRSS_parse_public_key.cold.1
- HRSS_poly3_invert.cold.1
- OPENSSL_built_in_curves_do_init.kOIDP224
- OPENSSL_built_in_curves_do_init.kOIDP256
- OPENSSL_built_in_curves_do_init.kOIDP384
- OPENSSL_built_in_curves_do_init.kOIDP521
- SSL_CIPHER_get_prf_nid.cold.1
- SSL_CIPHER_get_value.cold.1
- _BIO_snprintf
- _BN_MONT_CTX_new_for_modulus
- _BN_MONT_CTX_set
- _BUF_MEM_grow
- _BUF_MEM_grow_clean
- _CBS_data
- _CBS_init
- _CBS_len
- _CRYPTO_get_ex_new_index
- _HRSS_decap
- _HRSS_encap
- _HRSS_generate_key
- _HRSS_marshal_public_key
- _HRSS_parse_public_key
- _HRSS_poly3_invert
- _HRSS_poly3_mul
- _OPENSSL_built_in_curves
- _OPENSSL_built_in_curves_init
- _OPENSSL_built_in_curves_once
- _OPENSSL_built_in_curves_storage
- _SSL_CIPHER_get_value
- _SSL_CTX_set1_curves
- _SSL_set1_curves
- _ZN4bssl12_GLOBAL__N_110ECKeyShare5OfferEP6cbb_st.cold.1
- _ZN4bssl12_GLOBAL__N_110ECKeyShare6FinishEPNS_5ArrayIhEEPhNS_4SpanIKhEE.cold.1
- _ZN4bssl12_GLOBAL__N_110ECKeyShare6FinishEPNS_5ArrayIhEEPhNS_4SpanIKhEE.cold.2
- _ZN4bssl29ssl_tls13_cipher_meets_policyEtb.cold.1
- _ZN4bsslL26ext_alps_parse_serverhelloEPNS_13SSL_HANDSHAKEEPhP6cbs_st.cold.1
- _ZN4bsslL26ext_alps_parse_serverhelloEPNS_13SSL_HANDSHAKEEPhP6cbs_st.cold.2
- _ZN4bsslL26ext_alps_parse_serverhelloEPNS_13SSL_HANDSHAKEEPhP6cbs_st.cold.3
- __ZN4bssl10MakeUniqueINS_12_GLOBAL__N_110ECKeyShareEJiiEEENSt3__110unique_ptrIT_NS_8internal7DeleterEEEDpOT0_
- __ZN4bssl11SSLKeyShare6AcceptEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_110ECKeyShare5OfferEP6cbb_st
- __ZN4bssl12_GLOBAL__N_110ECKeyShare6FinishEPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_114CECPQ2KeyShare5OfferEP6cbb_st
- __ZN4bssl12_GLOBAL__N_114CECPQ2KeyShare6AcceptEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_114CECPQ2KeyShare6FinishEPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_114CECPQ2KeyShareD0Ev
- __ZN4bssl12_GLOBAL__N_114CECPQ2KeyShareD1Ev
- __ZN4bssl12_GLOBAL__N_114X25519KeyShare5OfferEP6cbb_st
- __ZN4bssl12_GLOBAL__N_114X25519KeyShare6FinishEPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_120P256Kyber768KeyShare5OfferEP6cbb_st
- __ZN4bssl12_GLOBAL__N_120P256Kyber768KeyShare6AcceptEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_120P256Kyber768KeyShare6FinishEPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_120P256Kyber768KeyShareD0Ev
- __ZN4bssl12_GLOBAL__N_120P256Kyber768KeyShareD1Ev
- __ZN4bssl12_GLOBAL__N_122X25519Kyber768KeyShare5OfferEP6cbb_st
- __ZN4bssl12_GLOBAL__N_122X25519Kyber768KeyShare6AcceptEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl12_GLOBAL__N_122X25519Kyber768KeyShare6FinishEPNS_5ArrayIhEEPhNS_4SpanIKhEE
- __ZN4bssl15tls1_set_curvesEPNS_5ArrayItEENS_4SpanIKiEE
- __ZN4bssl18ssl_add_cert_chainEPNS_13SSL_HANDSHAKEEP6cbb_st
- __ZN4bssl20ssl_cert_clear_certsEPNS_4CERTE
- __ZN4bssl20tls1_set_curves_listEPNS_5ArrayItEEPKc
- __ZN4bssl21ssl_output_cert_chainEPNS_13SSL_HANDSHAKEE
- __ZN4bssl22ssl_create_cipher_listEPNSt3__110unique_ptrINS_23SSLCipherPreferenceListENS_8internal7DeleterEEEPKcb
- __ZN4bssl23ssl_choose_tls13_cipherE6cbs_stttb
- __ZN4bssl28ssl_cipher_auth_mask_for_keyEPK11evp_pkey_st
- __ZN4bssl29ssl_tls13_cipher_meets_policyEtb
- __ZN4bssl5ArrayINS_15cipher_order_stEED2Ev
- __ZN4bsslL17hkdf_expand_labelENS_4SpanIhEEPK9env_md_stNS0_IKhEENS0_IKcEES6_
- __ZN4bsslL21ssl_cipher_apply_ruleEjjjjjtiibPPNS_15cipher_order_stES2_
- __ZN4bsslL21ssl_version_to_stringEt
- __ZNK4bssl12_GLOBAL__N_114CECPQ2KeyShare7GroupIDEv
- __ZNK4bssl12_GLOBAL__N_120P256Kyber768KeyShare7GroupIDEv
- __ZNSt3__110unique_ptrI11ec_group_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZTIN4bssl12_GLOBAL__N_114CECPQ2KeyShareE
- __ZTIN4bssl12_GLOBAL__N_120P256Kyber768KeyShareE
- __ZTSN4bssl12_GLOBAL__N_114CECPQ2KeyShareE
- __ZTSN4bssl12_GLOBAL__N_120P256Kyber768KeyShareE
- __ZTVN4bssl12_GLOBAL__N_114CECPQ2KeyShareE
- __ZTVN4bssl12_GLOBAL__N_120P256Kyber768KeyShareE
- _bio_fd_should_retry
- _bn_mod_exp_base_2_consttime
- _built_in_groups
- _built_in_groups_lock
- _ec_GFp_mont_group_finish
- _ec_GFp_mont_group_init
- _ec_GFp_mont_group_set_curve
- _ec_GFp_simple_group_finish
- _ec_GFp_simple_group_init
- _ec_GFp_simple_group_set_curve
- _ec_group_new
- _ec_group_set_generator
- _ec_wrapped_scalar_new
- _ge_precomp_0
- _kBoringSSLBinaryTag
- _kP224Params
- _kP256Params
- _kP384Params
- _kP521Params
- _kSharedKey
- _malloc_align32
- _poly2_reverse_700
- _poly3_cswap
- _poly3_from_poly
- _poly3_mul_aux
- _poly3_span_sub
- _poly_assert_normalized
- _poly_from_poly3
- _poly_lift
- _poly_marshal
- _poly_marshal_mod3
- _poly_mul
- _poly_mul_vec_aux
- _poly_short_sample
- _poly_short_sample_plus
- _poly_unmarshal
- _rsa_default_decrypt
- _sk_deep_copy
- _sk_delete
- _sk_dup
- _sk_find
- _sk_free
- _sk_insert
- _sk_new
- _sk_new_null
- _sk_num
- _sk_pop
- _sk_pop_free_ex
- _sk_push
- _sk_set
- _sk_shift
- _sk_value
- bn_big_endian_to_words.cold.1
- bn_mod_exp_base_2_consttime.cold.1
- bn_mod_exp_base_2_consttime.cold.2
- bn_mod_exp_base_2_consttime.cold.3
- bn_mod_exp_base_2_consttime.cold.4
- bn_mod_exp_base_2_consttime.cold.5
- ec_group_set_generator.cold.1
- ec_group_set_generator.cold.2
- ec_group_set_generator.cold.3
- ec_point_set_affine_coordinates.cold.1
- malloc_align32.cold.1
- poly_assert_normalized.cold.1
- poly_assert_normalized.cold.2
- poly_assert_normalized.cold.3
- poly_marshal_mod3.cold.1
- rsa_default_decrypt.cold.1
- sk_find.cold.1
- sk_find.cold.2
- sk_find.cold.3
- word_reverse.kMasks
CStrings:
+ "!BN_is_negative(&mont->N)"
+ "!BN_is_zero(&mont->N)"
+ "!buffers_alias(dst, n, src, n)"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio_mem.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/file.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/buf/buf.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bytestring/cbb.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/cipher_extra/e_tls.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/dsa/dsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_ctx.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ex_data.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/add.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/bn.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/ctx.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/div.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/mul.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/prime.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/random.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/shift.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/aead.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digest/digest.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/felem.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/oct.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p256.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/scalar.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/simple.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/rsa/padding.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/hpke/hpke.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/mem.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/stack/stack.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_both.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_lib.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_pkt.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_method.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_record.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/encrypted_client_hello.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/extensions.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_client.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_server.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/internal.h"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_both.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_pkt.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_aead_ctx.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_asn1.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_buffer.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cert.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cipher.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_key_share.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_lib.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_privkey.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_session.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_transcript.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_versions.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/t1_enc.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_both.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_client.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_enc.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_server.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_method.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_record.cc"
+ "BORINGSSL_keccak_absorb"
+ "CBS_len(&server_hello.session_id) <= SSL3_SESSION_ID_SIZE"
+ "CRYPTO_addc_u64"
+ "CRYPTO_get_ex_new_index_ex"
+ "CRYPTO_subc_u64"
+ "Decap"
+ "ECDHE-RSA-AES128-SHA256"
+ "Generate"
+ "OPENSSL_sk_find"
+ "RSA_padding_add_PKCS1_OAEP_mgf1"
+ "RSA_padding_check_PKCS1_OAEP_mgf1"
+ "SSL_CIPHER_get_handshake_digest"
+ "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
+ "X25519Kyber768Draft00"
+ "ab"
+ "ab+"
+ "bn.c"
+ "bn_minimal_width(&mont->N) == mont->N.width"
+ "bn_mont_ctx_set_RR_consttime"
+ "bn_set_static_words"
+ "borrow <= 1"
+ "carry <= 1"
+ "co_list[num - 1].cipher != nullptr"
+ "compress"
+ "constant_time_conditional_memxor"
+ "ctx->absorb_offset < ctx->rate_bytes"
+ "ext_alps_parse_serverhello_impl"
+ "field_len == BN_num_bytes(&group->field.N)"
+ "group->field.N.width == group->order.N.width"
+ "group->has_order"
+ "keccak.c"
+ "keccak_ctx->rate_bytes == 168"
+ "keccak_ctx->squeeze_offset == 0"
+ "kyber.c"
+ "lgBigR >= n_bits"
+ "num <= BN_MAX_WORDS"
+ "num == OPENSSL_ARRAY_SIZE(co_list)"
+ "num_funcs <= (size_t)(INT_MAX - ex_data_class->num_reserved)"
+ "num_funcs == 0"
+ "rb"
+ "rb+"
+ "reduce"
+ "reduce_once"
+ "remainder < 2u * kPrime"
+ "scalar_from_keccak_vartime"
+ "ssl_create_cipher_list"
+ "ssl_str_to_group_ids"
+ "threshold == mont->N.width"
+ "use_new_codepoint == hs->config->alps_use_new_codepoint"
+ "wb"
+ "x < 2 * kPrime"
+ "x < kPrime + 2u * kPrime * kPrime"
- "!BN_is_zero(&group->order)"
- "!is_zero"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio_mem.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/file.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/buf/buf.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bytestring/cbb.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/cipher_extra/e_tls.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/dsa/dsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_ctx.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ex_data.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/add.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/bn.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/ctx.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/div.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/mul.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/prime.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/random.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/shift.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/aead.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digest/digest.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/felem.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/oct.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p256.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/scalar.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/simple.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/wnaf.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/rsa/padding.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/hpke/hpke.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/mem.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_both.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_lib.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_pkt.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_method.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_record.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/encrypted_client_hello.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/extensions.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_client.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_server.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/internal.h"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_both.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_pkt.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_aead_ctx.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_asn1.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_buffer.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cert.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cipher.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_key_share.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_lib.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_privkey.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_session.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_transcript.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_versions.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/t1_enc.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_both.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_client.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_enc.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_server.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_method.cc"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_record.cc"
- "CECPQ2"
- "Finish"
- "HRSS_poly3_invert"
- "Offer"
- "P256Kyber768"
- "SSL_CIPHER_get_prf_nid"
- "UNDEF"
- "X25519Kyber768"
- "a"
- "a+"
- "bn_big_endian_to_words"
- "bn_mod_exp_base_2_consttime"
- "coeffs[N-1] == 0"
- "delta == 0"
- "ec_felem_equal(group, &group->one, &group->generator->raw.Z)"
- "ec_group_set_generator"
- "ec_point_set_affine_coordinates"
- "ext_alps_parse_serverhello"
- "f.v[0] & 1"
- "field_len == BN_num_bytes(&group->field)"
- "group->field.width == group->order.width"
- "group->generator == NULL"
- "hrss.c"
- "in_len == 0"
- "p > n_bits"
- "poly_assert_normalized"
- "poly_invert_mod2"
- "poly_marshal_mod3"
- "r"
- "r+"
- "rsa_default_decrypt"
- "sk_CRYPTO_EX_DATA_FUNCS_num(func_pointers) <= (size_t)(INT_MAX - ex_data_class->num_reserved)"
- "sk_find"
- "tls13 "
- "tls1_set_curves_list"
- "undefined"
- "w"
- "x->v[N + 1] == 0"
- "x->v[N + 2] == 0"
- "x->v[N] == 0"

```
