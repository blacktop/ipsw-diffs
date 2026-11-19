## agx_b000

> `Firmware/agx/armfw_g18g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3c7f8
-  __TEXT.__gxf_code: 0x4f40
+  __TEXT.__text: 0x3c8f0
+  __TEXT.__gxf_code: 0x4f60
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x20cc
+  __TEXT.__const: 0x2110
   __TEXT._rtk_patchbay: 0x23a
   __TEXT._rtk_tunables: 0x7e0
   __TEXT.__cstring: 0x247d
Functions:
~ sub_fffffc000000baf0 : 316 -> 332
~ sub_fffffc000000c3d0 -> sub_fffffc000000c3e0 : 10524 -> 10604
~ sub_fffffc0000033880 -> sub_fffffc00000338e0 : 648 -> 652
~ sub_fffffc0000038994 -> sub_fffffc00000389f8 : 436 -> 472
~ sub_fffffc0000038b48 -> sub_fffffc0000038bd0 : 428 -> 540
~ sub_fffffc000003c6b4 -> sub_fffffc000003c7ac : 332 -> 324
CStrings:
+ "Oct 14 2026 23:16:51"
- "Aug 30 2026 19:08:35"
```
