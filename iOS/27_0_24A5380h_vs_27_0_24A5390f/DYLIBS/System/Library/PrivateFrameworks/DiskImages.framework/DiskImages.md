## DiskImages

> `/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`

```diff

-698.0.0.0.0
-  __TEXT.__text: 0x3c520
-  __TEXT.__cstring: 0x69dc
+701.0.0.0.0
+  __TEXT.__text: 0x3c600
+  __TEXT.__cstring: 0x6a1c
   __TEXT.__const: 0x7e9
   __TEXT.__gcc_except_tab: 0x9e4
   __TEXT.__unwind_info: 0xfe0

   - /usr/lib/libz.1.dylib
   Functions: 1227
   Symbols:   354
-  CStrings:  1031
+  CStrings:  1033
 
Functions:
~ sub_25e66837c -> sub_25f8a937c : 420 -> 432
~ sub_25e668520 -> sub_25f8a952c : 1124 -> 1216
~ sub_25e66ba10 -> sub_25f8aca78 : 1360 -> 1396
~ sub_25e673a90 -> sub_25f8b4b1c : 940 -> 988
~ sub_25e691578 -> sub_25f8d2634 : 740 -> 776
CStrings:
+ "inStartSector>=0"
+ "inStartSector>=0 && inStartSector<fSectorCount"
```
