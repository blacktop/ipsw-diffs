## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-3102.120.13.0.0
-  __TEXT.__text: 0xe9a8
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x2ac
+3295.0.0.502.1
+  __TEXT.__text: 0xdf3c
+  __TEXT.__objc_methlist: 0x27c
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__cstring: 0xb27
+  __TEXT.__gcc_except_tab: 0x234
+  __TEXT.__cstring: 0xb89
   __TEXT.__oslogstring: 0x27c5
-  __TEXT.__unwind_info: 0x438
-  __TEXT.__objc_classname: 0xdf
-  __TEXT.__objc_methname: 0x79e
-  __TEXT.__objc_methtype: 0x28d
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x758
+  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x708
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x500
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__objc_const: 0xf88
-  __DATA.__objc_ivar: 0x12c
+  __AUTH_CONST.__objc_const: 0xf28
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x124
   __DATA.__data: 0xc8
-  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0xe0
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x50
   __CTF.__ctf: 0x338
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0D7A8AF2-25A3-377D-846D-5DFB6121044E
-  Functions: 371
-  Symbols:   1185
-  CStrings:  456
+  UUID: 3E48DBB8-0D56-384B-9B35-11CEFA0C294B
+  Functions: 168
+  Symbols:   698
+  CStrings:  285
 
