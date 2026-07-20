## MobileBackupCacheDeleteService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3038.0.0.0.0
-  __TEXT.__text: 0x12768
+3039.0.1.0.0
+  __TEXT.__text: 0x12958
   __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x20c0
-  __TEXT.__objc_methlist: 0x858
-  __TEXT.__const: 0x1a0
+  __TEXT.__objc_methlist: 0x860
+  __TEXT.__const: 0x1b0
   __TEXT.__gcc_except_tab: 0x2c4
   __TEXT.__cstring: 0x3d9c
   __TEXT.__oslogstring: 0x1f0d
-  __TEXT.__objc_methname: 0x2624
+  __TEXT.__objc_methname: 0x2666
   __TEXT.__objc_classname: 0xe1
   __TEXT.__objc_methtype: 0x444
   __TEXT.__unwind_info: 0x370

   __DATA_CONST.__got: 0x170
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x9c0
-  __DATA.__objc_selrefs: 0xa28
+  __DATA.__objc_selrefs: 0xa30
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x280
   __DATA.__bss: 0x98

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 339
+  Functions: 340
   Symbols:   185
-  CStrings:  847
+  CStrings:  848
 
Functions:
~ sub_100007340 : 452 -> 496
+ sub_100007530
CStrings:
+ "createIncompleteRestoreDirectoriesWithError:"
+ "removeIncompleteRestoreDirectoriesWithError:"
+ "removeIntermediateRestoreDirectoriesWithError:"
- "cleanupRestoreDirectoriesWithError:"
- "createRestoreDirectoriesWithError:"
```
