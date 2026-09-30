## agx_a000

> `Firmware/agx/armfw_g13g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`

```diff

-  __TEXT.__text: 0x40eb8
-  __TEXT.__gxf_code: 0x1154
+  __TEXT.__text: 0x40e6c
+  __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1d3c
-  __TEXT.__cstring: 0x1c57
+  __TEXT.__cstring: 0x1c55
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x1e8
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_ffffff8000030fd8 : 348 -> 356
~ sub_ffffff8000031618 -> sub_ffffff8000031620 : 88 -> 92
~ sub_ffffff800003509c -> sub_ffffff80000350a8 : 196 -> 192
~ sub_ffffff8000036350 -> sub_ffffff8000036358 : 528 -> 524
~ sub_ffffff8000036eec -> sub_ffffff8000036ef0 : 668 -> 672
~ sub_ffffff8000037e1c -> sub_ffffff8000037e24 : 368 -> 364
~ sub_ffffff8000038018 -> sub_ffffff800003801c : 468 -> 456
~ sub_ffffff8000038254 -> sub_ffffff800003824c : 664 -> 652
~ sub_ffffff80000384ec -> sub_ffffff80000384d8 : 1016 -> 1000
~ sub_ffffff80000388e4 -> sub_ffffff80000388c0 : 268 -> 256
~ sub_ffffff8000038dac -> sub_ffffff8000038d7c : 960 -> 992
~ sub_ffffff8000039798 -> sub_ffffff8000039788 : 484 -> 496
~ sub_ffffff800003adec -> sub_ffffff800003ade8 : 668 -> 664
~ sub_ffffff800003b088 -> sub_ffffff800003b080 : 796 -> 792
~ sub_ffffff800003b450 -> sub_ffffff800003b444 : 672 -> 668
~ sub_ffffff800003b8b0 -> sub_ffffff800003b8a0 : 228 -> 224
~ sub_ffffff800003c580 -> sub_ffffff800003c56c : 544 -> 532
~ sub_ffffff800003d8ac -> sub_ffffff800003d88c : 800 -> 816
~ sub_ffffff800003dfd8 -> sub_ffffff800003dfc8 : 508 -> 504
~ sub_ffffff800003e4b8 -> sub_ffffff800003e4a4 : 552 -> 540
~ sub_ffffff800003e770 -> sub_ffffff800003e750 : 212 -> 200
~ sub_ffffff800003eeb4 -> sub_ffffff800003ee88 : 208 -> 204
~ sub_ffffff800003ef84 -> sub_ffffff800003ef54 : 3196 -> 3204
~ sub_ffffff8000040384 -> sub_ffffff800004035c : 2124 -> 2092
~ sub_ffffff8000040d70 -> sub_ffffff8000040d28 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:19:47"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:30:22"
```
