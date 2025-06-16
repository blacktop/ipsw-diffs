## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-2679.0.25.0.0
+2679.40.6.0.0
   __TEXT.__text: 0xf014
   __TEXT.__auth_stubs: 0x8e0
   __TEXT.__objc_methlist: 0x160

   __DATA_CONST.__objc_const: 0xed0
   __DATA_CONST.__objc_selrefs: 0x80
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x480
   __DATA.__objc_classrefs: 0x38
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x11c
   __DATA.__data: 0xc8
-  __DATA_DIRTY.__const: 0xc0
+  __DATA_DIRTY.__const: 0xa0
   __DATA_DIRTY.__objc_const: 0x1f8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47DFAE00-7670-36FA-8122-0F08FE5494E1
+  UUID: 2FECE7F0-10FE-3F63-B223-CD0A97F20D58
   Functions: 369
   Symbols:   1074
   CStrings:  439
Symbols:
+ ___Block_byref_object_copy_.224
+ ___Block_byref_object_dispose_.225
+ ____xpc_remote_channel_enqueue_rx_block_invoke.49
+ ____xpc_remote_channel_enqueue_rx_block_invoke.49.cold.1
+ ____xpc_remote_channel_enqueue_rx_block_invoke.49.cold.2
+ ____xpc_remote_channel_enqueue_tx_block_invoke.46
+ ____xpc_remote_channel_enqueue_tx_block_invoke.46.cold.1
+ ____xpc_remote_channel_enqueue_tx_block_invoke.47
+ ____xpc_remote_channel_enqueue_tx_block_invoke.47.cold.1
+ ____xpc_remote_channel_enqueue_tx_block_invoke.47.cold.2
+ ____xpc_remote_connection_handle_new_channel_block_invoke.211
+ ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.1
+ ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.2
+ ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.3
+ ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.4
+ ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.5
+ ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.6
+ ____xpc_remote_connection_handle_new_channel_block_invoke.212
+ ____xpc_remote_connection_handle_new_channel_block_invoke.212.cold.1
+ ____xpc_remote_connection_handle_read_block_invoke.221
+ ____xpc_remote_connection_listen_block_invoke.188
+ ____xpc_remote_connection_open_stream_block_invoke.226
+ ____xpc_remote_connection_ready_block_invoke.216
+ ____xpc_remote_connection_ready_block_invoke.216.cold.1
+ ____xpc_remote_connection_ready_block_invoke.217
+ ____xpc_remote_connection_setup_nw_listener_block_invoke.207
+ ___block_literal_global.192
+ ___xpc_remote_channel_attach_stream_block_invoke.35
+ ___xpc_remote_channel_attach_stream_block_invoke.35.cold.1
- ___Block_byref_object_copy_.231
- ___Block_byref_object_dispose_.232
- ____xpc_remote_channel_enqueue_rx_block_invoke.52
- ____xpc_remote_channel_enqueue_rx_block_invoke.52.cold.1
- ____xpc_remote_channel_enqueue_rx_block_invoke.52.cold.2
- ____xpc_remote_channel_enqueue_tx_block_invoke.49
- ____xpc_remote_channel_enqueue_tx_block_invoke.49.cold.1
- ____xpc_remote_channel_enqueue_tx_block_invoke.50
- ____xpc_remote_channel_enqueue_tx_block_invoke.50.cold.1
- ____xpc_remote_channel_enqueue_tx_block_invoke.50.cold.2
- ____xpc_remote_connection_handle_new_channel_block_invoke.217
- ____xpc_remote_connection_handle_new_channel_block_invoke.217.cold.1
- ____xpc_remote_connection_handle_new_channel_block_invoke.217.cold.2
- ____xpc_remote_connection_handle_new_channel_block_invoke.217.cold.3
- ____xpc_remote_connection_handle_new_channel_block_invoke.217.cold.4
- ____xpc_remote_connection_handle_new_channel_block_invoke.217.cold.5
- ____xpc_remote_connection_handle_new_channel_block_invoke.217.cold.6
- ____xpc_remote_connection_handle_new_channel_block_invoke.218
- ____xpc_remote_connection_handle_new_channel_block_invoke.218.cold.1
- ____xpc_remote_connection_handle_read_block_invoke.228
- ____xpc_remote_connection_listen_block_invoke.189
- ____xpc_remote_connection_open_stream_block_invoke.233
- ____xpc_remote_connection_ready_block_invoke.223
- ____xpc_remote_connection_ready_block_invoke.223.cold.1
- ____xpc_remote_connection_ready_block_invoke.224
- ____xpc_remote_connection_setup_nw_listener_block_invoke.213
- ___block_literal_global.193
- ___xpc_remote_channel_attach_stream_block_invoke.37
- ___xpc_remote_channel_attach_stream_block_invoke.37.cold.1

```
