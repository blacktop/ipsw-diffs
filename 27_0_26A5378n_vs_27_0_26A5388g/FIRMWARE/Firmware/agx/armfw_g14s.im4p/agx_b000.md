## agx_b000

> `Firmware/agx/armfw_g14s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4e470
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x4e420
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1ef0
-  __TEXT.__cstring: 0x2349
+  __TEXT.__cstring: 0x2347
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff800003be5c : 348 -> 356
~ sub_ffffff800003c49c -> sub_ffffff800003c4a4 : 112 -> 116
~ sub_ffffff80000400d0 -> sub_ffffff80000400dc : 196 -> 192
~ sub_ffffff80000413c8 -> sub_ffffff80000413d0 : 528 -> 524
~ sub_ffffff8000041f94 -> sub_ffffff8000041f98 : 824 -> 828
~ sub_ffffff8000042dc8 -> sub_ffffff8000042dd0 : 724 -> 720
~ sub_ffffff8000043b80 -> sub_ffffff8000043b84 : 368 -> 364
~ sub_ffffff8000043d7c : 468 -> 456
~ sub_ffffff8000043fb8 -> sub_ffffff8000043fac : 664 -> 652
~ sub_ffffff8000044250 -> sub_ffffff8000044238 : 1008 -> 992
~ sub_ffffff8000044640 -> sub_ffffff8000044618 : 268 -> 256
~ sub_ffffff8000044b00 -> sub_ffffff8000044acc : 956 -> 988
~ sub_ffffff8000045a40 -> sub_ffffff8000045a2c : 328 -> 324
~ sub_ffffff80000460d8 -> sub_ffffff80000460c0 : 480 -> 492
~ sub_ffffff8000047724 -> sub_ffffff8000047718 : 668 -> 664
~ sub_ffffff80000479c0 -> sub_ffffff80000479b0 : 796 -> 792
~ sub_ffffff8000047d84 -> sub_ffffff8000047d70 : 672 -> 668
~ sub_ffffff80000481e4 -> sub_ffffff80000481cc : 228 -> 224
~ sub_ffffff8000048eb0 -> sub_ffffff8000048e94 : 544 -> 532
~ sub_ffffff800004a2f8 -> sub_ffffff800004a2d0 : 800 -> 816
~ sub_ffffff800004aa24 -> sub_ffffff800004aa0c : 504 -> 500
~ sub_ffffff800004af04 -> sub_ffffff800004aee8 : 420 -> 412
~ sub_ffffff800004b138 -> sub_ffffff800004b114 : 212 -> 200
~ sub_ffffff800004b87c -> sub_ffffff800004b84c : 208 -> 204
~ sub_ffffff800004bd64 -> sub_ffffff800004bd30 : 3192 -> 3200
~ sub_ffffff800004d7dc -> sub_ffffff800004d7b0 : 2476 -> 2444
~ sub_ffffff800004e328 -> sub_ffffff800004e2dc : 328 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:24:35"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:35:57"
```
