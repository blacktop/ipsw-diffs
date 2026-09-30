## agx_c000

> `Firmware/agx/armfw_g17g.im4p/agx_c000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3d4c4
+  __TEXT.__text: 0x3d4d8
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1070
+  __TEXT.__const: 0x1085
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2426
Functions:
~ sub_fffffc000000b478 : 316 -> 332
~ sub_fffffc00000347ec -> sub_fffffc00000347fc : 384 -> 388
~ sub_fffffc000003d380 -> sub_fffffc000003d394 : 324 -> 332
```
