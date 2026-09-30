## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

```diff

-710.0.1.0.0
-  __TEXT.__text: 0x27efc
+710.100.4.0.0
+  __TEXT.__text: 0x27e7c
   __TEXT.__auth_stubs: 0x1ef0
   __TEXT.__const: 0x44a
   __TEXT.__cstring: 0x3b55

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: 298FA19E-6765-3C91-B830-684299785C8A
-  Functions: 671
-  Symbols:   2159
+  UUID: DBF5E3F8-5A52-3523-AFB6-52465C0B1462
+  Functions: 673
+  Symbols:   2163
   CStrings:  660
 
Functions:
~ _OUTLINED_FUNCTION_0 : 24 -> 32
~ _GSSRuleAddMatch : 564 -> 556
~ _gsskrb5_acceptor_start : 2188 -> 2192
~ __gsskrb5_acquire_cred : 1076 -> 1072
~ __gssiakerb_acquire_cred : 744 -> 740
~ __gss_krb5_acquire_cred_ext : 3148 -> 3120
~ __gssapi_wrap_cfx_iov : 1488 -> 1468
~ _verify_flags : 156 -> 164
~ __gsskrb5_verify_header : 120 -> 116
~ __gsskrb5_inquire_cred : 776 -> 772
~ __gsskrb5_inquire_sec_context_by_oid : 780 -> 776
~ __gssapi_msg_order_export : 180 -> 172
~ __gssapi_msg_order_import : 360 -> 352
~ __gsskrb5_set_sec_context_option : 832 -> 824
~ _gss_accept_sec_context : 1256 -> 1252
~ _gss_add_oid_set_member : 200 -> 188
~ _gss_release_buffer_set : 156 -> 148
~ _gss_duplicate_oid : 196 -> 188
~ _gss_import_name : 896 -> 900
~ _gss_import_sec_context : 280 -> 276
~ _gss_inquire_cred : 916 -> 912
~ __gss_mech_import_name : 372 -> 368
+ _OUTLINED_FUNCTION_0
~ ___ApplePrivate_gss_oid_to_name : 120 -> 116
~ _gss_release_oid : 176 -> 168
+ _OUTLINED_FUNCTION_0
~ _select_mech : 440 -> 436
~ __gss_ntlm_accept_sec_context : 1236 -> 1232
~ _v2_verify_message : 232 -> 236
~ __gss_ntlm_cred_label_set : 744 -> 752
~ __netlogon_make_initial_auth_message : 644 -> 640
~ __netlogon_wrap_iov : 656 -> 660
~ _storeItem.cold.1 : 12 -> 4
~ __gss_mg_check_name.cold.1 : 20 -> 4
~ __gss_mg_check_credential.cold.1 : 20 -> 4

```
