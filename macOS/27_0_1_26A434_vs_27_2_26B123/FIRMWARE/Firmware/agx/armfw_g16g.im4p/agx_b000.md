## agx_b000

> `Firmware/agx/armfw_g16g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52740
-  __TEXT.__gxf_code: 0x5080
+  __TEXT.__text: 0x529a0
+  __TEXT.__gxf_code: 0x5220
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1db8
-  __TEXT.__cstring: 0x26a2
+  __TEXT.__const: 0x1dfc
+  __TEXT.__cstring: 0x26bf
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
-  __DATA.__gxf_data: 0x81b0
+  __DATA.__gxf_data: 0x81e8
   __DATA.__data: 0xeb8
   __DATA._rtk_init_stack: 0x4000
   __DATA.__const: 0xb40

   __DATA.__zerofill: 0x7a298
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 517
-  Symbols:   189
-  CStrings:  268
+  Symbols:   191
+  CStrings:  269
 
Symbols:
+ _agfUPPLRegisterPageCount
+ _agfUPPLRegisterPages
Functions:
~ sub_fffffc00000123d0 : 4800 -> 4876
~ sub_fffffc0000019238 -> sub_fffffc0000019284 : 17556 -> 17392
~ sub_fffffc000001df24 -> sub_fffffc000001decc : 1832 -> 1900
~ sub_fffffc0000020140 -> sub_fffffc000002012c : 1828 -> 1848
~ sub_fffffc0000023540 : 1596 -> 1664
~ sub_fffffc0000023d34 -> sub_fffffc0000023d78 : 1988 -> 2116
~ sub_fffffc00000244f8 -> sub_fffffc00000245bc : 1088 -> 1164
~ sub_fffffc0000024a5c -> sub_fffffc0000024b6c : 1460 -> 1592
~ sub_fffffc00000284c0 -> sub_fffffc0000028654 : 640 -> 684
~ sub_fffffc000002e168 -> sub_fffffc000002e328 : 44 -> 76
~ sub_fffffc000003041c -> sub_fffffc00000305fc : 1568 -> 1472
~ sub_fffffc00000377d0 -> sub_fffffc0000037950 : 1492 -> 1528
~ sub_fffffc000003da20 -> sub_fffffc000003dbc4 : 5292 -> 5328
~ sub_fffffc0000049700 -> sub_fffffc00000498c8 : 384 -> 388
~ sub_fffffc000004dff0 -> sub_fffffc000004e1bc : 436 -> 472
~ sub_fffffc000004e1a4 -> sub_fffffc000004e394 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:10:56"
+ "uPPL extension %u failed: %d"
- "Aug 30 2026 19:02:05"
```
