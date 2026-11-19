## agx_a000

> `Firmware/agx/armfw_g13g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`

```diff

-  __TEXT.__text: 0x40fac
-  __TEXT.__gxf_code: 0x1150
+  __TEXT.__text: 0x41030
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
~ sub_ffffff8000034924 -> sub_ffffff8000034910 : 648 -> 652
~ sub_ffffff800003beb4 -> sub_ffffff800003bea4 : 436 -> 472
~ sub_ffffff800003c068 -> sub_ffffff800003c07c : 428 -> 540
~ sub_ffffff8000040e68 -> sub_ffffff8000040eec : 332 -> 324
CStrings:
+ "Oct 14 2026 23:13:14"
- "Aug 30 2026 19:04:32"
```
