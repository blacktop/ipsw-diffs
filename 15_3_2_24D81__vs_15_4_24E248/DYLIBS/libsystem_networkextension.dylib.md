## libsystem_networkextension.dylib

> `/usr/lib/system/libsystem_networkextension.dylib`

```diff

-2063.80.10.0.0
+2063.101.3.0.0
   __TEXT.__text: 0x153a0
-  __TEXT.__auth_stubs: 0x890
+  __TEXT.__auth_stubs: 0x8a0
   __TEXT.__const: 0x100
   __TEXT.__cstring: 0x17ee
   __TEXT.__oslogstring: 0x291a
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x388
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x650
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__const: 0x800
   __DATA.__data: 0x29
   __DATA.__bss: 0x6b8

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: CD0C82E0-9B1B-3CAA-8CA7-466D1C439C3B
-  Functions: 268
-  Symbols:   550
+  UUID: 66000862-B9D9-3940-8AB3-0FDB8F568572
+  Functions: 269
+  Symbols:   552
   CStrings:  508
 
Symbols:
+ _NEHelperGetPid
+ _xpc_connection_get_pid
Functions:
~ _ne_session_set_socket_attributes : 412 -> 416
~ _ne_log_obj : 68 -> 72
~ _set_status : 84 -> 88
~ _notify_client : 144 -> 148
~ _ne_session_release : 140 -> 144
~ ___ne_session_release_block_invoke : 160 -> 144
~ _ne_session_clear_event_handler : 160 -> 152
~ ___ne_session_clear_event_handler_block_invoke : 92 -> 96
~ ___ne_session_create_block_invoke : 392 -> 396
~ ___ne_session_get_info_with_parameters_block_invoke : 480 -> 484
~ ___ne_session_parse_necp_drop_dest_array_block_invoke : 2224 -> 2228
~ _necp_drop_dest_copy_dest_entry_list : 1504 -> 1496
~ _ne_session_create_xpc_string_from_necp_level : 116 -> 108
~ _nehelper_queue : 68 -> 72
~ _ne_session_address_matches_subnets : 632 -> 620
+ _ne_session_type_to_string
~ _ne_session_copy_socket_attributes : 504 -> 472
- _ne_session_type_to_string
~ _ne_session_policy_copy_flow_divert_token : 1032 -> 1036
~ _ne_session_policy_copy_flow_divert_token_with_key : 1152 -> 1156
~ _ne_session_validate_flow_properties : 800 -> 812
~ __get_flow_divert_token_from_session_manager_block_invoke.301 : 248 -> 240
~ _ne_session_copy_app_data_from_flow_divert_socket : 676 -> 672
~ _ne_copy_signing_identifier_for_pid_with_audit_token : 632 -> 644
~ _ne_session_copy_os_version_string : 696 -> 704
~ _ne_copy_cached_synthesized_uuids_for_bundle_identifier_locked : 320 -> 316
~ _ne_session_set_socket_tracker_attributes : 580 -> 588
~ _ne_session_copy_socket_domain_attributes : 856 -> 792
+ _NEHelperGetPid
~ _ne_tracker_build_cache : 1492 -> 1484
~ _ne_tracker_domain_is_known_tracker : 1060 -> 1052
~ _ne_socket_set_attribution : 680 -> 676
~ _ne_log_large_obj : 68 -> 72
~ _ne_trie_init : 2420 -> 2416
~ _ne_trie_free : 372 -> 376
~ _ne_trie_save_to_file : 488 -> 492
~ _ne_trie_init_from_file : 2024 -> 1984
~ _ne_trie_has_high_ascii : 92 -> 88
~ _ne_trie_insert : 2596 -> 2576
~ _ne_trie_search : 972 -> 968

```
