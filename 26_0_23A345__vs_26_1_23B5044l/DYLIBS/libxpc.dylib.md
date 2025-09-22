## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-3089.0.11.0.0
-  __TEXT.__text: 0x3c034
-  __TEXT.__auth_stubs: 0x1210
+3089.40.13.0.1
+  __TEXT.__text: 0x42244
+  __TEXT.__auth_stubs: 0x1220
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x7696
-  __TEXT.__oslogstring: 0x1668
+  __TEXT.__const: 0x630
+  __TEXT.__cstring: 0x773b
+  __TEXT.__oslogstring: 0x30b5
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1190
+  __TEXT.__unwind_info: 0x1258
   __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x1c50
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x1c30
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_nlclslist: 0xe8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x910
-  __AUTH_CONST.__const: 0x1b18
+  __AUTH_CONST.__auth_got: 0x918
+  __AUTH_CONST.__const: 0x1af8
   __AUTH_CONST.__objc_const: 0x2338
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0xba8

   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x118
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: FD0E3621-E113-3F18-9F29-529D3B568825
-  Functions: 1791
-  Symbols:   4488
-  CStrings:  1242
+  UUID: C7D28DD7-F5FB-3D59-861E-3379F2C5FA10
+  Functions: 1910
+  Symbols:   4536
+  CStrings:  1359
 
