## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-2894.122.1.0.0
-  __TEXT.__text: 0x3a5e4
-  __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x32c
+3070.0.0.0.2
+  __TEXT.__text: 0x3bccc
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x35c
   __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x732c
-  __TEXT.__oslogstring: 0x1759
+  __TEXT.__cstring: 0x7672
+  __TEXT.__oslogstring: 0x1668
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x10a0
-  __TEXT.__objc_classname: 0x217
+  __TEXT.__unwind_info: 0x1168
+  __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x1b00
-  __DATA_CONST.__objc_classlist: 0x110
-  __DATA_CONST.__objc_nlclslist: 0xe0
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x1be0
+  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__objc_nlclslist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x880
-  __AUTH_CONST.__const: 0x1a08
-  __AUTH_CONST.__objc_const: 0x21a0
-  __DATA.__data: 0xb40
-  __DATA.__crash_info: 0x40
+  __DATA_CONST.__objc_superrefs: 0x58
+  __AUTH_CONST.__auth_got: 0x8f8
+  __AUTH_CONST.__const: 0x1b18
+  __AUTH_CONST.__objc_const: 0x2338
+  __AUTH.__objc_data: 0x50
+  __DATA.__data: 0xba8
+  __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x120
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: A46C2755-9586-33B8-9EA9-377F71175516
-  Functions: 1713
-  Symbols:   4304
-  CStrings:  1216
+  UUID: D972AD1B-9BF1-33EF-B521-81546D27EB3D
+  Functions: 1781
+  Symbols:   4461
+  CStrings:  1239
 
