## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-1322.3.0.0.0
-  __TEXT.__text: 0x28d64
+1323.2.0.0.0
+  __TEXT.__text: 0x28e70
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__const: 0x600
-  __TEXT.__cstring: 0x4839
+  __TEXT.__const: 0x610
+  __TEXT.__cstring: 0x4871
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x1588
+  __DATA_CONST.__const: 0x15a0
   __DATA_CONST.__helper: 0x8
   __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0x1730
   __AUTH.__data: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__data: 0x120
-  __DATA.__common: 0x19
-  __DATA.__bss: 0x1098
-  __DATA_DIRTY.__common: 0x20
+  __DATA.__common: 0x11
+  __DATA.__bss: 0x1048
+  __DATA_DIRTY.__common: 0x28
+  __DATA_DIRTY.__bss: 0x50
   __TPRO_CONST.__dyld_apis: 0x8
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 274FC511-EED1-3500-BFB4-69E0EB6945A2
+  UUID: D1059248-BCC1-3FB3-B582-4BF04400C2A7
   Functions: 1057
   Symbols:   2779
-  CStrings:  541
+  CStrings:  545
 
Symbols:
+ __ZNK6mach_o11ExportsTrie5validEyy
+ ____ZNK6mach_o11ExportsTrie5validEyy_block_invoke
+ ___block_descriptor_tmp.291
+ ___block_descriptor_tmp.293
+ ___block_descriptor_tmp.298
+ ___block_descriptor_tmp.300
+ ___block_descriptor_tmp.310
+ ___block_descriptor_tmp.33
- __ZNK6mach_o11ExportsTrie5validEy
- ____ZNK6mach_o11ExportsTrie5validEy_block_invoke
- ___block_descriptor_tmp.290
- ___block_descriptor_tmp.292
- ___block_descriptor_tmp.297
- ___block_descriptor_tmp.299
- ___block_descriptor_tmp.309
Functions:
~ __ZN5dyld45Atlas7Process11getSnapshotEPi : 512 -> 508
~ __dyld_call_with_writable_tpro_memory : 68 -> 72
~ _vm_read_safe : 148 -> 144
~ __ZN6mach_o12Architecture6byNameENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEE : 968 -> 1132
~ ____ZNK6mach_o11ExportsTrie5validEy_block_invoke -> ____ZNK6mach_o11ExportsTrie5validEyy_block_invoke : 300 -> 312
~ __ZNK6mach_o5Image13validLinkeditERKNS_6PolicyE : 744 -> 840
CStrings:
+ "armv8.1m.main"
+ "armv8m.main"
+ "thumbv8.1m.main"
+ "thumbv8m.main"

```
