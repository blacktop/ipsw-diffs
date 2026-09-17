## apfs_shrink_diskimage

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_shrink_diskimage`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x59354
+3288.40.13.0.0
+  __TEXT.__text: 0x59548
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__cstring: 0x12f3c
+  __TEXT.__cstring: 0x12f95
   __TEXT.__const: 0x230
   __TEXT.__unwind_info: 0xb90
   __DATA_CONST.__const: 0x728

   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__data: 0x1f0
-  __DATA.__common: 0x41c
+  __DATA.__common: 0x420
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 772
+  Functions: 773
   Symbols:   140
-  CStrings:  1503
+  CStrings:  1505
 
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "btree_node_compact"
```
