## agx_b000

> `Firmware/agx/armfw_g17p.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3b948
+  __TEXT.__text: 0x3b8fc
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
~ sub_fffffc0000029f68 -> sub_fffffc0000029f78 : 112 -> 116
~ sub_fffffc000002be2c -> sub_fffffc000002be40 : 832 -> 836
~ sub_fffffc000002cc68 -> sub_fffffc000002cc80 : 724 -> 720
~ sub_fffffc000002da30 -> sub_fffffc000002da44 : 368 -> 364
~ sub_fffffc000002dc2c -> sub_fffffc000002dc3c : 468 -> 456
~ sub_fffffc000002de68 -> sub_fffffc000002de6c : 664 -> 652
~ sub_fffffc000002e100 -> sub_fffffc000002e0f8 : 1008 -> 992
~ sub_fffffc000002e4f0 -> sub_fffffc000002e4d8 : 268 -> 256
~ sub_fffffc000002e9b0 -> sub_fffffc000002e98c : 956 -> 988
~ sub_fffffc000002f8f4 -> sub_fffffc000002f8f0 : 328 -> 324
~ sub_fffffc000002ff8c -> sub_fffffc000002ff84 : 468 -> 480
~ sub_fffffc000003026c -> sub_fffffc0000030270 : 2832 -> 2840
~ sub_fffffc00000334cc -> sub_fffffc00000334d8 : 196 -> 192
~ sub_fffffc00000349fc -> sub_fffffc0000034a04 : 528 -> 524
~ sub_fffffc0000036784 -> sub_fffffc0000036788 : 656 -> 652
~ sub_fffffc0000036a14 : 796 -> 792
~ sub_fffffc0000036dd8 -> sub_fffffc0000036dd4 : 672 -> 668
~ sub_fffffc0000037238 -> sub_fffffc0000037230 : 228 -> 224
~ sub_fffffc0000037f04 -> sub_fffffc0000037ef8 : 544 -> 532
~ sub_fffffc000003923c -> sub_fffffc0000039224 : 800 -> 816
~ sub_fffffc0000039968 -> sub_fffffc0000039960 : 508 -> 504
~ sub_fffffc0000039e44 -> sub_fffffc0000039e38 : 552 -> 540
~ sub_fffffc000003a0fc -> sub_fffffc000003a0e4 : 212 -> 200
~ sub_fffffc000003a734 -> sub_fffffc000003a710 : 208 -> 204
~ sub_fffffc000003ad40 -> sub_fffffc000003ad18 : 2332 -> 2300
~ sub_fffffc000003b800 -> sub_fffffc000003b7b8 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:27:53"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:39:50"
```
