## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.0.13.0.0
-  __TEXT.__text: 0x9fdec
-  __TEXT.__auth_stubs: 0x1e50
+532.40.3.0.0
+  __TEXT.__text: 0xa07d4
+  __TEXT.__auth_stubs: 0x1e60
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x106e0
+  __TEXT.__cstring: 0x107d9
   __TEXT.__const: 0xfef8
-  __TEXT.__oslogstring: 0x5c34
-  __TEXT.__gcc_except_tab: 0x2940
-  __TEXT.__unwind_info: 0x24a8
+  __TEXT.__oslogstring: 0x5de7
+  __TEXT.__gcc_except_tab: 0x2908
+  __TEXT.__unwind_info: 0x24b8
   __TEXT.__eh_frame: 0x130
-  __TEXT.__objc_classname: 0x240
-  __TEXT.__objc_methname: 0xe83
+  __TEXT.__objc_classname: 0x241
+  __TEXT.__objc_methname: 0xecf
   __TEXT.__objc_methtype: 0x62b
   __TEXT.__objc_stubs: 0xa0
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0xb898
+  __DATA_CONST.__const: 0xb890
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf40
-  __AUTH_CONST.__const: 0x18c8
+  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH_CONST.__const: 0x1908
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x2148
+  __AUTH_CONST.__objc_const: 0x21a8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0xd00
-  __DATA.__bss: 0x540
+  __DATA.__objc_ivar: 0x308
+  __DATA.__data: 0xd08
+  __DATA.__bss: 0x548
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x210
   __DATA_DIRTY.__bss: 0xcb8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 688DBE0A-B770-3032-B7BF-B30488E602CB
-  Functions: 3133
-  Symbols:   7410
-  CStrings:  3643
+  UUID: 738662EB-E4E8-323C-99C1-CAED3727FAE0
+  Functions: 3140
+  Symbols:   7433
+  CStrings:  3661
 
