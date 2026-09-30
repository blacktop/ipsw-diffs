## libVariableRuntimeDxe.dylib

> `/System/Library/PrivateFrameworks/EfiSupport.framework/Versions/A/libVariableRuntimeDxe.dylib`

```diff

-  __TEXT.__text: 0xb34a8
+  __TEXT.__text: 0xb3294
   __TEXT.__cstring: 0x177e4
   __TEXT.__ustring: 0x478
   __TEXT.__const: 0xeef0
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x2c08
+  __TEXT.__unwind_info: 0x2c10
   __TEXT.__eh_frame: 0x2564
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x16980
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _GetIndexFromSupportedLangCodes : 324 -> 332
~ _GetLangFromSupportedLangCodes : 236 -> 228
~ _GetFvbInfoByAddress : 340 -> 352
~ _InternalMemCopyMem : 400 -> 364
~ _MemoryFence : 16 -> 8
~ _BasePrintLibSPrintMarker : 3936 -> 3924
~ _ossl_i2c_uint64_int : 88 -> 92
~ _a2d_ASN1_OBJECT : 1060 -> 1036
~ _ossl_c2i_ASN1_OBJECT : 620 -> 612
~ _generate_v3 : 2076 -> 2064
~ _asn1_cb : 848 -> 836
~ _ASN1_get_object : 612 -> 560
~ _ASN1_put_object : 264 -> 256
~ _strip_ends : 228 -> 200
~ _mime_hdr_new : 316 -> 300
~ _mime_hdr_addparam : 312 -> 292
~ _ossl_asn1_do_adb : 280 -> 272
~ _readbuffer_gets : 432 -> 416
~ _BN_bn2dec : 584 -> 564
~ _BN_CTX_get : 352 -> 364
~ _bn_sqr_normal : 280 -> 268
~ _ossl_decoder_from_algorithm : 524 -> 512
~ _evp_asym_cipher_from_algorithm : 616 -> 608
~ _evp_pkey_ctx_setget_params_to_ctrl : 420 -> 412
~ _evp_pkey_get_params_to_ctrl : 352 -> 332
~ _fix_rsa_padding_mode : 724 -> 752
~ _fix_rsa_pss_saltlen : 428 -> 448
~ _fix_hkdf_mode : 312 -> 324
~ _fix_kdf_type : 424 -> 416
~ _ossl_dh_gen_type_name2id : 128 -> 140
~ _evp_md_from_algorithm : 1048 -> 1040
~ _evp_cipher_from_algorithm : 928 -> 920
~ _evp_rand_from_algorithm : 828 -> 820
~ _evp_kdf_from_algorithm : 584 -> 576
~ _keymgmt_from_algorithm : 1088 -> 1080
~ _evp_mac_from_algorithm : 580 -> 572
~ _evp_pkey_type2name : 56 -> 64
~ _evp_signature_from_algorithm : 2216 -> 2208
~ _evp_pkey_signature_init : 1600 -> 1592
~ _ossl_ht_insert : 736 -> 764
~ _grow_hashtable : 472 -> 476
~ _OSSL_parse_url : 1452 -> 1472
~ _algorithm_do_this : 416 -> 408
~ _OPENSSL_strlcat : 96 -> 92
~ _hexstr2buf_sep : 316 -> 308
~ _OPENSSL_strncasecmp : 144 -> 128
~ _OSSL_PARAM_locate : 104 -> 88
~ _OSSL_PARAM_free : 132 -> 116
~ _OSSL_PARAM_allocate_from_text : 892 -> 888
~ _provider_activate : 1176 -> 1168
~ _provider_activate_fallbacks : 372 -> 356
~ _CRYPTO_THREAD_init_local : 68 -> 80
~ _load_iv : 232 -> 236
~ _parse_name : 448 -> 432
~ _parse_value : 1584 -> 1576
~ _ossl_parse_query : 708 -> 712
~ _ossl_property_match_count : 392 -> 436
~ _RSA_padding_check_PKCS1_OAEP_mgf1 : 1244 -> 1240
~ _RSA_padding_check_PKCS1_type_1 : 428 -> 424
~ _ossl_rsa_verify_PKCS1_PSS_mgf1 : 1076 -> 1068
~ _ossl_rsa_oaeppss_nid2name : 60 -> 68
~ _RSA_padding_check_X931 : 316 -> 304
~ _SHA3_squeeze : 280 -> 260
~ _sha1_block_data_order : 812 -> 804
~ _SHA256_Final : 528 -> 516
~ _sha256_block_data_order : 636 -> 612
~ _SHA512_Final : 752 -> 740
~ _ossl_sm3_block_data_order : 9452 -> 9356
~ _OPENSSL_sk_delete_ptr : 144 -> 164
~ _UI_set_result_ex : 456 -> 448
~ _set_reasons : 276 -> 260
~ _X509V3_parse_list : 528 -> 520
~ _strip_spaces : 188 -> 172
~ _X509V3_NAME_from_section : 240 -> 232
~ _equal_email : 188 -> 212
~ _X509_NAME_print : 352 -> 336
~ _ossl_prov_bio_from_dispatch : 340 -> 332
~ _ossl_prov_seeding_from_dispatch : 456 -> 440
~ _pem2der_decode : 784 -> 792
~ _ossl_prov_get_keymgmt_export : 48 -> 40
~ _ossl_rand_drbg_new : 572 -> 628
~ _add_bytes : 136 -> 128
~ _tls1_sha256_final_raw : 72 -> 68
~ _tls1_sha512_final_raw : 116 -> 112
~ _ossl_gcm_get_ctx_params : 492 -> 472
~ _ossl_gcm_set_ctx_params : 688 -> 676
~ _ossl_uefi_provider_init : 324 -> 316
~ _EfiGetSystemConfigurationTable : 236 -> 244
~ _RegisterVariablePolicy : 676 -> 668
~ _VariablePropertyGetWithWildcardName : 356 -> 372
~ _CheckSignatureListFormat : 636 -> 640

```
