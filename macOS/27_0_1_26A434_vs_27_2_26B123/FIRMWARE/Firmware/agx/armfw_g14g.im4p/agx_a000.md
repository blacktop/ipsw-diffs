## agx_a000

> `Firmware/agx/armfw_g14g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x524f0
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x52574
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1f14
+  __TEXT.__const: 0x1f28
   __TEXT.__cstring: 0x20d1
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ __rtk_arm_start_bootstrap_area : 1888 -> 1868
~ sub_ffffff8000043e90 -> sub_ffffff8000043e7c : 648 -> 652
~ sub_ffffff800004cd3c -> sub_ffffff800004cd2c : 436 -> 472
~ sub_ffffff800004cef0 -> sub_ffffff800004cf04 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:05:46"
- "Aug 30 2026 18:56:46"
```
