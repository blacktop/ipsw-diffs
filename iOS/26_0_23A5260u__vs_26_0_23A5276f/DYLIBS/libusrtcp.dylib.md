## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-5569.0.37.0.12
-  __TEXT.__text: 0x5bf20
+5569.0.127.0.3
+  __TEXT.__text: 0x5c27c
   __TEXT.__auth_stubs: 0x1020
   __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe485
-  __TEXT.__cstring: 0x19c3
+  __TEXT.__oslogstring: 0xe59c
+  __TEXT.__cstring: 0x19dd
   __TEXT.__unwind_info: 0x440
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x388
+  __DATA_CONST.__const: 0x3e8
   __AUTH_CONST.__auth_got: 0x810
   __AUTH_CONST.__const: 0x1a8
   __AUTH.__data: 0x220

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A71B9B26-55D2-35D7-8B1D-E44D0222C751
-  Functions: 320
-  Symbols:   992
-  CStrings:  1105
+  UUID: DCD8EDC0-A476-3E1E-8178-1FE7C9C5C4D5
+  Functions: 322
+  Symbols:   999
+  CStrings:  1111
 
Symbols:
+ _____nw_frame_array_finalize_block_invoke
+ _____nw_frame_array_finalize_block_invoke.284
+ _____nw_frame_array_finalize_block_invoke.587
+ _____nw_signpost_is_enabled_block_invoke.496
+ ___block_descriptor_tmp.12
+ ___block_descriptor_tmp.17
+ ___block_descriptor_tmp.285
+ ___block_descriptor_tmp.488
+ ___block_descriptor_tmp.8.490
+ ___block_descriptor_tmp.801
+ ___block_literal_global.489
+ ___block_literal_global.799
- _____nw_signpost_is_enabled_block_invoke.482
- ___block_descriptor_tmp.474
- ___block_descriptor_tmp.8.476
- ___block_descriptor_tmp.9
- ___block_literal_global.11
- ___block_literal_global.475
- _nw_protocol_tcp_copy_frame_to_frame
CStrings:
+ "%{public}s frame_array %p not empty"
+ "%{public}s frame_array %p not empty, backtrace limit exceeded"
+ "%{public}s frame_array %p not empty, dumping backtrace:%{public}s"
+ "%{public}s frame_array %p not empty, no backtrace"
+ "%{public}s not enough memory to allocate segment, disabling RACK"
+ "tcp_rack_free_and_disable"

```
