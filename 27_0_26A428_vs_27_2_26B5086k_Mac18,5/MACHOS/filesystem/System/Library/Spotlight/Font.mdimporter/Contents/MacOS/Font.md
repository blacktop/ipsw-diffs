## Font

> `/System/Library/Spotlight/Font.mdimporter/Contents/MacOS/Font`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0x2ecc
+41.0.0.0.0
+  __TEXT.__text: 0x2f84
   __TEXT.__auth_stubs: 0x580
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x3cc
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__cstring: 0x399
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x2c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 41
+  Functions: 40
   Symbols:   126
-  CStrings:  32
+  CStrings:  31
 
CStrings:
- "Font Importer: Name table begins past end of file."
```
