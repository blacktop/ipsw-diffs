## agx_b000

> `Firmware/agx/armfw_g14d.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4f08c
-  __TEXT.__gxf_code: 0x10c8
+  __TEXT.__text: 0x4f14c
+  __TEXT.__gxf_code: 0x105c
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1f28
+  __TEXT.__const: 0x1f38
   __TEXT.__cstring: 0x236b
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
Functions:
~ sub_ffffff8000023a64 : 928 -> 924
~ sub_ffffff800002bccc -> sub_ffffff800002bcc8 : 1324 -> 1328
~ sub_ffffff800003a720 : 6908 -> 6968
~ __rtk_arm_start_bootstrap_area : 1888 -> 1868
~ sub_ffffff8000040468 -> sub_ffffff8000040490 : 384 -> 388
~ sub_ffffff800004930c -> sub_ffffff8000049338 : 436 -> 472
~ sub_ffffff80000494c0 -> sub_ffffff8000049510 : 428 -> 540
CStrings:
+ "Oct 14 2026 23:10:18"
- "Aug 30 2026 19:01:14"
```
