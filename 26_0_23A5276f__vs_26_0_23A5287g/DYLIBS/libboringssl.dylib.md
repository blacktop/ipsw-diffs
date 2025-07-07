## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.0.10.0.0
-  __TEXT.__text: 0x9fb0c
-  __TEXT.__auth_stubs: 0x1e20
+532.0.11.0.0
+  __TEXT.__text: 0x9fca4
+  __TEXT.__auth_stubs: 0x1e40
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x106bd
+  __TEXT.__cstring: 0x106e0
   __TEXT.__const: 0xfef8
-  __TEXT.__oslogstring: 0x5be2
+  __TEXT.__oslogstring: 0x5c34
   __TEXT.__gcc_except_tab: 0x2940
-  __TEXT.__unwind_info: 0x2490
+  __TEXT.__unwind_info: 0x24a8
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x240
-  __TEXT.__objc_methname: 0xe4d
+  __TEXT.__objc_methname: 0xe63
   __TEXT.__objc_methtype: 0x62b
   __TEXT.__objc_stubs: 0xa0
   __DATA_CONST.__got: 0xd0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH_CONST.__auth_got: 0xf38
   __AUTH_CONST.__const: 0x18c8
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x20e8
+  __AUTH_CONST.__objc_const: 0x2108
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2f0
+  __DATA.__objc_ivar: 0x2f4
   __DATA.__data: 0xd00
   __DATA.__bss: 0x548
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 76FFE13B-78D5-3721-B99D-5F8EE1051931
-  Functions: 3131
-  Symbols:   7400
-  CStrings:  3638
+  UUID: 7B24AFD5-41B9-3FF0-A419-C5BFDA5D2F63
+  Functions: 3133
+  Symbols:   7407
+  CStrings:  3641
 
Symbols:
+ GCC_except_table70
+ GCC_except_table77
+ _OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.received_disconnected
+ ___block_literal_global.130
+ ___block_literal_global.143
+ ___nw_protocol_boringssl_begin_connection_block_invoke.147
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.137
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.1
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.2
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.3
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.4
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.5
+ ___nw_protocol_boringssl_write_frames_block_invoke.133
+ ___nw_protocol_boringssl_write_frames_block_invoke.133.cold.1
+ _nw_protocol_boringssl_disconnected
+ _nw_protocol_boringssl_disconnected.cold.1
+ _nw_protocol_callbacks_set_disconnected
+ _nw_protocol_disconnected_quiet
- GCC_except_table69
- GCC_except_table76
- ___block_literal_global.129
- ___block_literal_global.142
- ___nw_protocol_boringssl_begin_connection_block_invoke.146
- ___nw_protocol_boringssl_get_input_frames_block_invoke.136
- ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.1
- ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.2
- ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.3
- ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.4
- ___nw_protocol_boringssl_get_input_frames_block_invoke.136.cold.5
- ___nw_protocol_boringssl_write_frames_block_invoke.132
- ___nw_protocol_boringssl_write_frames_block_invoke.132.cold.1
CStrings:
+ "%{public}s(%d) Already received disconnected from below; skipping PQ-TLS fallback"
+ "nw_protocol_boringssl_disconnected"
+ "received_disconnected"

```
