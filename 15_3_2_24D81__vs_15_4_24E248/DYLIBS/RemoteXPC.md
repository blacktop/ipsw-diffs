## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/Versions/A/RemoteXPC`

```diff

-2866.81.1.0.0
-  __TEXT.__text: 0x107b8
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x1a4
+2894.101.1.0.0
+  __TEXT.__text: 0x107f8
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x318
-  __TEXT.__cstring: 0xb0a
-  __TEXT.__oslogstring: 0x2744
-  __TEXT.__unwind_info: 0x440
+  __TEXT.__cstring: 0xb27
+  __TEXT.__oslogstring: 0x2722
+  __TEXT.__unwind_info: 0x478
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methname: 0x79e
   __TEXT.__objc_methtype: 0x28d

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__objc_const: 0x1178
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__objc_const: 0xf88
   __AUTH.__objc_data: 0x230
   __AUTH.__data: 0xe0
   __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0xc8
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x50
   __CTF.__ctf: 0x338
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC05FC36-81B1-3E8B-898D-4030FDF8D6DC
-  Functions: 373
-  Symbols:   781
+  UUID: B9EF1F2C-2BB5-3FE1-BC09-9F2D26289BBB
+  Functions: 377
+  Symbols:   792
   CStrings:  453
 
Symbols:
+ GCC_except_table112
+ GCC_except_table138
+ GCC_except_table211
+ GCC_except_table275
+ __Block_byref_object_copy_.286
+ __Block_byref_object_dispose_.287
+ ____xpc_remote_connection_set_nw_context_block_invoke
+ ___recv_file_transfer_block_invoke.295
+ ___recv_file_transfer_block_invoke_2.296
+ ___recv_file_transfer_block_invoke_2.296.cold.1
+ ___xpc_remote_connection_handle_new_channel_block_invoke.257
+ ___xpc_remote_connection_handle_new_channel_block_invoke.257.cold.1
+ ___xpc_remote_connection_handle_new_channel_block_invoke.257.cold.2
+ ___xpc_remote_connection_handle_new_channel_block_invoke.257.cold.3
+ ___xpc_remote_connection_handle_new_channel_block_invoke.257.cold.4
+ ___xpc_remote_connection_handle_new_channel_block_invoke.257.cold.5
+ ___xpc_remote_connection_handle_new_channel_block_invoke.257.cold.6
+ ___xpc_remote_connection_handle_new_channel_block_invoke.258
+ ___xpc_remote_connection_handle_new_channel_block_invoke.258.cold.1
+ ___xpc_remote_connection_handle_read_block_invoke.275
+ ___xpc_remote_connection_open_stream_block_invoke.290
+ ___xpc_remote_connection_ready_block_invoke.266.cold.1
+ ___xpc_remote_connection_ready_block_invoke.269
+ ___xpc_remote_connection_setup_nw_listener_block_invoke.251
+ __block_literal_global.246
+ _dispatch_queue_get_qos_class
+ _log.cold.1
+ _nw_context_create
+ _nw_context_set_isolate_protocol_stack
+ _nw_context_set_scheduling_mode
+ _nw_parameters_set_context
+ _xpc_remote_connection_alloc.cold.1
+ _xpc_remote_connection_create_nw_parameters.cold.1
+ _xpc_remote_connection_set_nw_context.context
+ _xpc_remote_connection_set_nw_context.onceToken
+ xpc_remote_connection_setup_nw_parameters.cold.2
+ xpc_remote_listener_create_for_remote_service.cold.1
- GCC_except_table111
- GCC_except_table137
- GCC_except_table202
- GCC_except_table270
- _OUTLINED_FUNCTION_23
- __Block_byref_object_copy_.283
- __Block_byref_object_dispose_.284
- ___recv_file_transfer_block_invoke.292
- ___recv_file_transfer_block_invoke_2.293
- ___recv_file_transfer_block_invoke_2.293.cold.1
- ___xpc_remote_connection_handle_new_channel_block_invoke.254
- ___xpc_remote_connection_handle_new_channel_block_invoke.254.cold.1
- ___xpc_remote_connection_handle_new_channel_block_invoke.254.cold.2
- ___xpc_remote_connection_handle_new_channel_block_invoke.254.cold.3
- ___xpc_remote_connection_handle_new_channel_block_invoke.254.cold.4
- ___xpc_remote_connection_handle_new_channel_block_invoke.254.cold.5
- ___xpc_remote_connection_handle_new_channel_block_invoke.254.cold.6
- ___xpc_remote_connection_handle_new_channel_block_invoke.255
- ___xpc_remote_connection_handle_new_channel_block_invoke.255.cold.1
- ___xpc_remote_connection_handle_read_block_invoke.272
- ___xpc_remote_connection_open_stream_block_invoke.287
- ___xpc_remote_connection_ready_block_invoke.263
- ___xpc_remote_connection_ready_block_invoke.263.cold.1
- ___xpc_remote_connection_setup_nw_listener_block_invoke.248
- __xpc_remote_connection_teardown.cold.3
CStrings:
+ "assertion failure: \"((self)->pending_streams_stqh_first == ((void*)0))\" -> %llu"
+ "assertion failure: \"_next\" -> %llu"
+ "assertion failure: \"_xpc_dictionary_get_reply_msg_id(message) == 0\" -> %llu"
+ "assertion failure: \"body_buf != ((void*)0) && body_len > 0\" -> %llu"
+ "assertion failure: \"canceled\" -> %llu"
+ "assertion failure: \"channel != ((void*)0)\" -> %llu"
+ "assertion failure: \"device != ((void*)0)\" -> %llu"
+ "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_DUPLEX\" -> %llu"
+ "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %llu"
+ "assertion failure: \"done\" -> %llu"
+ "assertion failure: \"fd != -1\" -> %llu"
+ "assertion failure: \"fd == -1\" -> %llu"
+ "assertion failure: \"h2_parameters\" -> %llu"
+ "assertion failure: \"msg_id != 0\" -> %llu"
+ "assertion failure: \"ps->direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_RX\" -> %llu"
+ "assertion failure: \"ps->direction == direction\" -> %llu"
+ "assertion failure: \"reply != ((void*)0)\" -> %llu"
+ "assertion failure: \"self\" -> %llu"
+ "assertion failure: \"self->root_channel == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->root_channel == channel\" -> %llu"
+ "assertion failure: \"self->root_connection == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->root_listener == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->state != XPC_REMOTE_CHANNEL_STATE_CANCELED\" -> %llu"
+ "assertion failure: \"self->state == XPC_REMOTE_CHANNEL_STATE_WAITING\" -> %llu"
+ "assertion failure: \"self->stream_direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %llu"
+ "assertion failure: \"self->stream_io != ((void*)0)\" -> %llu"
+ "assertion failure: \"self->type != XPC_REMOTE_LISTENER_TYPE_RSD\" -> %llu"
+ "assertion failure: \"self.state <= XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTING\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_INACTIVE\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_NOT_CONNECTED\" -> %llu"
+ "assertion failure: \"self.type != XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %llu"
+ "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %llu"
+ "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_RSD\" -> %llu"
+ "assertion failure: \"stream_id != 0\" -> %llu"
+ "remotexpc_realtime_messaging"
- "Invalid teardown type %d"
- "assertion failure: \"((self)->pending_streams_stqh_first == ((void *)0))\" -> %lld"
- "assertion failure: \"_next\" -> %lld"
- "assertion failure: \"_xpc_dictionary_get_reply_msg_id(message) == 0\" -> %lld"
- "assertion failure: \"body_buf != ((void *)0) && body_len > 0\" -> %lld"
- "assertion failure: \"canceled\" -> %lld"
- "assertion failure: \"channel != ((void *)0)\" -> %lld"
- "assertion failure: \"device != ((void *)0)\" -> %lld"
- "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_DUPLEX\" -> %lld"
- "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %lld"
- "assertion failure: \"done\" -> %lld"
- "assertion failure: \"fd != -1\" -> %lld"
- "assertion failure: \"fd == -1\" -> %lld"
- "assertion failure: \"h2_parameters\" -> %lld"
- "assertion failure: \"msg_id != 0\" -> %lld"
- "assertion failure: \"ps->direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_RX\" -> %lld"
- "assertion failure: \"ps->direction == direction\" -> %lld"
- "assertion failure: \"reply != ((void *)0)\" -> %lld"
- "assertion failure: \"self\" -> %lld"
- "assertion failure: \"self->root_channel == ((void *)0)\" -> %lld"
- "assertion failure: \"self->root_channel == channel\" -> %lld"
- "assertion failure: \"self->root_connection == ((void *)0)\" -> %lld"
- "assertion failure: \"self->root_listener == ((void *)0)\" -> %lld"
- "assertion failure: \"self->state != XPC_REMOTE_CHANNEL_STATE_CANCELED\" -> %lld"
- "assertion failure: \"self->state == XPC_REMOTE_CHANNEL_STATE_WAITING\" -> %lld"
- "assertion failure: \"self->stream_direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %lld"
- "assertion failure: \"self->stream_io != ((void *)0)\" -> %lld"
- "assertion failure: \"self->type != XPC_REMOTE_LISTENER_TYPE_RSD\" -> %lld"
- "assertion failure: \"self.state <= XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTING\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_INACTIVE\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_NOT_CONNECTED\" -> %lld"
- "assertion failure: \"self.type != XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %lld"
- "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %lld"
- "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_RSD\" -> %lld"
- "assertion failure: \"stream_id != 0\" -> %lld"

```
