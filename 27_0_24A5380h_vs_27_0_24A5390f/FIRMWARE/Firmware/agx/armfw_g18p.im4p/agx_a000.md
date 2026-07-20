## agx_a000

> `Firmware/agx/armfw_g18p.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3cae8
+  __TEXT.__text: 0x3ca9c
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1067
+  __TEXT.__const: 0x1068
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x2324
+  __TEXT.__cstring: 0x2322
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc0000023aac : 368 -> 384
~ sub_fffffc000002b130 -> sub_fffffc000002b140 : 112 -> 116
~ sub_fffffc000002cff4 -> sub_fffffc000002d008 : 832 -> 836
~ sub_fffffc000002de30 -> sub_fffffc000002de48 : 724 -> 720
~ sub_fffffc000002ebf8 -> sub_fffffc000002ec0c : 368 -> 364
~ sub_fffffc000002edf4 -> sub_fffffc000002ee04 : 468 -> 456
~ sub_fffffc000002f030 -> sub_fffffc000002f034 : 664 -> 652
~ sub_fffffc000002f2c8 -> sub_fffffc000002f2c0 : 1008 -> 992
~ sub_fffffc000002f6b8 -> sub_fffffc000002f6a0 : 268 -> 256
~ sub_fffffc000002fb78 -> sub_fffffc000002fb54 : 956 -> 988
~ sub_fffffc0000030abc -> sub_fffffc0000030ab8 : 328 -> 324
~ sub_fffffc0000031154 -> sub_fffffc000003114c : 468 -> 480
~ sub_fffffc0000031434 -> sub_fffffc0000031438 : 2832 -> 2840
~ sub_fffffc0000034694 -> sub_fffffc00000346a0 : 196 -> 192
~ sub_fffffc0000035bc4 -> sub_fffffc0000035bcc : 528 -> 524
~ sub_fffffc000003794c -> sub_fffffc0000037950 : 656 -> 652
~ sub_fffffc0000037bdc : 796 -> 792
~ sub_fffffc0000037fa0 -> sub_fffffc0000037f9c : 672 -> 668
~ sub_fffffc0000038400 -> sub_fffffc00000383f8 : 228 -> 224
~ sub_fffffc00000390cc -> sub_fffffc00000390c0 : 544 -> 532
~ sub_fffffc000003a404 -> sub_fffffc000003a3ec : 800 -> 816
~ sub_fffffc000003ab30 -> sub_fffffc000003ab28 : 508 -> 504
~ sub_fffffc000003b00c -> sub_fffffc000003b000 : 552 -> 540
~ sub_fffffc000003b2c4 -> sub_fffffc000003b2ac : 212 -> 200
~ sub_fffffc000003b8fc -> sub_fffffc000003b8d8 : 208 -> 204
~ sub_fffffc000003bef0 -> sub_fffffc000003bec8 : 2316 -> 2284
~ sub_fffffc000003c9a0 -> sub_fffffc000003c958 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:09:00"
- "!MIDR: 0x%llx"
- "Jun 30 2026 21:02:13"
```
