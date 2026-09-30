## agx_a000

> `Firmware/agx/armfw_g16s.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x51258
+  __TEXT.__text: 0x511fc
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x12e7
+  __TEXT.__const: 0x12e8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2f52
+  __TEXT.__cstring: 0x2f50
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc000003e91c : 112 -> 116
~ sub_fffffc00000407cc -> sub_fffffc00000407d0 : 832 -> 836
~ sub_fffffc0000041608 -> sub_fffffc0000041610 : 724 -> 720
~ sub_fffffc00000423cc -> sub_fffffc00000423d0 : 368 -> 364
~ sub_fffffc00000425c8 : 468 -> 456
~ sub_fffffc0000042804 -> sub_fffffc00000427f8 : 664 -> 652
~ sub_fffffc0000042a9c -> sub_fffffc0000042a84 : 1008 -> 992
~ sub_fffffc0000042e8c -> sub_fffffc0000042e64 : 268 -> 256
~ sub_fffffc000004334c -> sub_fffffc0000043318 : 956 -> 988
~ sub_fffffc000004428c -> sub_fffffc0000044278 : 328 -> 324
~ sub_fffffc0000044690 -> sub_fffffc0000044678 : 420 -> 416
~ sub_fffffc000004531c -> sub_fffffc0000045300 : 468 -> 480
~ sub_fffffc00000455fc -> sub_fffffc00000455ec : 3188 -> 3196
~ sub_fffffc0000048a34 -> sub_fffffc0000048a2c : 196 -> 192
~ sub_fffffc0000049d80 -> sub_fffffc0000049d74 : 528 -> 524
~ sub_fffffc000004bab0 -> sub_fffffc000004baa0 : 668 -> 664
~ sub_fffffc000004bd4c -> sub_fffffc000004bd38 : 788 -> 776
~ sub_fffffc000004c108 -> sub_fffffc000004c0e8 : 672 -> 668
~ sub_fffffc000004c568 -> sub_fffffc000004c544 : 228 -> 224
~ sub_fffffc000004d22c -> sub_fffffc000004d204 : 544 -> 532
~ sub_fffffc000004e668 -> sub_fffffc000004e634 : 792 -> 808
~ sub_fffffc000004ed8c -> sub_fffffc000004ed68 : 508 -> 504
~ sub_fffffc000004f270 -> sub_fffffc000004f248 : 420 -> 412
~ sub_fffffc000004f4a4 -> sub_fffffc000004f474 : 212 -> 200
~ sub_fffffc000004f990 -> sub_fffffc000004f954 : 328 -> 324
~ sub_fffffc000004fad8 -> sub_fffffc000004fa98 : 208 -> 204
~ sub_fffffc0000050450 -> sub_fffffc000005040c : 2852 -> 2832
~ sub_fffffc0000051114 -> sub_fffffc00000510bc : 332 -> 328
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:21:34"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:32:10"
```
