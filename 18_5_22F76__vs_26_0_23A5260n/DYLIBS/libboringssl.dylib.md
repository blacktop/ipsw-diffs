## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.122.1.0.0
-  __TEXT.__text: 0x9e220
-  __TEXT.__auth_stubs: 0x1970
+532.0.7.0.0
+  __TEXT.__text: 0x9f9d8
+  __TEXT.__auth_stubs: 0x1e20
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x10630
+  __TEXT.__cstring: 0x106bd
   __TEXT.__const: 0xfef8
-  __TEXT.__oslogstring: 0x577e
-  __TEXT.__gcc_except_tab: 0x28e8
-  __TEXT.__unwind_info: 0x2480
+  __TEXT.__oslogstring: 0x5be2
+  __TEXT.__gcc_except_tab: 0x2940
+  __TEXT.__unwind_info: 0x2488
   __TEXT.__eh_frame: 0x130
-  __TEXT.__objc_classname: 0x241
-  __TEXT.__objc_methname: 0xe76
-  __TEXT.__objc_methtype: 0x6f7
-  __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_classname: 0x240
+  __TEXT.__objc_methname: 0xe4d
+  __TEXT.__objc_methtype: 0x62b
+  __TEXT.__objc_stubs: 0xa0
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0xb890
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xcd0
+  __DATA_CONST.__objc_selrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0xf28
   __AUTH_CONST.__const: 0x18c8
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x2168
+  __AUTH_CONST.__objc_const: 0x20e8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x300
+  __DATA.__objc_ivar: 0x2f0
   __DATA.__data: 0xd00
-  __DATA.__bss: 0x550
+  __DATA.__bss: 0x548
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x210
-  __DATA_DIRTY.__bss: 0xdb0
+  __DATA_DIRTY.__bss: 0xcb0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 45A1A5D3-6A8C-32EF-975C-8A78A9D90076
-  Functions: 3121
-  Symbols:   7324
-  CStrings:  3624
+  UUID: D9D192BE-BC14-3DCE-9FE3-F05AC28B62BE
+  Functions: 3129
+  Symbols:   7396
+  CStrings:  3638
 
