## agx_a000

> `Firmware/agx/armfw_g14d.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4f3f8
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x4f3a8
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f48
-  __TEXT.__cstring: 0x2349
+  __TEXT.__cstring: 0x2347
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff800003cde4 : 348 -> 356
~ sub_ffffff800003d424 -> sub_ffffff800003d42c : 112 -> 116
~ sub_ffffff8000041058 -> sub_ffffff8000041064 : 196 -> 192
~ sub_ffffff8000042350 -> sub_ffffff8000042358 : 528 -> 524
~ sub_ffffff8000042f1c -> sub_ffffff8000042f20 : 824 -> 828
~ sub_ffffff8000043d50 -> sub_ffffff8000043d58 : 724 -> 720
~ sub_ffffff8000044b08 -> sub_ffffff8000044b0c : 368 -> 364
~ sub_ffffff8000044d04 : 468 -> 456
~ sub_ffffff8000044f40 -> sub_ffffff8000044f34 : 664 -> 652
~ sub_ffffff80000451d8 -> sub_ffffff80000451c0 : 1008 -> 992
~ sub_ffffff80000455c8 -> sub_ffffff80000455a0 : 268 -> 256
~ sub_ffffff8000045a88 -> sub_ffffff8000045a54 : 956 -> 988
~ sub_ffffff80000469c8 -> sub_ffffff80000469b4 : 328 -> 324
~ sub_ffffff8000047060 -> sub_ffffff8000047048 : 480 -> 492
~ sub_ffffff80000486ac -> sub_ffffff80000486a0 : 668 -> 664
~ sub_ffffff8000048948 -> sub_ffffff8000048938 : 796 -> 792
~ sub_ffffff8000048d0c -> sub_ffffff8000048cf8 : 672 -> 668
~ sub_ffffff800004916c -> sub_ffffff8000049154 : 228 -> 224
~ sub_ffffff8000049e38 -> sub_ffffff8000049e1c : 544 -> 532
~ sub_ffffff800004b280 -> sub_ffffff800004b258 : 800 -> 816
~ sub_ffffff800004b9ac -> sub_ffffff800004b994 : 504 -> 500
~ sub_ffffff800004be8c -> sub_ffffff800004be70 : 420 -> 412
~ sub_ffffff800004c0c0 -> sub_ffffff800004c09c : 212 -> 200
~ sub_ffffff800004c804 -> sub_ffffff800004c7d4 : 208 -> 204
~ sub_ffffff800004ccec -> sub_ffffff800004ccb8 : 3192 -> 3200
~ sub_ffffff800004e764 -> sub_ffffff800004e738 : 2476 -> 2444
~ sub_ffffff800004f2b0 -> sub_ffffff800004f264 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:20:49"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:31:27"
```
