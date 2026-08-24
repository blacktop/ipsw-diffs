## agx_b000

> `Firmware/agx/armfw_g16g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x525b8
+  __TEXT.__text: 0x52740
   __TEXT.__gxf_code: 0x5080
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1db8
-  __TEXT.__cstring: 0x267e
+  __TEXT.__cstring: 0x26a2
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x81b0
   __DATA.__data: 0xeb8
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xb30
+  __DATA.__const: 0xb40
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x7a278
+  __DATA.__zerofill: 0x7a298
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 517
   Symbols:   189
-  CStrings:  267
+  CStrings:  268
 
Functions:
~ sub_fffffc0000003984 : 8028 -> 8040
~ sub_fffffc00000123c4 -> sub_fffffc00000123d0 : 4772 -> 4800
~ sub_fffffc00000146ac -> sub_fffffc00000146d4 : 2392 -> 2420
~ sub_fffffc000002603c -> sub_fffffc0000026080 : 584 -> 600
~ sub_fffffc0000026a24 -> sub_fffffc0000026a78 : 804 -> 820
~ sub_fffffc0000026eec -> sub_fffffc0000026f50 : 1784 -> 1800
~ sub_fffffc00000286cc -> sub_fffffc0000028740 : 488 -> 480
~ sub_fffffc000002b2dc -> sub_fffffc000002b348 : 1628 -> 1684
~ sub_fffffc000002b938 -> sub_fffffc000002b9dc : 252 -> 280
~ sub_fffffc0000033298 -> sub_fffffc0000033358 : 1228 -> 1252
~ sub_fffffc0000033764 -> sub_fffffc000003383c : 2128 -> 2124
~ sub_fffffc00000341b8 -> sub_fffffc000003428c : 872 -> 856
~ sub_fffffc0000038370 -> sub_fffffc0000038434 : 1456 -> 1576
~ sub_fffffc00000397c8 -> sub_fffffc0000039904 : 7304 -> 7308
~ sub_fffffc000003bb04 -> sub_fffffc000003bc44 : 1120 -> 1192
~ sub_fffffc0000052478 -> sub_fffffc0000052600 : 328 -> 320
CStrings:
+ "Aug 11 2026 21:46:04"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:25:17"
```
