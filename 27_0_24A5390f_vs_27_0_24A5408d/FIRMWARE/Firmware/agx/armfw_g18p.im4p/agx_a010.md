## agx_a010

> `Firmware/agx/armfw_g18p.im4p/agx_a010`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3c6b8
+  __TEXT.__text: 0x3cc14
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1068
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x23d8
+  __TEXT.__cstring: 0x23fc
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
-  __DATA.__data: 0x17508
+  __DATA.__data: 0x17d28
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x798
+  __DATA.__const: 0x7a8
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5a758
+  __DATA.__zerofill: 0x5a778
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 416
   Symbols:   168
-  CStrings:  236
+  CStrings:  237
 
Functions:
~ sub_fffffc000000be28 : 10776 -> 11152
~ sub_fffffc000000fc04 -> sub_fffffc000000fd7c : 10000 -> 10020
~ sub_fffffc00000124ec -> sub_fffffc0000012678 : 4764 -> 4844
~ sub_fffffc0000015094 -> sub_fffffc0000015270 : 2060 -> 2108
~ sub_fffffc000001c6c8 -> sub_fffffc000001c8d4 : 360 -> 352
~ sub_fffffc000001ce24 -> sub_fffffc000001d028 : 1688 -> 1704
~ sub_fffffc000001dc0c -> sub_fffffc000001de20 : 756 -> 768
~ sub_fffffc000001e278 -> sub_fffffc000001e498 : 848 -> 832
~ sub_fffffc000001ecc8 -> sub_fffffc000001eed8 : 2372 -> 2376
~ sub_fffffc0000023658 -> sub_fffffc000002386c : 384 -> 368
~ sub_fffffc0000023f84 -> sub_fffffc0000024188 : 1368 -> 1380
~ sub_fffffc0000025060 -> sub_fffffc0000025270 : 768 -> 772
~ sub_fffffc00000276d0 -> sub_fffffc00000278e4 : 7364 -> 8076
~ sub_fffffc0000029394 -> sub_fffffc0000029870 : 2088 -> 2216
~ sub_fffffc000003c574 -> sub_fffffc000003cad0 : 332 -> 324
CStrings:
+ "Aug  5 2026 22:00:16"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:20:06"
```
