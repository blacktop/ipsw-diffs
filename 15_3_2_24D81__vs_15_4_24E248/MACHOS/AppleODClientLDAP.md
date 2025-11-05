## AppleODClientLDAP

> `/System/Library/OpenDirectory/Modules/AppleODClientLDAP.bundle/Contents/MacOS/AppleODClientLDAP`

```diff

 164.0.0.0.0
-  __TEXT.__text: 0x16960
+  __TEXT.__text: 0x16744
   __TEXT.__auth_stubs: 0x1250
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x5dba
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__cstring: 0x5db3
+  __TEXT.__unwind_info: 0x428
   __DATA_CONST.__auth_got: 0x928
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0x8

   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: 15FA54B6-7B67-3293-A53A-44FF0E280683
-  Functions: 304
-  Symbols:   815
-  CStrings:  1194
+  UUID: 2F119C47-F788-33B3-B36A-C1027AB78D50
+  Functions: 303
+  Symbols:   833
+  CStrings:  1192
 
Symbols:
+ GetRecordPrivileges.cold.1
+ ___ldap_conn_auth_on_connection_block_invoke.cold.1
+ ___ldap_make_trust_account_session_key_agent_if_applicable_block_invoke.473.cold.1
+ ___ldap_record_is_member_of_group_block_invoke.cold.1
+ __ldap_disable_reason_to_oderror
+ __ldap_odconn_search_block_invoke_2.cold.1
+ _ldap_conn_auth_on_connection.cold.1
+ _ldap_conn_sasl_auth.cold.1
+ _ldap_update_service_principals.cold.1
+ _ldap_update_service_principals.cold.2
+ aodc_log_cfarray_contents.cold.1
+ aodc_log_cfdict_contents.cold.1
+ ldap_copy_certs_for_all_replicas.cold.1
+ ldap_copy_certs_from_server.cold.1
+ ldap_odconn_init_verify_only_connection_support.cold.1
+ ldap_remove_all_real_policies.cold.1
+ ldap_server_has_cert_server.cold.1
+ odm_locate_service.cold.1
CStrings:
- "::1"
- "lo"

```
