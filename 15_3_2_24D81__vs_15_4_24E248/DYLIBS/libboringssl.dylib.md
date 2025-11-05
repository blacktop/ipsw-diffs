## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.60.4.0.0
-  __TEXT.__text: 0x99cd8
-  __TEXT.__auth_stubs: 0x15e0
-  __TEXT.__objc_methlist: 0xd8
-  __TEXT.__cstring: 0x11b89
-  __TEXT.__const: 0x10078
-  __TEXT.__oslogstring: 0x52be
-  __TEXT.__gcc_except_tab: 0x2978
-  __TEXT.__unwind_info: 0x21c8
-  __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x245
-  __TEXT.__objc_methname: 0xe17
+486.100.28.0.0
+  __TEXT.__text: 0x9fabc
+  __TEXT.__auth_stubs: 0x1790
+  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__cstring: 0x11dbb
+  __TEXT.__const: 0xfed8
+  __TEXT.__oslogstring: 0x56da
+  __TEXT.__gcc_except_tab: 0x2900
+  __TEXT.__unwind_info: 0x23c0
+  __TEXT.__eh_frame: 0x130
+  __TEXT.__objc_classname: 0x241
+  __TEXT.__objc_methname: 0xe76
   __TEXT.__objc_methtype: 0x6f7
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xb010
+  __TEXT.__objc_stubs: 0x60
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__const: 0xb088
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xb00
-  __AUTH_CONST.__const: 0x1f58
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x2318
+  __AUTH_CONST.__auth_got: 0xbe0
+  __AUTH_CONST.__const: 0x2238
+  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__objc_const: 0x2168
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0xce8
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0xd30
   __DATA.__bss: 0x9a8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D1D95DEA-FA2D-37B9-9D95-1DFFFEADCD17
-  Functions: 3005
-  Symbols:   4316
-  CStrings:  3573
+  UUID: D9D26751-AE96-3A27-8B9D-A3F4A5682366
+  Functions: 3136
+  Symbols:   4558
+  CStrings:  3614
 
