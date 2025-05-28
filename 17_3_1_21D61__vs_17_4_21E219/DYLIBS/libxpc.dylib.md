## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-2679.80.5.0.1
-  __TEXT.__text: 0x37834
-  __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__const: 0x590
-  __TEXT.__cstring: 0x6d72
-  __TEXT.__oslogstring: 0x12c3
+2748.102.2.0.0
+  __TEXT.__text: 0x3aee0
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_methlist: 0x224
+  __TEXT.__const: 0x5b0
+  __TEXT.__cstring: 0x70e2
+  __TEXT.__oslogstring: 0x152c
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1034
+  __TEXT.__unwind_info: 0x10f0
   __TEXT.__objc_classname: 0x217
-  __TEXT.__objc_methname: 0x1d2
+  __TEXT.__objc_methname: 0x1e4
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__auth_got: 0x828
+  __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3390
+  __DATA_CONST.__const: 0x33a8
   __DATA_CONST.__objc_classlist: 0x110
-  __DATA_CONST.__objc_nlclslist: 0xe8
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_nlclslist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2408
+  __DATA_CONST.__objc_const: 0x2390
   __DATA_CONST.__objc_selrefs: 0x88
-  __DATA.__objc_classrefs: 0x28
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__data: 0xba0
+  __DATA_CONST.__objc_classrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA.__data: 0xb40
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x8
   __DATA.__bss: 0x80

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  Functions: 1761
-  Symbols:   3858
-  CStrings:  1143
+  Functions: 1818
+  Symbols:   3954
+  CStrings:  1183
 