Symbols:
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ ____create_with_format_and_arguments_block_invoke.1
+ ____create_with_format_and_arguments_block_invoke.1.cold.1
+ ____create_with_format_and_arguments_block_invoke.10
+ ____create_with_format_and_arguments_block_invoke.10.cold.1
+ ____create_with_format_and_arguments_block_invoke.10.cold.2
+ ____create_with_format_and_arguments_block_invoke.14
+ ____create_with_format_and_arguments_block_invoke.37
+ ____create_with_format_and_arguments_block_invoke.4
+ ____create_with_format_and_arguments_block_invoke.44
+ ____create_with_format_and_arguments_block_invoke_2.18
+ ____create_with_format_and_arguments_block_invoke_2.40
+ ____create_with_format_and_arguments_block_invoke_2.40.cold.1
+ ____create_with_format_and_arguments_block_invoke_2.40.cold.2
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.15
+ ___block_descriptor_tmp.16
+ ___block_descriptor_tmp.3
+ ___block_descriptor_tmp.6
+ ___block_literal_global.116
+ ___block_literal_global.124
+ __os_crash_msg
+ __os_log_default
+ __os_log_send_and_compose_impl
+ __os_transaction_log_snapshot
+ __os_transaction_log_snapshot.cold.1
+ __xpc_allocate_buffer
+ _xpc_data_create.cold.1
- ____create_with_format_and_arguments_block_invoke.8
- ____create_with_format_and_arguments_block_invoke.8.cold.1
- ____create_with_format_and_arguments_block_invoke.8.cold.2
- ____create_with_format_and_arguments_block_invoke_11
- ____create_with_format_and_arguments_block_invoke_12
- ____create_with_format_and_arguments_block_invoke_13
- ____create_with_format_and_arguments_block_invoke_13.cold.1
- ____create_with_format_and_arguments_block_invoke_13.cold.2
- ____create_with_format_and_arguments_block_invoke_14
- ____create_with_format_and_arguments_block_invoke_2.12
- ____create_with_format_and_arguments_block_invoke_2.cold.1
- ____create_with_format_and_arguments_block_invoke_3.16
- ____create_with_format_and_arguments_block_invoke_4.18
- ____xpc_is_being_debugged_block_invoke
- ___block_descriptor_tmp.112
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.2
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.41
- ___block_descriptor_tmp.5
- ___block_literal_global.114
- __os_assert_log
- __os_transaction_log_active.cold.1
- __xpc_is_being_debugged.cold.1
- __xpc_is_being_debugged.pred
- _xpc_bundle_copy_resource_path
- _xpc_event_stream_check_in
- _xpc_event_stream_check_in2
CStrings:
+ "Given object not of required type. Given: %s, required: %s"
+ "Reply messages must not be sent as notifications; use xpc_dictionary_send_reply()"
+ "assertion failure: \"!_xpc_activity_is_unmanaged()\" -> %llu"
+ "assertion failure: \"!globals->remote_hooks\" -> %llu"
+ "assertion failure: \"!unmanaged\" -> %llu"
+ "assertion failure: \"!xgd->_key_string_cache\" -> %llu"
+ "assertion failure: \"!xgd->_ool_callback\" -> %llu"
+ "assertion failure: \"!xgd->_value_string_cache\" -> %llu"
+ "assertion failure: \"!xrm->_conn\" -> %llu"
+ "assertion failure: \"((&activity->eligibility_changed_handlers)->lh_first == ((void*)0))\" -> %llu"
+ "assertion failure: \"((((struct _xpc_base_s *)(self))->_xo_flags & (((xpc_flags_t)(1U << 0)))) != 0)\" -> %llu"
+ "assertion failure: \"(((port) != 0) && ((port) != ((mach_port_name_t) ~0)))\" -> %llu"
+ "assertion failure: \"((void*)0) == reply\" -> %llu"
+ "assertion failure: \"(*__error()) != 0\" -> %llu"
+ "assertion failure: \"(*__error()) != 9\" -> %llu"
+ "assertion failure: \"(*__error())\" -> %llu"
+ "assertion failure: \"(bool)strchr(\"])\", format[foi])\" -> %llu"
+ "assertion failure: \"__builtin___strlcpy_chk (new_buffer, sb->buffer, new, __builtin_object_size (new_buffer, 2 > 1 ? 1 : 0)) < new\" -> %llu"
+ "assertion failure: \"_xpc_activity_is_unmanaged()\" -> %llu"
+ "assertion failure: \"_xpc_mach_port_close_recv(port, 0, ((void*)0))\" -> %llu"
+ "assertion failure: \"_xpc_message_request_expects_reply(xmrq)\" -> %llu"
+ "assertion failure: \"_xpc_message_request_get_transport(xmrq) == XMSG_TRANSPORT_REMOTE\" -> %llu"
+ "assertion failure: \"binprefs\" -> %llu"
+ "assertion failure: \"bs_type\" -> %llu"
+ "assertion failure: \"cb != ((void*)0)\" -> %llu"
+ "assertion failure: \"change_fdguard_np(fd, ((void*)0), 0, &guard, guard_flags, &fd_flags)\" -> %{errno}d"
+ "assertion failure: \"checkin->recvp.disposition == 16\" -> %llu"
+ "assertion failure: \"connection == activity->reply_connection\" -> %llu"
+ "assertion failure: \"count_is_odd == 0\" -> %llu"
+ "assertion failure: \"dbuff\" -> %llu"
+ "assertion failure: \"dictionary\" -> %llu"
+ "assertion failure: \"entry != ((void*)0)\" -> %llu"
+ "assertion failure: \"entry->num_inflight_msg >= count\" -> %llu"
+ "assertion failure: \"error != ((void*)0)\" -> %llu"
+ "assertion failure: \"error == 0 && (((reply_port) != 0) && ((reply_port) != ((mach_port_name_t) ~0)))\" -> %llu"
+ "assertion failure: \"error\" -> %llu"
+ "assertion failure: \"event\" -> %llu"
+ "assertion failure: \"existing == self\" -> %llu"
+ "assertion failure: \"flat != ((void*)0) || dispatch_data_get_size(self->_ddata) == 0\" -> %llu"
+ "assertion failure: \"format[foi] == '}'\" -> %llu"
+ "assertion failure: \"format[foi] == delimiter\" -> %llu"
+ "assertion failure: \"got_data\" -> %llu"
+ "assertion failure: \"guarded_close_np(fd, &guard)\" -> %{errno}d"
+ "assertion failure: \"hard_limit > 2\" -> %llu"
+ "assertion failure: \"hooks->extension.cls\" -> %llu"
+ "assertion failure: \"hooks->extension.xet\" -> %llu"
+ "assertion failure: \"hooks->msg_dispose\" -> %llu"
+ "assertion failure: \"hooks->send_reply\" -> %llu"
+ "assertion failure: \"hooks->size == sizeof(*hooks)\" -> %llu"
+ "assertion failure: \"i < self->xb_count\" -> %llu"
+ "assertion failure: \"i <= os_transaction_count\" -> %llu"
+ "assertion failure: \"idx < self->count\" -> %llu"
+ "assertion failure: \"initial_state != ((void*)0)\" -> %llu"
+ "assertion failure: \"initial_state == XL_STATE_NEW\" -> %llu"
+ "assertion failure: \"io\" -> %llu"
+ "assertion failure: \"kr\" -> %llu"
+ "assertion failure: \"label != ((void*)0)\" -> %llu"
+ "assertion failure: \"matched == (match_result.error_code == AICMR_MATCH)\" -> %llu"
+ "assertion failure: \"msgid_lo & (~0x00ffffffu)\" -> %llu"
+ "assertion failure: \"name\" -> %llu"
+ "assertion failure: \"needed\" -> %llu"
+ "assertion failure: \"new >= sb->size * 2\" -> %llu"
+ "assertion failure: \"object\" -> %llu"
+ "assertion failure: \"olddepth <= xgd->_depth\" -> %llu"
+ "assertion failure: \"packed == _xpc_spawnattr_binprefs_size(binprefs)\" -> %llu"
+ "assertion failure: \"payload\" -> %llu"
+ "assertion failure: \"platform != _XPC_PLATFORM_DATA\" -> %llu"
+ "assertion failure: \"platform < _XPC_PLATFORM_COUNT\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setarchpref_np(psattr, self->xb_count, self->xb_cpu_types, self->xb_cpu_subtypes, ((void*)0))\" -> %llu"
+ "assertion failure: \"pthread_key_create(&_mig_tsd, ((void*)0))\" -> %llu"
+ "assertion failure: \"q != ((void*)0)\" -> %llu"
+ "assertion failure: \"rc\" -> %{errno}d"
+ "assertion failure: \"reply\" -> %llu"
+ "assertion failure: \"ret == 0 && own_path_len != 0\" -> %llu"
+ "assertion failure: \"rr == XPC_RECEIVE_RESULT_DICTIONARY\" -> %llu"
+ "assertion failure: \"sb->length < sb->size\" -> %llu"
+ "assertion failure: \"self->_dmsg != 0\" -> %llu"
+ "assertion failure: \"self->_graph_destructor == 0\" -> %llu"
+ "assertion failure: \"self->_len > 0\" -> %llu"
+ "assertion failure: \"self->_sent != 0\" -> %llu"
+ "assertion failure: \"self->_state == XC_STATE_CANCELED\" -> %llu"
+ "assertion failure: \"self->_state == XL_STATE_CANCELED\" -> %llu"
+ "assertion failure: \"self->_state == XS_STATE_CANCELED\" -> %llu"
+ "assertion failure: \"self->_state == XS_STATE_NEW\" -> %llu"
+ "assertion failure: \"self->_subtype == XPC_DICTIONARY_SUBTYPE_RECEIVED\" -> %llu"
+ "assertion failure: \"self->_sync != 0\" -> %llu"
+ "assertion failure: \"self->_wants_sigterm != 0\" -> %llu"
+ "assertion failure: \"self->_xo_xrefcnt == 1\" -> %llu"
+ "assertion failure: \"self->count < self->max_capacity\" -> %llu"
+ "assertion failure: \"self->file_transfer_id != 0\" -> %llu"
+ "assertion failure: \"self->state != XPC_FILE_TRANSFER_STATE_IN_PROGRESS\" -> %llu"
+ "assertion failure: \"self->state == XPC_FILE_TRANSFER_STATE_INIT\" -> %llu"
+ "assertion failure: \"self->state == XPC_FILE_TRANSFER_STATE_IN_PROGRESS\" -> %llu"
+ "assertion failure: \"self->transaction != ((void*)0)\" -> %llu"
+ "assertion failure: \"self->transport_cancel_writing == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->transport_start_writing == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->xep_state == XPC_EVENT_PUBLISHER_CANCELLED\" -> %llu"
+ "assertion failure: \"self->xep_state == XPC_EVENT_PUBLISHER_INACTIVE\" -> %llu"
+ "assertion failure: \"self->xep_token_cache\" -> %llu"
+ "assertion failure: \"serializer->_graph_destructor == &_xpc_serializer_free\" -> %llu"
+ "assertion failure: \"serializer->_ool_serialize_callback != ((void*)0)\" -> %llu"
+ "assertion failure: \"size > 0\" -> %llu"
+ "assertion failure: \"speclen > 0\" -> %llu"
+ "assertion failure: \"src->_depth == 0\" -> %llu"
+ "assertion failure: \"stats_out != ((void*)0)\" -> %llu"
+ "assertion failure: \"success\" -> %llu"
+ "assertion failure: \"token != 0\" -> %llu"
+ "assertion failure: \"unmanaged\" -> %llu"
+ "assertion failure: \"variant != XPC_BUNDLE_VARIANT_NONE\" -> %llu"
+ "assertion failure: \"xhandle != ((void*)0)\" -> %llu"
+ "assertion failure: \"xmrq\" -> %llu"
+ "assertion failure: \"xmrq->_transport == XMSG_TRANSPORT_MACH\" -> %llu"
+ "assertion failure: \"xmrq->_transport == XMSG_TRANSPORT_REMOTE\" -> %llu"
+ "assertion failure: \"xp->_subtype == XPLD_TRANSPORT_MACH\" -> %llu"
+ "assertion failure: \"xpc_data_get_bytes_ptr_and_length(lwcr_data, &lwcr_bytes, &lwcr_size)\" -> %llu"
+ "assertion failure: \"xpc_dictionary_get_count(self->properties)\" -> %llu"
+ "assertion failure: \"xpc_get_type(subs) == (&_xpc_type_array)\" -> %llu"
+ "on activation of exit_when_clean"
- "%s/%s.%s"

```
