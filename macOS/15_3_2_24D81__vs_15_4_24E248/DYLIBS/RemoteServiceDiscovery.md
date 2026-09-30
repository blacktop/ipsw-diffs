## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery`

```diff

-172.80.4.0.0
-  __TEXT.__text: 0xee88
+172.100.9.0.0
+  __TEXT.__text: 0xef00
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_methlist: 0x36c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x127c
-  __TEXT.__gcc_except_tab: 0x3e4
-  __TEXT.__oslogstring: 0x1c02
-  __TEXT.__unwind_info: 0x4c8
-  __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x971
-  __TEXT.__objc_methtype: 0x189
+  __TEXT.__cstring: 0x1299
+  __TEXT.__gcc_except_tab: 0x3bc
+  __TEXT.__oslogstring: 0x1bbc
+  __TEXT.__unwind_info: 0x508
+  __TEXT.__objc_classname: 0x99
+  __TEXT.__objc_methname: 0x94d
+  __TEXT.__objc_methtype: 0x169
   __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x458
-  __AUTH_CONST.__const: 0x760
+  __AUTH_CONST.__const: 0x7e0
   __AUTH_CONST.__objc_const: 0xb68
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0xbc
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 028A0BE1-7F77-3015-9278-767DCCA157F6
-  Functions: 443
-  Symbols:   924
-  CStrings:  493
+  UUID: 216444AA-0412-3775-9131-7861CB643C14
+  Functions: 449
+  Symbols:   935
+  CStrings:  491
 
Symbols:
+ -[SocketRemoteXpcProxy clientSock]
+ -[SocketRemoteXpcProxy serverSock]
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table113
+ GCC_except_table133
+ GCC_except_table137
+ GCC_except_table142
+ GCC_except_table178
+ GCC_except_table214
+ GCC_except_table216
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table35
+ GCC_except_table382
+ GCC_except_table4
+ GCC_except_table78
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table95
+ GCC_except_table98
+ OBJC_IVAR_$_SocketRemoteXpcProxy._clientSock
+ OBJC_IVAR_$_SocketRemoteXpcProxy._serverSock
+ __32-[SocketRemoteXpcProxy activate]_block_invoke.2
+ __32-[SocketRemoteXpcProxy activate]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e8_v12?0i8l
+ ___block_descriptor_52_e8_32s40r_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___proxy_log_block_invoke
+ ___remote_device_start_browsing_block_invoke.397
+ ___remote_device_start_browsing_block_invoke.397.cold.1
+ ___remote_service_accept_block_invoke.402
+ ___remote_service_connect_socket_impl_block_invoke.361
+ ___remote_service_connect_socket_impl_block_invoke.362
+ __block_literal_global.261
+ __block_literal_global.292
+ __block_literal_global.297
+ __block_literal_global.300
+ __block_literal_global.303
+ __block_literal_global.306
+ __block_literal_global.309
+ __block_literal_global.312
+ __block_literal_global.316
+ __block_literal_global.373
+ __block_literal_global.376
+ __block_literal_global.379
+ __block_literal_global.399
+ __block_literal_global.407
+ __remote_device_create_from_client_description_block_invoke.383
+ __remote_device_start_browsing_matching_block_invoke.230
+ __remote_device_start_browsing_matching_block_invoke.230.cold.1
+ __remote_device_start_browsing_matching_block_invoke.230.cold.2
+ __remote_device_start_browsing_matching_block_invoke.230.cold.3
+ __remote_service_listen_with_device_block_invoke.267
+ _close_drop_optional_np
+ _dup
+ _objc_msgSend$clientSock
+ _objc_msgSend$serverSock
+ _proxy_log
+ _xpc_file_transfer_create_with_fd
+ _xpc_file_transfer_write_to_fd
+ proxy_log._log
+ proxy_log.cold.1
+ proxy_log.once
+ remote_service_listen_with_device.cold.1
+ remoted_conn.cold.1
+ remoted_queue.cold.1
+ rsd_log.cold.1
- -[SocketRemoteXpcProxy proxyClient]
- -[SocketRemoteXpcProxy proxyServer]
- GCC_except_table10
- GCC_except_table103
- GCC_except_table105
- GCC_except_table107
- GCC_except_table109
- GCC_except_table111
- GCC_except_table114
- GCC_except_table117
- GCC_except_table119
- GCC_except_table131
- GCC_except_table15
- GCC_except_table151
- GCC_except_table155
- GCC_except_table160
- GCC_except_table196
- GCC_except_table27
- GCC_except_table396
- GCC_except_table46
- GCC_except_table56
- GCC_except_table7
- GCC_except_table8
- GCC_except_table97
- GCC_except_table99
- OBJC_IVAR_$_SocketRemoteXpcProxy._proxyClient
- OBJC_IVAR_$_SocketRemoteXpcProxy._proxyServer
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- __32-[SocketRemoteXpcProxy activate]_block_invoke.11
- ___remote_device_start_browsing_block_invoke.435
- ___remote_device_start_browsing_block_invoke.435.cold.1
- ___remote_service_accept_block_invoke.440
- ___remote_service_connect_socket_impl_block_invoke.401
- ___remote_service_connect_socket_impl_block_invoke.402
- __block_literal_global.304
- __block_literal_global.335
- __block_literal_global.340
- __block_literal_global.349
- __block_literal_global.352
- __block_literal_global.355
- __block_literal_global.359
- __block_literal_global.383
- __block_literal_global.387
- __block_literal_global.413
- __block_literal_global.416
- __block_literal_global.419
- __block_literal_global.437
- __block_literal_global.445
- __dispatch_source_type_read
- __remote_device_create_from_client_description_block_invoke.423
- __remote_device_start_browsing_matching_block_invoke.274
- __remote_device_start_browsing_matching_block_invoke.274.cold.1
- __remote_device_start_browsing_matching_block_invoke.274.cold.2
- __remote_device_start_browsing_matching_block_invoke.274.cold.3
- __remote_service_listen_with_device_block_invoke.310
- _dispatch_source_get_data
- _dispatch_source_get_handle
- _dispatch_source_set_cancel_handler
- _objc_msgSend$proxyClient
- _objc_msgSend$proxyServer
- _write
- remote_device_type_is_trusted.cold.2
CStrings:
+ "Got unexpected RemoteXPC message"
+ "Ti,R,N,V_clientSock"
+ "Ti,R,N,V_serverSock"
+ "_clientSock"
+ "_serverSock"
+ "assertion failure: \"_uuid != ((void*)0)\" -> %llu"
+ "assertion failure: \"connect_errno != 0\" -> %llu"
+ "assertion failure: \"connect_errno == 0\" -> %llu"
+ "assertion failure: \"d1 == ((void*)0)\" -> %llu"
+ "assertion failure: \"device != ((void*)0)\" -> %llu"
+ "assertion failure: \"device_desc != ((void*)0)\" -> %llu"
+ "assertion failure: \"device_name != ((void*)0)\" -> %llu"
+ "assertion failure: \"endpoint != ((void*)0)\" -> %llu"
+ "assertion failure: \"fd != -1\" -> %llu"
+ "assertion failure: \"heartbeat_queue\" -> %llu"
+ "assertion failure: \"local_device_desc != ((void*)0)\" -> %llu"
+ "assertion failure: \"local_device_service_names != ((void*)0)\" -> %llu"
+ "assertion failure: \"message != ((void *)0)\" -> %llu"
+ "assertion failure: \"name\" -> %llu"
+ "assertion failure: \"new_state == REMOTE_DEVICE_STATE_CONNECTED || new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %llu"
+ "assertion failure: \"new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %llu"
+ "assertion failure: \"reply != ((void *)0)\" -> %llu"
+ "assertion failure: \"self->connection != ((void*)0)\" -> %llu"
+ "assertion failure: \"self->device != ((void*)0)\" -> %llu"
+ "assertion failure: \"self->device_name != ((void*)0)\" -> %llu"
+ "assertion failure: \"self.device_id != 0\" -> %llu"
+ "assertion failure: \"self.device_id == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_id\")\" -> %llu"
+ "assertion failure: \"self.type != 0\" -> %llu"
+ "assertion failure: \"self.type == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_type\")\" -> %llu"
+ "assertion failure: \"sema\" -> %llu"
+ "assertion failure: \"service_desc != ((void*)0)\" -> %llu"
+ "assertion failure: \"services != ((void*)0)\" -> %llu"
+ "assertion failure: \"srv_conn != ((void*)0)\" -> %llu"
+ "assertion failure: \"xpc_get_type(msg) == (&_xpc_type_dictionary)\" -> %llu"
+ "assertion failure: \"xpc_get_type(srv->properties) == (&_xpc_type_dictionary)\" -> %llu"
+ "clientSock"
+ "serverSock"
+ "socket"
+ "v12@?0i8"
+ "write RemoteXPC to socket ended: %{darwin.errno}d"
+ "write socket to RemoteXPC ended: %{darwin.errno}d"
- "@\"NSObject<OS_dispatch_source>\""
- "Cancel socket proxy"
- "Client closed their socket"
- "OK"
- "Proxying %zu bytes from RemoteXPC to socket"
- "Proxying %zu bytes from socket over RemoteXPC"
- "T@\"NSObject<OS_dispatch_source>\",R,N,V_proxyServer"
- "Ti,R,N,V_proxyClient"
- "_proxyClient"
- "_proxyServer"
- "assertion failure: \"_uuid != ((void *)0)\" -> %lld"
- "assertion failure: \"connect_errno != 0\" -> %lld"
- "assertion failure: \"connect_errno == 0\" -> %lld"
- "assertion failure: \"d1 == ((void *)0)\" -> %lld"
- "assertion failure: \"device != ((void *)0)\" -> %lld"
- "assertion failure: \"device_desc != ((void *)0)\" -> %lld"
- "assertion failure: \"device_name != ((void *)0)\" -> %lld"
- "assertion failure: \"endpoint != ((void *)0)\" -> %lld"
- "assertion failure: \"fd != -1\" -> %lld"
- "assertion failure: \"heartbeat_queue\" -> %lld"
- "assertion failure: \"local_device_desc != ((void *)0)\" -> %lld"
- "assertion failure: \"local_device_service_names != ((void *)0)\" -> %lld"
- "assertion failure: \"message != ((void *)0)\" -> %lld"
- "assertion failure: \"name\" -> %lld"
- "assertion failure: \"new_state == REMOTE_DEVICE_STATE_CONNECTED || new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %lld"
- "assertion failure: \"new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %lld"
- "assertion failure: \"reply != ((void *)0)\" -> %lld"
- "assertion failure: \"self->connection != ((void *)0)\" -> %lld"
- "assertion failure: \"self->device != ((void *)0)\" -> %lld"
- "assertion failure: \"self->device_name != ((void *)0)\" -> %lld"
- "assertion failure: \"self.device_id != 0\" -> %lld"
- "assertion failure: \"self.device_id == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_id\")\" -> %lld"
- "assertion failure: \"self.type != 0\" -> %lld"
- "assertion failure: \"self.type == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_type\")\" -> %lld"
- "assertion failure: \"sema\" -> %lld"
- "assertion failure: \"service_desc != ((void *)0)\" -> %lld"
- "assertion failure: \"services != ((void *)0)\" -> %lld"
- "assertion failure: \"srv_conn != ((void *)0)\" -> %lld"
- "assertion failure: \"xpc_get_type(msg) == (&_xpc_type_dictionary)\" -> %lld"
- "assertion failure: \"xpc_get_type(srv->properties) == (&_xpc_type_dictionary)\" -> %lld"
- "proxyClient"
- "proxyServer"
- "unhandled type in remote_device_type_is_trusted: %d"

```
