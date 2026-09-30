## libETLDLOADCoreDumpDynamic.dylib

> `/usr/lib/libETLDLOADCoreDumpDynamic.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`

```diff

-  __TEXT.__text: 0x9f0
+  __TEXT.__text: 0x9a4
   __TEXT.__auth_stubs: 0xc0
-  __TEXT.__cstring: 0x1a5
+  __TEXT.__cstring: 0x179
   __TEXT.__unwind_info: 0x58
   __AUTH_CONST.__auth_got: 0x60
   - /usr/lib/libETLDLOADDynamic.dylib

   - /usr/lib/libTelephonyUtilDynamic.dylib
   Functions: 2
   Symbols:   14
-  CStrings:  11
+  CStrings:  10
 
Functions:
~ _ETLDLOADCoreDumpCaptureRecord : 940 -> 908
~ _ETLDLOADCoreDumpCaptureRecordFast : 1604 -> 1560
CStrings:
- "Capture 0x%x, length 0x%x, chunk size 0x%x\n"
```
