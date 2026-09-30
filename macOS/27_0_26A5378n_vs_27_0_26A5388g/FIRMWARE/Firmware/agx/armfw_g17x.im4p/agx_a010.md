## agx_a010

> `Firmware/agx/armfw_g17x.im4p/agx_a010`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3c798
+  __TEXT.__text: 0x3c74c
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x119f
+  __TEXT.__const: 0x11a0
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x21bb
+  __TEXT.__cstring: 0x21b9
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc0000023560 : 368 -> 384
~ sub_fffffc000002acd8 -> sub_fffffc000002ace8 : 112 -> 116
~ sub_fffffc000002cb9c -> sub_fffffc000002cbb0 : 832 -> 836
~ sub_fffffc000002d9d8 -> sub_fffffc000002d9f0 : 724 -> 720
~ sub_fffffc000002e7a0 -> sub_fffffc000002e7b4 : 368 -> 364
~ sub_fffffc000002e99c -> sub_fffffc000002e9ac : 468 -> 456
~ sub_fffffc000002ebd8 -> sub_fffffc000002ebdc : 664 -> 652
~ sub_fffffc000002ee70 -> sub_fffffc000002ee68 : 1008 -> 992
~ sub_fffffc000002f260 -> sub_fffffc000002f248 : 268 -> 256
~ sub_fffffc000002f720 -> sub_fffffc000002f6fc : 956 -> 988
~ sub_fffffc0000030664 -> sub_fffffc0000030660 : 328 -> 324
~ sub_fffffc0000030cfc -> sub_fffffc0000030cf4 : 468 -> 480
~ sub_fffffc0000030fdc -> sub_fffffc0000030fe0 : 2824 -> 2832
~ sub_fffffc0000034180 -> sub_fffffc000003418c : 196 -> 192
~ sub_fffffc00000356a8 -> sub_fffffc00000356b0 : 528 -> 524
~ sub_fffffc000003742c -> sub_fffffc0000037430 : 656 -> 652
~ sub_fffffc00000376bc : 796 -> 792
~ sub_fffffc0000037a80 -> sub_fffffc0000037a7c : 672 -> 668
~ sub_fffffc0000037ee0 -> sub_fffffc0000037ed8 : 228 -> 224
~ sub_fffffc0000038ba8 -> sub_fffffc0000038b9c : 544 -> 532
~ sub_fffffc0000039ee4 -> sub_fffffc0000039ecc : 800 -> 816
~ sub_fffffc000003a610 -> sub_fffffc000003a608 : 508 -> 504
~ sub_fffffc000003aaf4 -> sub_fffffc000003aae8 : 552 -> 540
~ sub_fffffc000003adac -> sub_fffffc000003ad94 : 212 -> 200
~ sub_fffffc000003b3e4 -> sub_fffffc000003b3c0 : 208 -> 204
~ sub_fffffc000003bb20 -> sub_fffffc000003baf8 : 2444 -> 2412
~ sub_fffffc000003c650 -> sub_fffffc000003c608 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:22:07"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:32:44"
```
