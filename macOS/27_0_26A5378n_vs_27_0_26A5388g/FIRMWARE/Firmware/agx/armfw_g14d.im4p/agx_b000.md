## agx_b000

> `Firmware/agx/armfw_g14d.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4ef60
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x4ef10
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f28
-  __TEXT.__cstring: 0x2349
+  __TEXT.__cstring: 0x2347
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff800003c94c : 348 -> 356
~ sub_ffffff800003cf8c -> sub_ffffff800003cf94 : 112 -> 116
~ sub_ffffff8000040bc0 -> sub_ffffff8000040bcc : 196 -> 192
~ sub_ffffff8000041eb8 -> sub_ffffff8000041ec0 : 528 -> 524
~ sub_ffffff8000042a84 -> sub_ffffff8000042a88 : 824 -> 828
~ sub_ffffff80000438b8 -> sub_ffffff80000438c0 : 724 -> 720
~ sub_ffffff8000044670 -> sub_ffffff8000044674 : 368 -> 364
~ sub_ffffff800004486c : 468 -> 456
~ sub_ffffff8000044aa8 -> sub_ffffff8000044a9c : 664 -> 652
~ sub_ffffff8000044d40 -> sub_ffffff8000044d28 : 1008 -> 992
~ sub_ffffff8000045130 -> sub_ffffff8000045108 : 268 -> 256
~ sub_ffffff80000455f0 -> sub_ffffff80000455bc : 956 -> 988
~ sub_ffffff8000046530 -> sub_ffffff800004651c : 328 -> 324
~ sub_ffffff8000046bc8 -> sub_ffffff8000046bb0 : 480 -> 492
~ sub_ffffff8000048214 -> sub_ffffff8000048208 : 668 -> 664
~ sub_ffffff80000484b0 -> sub_ffffff80000484a0 : 796 -> 792
~ sub_ffffff8000048874 -> sub_ffffff8000048860 : 672 -> 668
~ sub_ffffff8000048cd4 -> sub_ffffff8000048cbc : 228 -> 224
~ sub_ffffff80000499a0 -> sub_ffffff8000049984 : 544 -> 532
~ sub_ffffff800004ade8 -> sub_ffffff800004adc0 : 800 -> 816
~ sub_ffffff800004b514 -> sub_ffffff800004b4fc : 504 -> 500
~ sub_ffffff800004b9f4 -> sub_ffffff800004b9d8 : 420 -> 412
~ sub_ffffff800004bc28 -> sub_ffffff800004bc04 : 212 -> 200
~ sub_ffffff800004c36c -> sub_ffffff800004c33c : 208 -> 204
~ sub_ffffff800004c854 -> sub_ffffff800004c820 : 3192 -> 3200
~ sub_ffffff800004e2cc -> sub_ffffff800004e2a0 : 2476 -> 2444
~ sub_ffffff800004ee18 -> sub_ffffff800004edcc : 328 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:24:35"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:35:37"
```
