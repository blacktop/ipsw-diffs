## agx_a000

> `Firmware/agx/armfw_g17g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3d854
-  __TEXT.__gxf_code: 0x4f40
+  __TEXT.__text: 0x3d880
+  __TEXT.__gxf_code: 0x5130
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1070
+  __TEXT.__const: 0x10b4
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2370
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x20
-  __DATA.__gxf_data: 0x80b8
+  __TEXT.__chain_starts: 0x24
+  __DATA.__gxf_data: 0x8160
   __DATA.__data: 0x17d40
   __DATA._rtk_init_stack: 0x4000
   __DATA.__const: 0x7c8

   __DATA.__zerofill: 0x5a778
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 417
-  Symbols:   169
+  Symbols:   173
   CStrings:  236
 
Symbols:
+ _agfUPPLRegisterPageCount
+ _agfUPPLRegisterPages
+ _gClientFunctions
+ _premap_ranges
Functions:
~ sub_fffffc000000b8bc : 316 -> 332
~ sub_fffffc000000c30c -> sub_fffffc000000c31c : 12060 -> 11936
~ sub_fffffc0000034b7c -> sub_fffffc0000034b10 : 384 -> 388
~ sub_fffffc0000039624 -> sub_fffffc00000395bc : 432 -> 468
~ sub_fffffc00000397d4 -> sub_fffffc0000039790 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:08:17"
- "Aug 30 2026 18:59:20"
```
