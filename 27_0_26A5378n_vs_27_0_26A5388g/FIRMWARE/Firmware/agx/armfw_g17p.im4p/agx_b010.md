## agx_b010

> `Firmware/agx/armfw_g17p.im4p/agx_b010`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3b858
+  __TEXT.__text: 0x3b80c
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1cf7
+  __TEXT.__const: 0x1cf8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2273
+  __TEXT.__cstring: 0x2271
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc0000023178 : 368 -> 384
~ sub_fffffc0000029e78 -> sub_fffffc0000029e88 : 112 -> 116
~ sub_fffffc000002bd3c -> sub_fffffc000002bd50 : 832 -> 836
~ sub_fffffc000002cb78 -> sub_fffffc000002cb90 : 724 -> 720
~ sub_fffffc000002d940 -> sub_fffffc000002d954 : 368 -> 364
~ sub_fffffc000002db3c -> sub_fffffc000002db4c : 468 -> 456
~ sub_fffffc000002dd78 -> sub_fffffc000002dd7c : 664 -> 652
~ sub_fffffc000002e010 -> sub_fffffc000002e008 : 1008 -> 992
~ sub_fffffc000002e400 -> sub_fffffc000002e3e8 : 268 -> 256
~ sub_fffffc000002e8c0 -> sub_fffffc000002e89c : 956 -> 988
~ sub_fffffc000002f804 -> sub_fffffc000002f800 : 328 -> 324
~ sub_fffffc000002fe9c -> sub_fffffc000002fe94 : 468 -> 480
~ sub_fffffc000003017c -> sub_fffffc0000030180 : 2832 -> 2840
~ sub_fffffc00000333dc -> sub_fffffc00000333e8 : 196 -> 192
~ sub_fffffc000003490c -> sub_fffffc0000034914 : 528 -> 524
~ sub_fffffc0000036694 -> sub_fffffc0000036698 : 656 -> 652
~ sub_fffffc0000036924 : 796 -> 792
~ sub_fffffc0000036ce8 -> sub_fffffc0000036ce4 : 672 -> 668
~ sub_fffffc0000037148 -> sub_fffffc0000037140 : 228 -> 224
~ sub_fffffc0000037e14 -> sub_fffffc0000037e08 : 544 -> 532
~ sub_fffffc000003914c -> sub_fffffc0000039134 : 800 -> 816
~ sub_fffffc0000039878 -> sub_fffffc0000039870 : 508 -> 504
~ sub_fffffc0000039d54 -> sub_fffffc0000039d48 : 552 -> 540
~ sub_fffffc000003a00c -> sub_fffffc0000039ff4 : 212 -> 200
~ sub_fffffc000003a644 -> sub_fffffc000003a620 : 208 -> 204
~ sub_fffffc000003ac50 -> sub_fffffc000003ac28 : 2332 -> 2300
~ sub_fffffc000003b710 -> sub_fffffc000003b6c8 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:33:23"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:46:17"
```
