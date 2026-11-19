## agx_a000

> `Firmware/agx/armfw_g16g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52c34
-  __TEXT.__gxf_code: 0x5080
+  __TEXT.__text: 0x52df0
+  __TEXT.__gxf_code: 0x5220
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1d78
-  __TEXT.__cstring: 0x2722
+  __TEXT.__const: 0x1dbc
+  __TEXT.__cstring: 0x273f
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
-  __DATA.__gxf_data: 0x81b0
+  __DATA.__gxf_data: 0x81e8
   __DATA.__data: 0xeb8
   __DATA._rtk_init_stack: 0x4000
   __DATA.__const: 0xb50

   __DATA.__zerofill: 0x7a298
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 518
-  Symbols:   189
-  CStrings:  271
+  Symbols:   191
+  CStrings:  272
 
Symbols:
+ _agfUPPLRegisterPageCount
+ _agfUPPLRegisterPages
Functions:
~ sub_fffffc00000123dc : 4800 -> 4876
~ sub_fffffc0000019244 -> sub_fffffc0000019290 : 18632 -> 18304
~ sub_fffffc000001e364 -> sub_fffffc000001e268 : 1832 -> 1900
~ sub_fffffc0000020580 -> sub_fffffc00000204c8 : 1828 -> 1848
~ sub_fffffc00000239b8 -> sub_fffffc0000023914 : 1596 -> 1664
~ sub_fffffc00000241ac -> sub_fffffc000002414c : 1988 -> 2116
~ sub_fffffc0000024970 -> sub_fffffc0000024990 : 1088 -> 1164
~ sub_fffffc0000024ed4 -> sub_fffffc0000024f40 : 1460 -> 1592
~ sub_fffffc0000028938 -> sub_fffffc0000028a28 : 640 -> 684
~ sub_fffffc000002e5e0 -> sub_fffffc000002e6fc : 44 -> 76
~ sub_fffffc0000030860 -> sub_fffffc000003099c : 1568 -> 1472
~ sub_fffffc0000037cb0 -> sub_fffffc0000037d8c : 1492 -> 1528
~ sub_fffffc000003df14 -> sub_fffffc000003e014 : 5292 -> 5328
~ sub_fffffc0000049bf4 -> sub_fffffc0000049d18 : 384 -> 388
~ sub_fffffc000004e4e4 -> sub_fffffc000004e60c : 436 -> 472
~ sub_fffffc000004e698 -> sub_fffffc000004e7e4 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:06:40"
+ "uPPL extension %u failed: %d"
- "Aug 30 2026 18:57:35"
```
