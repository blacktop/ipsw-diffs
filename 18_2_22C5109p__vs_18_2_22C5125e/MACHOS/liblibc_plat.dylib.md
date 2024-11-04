## liblibc_plat.dylib

> `/System/ExclaveKit/usr/lib/system/liblibc_plat.dylib`

```diff

-696.60.269.0.1
-  __TEXT.__text: 0x22668
+696.60.281.0.0
+  __TEXT.__text: 0x2262c
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__cstring: 0x5d3f
+  __TEXT.__cstring: 0x5cd3
   __TEXT.__const: 0x1f60
   __TEXT.__unwind_info: 0x990
   __DATA.__auth_got: 0x258

   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib
-  Functions: 1233
-  Symbols:   4767
-  CStrings:  609
+  Functions: 1226
+  Symbols:   4732
+  CStrings:  610
 
Symbols:
+ easm_space_spanmapframe.cold.1
- easm_space_allocamxcontext.cold.1
- easm_space_allocendpoint.cold.1
- easm_space_allocexecutioncontext.cold.1
- easm_space_framecopy.cold.1
- easm_space_rootcopy.cold.1
- easm_space_spanalloc.cold.1
- easm_space_spanat.cold.1
- easm_space_spanconfig.cold.1
CStrings:
+ "(tb_message_encode_capability(&msg, (uint64_t) frame) == TB_ERROR_SUCCESS) && \"failed to encode capability\""
+ "ASAN: Panic disabled via xrt runflags, continuing...\n"
+ "TB_FATAL: invalid value: unexpected bits, 0x%!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "UBSAN: Panic disabled via xrt runflags, continuing...\n"
- "(decode_error == TB_ERROR_SUCCESS) && \"tb_message_decode_capability failed\""
- "(easm_failure__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.Failure\""
- "(easm_spanconfig__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.SpanConfig\""
- "(easm_spanrefconfig__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.SpanRefConfig\""

```
