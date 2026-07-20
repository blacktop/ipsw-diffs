## agx_b000

> `Firmware/agx/armfw_g16g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52614
+  __TEXT.__text: 0x525b8
   __TEXT.__gxf_code: 0x5080
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1db7
-  __TEXT.__cstring: 0x2680
+  __TEXT.__const: 0x1db8
+  __TEXT.__cstring: 0x267e
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc000003fbfc : 112 -> 116
~ sub_fffffc0000041ad0 -> sub_fffffc0000041ad4 : 832 -> 836
~ sub_fffffc000004290c -> sub_fffffc0000042914 : 724 -> 720
~ sub_fffffc00000436d0 -> sub_fffffc00000436d4 : 368 -> 364
~ sub_fffffc00000438cc : 468 -> 456
~ sub_fffffc0000043b08 -> sub_fffffc0000043afc : 664 -> 652
~ sub_fffffc0000043da0 -> sub_fffffc0000043d88 : 1008 -> 992
~ sub_fffffc0000044190 -> sub_fffffc0000044168 : 268 -> 256
~ sub_fffffc0000044650 -> sub_fffffc000004461c : 956 -> 988
~ sub_fffffc0000045594 -> sub_fffffc0000045580 : 328 -> 324
~ sub_fffffc0000045998 -> sub_fffffc0000045980 : 420 -> 416
~ sub_fffffc0000046624 -> sub_fffffc0000046608 : 468 -> 480
~ sub_fffffc0000046904 -> sub_fffffc00000468f4 : 3188 -> 3196
~ sub_fffffc0000049e60 -> sub_fffffc0000049e58 : 196 -> 192
~ sub_fffffc000004b198 -> sub_fffffc000004b18c : 520 -> 516
~ sub_fffffc000004cf18 -> sub_fffffc000004cf08 : 664 -> 660
~ sub_fffffc000004d1b0 -> sub_fffffc000004d19c : 784 -> 772
~ sub_fffffc000004d568 -> sub_fffffc000004d548 : 664 -> 660
~ sub_fffffc000004d9c0 -> sub_fffffc000004d99c : 228 -> 224
~ sub_fffffc000004e688 -> sub_fffffc000004e660 : 544 -> 532
~ sub_fffffc000004fac4 -> sub_fffffc000004fa90 : 788 -> 804
~ sub_fffffc00000501e4 -> sub_fffffc00000501c0 : 508 -> 504
~ sub_fffffc00000506c0 -> sub_fffffc0000050698 : 420 -> 412
~ sub_fffffc00000508f4 -> sub_fffffc00000508c4 : 212 -> 200
~ sub_fffffc0000050de0 -> sub_fffffc0000050da4 : 328 -> 324
~ sub_fffffc0000050f28 -> sub_fffffc0000050ee8 : 208 -> 204
~ sub_fffffc00000517fc -> sub_fffffc00000517b8 : 2868 -> 2848
~ sub_fffffc00000524d0 -> sub_fffffc0000052478 : 324 -> 328
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:25:17"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:36:40"
```
