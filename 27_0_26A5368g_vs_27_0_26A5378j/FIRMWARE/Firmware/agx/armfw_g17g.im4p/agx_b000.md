## agx_b000

> `Firmware/agx/armfw_g17g.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x3c8bc
-  __TEXT.__gxf_code: 0x4f70
+  __TEXT.__text: 0x3ce9c
+  __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x104f
+  __TEXT.__const: 0x106f
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2404

   __DATA.__gxf_data: 0x80b8
   __DATA.__data: 0x17520
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x7a0
+  __DATA.__const: 0x7b8
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5a738
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA.__zerofill: 0x5a758
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 416
-  Symbols:   168
+  Symbols:   169
   CStrings:  237
 
Sections:
~ __TEXT._rtk_patchbay : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
CStrings:
+ "Jun 29 2026 23:41:07"
- "Jun 16 2026 21:43:26"

```
