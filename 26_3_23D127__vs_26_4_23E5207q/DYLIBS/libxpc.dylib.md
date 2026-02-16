## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-3089.82.3.0.0
-  __TEXT.__text: 0x42420
+3102.100.97.502.1
+  __TEXT.__text: 0x41944
   __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0x630
-  __TEXT.__cstring: 0x79f7
-  __TEXT.__oslogstring: 0x30ec
+  __TEXT.__const: 0x600
+  __TEXT.__cstring: 0x7b6e
+  __TEXT.__oslogstring: 0x30c4
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1260
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x1c30
+  __DATA_CONST.__const: 0x1c10
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_nlclslist: 0xe8
   __DATA_CONST.__objc_protolist: 0xf8

   __AUTH.__objc_data: 0x50
   __DATA.__data: 0xcf8
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x8
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x118
+  __DATA_DIRTY.__bss: 0x130
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 26E3F9D7-75BB-3384-A2BF-2628F1DBB2BC
-  Functions: 1913
-  Symbols:   4543
-  CStrings:  1369
+  UUID: 731970E2-842D-3CF9-BCA0-76AEE5CEAC6C
+  Functions: 1935
+  Symbols:   4630
+  CStrings:  1379
 
Symbols:
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __MergedGlobals
+ ___block_descriptor_tmp.126
+ ___block_descriptor_tmp.34
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.8
+ ___block_literal_global.128
+ __copy_key_from_plist
+ __copy_path_in_shared_cache
+ __current_dyld_version.0
+ __current_dyld_version.1
+ __current_version
+ __os_log_debug_impl
+ __os_system_version_initialize
+ __os_transaction_xref_dispose.cold.1
+ __os_transaction_xref_dispose.cold.2
+ __sim_current_host_version
+ __xpc_connection_copy_attrs.cold.1
+ __xpc_connection_derive_connection_port
+ __xpc_connection_derive_connection_port.cold.1
+ __xpc_connection_derive_connection_port.cold.2
+ __xpc_connection_derive_connection_port.cold.3
+ __xpc_connection_init_recv_port
+ __xpc_pipe_derive_port
+ __xpc_pipe_derive_port.cold.1
+ __xpc_pipe_derive_port.cold.2
+ __xpc_session_dispose.cold.3
+ __xpc_session_dispose.cold.4
+ __xpc_session_fault
+ _launch_get_user_context
+ _os_transaction_create.cold.1
+ _os_transaction_create.cold.2
+ _xpc_service_set_attach_handler.cold.2
+ _xpc_service_set_attach_handler.cold.3
- ____xpc_session_setup_connection_handlers_block_invoke.cold.8
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.46
- ___block_literal_global.123
- ___block_literal_global.131
- __availability_version_check.cold.1
- __launchd_service_instance_create_request.cold.1
- __os_once
- __system_version_copy_string_plist
- __system_version_copy_string_sysctl
- __system_version_fallback
- __system_version_parse_string
- __system_version_plist_path
- __xpc_assert_dumping_ground
- __xpc_connection_init_send_port.cold.1
- __xpc_connection_init_send_port.cold.2
- __xpc_connection_init_send_port.cold.3
- __xpc_endpoint_create_bs.cold.1
- __xpc_endpoint_create_bs.cold.2
- __xpc_listener_activate.cold.3
- __xpc_plist_parse_date
- __xpc_session_log_handle._log
- __xpc_session_log_handle._once
- _current_host_version
- _current_version
- _der_vm_CEType_from_ccder_tag
- _os_system_version_get_current_version.cold.1
- _os_system_version_get_current_version.predicate
- _os_system_version_sim_get_current_host_version.cold.1
- _os_system_version_sim_get_current_host_version.predicate
- _parsed_host_version
- _parsed_version
- _populate_current_host_version
- _populate_current_version
CStrings:
+ "%s%s"
+ "Attempted to serialize xpc_data that is too large for what the wire protocol currently supports. Length was %zu and max supported is %u"
+ "Could not get attrs using %s for connection %s, pid %d: %d: %s"
+ "Kernel bug: Unexpected error from pipe mach_port_construct()"
+ "Kernel bug: Unexpected error from service attach port mach_port_construct()"
+ "Tried to create an XPC data with NULL bytes and %zu length"
+ "[%p] '%s': Transaction created"
+ "[%p] '%s': Transaction released"
+ "assertion failure: \"c_block\" -> %llu"
+ "assertion failure: \"m_block\" -> %llu"
+ "bssendp"
+ "exception"
+ "loginwindow"
+ "mach port"
+ "nil"
+ "pid domain"
+ "token.pid"
- "Peer rejected"
- "The executable did not ship in the bundle"
- "Underlying connection invalidated"
- "assertion failure: \"bs_type\" -> %llu"
- "assertion failure: \"initial_state != ((void*)0)\" -> %llu"
- "assertion failure: \"label != ((void*)0)\" -> %llu"
- "assertion failure: \"name\" -> %llu"

```
