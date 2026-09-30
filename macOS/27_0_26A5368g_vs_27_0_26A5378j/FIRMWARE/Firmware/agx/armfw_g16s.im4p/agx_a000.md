## agx_a000

> `Firmware/agx/armfw_g16s.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x50e44
-  __TEXT.__gxf_code: 0x4f70
+  __TEXT.__text: 0x51258
+  __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x12e7

   __DATA.__gxf_data: 0x80b8
   __DATA.__data: 0x17198
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xb88
+  __DATA.__const: 0xba0
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x5ea58
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
-  Functions: 498
-  Symbols:   168
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
+  Functions: 499
+  Symbols:   169
   CStrings:  305
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
CStrings:
+ "Jun 29 2026 23:32:10"
- "Jun 16 2026 21:33:10"

```
