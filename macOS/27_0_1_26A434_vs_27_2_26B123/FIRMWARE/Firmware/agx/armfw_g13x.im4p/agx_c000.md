## agx_c000

> `Firmware/agx/armfw_g13x.im4p/agx_c000`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x44978
-  __TEXT.__gxf_code: 0x1150
+  __TEXT.__text: 0x449f4
+  __TEXT.__gxf_code: 0x10e4
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x1f70
+  __TEXT.__const: 0x1f80
   __TEXT.__cstring: 0x1f57
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x1e8
Functions:
~ sub_ffffff800002007c : 1272 -> 1264
~ __rtk_arm_start_bootstrap_area : 1888 -> 1868
~ sub_ffffff8000036a84 -> sub_ffffff8000036a68 : 384 -> 388
~ sub_ffffff800003ec40 -> sub_ffffff800003ec28 : 436 -> 472
~ sub_ffffff800003edf4 -> sub_ffffff800003ee00 : 428 -> 540
~ sub_ffffff8000044834 -> sub_ffffff80000448b0 : 332 -> 324
CStrings:
+ "Oct 14 2026 23:15:08"
- "Aug 30 2026 19:06:31"
```
