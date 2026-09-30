## com.apple.driver.DiskImages

> `com.apple.driver.DiskImages`

```diff

-  __TEXT.__cstring: 0x1b08
-  __TEXT_EXEC.__text: 0xe140
+  __TEXT.__cstring: 0x1b45
+  __TEXT_EXEC.__text: 0xe18c
   __TEXT_EXEC.__auth_stubs: 0x550
   __DATA.__data: 0x188
   __DATA.__common: 0x1a0

   __DATA_CONST.__kalloc_var: 0xa0
   __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0xb0
-  Functions: 373
-  Symbols:   913
-  CStrings:  282
+  Functions: 374
+  Symbols:   914
+  CStrings:  283
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN13IOHDIXHDDrive16sanitizeIOResultEi
Functions:
~ __ZN22IOHDIXHDDriveOutKernel12processReplyEPK13HDIReplyOOL64P18IOMemoryDescriptor : 628 -> 644
+ __ZN13IOHDIXHDDrive16sanitizeIOResultEi
~ _CreateDecomposedURLWithStrictnessLevel : 3456 -> 3424
~ _DI_strstr : 140 -> 136
CStrings:
+ "698"
+ "IOHDIXHDDrive::sanitizeIOResult: Mapping DI error %d to EIO\n"
- "696"

```
