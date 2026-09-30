## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-467.0.0.0.0
-  __TEXT.__text: 0x832cc
-  __TEXT.__cstring: 0x13398
+469.0.0.0.0
+  __TEXT.__text: 0x83430
+  __TEXT.__cstring: 0x133db
   __TEXT.__const: 0x920
   __TEXT.__oslogstring: 0x31
   __TEXT.__unwind_info: 0xd78

   - /usr/lib/liblzma.5.dylib
   Functions: 1072
   Symbols:   1310
-  CStrings:  2902
+  CStrings:  2905
 
Functions:
~ _rawimg_destroy : 164 -> 172
~ _rawimg_create_with_stream : 1360 -> 1376
~ __Z13pc_array_initmm : 120 -> 188
~ _aeaOutputStreamCloseAndUpdateContext : 1088 -> 1144
~ _BXPatch5InPlace : 2904 -> 3028
~ _workerProc : 8076 -> 8160
CStrings:
+ "array too large"
+ "invalid reference entry: %s"
+ "worker reported errors"
```
