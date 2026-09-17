## agx_a000

> `Firmware/agx/armfw_g17p.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3c044
+  __TEXT.__text: 0x3c058
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1cf8
+  __TEXT.__const: 0x1d0d
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__cstring: 0x2303
Functions:
~ sub_fffffc000000a864 : 316 -> 332
~ sub_fffffc00000333a4 -> sub_fffffc00000333b4 : 384 -> 388
~ sub_fffffc000003bf00 -> sub_fffffc000003bf14 : 324 -> 332
```
