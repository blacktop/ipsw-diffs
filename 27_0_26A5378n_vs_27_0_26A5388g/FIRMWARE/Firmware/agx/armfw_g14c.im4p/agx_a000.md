## agx_a000

> `Firmware/agx/armfw_g14c.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4ecb8
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x4ec68
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f08
-  __TEXT.__cstring: 0x2349
+  __TEXT.__cstring: 0x2347
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff800003c6a4 : 348 -> 356
~ sub_ffffff800003cce4 -> sub_ffffff800003ccec : 112 -> 116
~ sub_ffffff8000040918 -> sub_ffffff8000040924 : 196 -> 192
~ sub_ffffff8000041c10 -> sub_ffffff8000041c18 : 528 -> 524
~ sub_ffffff80000427dc -> sub_ffffff80000427e0 : 824 -> 828
~ sub_ffffff8000043610 -> sub_ffffff8000043618 : 724 -> 720
~ sub_ffffff80000443c8 -> sub_ffffff80000443cc : 368 -> 364
~ sub_ffffff80000445c4 : 468 -> 456
~ sub_ffffff8000044800 -> sub_ffffff80000447f4 : 664 -> 652
~ sub_ffffff8000044a98 -> sub_ffffff8000044a80 : 1008 -> 992
~ sub_ffffff8000044e88 -> sub_ffffff8000044e60 : 268 -> 256
~ sub_ffffff8000045348 -> sub_ffffff8000045314 : 956 -> 988
~ sub_ffffff8000046288 -> sub_ffffff8000046274 : 328 -> 324
~ sub_ffffff8000046920 -> sub_ffffff8000046908 : 480 -> 492
~ sub_ffffff8000047f6c -> sub_ffffff8000047f60 : 668 -> 664
~ sub_ffffff8000048208 -> sub_ffffff80000481f8 : 796 -> 792
~ sub_ffffff80000485cc -> sub_ffffff80000485b8 : 672 -> 668
~ sub_ffffff8000048a2c -> sub_ffffff8000048a14 : 228 -> 224
~ sub_ffffff80000496f8 -> sub_ffffff80000496dc : 544 -> 532
~ sub_ffffff800004ab40 -> sub_ffffff800004ab18 : 800 -> 816
~ sub_ffffff800004b26c -> sub_ffffff800004b254 : 504 -> 500
~ sub_ffffff800004b74c -> sub_ffffff800004b730 : 420 -> 412
~ sub_ffffff800004b980 -> sub_ffffff800004b95c : 212 -> 200
~ sub_ffffff800004c0c4 -> sub_ffffff800004c094 : 208 -> 204
~ sub_ffffff800004c5ac -> sub_ffffff800004c578 : 3192 -> 3200
~ sub_ffffff800004e024 -> sub_ffffff800004dff8 : 2476 -> 2444
~ sub_ffffff800004eb70 -> sub_ffffff800004eb24 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:20:48"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:31:24"
```
