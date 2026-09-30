## agx_a000

> `Firmware/agx/armfw_g16g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52b08
+  __TEXT.__text: 0x52aac
   __TEXT.__gxf_code: 0x5080
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1d77
-  __TEXT.__cstring: 0x2700
+  __TEXT.__const: 0x1d78
+  __TEXT.__cstring: 0x26fe
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc00000400f0 : 112 -> 116
~ sub_fffffc0000041fc4 -> sub_fffffc0000041fc8 : 832 -> 836
~ sub_fffffc0000042e00 -> sub_fffffc0000042e08 : 724 -> 720
~ sub_fffffc0000043bc4 -> sub_fffffc0000043bc8 : 368 -> 364
~ sub_fffffc0000043dc0 : 468 -> 456
~ sub_fffffc0000043ffc -> sub_fffffc0000043ff0 : 664 -> 652
~ sub_fffffc0000044294 -> sub_fffffc000004427c : 1008 -> 992
~ sub_fffffc0000044684 -> sub_fffffc000004465c : 268 -> 256
~ sub_fffffc0000044b44 -> sub_fffffc0000044b10 : 956 -> 988
~ sub_fffffc0000045a88 -> sub_fffffc0000045a74 : 328 -> 324
~ sub_fffffc0000045e8c -> sub_fffffc0000045e74 : 420 -> 416
~ sub_fffffc0000046b18 -> sub_fffffc0000046afc : 468 -> 480
~ sub_fffffc0000046df8 -> sub_fffffc0000046de8 : 3188 -> 3196
~ sub_fffffc000004a354 -> sub_fffffc000004a34c : 196 -> 192
~ sub_fffffc000004b68c -> sub_fffffc000004b680 : 520 -> 516
~ sub_fffffc000004d40c -> sub_fffffc000004d3fc : 664 -> 660
~ sub_fffffc000004d6a4 -> sub_fffffc000004d690 : 784 -> 772
~ sub_fffffc000004da5c -> sub_fffffc000004da3c : 664 -> 660
~ sub_fffffc000004deb4 -> sub_fffffc000004de90 : 228 -> 224
~ sub_fffffc000004eb7c -> sub_fffffc000004eb54 : 544 -> 532
~ sub_fffffc000004ffb8 -> sub_fffffc000004ff84 : 788 -> 804
~ sub_fffffc00000506d8 -> sub_fffffc00000506b4 : 508 -> 504
~ sub_fffffc0000050bb4 -> sub_fffffc0000050b8c : 420 -> 412
~ sub_fffffc0000050de8 -> sub_fffffc0000050db8 : 212 -> 200
~ sub_fffffc00000512d4 -> sub_fffffc0000051298 : 328 -> 324
~ sub_fffffc000005141c -> sub_fffffc00000513dc : 208 -> 204
~ sub_fffffc0000051cf0 -> sub_fffffc0000051cac : 2868 -> 2848
~ sub_fffffc00000529c4 -> sub_fffffc000005296c : 332 -> 328
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:21:02"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:31:42"
```
