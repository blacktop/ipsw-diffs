## agx_b000

> `Firmware/agx/armfw_g16c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x513f4
+  __TEXT.__text: 0x51398
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x12e7
+  __TEXT.__const: 0x12e8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2ee4
+  __TEXT.__cstring: 0x2ee2
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc000003eab8 : 112 -> 116
~ sub_fffffc0000040968 -> sub_fffffc000004096c : 832 -> 836
~ sub_fffffc00000417a4 -> sub_fffffc00000417ac : 724 -> 720
~ sub_fffffc0000042568 -> sub_fffffc000004256c : 368 -> 364
~ sub_fffffc0000042764 : 468 -> 456
~ sub_fffffc00000429a0 -> sub_fffffc0000042994 : 664 -> 652
~ sub_fffffc0000042c38 -> sub_fffffc0000042c20 : 1008 -> 992
~ sub_fffffc0000043028 -> sub_fffffc0000043000 : 268 -> 256
~ sub_fffffc00000434e8 -> sub_fffffc00000434b4 : 956 -> 988
~ sub_fffffc0000044428 -> sub_fffffc0000044414 : 328 -> 324
~ sub_fffffc000004482c -> sub_fffffc0000044814 : 420 -> 416
~ sub_fffffc00000454b8 -> sub_fffffc000004549c : 468 -> 480
~ sub_fffffc0000045798 -> sub_fffffc0000045788 : 3188 -> 3196
~ sub_fffffc0000048bd0 -> sub_fffffc0000048bc8 : 196 -> 192
~ sub_fffffc0000049f1c -> sub_fffffc0000049f10 : 528 -> 524
~ sub_fffffc000004bc4c -> sub_fffffc000004bc3c : 668 -> 664
~ sub_fffffc000004bee8 -> sub_fffffc000004bed4 : 788 -> 776
~ sub_fffffc000004c2a4 -> sub_fffffc000004c284 : 672 -> 668
~ sub_fffffc000004c704 -> sub_fffffc000004c6e0 : 228 -> 224
~ sub_fffffc000004d3c8 -> sub_fffffc000004d3a0 : 544 -> 532
~ sub_fffffc000004e804 -> sub_fffffc000004e7d0 : 792 -> 808
~ sub_fffffc000004ef28 -> sub_fffffc000004ef04 : 508 -> 504
~ sub_fffffc000004f40c -> sub_fffffc000004f3e4 : 420 -> 412
~ sub_fffffc000004f640 -> sub_fffffc000004f610 : 212 -> 200
~ sub_fffffc000004fb2c -> sub_fffffc000004faf0 : 328 -> 324
~ sub_fffffc000004fc74 -> sub_fffffc000004fc34 : 208 -> 204
~ sub_fffffc00000505ec -> sub_fffffc00000505a8 : 2852 -> 2832
~ sub_fffffc00000512b0 -> sub_fffffc0000051258 : 324 -> 328
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:26:15"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:37:33"
```
