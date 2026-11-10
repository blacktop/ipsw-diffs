## agx_b000

> `Firmware/agx/armfw_g15g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x54e14
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x550b0
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x23f4
+  __TEXT.__const: 0x2438
   __TEXT.__cstring: 0x25c8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc0000018e78 : 19420 -> 19460
~ sub_fffffc000001e2b4 -> sub_fffffc000001e2dc : 1832 -> 1896
~ sub_fffffc00000204d0 -> sub_fffffc0000020538 : 1828 -> 1848
~ sub_fffffc00000230a0 -> sub_fffffc000002311c : 1596 -> 1664
~ sub_fffffc0000023894 -> sub_fffffc0000023954 : 1988 -> 2116
~ sub_fffffc0000024058 -> sub_fffffc0000024198 : 1016 -> 1096
~ sub_fffffc00000246e0 -> sub_fffffc0000024870 : 1460 -> 1596
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc00000467bc -> sub_fffffc00000469c0 : 648 -> 652
~ sub_fffffc000004f668 -> sub_fffffc000004f870 : 436 -> 472
~ sub_fffffc000004f81c -> sub_fffffc000004fa48 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:10:16"
- "Aug 30 2026 19:01:32"
```
