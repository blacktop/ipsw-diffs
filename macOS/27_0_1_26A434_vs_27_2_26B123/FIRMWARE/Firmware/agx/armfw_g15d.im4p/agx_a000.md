## agx_a000

> `Firmware/agx/armfw_g15d.im4p/agx_a000`

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

-  __TEXT.__text: 0x53df8
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x54080
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x12a8
+  __TEXT.__const: 0x12e8
   __TEXT.__cstring: 0x2bcf
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc0000018b04 : 20304 -> 20316
~ sub_fffffc000001e2c0 -> sub_fffffc000001e2cc : 1832 -> 1896
~ sub_fffffc00000204c4 -> sub_fffffc0000020510 : 1212 -> 1232
~ sub_fffffc0000022ec8 -> sub_fffffc0000022f28 : 1672 -> 1740
~ sub_fffffc00000237c8 -> sub_fffffc000002386c : 1848 -> 1976
~ sub_fffffc0000023f00 -> sub_fffffc0000024024 : 1092 -> 1172
~ sub_fffffc00000246d8 -> sub_fffffc000002484c : 1444 -> 1588
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc000004477c -> sub_fffffc000004496c : 384 -> 388
~ sub_fffffc000004dff0 -> sub_fffffc000004e1e4 : 436 -> 472
~ sub_fffffc000004e1a4 -> sub_fffffc000004e3bc : 428 -> 540
~ sub_fffffc0000053cb8 -> sub_fffffc0000053f40 : 328 -> 320
CStrings:
+ "Oct 14 2026 23:07:10"
- "Aug 30 2026 18:58:07"
```
