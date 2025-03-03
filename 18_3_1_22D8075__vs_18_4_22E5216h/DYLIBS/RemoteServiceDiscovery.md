## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

```diff

-172.80.4.0.0
-  __TEXT.__text: 0xe118
-  __TEXT.__auth_stubs: 0xa50
+172.100.9.0.0
+  __TEXT.__text: 0xe1d0
+  __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_methlist: 0x36c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x127c
-  __TEXT.__gcc_except_tab: 0x3e4
-  __TEXT.__oslogstring: 0x1c7d
-  __TEXT.__unwind_info: 0x488
-  __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x971
-  __TEXT.__objc_methtype: 0x189
+  __TEXT.__cstring: 0x1299
+  __TEXT.__gcc_except_tab: 0x3bc
+  __TEXT.__oslogstring: 0x1c37
+  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__objc_classname: 0x99
+  __TEXT.__objc_methname: 0x94d
+  __TEXT.__objc_methtype: 0x169
   __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x598
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__objc_const: 0xb68
   __DATA.__objc_ivar: 0xbc
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 427
-  Symbols:   720
-  CStrings:  499
+  Functions: 433
+  Symbols:   725
+  CStrings:  496
 
Symbols:
+ _close_drop_optional_np
+ _dup
+ _xpc_file_transfer_create_with_fd
+ _xpc_file_transfer_write_to_fd
- __dispatch_source_type_read
- _dispatch_source_get_data
- _dispatch_source_get_handle
- _dispatch_source_set_cancel_handler
- _os_variant_is_darwinos
- _write
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
- "\x14"
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