Symbols:
+ -[boringssl_concrete_nw_protocol_boringssl destroy]
+ GCC_except_table101
+ GCC_except_table151
+ GCC_except_table160
+ GCC_except_table179
+ GCC_except_table357
+ GCC_except_table360
+ GCC_except_table363
+ GCC_except_table369
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table76
+ GCC_except_table93
+ _MLKEM768_public_key_free
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_SecSessionInfo
+ _OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.internal_reference
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _SSL_SESSION_get0_ticket
+ _SSL_SESSION_get_ticket_age_add
+ _SSL_SESSION_get_time
+ _SSL_SESSION_get_timeout
+ _SecTrustSetExceptions
+ __ZN4bssl6VectorINS_10ALPSConfigEED1Ev
+ __ZNSt3__110unique_ptrI10buf_mem_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI10ssl_ctx_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI11ec_point_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI11evp_pkey_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI12ecdsa_sig_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI14ssl_session_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI15ssl_ech_keys_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI16crypto_buffer_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI17err_save_state_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI17spake2plus_ctx_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI17ssl_credential_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI19stack_st_SSL_CIPHERN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI22stack_st_CRYPTO_BUFFERN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI32stack_st_SRTP_PROTECTION_PROFILEN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI6bio_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI6ssl_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI9bignum_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI9ec_key_stN4bssl8internal7DeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrIN4bssl10SSL3_STATEENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl10SSL_CONFIGENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11DTLS1_STATEENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11SSLKeyShareENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11hm_fragmentENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl12SSLPAKEShareENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl12_GLOBAL__N_110ECKeyShareENS1_8internal7DeleterEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN4bssl13SSL_HANDSHAKEENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl14DTLSEpochStateENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl14SSLAEADContextENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl15ECHServerConfigENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl19SSL_HANDSHAKE_HINTSENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl21RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl23SSLCipherPreferenceListENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27AES128RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27AES256RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27ChaChaRecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl4CERTENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl9ECHConfigENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl9TicketKeyENS1_8internal7DeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIcN4bssl8internal7DeleterEE5resetB8ne200100EPc
+ __ZNSt3__110unique_ptrIhN4bssl8internal7DeleterEE5resetB8ne200100EPh
+ __ZNSt3__113__fill_n_boolB8ne200100ILb0ENS_8__bitsetILm4ELm256EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS_29__size_difference_type_traitsIS4_vE9size_typeE
+ __ZNSt3__123__copy_backward_alignedB8ne200100INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
+ __ZNSt3__125__copy_backward_unalignedB8ne200100INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
+ __ZNSt3__16bitsetILm256EElSB8ne200100Em
+ ___block_descriptor_76_e9_B16?0^v8lu56l8
+ ___block_literal_global.129
+ ___block_literal_global.142
+ ___block_literal_global.257
+ ___boringssl_context_evaluate_trust_async_external_block_invoke.202
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.194
+ ___boringssl_context_new_session_handler_block_invoke.234
+ ___boringssl_context_update_encryption_level_block_invoke.212
+ ___boringssl_context_update_encryption_level_block_invoke.214
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.17
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.19
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.19.cold.1
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.22
+ ___nw_protocol_boringssl_begin_connection_block_invoke.146
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.136
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.1
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.2
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.3
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.4
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.5
+ ___nw_protocol_boringssl_write_frames_block_invoke.132
+ ___nw_protocol_boringssl_write_frames_block_invoke.132.cold.1
+ _boringssl_config_get_pqtls_fallback_enabled_for_endpoint
+ _boringssl_context_set_encryption_secrets.cold.1
+ _boringssl_session_export_session_info
+ _boringssl_session_get_negotiated_pake
+ _boringssl_session_set_session_state.cold.4
+ _nw_frame_copy_external_data
+ _nw_protocol_boringssl_error.cold.5
+ _nw_protocol_boringssl_error.cold.6
+ _nw_protocol_boringssl_initiate_pqtls_fallback
+ _nw_protocol_boringssl_initiate_pqtls_fallback.cold.1
+ _nw_protocol_callbacks_set_add_input_handler
+ _nw_protocol_callbacks_set_connect
+ _nw_protocol_callbacks_set_connected
+ _nw_protocol_callbacks_set_copy_info
+ _nw_protocol_callbacks_set_disconnect
+ _nw_protocol_callbacks_set_error
+ _nw_protocol_callbacks_set_finalize_output_frames
+ _nw_protocol_callbacks_set_get_input_frames
+ _nw_protocol_callbacks_set_get_output_frames
+ _nw_protocol_callbacks_set_input_available
+ _nw_protocol_callbacks_set_input_finished
+ _nw_protocol_callbacks_set_output_available
+ _nw_protocol_callbacks_set_output_finished
+ _nw_protocol_callbacks_set_remove_input_handler
+ _nw_protocol_callbacks_set_replace_input_handler
+ _nw_protocol_callbacks_set_reset
+ _nw_protocol_callbacks_set_waiting_for_output
+ _nw_protocol_connect
+ _nw_protocol_connect_is_valid
+ _nw_protocol_connected
+ _nw_protocol_connected_is_valid
+ _nw_protocol_copy_info
+ _nw_protocol_copy_info_is_valid
+ _nw_protocol_destroy
+ _nw_protocol_disconnect
+ _nw_protocol_disconnect_is_valid
+ _nw_protocol_disconnected
+ _nw_protocol_disconnected_is_valid
+ _nw_protocol_downcast
+ _nw_protocol_error
+ _nw_protocol_error_is_valid
+ _nw_protocol_finalize_output_frames
+ _nw_protocol_finalize_output_frames_is_valid
+ _nw_protocol_get_flow_id
+ _nw_protocol_get_input_frames
+ _nw_protocol_get_input_frames_is_valid
+ _nw_protocol_get_local_endpoint
+ _nw_protocol_get_local_endpoint_is_valid
+ _nw_protocol_get_message_properties
+ _nw_protocol_get_message_properties_is_valid
+ _nw_protocol_get_name
+ _nw_protocol_get_output_frames
+ _nw_protocol_get_output_frames_is_valid
+ _nw_protocol_get_output_handler
+ _nw_protocol_get_parameters
+ _nw_protocol_get_parameters_is_valid
+ _nw_protocol_get_remote_endpoint
+ _nw_protocol_input_available
+ _nw_protocol_input_available_is_valid
+ _nw_protocol_input_finished
+ _nw_protocol_input_finished_is_valid
+ _nw_protocol_new_objc
+ _nw_protocol_notify
+ _nw_protocol_one_to_one_callbacks_new
+ _nw_protocol_output_available
+ _nw_protocol_register_extended
+ _nw_protocol_remove_input_handler
+ _nw_protocol_remove_input_handler_is_valid
+ _nw_protocol_reset
+ _nw_protocol_reset_is_valid
+ _nw_protocol_set_flow_id
+ _nw_protocol_set_input_handler
+ _nw_protocol_set_output_handler
+ _nw_protocol_supports_external_data
+ _nw_protocol_supports_external_data_is_valid
+ _nw_protocol_upcast
+ _nw_protocol_waiting_for_output
+ _nw_protocol_waiting_for_output_is_valid
+ _nw_settings_get_pqtls_fallback_allowed_for_endpoint
+ _objc_alloc
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$initWithPSK:::::
+ _objc_opt_class
+ _sec_protocol_options_get_default_max_dtls_protocol_version
+ _sec_protocol_options_get_default_max_tls_protocol_version
+ _sec_protocol_options_get_default_min_dtls_protocol_version
+ _sec_protocol_options_get_default_min_tls_protocol_version
+ _sec_protocol_options_set_pqtls_mode
- -[boringssl_concrete_nw_protocol_boringssl dealloc]
- GCC_except_table100
- GCC_except_table150
- GCC_except_table176
- GCC_except_table355
- GCC_except_table359
- GCC_except_table361
- GCC_except_table368
- GCC_except_table370
- GCC_except_table64
- GCC_except_table67
- GCC_except_table91
- OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.max_allowed_dtls_version
- OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.max_allowed_tls_version
- OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.protocol
- _EVP_MD_CTX_new
- _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.min_allowed_dtls_version
- _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.min_allowed_tls_version
- __ZN4bssl6DeleteINS_15ECHServerConfigEEEvPT_
- __ZN4bssl6DeleteINS_19SSL_HANDSHAKE_HINTSEEEvPT_
- __ZN4bssl6VectorINS_10ALPSConfigEED2Ev
- __ZNSt3__110unique_ptrI10buf_mem_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI10ssl_ctx_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI11ec_point_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI11evp_pkey_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI12ecdsa_sig_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI14ssl_session_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI15ssl_ech_keys_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI16crypto_buffer_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI17err_save_state_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI17ssl_credential_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI19stack_st_SSL_CIPHERN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI22stack_st_CRYPTO_BUFFERN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI32stack_st_SRTP_PROTECTION_PROFILEN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI6bio_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI6ssl_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI9bignum_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI9ec_key_stN4bssl8internal7DeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrIN4bssl10SSL3_STATEENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl10SSL_CONFIGENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl11DTLS1_STATEENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl11SSLKeyShareENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl11hm_fragmentENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl12SSLPAKEShareENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl12_GLOBAL__N_110ECKeyShareENS1_8internal7DeleterEED1B8ne190102Ev
- __ZNSt3__110unique_ptrIN4bssl13SSL_HANDSHAKEENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl14DTLSEpochStateENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl14SSLAEADContextENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl15ECHServerConfigENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl19SSL_HANDSHAKE_HINTSENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl21RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl23SSLCipherPreferenceListENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl27AES128RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl27AES256RecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl27ChaChaRecordNumberEncrypterENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl4CERTENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl9ECHConfigENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN4bssl9TicketKeyENS1_8internal7DeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIcN4bssl8internal7DeleterEE5resetB8ne190102EPc
- __ZNSt3__110unique_ptrIhN4bssl8internal7DeleterEE5resetB8ne190102EPh
- __ZNSt3__113__fill_n_boolB8ne190102ILb0ENS_8__bitsetILm4ELm256EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS4_9size_typeE
- __ZNSt3__123__copy_backward_alignedB8ne190102INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
- __ZNSt3__125__copy_backward_unalignedB8ne190102INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
- __ZNSt3__16bitsetILm256EElSB8ne190102Em
- ___block_descriptor_60_e9_B16?0^v8l
- ___block_literal_global.130
- ___block_literal_global.143
- ___block_literal_global.256
- ___boringssl_context_evaluate_trust_async_external_block_invoke.206
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.202
- ___boringssl_context_new_session_handler_block_invoke.238
- ___boringssl_context_update_encryption_level_block_invoke.216
- ___boringssl_context_update_encryption_level_block_invoke.218
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.16
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.18
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.18.cold.1
- ___nw_protocol_boringssl_begin_connection_block_invoke.147
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.1
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.2
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.3
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.4
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.5
- ___nw_protocol_boringssl_write_frames_block_invoke.133
- ___nw_protocol_boringssl_write_frames_block_invoke.133.cold.1
- _bn_mont_ctx_init
- _boringssl_config_get_max_dtls_version_allowed
- _boringssl_config_get_max_tls_version_allowed
- _boringssl_config_get_min_dtls_version_allowed
- _boringssl_config_get_min_tls_version_allowed
- _ge_p2_0
- _ge_p3_0
- _ge_p3_to_p2
- _nw_frame_get_external_data
- _nw_protocol_register
- _nw_protocol_set_default_one_to_one_callbacks
CStrings:
+ "%{public}s(%d) %{public}s[%p] Error not propagated up the stack"
+ "%{public}s(%d) %{public}s[%p] PQ-TLS fallback initiated; shortcircuiting the error propagation up the stack"
+ "%{public}s(%d) %{public}s[%p] Propagating error up the stack"
+ "%{public}s(%d) %{public}s[%p] SSL_SESSION for resumption has ciphersuite: %s (id: %u)"
+ "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) ech(%{bool}d) pqtls(%{bool}d), pake(%{bool}d)]"
+ "%{public}s(%d) %{public}s[%p] TLS connected [server(%d) version(0x%04x) ciphersuite(%s) group(0x%04x) signature_alg(0x%04x) alpn(%{public}s) resumed(%d) offered_ticket(%d) in_early_data(%d) early_data_accepted(%d) false_started(%d) ocsp_received(%d) sct_received(%d) connect_time(%llums) flight_time(%llums) rtt(%llums) write_stalls(%zu) read_stalls(%zu) pake(0x%04x)]"
+ "%{public}s(%d) %{public}s[%p] currently in early data? %s, early data accepted? %s"
+ "%{public}s(%d) %{public}s[%p] nw_protocol_connected_is_valid failed"
+ "%{public}s(%d) %{public}s[%p] nw_protocol_get_input_frames(%s) is not valid"
+ "%{public}s(%d) %{public}s[%p] nw_protocol_get_output_frames(%s) is not valid"
+ "%{public}s(%d) %{public}s[%p] nw_protocol_supports_external_data(%s) is not valid"
+ "%{public}s(%d) %{public}s[%p] updating read secret. Level: %u, secret_data_length: %zu urrently negotiated ciphersuite: %u"
+ "%{public}s(%d) %{public}s[%p] updating write secret. Level: %u, secret_data_length: %zu, currently negotiated ciphersuite: %u"
+ "%{public}s(%d) Initiating PQ-TLS fallback"
+ "%{public}s(%d) PQ-TLS disabled; skipping fallback path"
+ "%{public}s(%d) PQ-TLS fallback disallowed for endpoint; skipping PQ-TLS fallback"
+ "%{public}s(%d) input protocol is NULL; skipping PQ-TLS fallback"
+ "%{public}s(%d) no TLS options; skipping PQ-TLS fallback"
+ "%{public}s(%d) no parameters; skipping PQ-TLS fallback"
+ "%{public}s(%d) no remote endpoint; skipping PQ-TLS fallback"
+ "boringssl_context_set_encryption_secrets"
+ "boringssl_context_set_encryption_secrets_block_invoke"
+ "dataWithBytes:length:"
+ "destroy"
+ "initWithPSK:::::"
+ "internal_reference"
+ "nw_protocol_boringssl_initiate_pqtls_fallback"
- "#\"?r\xc1!\xb2"
- "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) ech(%{bool}d) pqtls(%{bool}d)]"
- "%{public}s(%d) %{public}s[%p] TLS connected [version(0x%04x) ciphersuite(%s) group(0x%04x) signature_alg(0x%04x) alpn(%{public}s) resumed(%d) offered_ticket(%d) false_started(%d) ocsp_received(%d) sct_received(%d) connect_time(%llums) flight_time(%llums) rtt(%llums) write_stalls(%zu) read_stalls(%zu)]"
- "%{public}s(%d) %{public}s[%p] no input_protocol or supports_external_data callback"
- "%{public}s(%d) %{public}s[%p] no output_handler or get_input_frames callback"
- "%{public}s(%d) %{public}s[%p] no output_handler or get_output_frames callback"
- "%{public}s(%d) %{public}s[%p] no protocol->default_input_handler or connected callback"
- "max_allowed_dtls_version"
- "max_allowed_tls_version"
- "min_allowed_dtls_version"
- "min_allowed_tls_version"
- "protocol"
- "{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}"

```
