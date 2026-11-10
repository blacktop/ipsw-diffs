## agx_b000

> `Firmware/agx/armfw_g15s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x503a8
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x5062c
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1120
+  __TEXT.__const: 0x1160
   __TEXT.__cstring: 0x27a4
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_fffffc00000176f4 : 20312 -> 20328
~ sub_fffffc000001ceb8 -> sub_fffffc000001cec8 : 1832 -> 1896
~ sub_fffffc000001f0bc -> sub_fffffc000001f10c : 1212 -> 1232
~ sub_fffffc0000021ac0 -> sub_fffffc0000021b24 : 1672 -> 1740
~ sub_fffffc00000223c0 -> sub_fffffc0000022468 : 1848 -> 1976
~ sub_fffffc0000022af8 -> sub_fffffc0000022c20 : 1092 -> 1172
~ sub_fffffc00000232d0 -> sub_fffffc0000023448 : 1444 -> 1588
~ sub_fffffc00000290c0 -> sub_fffffc00000292c8 : 936 -> 928
~ __rtk_arm_start_bootstrap_area : 1892 -> 1872
~ sub_fffffc0000041794 -> sub_fffffc0000041980 : 384 -> 388
~ sub_fffffc000004a638 -> sub_fffffc000004a828 : 436 -> 472
~ sub_fffffc000004a7ec -> sub_fffffc000004aa00 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:11:37"
- "Aug 30 2026 19:02:49"
```