Symbols:
+ -[OS_xpc_remote_connection setTls_options:]
+ -[OS_xpc_remote_connection tls_options]
+ GCC_except_table119
+ GCC_except_table54
+ GCC_except_table83
+ GCC_except_table95
+ _OBJC_IVAR_$_OS_xpc_remote_connection._tls_options
+ __MergedGlobals
+ __MergedGlobals.1
+ ___Block_byref_object_copy_.240
+ ___Block_byref_object_dispose_.241
+ ____xpc_remote_channel_enqueue_rx_block_invoke.48
+ ____xpc_remote_channel_enqueue_tx_block_invoke.45
+ ____xpc_remote_connection_handle_new_channel_block_invoke.227
+ ____xpc_remote_connection_handle_new_channel_block_invoke.228
+ ____xpc_remote_connection_handle_read_block_invoke.237
+ ____xpc_remote_connection_listen_block_invoke.201
+ ____xpc_remote_connection_open_stream_block_invoke.242
+ ____xpc_remote_connection_ready_block_invoke.232
+ ____xpc_remote_connection_ready_block_invoke.233
+ ____xpc_remote_connection_setup_nw_listener_block_invoke.223
+ ___block_literal_global.194
+ ___block_literal_global.197
+ ___block_literal_global.205
+ ___block_literal_global.220
+ ___xpc_remote_channel_attach_stream_block_invoke.34
+ ___xpc_remote_channel_create_block_invoke.21
+ ___xpc_remote_channel_create_block_invoke.23
+ ___xpc_remote_channel_create_block_invoke.29
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$setTls_options:
+ _objc_msgSend$tls_options
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x6
+ _xpc_remote_connection_set_tls_options
- -[OS_xpc_remote_connection setTls_identity:]
- -[OS_xpc_remote_connection setTls_verify:]
- -[OS_xpc_remote_connection setTls_verify_queue:]
- -[OS_xpc_remote_connection tls_identity]
- -[OS_xpc_remote_connection tls_verify]
- -[OS_xpc_remote_connection tls_verify_queue]
- -[OS_xpc_remote_listener dealloc].cold.1
- GCC_except_table122
- GCC_except_table188
- GCC_except_table189
- GCC_except_table190
- GCC_except_table193
- GCC_except_table194
- GCC_except_table195
- GCC_except_table196
- GCC_except_table257
- GCC_except_table53
- GCC_except_table86
- GCC_except_table98
- _OBJC_IVAR_$_OS_xpc_remote_connection._tls_identity
- _OBJC_IVAR_$_OS_xpc_remote_connection._tls_verify
- _OBJC_IVAR_$_OS_xpc_remote_connection._tls_verify_queue
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- ___Block_byref_object_copy_.250
- ___Block_byref_object_dispose_.251
- ____recv_file_transfer_block_invoke_2.cold.1
- ____recv_file_transfer_block_invoke_2.cold.2
- ____recv_file_transfer_block_invoke_5.cold.1
- ____xpc_remote_channel_enqueue_rx_block_invoke.49
- ____xpc_remote_channel_enqueue_rx_block_invoke.49.cold.1
- ____xpc_remote_channel_enqueue_rx_block_invoke.49.cold.2
- ____xpc_remote_channel_enqueue_rx_block_invoke.cold.1
- ____xpc_remote_channel_enqueue_rx_block_invoke.cold.2
- ____xpc_remote_channel_enqueue_rx_block_invoke.cold.3
- ____xpc_remote_channel_enqueue_tx_block_invoke.46.cold.1
- ____xpc_remote_channel_enqueue_tx_block_invoke.47
- ____xpc_remote_channel_enqueue_tx_block_invoke.47.cold.1
- ____xpc_remote_channel_enqueue_tx_block_invoke.47.cold.2
- ____xpc_remote_channel_enqueue_tx_block_invoke.cold.1
- ____xpc_remote_channel_enqueue_tx_block_invoke.cold.2
- ____xpc_remote_channel_enqueue_tx_block_invoke.cold.3
- ____xpc_remote_channel_header_handler_block_invoke.cold.1
- ____xpc_remote_channel_header_handler_block_invoke.cold.2
- ____xpc_remote_channel_header_handler_block_invoke.cold.3
- ____xpc_remote_connection_connect_complete_block_invoke.cold.1
- ____xpc_remote_connection_connect_complete_block_invoke.cold.2
- ____xpc_remote_connection_connect_complete_block_invoke.cold.3
- ____xpc_remote_connection_connect_complete_block_invoke.cold.4
- ____xpc_remote_connection_handle_new_channel_block_invoke.237
- ____xpc_remote_connection_handle_new_channel_block_invoke.237.cold.1
- ____xpc_remote_connection_handle_new_channel_block_invoke.237.cold.2
- ____xpc_remote_connection_handle_new_channel_block_invoke.237.cold.3
- ____xpc_remote_connection_handle_new_channel_block_invoke.237.cold.4
- ____xpc_remote_connection_handle_new_channel_block_invoke.237.cold.5
- ____xpc_remote_connection_handle_new_channel_block_invoke.237.cold.6
- ____xpc_remote_connection_handle_new_channel_block_invoke.238
- ____xpc_remote_connection_handle_new_channel_block_invoke.238.cold.1
- ____xpc_remote_connection_handle_new_channel_block_invoke.cold.1
- ____xpc_remote_connection_handle_new_channel_block_invoke.cold.2
- ____xpc_remote_connection_handle_read_block_invoke.247
- ____xpc_remote_connection_handle_read_block_invoke.cold.1
- ____xpc_remote_connection_handle_read_block_invoke_3.cold.1
- ____xpc_remote_connection_listen_block_invoke.211
- ____xpc_remote_connection_listen_block_invoke.cold.1
- ____xpc_remote_connection_listen_block_invoke.cold.2
- ____xpc_remote_connection_listen_block_invoke.cold.3
- ____xpc_remote_connection_listen_block_invoke.cold.4
- ____xpc_remote_connection_open_stream_block_invoke.252
- ____xpc_remote_connection_ready_block_invoke.242
- ____xpc_remote_connection_ready_block_invoke.242.cold.1
- ____xpc_remote_connection_ready_block_invoke.243
- ____xpc_remote_connection_ready_block_invoke.cold.1
- ____xpc_remote_connection_ready_block_invoke_2.cold.1
- ____xpc_remote_connection_send_reply_message_block_invoke.cold.1
- ____xpc_remote_connection_send_reply_message_block_invoke.cold.2
- ____xpc_remote_connection_setup_nw_listener_block_invoke.233
- ____xpc_remote_connection_setup_nw_listener_block_invoke.cold.1
- ____xpc_remote_connection_wakeup_block_invoke.cold.1
- ____xpc_remote_connection_wakeup_block_invoke.cold.2
- ____xpc_remote_message_create_block_invoke.cold.1
- ____xpc_remote_message_create_block_invoke.cold.2
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_literal_global.204
- ___block_literal_global.207
- ___block_literal_global.215
- ___block_literal_global.230
- ___xpc_remote_channel_arm_read_block_invoke.cold.1
- ___xpc_remote_channel_arm_read_block_invoke.cold.2
- ___xpc_remote_channel_arm_read_block_invoke.cold.3
- ___xpc_remote_channel_arm_read_block_invoke.cold.4
- ___xpc_remote_channel_arm_read_block_invoke.cold.5
- ___xpc_remote_channel_attach_stream_block_invoke.35
- ___xpc_remote_channel_attach_stream_block_invoke.35.cold.1
- ___xpc_remote_channel_create_block_invoke.22
- ___xpc_remote_channel_create_block_invoke.22.cold.1
- ___xpc_remote_channel_create_block_invoke.22.cold.2
- ___xpc_remote_channel_create_block_invoke.22.cold.3
- ___xpc_remote_channel_create_block_invoke.22.cold.4
- ___xpc_remote_channel_create_block_invoke.24.cold.1
- ___xpc_remote_channel_create_block_invoke.25.cold.1
- ___xpc_remote_channel_create_block_invoke.27
- ___xpc_remote_channel_create_block_invoke.30
- ___xpc_remote_channel_create_block_invoke.30.cold.1
- ___xpc_remote_channel_create_block_invoke.30.cold.2
- ___xpc_remote_channel_create_block_invoke.cold.1
- ___xpc_remote_channel_create_block_invoke.cold.2
- ___xpc_remote_channel_create_block_invoke.cold.3
- ___xpc_remote_channel_create_block_invoke.cold.4
- ___xpc_remote_channel_create_block_invoke.cold.5
- ___xpc_remote_channel_send_block_invoke.cold.1
- ___xpc_remote_connection_activate_block_invoke.cold.1
- ___xpc_remote_connection_activate_block_invoke.cold.2
- ___xpc_remote_connection_activate_block_invoke.cold.3
- ___xpc_remote_connection_message_dispose_block_invoke.cold.1
- ___xpc_remote_connection_message_dispose_block_invoke.cold.2
- ___xpc_remote_connection_send_barrier_block_invoke.cold.1
- ___xpc_remote_connection_send_barrier_block_invoke.cold.2
- ___xpc_remote_connection_send_message_block_invoke.cold.1
- ___xpc_remote_connection_send_message_block_invoke.cold.2
- ___xpc_remote_connection_send_message_block_invoke.cold.3
- ___xpc_remote_connection_send_message_with_reply_block_invoke.cold.1
- ___xpc_remote_connection_send_message_with_reply_block_invoke.cold.2
- ___xpc_remote_connection_send_message_with_reply_block_invoke.cold.3
- ___xpc_remote_connection_send_message_with_reply_sync_block_invoke.cold.1
- ___xpc_remote_connection_set_local_service_version_block_invoke.cold.1
- ___xpc_remote_connection_teardown.cold.1
- ___xpc_remote_connection_teardown_continue.cold.1
- ___xpc_remote_connection_teardown_continue.cold.2
- ___xpc_remote_connection_teardown_continue.cold.3
- __log.cold.1
- __log.logger
- __log.onceToken
- __xpc_extension_type_remote_connection
- __xpc_remote_channel_deliver_message.cold.1
- __xpc_remote_channel_enqueue_rx.cold.1
- __xpc_remote_channel_enqueue_tx.cold.1
- __xpc_remote_channel_send_stream_header.cold.1
- __xpc_remote_channel_send_stream_header.cold.2
- __xpc_remote_connection_alloc.cold.1
- __xpc_remote_connection_connect.cold.1
- __xpc_remote_connection_connect_complete.cold.1
- __xpc_remote_connection_connect_complete.cold.10
- __xpc_remote_connection_connect_complete.cold.11
- __xpc_remote_connection_connect_complete.cold.12
- __xpc_remote_connection_connect_complete.cold.2
- __xpc_remote_connection_connect_complete.cold.3
- __xpc_remote_connection_connect_complete.cold.4
- __xpc_remote_connection_connect_complete.cold.5
- __xpc_remote_connection_connect_complete.cold.6
- __xpc_remote_connection_connect_complete.cold.7
- __xpc_remote_connection_connect_complete.cold.8
- __xpc_remote_connection_connect_complete.cold.9
- __xpc_remote_connection_connect_doa.cold.1
- __xpc_remote_connection_connect_doa.cold.2
- __xpc_remote_connection_connect_doa.cold.3
- __xpc_remote_connection_connect_doa.cold.4
- __xpc_remote_connection_connect_failed.cold.1
- __xpc_remote_connection_connect_failed.cold.2
- __xpc_remote_connection_connect_failed.cold.3
- __xpc_remote_connection_connect_failed.cold.4
- __xpc_remote_connection_connect_failed.cold.5
- __xpc_remote_connection_create_nw_parameters.cold.1
- __xpc_remote_connection_flush.cold.1
- __xpc_remote_connection_handle_read.cold.1
- __xpc_remote_connection_handle_read.cold.10
- __xpc_remote_connection_handle_read.cold.11
- __xpc_remote_connection_handle_read.cold.12
- __xpc_remote_connection_handle_read.cold.13
- __xpc_remote_connection_handle_read.cold.14
- __xpc_remote_connection_handle_read.cold.15
- __xpc_remote_connection_handle_read.cold.2
- __xpc_remote_connection_handle_read.cold.3
- __xpc_remote_connection_handle_read.cold.4
- __xpc_remote_connection_handle_read.cold.5
- __xpc_remote_connection_handle_read.cold.6
- __xpc_remote_connection_handle_read.cold.7
- __xpc_remote_connection_handle_read.cold.8
- __xpc_remote_connection_handle_read.cold.9
- __xpc_remote_connection_parse_flags.cold.1
- __xpc_remote_connection_parse_mode_flags.cold.1
- __xpc_remote_connection_send_ool_message_content.cold.1
- __xpc_remote_connection_send_ool_message_content.cold.2
- __xpc_remote_connection_send_reply_message.cold.1
- __xpc_remote_connection_set_nw_context.context
- __xpc_remote_connection_set_nw_context.onceToken
- __xpc_remote_connection_wakeup.cold.1
- __xpc_remote_connection_wakeup.cold.2
- __xpc_remote_connection_wakeup.cold.3
- __xpc_remote_message_create.cold.1
- __xpc_remote_message_create.cold.2
- __xpc_remote_pending_stream_find.cold.1
- __xpc_remote_stream_remove.cold.1
- _hooks
- _objc_msgSend$setTls_identity:
- _objc_msgSend$setTls_verify:
- _objc_msgSend$setTls_verify_queue:
- _objc_msgSend$tls_identity
- _objc_msgSend$tls_verify
- _objc_msgSend$tls_verify_queue
- _xpc_remote_channel_arm_read.cold.1
- _xpc_remote_channel_arm_read.cold.2
- _xpc_remote_channel_arm_read.cold.3
- _xpc_remote_channel_attach_stream.cold.1
- _xpc_remote_channel_attach_stream.cold.2
- _xpc_remote_channel_attach_stream.cold.3
- _xpc_remote_channel_attach_stream.cold.4
- _xpc_remote_channel_attach_stream.cold.5
- _xpc_remote_channel_attach_stream.cold.6
- _xpc_remote_channel_attach_stream.cold.7
- _xpc_remote_channel_cancel.cold.1
- _xpc_remote_channel_cancel.cold.2
- _xpc_remote_channel_cancel.cold.3
- _xpc_remote_channel_create.cold.1
- _xpc_remote_connection_copy_remote_address_string.cold.1
- _xpc_remote_connection_copy_remote_endpoint.cold.1
- _xpc_remote_connection_create_remote_service_listener.cold.1
- _xpc_remote_connection_create_with_remote_service.cold.1
- _xpc_remote_connection_create_with_remote_service.cold.2
- _xpc_remote_connection_create_with_remote_service.cold.3
- _xpc_remote_connection_get_remote_service_version.cold.1
- _xpc_remote_connection_is_server.cold.1
- _xpc_remote_connection_send_message.cold.1
- _xpc_remote_connection_send_message_with_reply.cold.1
- _xpc_remote_connection_send_message_with_reply_sync.cold.1
- _xpc_remote_connection_send_message_with_reply_sync.cold.2
- _xpc_remote_connection_send_message_with_reply_sync.cold.3
- _xpc_remote_connection_send_message_with_reply_sync.cold.4
- _xpc_remote_connection_send_reply.cold.1
- _xpc_remote_connection_set_event_handler.cold.1
- _xpc_remote_connection_set_local_service_version.cold.1
- _xpc_remote_connection_set_target_queue.cold.1
- _xpc_remote_connection_set_tls.cold.1
- _xpc_remote_connection_set_tls.cold.2
- _xpc_remote_connection_set_tls.cold.3
- _xpc_remote_connection_set_traffic_class.cold.1
- _xpc_remote_connection_setup_nw_parameters.cold.1
- _xpc_remote_connection_setup_nw_parameters.cold.2
- _xpc_remote_listener_create_for_remote_service.cold.1
CStrings:
+ "BUG IN CLIENT OF RemoteXPC: Attempt to configure TLS with NULL options."
- "#16@0:8"
- "*"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_data>\""
- "@\"NSObject<OS_dispatch_io>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_nw_connection>\""
- "@\"NSObject<OS_nw_listener>\""
- "@\"NSObject<OS_sec_identity>\""
- "@\"NSString\"16@0:8"
- "@\"OS_remote_service\""
- "@\"OS_xpc_remote_channel\""
- "@\"OS_xpc_remote_listener\""
- "@\"OS_xpc_remote_message\""
- "@\"OS_xpc_remote_outstanding_reply\""
- "@\"OS_xpc_remote_pending_stream\""
- "@\"OS_xpc_remote_stream\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "C"
- "I"
- "NSObject"
- "OS_xpc_object"
- "OS_xpc_remote_channel"
- "OS_xpc_remote_connection"
- "OS_xpc_remote_listener"
- "OS_xpc_remote_message"
- "OS_xpc_remote_outstanding_reply"
- "OS_xpc_remote_pending_stream"
- "OS_xpc_remote_stream"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internal_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_target_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_tls_verify_queue"
- "T@\"NSObject<OS_sec_identity>\",&,N,V_tls_identity"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"OS_xpc_remote_listener\",&,N,V_listener"
- "T@?,C,N,V_event_handler"
- "T@?,C,N,V_tls_verify"
- "TB,N,V_send_in_progress"
- "TQ,R"
- "Ti,N,V_type"
- "Ti,V_state"
- "Vv16@0:8"
- "[16@\"NSObject<OS_xpc_object>\"]"
- "^{_NSZone=}16@0:8"
- "_event_handler"
- "_internal_queue"
- "_listener"
- "_send_in_progress"
- "_state"
- "_target_queue"
- "_tls_identity"
- "_tls_verify"
- "_tls_verify_queue"
- "_type"
- "accept_handler"
- "autorelease"
- "barrier"
- "body"
- "cancel_handler"
- "class"
- "completion_handler"
- "conformsToProtocol:"
- "conn"
- "copy"
- "dealloc"
- "debugDescription"
- "description"
- "direction"
- "disable_adaptive_write_timeout"
- "error"
- "event_handler"
- "first_msg_id"
- "hash"
- "i"
- "i16@0:8"
- "internal_queue"
- "io"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "link_stqe_next"
- "local_service_version"
- "msg_handler"
- "msg_id"
- "msgq_stqh_first"
- "msgq_stqh_last"
- "next_msg_id"
- "ool"
- "ool_length"
- "outstanding_replies_stqh_first"
- "outstanding_replies_stqh_last"
- "parent_io"
- "pending_streams_stqh_first"
- "pending_streams_stqh_last"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preexisting_connection"
- "preexisting_socket"
- "protocol_feature_flags"
- "protocol_version_number"
- "queue"
- "release"
- "remote_service"
- "remote_service_name"
- "remote_service_version"
- "reply_channel"
- "reply_channel_helo_received"
- "reply_handler"
- "reply_queue"
- "requires_nw_listener_create_workaround"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "root_channel"
- "root_channel_helo_received"
- "root_connection"
- "root_listener"
- "self"
- "send_in_progress"
- "server_mode"
- "setEvent_handler:"
- "setInternal_queue:"
- "setListener:"
- "setSend_in_progress:"
- "setState:"
- "setTarget_queue:"
- "setTls_identity:"
- "setTls_verify:"
- "setTls_verify_queue:"
- "setType:"
- "state"
- "stream_direction"
- "stream_id"
- "stream_io"
- "streams_stqh_first"
- "streams_stqh_last"
- "superclass"
- "target_queue"
- "tls_identity"
- "tls_verify"
- "tls_verify_queue"
- "traffic_class"
- "tx_complete"
- "type"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "wants_reply"
- "wire_version"
- "zone"

```
