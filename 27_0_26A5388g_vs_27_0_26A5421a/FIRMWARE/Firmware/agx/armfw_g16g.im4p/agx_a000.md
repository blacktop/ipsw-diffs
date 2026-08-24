## agx_a000

> `Firmware/agx/armfw_g16g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52aac
+  __TEXT.__text: 0x52c34
   __TEXT.__gxf_code: 0x5080
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1d78
-  __TEXT.__cstring: 0x26fe
+  __TEXT.__cstring: 0x2722
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x81b0
   __DATA.__data: 0xeb8
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xb40
+  __DATA.__const: 0xb50
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x7a278
+  __DATA.__zerofill: 0x7a298
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 518
   Symbols:   189
-  CStrings:  270
+  CStrings:  271
 
Functions:
~ sub_fffffc0000003984 : 8028 -> 8040
~ sub_fffffc00000123d0 -> sub_fffffc00000123dc : 4772 -> 4800
~ sub_fffffc00000146b8 -> sub_fffffc00000146e0 : 2392 -> 2420
~ sub_fffffc00000264b4 -> sub_fffffc00000264f8 : 584 -> 600
~ sub_fffffc0000026e9c -> sub_fffffc0000026ef0 : 804 -> 820
~ sub_fffffc0000027364 -> sub_fffffc00000273c8 : 1784 -> 1800
~ sub_fffffc0000028b44 -> sub_fffffc0000028bb8 : 488 -> 480
~ sub_fffffc000002b754 -> sub_fffffc000002b7c0 : 1628 -> 1684
~ sub_fffffc000002bdb0 -> sub_fffffc000002be54 : 252 -> 280
~ sub_fffffc00000336dc -> sub_fffffc000003379c : 1228 -> 1252
~ sub_fffffc0000033ba8 -> sub_fffffc0000033c80 : 2128 -> 2124
~ sub_fffffc00000345fc -> sub_fffffc00000346d0 : 872 -> 856
~ sub_fffffc0000038850 -> sub_fffffc0000038914 : 1456 -> 1576
~ sub_fffffc0000039ca8 -> sub_fffffc0000039de4 : 7304 -> 7308
~ sub_fffffc000003bfe4 -> sub_fffffc000003c124 : 1120 -> 1192
~ sub_fffffc000005296c -> sub_fffffc0000052af4 : 328 -> 320
CStrings:
+ "Aug 11 2026 21:41:06"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:21:02"
```
