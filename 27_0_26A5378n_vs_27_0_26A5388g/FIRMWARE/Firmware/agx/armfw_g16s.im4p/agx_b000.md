## agx_b000

> `Firmware/agx/armfw_g16s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x510f8
+  __TEXT.__text: 0x5109c
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
~ sub_fffffc000003e7bc : 112 -> 116
~ sub_fffffc000004066c -> sub_fffffc0000040670 : 832 -> 836
~ sub_fffffc00000414a8 -> sub_fffffc00000414b0 : 724 -> 720
~ sub_fffffc000004226c -> sub_fffffc0000042270 : 368 -> 364
~ sub_fffffc0000042468 : 468 -> 456
~ sub_fffffc00000426a4 -> sub_fffffc0000042698 : 664 -> 652
~ sub_fffffc000004293c -> sub_fffffc0000042924 : 1008 -> 992
~ sub_fffffc0000042d2c -> sub_fffffc0000042d04 : 268 -> 256
~ sub_fffffc00000431ec -> sub_fffffc00000431b8 : 956 -> 988
~ sub_fffffc000004412c -> sub_fffffc0000044118 : 328 -> 324
~ sub_fffffc0000044530 -> sub_fffffc0000044518 : 420 -> 416
~ sub_fffffc00000451bc -> sub_fffffc00000451a0 : 468 -> 480
~ sub_fffffc000004549c -> sub_fffffc000004548c : 3188 -> 3196
~ sub_fffffc00000488d4 -> sub_fffffc00000488cc : 196 -> 192
~ sub_fffffc0000049c20 -> sub_fffffc0000049c14 : 528 -> 524
~ sub_fffffc000004b950 -> sub_fffffc000004b940 : 668 -> 664
~ sub_fffffc000004bbec -> sub_fffffc000004bbd8 : 788 -> 776
~ sub_fffffc000004bfa8 -> sub_fffffc000004bf88 : 672 -> 668
~ sub_fffffc000004c408 -> sub_fffffc000004c3e4 : 228 -> 224
~ sub_fffffc000004d0cc -> sub_fffffc000004d0a4 : 544 -> 532
~ sub_fffffc000004e508 -> sub_fffffc000004e4d4 : 792 -> 808
~ sub_fffffc000004ec2c -> sub_fffffc000004ec08 : 508 -> 504
~ sub_fffffc000004f110 -> sub_fffffc000004f0e8 : 420 -> 412
~ sub_fffffc000004f344 -> sub_fffffc000004f314 : 212 -> 200
~ sub_fffffc000004f830 -> sub_fffffc000004f7f4 : 328 -> 324
~ sub_fffffc000004f978 -> sub_fffffc000004f938 : 208 -> 204
~ sub_fffffc00000502f0 -> sub_fffffc00000502ac : 2852 -> 2832
~ sub_fffffc0000050fb4 -> sub_fffffc0000050f5c : 332 -> 328
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:26:16"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:37:32"
```
