## sptm.t8160.release.im4p

> `Firmware/sptm.t8160.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__LATE_CONST.__late_const`

```diff

 820.40.24.0.0
-  __TEXT.__cstring: 0x1632c
+  __TEXT.__cstring: 0x163e4
   __TEXT.__const: 0xaa4
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
   __DATA_CONST.__const: 0x7c00
   __LATE_CONST.__late_const: 0x8c890
-  __TEXT_EXEC.__text: 0x613b4
+  __TEXT_EXEC.__text: 0x616d4
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf

   __BOOTDATA.__data: 0x18000
   Functions: 408
   Symbols:   1
-  CStrings:  2599
+  CStrings:  2602
 
Functions:
~ sub_fffffff0270e3a70 : 6692 -> 7064
~ sub_fffffff0270e5a38 -> sub_fffffff0270e5bac : 2756 -> 3172
~ sub_fffffff0270ea434 -> sub_fffffff0270ea748 : 4180 -> 4188
~ sub_fffffff0270eb488 -> sub_fffffff0270eb7a4 : 13452 -> 13456
CStrings:
+ "%s: dart %p (%s:%u): Inconsistent unganged clock protection configuration"
+ "(&dart_gapf_ungang_map[state->gapf_ungang_map_index].lock)"
+ "SPTM-820.40.24|2026-10-03:14:50:35.671934|"
+ "sptm_t8110dart_skip_disable_clock_protection_write"
- "SPTM-820.40.24|2026-10-03:20:11:40.632663|"
```
