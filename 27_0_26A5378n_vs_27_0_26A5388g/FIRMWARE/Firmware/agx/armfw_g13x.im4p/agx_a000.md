## agx_a000

> `Firmware/agx/armfw_g13x.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4493c
-  __TEXT.__gxf_code: 0x1154
+  __TEXT.__text: 0x448f0
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
~ sub_ffffff80000330c8 : 348 -> 356
~ sub_ffffff8000033708 -> sub_ffffff8000033710 : 112 -> 116
~ sub_ffffff80000372d0 -> sub_ffffff80000372dc : 196 -> 192
~ sub_ffffff80000385c8 -> sub_ffffff80000385d0 : 528 -> 524
~ sub_ffffff8000039160 -> sub_ffffff8000039164 : 668 -> 672
~ sub_ffffff800003a07c -> sub_ffffff800003a084 : 368 -> 364
~ sub_ffffff800003a278 -> sub_ffffff800003a27c : 468 -> 456
~ sub_ffffff800003a4b4 -> sub_ffffff800003a4ac : 664 -> 652
~ sub_ffffff800003a74c -> sub_ffffff800003a738 : 1016 -> 1000
~ sub_ffffff800003ab44 -> sub_ffffff800003ab20 : 268 -> 256
~ sub_ffffff800003b00c -> sub_ffffff800003afdc : 956 -> 988
~ sub_ffffff800003bf4c -> sub_ffffff800003bf3c : 328 -> 324
~ sub_ffffff800003c5e4 -> sub_ffffff800003c5d0 : 480 -> 492
~ sub_ffffff800003dc34 -> sub_ffffff800003dc2c : 668 -> 664
~ sub_ffffff800003ded0 -> sub_ffffff800003dec4 : 796 -> 792
~ sub_ffffff800003e298 -> sub_ffffff800003e288 : 672 -> 668
~ sub_ffffff800003e6f8 -> sub_ffffff800003e6e4 : 228 -> 224
~ sub_ffffff800003f3c4 -> sub_ffffff800003f3ac : 544 -> 532
~ sub_ffffff800004080c -> sub_ffffff80000407e8 : 800 -> 816
~ sub_ffffff8000040f38 -> sub_ffffff8000040f24 : 508 -> 504
~ sub_ffffff800004141c -> sub_ffffff8000041404 : 420 -> 412
~ sub_ffffff8000041650 -> sub_ffffff8000041630 : 212 -> 200
~ sub_ffffff8000041d94 -> sub_ffffff8000041d68 : 208 -> 204
~ sub_ffffff800004227c -> sub_ffffff800004224c : 3188 -> 3196
~ sub_ffffff8000043ce8 -> sub_ffffff8000043cc0 : 2412 -> 2380
~ sub_ffffff80000447f4 -> sub_ffffff80000447ac : 336 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:19:51"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:30:27"
```
