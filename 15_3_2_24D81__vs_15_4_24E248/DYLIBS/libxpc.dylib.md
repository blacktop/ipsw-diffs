## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-2866.81.1.0.0
-  __TEXT.__text: 0x3c714
-  __TEXT.__auth_stubs: 0x11a0
+2894.101.1.0.0
+  __TEXT.__text: 0x3c544
+  __TEXT.__auth_stubs: 0x11b0
   __TEXT.__delay_stubs: 0xdc
   __TEXT.__delay_helper: 0x148
-  __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x650
-  __TEXT.__cstring: 0x7654
-  __TEXT.__oslogstring: 0x1709
+  __TEXT.__objc_methlist: 0x32c
+  __TEXT.__const: 0x640
+  __TEXT.__cstring: 0x787d
+  __TEXT.__oslogstring: 0x1759
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1298
+  __TEXT.__unwind_info: 0x1260
   __TEXT.__objc_classname: 0x217
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x1190
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x11a0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_nlclslist: 0xe0
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88
+  __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x900
-  __AUTH_CONST.__const: 0x2488
-  __AUTH_CONST.__objc_const: 0x2390
+  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__const: 0x2498
+  __AUTH_CONST.__objc_const: 0x21a0
   __DATA.__data: 0xb48
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x10
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x80

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 564B7785-E7C4-3231-8BF1-3FBB266B6599
-  Functions: 1724
-  Symbols:   2882
-  CStrings:  1234
+  UUID: C211DDEA-E3C5-351D-8619-900C01BEDFC9
+  Functions: 1745
+  Symbols:   3031
+  CStrings:  1258
 
