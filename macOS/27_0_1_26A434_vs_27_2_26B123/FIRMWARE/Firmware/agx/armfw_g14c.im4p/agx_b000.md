## agx_b000

> `Firmware/agx/armfw_g14c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4e954
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x4ea14
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1ef0
+  __TEXT.__const: 0x1f00
   __TEXT.__cstring: 0x236b
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_ffffff8000023550 : 928 -> 924
~ sub_ffffff800002b770 -> sub_ffffff800002b76c : 1324 -> 1328
~ sub_ffffff800003a01c : 6856 -> 6916
~ __rtk_arm_start_bootstrap_area : 1888 -> 1868
~ sub_ffffff800003fd30 -> sub_ffffff800003fd58 : 384 -> 388
~ sub_ffffff8000048bd4 -> sub_ffffff8000048c00 : 436 -> 472
~ sub_ffffff8000048d88 -> sub_ffffff8000048dd8 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:10:05"
- "Aug 30 2026 19:01:06"
```
