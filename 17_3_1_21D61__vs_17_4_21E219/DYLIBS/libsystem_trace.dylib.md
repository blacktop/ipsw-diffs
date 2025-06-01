## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-1481.40.16.0.0
-  __TEXT.__text: 0x160dc
-  __TEXT.__auth_stubs: 0x1000
+1510.100.35.0.1
+  __TEXT.__text: 0x161b8
+  __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_methlist: 0x64
-  __TEXT.__const: 0x14e
-  __TEXT.__cstring: 0x13d2
+  __TEXT.__const: 0x156
+  __TEXT.__cstring: 0x1486
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__oslogstring: 0x137
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__unwind_info: 0x40c
   __TEXT.__objc_classname: 0x24
   __TEXT.__objc_methname: 0x391
   __TEXT.__objc_methtype: 0xc5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x300
   __DATA_CONST.__objc_selrefs: 0x160
+  __DATA_CONST.__objc_classrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__auth_got: 0x808
   __AUTH.__data: 0x168
-  __DATA.__objc_classrefs: 0x10
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0xb0
+  __DATA.__data: 0xb8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x150
   __DATA_DIRTY.__bss: 0x2e8

   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 4408AD69-B633-3A3F-954D-9904E7D26B88
-  Functions: 306
+  UUID: 96EDACA8-BD74-340E-A5E4-F196588B0902
+  Functions: 307
   Symbols:   929
-  CStrings:  410
+  CStrings:  412
 
Symbols:
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.3.394
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.381
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.64
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.68
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.72
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.76
+ ___block_literal_global.105
+ ___block_literal_global.350
+ ___block_literal_global.393
+ ___block_literal_global.78
+ __os_log_unreliable_impl
- ___block_descriptor_tmp.101
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.3.393
- ___block_descriptor_tmp.31
- ___block_descriptor_tmp.380
- ___block_descriptor_tmp.61
- ___block_descriptor_tmp.63
- ___block_descriptor_tmp.65
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.71
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.75
- ___block_literal_global.103
- ___block_literal_global.349
- ___block_literal_global.392
- ___block_literal_global.77
- _voucher_activity_trace_v
CStrings:
+ "BUG IN CLIENT OF LIBTRACE: Calling the unreliable interfaces on a fault is not supported"
+ "BUG IN LIBTRACE: Using oversized messages with unreliable interfaces shouldn't be possible"

```
