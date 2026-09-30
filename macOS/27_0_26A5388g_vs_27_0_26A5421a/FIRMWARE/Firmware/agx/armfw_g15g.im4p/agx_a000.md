## agx_a000

> `Firmware/agx/armfw_g15g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4f178
+  __TEXT.__text: 0x4f308
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x23e4
-  __TEXT.__cstring: 0x2400
+  __TEXT.__cstring: 0x2424
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe10
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x9e0
+  __DATA.__const: 0x9f0
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x68ed8
+  __DATA.__zerofill: 0x68ef8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 490
   Symbols:   197
-  CStrings:  256
+  CStrings:  257
 
Functions:
~ sub_fffffc00000037e0 : 4596 -> 4600
~ sub_fffffc0000011090 -> sub_fffffc0000011094 : 4460 -> 4480
~ sub_fffffc0000013234 -> sub_fffffc000001324c : 2392 -> 2420
~ sub_fffffc00000246b0 -> sub_fffffc00000246e4 : 584 -> 600
~ sub_fffffc000002503c -> sub_fffffc0000025080 : 804 -> 820
~ sub_fffffc0000025504 -> sub_fffffc0000025558 : 1784 -> 1800
~ sub_fffffc00000269fc -> sub_fffffc0000026a60 : 1628 -> 1684
~ sub_fffffc0000027058 -> sub_fffffc00000270f4 : 252 -> 280
~ sub_fffffc000003230c -> sub_fffffc00000323c4 : 740 -> 764
~ sub_fffffc00000325f0 -> sub_fffffc00000326c0 : 2048 -> 2044
~ sub_fffffc0000035c30 -> sub_fffffc0000035cfc : 1480 -> 1600
~ sub_fffffc00000370a0 -> sub_fffffc00000371e4 : 8468 -> 8472
~ sub_fffffc0000039868 -> sub_fffffc00000399b0 : 1116 -> 1188
CStrings:
+ "Aug 11 2026 21:40:45"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:20:49"
```
