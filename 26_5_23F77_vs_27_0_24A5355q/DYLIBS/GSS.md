## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

```diff

-710.100.4.0.0
-  __TEXT.__text: 0x27e7c
-  __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__const: 0x44a
+720.0.0.0.0
+  __TEXT.__text: 0x27f1c
+  __TEXT.__const: 0x43a
   __TEXT.__cstring: 0x3b55
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x728
-  __DATA_CONST.__got: 0x180
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1378
-  __AUTH_CONST.__auth_got: 0xf78
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2b8
   __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__auth_got: 0xf78
   __DATA.__data: 0xd10
   __DATA.__bss: 0x28c
   __DATA.__common: 0x94

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: 56A108D5-ABD6-3588-87B6-6704A02E446B
+  UUID: 19E3BC9C-CE6C-3681-99A4-84D7F3E72B37
   Functions: 673
   Symbols:   2163
   CStrings:  660
Functions:
~ __gsskrb5i_is_cfx : 320 -> 324
~ __gssapi_wrap_arcfour : 964 -> 972
~ __gssapi_unwrap_arcfour : 1096 -> 1104
~ __gssapi_wrap_cfx_iov : 1468 -> 1480
~ __gssapi_unwrap_cfx_iov : 1368 -> 1388
~ _unrotate_iov : 552 -> 564
~ __gssapi_wrap_cfx : 924 -> 928
~ _rrc_rotate : 292 -> 296
~ _check_compat : 264 -> 268
~ __gssapi_make_mech_header : 172 -> 176
~ _import_hostbased_name : 364 -> 368
~ _init_krb5_auth : 944 -> 948
~ __gsskrb5_inquire_sec_context_by_oid : 776 -> 780
~ __gsskrb5_pseudo_random : 628 -> 632
~ __gssapi_msg_order_check : 268 -> 260
~ _elem_insert : 140 -> 148
~ __gssapi_msg_order_export : 172 -> 176
~ __gss_mg_log : 272 -> 228
~ __gss_mg_create_cferror : 532 -> 536
~ _gss_krb5_free_lucid_sec_context : 204 -> 212
~ ___ApplePrivate_gss_mo_set : 216 -> 220
~ ___ApplePrivate_gss_mo_get : 220 -> 224
~ ___ApplePrivate_gss_mo_name : 244 -> 248
~ _make_sasl_name : 396 -> 432
~ _test_mech_attrs : 276 -> 280
~ __gss_ntlm_accept_sec_context : 1232 -> 1236
~ __gss_ntlm_wrap : 268 -> 272
~ __gss_ntlm_init_sec_context : 3148 -> 3160
~ __netlogon_make_initial_auth_message : 640 -> 652
~ __netlogon_import_name : 324 -> 328
~ __netlogon_seal : 460 -> 464

```
