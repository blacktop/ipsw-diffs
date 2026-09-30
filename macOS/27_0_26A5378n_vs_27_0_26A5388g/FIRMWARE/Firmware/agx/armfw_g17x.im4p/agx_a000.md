## agx_a000

> `Firmware/agx/armfw_g17x.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3cb14
+  __TEXT.__text: 0x3cac8
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x119f
+  __TEXT.__const: 0x11a0
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x21bb
+  __TEXT.__cstring: 0x21b9
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc00000238dc : 368 -> 384
~ sub_fffffc000002b054 -> sub_fffffc000002b064 : 112 -> 116
~ sub_fffffc000002cf18 -> sub_fffffc000002cf2c : 832 -> 836
~ sub_fffffc000002dd54 -> sub_fffffc000002dd6c : 724 -> 720
~ sub_fffffc000002eb1c -> sub_fffffc000002eb30 : 368 -> 364
~ sub_fffffc000002ed18 -> sub_fffffc000002ed28 : 468 -> 456
~ sub_fffffc000002ef54 -> sub_fffffc000002ef58 : 664 -> 652
~ sub_fffffc000002f1ec -> sub_fffffc000002f1e4 : 1008 -> 992
~ sub_fffffc000002f5dc -> sub_fffffc000002f5c4 : 268 -> 256
~ sub_fffffc000002fa9c -> sub_fffffc000002fa78 : 956 -> 988
~ sub_fffffc00000309e0 -> sub_fffffc00000309dc : 328 -> 324
~ sub_fffffc0000031078 -> sub_fffffc0000031070 : 468 -> 480
~ sub_fffffc0000031358 -> sub_fffffc000003135c : 2824 -> 2832
~ sub_fffffc00000344fc -> sub_fffffc0000034508 : 196 -> 192
~ sub_fffffc0000035a24 -> sub_fffffc0000035a2c : 528 -> 524
~ sub_fffffc00000377a8 -> sub_fffffc00000377ac : 656 -> 652
~ sub_fffffc0000037a38 : 796 -> 792
~ sub_fffffc0000037dfc -> sub_fffffc0000037df8 : 672 -> 668
~ sub_fffffc000003825c -> sub_fffffc0000038254 : 228 -> 224
~ sub_fffffc0000038f24 -> sub_fffffc0000038f18 : 544 -> 532
~ sub_fffffc000003a260 -> sub_fffffc000003a248 : 800 -> 816
~ sub_fffffc000003a98c -> sub_fffffc000003a984 : 508 -> 504
~ sub_fffffc000003ae70 -> sub_fffffc000003ae64 : 552 -> 540
~ sub_fffffc000003b128 -> sub_fffffc000003b110 : 212 -> 200
~ sub_fffffc000003b760 -> sub_fffffc000003b73c : 208 -> 204
~ sub_fffffc000003be9c -> sub_fffffc000003be74 : 2444 -> 2412
~ sub_fffffc000003c9cc -> sub_fffffc000003c984 : 328 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:29:10"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:41:03"
```
