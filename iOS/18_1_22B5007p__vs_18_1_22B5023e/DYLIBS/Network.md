## Network

> `/System/Library/Frameworks/Network.framework/Network`

```diff

-4277.0.121.0.0
-  __TEXT.__text: 0xc31118
-  __TEXT.__auth_stubs: 0x5c40
+4277.40.40.0.1
+  __TEXT.__text: 0xc5110c
+  __TEXT.__auth_stubs: 0x5c20
   __TEXT.__delay_stubs: 0x370
   __TEXT.__delay_helper: 0xb90
   __TEXT.__init_offsets: 0x5a8
   __TEXT.__objc_methlist: 0x788c
   __TEXT.__const: 0xcf250
-  __TEXT.__cstring: 0x5c57b
-  __TEXT.__swift5_typeref: 0x36c2
+  __TEXT.__cstring: 0x5c795
+  __TEXT.__swift5_typeref: 0x36c0
   __TEXT.__swift5_capture: 0x19d0
   __TEXT.__swift5_reflstr: 0x2408
   __TEXT.__swift5_assocty: 0x838

   __TEXT.__swift5_proto: 0x6ec
   __TEXT.__swift5_types: 0x440
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__oslogstring: 0x11ddd1
-  __TEXT.__gcc_except_tab: 0x8a214
-  __TEXT.__unwind_info: 0x18078
-  __TEXT.__eh_frame: 0x646c
+  __TEXT.__oslogstring: 0x11e983
+  __TEXT.__gcc_except_tab: 0x8a8e0
+  __TEXT.__unwind_info: 0x180e0
+  __TEXT.__eh_frame: 0x620c
   __TEXT.__objc_classname: 0x2307
-  __TEXT.__objc_methname: 0x13ca4
-  __TEXT.__objc_methtype: 0x8fd6
-  __TEXT.__objc_stubs: 0x99e0
+  __TEXT.__objc_methname: 0x13d70
+  __TEXT.__objc_methtype: 0x9004
+  __TEXT.__objc_stubs: 0x9a60
   __DATA_CONST.__got: 0xda0
-  __DATA_CONST.__const: 0x12580
+  __DATA_CONST.__const: 0x12620
   __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3480
+  __DATA_CONST.__objc_selrefs: 0x3498
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x6b8
-  __AUTH_CONST.__auth_got: 0x2ed8
-  __AUTH_CONST.__auth_ptr: 0x1020
+  __AUTH_CONST.__auth_got: 0x2ec8
+  __AUTH_CONST.__auth_ptr: 0xe98
   __AUTH_CONST.__const: 0xc798
-  __AUTH_CONST.__cfstring: 0x8060
-  __AUTH_CONST.__objc_const: 0x26958
+  __AUTH_CONST.__cfstring: 0x80a0
+  __AUTH_CONST.__objc_const: 0x26a58
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x3930
-  __AUTH.__data: 0x4bd8
-  __DATA.__objc_ivar: 0x25ec
-  __DATA.__data: 0x63b0
+  __AUTH.__objc_data: 0x38e0
+  __AUTH.__data: 0x4960
+  __DATA.__objc_ivar: 0x260c
+  __DATA.__data: 0x62f8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x107a0
+  __DATA.__bss: 0x107f0
   __DATA.__common: 0x2790
-  __DATA_DIRTY.__objc_data: 0x1040
-  __DATA_DIRTY.__data: 0xf8
-  __DATA_DIRTY.__bss: 0xc50
+  __DATA_DIRTY.__objc_data: 0x1090
+  __DATA_DIRTY.__data: 0x490
+  __DATA_DIRTY.__bss: 0xc90
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 21111
-  Symbols:   15177
-  CStrings:  32540
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 21149
+  Symbols:   15211
+  CStrings:  32604
 
Symbols:
+ _CFDictionaryGetCount
+ _CFDictionaryRemoveAllValues
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _network_config_get_tcp_l4s_enabled
+ _networkd_settings_get_bool_with_default
+ _nw_hash_table_create_no_lock
+ _nw_hash_table_create_with_lock
+ _nw_http_authentication_options_copy_appsso_h1_fallback_headers
+ _nw_http_authentication_options_set_appsso_h1_fallback_headers
+ _nw_http_authentication_options_set_h1_fallback_cache
+ _nw_setting_enable_tcp_l4s
+ _nw_setting_enable_tcp_l4s_denominator
+ _nw_setting_enable_tcp_l4s_numerator
- _nw_hash_table_create
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "\x03\x11\xf0\xf0\xf0\xf0\x1eR\x11at\x11\x11\x11&V"
+ "\x11\x17"
+ "!\x1e\x12"
+ "%!{(MISSING)public}s %!s(MISSING)ing TCP L4S"
+ "%!{(MISSING)public}s %!{(MISSING)public}s%!s(MISSING)ATS requires TLS but is not currently enforced"
+ "%!{(MISSING)public}s %!{(MISSING)public}s%!s(MISSING)Proxy credential was rejected, cancelling connection"
+ "%!{(MISSING)public}s %!{(MISSING)public}s%!s(MISSING)Reporting connected with protocol: %!p(MISSING), flow: %!l(MISSING)lx"
+ "%!{(MISSING)public}s Changing TCP L4S to %!l(MISSING)ld"
+ "%!{(MISSING)public}s Hash node state was %!{(MISSING)public}s, not pending_free"
+ "%!{(MISSING)public}s Invalid node state=%!{(MISSING)public}s, apply_count=%!d(MISSING)"
+ "%!{(MISSING)public}s Invalid node, state=%!{(MISSING)public}s, apply_count=%!d(MISSING)"
+ "%!{(MISSING)public}s Locking invalid hash table"
+ "%!{(MISSING)public}s Node that isn't in tailq, state=%!{(MISSING)public}s, apply_count=%!d(MISSING)"
+ "%!{(MISSING)public}s TCP L4S was set to: %!u(MISSING)"
+ "%!{(MISSING)public}s Tried to free hash node with apply_count %!d(MISSING)"
+ "%!{(MISSING)public}s Tried to free pending_free hash node that was not in list"
+ "%!{(MISSING)public}s Tried to remove invalid node, state: %!{(MISSING)public}s"
+ "%!{(MISSING)public}s [C%!u(MISSING)] create connection to connected fd %!{(MISSING)public}@"
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] Already servicing writes, ignoring..."
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] Attempted to register context with zombified multiplexed protocol %!p(MISSING)"
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] Attempted to register context with zombified multiplexed protocol %!p(MISSING), backtrace limit exceeded"
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] Attempted to register context with zombified multiplexed protocol %!p(MISSING), dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] Attempted to register context with zombified multiplexed protocol %!p(MISSING), no backtrace"
+ "%!{(MISSING)public}s allocated_input_frames should be empty on destroy, but has %!u(MISSING) frames"
+ "%!{(MISSING)public}s allocated_input_frames should be empty on destroy, but has %!u(MISSING) frames, backtrace limit exceeded"
+ "%!{(MISSING)public}s allocated_input_frames should be empty on destroy, but has %!u(MISSING) frames, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s allocated_input_frames should be empty on destroy, but has %!u(MISSING) frames, no backtrace"
+ "%!{(MISSING)public}s allocated_output_frames should be empty on destroy, but has %!u(MISSING) frames"
+ "%!{(MISSING)public}s allocated_output_frames should be empty on destroy, but has %!u(MISSING) frames, backtrace limit exceeded"
+ "%!{(MISSING)public}s allocated_output_frames should be empty on destroy, but has %!u(MISSING) frames, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s allocated_output_frames should be empty on destroy, but has %!u(MISSING) frames, no backtrace"
+ "%!{(MISSING)public}s attempt to relinquish guarded fd %!d(MISSING)"
+ "%!{(MISSING)public}s attempt to relinquish guarded fd %!d(MISSING), backtrace limit exceeded"
+ "%!{(MISSING)public}s attempt to relinquish guarded fd %!d(MISSING), dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s attempt to relinquish guarded fd %!d(MISSING), no backtrace"
+ "%!{(MISSING)public}s attempt to relinquish invalid fd %!d(MISSING)"
+ "%!{(MISSING)public}s attempt to relinquish invalid fd %!d(MISSING), backtrace limit exceeded"
+ "%!{(MISSING)public}s attempt to relinquish invalid fd %!d(MISSING), dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s attempt to relinquish invalid fd %!d(MISSING), no backtrace"
+ "%!{(MISSING)public}s called with null fd_wrapper"
+ "%!{(MISSING)public}s called with null fd_wrapper, backtrace limit exceeded"
+ "%!{(MISSING)public}s called with null fd_wrapper, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s called with null fd_wrapper, no backtrace"
+ "%!{(MISSING)public}s called with null h1_fallback_cache"
+ "%!{(MISSING)public}s called with null h1_fallback_cache, backtrace limit exceeded"
+ "%!{(MISSING)public}s called with null h1_fallback_cache, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s called with null h1_fallback_cache, no backtrace"
+ "%!{(MISSING)public}s enable TCP L4S sampled at: %!u(MISSING) / %!u(MISSING)"
+ "%!{(MISSING)public}s invalid pre_connected_fd: %!{(MISSING)public}@"
+ "%!{(MISSING)public}s invalid pre_connected_fd: %!{(MISSING)public}@, backtrace limit exceeded"
+ "%!{(MISSING)public}s invalid pre_connected_fd: %!{(MISSING)public}@, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s invalid pre_connected_fd: %!{(MISSING)public}@, no backtrace"
+ "%!{(MISSING)public}s nw_hash_table_create_no_lock failed"
+ "%!{(MISSING)public}s nw_hash_table_create_no_lock failed, backtrace limit exceeded"
+ "%!{(MISSING)public}s nw_hash_table_create_no_lock failed, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s nw_hash_table_create_no_lock failed, no backtrace"
+ "%!{(MISSING)public}s prohibit joining for connection to connected fd %!{(MISSING)public}@"
+ "%!{(MISSING)public}s table count %!d(MISSING) != 0"
+ "%!{(MISSING)public}s table count %!d(MISSING) != 0, backtrace limit exceeded"
+ "%!{(MISSING)public}s table count %!d(MISSING) != 0, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s table count %!d(MISSING) != 0, no backtrace"
+ "--"
+ "4277.40.40.0.1"
+ "6b\x15(#["
+ "@\"NSObject<OS_sec_trust>\""
+ "HTTPMaximumConnectionsPerHost"
+ "__nw_protocol_get_callbacks"
+ "__nw_protocol_get_handle"
+ "__nw_protocol_get_identifier"
+ "__nw_protocol_get_input_handler"
+ "__nw_protocol_get_output_handler"
+ "__nw_protocol_get_output_handler_context"
+ "__nw_protocol_set_callbacks"
+ "__nw_protocol_set_handle"
+ "__nw_protocol_set_identifier"
+ "__nw_protocol_set_output_handler_context"
+ "_appssoH1FallbackHeaders"
+ "_h1FallbackCache"
+ "_peerTrustInternal"
+ "_pendingErrorFromFailedConnection"
+ "deleteCharactersInRange:"
+ "do_not_guard"
+ "enable_tcp_l4s"
+ "enable_tcp_l4s_denominator"
+ "enable_tcp_l4s_numerator"
+ "freeing"
+ "has_nat64_prefixes"
+ "in_list"
+ "insertString:atIndex:"
+ "invalid_state"
+ "next_node->apply_count"
+ "nw_authentication_credential_cache_entry_get_type"
+ "nw_authentication_credential_cache_entry_set_type"
+ "nw_fd_wrapper_create_do_not_guard"
+ "nw_fd_wrapper_relinquish_fd"
+ "nw_hash_table_create_no_lock"
+ "nw_hash_table_create_with_lock"
+ "nw_hash_table_lock"
+ "nw_hash_table_remove_node_internal"
+ "nw_http_authentication_apply_appsso_headers"
+ "nw_http_authentication_options_copy_appsso_h1_fallback_headers"
+ "nw_http_authentication_options_copy_h1_fallback_cache"
+ "nw_http_authentication_options_set_appsso_h1_fallback_headers"
+ "nw_http_authentication_options_set_h1_fallback_cache"
+ "nw_http_authentication_set_version"
+ "nw_protocol_is_zombie"
+ "nw_resolver_derive_service_flags"
+ "pending_free"
+ "{nw_flow_protocol=\"protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"listen_protocol\"{nw_listen_protocol=\"callbacks\"^{nw_listen_protocol_callbacks}\"protocol_handler\"^{nw_protocol}\"protocol_handler_context\"^v\"handle\"^v}\"replay_protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"handler\"@\"NWConcrete_nw_endpoint_handler\"\"retained_flow\"@\"NWConcrete_nw_endpoint_flow\"\"parameters\"@\"NSObject<OS_nw_parameters>\"\"context\"@\"NSObject<OS_nw_context>\"\"write_requests\"@\"NSObject<OS_nw_write_request>\"\"initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"cloned_initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"read_requests\"@\"NSObject<OS_nw_read_request>\"\"last_output_context\"@\"NSObject<OS_nw_content_context>\"\"metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"input_metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"output_context\"@\"NSObject<OS_nw_content_context>\"\"input_contexts\"@\"NSObject<OS_nw_dictionary>\"\"single_input_context\"@\"NSObject<OS_nw_content_context>\"\"pending_input_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"candidate_output_handlers\"^{nw_hash_table}\"fast_open_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"final_read_list\"@\"NSObject<OS_nw_array>\"\"last_error\"@\"NSObject<OS_nw_error>\"\"fast_open_frame_finalized_count\"I\"initialized\"b1\"last_output_context_pending\"b1\"servicing_reads\"b1\"servicing_writes\"b1\"input_finished\"b1\"waiting_for_initial_read\"b1\"deferred_final_read\"b1\"delivered_final_read\"b1\"flow_unregistered\"b1\"flow_disconnected\"b1\"waiting_for_connected\"b1\"in_fast_open\"b1\"unused\"b4\"__pad\"[2C]}"
- "\x03\x11\xf0\xf0\xf0\xf0\x1eR\x11ad\x11\x11\x11&V"
- "\x11\x16"
- "!\x1e\x11"
- "%!{(MISSING)public}s Invalid node with an apply_count of 0"
- "%!{(MISSING)public}s Tried to free hash node that was not in list"
- "%!{(MISSING)public}s Tried to remove invalid node"
- "%!{(MISSING)public}s UDP listen socket recvmsg %!{(MISSING)darwin.errno}d, backtrace limit exceeded"
- "%!{(MISSING)public}s UDP listen socket recvmsg %!{(MISSING)darwin.errno}d, dumping backtrace:%!{(MISSING)public}s"
- "%!{(MISSING)public}s UDP listen socket recvmsg %!{(MISSING)darwin.errno}d, no backtrace"
- "%!{(MISSING)public}s [C%!u(MISSING)] create connection to connected fd %!d(MISSING)"
- "%!{(MISSING)public}s nw_hash_table_create failed"
- "%!{(MISSING)public}s nw_hash_table_create failed, backtrace limit exceeded"
- "%!{(MISSING)public}s nw_hash_table_create failed, dumping backtrace:%!{(MISSING)public}s"
- "%!{(MISSING)public}s nw_hash_table_create failed, no backtrace"
- "%!{(MISSING)public}s nw_protocol_socket_obj_alloc failed"
- "%!{(MISSING)public}s nw_protocol_socket_obj_alloc failed, backtrace limit exceeded"
- "%!{(MISSING)public}s nw_protocol_socket_obj_alloc failed, dumping backtrace:%!{(MISSING)public}s"
- "%!{(MISSING)public}s nw_protocol_socket_obj_alloc failed, no backtrace"
- "%!{(MISSING)public}s prohibit joining for connection to connected fd %!d(MISSING)"
- "%!{(MISSING)public}s protocol options are not http_sniffing"
- "%!{(MISSING)public}s protocol options are not http_sniffing, backtrace limit exceeded"
- "%!{(MISSING)public}s protocol options are not http_sniffing, dumping backtrace:%!{(MISSING)public}s"
- "%!{(MISSING)public}s protocol options are not http_sniffing, no backtrace"
- "--%!@(MISSING)"
- "4277.0.121"
- "4b\x15(#["
- "Multipart response, no part for body"
- "nw_hash_node_is_in_tailq"
- "nw_hash_table_create"
- "nw_http_sniffing_options_get_is_top_level_navigation"
- "nw_http_sniffing_options_set_is_top_level_navigation"
- "nw_protocol_get_callbacks"
- "nw_protocol_get_handle"
- "nw_protocol_get_identifier"
- "nw_protocol_get_name"
- "nw_protocol_get_output_handler_context"
- "nw_protocol_set_callbacks"
- "nw_protocol_set_handle"
- "nw_protocol_set_identifier"
- "nw_protocol_set_input_handler"
- "nw_protocol_set_output_handler"
- "nw_protocol_set_output_handler_context"
- "nw_protocol_socket_create"
- "temp_node->apply_count"
- "{nw_flow_protocol=\"protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"listen_protocol\"{nw_listen_protocol=\"callbacks\"^{nw_listen_protocol_callbacks}\"protocol_handler\"^{nw_protocol}\"protocol_handler_context\"^v\"handle\"^v}\"replay_protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"handler\"@\"NWConcrete_nw_endpoint_handler\"\"retained_flow\"@\"NWConcrete_nw_endpoint_flow\"\"parameters\"@\"NSObject<OS_nw_parameters>\"\"context\"@\"NSObject<OS_nw_context>\"\"write_requests\"@\"NSObject<OS_nw_write_request>\"\"initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"cloned_initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"read_requests\"@\"NSObject<OS_nw_read_request>\"\"last_output_context\"@\"NSObject<OS_nw_content_context>\"\"metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"input_metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"output_context\"@\"NSObject<OS_nw_content_context>\"\"input_contexts\"@\"NSObject<OS_nw_dictionary>\"\"single_input_context\"@\"NSObject<OS_nw_content_context>\"\"pending_input_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"candidate_output_handlers\"^{nw_hash_table}\"fast_open_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"final_read_list\"@\"NSObject<OS_nw_array>\"\"last_error\"@\"NSObject<OS_nw_error>\"\"fast_open_frame_finalized_count\"I\"initialized\"b1\"last_output_context_pending\"b1\"servicing_reads\"b1\"input_finished\"b1\"waiting_for_initial_read\"b1\"deferred_final_read\"b1\"delivered_final_read\"b1\"flow_unregistered\"b1\"flow_disconnected\"b1\"waiting_for_connected\"b1\"in_fast_open\"b1\"unused\"b5\"__pad\"[2C]}"

```
