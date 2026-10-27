## agx_c000

> `Firmware/agx/armfw_g15g.im4p/agx_c000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x54a6c
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x54d08
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x23f4
+  __TEXT.__const: 0x2438
   __TEXT.__cstring: 0x25c8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc0000018e70 : 19464 -> 19504
~ sub_fffffc000001e2d8 -> sub_fffffc000001e300 : 1832 -> 1896
~ sub_fffffc00000204f4 -> sub_fffffc000002055c : 1828 -> 1848
~ sub_fffffc00000230c4 -> sub_fffffc0000023140 : 1596 -> 1664
~ sub_fffffc00000238b8 -> sub_fffffc0000023978 : 1988 -> 2116
~ sub_fffffc000002407c -> sub_fffffc00000241bc : 1016 -> 1096
~ sub_fffffc0000024704 -> sub_fffffc0000024894 : 1460 -> 1596
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc0000046414 -> sub_fffffc0000046618 : 648 -> 652
~ sub_fffffc000004f2c0 -> sub_fffffc000004f4c8 : 436 -> 472
~ sub_fffffc000004f474 -> sub_fffffc000004f6a0 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:13:54"
- "Aug 30 2026 19:05:18"
```
