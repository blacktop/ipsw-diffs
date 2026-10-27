## agx_b000

> `Firmware/agx/armfw_g15d.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x53f14
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x5419c
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x12a8
+  __TEXT.__const: 0x12e8
   __TEXT.__cstring: 0x2bb2
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc0000018b98 : 20304 -> 20316
~ sub_fffffc000001e354 -> sub_fffffc000001e360 : 1832 -> 1896
~ sub_fffffc0000020558 -> sub_fffffc00000205a4 : 1212 -> 1232
~ sub_fffffc0000022f5c -> sub_fffffc0000022fbc : 1672 -> 1740
~ sub_fffffc000002385c -> sub_fffffc0000023900 : 1848 -> 1976
~ sub_fffffc0000023f94 -> sub_fffffc00000240b8 : 1092 -> 1172
~ sub_fffffc000002476c -> sub_fffffc00000248e0 : 1444 -> 1588
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc0000044898 -> sub_fffffc0000044a88 : 384 -> 388
~ sub_fffffc000004e10c -> sub_fffffc000004e300 : 436 -> 472
~ sub_fffffc000004e2c0 -> sub_fffffc000004e4d8 : 428 -> 540
~ sub_fffffc0000053dd4 -> sub_fffffc000005405c : 320 -> 328
CStrings:
+ "Oct 14 2026 23:11:51"
- "Aug 30 2026 19:03:03"
```