Symbols:
+ -[OS_xpc_peer_requirement dealloc]
+ -[OS_xpc_peer_requirement description]
+ -[OS_xpc_peer_requirement init]
+ _OBJC_CLASS_$_OS_xpc_peer_requirement
+ _OBJC_CLASS_$_OS_xpc_string_cache
+ _OBJC_METACLASS_$_OS_xpc_peer_requirement
+ _OBJC_METACLASS_$_OS_xpc_string_cache
+ _OUTLINED_FUNCTION_0
+ __OBJC_$_INSTANCE_METHODS_OS_xpc_peer_requirement
+ __OBJC_$_PROP_LIST_OS_xpc_string_cache
+ __OBJC_$_PROTOCOL_REFS_OS_xpc_string_cache
+ __OBJC_CLASS_PROTOCOLS_$_OS_xpc_string_cache
+ __OBJC_CLASS_RO_$_OS_xpc_peer_requirement
+ __OBJC_CLASS_RO_$_OS_xpc_string_cache
+ __OBJC_LABEL_PROTOCOL_$_OS_xpc_string_cache
+ __OBJC_METACLASS_RO_$_OS_xpc_peer_requirement
+ __OBJC_METACLASS_RO_$_OS_xpc_string_cache
+ __OBJC_PROTOCOL_$_OS_xpc_string_cache
+ __OS_xpc_type_string_cache
+ ____xpc_collection_apply_f_block_invoke
+ ____xpc_collection_apply_f_block_invoke_2
+ ____xpc_get_uid_for_name_block_invoke
+ ____xpc_listener_cancel_locked_block_invoke.23
+ ____xpc_session_complete_cancelation_locked_block_invoke.48
+ ____xpc_string_cache_for_each_block_invoke
+ ____xpc_string_cache_get_entries_block_invoke
+ ____xpc_string_cache_get_entries_sorted_block_invoke
+ ___block_descriptor_tmp.10
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.54
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.64
+ ___block_descriptor_tmp.65
+ ___block_literal_global.114
+ ___block_literal_global.22
+ ___block_literal_global.28
+ ___block_literal_global.44
+ ___block_literal_global.47
+ __availability_version_check.cold.1
+ __os_transaction_log_active.cold.2
+ __transaction_snapshot_write_crash_message.asi_str
+ __xpc_cached_string_create
+ __xpc_collection_apply_f
+ __xpc_connection_init_send_port
+ __xpc_connection_init_send_port.cold.1
+ __xpc_connection_init_send_port.cold.2
+ __xpc_connection_init_send_port.cold.3
+ __xpc_dictionary_mach_helper
+ __xpc_dictionary_node_get_key
+ __xpc_dictionary_set_value
+ __xpc_get_uid_for_name
+ __xpc_get_uid_for_name.bufsize
+ __xpc_get_uid_for_name.cold.1
+ __xpc_get_uid_for_name.onceToken
+ __xpc_graph_deserializer_get_key_string_cache
+ __xpc_graph_deserializer_get_value_string_cache
+ __xpc_graph_deserializer_set_key_string_cache
+ __xpc_graph_deserializer_set_key_string_cache.cold.1
+ __xpc_graph_deserializer_set_value_string_cache
+ __xpc_graph_deserializer_set_value_string_cache.cold.1
+ __xpc_is_cyclic
+ __xpc_is_cyclic_helper
+ __xpc_listener_assert_inactive
+ __xpc_listener_set_incoming_session_handler
+ __xpc_listener_string_for_state
+ __xpc_mach_port_make_send_once
+ __xpc_peer_requirement_alloc
+ __xpc_peer_requirement_create_lwcr_entitlement_requirement
+ __xpc_peer_requirement_dispose
+ __xpc_peer_requirement_handle_lwcr_match
+ __xpc_peer_requirement_match_token
+ __xpc_rich_error_peer_requirement_convert_failed
+ __xpc_string_cache_copy
+ __xpc_string_cache_debug
+ __xpc_string_cache_debug_desc
+ __xpc_string_cache_desc
+ __xpc_string_cache_deserialize
+ __xpc_string_cache_dispose
+ __xpc_string_cache_equal
+ __xpc_string_cache_free_entries
+ __xpc_string_cache_get_entries_sorted
+ __xpc_string_cache_get_string
+ __xpc_string_cache_hash
+ __xpc_string_cache_remove
+ __xpc_string_cache_serialize
+ __xpc_string_cache_try_remove
+ __xpc_string_cache_wire_length
+ __xpc_string_create_base
+ __xpc_string_set_value.cold.1
+ __xpc_token_satisfies_lwcr
+ __xpc_token_satisfies_lwcr.cold.1
+ __xpc_type_string_cache
+ __xpc_xml_create_string_no_copy_with_string_cache
+ _ce_element_array_free
+ _convert_xpc_array_to_ce_elem_array
+ _getpwnam_r
+ _mach_port_extract_right
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_storeWeak
+ _os_map_str_count
+ _os_map_str_delete
+ _os_map_str_destroy
+ _os_map_str_find
+ _os_map_str_foreach
+ _os_map_str_init
+ _os_map_str_insert
+ _os_unfair_recursive_lock_lock_with_options
+ _os_unfair_recursive_lock_unlock
+ _qsort_b
+ _sysconf
+ _xpc_bundle_create_from_origin_with_string_cache
+ _xpc_bundle_create_with_string_cache
+ _xpc_connection_set_peer_requirement
+ _xpc_create_from_plist_with_string_cache
+ _xpc_create_from_serialization_with_string_cache
+ _xpc_dictionary_set_value_with_key_string_cache
+ _xpc_endpoint_create_bs_named_user
+ _xpc_listener_set_incoming_session_handler
+ _xpc_listener_set_peer_requirement
+ _xpc_peer_requirement_create_entitlement_exists
+ _xpc_peer_requirement_create_entitlement_matches_value
+ _xpc_peer_requirement_create_lwcr
+ _xpc_peer_requirement_create_platform_identity
+ _xpc_peer_requirement_create_team_identity
+ _xpc_peer_requirement_match_received_message
+ _xpc_rich_error_create_no_copy
+ _xpc_service_instance_set_archpref
+ _xpc_service_set_attach_handler.cold.1
+ _xpc_session_set_peer_requirement
+ _xpc_string_cache_create
+ _xpc_string_cache_for_each
+ _xpc_string_cache_get_count
+ _xpc_string_cache_get_name
+ _xpc_string_create_cached
- ____xpc_listener_cancel_locked_block_invoke.21
- ____xpc_session_complete_cancelation_locked_block_invoke.47
- ___block_descriptor_tmp.115
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.38
- ___block_descriptor_tmp.53
- ___block_descriptor_tmp.57
- ___block_literal_global.117
- ___block_literal_global.126
- ___block_literal_global.20
- ___block_literal_global.27
- ___block_literal_global.46
- __xpc_connection_check_peer_requirement.cold.2
- __xpc_connection_init.cold.10
- __xpc_connection_init.cold.11
- __xpc_connection_init.cold.9
- __xpc_connection_set_lwcr
- __xpc_connection_set_lwcr.cold.1
- __xpc_connection_set_lwcr.cold.2
- __xpc_connection_set_lwcr_entitlement_requirement
- __xpc_connection_set_lwcr_requirements
- __xpc_connection_set_lwcr_requirements.cold.1
- __xpc_connection_token_satisfies_lwcr
- __xpc_connection_token_satisfies_lwcr.cold.1
- __xpc_make_serialization_with_ool_impl.cold.2
- __xpc_remote_received_message_init
- __xpc_session_cancel_with_code
- __xpc_string_create
- _launch_active_user_switch
- _sprintf
- _xpc_connection_set_peer_lightweight_code_requirement.cold.1
CStrings:
+ "\t\"%s\" => %zu\n"
+ "%s.%p"
+ ", name = %s, count = %zu"
+ ", str = %s, len = %zu, string cache = %p"
+ "<%s: %p> { name = %s, mutgen = %llu, count = %zu, peak_count = %zu, "
+ "<%s: %p> { string cache = %p, length = %zu, contents = \""
+ "Attempting to create peer requirement with invalid type: %s"
+ "B24@?0^v8Q16"
+ "Cached XPC strings are immutable"
+ "Could not get bufsize for getpwnam_r(): %s"
+ "Could not get uid for user %s: %s"
+ "Disposing non-empty string cache"
+ "Encountered XPC object loop: %s"
+ "LWCR invalid: %s"
+ "LWCR requirement doesn't match: %s (%d)"
+ "Listener must be inactive to %s, but listener is %s"
+ "OS_xpc_peer_requirement"
+ "OS_xpc_string_cache"
+ "Remaining %d os_transaction + %d xpc_transaction_begin\n"
+ "Security policy issue"
+ "Session must be inactive to %s, but session is %s"
+ "Tried to serialize an object containing a cycle"
+ "Unable to convert LWCR dictionary to LWCR data"
+ "Unreasonably large name"
+ "[\"%s\"] -> %p"
+ "[%p] Dropping check-in message due to code signing requirement: %s"
+ "[%p] Received message forbidden due to code signing requirement: %s"
+ "[%zu] -> %p"
+ "archpref"
+ "com.apple.xpc.anonymous.%p"
+ "i24@?0r^v8r^v16"
+ "os_transaction: [%p] '%s', created %llu sec ago\n"
+ "service-ctl-reply-port"
+ "set incoming session handler"
+ "set peer requirement"
+ "string cache"
- ", str = %s, len = %lu"
- "0xdeadbeeff00dface"
- "<%s: %p> { length = %lu, contents = \""
- "Attempting to set LWCR with invalid type: %s"
- "Session must be inactive to %s, not %s"
- "[%p] Dropping check-in message due to code signing requirement: %d"
- "[%p] LWCR invalid: %s"
- "[%p] LWCR requirement doesn't match: %s"
- "[%p] Received message forbidden due to code signing requirement: %d"
- "[%p] Set peer lightweight code requirement on connection (%s): %s"
- "[%p] Set peer lightweight code requirement on connection: %s"
- "[%p] Unable to convert LWCR dictionary to LWCR data"
- "com.apple.xpc.anonymous.%s"

```
