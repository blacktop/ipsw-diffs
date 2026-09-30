## agx_a010

> `Firmware/agx/armfw_g18p.im4p/agx_a010`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3c704
+  __TEXT.__text: 0x3c6b8
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1067
+  __TEXT.__const: 0x1068
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x23da
+  __TEXT.__cstring: 0x23d8
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc0000023658 : 368 -> 384
~ sub_fffffc000002ad4c -> sub_fffffc000002ad5c : 112 -> 116
~ sub_fffffc000002cc10 -> sub_fffffc000002cc24 : 832 -> 836
~ sub_fffffc000002da4c -> sub_fffffc000002da64 : 724 -> 720
~ sub_fffffc000002e814 -> sub_fffffc000002e828 : 368 -> 364
~ sub_fffffc000002ea10 -> sub_fffffc000002ea20 : 468 -> 456
~ sub_fffffc000002ec4c -> sub_fffffc000002ec50 : 664 -> 652
~ sub_fffffc000002eee4 -> sub_fffffc000002eedc : 1008 -> 992
~ sub_fffffc000002f2d4 -> sub_fffffc000002f2bc : 268 -> 256
~ sub_fffffc000002f794 -> sub_fffffc000002f770 : 956 -> 988
~ sub_fffffc00000306d8 -> sub_fffffc00000306d4 : 328 -> 324
~ sub_fffffc0000030d70 -> sub_fffffc0000030d68 : 468 -> 480
~ sub_fffffc0000031050 -> sub_fffffc0000031054 : 2832 -> 2840
~ sub_fffffc00000342b0 -> sub_fffffc00000342bc : 196 -> 192
~ sub_fffffc00000357e0 -> sub_fffffc00000357e8 : 528 -> 524
~ sub_fffffc0000037568 -> sub_fffffc000003756c : 656 -> 652
~ sub_fffffc00000377f8 : 796 -> 792
~ sub_fffffc0000037bbc -> sub_fffffc0000037bb8 : 672 -> 668
~ sub_fffffc000003801c -> sub_fffffc0000038014 : 228 -> 224
~ sub_fffffc0000038ce8 -> sub_fffffc0000038cdc : 544 -> 532
~ sub_fffffc000003a020 -> sub_fffffc000003a008 : 800 -> 816
~ sub_fffffc000003a74c -> sub_fffffc000003a744 : 508 -> 504
~ sub_fffffc000003ac28 -> sub_fffffc000003ac1c : 552 -> 540
~ sub_fffffc000003aee0 -> sub_fffffc000003aec8 : 212 -> 200
~ sub_fffffc000003b518 -> sub_fffffc000003b4f4 : 208 -> 204
~ sub_fffffc000003bb0c -> sub_fffffc000003bae4 : 2316 -> 2284
~ sub_fffffc000003c5bc -> sub_fffffc000003c574 : 328 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:20:06"
- "!MIDR: 0x%llx"
- "Jun 30 2026 21:10:43"
```
