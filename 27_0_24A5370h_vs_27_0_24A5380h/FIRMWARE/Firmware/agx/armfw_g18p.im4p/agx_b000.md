## agx_b000

> `Firmware/agx/armfw_g18p.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x3bddc
-  __TEXT.__gxf_code: 0x4f70
+  __TEXT.__text: 0x3c704
+  __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1065
+  __TEXT.__const: 0x1067
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x23da

   __DATA.__gxf_data: 0x80b8
   __DATA.__data: 0x17508
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x780
+  __DATA.__const: 0x798
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5a718
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
-  Functions: 415
-  Symbols:   167
+  __DATA.__zerofill: 0x5a758
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
+  Functions: 416
+  Symbols:   168
   CStrings:  236
 
Sections:
~ __TEXT._rtk_patchbay : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__chain_starts : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA._rtk_power : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
CStrings:
+ "Jun 30 2026 21:08:05"
- "Jun 18 2026 19:44:05"

```
