## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.122.1.0.0
-  __TEXT.__text: 0x9e220
-  __TEXT.__auth_stubs: 0x1970
+486.140.5.0.1
+  __TEXT.__text: 0x9e3d0
+  __TEXT.__auth_stubs: 0x1980
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__cstring: 0x10630
   __TEXT.__const: 0xfef8
-  __TEXT.__oslogstring: 0x577e
+  __TEXT.__oslogstring: 0x579b
   __TEXT.__gcc_except_tab: 0x28e8
-  __TEXT.__unwind_info: 0x2480
+  __TEXT.__unwind_info: 0x2488
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x241
   __TEXT.__objc_methname: 0xe76

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xcd0
+  __AUTH_CONST.__auth_got: 0xcd8
   __AUTH_CONST.__const: 0x18c8
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x2168

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 45A1A5D3-6A8C-32EF-975C-8A78A9D90076
-  Functions: 3121
-  Symbols:   7324
+  UUID: 97165C28-0ACD-3251-A6D7-B4C55EA0A649
+  Functions: 3124
+  Symbols:   7331
   CStrings:  3624
 
Symbols:
+ GCC_except_table120
+ GCC_except_table153
+ GCC_except_table92
+ _SSL_renegotiate_pending
+ ___boringssl_context_certificate_request_callback_block_invoke.215
+ ___boringssl_context_new_session_handler_block_invoke.240
+ ___boringssl_context_update_encryption_level_block_invoke.219
+ ___boringssl_context_update_encryption_level_block_invoke.221
+ _boringssl_session_get_negotiated_pake
+ _nw_protocol_get_parameters
- GCC_except_table119
- GCC_except_table152
- GCC_except_table91
- ___boringssl_context_new_session_handler_block_invoke.238
- ___boringssl_context_update_encryption_level_block_invoke.216
- ___boringssl_context_update_encryption_level_block_invoke.218
CStrings:
+ "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) ech(%{bool}d) pqtls(%{bool}d), pake(%{bool}d)]"
+ "%{public}s(%d) %{public}s[%p] TLS connected [version(0x%04x) ciphersuite(%s) group(0x%04x) signature_alg(0x%04x) alpn(%{public}s) resumed(%d) offered_ticket(%d) false_started(%d) ocsp_received(%d) sct_received(%d) connect_time(%llums) flight_time(%llums) rtt(%llums) write_stalls(%zu) read_stalls(%zu) pake(0x%04x)]"
- "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) ech(%{bool}d) pqtls(%{bool}d)]"
- "%{public}s(%d) %{public}s[%p] TLS connected [version(0x%04x) ciphersuite(%s) group(0x%04x) signature_alg(0x%04x) alpn(%{public}s) resumed(%d) offered_ticket(%d) false_started(%d) ocsp_received(%d) sct_received(%d) connect_time(%llums) flight_time(%llums) rtt(%llums) write_stalls(%zu) read_stalls(%zu)]"

```
