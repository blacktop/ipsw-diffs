## ldap

> `/System/Library/OpenDirectory/Modules/ldap.bundle/Contents/MacOS/ldap`

```diff

 904.0.0.0.0
-  __TEXT.__text: 0xe52c
+  __TEXT.__text: 0xdef0
   __TEXT.__auth_stubs: 0xdb0
   __TEXT.__const: 0x100
   __TEXT.__oslogstring: 0x1188
   __TEXT.__cstring: 0xc0b
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x210
   __DATA_CONST.__auth_got: 0x6d8
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x8

   - /System/Library/Frameworks/LDAP.framework/Versions/A/LDAP
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA9F500B-051B-3A59-854C-0303B35E269F
-  Functions: 199
-  Symbols:   1411
+  UUID: B4E04399-498C-392C-895F-BFDD2EDE48D9
+  Functions: 197
+  Symbols:   1530
   CStrings:  313
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/opendirectoryd_executables/install/TempContent/Objects/opendirectoryd.build/ldap.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/opendirectoryd_executables/install/TempContent/Objects/opendirectoryd.build/ldap.build/Objects-normal/arm64e/ldap.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/opendirectoryd_executables/install/TempContent/Objects/opendirectoryd.build/ldap.build/Objects-normal/arm64e/ldap_vers.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/opendirectoryd_executables/src/modules/ldap/
+ ___add_msg_ctx_block_invoke_2.cold.1
+ ___bervals_from_array_block_invoke.cold.2
+ ___class_hierarchy_copy_block_invoke.167.cold.2
+ ___class_hierarchy_copy_block_invoke.cold.2
+ ___do_modification_block_invoke.205.cold.3
+ ___do_modification_block_invoke.205.cold.4
+ ___do_modification_block_invoke.205.cold.5
+ ___query_add_predicate_block_invoke.cold.2
+ ___reconnect_ldap_block_invoke_2.cold.2
+ ___reconnect_ldap_block_invoke_2.cold.3
+ ___reconnect_ldap_block_invoke_2.cold.4
+ ___reconnect_ldap_block_invoke_2.cold.5
+ ___required_attributes_copy_block_invoke.cold.1
+ ___result_callback_block_invoke.cold.10
+ ___result_callback_block_invoke.cold.11
+ ___result_callback_block_invoke.cold.12
+ ___result_callback_block_invoke.cold.13
+ ___result_callback_block_invoke.cold.14
+ ___result_callback_block_invoke.cold.15
+ ___result_callback_block_invoke.cold.16
+ ___result_callback_block_invoke.cold.17
+ ___result_callback_block_invoke.cold.18
+ ___result_callback_block_invoke.cold.19
+ ___result_callback_block_invoke.cold.20
+ ___result_callback_block_invoke.cold.21
+ ___result_callback_block_invoke.cold.8
+ ___result_callback_block_invoke.cold.9
+ __odm_NodeCreateRecord_block_invoke.16.cold.2
+ __odm_NodeCreateRecord_block_invoke.18.cold.1
+ __odm_NodeCreateRecord_block_invoke_2.cold.2
+ _add_msg_ctx.cold.3
+ _close_ldap.cold.1
+ _connect_ldap.cold.5
+ _connect_ldap.cold.6
+ _connect_ldap.cold.7
+ _connect_ldap.cold.8
+ _connect_ldap.cold.9
+ _connection_close.cold.2
+ _connection_close.cold.3
+ _connection_close.cold.4
+ _connection_open.cold.3
+ _connection_open.cold.4
+ _connection_open.cold.5
+ _do_modification.cold.2
+ _issue_query.cold.4
+ _issue_query.cold.5
+ _issue_query.cold.6
+ _issue_query.cold.7
+ _issue_query.cold.8
+ _issue_query.cold.9
+ _ldap_context_clearrequests.cold.1
+ _parse_ldap_error.cold.3
+ _parse_ldap_error.cold.4
+ _query_create_searchFilter.cold.1
+ _reconnect_ldap.cold.12
+ _reconnect_ldap.cold.13
+ _reconnect_ldap.cold.14
+ _reconnect_ldap.cold.15
+ _reconnect_ldap.cold.16
+ _reconnect_ldap.cold.17
+ _reconnect_ldap.cold.18
+ _reconnect_ldap.cold.19
+ _reconnect_ldap.cold.20
+ _reconnect_ldap.cold.21
+ _reconnect_ldap.cold.22
+ _reconnect_ldap.cold.23
+ _reconnect_ldap.cold.24
+ _reconnect_ldap.cold.25
+ _reconnect_ldap.cold.26
+ _reconnect_ldap.cold.27
+ _reconnect_ldap.cold.28
+ _reconnect_ldap.cold.29
+ _reconnect_ldap.cold.30
+ _remove_msg_ctx.cold.2
+ _respond_to_request.cold.10
+ _respond_to_request.cold.11
+ _respond_to_request.cold.12
+ _respond_to_request.cold.13
+ _respond_to_request.cold.8
+ _respond_to_request.cold.9
+ _respond_with_error.cold.10
+ _respond_with_error.cold.11
+ _respond_with_error.cold.12
+ _respond_with_error.cold.6
+ _respond_with_error.cold.7
+ _respond_with_error.cold.8
+ _respond_with_error.cold.9
+ _result_callback.cold.2
+ _result_callback.cold.3
+ _update_context_from_options.cold.1
+ _update_dn_base.cold.3
+ _update_dn_base.cold.4
+ _update_dn_values.cold.1
+ _update_dn_values.cold.2
+ odm_NodeSetCredentialsExtended.cold.1
+ odm_NodeSetCredentialsExtended.cold.2
+ odm_QueryCreateWithNode.cold.1
+ odm_RecordDelete.cold.2
+ odm_RecordVerifyPassword.cold.2
+ odm_create_connection_with_options.cold.2
+ odm_locate_service.cold.10
+ odm_locate_service.cold.11
+ odm_locate_service.cold.12
+ odm_locate_service.cold.13
+ odm_locate_service.cold.14
+ odm_locate_service.cold.15
+ odm_locate_service.cold.16
+ odm_locate_service.cold.17
+ odm_locate_service.cold.18
+ odm_locate_service.cold.19
+ odm_locate_service.cold.20
+ odm_locate_service.cold.7
+ odm_locate_service.cold.8
+ odm_locate_service.cold.9
+ translate_recordtype.cold.2
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/opendirectoryd_executables/install/TempContent/Objects/opendirectoryd.build/ldap.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/opendirectoryd_executables/install/TempContent/Objects/opendirectoryd.build/ldap.build/Objects-normal/arm64e/ldap.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/opendirectoryd_executables/install/TempContent/Objects/opendirectoryd.build/ldap.build/Objects-normal/arm64e/ldap_vers.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/opendirectoryd_executables/src/modules/ldap/
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9

```
