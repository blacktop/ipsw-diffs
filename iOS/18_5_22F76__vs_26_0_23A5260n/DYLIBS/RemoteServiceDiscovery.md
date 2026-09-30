## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

```diff

-172.100.9.0.0
-  __TEXT.__text: 0xe1d0
+196.0.0.0.0
+  __TEXT.__text: 0xe1c8
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1299
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x12bc
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__oslogstring: 0x1c37
   __TEXT.__unwind_info: 0x4a0

   __TEXT.__objc_methtype: 0x169
   __TEXT.__objc_stubs: 0x760
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x5e8
+  __DATA_CONST.__const: 0x5f8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__objc_const: 0xb68
+  __AUTH.__objc_data: 0x28
   __DATA.__objc_ivar: 0xbc
   __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x1b8
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9EF17908-9721-3180-97F0-8E88FB06DB74
+  UUID: 220584FC-749A-33F1-8B28-92094FA7434B
   Functions: 433
   Symbols:   1352
-  CStrings:  492
+  CStrings:  494
 
Symbols:
+ ____remote_device_start_browsing_block_invoke.369
+ ____remote_device_start_browsing_block_invoke.369.cold.1
+ ____remote_service_accept_block_invoke.374
+ ____remote_service_connect_socket_impl_block_invoke.344
+ ____remote_service_connect_socket_impl_block_invoke.345
+ ___block_literal_global.326
+ ___block_literal_global.329
+ ___block_literal_global.350
+ ___block_literal_global.353
+ ___block_literal_global.356
+ ___block_literal_global.371
+ ___block_literal_global.377
+ ___remote_device_create_from_client_description_block_invoke.358
+ _remote_device_copy_local_services
+ _remote_device_copy_local_services.cold.1
+ _remote_device_copy_local_services.cold.2
+ _remote_device_copy_local_services.cold.3
- ____remote_device_start_browsing_block_invoke.367
- ____remote_device_start_browsing_block_invoke.367.cold.1
- ____remote_service_accept_block_invoke.372
- ____remote_service_connect_socket_impl_block_invoke.342
- ____remote_service_connect_socket_impl_block_invoke.343
- ___block_literal_global.324
- ___block_literal_global.327
- ___block_literal_global.348
- ___block_literal_global.351
- ___block_literal_global.354
- ___block_literal_global.369
- ___block_literal_global.375
- ___remote_device_create_from_client_description_block_invoke.356
- _remote_device_copy_local_service_names
- _remote_device_copy_local_service_names.cold.1
- _remote_device_copy_local_service_names.cold.2
- _remote_device_copy_local_service_names.cold.3
Functions:
~ _remote_device_type_is_trusted : 48 -> 52
~ _remote_device_copy_local_service_names -> _remote_device_copy_local_services : 320 -> 312
~ _local_device_copy_identity : 1892 -> 1888
CStrings:
+ "virtualmachine"
+ "virtualmachine-host"

```
