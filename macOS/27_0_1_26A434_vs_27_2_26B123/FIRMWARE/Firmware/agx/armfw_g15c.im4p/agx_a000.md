## agx_a000

> `Firmware/agx/armfw_g15c.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x53204
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x53490
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x11b8
+  __TEXT.__const: 0x11f8
   __TEXT.__cstring: 0x2bcf
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc0000017ffc : 20268 -> 20284
~ sub_fffffc000001d794 -> sub_fffffc000001d7a4 : 1832 -> 1896
~ sub_fffffc000001f998 -> sub_fffffc000001f9e8 : 1212 -> 1232
~ sub_fffffc000002239c -> sub_fffffc0000022400 : 1672 -> 1740
~ sub_fffffc0000022c9c -> sub_fffffc0000022d44 : 1848 -> 1976
~ sub_fffffc00000233d4 -> sub_fffffc00000234fc : 1092 -> 1172
~ sub_fffffc0000023bac -> sub_fffffc0000023d24 : 1444 -> 1588
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc0000043b88 -> sub_fffffc0000043d7c : 384 -> 388
~ sub_fffffc000004d3fc -> sub_fffffc000004d5f4 : 436 -> 472
~ sub_fffffc000004d5b0 -> sub_fffffc000004d7cc : 428 -> 540
CStrings:
+ "Oct 14 2026 23:07:10"
- "Aug 30 2026 18:58:08"
```
