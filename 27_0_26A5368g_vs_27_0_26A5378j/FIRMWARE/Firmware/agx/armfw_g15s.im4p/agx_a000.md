## agx_a000

> `Firmware/agx/armfw_g15s.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x50434
+  __TEXT.__text: 0x5069c
   __TEXT.__gxf_code: 0x10cc
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe70
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xa10
+  __DATA.__const: 0xa28
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xcae98
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
-  Functions: 502
-  Symbols:   177
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
+  Functions: 503
+  Symbols:   178
   CStrings:  276
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
CStrings:
+ "Jun 29 2026 23:32:09"
- "Jun 16 2026 21:33:08"

```