Symbols:
+ GCC_except_table52
+ GCC_except_table72
+ _OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.output_batched_bytes_written
+ _OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.output_batching_frame
+ _OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.output_pending_length
+ _OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.pqtls_fallback_initiated
+ ___block_descriptor_32_e8_v12?0I8l
+ ___block_literal_global.134
+ ___block_literal_global.149
+ ___block_literal_global.157
+ ___block_literal_global.160
+ ___nw_boringssl_batching_register_batching_size_updates_block_invoke
+ ___nw_boringssl_batching_register_batching_size_updates_block_invoke_2
+ ___nw_protocol_boringssl_begin_connection_block_invoke.153
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.143
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.1
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.2
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.3
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.4
+ ___nw_protocol_boringssl_get_input_frames_block_invoke.143.cold.5
+ ___nw_protocol_boringssl_identifier_block_invoke.cold.1
+ ___nw_protocol_boringssl_initiate_pqtls_fallback_block_invoke
+ ___nw_protocol_boringssl_write_frames_block_invoke.138
+ ___nw_protocol_boringssl_write_frames_block_invoke.138.cold.1
+ _network_config_register_boringssl_batching_size_updates
+ _nw_batching_finaltxt_size
+ _nw_batching_plaintxt_size
+ _nw_boringssl_batching_register_batching_size_updates.onceToken
+ _nw_protocol_boringssl_allocate_batching_frame
+ _nw_protocol_boringssl_allocate_batching_frame.cold.1
+ _nw_protocol_boringssl_allocate_batching_frame.cold.2
+ _nw_protocol_boringssl_allocate_batching_frame.cold.3
+ _nw_protocol_boringssl_allocate_batching_frame.cold.4
+ _nw_protocol_boringssl_allocate_batching_frame.cold.5
+ _nw_protocol_boringssl_allocate_batching_frame.cold.6
+ _nw_protocol_boringssl_disconnected.cold.2
+ _nw_protocol_boringssl_error.cold.7
+ _nw_protocol_boringssl_flush_batching_frame
+ _nw_protocol_boringssl_flush_batching_frame.cold.1
+ _nw_protocol_boringssl_flush_batching_frame.cold.2
+ _nw_protocol_boringssl_flush_batching_frame.cold.3
+ _nw_protocol_boringssl_flush_batching_frame.cold.4
+ _nw_protocol_boringssl_get_output_frames.cold.8
+ _nw_protocol_boringssl_input_finished.cold.4
- GCC_except_table23
- GCC_except_table70
- GCC_except_table77
- _OBJC_IVAR_$_boringssl_concrete_nw_protocol_boringssl.received_disconnected
- _OUTLINED_FUNCTION_47
- ___block_descriptor_40_e8_32r_e31_B16?0"NSObject<OS_nw_frame>"8lr32l8
- ___block_literal_global.130
- ___block_literal_global.143
- ___nw_protocol_boringssl_begin_connection_block_invoke.147
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.1
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.2
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.3
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.4
- ___nw_protocol_boringssl_get_input_frames_block_invoke.137.cold.5
- ___nw_protocol_boringssl_write_bytes_block_invoke
- ___nw_protocol_boringssl_write_frames_block_invoke.133
- ___nw_protocol_boringssl_write_frames_block_invoke.133.cold.1
- _nw_protocol_boringssl_write_bytes.cold.10
- _nw_protocol_boringssl_write_bytes.cold.11
- _nw_protocol_boringssl_write_bytes.cold.12
- _nw_protocol_boringssl_write_bytes.cold.13
- _nw_protocol_boringssl_write_bytes.cold.14
- _nw_protocol_boringssl_write_bytes.cold.5
- _nw_protocol_boringssl_write_bytes.cold.6
- _nw_protocol_boringssl_write_bytes.cold.7
- _nw_protocol_boringssl_write_bytes.cold.8
- _nw_protocol_boringssl_write_bytes.cold.9
CStrings:
+ "%{public}s(%d) %{public}s[%p] Creating larger frame to accommodate %u bytes"
+ "%{public}s(%d) %{public}s[%p] allocated new batching frame: %u bytes capacity"
+ "%{public}s(%d) %{public}s[%p] claiming batching frame with %u bytes failed"
+ "%{public}s(%d) %{public}s[%p] failed to finalize batching frame"
+ "%{public}s(%d) %{public}s[%p] failed to get unclaimed bytes from batching frame"
+ "%{public}s(%d) %{public}s[%p] flushed batching frame: %s"
+ "%{public}s(%d) %{public}s[%p] ignoring disconnected during pqtls fallback"
+ "%{public}s(%d) %{public}s[%p] ignoring error during pqtls fallback"
+ "%{public}s(%d) %{public}s[%p] ignoring input_finished during pqtls fallback"
+ "%{public}s(%d) %{public}s[%p] no batching frames available; requested min=%d, max=%u"
+ "%{public}s(%d) %{public}s[%p] no output handler available"
+ "%{public}s(%d) %{public}s[%p] received output available"
+ "%{public}s(%d) %{public}s[%p] wrote %u bytes to batching frame"
+ "%{public}s(%d) Performing PQ-TLS fallback"
+ "%{public}s(%d) safe input protocol is NULL; skipping PQ-TLS fallback"
+ "end of write_frames"
+ "frame full"
+ "immediate mode"
+ "nw_protocol_boringssl_allocate_batching_frame"
+ "nw_protocol_boringssl_flush_batching_frame"
+ "nw_protocol_boringssl_initiate_pqtls_fallback_block_invoke"
+ "nw_protocol_boringssl_write_to_batching_frame"
+ "output_batched_bytes_written"
+ "output_batching_frame"
+ "output_pending_length"
+ "pqtls_fallback_initiated"
+ "v12@?0I8"
- "%{public}s(%d) %{public}s[%p] claiming frame with %u bytes failed"
- "%{public}s(%d) %{public}s[%p] failed to use %u frames, marking as failed"
- "%{public}s(%d) %{public}s[%p] output frames count is zero"
- "%{public}s(%d) %{public}s[%p] output_frames is empty; requested min=%d, max=%d"
- "%{public}s(%d) %{public}s[%p] received input available"
- "%{public}s(%d) %{public}s[%p] total bytes written: 0 (no finalize_output_frames callback)"
- "%{public}s(%d) %{public}s[%p] total bytes written: 0 (no output frames available)"
- "%{public}s(%d) Already received disconnected from below; skipping PQ-TLS fallback"
- "received_disconnected"

```
