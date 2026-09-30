## libsystem_trace.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_trace.dylib`

```diff

-1612.60.25.0.0
-  __TEXT.__text: 0x9418
+1612.60.26.0.0
+  __TEXT.__text: 0x9478
   __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__cstring: 0x1253
+  __TEXT.__cstring: 0x1169
   __TEXT.__const: 0x446
   __TEXT.__objc_classname: 0xb
   __TEXT.__objc_methname: 0x1ee

   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_platform.dylib
-  Functions: 153
-  Symbols:   307
-  CStrings:  248
+  Functions: 154
+  Symbols:   308
+  CStrings:  247
 
Symbols:
+ __block_descriptor_tmp.51
+ __block_descriptor_tmp.55
+ __block_descriptor_tmp.57
+ __u8__v_encode_block_invoke.56
+ _oslogbase_logdata__encode
- __block_descriptor_tmp.47
- __block_descriptor_tmp.50
- __block_descriptor_tmp.52
- __u8__v_encode_block_invoke.51
CStrings:
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
- "(oslogexclaves_signposterror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogExclaves.SignpostError\""
- "(oslogexclaves_subsystemerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogExclaves.SubsystemError\""

```
