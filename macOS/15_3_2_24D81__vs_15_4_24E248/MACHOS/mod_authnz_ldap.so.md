## mod_authnz_ldap.so

> `/usr/libexec/apache2/mod_authnz_ldap.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xf4e8
+880.0.0.0.0
+  __TEXT.__text: 0xe260
   __TEXT.__auth_stubs: 0x380
   __TEXT.__cstring: 0x28b1
-  __TEXT.__unwind_info: 0x7c
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: FCA54E3F-B494-3905-9EDA-4CFBEF7E1069
+  UUID: 785DEAF5-F754-3DE7-B160-1406C7F8CA3A
   Functions: 28
   Symbols:   108
   CStrings:  180
Functions:
~ _create_authnz_ldap_dir_config : 364 -> 360
~ _register_hooks : 352 -> 356
~ _mod_auth_ldap_parse_url : 2260 -> 2004
~ _set_bind_password : 520 -> 468
~ _mod_auth_ldap_add_subgroup_attribute : 200 -> 180
~ _mod_auth_ldap_add_subgroup_class : 152 -> 144
~ _mod_auth_ldap_set_subgroup_maxdepth : 84 -> 72
~ _mod_auth_ldap_add_group_attribute : 152 -> 144
~ _mod_auth_ldap_set_deref : 344 -> 292
~ _set_bind_pattern : 200 -> 188
~ _authnz_ldap_post_config : 1100 -> 1024
~ _authn_ldap_check_password : 8616 -> 7984
~ _ldap_determine_binddn : 420 -> 336
~ _authn_ldap_build_filter : 976 -> 884
~ _authn_ldap_xlate_password : 268 -> 236
~ _set_request_vars : 708 -> 600
~ _get_conv_set : 336 -> 292
~ _derive_codepage_from_lang : 284 -> 248
~ _ldapuser_check_authorization : 8496 -> 7900
~ _ldap_parse_config : 252 -> 232
~ _get_connection_for_authz : 408 -> 328
~ _authnz_ldap_cleanup_connection_close : 64 -> 60
~ _ldapgroup_check_authorization : 12396 -> 11532
~ _ldapdn_check_authorization : 6548 -> 6088
~ _ldapattribute_check_authorization : 7496 -> 6968
~ _ldapfilter_check_authorization : 9460 -> 8792
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authnz_ldap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authnz_ldap.c"

```
