## agx_b000

> `Firmware/agx/armfw_g14c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4e828
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x4e7d8
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
~ sub_ffffff800003c214 : 348 -> 356
~ sub_ffffff800003c854 -> sub_ffffff800003c85c : 112 -> 116
~ sub_ffffff8000040488 -> sub_ffffff8000040494 : 196 -> 192
~ sub_ffffff8000041780 -> sub_ffffff8000041788 : 528 -> 524
~ sub_ffffff800004234c -> sub_ffffff8000042350 : 824 -> 828
~ sub_ffffff8000043180 -> sub_ffffff8000043188 : 724 -> 720
~ sub_ffffff8000043f38 -> sub_ffffff8000043f3c : 368 -> 364
~ sub_ffffff8000044134 : 468 -> 456
~ sub_ffffff8000044370 -> sub_ffffff8000044364 : 664 -> 652
~ sub_ffffff8000044608 -> sub_ffffff80000445f0 : 1008 -> 992
~ sub_ffffff80000449f8 -> sub_ffffff80000449d0 : 268 -> 256
~ sub_ffffff8000044eb8 -> sub_ffffff8000044e84 : 956 -> 988
~ sub_ffffff8000045df8 -> sub_ffffff8000045de4 : 328 -> 324
~ sub_ffffff8000046490 -> sub_ffffff8000046478 : 480 -> 492
~ sub_ffffff8000047adc -> sub_ffffff8000047ad0 : 668 -> 664
~ sub_ffffff8000047d78 -> sub_ffffff8000047d68 : 796 -> 792
~ sub_ffffff800004813c -> sub_ffffff8000048128 : 672 -> 668
~ sub_ffffff800004859c -> sub_ffffff8000048584 : 228 -> 224
~ sub_ffffff8000049268 -> sub_ffffff800004924c : 544 -> 532
~ sub_ffffff800004a6b0 -> sub_ffffff800004a688 : 800 -> 816
~ sub_ffffff800004addc -> sub_ffffff800004adc4 : 504 -> 500
~ sub_ffffff800004b2bc -> sub_ffffff800004b2a0 : 420 -> 412
~ sub_ffffff800004b4f0 -> sub_ffffff800004b4cc : 212 -> 200
~ sub_ffffff800004bc34 -> sub_ffffff800004bc04 : 208 -> 204
~ sub_ffffff800004c11c -> sub_ffffff800004c0e8 : 3192 -> 3200
~ sub_ffffff800004db94 -> sub_ffffff800004db68 : 2476 -> 2444
~ sub_ffffff800004e6e0 -> sub_ffffff800004e694 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:24:50"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:35:37"
```
