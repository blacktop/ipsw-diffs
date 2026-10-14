## sptm.t8160.release.im4p

> `Firmware/sptm.t8160.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__LATE_CONST.__late_const`

```diff

-820.40.23.0.0
+820.40.24.0.0
   __TEXT.__cstring: 0x1632c
   __TEXT.__const: 0xaa4
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
   __DATA_CONST.__const: 0x7c00
   __LATE_CONST.__late_const: 0x8c890
-  __TEXT_EXEC.__text: 0x61160
+  __TEXT_EXEC.__text: 0x613b4
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf
Functions:
~ sub_fffffff0270d5b10 : 884 -> 1472
~ sub_fffffff0270daf6c -> sub_fffffff0270db1b8 : 616 -> 624
~ sub_fffffff02711511c -> sub_fffffff027115370 : 68 -> 80
CStrings:
+ "SPTM-820.40.24|2026-10-03:20:11:40.632663|"
- "SPTM-820.40.23|2026-09-27:19:59:11.633384|"
```
