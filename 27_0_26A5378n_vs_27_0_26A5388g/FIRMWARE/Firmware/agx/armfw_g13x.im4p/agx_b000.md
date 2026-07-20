## agx_b000

> `Firmware/agx/armfw_g13x.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x44898
-  __TEXT.__gxf_code: 0x1154
+  __TEXT.__text: 0x4484c
+  __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f70
-  __TEXT.__cstring: 0x1f35
+  __TEXT.__cstring: 0x1f33
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x1e8
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff8000033024 : 348 -> 356
~ sub_ffffff8000033664 -> sub_ffffff800003366c : 112 -> 116
~ sub_ffffff800003722c -> sub_ffffff8000037238 : 196 -> 192
~ sub_ffffff8000038524 -> sub_ffffff800003852c : 528 -> 524
~ sub_ffffff80000390bc -> sub_ffffff80000390c0 : 668 -> 672
~ sub_ffffff8000039fd8 -> sub_ffffff8000039fe0 : 368 -> 364
~ sub_ffffff800003a1d4 -> sub_ffffff800003a1d8 : 468 -> 456
~ sub_ffffff800003a410 -> sub_ffffff800003a408 : 664 -> 652
~ sub_ffffff800003a6a8 -> sub_ffffff800003a694 : 1016 -> 1000
~ sub_ffffff800003aaa0 -> sub_ffffff800003aa7c : 268 -> 256
~ sub_ffffff800003af68 -> sub_ffffff800003af38 : 956 -> 988
~ sub_ffffff800003bea8 -> sub_ffffff800003be98 : 328 -> 324
~ sub_ffffff800003c540 -> sub_ffffff800003c52c : 480 -> 492
~ sub_ffffff800003db90 -> sub_ffffff800003db88 : 668 -> 664
~ sub_ffffff800003de2c -> sub_ffffff800003de20 : 796 -> 792
~ sub_ffffff800003e1f4 -> sub_ffffff800003e1e4 : 672 -> 668
~ sub_ffffff800003e654 -> sub_ffffff800003e640 : 228 -> 224
~ sub_ffffff800003f320 -> sub_ffffff800003f308 : 544 -> 532
~ sub_ffffff8000040768 -> sub_ffffff8000040744 : 800 -> 816
~ sub_ffffff8000040e94 -> sub_ffffff8000040e80 : 508 -> 504
~ sub_ffffff8000041378 -> sub_ffffff8000041360 : 420 -> 412
~ sub_ffffff80000415ac -> sub_ffffff800004158c : 212 -> 200
~ sub_ffffff8000041cf0 -> sub_ffffff8000041cc4 : 208 -> 204
~ sub_ffffff80000421d8 -> sub_ffffff80000421a8 : 3188 -> 3196
~ sub_ffffff8000043c44 -> sub_ffffff8000043c1c : 2412 -> 2380
~ sub_ffffff8000044750 -> sub_ffffff8000044708 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:22:59"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:33:34"
```
