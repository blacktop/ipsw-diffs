## libParallelCompression.dylib

> `/usr/lib/libParallelCompression.dylib`

```diff

-423.100.6.0.0
-  __TEXT.__text: 0x5543c
+443.0.0.0.0
+  __TEXT.__text: 0x5563c
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__cstring: 0xe398
+  __TEXT.__cstring: 0xe3da
   __TEXT.__const: 0x840
-  __TEXT.__oslogstring: 0x21
+  __TEXT.__oslogstring: 0x31
   __TEXT.__unwind_info: 0x940
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0x38

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
-  UUID: 83686B3C-75BD-34EB-B538-1E6F4C0222D0
+  UUID: 6C420E62-FF3D-39AA-8EE5-C99D31A68466
   Functions: 747
-  Symbols:   1661
-  CStrings:  2245
+  Symbols:   1659
+  CStrings:  2247
 
Symbols:
+ _rawimg_allocate_header_and_footer
- _getHeader
CStrings:
+ "Can't allocate header/footer"
+ "Fork missing header/footer"
+ "Too much fork padding: %zu"
+ "[0x%08x] %{public}s"
+ "[0x%08x](warning) %{public}s"
- "[0x%08x] %s"
- "[0x%08x](warning) %s"
- "too much padding"

```
