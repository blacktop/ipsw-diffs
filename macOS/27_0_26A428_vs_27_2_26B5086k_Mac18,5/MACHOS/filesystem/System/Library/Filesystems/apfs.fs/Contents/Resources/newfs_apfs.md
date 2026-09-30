## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x54304
+3288.40.13.0.0
+  __TEXT.__text: 0x544fc
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__cstring: 0x106b5
+  __TEXT.__cstring: 0x10710
   __TEXT.__const: 0x84a1
   __TEXT.__oslogstring: 0x125
   __TEXT.__unwind_info: 0xb78

   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__data: 0x14a
-  __DATA.__common: 0x418
+  __DATA.__common: 0x41c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 806
+  Functions: 807
   Symbols:   161
-  CStrings:  1392
+  CStrings:  1394
 
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "3288.40.13"
+ "btree_node_compact"
- "3288.1.3"
```
