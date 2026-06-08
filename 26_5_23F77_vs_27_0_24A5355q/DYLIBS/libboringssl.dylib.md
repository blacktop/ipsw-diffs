## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.120.8.0.0
-  __TEXT.__text: 0xa2c5c
-  __TEXT.__auth_stubs: 0x1e50
+577.0.0.0.0
+  __TEXT.__text: 0xa2740
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x12241
+  __TEXT.__cstring: 0x12304
   __TEXT.__const: 0xff48
-  __TEXT.__oslogstring: 0x68ec
-  __TEXT.__gcc_except_tab: 0x2944
-  __TEXT.__unwind_info: 0x25a8
+  __TEXT.__oslogstring: 0x6b0d
+  __TEXT.__gcc_except_tab: 0x289c
+  __TEXT.__unwind_info: 0x2590
   __TEXT.__eh_frame: 0x130
-  __TEXT.__objc_classname: 0x244
-  __TEXT.__objc_methname: 0xfbb
-  __TEXT.__objc_methtype: 0x62b
-  __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0xb9a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xb9e8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf40
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1948
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x22e8
+  __AUTH_CONST.__objc_const: 0x2308
+  __AUTH_CONST.__weak_auth_got: 0x8
+  __AUTH_CONST.__auth_got: 0xf48
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_ivar: 0x334
   __DATA.__data: 0xd58
   __DATA.__bss: 0x568
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x218
+  __DATA_DIRTY.__data: 0x220
   __DATA_DIRTY.__bss: 0xcb0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8F048915-B7AF-3687-89E7-816F6FE917B0
-  Functions: 3270
-  Symbols:   7763
-  CStrings:  3746
+  UUID: A3D26AF8-139E-32BE-A30B-4331A27DE378
+  Functions: 3258
+  Symbols:   7711
+  CStrings:  3450
 
