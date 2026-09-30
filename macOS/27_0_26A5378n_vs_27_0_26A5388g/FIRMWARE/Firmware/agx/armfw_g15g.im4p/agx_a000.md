## agx_a000

> `Firmware/agx/armfw_g15g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4f1c8
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x4f178
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x23e4
-  __TEXT.__cstring: 0x2402
+  __TEXT.__cstring: 0x2400
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc000003d25c : 348 -> 356
~ sub_fffffc000003d89c -> sub_fffffc000003d8a4 : 88 -> 92
~ sub_fffffc00000413d8 -> sub_fffffc00000413e4 : 196 -> 192
~ sub_fffffc00000426f0 -> sub_fffffc00000426f8 : 528 -> 524
~ sub_fffffc00000432c0 -> sub_fffffc00000432c4 : 824 -> 828
~ sub_fffffc00000440f4 -> sub_fffffc00000440fc : 724 -> 720
~ sub_fffffc0000044eac -> sub_fffffc0000044eb0 : 368 -> 364
~ sub_fffffc00000450a8 : 468 -> 456
~ sub_fffffc00000452e4 -> sub_fffffc00000452d8 : 664 -> 652
~ sub_fffffc000004557c -> sub_fffffc0000045564 : 1008 -> 992
~ sub_fffffc000004596c -> sub_fffffc0000045944 : 268 -> 256
~ sub_fffffc0000045e2c -> sub_fffffc0000045df8 : 956 -> 988
~ sub_fffffc0000046d6c -> sub_fffffc0000046d58 : 328 -> 324
~ sub_fffffc0000047404 -> sub_fffffc00000473ec : 480 -> 492
~ sub_fffffc0000048a50 -> sub_fffffc0000048a44 : 668 -> 664
~ sub_fffffc0000048cec -> sub_fffffc0000048cdc : 796 -> 792
~ sub_fffffc00000490b0 -> sub_fffffc000004909c : 672 -> 668
~ sub_fffffc0000049510 -> sub_fffffc00000494f8 : 228 -> 224
~ sub_fffffc000004a1e0 -> sub_fffffc000004a1c4 : 544 -> 532
~ sub_fffffc000004b624 -> sub_fffffc000004b5fc : 800 -> 816
~ sub_fffffc000004bd50 -> sub_fffffc000004bd38 : 504 -> 500
~ sub_fffffc000004c22c -> sub_fffffc000004c210 : 420 -> 412
~ sub_fffffc000004c460 -> sub_fffffc000004c43c : 212 -> 200
~ sub_fffffc000004cba4 -> sub_fffffc000004cb74 : 208 -> 204
~ sub_fffffc000004cc74 -> sub_fffffc000004cc40 : 3200 -> 3208
~ sub_fffffc000004e42c -> sub_fffffc000004e400 : 2740 -> 2708
~ sub_fffffc000004f080 -> sub_fffffc000004f034 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:20:49"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:31:26"
```
