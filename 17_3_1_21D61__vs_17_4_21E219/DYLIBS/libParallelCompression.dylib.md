## libParallelCompression.dylib

> `/usr/lib/libParallelCompression.dylib`

```diff

-398.0.0.0.0
-  __TEXT.__text: 0x56f88
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__cstring: 0xe302
+405.100.1.0.0
+  __TEXT.__text: 0x56448
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__cstring: 0xe30c
   __TEXT.__oslogstring: 0x21
   __TEXT.__const: 0x830
-  __TEXT.__unwind_info: 0x990
+  __TEXT.__unwind_info: 0x98c
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x108
   __AUTH_CONST.__auth_ptr: 0x60
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__const: 0x70
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x698
   __DATA.__data: 0x10
   __DATA.__bss: 0x8
   __DATA_DIRTY.__const: 0x58

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
-  Functions: 774
-  Symbols:   1648
+  Functions: 775
+  Symbols:   1649
   CStrings:  2237
 
Symbols:
+ _RawImagePatchInternal
+ _calloc
+ _malloc
+ _realloc
+ _valloc
- ___sprintf_chk
- _malloc_type_calloc
- _malloc_type_malloc
- _malloc_type_realloc
- _malloc_type_valloc
CStrings:
+ "(stream based)"
+ "RawImagePatchInternal"
+ "creating compression stream %s"
- "RawImagePatch"
- "Too many chunks"
- "creating compression stream"

```
