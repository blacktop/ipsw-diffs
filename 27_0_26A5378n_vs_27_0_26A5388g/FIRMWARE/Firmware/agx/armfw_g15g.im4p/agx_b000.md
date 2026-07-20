## agx_b000

> `Firmware/agx/armfw_g15g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x54ce4
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x54c94
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x23f4
-  __TEXT.__cstring: 0x25a6
+  __TEXT.__cstring: 0x25a4
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc0000042d78 : 348 -> 356
~ sub_fffffc00000433b8 -> sub_fffffc00000433c0 : 88 -> 92
~ sub_fffffc0000046ef4 -> sub_fffffc0000046f00 : 196 -> 192
~ sub_fffffc000004820c -> sub_fffffc0000048214 : 528 -> 524
~ sub_fffffc0000048ddc -> sub_fffffc0000048de0 : 824 -> 828
~ sub_fffffc0000049c10 -> sub_fffffc0000049c18 : 724 -> 720
~ sub_fffffc000004a9c8 -> sub_fffffc000004a9cc : 368 -> 364
~ sub_fffffc000004abc4 : 468 -> 456
~ sub_fffffc000004ae00 -> sub_fffffc000004adf4 : 664 -> 652
~ sub_fffffc000004b098 -> sub_fffffc000004b080 : 1008 -> 992
~ sub_fffffc000004b488 -> sub_fffffc000004b460 : 268 -> 256
~ sub_fffffc000004b948 -> sub_fffffc000004b914 : 956 -> 988
~ sub_fffffc000004c888 -> sub_fffffc000004c874 : 328 -> 324
~ sub_fffffc000004cf20 -> sub_fffffc000004cf08 : 480 -> 492
~ sub_fffffc000004e56c -> sub_fffffc000004e560 : 668 -> 664
~ sub_fffffc000004e808 -> sub_fffffc000004e7f8 : 796 -> 792
~ sub_fffffc000004ebcc -> sub_fffffc000004ebb8 : 672 -> 668
~ sub_fffffc000004f02c -> sub_fffffc000004f014 : 228 -> 224
~ sub_fffffc000004fcfc -> sub_fffffc000004fce0 : 544 -> 532
~ sub_fffffc0000051140 -> sub_fffffc0000051118 : 800 -> 816
~ sub_fffffc000005186c -> sub_fffffc0000051854 : 504 -> 500
~ sub_fffffc0000051d48 -> sub_fffffc0000051d2c : 420 -> 412
~ sub_fffffc0000051f7c -> sub_fffffc0000051f58 : 212 -> 200
~ sub_fffffc00000526c0 -> sub_fffffc0000052690 : 208 -> 204
~ sub_fffffc0000052790 -> sub_fffffc000005275c : 3200 -> 3208
~ sub_fffffc0000053f48 -> sub_fffffc0000053f1c : 2740 -> 2708
~ sub_fffffc0000054b9c -> sub_fffffc0000054b50 : 328 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:25:17"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:35:42"
```