Symbols:
+ GCC_except_table160
+ GCC_except_table64
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.ats_failure_reason
+ _OUTLINED_FUNCTION_54
+ _TLS_METRIC_FAILURE_ATS_REASON
+ __ZNSt3__110unique_ptrI10buf_mem_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI10ssl_ctx_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI11ec_point_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI11evp_pkey_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI12ecdsa_sig_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI14ssl_session_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI15ssl_ech_keys_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI16crypto_buffer_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI17err_save_state_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI17spake2plus_ctx_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI17ssl_credential_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI19stack_st_SSL_CIPHERN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI22stack_st_CRYPTO_BUFFERN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI32stack_st_SRTP_PROTECTION_PROFILEN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI6bio_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI6ssl_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI9bignum_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrI9ec_key_stN4bssl8internal7DeleterEE5resetB9fqe220100EPS1_
+ __ZNSt3__110unique_ptrIN4bssl10SSL3_STATEENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl10SSL_CONFIGENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11DTLS1_STATEENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11SSLKeyShareENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl11hm_fragmentENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl12SSLPAKEShareENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl12_GLOBAL__N_110ECKeyShareENS1_8internal7DeleterEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrIN4bssl13SSL_HANDSHAKEENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl14DTLSEpochStateENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl14SSLAEADContextENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl15ECHServerConfigENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl19SSL_HANDSHAKE_HINTSENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl21RecordNumberEncrypterENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl23SSLCipherPreferenceListENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27AES128RecordNumberEncrypterENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27AES256RecordNumberEncrypterENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl27ChaChaRecordNumberEncrypterENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl4CERTENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl9ECHConfigENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIN4bssl9TicketKeyENS1_8internal7DeleterEE5resetB9fqe220100EPS2_
+ __ZNSt3__110unique_ptrIcN4bssl8internal7DeleterEE5resetB9fqe220100EPc
+ __ZNSt3__110unique_ptrIhN4bssl8internal7DeleterEE5resetB9fqe220100EPh
+ __ZNSt3__120__copy_backward_implINS_17_ClassicAlgPolicyEEclB9fqe220100INS_8__bitsetILm4ELm256EEELb0EEENS_4pairINS_14__bit_iteratorIT_XT0_EXLi0EEEENS7_IS8_Lb0EXLi0EEEEEES9_S9_SA_
+ __ZNSt3__123__copy_backward_alignedB9fqe220100INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
+ __ZNSt3__123__specialized_algorithmINS_10_Algorithm8__fill_nEJNS_17__single_iteratorINS_14__bit_iteratorINS_8__bitsetILm4ELm256EEELb0ELm0EEEEEEE6__implB9fqe220100ILb0EEEvS7_m
+ __ZNSt3__123__specialized_algorithmINS_10_Algorithm8__fill_nEJNS_17__single_iteratorINS_14__bit_iteratorINS_8__bitsetILm4ELm256EEELb0ELm0EEEEEEE6__implB9fqe220100ILb1EEEvS7_m
+ __ZNSt3__123__specialized_algorithmINS_10_Algorithm8__fill_nEJNS_17__single_iteratorINS_14__bit_iteratorINS_8__bitsetILm4ELm256EEELb0ELm0EEEEEEEclB9fqe220100ImbEES7_S7_T_RKT0_
+ __ZNSt3__124__copy_move_unwrap_itersB9fqe220100INS_20__copy_backward_implINS_17_ClassicAlgPolicyEEENS_14__bit_iteratorINS_8__bitsetILm4ELm256EEELb0ELm0EEES7_S7_Li0EEENS_4pairIT0_T2_EES9_T1_SA_
+ __ZNSt3__125__copy_backward_unalignedB9fqe220100INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
+ __ZNSt3__16bitsetILm256EElSB9fqe220100Em
+ ___block_descriptor_32_e162_B16?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8l
+ ___block_descriptor_40_e162_B16?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8l
+ ___block_descriptor_40_e162_B16?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8lu32l8
+ ___block_descriptor_40_e8_32s_e162_B16?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8ls32l8
+ ___block_descriptor_56_e8_32s_e162_B16?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8ls32l8
+ ___block_descriptor_72_e8_32s40bs_e8_v12?0B8ls32l8u64l8s40l8
+ ___block_descriptor_88_e8_32r40r48r_e162_B16?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8lu56l8u64l8r32l8r40l8r48l8
+ ___block_literal_global.133
+ ___block_literal_global.148
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.90
+ ___block_literal_global.92
+ ___boringssl_context_evaluate_trust_async_external_block_invoke.214
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.208
+ ___boringssl_context_evaluate_trust_async_internal_log_only_block_invoke.212
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.18
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.20
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.20.cold.1
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.23
+ ___nw_protocol_boringssl_begin_connection_block_invoke.152
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.142
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.142.cold.1
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.142.cold.2
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.142.cold.3
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.142.cold.4
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.142.cold.5
+ ___nw_protocol_boringssl_write_frames_block_invoke.137
+ ___nw_protocol_boringssl_write_frames_block_invoke.137.cold.1
+ _boringssl_context_alert_callback_handler.cold.1
+ _boringssl_context_ciphersuites_match_group
+ _boringssl_context_ciphersuites_match_groups
+ _boringssl_context_get_ats_failure_reason
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _sec_protocol_metadata_access_locked_content
- GCC_except_table156
- GCC_except_table194
- GCC_except_table61
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_59
- _OUTLINED_FUNCTION_60
- _OUTLINED_FUNCTION_61
- _OUTLINED_FUNCTION_62
- _OUTLINED_FUNCTION_63
- _OUTLINED_FUNCTION_64
- _OUTLINED_FUNCTION_65
- _OUTLINED_FUNCTION_66
- _OUTLINED_FUNCTION_67
- __ZNSt3__110unique_ptrI10buf_mem_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI10ssl_ctx_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI11ec_point_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI11evp_pkey_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI12ecdsa_sig_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI14ssl_session_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI15ssl_ech_keys_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI16crypto_buffer_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI17err_save_state_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI17spake2plus_ctx_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI17ssl_credential_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI19stack_st_SSL_CIPHERN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI22stack_st_CRYPTO_BUFFERN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI32stack_st_SRTP_PROTECTION_PROFILEN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI6bio_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI6ssl_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI9bignum_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI9ec_key_stN4bssl8internal7DeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrIN4bssl10SSL3_STATEENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl10SSL_CONFIGENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl11DTLS1_STATEENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl11SSLKeyShareENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl11hm_fragmentENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl12SSLPAKEShareENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl12_GLOBAL__N_110ECKeyShareENS1_8internal7DeleterEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN4bssl13SSL_HANDSHAKEENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl14DTLSEpochStateENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl14SSLAEADContextENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl15ECHServerConfigENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl19SSL_HANDSHAKE_HINTSENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl21RecordNumberEncrypterENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl23SSLCipherPreferenceListENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl27AES128RecordNumberEncrypterENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl27AES256RecordNumberEncrypterENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl27ChaChaRecordNumberEncrypterENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl4CERTENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl9ECHConfigENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN4bssl9TicketKeyENS1_8internal7DeleterEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIcN4bssl8internal7DeleterEE5resetB9nqe210106EPc
- __ZNSt3__110unique_ptrIhN4bssl8internal7DeleterEE5resetB9nqe210106EPh
- __ZNSt3__113__fill_n_boolB9nqe210106ILb0ENS_8__bitsetILm4ELm256EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS_29__size_difference_type_traitsIS4_vE9size_typeE
- __ZNSt3__120__copy_backward_implINS_17_ClassicAlgPolicyEEclB9nqe210106INS_8__bitsetILm4ELm256EEELb0EEENS_4pairINS_14__bit_iteratorIT_XT0_EXLi0EEEENS7_IS8_Lb0EXLi0EEEEEES9_S9_SA_
- __ZNSt3__123__copy_backward_alignedB9nqe210106INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
- __ZNSt3__124__copy_move_unwrap_itersB9nqe210106INS_20__copy_backward_implINS_17_ClassicAlgPolicyEEENS_14__bit_iteratorINS_8__bitsetILm4ELm256EEELb0ELm0EEES7_S7_Li0EEENS_4pairIT0_T2_EES9_T1_SA_
- __ZNSt3__125__copy_backward_unalignedB9nqe210106INS_8__bitsetILm4ELm256EEELb0EEENS_14__bit_iteratorIT_Lb0EXLi0EEEENS3_IS4_XT0_EXLi0EEEES6_S5_
- __ZNSt3__16bitsetILm256EElSB9nqe210106Em
- ___block_descriptor_32_e9_B16?0^v8l
- ___block_descriptor_40_e9_B16?0^v8l
- ___block_descriptor_48_e8_32bs_e8_v12?0B8lu40l8s32l8
- ___block_descriptor_56_e8_32s_e9_B16?0^v8ls32l8
- ___block_descriptor_88_e8_32r40r48r_e9_B16?0^v8lu56l8u64l8r32l8r40l8r48l8
- ___block_literal_global.134
- ___block_literal_global.149
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.89
- ___block_literal_global.91
- ___boringssl_context_evaluate_trust_async_external_block_invoke.213
- ___boringssl_context_evaluate_trust_async_external_block_invoke_3.cold.4
- ___boringssl_context_evaluate_trust_async_external_block_invoke_3.cold.5
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.207
- ___boringssl_context_evaluate_trust_async_internal_log_only_block_invoke.210
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.17
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.19
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.19.cold.1
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.22
- ___nw_protocol_boringssl_begin_connection_block_invoke.153
- ___nw_protocol_boringssl_get_input_frames_block_invoke.143
- ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.1
- ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.2
- ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.3
- ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.4
- ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.5
- ___nw_protocol_boringssl_write_frames_block_invoke.138
- ___nw_protocol_boringssl_write_frames_block_invoke.138.cold.1
- _nw_protocol_metadata_access_handle
- _objc_release_x10
CStrings:
+ "%{public}s(%d) %{public}s[%p] Error [ATS FCPv2.1 violation]: Server certificate signed using signature algorithm %{public}s not advertised in client hello for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] Error [ATS FCPv2.1 violation]: TLS 1.2 negotiated without extended master secret (EMS) for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] Error [ATS Violation]: ATS certificate trust requirement not satisfied for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] Error [ATS violation]: ECDSA key size %zu bits is less than minimum %d bits for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] Error [ATS violation]: Leaf certificate hash algorithm (%d) is not at least SHA-256 for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] Error [ATS violation]: Leaf certificate is absent for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] Error [ATS violation]: Peer public key not set for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] Error [ATS violation]: RSA key size %zu bits is less than minimum %d bits for server: %{public}s"
+ "1!`"
+ "B16@?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]@@@@@@@@@@@@***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8"
+ "ats_failure_reason"
+ "nw_protocol_boringssl_disconnect has been called re-entrantly, returning early to avoid double disconnect."
- "#16@0:8"
- "%{public}s(%d) %{public}s[%p] ATS violation: EC key size %zu less than minimum bound %d"
- "%{public}s(%d) %{public}s[%p] ATS violation: Leaf certificate hash algorithm (%d) is not at least SHA-256"
- "%{public}s(%d) %{public}s[%p] ATS violation: Leaf certificate is absent"
- "%{public}s(%d) %{public}s[%p] ATS violation: RSA key size %zu less than minimum bound %d"
- "%{public}s(%d) %{public}s[%p] FCS TLS v2 compliance error: leaf cert signature algorithm not in offered signature algorithms"
- "(sockaddr_in_4_6=\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]}\"sin\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"sin6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})"
- "*"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_data>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_nw_array>\""
- "@\"NSObject<OS_nw_association>\""
- "@\"NSObject<OS_nw_context>\""
- "@\"NSObject<OS_nw_frame>\""
- "@\"NSObject<OS_nw_parameters>\""
- "@\"NSObject<OS_nw_protocol_metadata>\""
- "@\"NSObject<OS_nw_protocol_options>\""
- "@\"NSObject<OS_sec_array>\""
- "@\"NSObject<OS_sec_identity>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\"16@0:8"
- "@\"boringssl_concrete_boringssl_ctx\""
- "@\"boringssl_concrete_boringssl_identity\""
- "@\"boringssl_concrete_boringssl_psk_cache\""
- "@\"boringssl_concrete_boringssl_session_cache\""
- "@\"boringssl_concrete_boringssl_session_state\""
- "@\"boringssl_concrete_nw_protocol_boringssl\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "I"
- "NSObject"
- "OS_boringssl_context_state"
- "OS_boringssl_ctx"
- "OS_boringssl_identity"
- "OS_boringssl_psk"
- "OS_boringssl_psk_cache"
- "OS_boringssl_session_cache"
- "OS_boringssl_session_state"
- "OS_nw_protocol_boringssl"
- "Q"
- "Q16@0:8"
- "S"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "[16C]"
- "[84c]"
- "^?"
- "^v"
- "^{_NSZone=}16@0:8"
- "^{__CFArray=}"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
- "^{__SecTrust=}"
- "^{boringssl_legacy_ctx=I^v}"
- "^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v}"
- "^{ssl_ctx_st=}"
- "^{ssl_st=}"
- "address_string"
- "alert_callback"
- "allow_server_identity_change"
- "alpn_enabled"
- "alpn_protocols"
- "application_output_handler"
- "association"
- "async_context"
- "async_count"
- "ats_violation_detected"
- "autorelease"
- "b1"
- "backup_peer_trust_ref"
- "boringssl_bio"
- "boringssl_concrete_boringssl_context_state"
- "boringssl_concrete_boringssl_ctx"
- "boringssl_concrete_boringssl_identity"
- "boringssl_concrete_boringssl_psk"
- "boringssl_concrete_boringssl_psk_cache"
- "boringssl_concrete_boringssl_session_cache"
- "boringssl_concrete_boringssl_session_state"
- "boringssl_concrete_nw_protocol_boringssl"
- "boringssl_context_evaluate_trust_async_external_block_invoke_2"
- "boringssl_handle"
- "cached_content_type"
- "callbacks"
- "cancelled"
- "cert_lookup_done"
- "certificate_compression_algorithm"
- "certificate_compression_enabled"
- "certificate_compression_used"
- "certificate_signature_algorithm"
- "certificates"
- "challenge_block"
- "challenge_queue"
- "ciphersuite_configuration_string"
- "claimed_input_bytes"
- "class"
- "client_queue"
- "client_raw_public_key_certificates"
- "conformsToProtocol:"
- "connected_callback"
- "containsString:"
- "context"
- "current_flight_time"
- "current_handshake_state"
- "current_handshake_type"
- "current_input_frame"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "decrypt_block"
- "decryption_result"
- "deferred_input_finished"
- "destroy"
- "did_receive_data_once"
- "early_data_enabled"
- "early_output_handler"
- "ech_enabled"
- "encryption_read_level"
- "encryption_write_level"
- "enforce_ev"
- "external_frames"
- "fallback_mode"
- "fcs_tls_v2_compliance_mode_enabled"
- "finalized_output_frame_array"
- "flight_direction"
- "handshake_end"
- "handshake_func"
- "handshake_message_callback"
- "handshake_message_callback_queue"
- "handshake_output_handler"
- "handshake_start"
- "handshake_state_callback"
- "handshake_timer"
- "hasSuffix:"
- "hash"
- "i"
- "identity"
- "in_write_frames"
- "inbound_byte_count"
- "initWithPSK:::::"
- "initial_output_handler"
- "input_available_unacknowledged"
- "input_frame_array"
- "input_frame_byte_count"
- "input_suspended"
- "internal_reference"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "key_update_block"
- "key_update_queue"
- "legacy_context"
- "list"
- "log_identities_redacted"
- "log_str"
- "logging_disabled"
- "message_mode"
- "message_writer"
- "metadata"
- "minimum_ecdsa_key_size"
- "minimum_rsa_key_size"
- "minimum_signature_algorithm"
- "new_session_ticket_request"
- "npn_enabled"
- "nsURLRequestAttribution"
- "nw_protocol_boringssl_disconnect has been called re-entrantly and will call boringssl_session_disconnect a second time."
- "ocsp_enable"
- "offered_ticket"
- "old_ats_enforced"
- "old_ats_enforced_compat"
- "old_identity"
- "options"
- "outbound_byte_count"
- "output_application_frame_array"
- "output_batched_bytes_written"
- "output_batching_frame"
- "output_early_frame_array"
- "output_frame_array"
- "output_handshake_frame_array"
- "output_initial_frame_array"
- "output_pending_length"
- "output_protocol_supports_early_data"
- "pake_offered"
- "parameters"
- "peer_cert_chain"
- "peer_public_key"
- "peer_trust_evaluation_error"
- "peer_trust_ref"
- "peer_trust_result"
- "peer_verification_in_progress"
- "peer_verified"
- "pending_output_buffer"
- "pending_output_buffer_length"
- "pending_output_data"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pqtls_fallback_initiated"
- "private_key"
- "private_key_decrypt_block"
- "private_key_operation_complete"
- "private_key_queue"
- "private_key_sign_block"
- "psk_cache"
- "psk_negotiated"
- "psk_selection_block"
- "psk_selection_queue"
- "queue"
- "r*"
- "r^v"
- "read_frame_array"
- "read_func"
- "read_ready"
- "received_certificate_request"
- "received_connect"
- "recovered_session"
- "ref_cnt"
- "release"
- "remote_address"
- "renewed"
- "request_epoch_ms"
- "respondsToSelector:"
- "response_epoch_ms"
- "resumed"
- "resumed_session_ticket_request"
- "retain"
- "retainCount"
- "sct_enable"
- "self"
- "sent_error"
- "serialized_session"
- "serialized_session_length"
- "server"
- "server_raw_public_key_certificates"
- "servicing_handshake"
- "servicing_reads"
- "session_cache"
- "session_state"
- "session_ticket_enabled"
- "session_update_block"
- "session_update_queue"
- "sign_block"
- "signature_result"
- "skip_ats_trust_evaluation"
- "ssl_alert"
- "ssl_ctx"
- "ssl_max_version"
- "ssl_min_version"
- "ssl_session"
- "ssl_state"
- "started_flight"
- "started_negotiation"
- "stringWithUTF8String:"
- "subject_name"
- "superclass"
- "tls13_aesgcm_enabled"
- "tls13_chacha20poly1305_enabled"
- "tls13_epsk_offered"
- "total_flight_time"
- "tried_resumption"
- "trust_evaluation_complete"
- "trust_invalid_certs"
- "unassigned_input_frame_array"
- "used_extended_master_secret"
- "v16@0:8"
- "verify_block"
- "verify_queue"
- "waiting_for_writable"
- "wake_flag"
- "write_func"
- "write_ready"
- "zone"
- "{boringssl_ctx_alert=\"ssl_alert_type\"i\"ssl_alert_level\"C\"ssl_alert_code\"C\"ssl_warning_count\"C}"
- "{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}"

```
