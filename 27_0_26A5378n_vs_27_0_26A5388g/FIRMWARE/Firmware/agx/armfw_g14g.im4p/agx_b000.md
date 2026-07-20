## agx_b000

> `Firmware/agx/armfw_g14g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x523a0
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x52350
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f14
-  __TEXT.__cstring: 0x20af
+  __TEXT.__cstring: 0x20ad
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff8000040430 : 348 -> 356
~ sub_ffffff8000040a70 -> sub_ffffff8000040a78 : 88 -> 92
~ sub_ffffff80000445a8 -> sub_ffffff80000445b4 : 196 -> 192
~ sub_ffffff80000458c0 -> sub_ffffff80000458c8 : 528 -> 524
~ sub_ffffff8000046490 -> sub_ffffff8000046494 : 824 -> 828
~ sub_ffffff80000472c4 -> sub_ffffff80000472cc : 724 -> 720
~ sub_ffffff800004807c -> sub_ffffff8000048080 : 368 -> 364
~ sub_ffffff8000048278 : 468 -> 456
~ sub_ffffff80000484b4 -> sub_ffffff80000484a8 : 664 -> 652
~ sub_ffffff800004874c -> sub_ffffff8000048734 : 1008 -> 992
~ sub_ffffff8000048b3c -> sub_ffffff8000048b14 : 268 -> 256
~ sub_ffffff8000048ffc -> sub_ffffff8000048fc8 : 956 -> 988
~ sub_ffffff8000049f3c -> sub_ffffff8000049f28 : 328 -> 324
~ sub_ffffff800004a5d4 -> sub_ffffff800004a5bc : 480 -> 492
~ sub_ffffff800004bc20 -> sub_ffffff800004bc14 : 668 -> 664
~ sub_ffffff800004bebc -> sub_ffffff800004beac : 796 -> 792
~ sub_ffffff800004c280 -> sub_ffffff800004c26c : 672 -> 668
~ sub_ffffff800004c6e0 -> sub_ffffff800004c6c8 : 228 -> 224
~ sub_ffffff800004d3b0 -> sub_ffffff800004d394 : 544 -> 532
~ sub_ffffff800004e7f4 -> sub_ffffff800004e7cc : 800 -> 816
~ sub_ffffff800004ef20 -> sub_ffffff800004ef08 : 504 -> 500
~ sub_ffffff800004f3fc -> sub_ffffff800004f3e0 : 420 -> 412
~ sub_ffffff800004f630 -> sub_ffffff800004f60c : 212 -> 200
~ sub_ffffff800004fd74 -> sub_ffffff800004fd44 : 208 -> 204
~ sub_ffffff800004fe44 -> sub_ffffff800004fe10 : 3200 -> 3208
~ sub_ffffff8000051768 -> sub_ffffff800005173c : 2384 -> 2352
~ sub_ffffff8000052258 -> sub_ffffff800005220c : 328 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:24:02"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:34:52"
```
