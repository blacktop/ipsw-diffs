## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-2679.80.5.0.1
-  __TEXT.__text: 0xf014
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x160
+2748.102.2.0.0
+  __TEXT.__text: 0xf47c
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x1a8
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__cstring: 0x9d5
-  __TEXT.__oslogstring: 0x273a
-  __TEXT.__unwind_info: 0x38c
+  __TEXT.__cstring: 0xa6c
+  __TEXT.__oslogstring: 0x273b
+  __TEXT.__unwind_info: 0x39c
   __TEXT.__objc_classname: 0xdf
-  __TEXT.__objc_methname: 0x660
-  __TEXT.__objc_methtype: 0x270
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x708
+  __TEXT.__objc_methname: 0x79e
+  __TEXT.__objc_methtype: 0x28d
+  __TEXT.__objc_stubs: 0x280
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x730
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xed0
-  __DATA_CONST.__objc_selrefs: 0x80
+  __DATA_CONST.__objc_const: 0xf80
+  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_classrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x480
-  __DATA.__objc_classrefs: 0x38
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x11c
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x4e0
+  __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0xc8
-  __DATA_DIRTY.__const: 0xa0
+  __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__objc_const: 0x1f8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0xe0

   __CTF.__ctf: 0x338
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98A14B1B-A919-3161-B30F-FDE9E96E69AA
-  Functions: 369
-  Symbols:   1074
-  CStrings:  439
+  UUID: 508F5322-3C95-3873-8238-9D48A49B8F92
+  Functions: 382
+  Symbols:   1123
+  CStrings:  457
 
Symbols:
+ -[OS_xpc_remote_connection setTls_identity:]
+ -[OS_xpc_remote_connection setTls_verify:]
+ -[OS_xpc_remote_connection setTls_verify_queue:]
+ -[OS_xpc_remote_connection tls_identity]
+ -[OS_xpc_remote_connection tls_verify]
+ -[OS_xpc_remote_connection tls_verify_queue]
+ GCC_except_table120
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table52
+ GCC_except_table85
+ GCC_except_table96
+ _OBJC_IVAR_$_OS_xpc_remote_connection._tls_identity
+ _OBJC_IVAR_$_OS_xpc_remote_connection._tls_verify
+ _OBJC_IVAR_$_OS_xpc_remote_connection._tls_verify_queue
+ _OBJC_IVAR_$_OS_xpc_remote_connection.disable_adaptive_write_timeout
+ ___Block_byref_object_copy_.244
+ ___Block_byref_object_dispose_.245
+ ____xpc_remote_connection_handle_new_channel_block_invoke.231
+ ____xpc_remote_connection_handle_new_channel_block_invoke.231.cold.1
+ ____xpc_remote_connection_handle_new_channel_block_invoke.231.cold.2
+ ____xpc_remote_connection_handle_new_channel_block_invoke.231.cold.3
+ ____xpc_remote_connection_handle_new_channel_block_invoke.231.cold.4
+ ____xpc_remote_connection_handle_new_channel_block_invoke.231.cold.5
+ ____xpc_remote_connection_handle_new_channel_block_invoke.231.cold.6
+ ____xpc_remote_connection_handle_new_channel_block_invoke.232
+ ____xpc_remote_connection_handle_new_channel_block_invoke.232.cold.1
+ ____xpc_remote_connection_handle_read_block_invoke.241
+ ____xpc_remote_connection_listen_block_invoke.208
+ ____xpc_remote_connection_open_stream_block_invoke.246
+ ____xpc_remote_connection_ready_block_invoke.236
+ ____xpc_remote_connection_ready_block_invoke.236.cold.1
+ ____xpc_remote_connection_ready_block_invoke.237
+ ____xpc_remote_connection_setup_nw_listener_block_invoke.227
+ ___block_descriptor_56_e8_32s40s48bs_e42_v16?0"NSObject<OS_nw_protocol_options>"8ls32l8s48l8s40l8
+ ___block_literal_global.202
+ ___block_literal_global.205
+ ___block_literal_global.212
+ ___xpc_remote_connection_create_configure_tls_block_block_invoke
+ ___xpc_remote_connection_send_message_with_reply_block_invoke.58
+ __nw_parameters_configure_protocol_default_configuration
+ __xpc_remote_connection_create_nw_parameters
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _nw_error_copy_cf_error
+ _nw_parameters_create_secure_tcp
+ _nw_tls_copy_sec_protocol_options
+ _objc_msgSend$copy
+ _objc_msgSend$setTls_identity:
+ _objc_msgSend$setTls_verify:
+ _objc_msgSend$setTls_verify_queue:
+ _objc_msgSend$tls_identity
+ _objc_msgSend$tls_verify
+ _objc_msgSend$tls_verify_queue
+ _remote_device_get_xpc_remote_connection_mode_flags
+ _remote_service_copy_device
+ _sec_protocol_options_append_tls_ciphersuite_group
+ _sec_protocol_options_set_local_identity
+ _sec_protocol_options_set_max_tls_protocol_version
+ _sec_protocol_options_set_min_tls_protocol_version
+ _sec_protocol_options_set_peer_authentication_required
+ _sec_protocol_options_set_verify_block
+ _xpc_remote_connection_create_configure_tls_block
+ _xpc_remote_connection_set_tls
+ _xpc_remote_connection_set_tls.cold.1
+ _xpc_remote_connection_set_tls.cold.2
- GCC_except_table110
- GCC_except_table21
- GCC_except_table23
- GCC_except_table48
- GCC_except_table76
- GCC_except_table86
- ___Block_byref_object_copy_.224
- ___Block_byref_object_dispose_.225
- ____xpc_remote_connection_handle_new_channel_block_invoke.211
- ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.1
- ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.2
- ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.3
- ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.4
- ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.5
- ____xpc_remote_connection_handle_new_channel_block_invoke.211.cold.6
- ____xpc_remote_connection_handle_new_channel_block_invoke.212
- ____xpc_remote_connection_handle_new_channel_block_invoke.212.cold.1
- ____xpc_remote_connection_handle_read_block_invoke.221
- ____xpc_remote_connection_listen_block_invoke.188
- ____xpc_remote_connection_open_stream_block_invoke.226
- ____xpc_remote_connection_ready_block_invoke.216
- ____xpc_remote_connection_ready_block_invoke.216.cold.1
- ____xpc_remote_connection_ready_block_invoke.217
- ____xpc_remote_connection_setup_nw_listener_block_invoke.207
- ___block_literal_global.182
- ___block_literal_global.185
- ___block_literal_global.192
- ___xpc_remote_connection_send_message_with_reply_block_invoke.56
CStrings:
+ "\x12\x11\x11(Q\x11'"
+ "@\"NSObject<OS_sec_identity>\""
+ "BUG IN CLIENT OF RemoteXPC: Attempt to configure TLS on connection created with preexisting nw_connection_t"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_tls_verify_queue"
+ "T@\"NSObject<OS_sec_identity>\",&,N,V_tls_identity"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_tls_verify"
+ "[%p] Got nw_connection failed with error %{public}@"
+ "_tls_identity"
+ "_tls_verify"
+ "_tls_verify_queue"
+ "copy"
+ "disable_adaptive_write_timeout"
+ "setTls_identity:"
+ "setTls_verify:"
+ "setTls_verify_queue:"
+ "tls_identity"
+ "tls_verify"
+ "tls_verify_queue"
+ "v16@?0@\"NSObject<OS_nw_protocol_options>\"8"
- "\x12\x11\x11(Q\x11$"
- "[%p] Got nw_connection failed with error %{errno}d"

```
