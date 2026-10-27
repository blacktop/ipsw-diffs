## agx_a010

> `Firmware/agx/armfw_g17p.im4p/agx_a010`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3be6c
-  __TEXT.__gxf_code: 0x4f40
+  __TEXT.__text: 0x3bf68
+  __TEXT.__gxf_code: 0x5150
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1cf8
+  __TEXT.__const: 0x1d3c
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__cstring: 0x2295
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x20
-  __DATA.__gxf_data: 0x80b8
+  __TEXT.__chain_starts: 0x24
+  __DATA.__gxf_data: 0x8168
   __DATA.__data: 0x17c98
   __DATA._rtk_init_stack: 0x4000
   __DATA.__const: 0x830

   __DATA.__zerofill: 0x5b1d8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 433
-  Symbols:   187
+  Symbols:   191
   CStrings:  233
 
Symbols:
+ _agfUPPLRegisterPageCount
+ _agfUPPLRegisterPages
+ _gClientFunctions
+ _premap_ranges
Functions:
~ sub_fffffc000000a864 : 316 -> 332
~ sub_fffffc000000b2b0 -> sub_fffffc000000b2c0 : 10924 -> 11008
~ sub_fffffc00000331cc -> sub_fffffc0000033230 : 384 -> 388
~ sub_fffffc0000037c74 -> sub_fffffc0000037cdc : 432 -> 468
~ sub_fffffc0000037e24 -> sub_fffffc0000037eb0 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:20:38"
- "Aug 30 2026 19:12:42"
```