Symbols:
+ _CEBuffer_cmp
+ ___assert_rtn
+ ___launch_domain_routine_async_block_invoke.50
+ ___launch_domain_routine_async_block_invoke.55
+ ___launch_domain_routine_async_block_invoke.55.cold.1
+ ___launch_service_monitor_removal_port_block_invoke.45
+ ___xpc_activity_dispatch_block_invoke.134.cold.6
+ ___xpc_activity_dispatch_block_invoke.134.cold.7
+ ___xpc_activity_dispatch_block_invoke.136.cold.1
+ ___xpc_activity_dispatch_block_invoke.cold.1
+ ___xpc_activity_dispatch_block_invoke.cold.2
+ ___xpc_activity_dispatch_block_invoke.cold.3
+ ___xpc_activity_dispatch_block_invoke.cold.4
+ ___xpc_activity_dispatch_block_invoke.cold.5
+ ___xpc_activity_dispatch_block_invoke.cold.6
+ ___xpc_activity_dispatch_block_invoke.cold.7
+ ___xpc_activity_set_state_with_completion_status_block_invoke.cold.1
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.10
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.11
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.2
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.3
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.4
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.5
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.6
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.7
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.8
+ ___xpc_listener_setup_connection_handlers_block_invoke.cold.9
+ ___xpc_runtime_get_self_entitlements_block_invoke.cold.1
+ ___xpc_session_setup_connection_handlers_block_invoke.cold.2
+ ___xpc_session_setup_connection_handlers_block_invoke.cold.3
+ ___xpc_session_setup_connection_handlers_block_invoke.cold.4
+ ___xpc_session_setup_connection_handlers_block_invoke.cold.5
+ ___xpc_session_setup_connection_handlers_block_invoke.cold.6
+ ___xpc_session_setup_connection_handlers_block_invoke.cold.7
+ ___xpc_session_setup_connection_handlers_block_invoke.cold.8
+ __block_descriptor_tmp.118
+ __block_descriptor_tmp.127
+ __block_literal_global.120
+ __block_literal_global.129
+ __rdar_128295526_error
+ __xpc_activity_register_block_invoke.cold.1
+ __xpc_activity_set_criteria_block_invoke.70.cold.1
+ __xpc_activity_set_criteria_block_invoke.70.cold.2
+ __xpc_activity_set_criteria_block_invoke.70.cold.3
+ __xpc_activity_set_criteria_block_invoke.cold.1
+ __xpc_activity_set_criteria_block_invoke.cold.2
+ __xpc_activity_set_criteria_block_invoke.cold.3
+ __xpc_activity_unregister.cold.1
+ __xpc_alloc_typed
+ __xpc_connection_evaluate_check_in
+ __xpc_connection_init_failed
+ __xpc_connection_validate_check_in_is_for_service
+ __xpc_realloc_typed
+ _der_decode_boolean
+ _der_decode_entitlements
+ _der_decode_number
+ _der_decode_numeric_string
+ _der_decode_string
+ _der_decode_utc_time
+ _der_validate_array
+ _der_vm_CEType_from_ccder_tag
+ _der_vm_execute_match_integer
+ _der_vm_execute_match_string_prefix
+ _fetch_xpcservice_info.cold.1
+ _launch_report_service_lookup.cold.1
+ _launch_urgent_log_submission_completed
+ _os_transaction_log_active.cold.1
+ _xpc_activity_create_control_channel.cold.1
+ _xpc_activity_create_control_channel.cold.2
+ _xpc_activity_dispose.cold.2
+ _xpc_activity_end_running.cold.1
+ _xpc_activity_set_criteria.cold.2
+ _xpc_activity_set_criteria.cold.3
+ _xpc_activity_set_state_from_cts.cold.1
+ _xpc_activity_set_state_with_completion_status.cold.1
+ _xpc_activity_unregister.cold.1
+ _xpc_add_bundle_with_lwcr
+ _xpc_alloc_typed.cold.1
+ _xpc_array_debug_desc.cold.1
+ _xpc_array_debug_desc.cold.2
+ _xpc_array_debug_desc.cold.3
+ _xpc_array_desc.cold.1
+ _xpc_array_serialize.cold.1
+ _xpc_base_debug.cold.1
+ _xpc_base_debug.cold.2
+ _xpc_base_debug_desc.cold.1
+ _xpc_base_desc.cold.1
+ _xpc_bundle_desc.cold.1
+ _xpc_connection_activate_if_needed.cold.1
+ _xpc_connection_activate_if_needed.cold.2
+ _xpc_connection_activate_if_needed.cold.3
+ _xpc_connection_activate_if_needed.cold.4
+ _xpc_connection_bs_seal_listener
+ _xpc_connection_check_peer_requirement.cold.1
+ _xpc_connection_check_peer_requirement.cold.2
+ _xpc_connection_copy_listener_port.cold.1
+ _xpc_connection_copy_listener_port.cold.2
+ _xpc_connection_copy_listener_port.cold.3
+ _xpc_connection_handle_sent_event.cold.3
+ _xpc_connection_init.cold.10
+ _xpc_connection_init.cold.11
+ _xpc_connection_init.cold.5
+ _xpc_connection_init.cold.6
+ _xpc_connection_init.cold.7
+ _xpc_connection_init.cold.8
+ _xpc_connection_init.cold.9
+ _xpc_connection_init_failed.cold.1
+ _xpc_connection_init_failed.cold.2
+ _xpc_connection_last_xref_cancel.cold.1
+ _xpc_connection_mach_event.cold.7
+ _xpc_connection_pass2mig.cold.1
+ _xpc_connection_set_event_handler_f.cold.1
+ _xpc_connection_set_lwcr.cold.1
+ _xpc_connection_set_lwcr.cold.2
+ _xpc_connection_set_lwcr_requirements.cold.1
+ _xpc_connection_unpack_message.cold.2
+ _xpc_connection_validate_check_in_is_for_service.cold.1
+ _xpc_dictionary_desc_apply.cold.1
+ _xpc_dictionary_desc_apply.cold.2
+ _xpc_dictionary_desc_apply.cold.3
+ _xpc_dictionary_serialize_apply.cold.1
+ _xpc_dyld_image_callback.cold.1
+ _xpc_file_transfer_serialize.cold.5
+ _xpc_get_extension_vtable.cold.1
+ _xpc_is_being_debugged.cold.1
+ _xpc_listener_activate.cold.2
+ _xpc_listener_activate.cold.3
+ _xpc_listener_dispose.cold.2
+ _xpc_make_serialization_with_ool_impl.cold.2
+ _xpc_realloc_typed.cold.1
+ _xpc_runtime_get_entitlements_data.cold.1
+ _xpc_runtime_get_self_entitlements.cold.1
+ _xpc_runtime_is_app_sandboxed.cold.1
+ _xpc_service_instance_set_use_sec_transition_shims
+ _xpc_session_activate_locked.cold.1
+ _xpc_session_cancel_with_reason.cold.1
+ _xpc_session_create_from_connection_4SWIFT.cold.1
+ _xpc_session_create_with_connection.cold.2
+ _xpc_session_dispose.cold.2
+ _xpc_shmem_create_with_prot.cold.1
+ do_mach_notify_no_senders.cold.1
+ do_mach_notify_port_destroyed.cold.1
+ launch_urgent_log_submission_completed.cold.1
+ os_system_version_get_current_version.cold.1
+ os_system_version_get_ios_support_version.cold.1
+ os_system_version_sim_get_current_host_version.cold.1
+ xpc_activity_register.cold.1
+ xpc_activity_register.cold.2
+ xpc_activity_set_criteria.cold.1
+ xpc_activity_unregister.cold.1
+ xpc_connection_bs_seal_listener.cold.1
+ xpc_connection_bs_seal_listener.cold.2
+ xpc_connection_bs_seal_listener.cold.3
+ xpc_connection_cancel.cold.1
+ xpc_connection_set_peer_lightweight_code_requirement.cold.1
+ xpc_listener_cancel.cold.1
+ xpc_listener_create.cold.1
+ xpc_listener_create_anonymous.cold.1
+ xpc_session_create_mach_service.cold.1
+ xpc_session_create_xpc_endpoint.cold.1
+ xpc_session_create_xpc_service.cold.1
- ___launch_domain_routine_async_block_invoke.48
- ___launch_domain_routine_async_block_invoke.53
- ___launch_domain_routine_async_block_invoke.53.cold.1
- ___launch_service_monitor_removal_port_block_invoke.43
- __block_descriptor_tmp.113
- __block_descriptor_tmp.27
- __block_literal_global.115
- __xpc_alloc
- __xpc_realloc
- _xpc_alloc.cold.1
- _xpc_realloc.cold.1
CStrings:
+ "!(consume_suspend_cnt && ready_only)"
+ "!(ready_only && (self->_type == XC_TYPE_PEER))"
+ "!ready_only"
+ "Couldn't retrieve XPCService dictionary from service bundle. Cause: %s"
+ "Entitlements element not allowed"
+ "Sealing is only possible for listeners."
+ "UTC Time element not allowed"
+ "Unknown DER entitlements encoding"
+ "Unknown UTC Time encoding"
+ "Unknown numeric string encoding"
+ "[%p] %{public}s connection: mach=%{bool}d listener=%{bool}d peer=%{bool}d name=%{public}s"
+ "[%p] %{public}s connection: name=%{public}s publishToken=%{public}llu"
+ "[%p] Sealing failed to init recv right."
+ "[%p] Sealing failed to make send right."
+ "_xpc_connection_activate_if_needed"
+ "_xpc_connection_init"
+ "activated"
+ "activating"
+ "connection.c"
+ "der_decode_entitlements"
+ "der_decode_numeric_string"
+ "der_decode_utc_time"
+ "init-ready"
+ "lwcr"
+ "numeric string element not allowed"
+ "pid-version"
+ "readying"
+ "readying error"
+ "xpc_connection_bs_seal_listener"
- "1"
- "Configuration error: Couldn't retrieve XPCService dictionary from service bundle."
- "[%p] activating connection: mach=%{bool}d listener=%{bool}d peer=%{bool}d name=%{public}s"
- "[%p] activating connection: name=%{public}s publishToken=%{public}llu"
- "])"

```
