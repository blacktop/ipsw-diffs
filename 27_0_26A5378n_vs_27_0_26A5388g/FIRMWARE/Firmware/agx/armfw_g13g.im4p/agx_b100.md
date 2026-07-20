## agx_b100

> `Firmware/agx/armfw_g13g.im4p/agx_b100`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`

```diff

-  __TEXT.__text: 0x40f28
-  __TEXT.__gxf_code: 0x1154
+  __TEXT.__text: 0x40edc
+  __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1d3c
-  __TEXT.__cstring: 0x1c57
+  __TEXT.__cstring: 0x1c55
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x1e8
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff8000031048 : 348 -> 356
~ sub_ffffff8000031688 -> sub_ffffff8000031690 : 88 -> 92
~ sub_ffffff800003510c -> sub_ffffff8000035118 : 196 -> 192
~ sub_ffffff80000363c0 -> sub_ffffff80000363c8 : 528 -> 524
~ sub_ffffff8000036f5c -> sub_ffffff8000036f60 : 668 -> 672
~ sub_ffffff8000037e8c -> sub_ffffff8000037e94 : 368 -> 364
~ sub_ffffff8000038088 -> sub_ffffff800003808c : 468 -> 456
~ sub_ffffff80000382c4 -> sub_ffffff80000382bc : 664 -> 652
~ sub_ffffff800003855c -> sub_ffffff8000038548 : 1016 -> 1000
~ sub_ffffff8000038954 -> sub_ffffff8000038930 : 268 -> 256
~ sub_ffffff8000038e1c -> sub_ffffff8000038dec : 960 -> 992
~ sub_ffffff8000039808 -> sub_ffffff80000397f8 : 484 -> 496
~ sub_ffffff800003ae5c -> sub_ffffff800003ae58 : 668 -> 664
~ sub_ffffff800003b0f8 -> sub_ffffff800003b0f0 : 796 -> 792
~ sub_ffffff800003b4c0 -> sub_ffffff800003b4b4 : 672 -> 668
~ sub_ffffff800003b920 -> sub_ffffff800003b910 : 228 -> 224
~ sub_ffffff800003c5f0 -> sub_ffffff800003c5dc : 544 -> 532
~ sub_ffffff800003d91c -> sub_ffffff800003d8fc : 800 -> 816
~ sub_ffffff800003e048 -> sub_ffffff800003e038 : 508 -> 504
~ sub_ffffff800003e528 -> sub_ffffff800003e514 : 552 -> 540
~ sub_ffffff800003e7e0 -> sub_ffffff800003e7c0 : 212 -> 200
~ sub_ffffff800003ef24 -> sub_ffffff800003eef8 : 208 -> 204
~ sub_ffffff800003eff4 -> sub_ffffff800003efc4 : 3196 -> 3204
~ sub_ffffff80000403f4 -> sub_ffffff80000403cc : 2124 -> 2092
~ sub_ffffff8000040de0 -> sub_ffffff8000040d98 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:26:20"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:37:54"
```
