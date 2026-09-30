## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.40.3.0.0
-  __TEXT.__text: 0xa07d4
-  __TEXT.__auth_stubs: 0x1e60
+532.60.5.0.0
+  __TEXT.__text: 0xa11d4
+  __TEXT.__auth_stubs: 0x1e70
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x107d9
-  __TEXT.__const: 0xfef8
+  __TEXT.__cstring: 0x10848
+  __TEXT.__const: 0x10018
   __TEXT.__oslogstring: 0x5de7
-  __TEXT.__gcc_except_tab: 0x2908
-  __TEXT.__unwind_info: 0x24b8
+  __TEXT.__gcc_except_tab: 0x2948
+  __TEXT.__unwind_info: 0x24e0
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x241
   __TEXT.__objc_methname: 0xecf

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH_CONST.__auth_got: 0xf50
   __AUTH_CONST.__const: 0x1908
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x21a8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x308
-  __DATA.__data: 0xd08
+  __DATA.__data: 0xd10
   __DATA.__bss: 0x540
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x210

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CCC35852-2719-3773-9083-3A356AEA4754
-  Functions: 3140
-  Symbols:   7433
-  CStrings:  3661
+  UUID: 3E6F28DA-4565-38BA-A25F-8668FDDB8D96
+  Functions: 3154
+  Symbols:   7471
+  CStrings:  3667
 
Symbols:
+ GCC_except_table121
+ GCC_except_table154
+ GCC_except_table23
+ GCC_except_table30
+ GCC_except_table98
+ _SSL_CREDENTIAL_set1_signing_algorithm_prefs
+ _SSL_set1_group_ids
+ _SSL_set_compliance_policy
+ _SSL_set_signing_algorithm_prefs
+ _SSL_set_verify_algorithm_prefs
+ _TLS_METRIC_PQTLS_USED
+ __ZL15check_group_idsN4bssl4SpanIKtEE
+ __ZL16compare_uint16_tPKvS0_
+ __ZL16set_sigalg_prefsPN4bssl5ArrayItEENS_4SpanIKtEE
+ __ZN10fips202205L13kTLS12CiphersE
+ __ZN10fips202205L7kGroupsE
+ __ZN10fips202205L8kSigAlgsE
+ __ZN4bssl19ssl_group_id_to_nidEt
+ __ZN9wpa202304L13kTLS12CiphersE
+ __ZN9wpa202304L7kGroupsE
+ __ZN9wpa202304L8kSigAlgsE
+ __ZZN4bsslL28ssl_write_client_cipher_listEPKNS_13SSL_HANDSHAKEEP6cbb_stNS_23ssl_client_hello_type_tEE12kCiphersCNSA
+ ___block_literal_global.84
+ ___block_literal_global.86
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.18
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.21
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.21.cold.1
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke.23
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke_2.19
+ ___boringssl_session_apply_protocol_options_for_transport_block_invoke_2.19.cold.1
+ _boringssl_context_set_cnsa_compliance_policy
+ _boringssl_metrics_create_biome_connection_event
+ _boringssl_metrics_create_biome_connection_event.cold.1
+ _boringssl_session_get_used_pqtls
+ _strstr
- GCC_except_table120
- GCC_except_table153
- GCC_except_table46
- GCC_except_table96
- ___block_literal_global.80
- ___block_literal_global.82
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.17
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.19
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.19.cold.1
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke.22
- ___boringssl_session_apply_protocol_options_for_transport_block_invoke_2.cold.1
CStrings:
+ ".apple"
+ "TLSBiomeConnectionEvent"
+ "apple.com"
+ "boringssl_metrics_create_biome_connection_event"
+ "icloud.com"
+ "pqtls_used"

```
