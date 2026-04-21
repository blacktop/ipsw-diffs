## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.120.6.0.0
-  __TEXT.__text: 0xa25e8
+532.120.8.0.0
+  __TEXT.__text: 0xa2c5c
   __TEXT.__auth_stubs: 0x1e50
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x121f3
+  __TEXT.__cstring: 0x12241
   __TEXT.__const: 0xff48
-  __TEXT.__oslogstring: 0x67a3
+  __TEXT.__oslogstring: 0x68ec
   __TEXT.__gcc_except_tab: 0x2944
-  __TEXT.__unwind_info: 0x25a0
+  __TEXT.__unwind_info: 0x25a8
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x244
-  __TEXT.__objc_methname: 0xfa1
+  __TEXT.__objc_methname: 0xfbb
   __TEXT.__objc_methtype: 0x62b
   __TEXT.__objc_stubs: 0xa0
   __DATA_CONST.__got: 0xf8

   __AUTH_CONST.__auth_got: 0xf40
   __AUTH_CONST.__const: 0x1948
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x22c8
+  __AUTH_CONST.__objc_const: 0x22e8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x32c
+  __DATA.__objc_ivar: 0x330
   __DATA.__data: 0xd58
   __DATA.__bss: 0x568
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0023EA9E-9460-37A6-B951-6A90761CD2E6
-  Functions: 3266
-  Symbols:   7756
-  CStrings:  3741
+  UUID: 3A9F558D-300B-333D-B9AF-61EA9D989C8F
+  Functions: 3270
+  Symbols:   7763
+  CStrings:  3746
 
Symbols:
+ GCC_except_table156
+ GCC_except_table194
+ GCC_except_table61
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.skip_ats_trust_evaluation
+ ___boringssl_context_certificate_request_callback_block_invoke.223
+ ___boringssl_context_evaluate_trust_async_external_block_invoke.213
+ ___boringssl_context_evaluate_trust_async_external_block_invoke.217
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.202
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.207
+ ___boringssl_context_evaluate_trust_async_internal_log_only_block_invoke.211
+ ___boringssl_context_new_session_handler_block_invoke.252
+ ___boringssl_context_update_encryption_level_block_invoke.227
+ ___boringssl_context_update_encryption_level_block_invoke.229
+ _boringssl_context_log_potential_ats_violation_fcp_v2_1_negotiated_ciphersuite
+ _boringssl_context_log_potential_ats_violation_fcp_v2_1_negotiated_ciphersuite.cold.1
+ _boringssl_context_set_skip_ats_trust_evaluation
- GCC_except_table153
- GCC_except_table191
- GCC_except_table59
- ___boringssl_context_certificate_request_callback_block_invoke.222
- ___boringssl_context_evaluate_trust_async_external_block_invoke.212
- ___boringssl_context_evaluate_trust_async_external_block_invoke.216
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.201
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.206
- ___boringssl_context_evaluate_trust_async_internal_log_only_block_invoke.209
- ___boringssl_context_new_session_handler_block_invoke.251
- ___boringssl_context_update_encryption_level_block_invoke.226
- ___boringssl_context_update_encryption_level_block_invoke.228
Functions:
~ _nw_protocol_boringssl_copy_options_contents : 1520 -> 1532
~ ___boringssl_session_apply_protocol_options_for_transport_block_invoke : 7076 -> 7128
~ ___boringssl_context_evaluate_trust_async_external_block_invoke_3 : 5756 -> 6268
- _OUTLINED_FUNCTION_10
+ _boringssl_ciphers_copy_fcs_tls_v2_ciphersuites
+ _boringssl_context_set_skip_ats_trust_evaluation
+ _boringssl_context_log_potential_ats_violation_fcp_v2_1_negotiated_ciphersuite
~ _boringssl_context_update_potential_ATS_violations : 916 -> 948
+ _OUTLINED_FUNCTION_11
+ _boringssl_context_set_enable_message_mode.cold.1
CStrings:
+ "%{public}s(%d) %{public}s[%p] Skipping local ATS trust evaluation (ats_trust_policy=skip)"
+ "%{public}s(%d) %{public}s[%p] TLS configured [server(%d) min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) cc_mode_enforced(%{bool}d) ech(%{bool}d) pqtls(%{bool}d), pake(%{bool}d) skip_ats_trust(%{bool}d)]"
+ "%{public}s(%d) %{public}s[%p] Warning [ATS FCPv2.1 violation]: Ciphersuite(%s) not offered in ATS FCP_v2.1 mode negotiated for server: %{public}s"
+ "%{public}s(%d) %{public}s[%p] fcs_v2_ciphersuites unexpectedly NULL"
+ "boringssl_context_log_potential_ats_violation_fcp_v2_1_negotiated_ciphersuite"
+ "skip_ats_trust_evaluation"
- "%{public}s(%d) %{public}s[%p] TLS configured [server(%d) min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) cc_mode_enforced(%{bool}d) ech(%{bool}d) pqtls(%{bool}d), pake(%{bool}d)]"

```