Symbols:
+ -[OS_xpc_session dealloc]
+ -[OS_xpc_session description]
+ -[OS_xpc_session init]
+ _CESerializeWithOptions
+ _CESizeSerialization
+ _CEValidateWithOptions
+ _CEXPCRuntime
+ ____xpc_dict_copy_sorted_keys_block_invoke
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.22
+ ___block_descriptor_tmp.50
+ ___block_literal_global.112
+ ___block_literal_global.121
+ ___block_literal_global.21
+ ___block_literal_global.44
+ ___convert_xpc_array_to_ce_elem_array_block_invoke
+ ___sandbox_ms
+ ___serialize_xpc_array_block_invoke
+ ___serialize_xpc_dict_block_invoke
+ ___xpc_session_send_message_with_reply_async_block_invoke_2.cold.1
+ __xpc_connection_check_peer_requirement
+ __xpc_connection_extract_connection
+ __xpc_connection_set_lwcr
+ __xpc_connection_set_lwcr_entitlement_requirement
+ __xpc_connection_set_lwcr_requirements
+ __xpc_connection_token_satisfies_lwcr
+ __xpc_connection_token_satisfies_lwcr.cold.1
+ __xpc_copy_csops_string
+ __xpc_dict_copy_sorted_keys
+ __xpc_envdict_putenv
+ __xpc_runtime_process_has_entered_sandbox
+ __xpc_session_alloc
+ __xpc_session_create_from_connection_4SWIFT
+ __xpc_session_extract_connection_4SWIFT
+ __xpc_session_get_peer_audit_token_4SWIFT
+ __xpc_session_is_extracted
+ _amfi_developer_mode_resolved
+ _amfi_developer_mode_status
+ _amfi_interface_authorize_local_signing
+ _amfi_interface_cdhash_in_trustcache
+ _amfi_interface_get_local_signing_private_key
+ _amfi_interface_get_local_signing_public_key
+ _amfi_interface_query_bootarg_state
+ _amfi_interface_set_local_signing_public_key
+ _amfi_launch_constraint_matches_process
+ _amfi_launch_constraint_set_spawnattr
+ _cc_clear
+ _ccder_blob_encode_body
+ _ccder_blob_encode_body_tl
+ _ccder_blob_encode_len
+ _ccder_blob_encode_tag
+ _ccder_blob_encode_tl
+ _ccder_blob_reserve
+ _ccder_blob_reserve_tl
+ _ccder_sizeof
+ _ccder_sizeof_len
+ _ccder_sizeof_tag
+ _der_encode_number
+ _der_size_dictionary
+ _der_size_element
+ _memset_s
+ _os_map_128_destroy
+ _os_map_128_find
+ _os_map_128_init
+ _os_map_128_insert
+ _posix_spawnattr_setmacpolicyinfo_np
+ _serialize_xpc_dict
+ _serialize_xpc_object
+ _xpc_connection_set_peer_entitlement_exists_requirement
+ _xpc_connection_set_peer_entitlement_matches_value_requirement
+ _xpc_connection_set_peer_lightweight_code_requirement
+ _xpc_connection_set_peer_platform_identity_requirement
+ _xpc_connection_set_peer_team_identity_requirement
+ _xpc_create_data_from_lwcr_dictionary
+ _xpc_create_lwcr_dictionary
+ _xpc_create_lwcr_query_for_validation_category
+ _xpc_endpoint_create_bs_from_port
+ _xpc_get_service_name_from_pid
+ _xpc_is_xpcservice
- __OBJC_$_PROP_LIST_OS_xpc_session
- __OBJC_$_PROTOCOL_REFS_OS_xpc_session
- __OBJC_CLASS_PROTOCOLS_$_OS_xpc_session
- __OBJC_LABEL_PROTOCOL_$_OS_xpc_session
- __OBJC_PROTOCOL_$_OS_xpc_session
- __OS_xpc_type_session
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.115
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.49
- ___block_literal_global.107
- ___block_literal_global.117
- ___block_literal_global.20
- ___block_literal_global.43
- __xpc_session__wire_length
- __xpc_session_copy
- __xpc_session_debug
- __xpc_session_desc
- __xpc_session_deserialize
- __xpc_session_equal
- __xpc_session_hash
- __xpc_session_serialize
CStrings:
+ "$in"
+ "$query"
+ "%s.peer[%d]"
+ "AMFI"
+ "Attempting to set LWCR with invalid type: %s"
+ "Attempting to set entitlement matching value with unsupported value type: %s"
+ "B24@?0Q8^v16"
+ "Cannot force the listener to be both a MachService and a XPCService"
+ "Connection message forbidden due to code signing requirement: %d"
+ "Constraint too large"
+ "Dropping check-in message due to code signing requirement: %d"
+ "Extracted"
+ "No Constraint provided"
+ "Peer forbidden (code signing)"
+ "Reply message forbidden due to code signing requirement: %d"
+ "Session must be inactive to extract the connection, not %s"
+ "T@\"NSString\",?,R,C"
+ "Underlying connection extracted"
+ "[%p] Channel could not return listener port."
+ "[%p] Channel returned listener port: 0x%x"
+ "[%p] Falling back to bootstrap_look_up() = %d, lp: 0x%x"
+ "[%p] LWCR invalid: %s"
+ "[%p] LWCR requirement doesn't match: %s"
+ "[%p] Peer session extracted"
+ "[%p] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED"
+ "[%p] Session created from connection [%p]"
+ "[%p] Set peer lightweight code requirement on connection (%s): %s"
+ "[%p] Set peer lightweight code requirement on connection: %s"
+ "[%p] Unable to convert LWCR dictionary to LWCR data"
+ "[%p] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()"
+ "ccat"
+ "comp"
+ "entitlements"
+ "failed to serialized value for key: %s"
+ "invalid flags value %llu"
+ "no value for key: %s"
+ "reqs"
+ "security.mac.amfi.developer_mode_resolved"
+ "security.mac.amfi.developer_mode_status"
+ "service-name"
+ "signing-identifier"
+ "team-identifier-for-current-process"
+ "unsupported type: %s"
+ "validation-category"
+ "vers"
+ "xpc_connection_set_peer_* family must be called no more than once"
- "%s. State: %s.%s"
- "%s.peer.%s"
- "Attempt to serialize a session."
- "Cancelation Reason: %s"
- "None"
- "[%p] invalidated on xpc_connection_cancel()"

```
