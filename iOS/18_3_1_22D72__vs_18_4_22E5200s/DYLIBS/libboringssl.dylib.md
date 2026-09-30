## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.60.4.0.0
-  __TEXT.__text: 0x98178
-  __TEXT.__auth_stubs: 0x1790
-  __TEXT.__objc_methlist: 0xd8
-  __TEXT.__cstring: 0x103ac
-  __TEXT.__const: 0x10068
-  __TEXT.__oslogstring: 0x5362
-  __TEXT.__gcc_except_tab: 0x2978
-  __TEXT.__unwind_info: 0x21a0
+486.100.24.0.0
+  __TEXT.__text: 0x9a670
+  __TEXT.__auth_stubs: 0x1950
+  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__cstring: 0x10391
+  __TEXT.__const: 0xfd98
+  __TEXT.__oslogstring: 0x551d
+  __TEXT.__gcc_except_tab: 0x2a8c
+  __TEXT.__unwind_info: 0x2390
   __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x245
-  __TEXT.__objc_methname: 0xe17
+  __TEXT.__objc_classname: 0x241
+  __TEXT.__objc_methname: 0xe76
   __TEXT.__objc_methtype: 0x6f7
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xb7f0
+  __TEXT.__objc_stubs: 0x60
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__const: 0xb858
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x1618
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x2318
+  __AUTH_CONST.__auth_got: 0xcc0
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x16d8
+  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__objc_const: 0x2168
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0xcb8
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0xd10
   __DATA.__bss: 0x550
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x210

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2984
-  Symbols:   3465
-  CStrings:  3584
+  Functions: 3037
+  Symbols:   3574
+  CStrings:  3595
 
Symbols:
+ _OBJC_CLASS_$_NSString
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
+ _nw_endpoint_create_host_with_numeric_port
+ _nw_path_is_direct
+ _nw_path_is_local
+ _nw_protocol_get_input_handler
+ _nw_protocol_get_path
+ _nw_settings_get_pqtls_enabled
+ _objc_msgSend
+ _objc_retain_x26
+ _sec_identity_copy_SPAKE2PLUSV1_client_identity
+ _sec_identity_copy_SPAKE2PLUSV1_client_password_verifier
+ _sec_identity_copy_SPAKE2PLUSV1_context
+ _sec_identity_copy_SPAKE2PLUSV1_registration_record
+ _sec_identity_copy_SPAKE2PLUSV1_server_identity
+ _sec_identity_copy_SPAKE2PLUSV1_server_password_verifier
+ _sec_identity_copy_type
+ _sec_protocol_configuration_copy_transformed_options_for_address
+ _sec_protocol_configuration_copy_transformed_options_for_host
CStrings:
+ "%{public}s(%d) %{public}s[%p] Invalid sec_identity provided (SEC_PROTOCOL_IDENTITY_TYPE_INVALID)"
+ "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) ech(%{bool}d) pqtls(%{bool}d)]"
+ "%{public}s(%d) %{public}s[%p] Unsupported sec_identity provided (%d)"
+ "%{public}s(%d) KYBER_private_key not initialized"
+ "%{public}s(%d) KYBER_public_key not initialized"
+ "%{public}s(%d) cckem_decapsulate failed"
+ "%{public}s(%d) cckem_encapsulate failed"
+ "%{public}s(%d) cckem_export_pubkey failed"
+ "."
+ ".local"
+ ".local."
+ "ConfirmationKeys"
+ "KYBER_decap"
+ "KYBER_encap"
+ "KYBER_generate_key"
+ "KYBER_parse_public_key"
+ "SharedKey"
+ "ats_non_pfs_ciphersuite_allowed"
+ "boringssl_context_set_ats_non_pfs_ciphersuite_allowed"
+ "boringssl_context_set_identity"
+ "containsString:"
+ "hasSuffix:"
+ "pqtls_enabled"
+ "stringWithUTF8String:"
- "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ech(%{bool}d)]"
- "0 `"
- "BORINGSSL_keccak_absorb"
- "compress"
- "ctx->absorb_offset < ctx->rate_bytes"
- "keccak.c"
- "keccak_ctx->rate_bytes == 168"
- "keccak_ctx->squeeze_offset == 0"
- "kyber.c"
- "reduce"
- "reduce_once"
- "remainder < 2u * kPrime"
- "scalar_from_keccak_vartime"
- "x < 2 * kPrime"
- "x < kPrime + 2u * kPrime * kPrime"

```
