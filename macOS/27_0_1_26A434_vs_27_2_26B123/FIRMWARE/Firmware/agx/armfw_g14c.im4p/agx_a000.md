## agx_a000

> `Firmware/agx/armfw_g14c.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4ede4
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x4eea4
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1f08
+  __TEXT.__const: 0x1f18
   __TEXT.__cstring: 0x236b
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_ffffff80000236f0 : 928 -> 924
~ sub_ffffff800002b910 -> sub_ffffff800002b90c : 1324 -> 1328
~ sub_ffffff800003a438 : 6972 -> 7032
~ __rtk_arm_start_bootstrap_area : 1888 -> 1868
~ sub_ffffff80000401c0 -> sub_ffffff80000401e8 : 384 -> 388
~ sub_ffffff8000049064 -> sub_ffffff8000049090 : 436 -> 472
~ sub_ffffff8000049218 -> sub_ffffff8000049268 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:06:21"
- "Aug 30 2026 18:57:17"
```
