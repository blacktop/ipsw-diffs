## IOMFBDiagnose

> `/usr/bin/IOMFBDiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-700.50.85.0.0
-  __TEXT.__text: 0x10018
+700.50.97.9.0
+  __TEXT.__text: 0x1001c
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__const: 0xab4
-  __TEXT.__cstring: 0x7e4d
+  __TEXT.__cstring: 0x7eb3
   __TEXT.__objc_methname: 0x62
   __TEXT.__unwind_info: 0x1d8
-  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__const: 0xd20
   __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x160

   - /usr/lib/libobjc.A.dylib
   Functions: 118
   Symbols:   56
-  CStrings:  1285
+  CStrings:  1289
 
Functions:
~ sub_100010910 : 248 -> 252
CStrings:
+ "    [%2u] surfaceID = %u (0x%x)\n"
+ "MissingTERecoveryPanic"
+ "MissingTERecoveryReset"
+ "MissingTERecoveryResolved"
+ "MissingTERecoveryStart"
- "    [%2u] surfaceID = %u\n"
```
