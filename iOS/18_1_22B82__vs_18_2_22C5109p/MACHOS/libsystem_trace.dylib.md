## libsystem_trace.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_trace.dylib`

```diff

-1612.40.4.0.0
-  __TEXT.__text: 0x925c
-  __TEXT.__auth_stubs: 0x470
+1612.60.25.0.0
+  __TEXT.__text: 0x9418
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__cstring: 0x1174
+  __TEXT.__cstring: 0x1253
   __TEXT.__const: 0x446
   __TEXT.__objc_classname: 0xb
   __TEXT.__objc_methname: 0x1ee
   __TEXT.__objc_methtype: 0xc5
-  __TEXT.__unwind_info: 0x218
-  __DATA.__auth_got: 0x240
+  __TEXT.__unwind_info: 0x220
+  __DATA.__auth_got: 0x250
   __DATA.__got: 0x10
   __DATA.__auth_ptr: 0x20
-  __DATA.__const: 0x370
+  __DATA.__const: 0x3b0
   __DATA.__objc_classlist: 0x8
   __DATA.__objc_protolist: 0x8
   __DATA.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc8
   __DATA.__ENDPOINTS: 0x107
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x290
   __DATA.__common: 0x20
   - /System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation
   - /System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
+  - /System/ExclaveKit/usr/lib/system/libdispatch.dylib
+  - /System/ExclaveKit/usr/lib/system/libdyld.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc_plat.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_platform.dylib
-  Functions: 146
-  Symbols:   292
-  CStrings:  240
+  Functions: 153
+  Symbols:   307
+  CStrings:  248
 
Symbols:
+ __NSConcreteGlobalBlock
+ ____os_log_image_find_block_invoke
+ ___block_literal_global
+ __os_log_image_register
+ _dispatch_once
+ _mh_uuid_cache_find
+ _mh_uuid_cache_find_index
+ _mh_uuid_cache_init
+ _mh_uuid_cache_insert
+ _os_log_image_find.onceToken
+ _tb_endpoint_set_interface_identifier
+ _tb_message_configure_received
+ _xrt_process_images
+ mh_uuid_cache_find.cold.1
+ mh_uuid_cache_insert.cold.1
+ mh_uuid_cache_insert.cold.2
+ mh_uuid_cache_insert.cold.3
- __os_log_flatten_backtrace
- __os_log_payload_set_max_size
- _cl4_platform_address_space_uuid
- _fix_missing_symbolication
- _tb_message_configure_recieved
CStrings:
+ "Image lookup returned unexpected error %!d(MISSING)"
+ "Invalid image uuid cache"
+ "Invalid image uuid cache entry"
+ "MH address is not empty"
+ "MH addresses do not match"
+ "[%!s(MISSING)][error] failed to initialize libtrace uuid cache (error: %!d(MISSING))"
+ "err"
+ "v8@?0"

```