Symbols:
+ BN_div.cold.1
+ BN_div.cold.2
+ CRYPTO_chacha_20.cold.1
+ GCC_except_table100
+ GCC_except_table123
+ GCC_except_table131
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table16
+ GCC_except_table161
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table26
+ GCC_except_table356
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table368
+ GCC_except_table370
+ GCC_except_table47
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table67
+ GCC_except_table80
+ GCC_except_table95
+ KYBER_decap.cold.1
+ KYBER_decap.cold.2
+ KYBER_encap.cold.1
+ KYBER_encap.cold.2
+ KYBER_generate_key.cold.1
+ KYBER_generate_key.cold.2
+ KYBER_parse_public_key.cold.1
+ MLKEM768_decap.cold.1
+ MLKEM768_decap.cold.2
+ MLKEM768_encap.cold.1
+ MLKEM768_encap.cold.2
+ MLKEM768_generate_key.cold.1
+ MLKEM768_generate_key.cold.2
+ MLKEM768_parse_public_key.cold.1
+ OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.ats_non_pfs_ciphersuite_allowed
+ OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.pqtls_enabled
+ _AES_encrypt
+ _AES_set_encrypt_key
+ _BCM_rand_bytes
+ _BCM_rand_bytes_with_additional_data
+ _BCM_sha1_init
+ _BCM_sha1_transform
+ _BCM_sha256_final
+ _BCM_sha256_init
+ _BCM_sha256_transform
+ _BCM_sha256_update
+ _BCM_sha384_init
+ _BCM_sha512_final
+ _BCM_sha512_init
+ _BCM_sha512_transform
+ _BCM_sha512_update
+ _CBS_get_asn1_element
+ _CBS_stow
+ _CRYPTO_chacha_20
+ _EC_POINT_add
+ _EC_POINT_invert
+ _HKDF
+ _MLKEM768_decap
+ _MLKEM768_encap
+ _MLKEM768_generate_key
+ _MLKEM768_parse_public_key
+ _MLKEM768_private_key_free
+ _M_bytes
+ _N_bytes
+ _OBJC_CLASS_$_NSString
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _SPAKE2PLUS_CTX_free
+ _SPAKE2PLUS_CTX_new_context
+ _SPAKE2PLUS_CTX_new_prover
+ _SPAKE2PLUS_CTX_new_verifier
+ _SPAKE2PLUS_compute_prover_confirmation
+ _SPAKE2PLUS_generate_prover_share
+ _SPAKE2PLUS_process_prover_share
+ _SSL_CREDENTIAL_new_SPAKE2PLUSV1
+ _SSL_CREDENTIAL_set1_PAKE_client_password_record
+ _SSL_CREDENTIAL_set1_PAKE_identities
+ _SSL_CREDENTIAL_set1_PAKE_server_password_record
+ _SSL_add1_credential
+ _SSL_negotiated_pake
+ _SSL_set_tls13_pqtls_ciphersuites_enabled
+ _TLS_METRIC_ATS_NON_PFS_CIPHERSUITE_ALLOWED
+ _TLS_METRIC_PQTLS_ENABLED
+ _ZN4bssl18dtls1_write_recordEP6ssl_stiNS_4SpanIKhEEt.cold.1
+ _ZN4bssl18dtls1_write_recordEP6ssl_stiNS_4SpanIKhEEt.cold.2
+ _ZN4bssl20ssl_client_handshakeEPNS_13SSL_HANDSHAKEE.cold.11
+ _ZN4bssl20ssl_client_handshakeEPNS_13SSL_HANDSHAKEE.cold.12
+ _ZN4bssl20ssl_client_handshakeEPNS_13SSL_HANDSHAKEE.cold.13
+ _ZN4bssl21ssl_record_prefix_lenEPK6ssl_st.cold.1
+ _ZN4bssl24tls13_derive_session_pskEP14ssl_session_stNS_4SpanIKhEEb.cold.1
+ _ZN4bssl43tls1_record_handshake_hashes_for_channel_idEPNS_13SSL_HANDSHAKEE.cold.1
+ __ZN4bssl12SSLPAKEShareC2EtPKhmS2_mS2_m
+ __ZN4bssl12SSLPAKEShareD0Ev
+ __ZN4bssl12SSLPAKEShareD1Ev
+ __ZN4bssl12SSLPAKEShareD2Ev
+ __ZN4bssl12_GLOBAL__N_116CNsaCipherScorerD0Ev
+ __ZN4bssl12_GLOBAL__N_116CNsaCipherScorerD1Ev
+ __ZN4bssl12_GLOBAL__N_117AesHwCipherScorerD0Ev
+ __ZN4bssl12_GLOBAL__N_117AesHwCipherScorerD1Ev
+ __ZN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShare5DecapEPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShare5EncapEP6cbb_stPNS_5ArrayIhEEPhNS_4SpanIKhEE
+ __ZN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShare8GenerateEP6cbb_st
+ __ZN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShareD0Ev
+ __ZN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShareD1Ev
+ __ZN4bssl13InplaceVectorINS_21DTLS_OUTGOING_MESSAGEELm7EE11TryPushBackES1_
+ __ZN4bssl13InplaceVectorIhLm32EEaSERKS1_
+ __ZN4bssl13InplaceVectorIhLm48EEaSERKS1_
+ __ZN4bssl13InplaceVectorIhLm64EEaSERKS1_
+ __ZN4bssl13SSLTranscript17AddToBufferOrHashENS_4SpanIKhEE
+ __ZN4bssl13SSLTranscriptC1Eb
+ __ZN4bssl13SSLTranscriptC2Eb
+ __ZN4bssl14SSLAEADContext16CreateNullCipherEv
+ __ZN4bssl14SSLAEADContext24CreatePlaceholderForQUICEPK13ssl_cipher_st
+ __ZN4bssl14SSLAEADContext24GenerateRecordNumberMaskENS_4SpanIhEENS1_IKhEE
+ __ZN4bssl14SSLAEADContext27CreateRecordNumberEncrypterEv
+ __ZN4bssl14SSLAEADContext6CreateE20evp_aead_direction_ttPK13ssl_cipher_stNS_4SpanIKhEES7_S7_
+ __ZN4bssl14SSLAEADContextC2EPK13ssl_cipher_st
+ __ZN4bssl14SSLAEADContextD2Ev
+ __ZN4bssl15cxx17_destroy_nIPNS_10ALPSConfigEEET_S3_m
+ __ZN4bssl16dtls_seal_recordEP6ssl_stPhPmmhPKhmt
+ __ZN4bssl16ssl_add_CA_namesEPKNS_13SSL_HANDSHAKEEP6cbb_st
+ __ZN4bssl16ssl_has_CA_namesEPKNS_10SSL_CONFIGE
+ __ZN4bssl17SSL_parse_CA_listEP6ssl_stPhP6cbs_st
+ __ZN4bssl18dtls1_write_recordEP6ssl_stiNS_4SpanIKhEEt
+ __ZN4bssl20dtls_seal_prefix_lenEPK6ssl_stt
+ __ZN4bssl21ssl_setup_pake_sharesEPNS_13SSL_HANDSHAKEE
+ __ZN4bssl22dtls_max_seal_overheadEPK6ssl_stt
+ __ZN4bssl22ssl_add_client_CA_listEPKNS_13SSL_HANDSHAKEEP6cbb_st
+ __ZN4bssl23ssl_cert_extract_issuerEPK6cbs_stPS0_
+ __ZN4bssl23ssl_cert_matches_issuerEPK6cbs_stS2_
+ __ZN4bssl23ssl_cipher_get_evp_aeadEPPK11evp_aead_stPmS4_PK13ssl_cipher_stt
+ __ZN4bssl23tls12_check_peer_sigalgEPKNS_13SSL_HANDSHAKEEPhtP11evp_pkey_st
+ __ZN4bssl24AESRecordNumberEncrypter12GenerateMaskENS_4SpanIhEENS1_IKhEE
+ __ZN4bssl24AESRecordNumberEncrypter6SetKeyENS_4SpanIKhEE
+ __ZN4bssl24tls13_derive_session_pskEP14ssl_session_stNS_4SpanIKhEEb
+ __ZN4bssl26ssl_needs_record_splittingEPK6ssl_st
+ __ZN4bssl27AES128RecordNumberEncrypter7KeySizeEv
+ __ZN4bssl27AES128RecordNumberEncrypterD0Ev
+ __ZN4bssl27AES128RecordNumberEncrypterD1Ev
+ __ZN4bssl27AES256RecordNumberEncrypter7KeySizeEv
+ __ZN4bssl27AES256RecordNumberEncrypterD0Ev
+ __ZN4bssl27AES256RecordNumberEncrypterD1Ev
+ __ZN4bssl27ChaChaRecordNumberEncrypter12GenerateMaskENS_4SpanIhEENS1_IKhEE
+ __ZN4bssl27ChaChaRecordNumberEncrypter6SetKeyENS_4SpanIKhEE
+ __ZN4bssl27ChaChaRecordNumberEncrypter7KeySizeEv
+ __ZN4bssl27ChaChaRecordNumberEncrypterD0Ev
+ __ZN4bssl27ChaChaRecordNumberEncrypterD1Ev
+ __ZN4bssl27ssl_pkey_supports_algorithmEPK6ssl_stP11evp_pkey_sttb
+ __ZN4bssl27tls1_generate_master_secretEPNS_13SSL_HANDSHAKEENS_4SpanIhEENS2_IKhEE
+ __ZN4bssl28dtls_record_header_write_lenEPK6ssl_stt
+ __ZN4bssl30ssl_ext_pake_parse_serverhelloEPNS_13SSL_HANDSHAKEEPtPNS_5ArrayIhEEPhP6cbs_st
+ __ZN4bssl31ssl_alpn_list_contains_protocolENS_4SpanIKhEES2_
+ __ZN4bssl3NewINS_12SSLPAKEShareEJRtPKhmS4_mS4_mEEEPT_DpOT0_
+ __ZN4bssl3NewINS_12SSLPAKEShareEJRtPhmS3_mRA65_hRmEEEPT_DpOT0_
+ __ZN4bssl3NewINS_14SSLAEADContextEJDnEEEPT_DpOT0_
+ __ZN4bssl3NewINS_14SSLAEADContextEJRPK13ssl_cipher_stEEEPT_DpOT0_
+ __ZN4bssl40ssl_credential_matches_requested_issuersEPNS_13SSL_HANDSHAKEEPK17ssl_credential_st
+ __ZN4bssl5ArrayIP17ssl_credential_stE17InitUninitializedEm
+ __ZN4bssl5ArrayIbE17InitUninitializedEm
+ __ZN4bssl5ArrayIhE17InitUninitializedEm
+ __ZN4bssl5ArrayIiE17InitUninitializedEm
+ __ZN4bssl5ArrayItE17InitUninitializedEm
+ __ZN4bssl6DeleteINS_14DTLSEpochStateEEEvPT_
+ __ZN4bssl6VectorINS_10ALPSConfigEED2Ev
+ __ZN4bssl6VectorINS_18CertCompressionAlgEE9MaybeGrowEv
+ __ZN4bssl6VectorINS_18CertCompressionAlgEED2Ev
+ __ZN4bssl6VectorINSt3__110unique_ptrI17ssl_credential_stNS_8internal7DeleterEEEE5clearEv
+ __ZN4bssl6VectorINSt3__110unique_ptrI17ssl_credential_stNS_8internal7DeleterEEEE9MaybeGrowEv
+ __ZN4bssl6VectorINSt3__110unique_ptrINS_15ECHServerConfigENS_8internal7DeleterEEEE5clearEv
+ __ZN4bsslL14get_write_aeadEPK6ssl_stt
+ __ZN4bsslL16marshal_CA_namesEPK22stack_st_CRYPTO_BUFFERS2_P6cbb_st
+ __ZN4bsslL16tls13_psk_binderEPhPmPK14ssl_session_stRKNS_13SSLTranscriptENS_4SpanIKhEEmbb
+ __ZN4bsslL17hkdf_expand_labelENS_4SpanIhEEPK9env_md_stNS0_IKhEENS0_IKcEES6_b
+ __ZN4bsslL17tls13_verify_dataEPhPmPK9env_md_sttNS_4SpanIKhEES7_b
+ __ZN4bsslL22quic_ticket_compatibleEPK14ssl_session_stPKNS_10SSL_CONFIGE
+ __ZN4bsslL24ext_pake_add_clienthelloEPKNS_13SSL_HANDSHAKEEP6cbb_stS4_NS_23ssl_client_hello_type_tE
+ __ZN4bsslL25tls_seal_align_prefix_lenEPK6ssl_st
+ __ZN4bsslL26ext_pake_parse_clienthelloEPNS_13SSL_HANDSHAKEEPhP6cbs_st
+ __ZN4bsslL26parse_dtls13_record_headerEP6ssl_stP6cbs_stNS_4SpanIhEEhS3_PyPtPm
+ __ZN4bsslL29derive_secret_with_transcriptEPKNS_13SSL_HANDSHAKEEPNS_13InplaceVectorIhLm48EEERKNS_13SSLTranscriptENS_4SpanIKcEE
+ __ZN4bsslL42ssl_ext_supported_versions_add_serverhelloEPNS_13SSL_HANDSHAKEEP6cbb_st
+ __ZN4bsslL43ext_certificate_authorities_add_clienthelloEPKNS_13SSL_HANDSHAKEEP6cbb_stS4_NS_23ssl_client_hello_type_tE
+ __ZN4bsslL45ext_certificate_authorities_parse_clienthelloEPNS_13SSL_HANDSHAKEEPhP6cbs_st
+ __ZNK17ssl_credential_st19ChainContainsIssuerEN4bssl4SpanIKhEE
+ __ZNK4bssl12_GLOBAL__N_116CNsaCipherScorer8EvaluateEPK13ssl_cipher_st
+ __ZNK4bssl12_GLOBAL__N_117AesHwCipherScorer8EvaluateEPK13ssl_cipher_st
+ __ZNK4bssl12_GLOBAL__N_122X25519MLKEM768KeyShare7GroupIDEv
+ __ZNK4bssl13SSLTranscript10HashBufferEP13env_md_ctx_stPK9env_md_st
+ __ZNSt3__110unique_ptrI10buf_mem_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI10ssl_ctx_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI11ec_point_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI11evp_pkey_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI12ecdsa_sig_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI14ssl_session_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI15ssl_ech_keys_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI16crypto_buffer_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI17err_save_state_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI17ssl_credential_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI19stack_st_SSL_CIPHERN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI22stack_st_CRYPTO_BUFFERN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI32stack_st_SRTP_PROTECTION_PROFILEN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI6bio_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI6ssl_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI9bignum_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI9ec_key_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrIN4bssl10SSL3_STATEENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl10SSL_CONFIGENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11DTLS1_STATEENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11SSLKeyShareENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11hm_fragmentENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl12SSLPAKEShareENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl12_GLOBAL__N_110ECKeyShareENS1_8internal7DeleterEED1B8ne190102Ev
+ __ZNSt3__110unique_ptrIN4bssl13SSL_HANDSHAKEENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl14DTLSEpochStateENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl14SSLAEADContextENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl15ECHServerConfigENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl19SSL_HANDSHAKE_HINTSENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl21RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl23SSLCipherPreferenceListENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27AES128RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27AES256RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27ChaChaRecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl4CERTENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl9ECHConfigENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIN4bssl9TicketKeyENS1_8internal7DeleterEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrIcN4bssl8internal7DeleterEE5resetB8ne190102EPc
+ __ZNSt3__110unique_ptrIhN4bssl8internal7DeleterEE5resetB8ne190102EPh
+ __ZNSt3__113__fill_n_boolB8ne190102ILb0ENS_8__bitsetILm4ELm256EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS4_9size_typeE
+ __ZNSt3__123__copy_backward_alignedB8ne190102INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
+ __ZNSt3__125__copy_backward_unalignedB8ne190102INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
+ __ZNSt3__16bitsetILm256EElSB8ne190102Em
+ __ZTIN4bssl12SSLPAKEShareE
+ __ZTIN4bssl12_GLOBAL__N_112CipherScorerE
+ __ZTIN4bssl12_GLOBAL__N_116CNsaCipherScorerE
+ __ZTIN4bssl12_GLOBAL__N_117AesHwCipherScorerE
+ __ZTIN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShareE
+ __ZTIN4bssl21RecordNumberEncrypterE
+ __ZTIN4bssl24AESRecordNumberEncrypterE
+ __ZTIN4bssl27AES128RecordNumberEncrypterE
+ __ZTIN4bssl27AES256RecordNumberEncrypterE
+ __ZTIN4bssl27ChaChaRecordNumberEncrypterE
+ __ZTSN4bssl12SSLPAKEShareE
+ __ZTSN4bssl12_GLOBAL__N_112CipherScorerE
+ __ZTSN4bssl12_GLOBAL__N_116CNsaCipherScorerE
+ __ZTSN4bssl12_GLOBAL__N_117AesHwCipherScorerE
+ __ZTSN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShareE
+ __ZTSN4bssl21RecordNumberEncrypterE
+ __ZTSN4bssl24AESRecordNumberEncrypterE
+ __ZTSN4bssl27AES128RecordNumberEncrypterE
+ __ZTSN4bssl27AES256RecordNumberEncrypterE
+ __ZTSN4bssl27ChaChaRecordNumberEncrypterE
+ __ZTVN4bssl12SSLPAKEShareE
+ __ZTVN4bssl12_GLOBAL__N_116CNsaCipherScorerE
+ __ZTVN4bssl12_GLOBAL__N_117AesHwCipherScorerE
+ __ZTVN4bssl12_GLOBAL__N_122X25519MLKEM768KeyShareE
+ __ZTVN4bssl27AES128RecordNumberEncrypterE
+ __ZTVN4bssl27AES256RecordNumberEncrypterE
+ __ZTVN4bssl27ChaChaRecordNumberEncrypterE
+ __ZZN4bssl27tls1_generate_master_secretEPNS_13SSL_HANDSHAKEENS_4SpanIhEENS2_IKhEEE18kMasterSecretLabel
+ __ZZN4bssl27tls1_generate_master_secretEPNS_13SSL_HANDSHAKEENS_4SpanIhEENS2_IKhEEE26kExtendedMasterSecretLabel
+ __ZZN4bsslL17hkdf_expand_labelENS_4SpanIhEEPK9env_md_stNS0_IKhEENS0_IKcEES6_bE18kDTLS13LabelPrefix
+ __ZZN4bsslL28ssl_write_client_cipher_listEPKNS_13SSL_HANDSHAKEEP6cbb_stNS_23ssl_client_hello_type_tEE19kCiphersAESHardware
+ __ZZN4bsslL28ssl_write_client_cipher_listEPKNS_13SSL_HANDSHAKEEP6cbb_stNS_23ssl_client_hello_type_tEE21kCiphersNoAESHardware
+ __ZZN4bsslL28ssl_write_client_cipher_listEPKNS_13SSL_HANDSHAKEEP6cbb_stNS_23ssl_client_hello_type_tEE24kCiphersAESHardwarePQTLS
+ __ZZN4bsslL28ssl_write_client_cipher_listEPKNS_13SSL_HANDSHAKEEP6cbb_stNS_23ssl_client_hello_type_tEE26kCiphersNoAESHardwarePQTLS
+ ___block_descriptor_40_e9_B16?0^v8l
+ ___block_descriptor_48_e8_32s40s_e5_v8?0l
+ ___block_descriptor_52_e9_B16?0^v8lu32l8
+ ___block_descriptor_57_e8_32s40r_e36_B24?0Q8"NSObject<OS_xpc_object>"16l
+ ___boringssl_context_new_session_handler_block_invoke_2
+ __block_literal_global.82
+ __boringssl_context_copy_global_trust_queue_for_qos_block_invoke.197
+ __boringssl_context_evaluate_trust_async_external_block_invoke.212
+ __boringssl_context_evaluate_trust_async_internal_block_invoke.200
+ __boringssl_context_evaluate_trust_async_internal_block_invoke.206
+ __boringssl_context_new_session_handler_block_invoke.262
+ __boringssl_context_start_handshake_timer_block_invoke.26
+ __boringssl_context_update_encryption_level_block_invoke.233
+ __boringssl_context_update_encryption_level_block_invoke.236
+ __boringssl_log_open_block_invoke.cold.1
+ __boringssl_session_apply_protocol_options_for_transport_block_invoke.18
+ __boringssl_session_apply_protocol_options_for_transport_block_invoke.20
+ __boringssl_session_apply_protocol_options_for_transport_block_invoke.20.cold.1
+ __nw_protocol_boringssl_copy_definition_block_invoke.cold.1
+ __nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.4
+ __nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.5
+ _aes_nohw_encrypt
+ _aes_nohw_encrypt_batch
+ _aes_nohw_expand_round_keys
+ _aes_nohw_from_batch
+ _aes_nohw_mix_columns
+ _aes_nohw_rcon
+ _aes_nohw_set_encrypt_key
+ _aes_nohw_sub_block
+ _aes_nohw_sub_bytes
+ _aes_nohw_to_batch
+ _aes_nohw_transpose
+ _boringssl_context_get_ats_non_pfs_ciphersuite_allowed
+ _boringssl_context_set_ats_non_pfs_ciphersuite_allowed
+ _boringssl_helper_dispatch_data_copyout_and_alloc
+ _boringssl_session_get_pqtls_enabled
+ _cchkdf
+ _cckem_decapsulate
+ _cckem_encapsulate
+ _cckem_export_pubkey
+ _cckem_full_ctx_init
+ _cckem_generate_key
+ _cckem_import_pubkey
+ _cckem_kyber768
+ _cckem_pub_ctx_init
+ _cckem_public_ctx
+ _cckem_sizeof_full_ctx
+ _cckem_sizeof_pub_ctx
+ _compute_transcript_and_confirmation_messages
+ _nw_endpoint_create_host_with_numeric_port
+ _nw_path_is_direct
+ _nw_path_is_local
+ _nw_protocol_boringssl_copy_metadata_contents
+ _nw_protocol_boringssl_read_bytes_wrapper
+ _nw_protocol_boringssl_write_bytes_wrapper
+ _nw_protocol_get_input_handler
+ _nw_protocol_get_path
+ _nw_settings_get_pqtls_enabled
+ _objc_msgSend
+ _objc_msgSend$containsString:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$stringWithUTF8String:
+ _sec_identity_copy_SPAKE2PLUSV1_client_identity
+ _sec_identity_copy_SPAKE2PLUSV1_client_password_verifier
+ _sec_identity_copy_SPAKE2PLUSV1_context
+ _sec_identity_copy_SPAKE2PLUSV1_registration_record
+ _sec_identity_copy_SPAKE2PLUSV1_server_identity
+ _sec_identity_copy_SPAKE2PLUSV1_server_password_verifier
+ _sec_identity_copy_type
+ _sec_protocol_configuration_copy_transformed_options_for_address
+ _sec_protocol_configuration_copy_transformed_options_for_host
+ aes_nohw_from_batch.cold.1
+ aes_nohw_to_batch.cold.1
+ boringssl_config_get_tls13_external_psk_enabled.cold.1
+ boringssl_config_get_whitelisted_bundle_identifier.cold.1
+ boringssl_context_info_handler.cold.1
+ boringssl_context_set_identity.cold.1
+ boringssl_context_set_identity.cold.2
+ boringssl_log_open.cold.1
+ boringssl_metrics_log_connection.cold.1
+ boringssl_metrics_log_connection_failure.cold.1
+ boringssl_metrics_log_ech.cold.1
+ boringssl_session_disconnect.cold.1
+ boringssl_session_disconnect.cold.2
+ boringssl_session_set_state.cold.1
+ nw_boringssl_read.cold.2
+ nw_protocol_boringssl_begin_connection.cold.12
+ nw_protocol_boringssl_connected.cold.4
+ nw_protocol_boringssl_connected.cold.5
+ nw_protocol_boringssl_copy_definition.cold.1
+ nw_protocol_boringssl_disconnect.cold.2
+ nw_protocol_boringssl_disconnect.cold.3
+ nw_protocol_boringssl_disconnect.cold.4
+ nw_protocol_boringssl_error.cold.2
+ nw_protocol_boringssl_error.cold.3
+ nw_protocol_boringssl_error.cold.4
+ nw_protocol_boringssl_get_input_frames.cold.3
+ nw_protocol_boringssl_get_output_frames.cold.7
+ nw_protocol_boringssl_handshake_negotiate.cold.3
+ nw_protocol_boringssl_handshake_negotiate.cold.4
+ nw_protocol_boringssl_handshake_negotiate.cold.5
+ nw_protocol_boringssl_identifier.cold.1
+ nw_protocol_boringssl_input_finished.cold.3
+ nw_protocol_boringssl_write_frames.cold.4
- BORINGSSL_keccak_absorb.cold.1
- GCC_except_table121
- GCC_except_table127
- GCC_except_table149
- GCC_except_table154
- GCC_except_table156
- GCC_except_table158
- GCC_except_table160
- GCC_except_table163
- GCC_except_table23
- GCC_except_table352
- GCC_except_table353
- GCC_except_table357
- GCC_except_table358
- GCC_except_table364
- GCC_except_table366
- GCC_except_table371
- GCC_except_table63
- GCC_except_table78
- GCC_except_table93
- GCC_except_table97
- _BORINGSSL_keccak
- _BORINGSSL_keccak_absorb
- _BORINGSSL_keccak_init
- _BORINGSSL_keccak_squeeze
- _KYBER_encap_external_entropy
- _KYBER_generate_key_external_entropy
- _RAND_bytes_with_additional_data
- _ZN4bssl16dtls_seal_recordEP6ssl_stPhPmmhPKhmNS_17dtls1_use_epoch_tE.cold.1
- _ZN4bssl16dtls_seal_recordEP6ssl_stPhPmmhPKhmNS_17dtls1_use_epoch_tE.cold.2
- _ZN4bssl18dtls1_write_recordEP6ssl_stiNS_4SpanIKhEENS_17dtls1_use_epoch_tE.cold.1
- _ZN4bssl18dtls1_write_recordEP6ssl_stiNS_4SpanIKhEENS_17dtls1_use_epoch_tE.cold.2
- _ZN4bssl22tls13_server_handshakeEPNS_13SSL_HANDSHAKEE.cold.3
- _ZN4bsslL12add_outgoingEP6ssl_stbNS_5ArrayIhEE.cold.1
- _ZN4bsslL14get_write_aeadEPK6ssl_stNS_17dtls1_use_epoch_tE.cold.1
- _ZN4bsslL24ext_ri_parse_serverhelloEPNS_13SSL_HANDSHAKEEPhP6cbs_st.cold.3
- _ZN4bsslL24ext_ri_parse_serverhelloEPNS_13SSL_HANDSHAKEEPhP6cbs_st.cold.4
- _ZN4bsslL26ssl_decrypt_ticket_with_cbEPNS_13SSL_HANDSHAKEEPNS_5ArrayIhEEPbNS_4SpanIKhEE.cold.1
- _ZNK4bssl14SSLAEADContext13RecordVersionEv.cold.1
- _ZNK4bssl14SSLAEADContext15ProtocolVersionEv.cold.1
- __ZN4bssl13GrowableArrayINS_18CertCompressionAlgEE9MaybeGrowEv
- __ZN4bssl13GrowableArrayINSt3__110unique_ptrI17ssl_credential_stNS_8internal7DeleterEEEE4PushES6_
- __ZN4bssl13GrowableArrayINSt3__110unique_ptrI17ssl_credential_stNS_8internal7DeleterEEEE9MaybeGrowEv
- __ZN4bssl13SSLTranscriptC1Ev
- __ZN4bssl13SSLTranscriptC2Ev
- __ZN4bssl13SSL_HANDSHAKE13ResizeSecretsEm
- __ZN4bssl14SSLAEADContext16CreateNullCipherEb
- __ZN4bssl14SSLAEADContext22SetVersionIfNullCipherEt
- __ZN4bssl14SSLAEADContext24CreatePlaceholderForQUICEtPK13ssl_cipher_st
- __ZN4bssl14SSLAEADContext4SealEPhPmmhtyNS_4SpanIKhEEPS4_m
- __ZN4bssl14SSLAEADContext6CreateE20evp_aead_direction_ttbPK13ssl_cipher_stNS_4SpanIKhEES7_S7_
- __ZN4bssl16dtls_seal_recordEP6ssl_stPhPmmhPKhmNS_17dtls1_use_epoch_tE
- __ZN4bssl18dtls1_write_recordEP6ssl_stiNS_4SpanIKhEENS_17dtls1_use_epoch_tE
- __ZN4bssl20dtls_seal_prefix_lenEPK6ssl_stNS_17dtls1_use_epoch_tE
- __ZN4bssl22dtls_max_seal_overheadEPK6ssl_stNS_17dtls1_use_epoch_tE
- __ZN4bssl22ssl_add_client_CA_listEPNS_13SSL_HANDSHAKEEP6cbb_st
- __ZN4bssl23ssl_cipher_get_evp_aeadEPPK11evp_aead_stPmS4_PK13ssl_cipher_sttb
- __ZN4bssl23tls12_check_peer_sigalgEPKNS_13SSL_HANDSHAKEEPht
- __ZN4bssl24ssl_parse_client_CA_listEP6ssl_stPhP6cbs_st
- __ZN4bssl24tls13_derive_session_pskEP14ssl_session_stNS_4SpanIKhEE
- __ZN4bssl25ssl_seal_align_prefix_lenEPK6ssl_st
- __ZN4bssl27ssl_pkey_supports_algorithmEPK6ssl_stP11evp_pkey_stt
- __ZN4bssl27tls1_generate_master_secretEPNS_13SSL_HANDSHAKEEPhNS_4SpanIKhEE
- __ZN4bssl3NewINS_14SSLAEADContextEJRtRbRPK13ssl_cipher_stEEEPT_DpOT0_
- __ZN4bssl3NewINS_14SSLAEADContextEJRtbRPK13ssl_cipher_stEEEPT_DpOT0_
- __ZN4bssl3NewINS_14SSLAEADContextEJiRbDnEEEPT_DpOT0_
- __ZN4bssl5ArrayINS_10ALPSConfigEE5ResetEPS1_m
- __ZN4bssl5ArrayINS_10ALPSConfigEED2Ev
- __ZN4bssl5ArrayINS_18CertCompressionAlgEE4InitEm
- __ZN4bssl5ArrayINS_18CertCompressionAlgEED2Ev
- __ZN4bssl5ArrayINSt3__110unique_ptrI17ssl_credential_stNS_8internal7DeleterEEEE4InitEm
- __ZN4bssl5ArrayINSt3__110unique_ptrI17ssl_credential_stNS_8internal7DeleterEEEE5ResetEPS6_m
- __ZN4bssl5ArrayINSt3__110unique_ptrI17ssl_credential_stNS_8internal7DeleterEEEED2Ev
- __ZN4bssl5ArrayINSt3__110unique_ptrINS_15ECHServerConfigENS_8internal7DeleterEEEE5ResetEPS6_m
- __ZN4bssl5ArrayINSt3__110unique_ptrINS_15ECHServerConfigENS_8internal7DeleterEEEED2Ev
- __ZN4bssl5ArrayIP17ssl_credential_stE4InitEm
- __ZN4bssl5ArrayIbE4InitEm
- __ZN4bssl5ArrayIhE4InitEm
- __ZN4bssl5ArrayIiE4InitEm
- __ZN4bssl5ArrayItE4InitEm
- __ZN4bssl6DeleteINS_14SSLAEADContextEEEvPT_
- __ZN4bsslL14get_write_aeadEPK6ssl_stNS_17dtls1_use_epoch_tE
- __ZN4bsslL16tls13_psk_binderEPhPmPK14ssl_session_stRKNS_13SSLTranscriptENS_4SpanIKhEEmb
- __ZN4bsslL17tls13_verify_dataEPhPmPK9env_md_sttNS_4SpanIKhEES7_
- __ZN4bsslL26ssl_decrypt_ticket_with_cbEPNS_13SSL_HANDSHAKEEPNS_5ArrayIhEEPbNS_4SpanIKhEE
- __ZN4bsslL26ssl_needs_record_splittingEPK6ssl_st
- __ZN4bsslL29derive_secret_with_transcriptEPKNS_13SSL_HANDSHAKEENS_4SpanIhEERKNS_13SSLTranscriptENS3_IKcEE
- __ZN4bsslL38SSL_SESSION_parse_bounded_octet_stringEP6cbs_stPhS2_hj
- __ZNK4bssl14SSLAEADContext13RecordVersionEv
- __ZNK4bssl14SSLAEADContext15ProtocolVersionEv
- __ZNSt3__110unique_ptrI10buf_mem_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI10ssl_ctx_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI11ec_point_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI11evp_pkey_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI12ecdsa_sig_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI14ssl_session_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI15ssl_ech_keys_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI16crypto_buffer_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI17err_save_state_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI17ssl_credential_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI19stack_st_SSL_CIPHERN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI22stack_st_CRYPTO_BUFFERN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI32stack_st_SRTP_PROTECTION_PROFILEN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI6bio_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI6ssl_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI9bignum_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI9ec_key_stN4bssl8internal7DeleterEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrIN4bssl10SSL3_STATEENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl10SSL_CONFIGENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl11DTLS1_STATEENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl11SSLKeyShareENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl11hm_fragmentENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl12_GLOBAL__N_110ECKeyShareENS1_8internal7DeleterEED1B8ne180100Ev
- __ZNSt3__110unique_ptrIN4bssl13SSL_HANDSHAKEENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl14SSLAEADContextENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl15ECHServerConfigENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl19SSL_HANDSHAKE_HINTSENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl23SSLCipherPreferenceListENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl4CERTENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl9ECHConfigENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIN4bssl9TicketKeyENS1_8internal7DeleterEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrIcN4bssl8internal7DeleterEE5resetB8ne180100EPc
- __ZNSt3__110unique_ptrIhN4bssl8internal7DeleterEE5resetB8ne180100EPh
- __ZNSt3__123__copy_backward_alignedB8ne180100INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
- __ZNSt3__125__copy_backward_unalignedB8ne180100INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
- __ZNSt3__16bitsetILm256EElSB8ne180100Em
- __ZNSt3__18__fill_nB8ne180100ILb0ENS_8__bitsetILm4ELm256EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS4_9size_typeE
- __ZZN4bssl27tls1_generate_master_secretEPNS_13SSL_HANDSHAKEEPhNS_4SpanIKhEEE18kMasterSecretLabel
- __ZZN4bssl27tls1_generate_master_secretEPNS_13SSL_HANDSHAKEEPhNS_4SpanIKhEEE26kExtendedMasterSecretLabel
- ___block_descriptor_60_e8_32s_e9_B16?0^v8lu48l8
- __block_literal_global.78
- __boringssl_context_copy_global_trust_queue_for_qos_block_invoke.195
- __boringssl_context_evaluate_trust_async_external_block_invoke.210
- __boringssl_context_evaluate_trust_async_internal_block_invoke.198
- __boringssl_context_evaluate_trust_async_internal_block_invoke.204
- __boringssl_context_start_handshake_timer_block_invoke.24
- __boringssl_context_update_encryption_level_block_invoke.231
- __boringssl_context_update_encryption_level_block_invoke.234
- __boringssl_session_apply_protocol_options_for_transport_block_invoke.14
- __boringssl_session_apply_protocol_options_for_transport_block_invoke.16
- __boringssl_session_apply_protocol_options_for_transport_block_invoke.16.cold.1
- _do_library_init
- _encrypt_cpa
- _kInverseNTTRoots
- _kMasks
- _kModRoots
- _kNTTRoots
- _keccak_f
- _keccak_init
- _kyber_marshal_public_key
- _kyber_parse_public_key_no_hash
- _matrix_expand
- _once
- _reduce
- _reduce_once
- _scalar_centered_binomial_distribution_eta_2_with_prf
- _scalar_compress
- _scalar_decode
- _scalar_encode
- _scalar_inner_product
- _scalar_inverse_ntt
- _scalar_mult
- _vector_ntt
- keccak_f.kRoundConstants
- matrix_expand.cold.1
- matrix_expand.cold.2
- reduce.cold.1
- reduce_once.cold.1
- scalar_compress.cold.1
CStrings:
+ "!buffers_alias(out, in_len, in, in_len) || in == out"
+ "!hs->received_hello_verify_request"
+ "%{public}s(%d) %{public}s[%p] Invalid sec_identity provided (SEC_PROTOCOL_IDENTITY_TYPE_INVALID)"
+ "%{public}s(%d) %{public}s[%p] SSL_shutdown returned. Disconnect successful? %@"
+ "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) ech(%{bool}d) pqtls(%{bool}d)]"
+ "%{public}s(%d) %{public}s[%p] Unsupported sec_identity provided (%d)"
+ "%{public}s(%d) %{public}s[%p] boringssl session state changed from %s to %s"
+ "%{public}s(%d) %{public}s[%p] calling SSL_shutdown."
+ "%{public}s(%d) %{public}s[%p] secret_len: %zu, identity_len: %zu"
+ "%{public}s(%d) KYBER_private_key not initialized"
+ "%{public}s(%d) KYBER_public_key not initialized"
+ "%{public}s(%d) MLKEM768_private_key not initialized"
+ "%{public}s(%d) MLKEM768_public_key not initialized"
+ "%{public}s(%d) cckem_decapsulate failed"
+ "%{public}s(%d) cckem_encapsulate failed"
+ "%{public}s(%d) cckem_export_pubkey failed"
+ "."
+ ".local"
+ ".local."
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio_mem.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/file.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/buf/buf.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bytestring/cbb.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/cipher_extra/e_tls.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/dsa/dsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_ctx.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ex_data.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/add.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/bn.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/ctx.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/div.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/mul.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/prime.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/random.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/shift.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/aead.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digest/digest.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/felem.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/oct.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p256.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/scalar.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/simple.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/rsa/padding.c.inc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/hpke/hpke.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/mem.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/stack/stack.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_both.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_lib.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_pkt.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_method.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_record.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/encrypted_client_hello.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/extensions.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_client.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_server.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/internal.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_both.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_pkt.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_aead_ctx.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_asn1.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_buffer.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cert.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cipher.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_credential.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_key_share.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_lib.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_privkey.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_session.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_transcript.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_versions.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/t1_enc.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_both.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_client.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_enc.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_server.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_method.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_record.cc"
+ "BN_div"
+ "CRYPTO_chacha_20"
+ "ConfirmationKeys"
+ "DTLSv1.3"
+ "KYBER_decap"
+ "KYBER_encap"
+ "KYBER_generate_key"
+ "KYBER_parse_public_key"
+ "MLKEM768_decap"
+ "MLKEM768_encap"
+ "MLKEM768_generate_key"
+ "MLKEM768_parse_public_key"
+ "SharedKey"
+ "X25519MLKEM768"
+ "aead.c.inc"
+ "aes_nohw.c.inc"
+ "aes_nohw_from_batch"
+ "aes_nohw_to_batch"
+ "ats_non_pfs_ciphersuite_allowed"
+ "began nw_protocol_boringssl_disconnect: boringssl session state is: %s"
+ "bn.c.inc"
+ "boringssl called disconnect down the stack"
+ "boringssl_context_set_ats_non_pfs_ciphersuite_allowed"
+ "boringssl_context_set_identity"
+ "boringssl_session_disconnect"
+ "boringssl_session_set_state"
+ "bytes.c.inc"
+ "chacha.c"
+ "cipher->algorithm_enc & (SSL_AES128GCM | SSL_AES256GCM)"
+ "cipher.c.inc"
+ "containsString:"
+ "ctx.c.inc"
+ "d0 & (((BN_ULONG)1) << (BN_BITS2 - 1))"
+ "digest.c.inc"
+ "digest_len == hs->new_session->original_handshake_hash.size()"
+ "div.c.inc"
+ "div_extra.c.inc"
+ "ec.c.inc"
+ "ec_key.c.inc"
+ "exponentiation.c.inc"
+ "felem.c.inc"
+ "handle_hello_verify_request"
+ "hasSuffix:"
+ "kdf.c.inc"
+ "len == hs->secret.size()"
+ "montgomery_inv.c.inc"
+ "msg.type == DTLS1_MT_HELLO_VERIFY_REQUEST"
+ "mul.c.inc"
+ "n0 < d0"
+ "nonce_len == fixed_nonce_.size()"
+ "nope"
+ "num_blocks <= AES_NOHW_BATCH_SIZE"
+ "nw_protocol_boringssl_disconnect has been called re-entrantly and will call boringssl_session_disconnect a second time."
+ "oct.c.inc"
+ "p224-64.c.inc"
+ "p256.c.inc"
+ "padding.c.inc"
+ "pqtls_enabled"
+ "prime.c.inc"
+ "random.c.inc"
+ "seal_next_message"
+ "session->secret.size() == EVP_MD_size(digest)"
+ "sha256.c.inc"
+ "sha512.c.inc"
+ "sn"
+ "ssl->d1->outgoing_written < ssl->d1->outgoing_messages.size()"
+ "ssl->s3->initial_handshake_complete == !ssl->s3->previous_client_finished.empty()"
+ "ssl->s3->previous_client_finished.size() == ssl->s3->previous_server_finished.size()"
+ "ssl->s3->version != 0"
+ "ssl->s3->version == 0"
+ "ssl->s3->version == 0 || (hs->early_data_offered && ssl->s3->version == hs->early_session->ssl_version)"
+ "ssl_protocol_version(ssl) < TLS1_3_VERSION"
+ "ssl_record_prefix_len"
+ "ssl_session_protocol_version(hs->early_session.get()) >= TLS1_3_VERSION"
+ "stringWithUTF8String:"
+ "tls13_derive_session_psk"
+ "tls1_record_handshake_hashes_for_channel_id"
+ "wnaf.c.inc"
+ "yes"
- "!expected_len || ssl->s3->previous_client_finished_len"
- "!expected_len || ssl->s3->previous_server_finished_len"
- "!ssl->s3->have_version"
- "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ech(%{bool}d)]"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/bio_mem.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bio/file.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/buf/buf.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/bytestring/cbb.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/cipher_extra/e_tls.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/dsa/dsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/evp_ctx.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ec_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/ex_data.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/add.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/bn.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/ctx.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/div.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/mul.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/prime.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/random.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/shift.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/aead.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digest/digest.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/felem.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/oct.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p256.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/scalar.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/simple.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/rsa/padding.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/hpke/hpke.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/mem.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/stack/stack.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_both.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_lib.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/d1_pkt.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_method.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/dtls_record.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/encrypted_client_hello.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/extensions.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_client.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/handshake_server.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/internal.h"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_both.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/s3_pkt.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_aead_ctx.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_asn1.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_buffer.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cert.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_cipher.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_credential.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_key_share.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_lib.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_privkey.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_session.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_transcript.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_versions.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/t1_enc.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_both.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_client.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_enc.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls13_server.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_method.cc"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/tls_record.cc"
- "0 `"
- "BORINGSSL_keccak_absorb"
- "CBS_len(&server_hello.session_id) <= SSL3_SESSION_ID_SIZE"
- "ProtocolVersion"
- "RecordVersion"
- "TLS client read_hello_verify_request"
- "aead.c"
- "aead_ctx->ProtocolVersion() == protocol_version"
- "bn.c"
- "bytes.c"
- "cipher.c"
- "ciphertext_len == len_copy"
- "compress"
- "ctx->absorb_offset < ctx->rate_bytes"
- "ctx.c"
- "digest.c"
- "div.c"
- "div_extra.c"
- "do_read_hello_verify_request"
- "dtls_record.cc"
- "dtls_seal_record"
- "ec.c"
- "ec_key.c"
- "exponentiation.c"
- "felem.c"
- "fixed_iv.size() <= sizeof(aead_ctx->fixed_nonce_)"
- "get_write_aead"
- "hs->expected_client_finished().size() <= 0xff"
- "hs->max_version < TLS1_3_VERSION"
- "hs->session_id_len <= sizeof(hs->session_id)"
- "is_null_cipher()"
- "kdf.c"
- "keccak.c"
- "keccak_ctx->rate_bytes == 168"
- "keccak_ctx->squeeze_offset == 0"
- "kyber.c"
- "len == hs->secret().size()"
- "montgomery_inv.c"
- "mul.c"
- "nonce_len == fixed_nonce_len_"
- "oct.c"
- "p224-64.c"
- "p256.c"
- "padding.c"
- "prime.c"
- "random.c"
- "reduce"
- "reduce_once"
- "remainder < 2u * kPrime"
- "scalar_from_keccak_vartime"
- "sha256.c"
- "sha512.c"
- "ssl->d1->w_epoch >= 1"
- "ssl->s3->have_version"
- "ssl->s3->have_version == ssl->s3->initial_handshake_complete"
- "ssl->s3->initial_handshake_complete == (ssl->s3->previous_client_finished_len != 0)"
- "ssl->s3->initial_handshake_complete == (ssl->s3->previous_server_finished_len != 0)"
- "wnaf.c"
- "x < 2 * kPrime"
- "x < kPrime + 2u * kPrime * kPrime"

```
