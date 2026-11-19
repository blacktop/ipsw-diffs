## agx_b100

> `Firmware/agx/armfw_g13g.im4p/agx_b100`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`

```diff

-  __TEXT.__text: 0x4101c
-  __TEXT.__gxf_code: 0x1150
+  __TEXT.__text: 0x410a0
+  __TEXT.__gxf_code: 0x10e4
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1d3c
+  __TEXT.__const: 0x1d50
   __TEXT.__cstring: 0x1c79
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x1e8
Functions:
~ __rtk_arm_start_bootstrap_area : 1888 -> 1868
~ sub_ffffff8000034994 -> sub_ffffff8000034980 : 648 -> 652
~ sub_ffffff800003bf24 -> sub_ffffff800003bf14 : 436 -> 472
~ sub_ffffff800003c0d8 -> sub_ffffff800003c0ec : 428 -> 540
~ sub_ffffff8000040ed8 -> sub_ffffff8000040f5c : 332 -> 324
CStrings:
+ "Oct 14 2026 23:16:33"
- "Aug 30 2026 19:08:02"
```
