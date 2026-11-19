## agx_b000

> `Firmware/agx/armfw_g15c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52dc0
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x5304c
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x11b8
+  __TEXT.__const: 0x11f8
   __TEXT.__cstring: 0x2bb2
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc0000018020 : 20312 -> 20328
~ sub_fffffc000001d7e4 -> sub_fffffc000001d7f4 : 1832 -> 1896
~ sub_fffffc000001f9e8 -> sub_fffffc000001fa38 : 1212 -> 1232
~ sub_fffffc00000223ec -> sub_fffffc0000022450 : 1672 -> 1740
~ sub_fffffc0000022cec -> sub_fffffc0000022d94 : 1848 -> 1976
~ sub_fffffc0000023424 -> sub_fffffc000002354c : 1092 -> 1172
~ sub_fffffc0000023bfc -> sub_fffffc0000023d74 : 1444 -> 1588
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc0000043744 -> sub_fffffc0000043938 : 384 -> 388
~ sub_fffffc000004cfb8 -> sub_fffffc000004d1b0 : 436 -> 472
~ sub_fffffc000004d16c -> sub_fffffc000004d388 : 428 -> 540
~ sub_fffffc0000052c80 -> sub_fffffc0000052f0c : 320 -> 328
CStrings:
+ "Oct 14 2026 23:11:42"
- "Aug 30 2026 19:02:57"
```
