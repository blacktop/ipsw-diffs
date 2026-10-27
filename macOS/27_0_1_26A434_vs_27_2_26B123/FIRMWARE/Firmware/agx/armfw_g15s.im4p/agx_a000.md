## agx_a000

> `Firmware/agx/armfw_g15s.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x507d4
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x50a58
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1120
+  __TEXT.__const: 0x1160
   __TEXT.__cstring: 0x27c1
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc00000176d0 : 20268 -> 20284
~ sub_fffffc000001ce68 -> sub_fffffc000001ce78 : 1832 -> 1896
~ sub_fffffc000001f06c -> sub_fffffc000001f0bc : 1212 -> 1232
~ sub_fffffc0000021a70 -> sub_fffffc0000021ad4 : 1672 -> 1740
~ sub_fffffc0000022370 -> sub_fffffc0000022418 : 1848 -> 1976
~ sub_fffffc0000022aa8 -> sub_fffffc0000022bd0 : 1092 -> 1172
~ sub_fffffc0000023280 -> sub_fffffc00000233f8 : 1444 -> 1588
~ sub_fffffc0000029158 -> sub_fffffc0000029360 : 936 -> 928
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc0000041bc0 -> sub_fffffc0000041dac : 384 -> 388
~ sub_fffffc000004aa64 -> sub_fffffc000004ac54 : 436 -> 472
~ sub_fffffc000004ac18 -> sub_fffffc000004ae2c : 428 -> 540
~ sub_fffffc0000050690 -> sub_fffffc0000050914 : 324 -> 332
CStrings:
+ "Oct 14 2026 23:07:07"
- "Aug 30 2026 18:58:03"
```
