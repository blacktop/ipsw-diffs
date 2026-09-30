## agx_b000

> `Firmware/agx/armfw_g17p.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3b8fc
+  __TEXT.__text: 0x3be6c
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1cf8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2271
+  __TEXT.__cstring: 0x2295
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
-  __DATA.__data: 0x17478
+  __DATA.__data: 0x17c98
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x820
+  __DATA.__const: 0x830
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5b198
+  __DATA.__zerofill: 0x5b1d8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 433
   Symbols:   187
-  CStrings:  232
+  CStrings:  233
 
Functions:
~ sub_fffffc0000003ab4 : 7884 -> 7880
~ sub_fffffc000000b2b4 -> sub_fffffc000000b2b0 : 10592 -> 10924
~ sub_fffffc000000f214 -> sub_fffffc000000f35c : 10304 -> 10324
~ sub_fffffc0000011c2c -> sub_fffffc0000011d88 : 4880 -> 4952
~ sub_fffffc0000014820 -> sub_fffffc00000149c4 : 2044 -> 2092
~ sub_fffffc000001c094 -> sub_fffffc000001c268 : 360 -> 352
~ sub_fffffc000001c7fc -> sub_fffffc000001c9c8 : 1676 -> 1692
~ sub_fffffc000001d5d4 -> sub_fffffc000001d7b0 : 756 -> 768
~ sub_fffffc000001dc5c -> sub_fffffc000001de44 : 848 -> 832
~ sub_fffffc000001e69c -> sub_fffffc000001e874 : 2332 -> 2340
~ sub_fffffc000002072c -> sub_fffffc000002090c : 2108 -> 2120
~ sub_fffffc0000023178 -> sub_fffffc0000023364 : 384 -> 368
~ sub_fffffc0000023a10 -> sub_fffffc0000023bec : 1368 -> 1380
~ sub_fffffc0000024aec -> sub_fffffc0000024cd4 : 768 -> 772
~ sub_fffffc0000026cdc -> sub_fffffc0000026ec8 : 6324 -> 7096
~ sub_fffffc0000028590 -> sub_fffffc0000028a80 : 2084 -> 2212
CStrings:
+ "Aug 11 2026 21:48:48"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:27:53"
```
