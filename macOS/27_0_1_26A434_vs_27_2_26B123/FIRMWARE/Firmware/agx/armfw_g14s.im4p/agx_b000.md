## agx_b000

> `Firmware/agx/armfw_g14s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4e5a0
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x4e670
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1ef0
+  __TEXT.__const: 0x1f00
   __TEXT.__cstring: 0x236b
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_ffffff8000023308 : 928 -> 924
~ sub_ffffff8000025e84 -> sub_ffffff8000025e80 : 724 -> 732
~ sub_ffffff8000026a18 -> sub_ffffff8000026a1c : 796 -> 804
~ sub_ffffff800002b450 -> sub_ffffff800002b45c : 1324 -> 1328
~ sub_ffffff8000039c64 -> sub_ffffff8000039c74 : 6860 -> 6920
~ __rtk_arm_start_bootstrap_area : 1888 -> 1868
~ sub_ffffff800003f97c -> sub_ffffff800003f9b4 : 384 -> 388
~ sub_ffffff8000048820 -> sub_ffffff800004885c : 436 -> 472
~ sub_ffffff80000489d4 -> sub_ffffff8000048a34 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:10:03"
- "Aug 30 2026 19:01:08"
```
