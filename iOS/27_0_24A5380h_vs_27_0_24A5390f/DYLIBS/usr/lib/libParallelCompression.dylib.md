## libParallelCompression.dylib

> `/usr/lib/libParallelCompression.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-467.0.0.0.0
-  __TEXT.__text: 0x55dbc
-  __TEXT.__cstring: 0xf571
+469.0.0.0.0
+  __TEXT.__text: 0x55e94
+  __TEXT.__cstring: 0xf581
   __TEXT.__const: 0x830
   __TEXT.__oslogstring: 0x31
   __TEXT.__unwind_info: 0x968

   - /usr/lib/liblzma.5.dylib
   Functions: 759
   Symbols:   990
-  CStrings:  2261
+  CStrings:  2262
 
Functions:
~ _BXPatch5InPlace : 2904 -> 3028
~ __Z13pc_array_initmm : 120 -> 188
~ _rawimg_destroy : 164 -> 172
~ _rawimg_create_with_stream : 1360 -> 1376
CStrings:
+ "array too large"
```
