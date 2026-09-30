## apfs_invert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x5218c
+3288.40.13.0.0
+  __TEXT.__text: 0x52384
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0x10fb3
+  __TEXT.__cstring: 0x1100e
   __TEXT.__const: 0x8418
   __TEXT.__unwind_info: 0xb40
   __DATA_CONST.__const: 0x838

   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__data: 0x3f8
-  __DATA.__common: 0x41c
+  __DATA.__common: 0x420
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 753
+  Functions: 754
   Symbols:   143
-  CStrings:  1401
+  CStrings:  1403
 
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "3288.40.13"
+ "btree_node_compact"
- "3288.1.3"
```
