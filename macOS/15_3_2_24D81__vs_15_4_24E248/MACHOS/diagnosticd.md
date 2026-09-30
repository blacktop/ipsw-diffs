## diagnosticd

> `/usr/libexec/diagnosticd`

```diff

-1612.80.7.0.0
-  __TEXT.__text: 0x584c
-  __TEXT.__auth_stubs: 0xa20
+1643.100.44.0.0
+  __TEXT.__text: 0x6a68
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_stubs: 0x3e0
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xca0
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x1175
   __TEXT.__objc_methname: 0x285
-  __TEXT.__unwind_info: 0x168
-  __DATA_CONST.__auth_got: 0x518
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6e0
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__auth_got: 0x618
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x900
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0xf8
+  __DATA.__os_assumes_log: 0x8
   __DATA.__data: 0x1a4
   __DATA.__crash_info: 0x40
-  __DATA.__os_assumes_log: 0x8
-  __DATA.__bss: 0x1d8
+  __DATA.__bss: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/BridgeXPC.framework/Versions/A/BridgeXPC
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/Versions/A/LoggingSupport
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Versions/A/Tightbeam
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93E2D583-1AC2-35D4-A40B-D87C486ABF2D
-  Functions: 68
-  Symbols:   191
-  CStrings:  165
+  - /usr/lib/libz.1.dylib
+  UUID: 358D3BA4-F431-33EE-81BB-CC322B4571FF
+  Functions: 89
+  Symbols:   226
+  CStrings:  183
 
Symbols:
+ __Block_object_dispose
+ __xpc_type_int64
+ __xpc_type_uint64
+ _crc32
+ _exclaves_lookup_service
+ _printf
+ _strlen
+ _tb_client_connection_activate
+ _tb_client_connection_create
+ _tb_client_connection_create_with_endpoint
+ _tb_client_connection_message_construct
+ _tb_client_connection_message_destruct
+ _tb_connection_send_query
+ _tb_endpoint_create_with_data
+ _tb_endpoint_set_interface_identifier
+ _tb_message_complete
+ _tb_message_configure_received
+ _tb_message_construct
+ _tb_message_decode_u64
+ _tb_message_decode_u8
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
+ _tb_message_raw_encode_u8
+ _tb_message_subrange
+ _tb_transport_message_buffer_wrap_buffer
+ _xpc_create_from_plist
+ _xpc_dictionary_apply
+ _xpc_dictionary_get_dictionary
+ _xpc_dictionary_get_value
+ _xpc_uint64_get_value
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/diagnosticd.build/DerivedSources/OSLogDarwin_C.c"
+ "B24@?0r*8^v16"
+ "B32@?0Q8^{oslogdarwin_streamprefsvalue_s=IQ}16Q24"
+ "Exclaves log server not available"
+ "Failed to initialize config admin client"
+ "I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8"
+ "TB_ASSERT: (err == TB_ERROR_SUCCESS) && \"failed to wrap packed buffer\""
+ "TB_ASSERT: (oslogdarwin_streamprefsbatch__raw_encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.StreamPrefsBatch\""
+ "TB_ASSERT: (vErr == TB_ERROR_SUCCESS) && \"tb_message_subrange failed\""
+ "TB_FATAL: invalid tag in array metadata: 0x%x"
+ "TB_FATAL: invalid tag in array metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid value: unexpected case value, %llx"
+ "TB_FATAL: invalid value: unexpected case value, %llx (%s:%d)\n"
+ "com.apple.service.LogServer_xnuproxy"
+ "failed to set stream preferences in exclaves: full cache"
+ "failed to set stream preferences in exclaves: invalid subsystem id"
+ "v24@?0Q8r^{oslogdarwin_streamprefsvalue_s=IQ}16"
+ "v24@?0{oslogdarwin_configadmin_setstreampreferences__result_s=C(?={oslogdarwin_configerror_s=Q})}8"

```
