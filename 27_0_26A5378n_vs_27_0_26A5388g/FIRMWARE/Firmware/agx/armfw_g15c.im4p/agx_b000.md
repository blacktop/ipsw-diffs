## agx_b000

> `Firmware/agx/armfw_g15c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52c90
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x52c3c
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x11b8
-  __TEXT.__cstring: 0x2b90
+  __TEXT.__cstring: 0x2b8e
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc000003fc20 : 348 -> 356
~ sub_fffffc0000040260 -> sub_fffffc0000040268 : 112 -> 116
~ sub_fffffc0000043e94 -> sub_fffffc0000043ea0 : 196 -> 192
~ sub_fffffc0000045180 -> sub_fffffc0000045188 : 528 -> 524
~ sub_fffffc0000045d4c -> sub_fffffc0000045d50 : 824 -> 828
~ sub_fffffc0000046b80 -> sub_fffffc0000046b88 : 724 -> 720
~ sub_fffffc0000047938 -> sub_fffffc000004793c : 368 -> 364
~ sub_fffffc0000047b34 : 468 -> 456
~ sub_fffffc0000047d70 -> sub_fffffc0000047d64 : 664 -> 652
~ sub_fffffc0000048008 -> sub_fffffc0000047ff0 : 1008 -> 992
~ sub_fffffc00000483f8 -> sub_fffffc00000483d0 : 268 -> 256
~ sub_fffffc00000488b8 -> sub_fffffc0000048884 : 956 -> 988
~ sub_fffffc00000497f8 -> sub_fffffc00000497e4 : 328 -> 324
~ sub_fffffc0000049bfc -> sub_fffffc0000049be4 : 420 -> 416
~ sub_fffffc000004a888 -> sub_fffffc000004a86c : 480 -> 492
~ sub_fffffc000004bed4 -> sub_fffffc000004bec4 : 668 -> 664
~ sub_fffffc000004c170 -> sub_fffffc000004c15c : 788 -> 776
~ sub_fffffc000004c52c -> sub_fffffc000004c50c : 672 -> 668
~ sub_fffffc000004c98c -> sub_fffffc000004c968 : 228 -> 224
~ sub_fffffc000004d650 -> sub_fffffc000004d628 : 544 -> 532
~ sub_fffffc000004ea98 -> sub_fffffc000004ea64 : 792 -> 808
~ sub_fffffc000004f1bc -> sub_fffffc000004f198 : 508 -> 504
~ sub_fffffc000004f6a0 -> sub_fffffc000004f678 : 420 -> 412
~ sub_fffffc000004f8d4 -> sub_fffffc000004f8a4 : 212 -> 200
~ sub_fffffc000004fecc -> sub_fffffc000004fe90 : 328 -> 324
~ sub_fffffc0000050014 -> sub_fffffc000004ffd4 : 208 -> 204
~ sub_fffffc00000504fc -> sub_fffffc00000504b8 : 3188 -> 3196
~ sub_fffffc0000051f64 -> sub_fffffc0000051f28 : 2632 -> 2612
~ sub_fffffc0000052b4c -> sub_fffffc0000052afc : 324 -> 328
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:26:26"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:37:43"
```
