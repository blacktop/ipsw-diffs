## agx_a000

> `Firmware/agx/armfw_g17p.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3bb20
+  __TEXT.__text: 0x3bad4
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1cf7
+  __TEXT.__const: 0x1cf8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x22e1
+  __TEXT.__cstring: 0x22df
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc0000023350 : 368 -> 384
~ sub_fffffc000002a140 -> sub_fffffc000002a150 : 112 -> 116
~ sub_fffffc000002c004 -> sub_fffffc000002c018 : 832 -> 836
~ sub_fffffc000002ce40 -> sub_fffffc000002ce58 : 724 -> 720
~ sub_fffffc000002dc08 -> sub_fffffc000002dc1c : 368 -> 364
~ sub_fffffc000002de04 -> sub_fffffc000002de14 : 468 -> 456
~ sub_fffffc000002e040 -> sub_fffffc000002e044 : 664 -> 652
~ sub_fffffc000002e2d8 -> sub_fffffc000002e2d0 : 1008 -> 992
~ sub_fffffc000002e6c8 -> sub_fffffc000002e6b0 : 268 -> 256
~ sub_fffffc000002eb88 -> sub_fffffc000002eb64 : 956 -> 988
~ sub_fffffc000002facc -> sub_fffffc000002fac8 : 328 -> 324
~ sub_fffffc0000030164 -> sub_fffffc000003015c : 468 -> 480
~ sub_fffffc0000030444 -> sub_fffffc0000030448 : 2832 -> 2840
~ sub_fffffc00000336a4 -> sub_fffffc00000336b0 : 196 -> 192
~ sub_fffffc0000034bd4 -> sub_fffffc0000034bdc : 528 -> 524
~ sub_fffffc000003695c -> sub_fffffc0000036960 : 656 -> 652
~ sub_fffffc0000036bec : 796 -> 792
~ sub_fffffc0000036fb0 -> sub_fffffc0000036fac : 672 -> 668
~ sub_fffffc0000037410 -> sub_fffffc0000037408 : 228 -> 224
~ sub_fffffc00000380dc -> sub_fffffc00000380d0 : 544 -> 532
~ sub_fffffc0000039414 -> sub_fffffc00000393fc : 800 -> 816
~ sub_fffffc0000039b40 -> sub_fffffc0000039b38 : 508 -> 504
~ sub_fffffc000003a01c -> sub_fffffc000003a010 : 552 -> 540
~ sub_fffffc000003a2d4 -> sub_fffffc000003a2bc : 212 -> 200
~ sub_fffffc000003a90c -> sub_fffffc000003a8e8 : 208 -> 204
~ sub_fffffc000003af18 -> sub_fffffc000003aef0 : 2332 -> 2300
~ sub_fffffc000003b9d8 -> sub_fffffc000003b990 : 328 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:21:10"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:31:47"
```
