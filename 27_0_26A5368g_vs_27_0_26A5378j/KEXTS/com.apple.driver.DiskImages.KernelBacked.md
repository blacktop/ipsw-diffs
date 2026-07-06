## com.apple.driver.DiskImages.KernelBacked

> `com.apple.driver.DiskImages.KernelBacked`

```diff

   __TEXT.__cstring: 0x725
-  __TEXT_EXEC.__text: 0x8c14
-  __TEXT_EXEC.__auth_stubs: 0x3c0
+  __TEXT_EXEC.__text: 0x8c20
+  __TEXT_EXEC.__auth_stubs: 0x3d0
   __DATA.__data: 0xc4
   __DATA.__common: 0x178
   __DATA.__bss: 0x4

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x5da0
   __DATA_CONST.__kalloc_type: 0x240
-  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0xa0
   Functions: 311
-  Symbols:   857
+  Symbols:   858
   CStrings:  73
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN13IOHDIXHDDrive16sanitizeIOResultEi
Functions:
~ __ZN21IOHDIXHDDriveInKernel14processCommandER13IOHDIXCommandR12BounceBuffer : 1304 -> 1316

```
