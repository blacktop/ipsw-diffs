## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x4fad4
+3288.40.13.0.0
+  __TEXT.__text: 0x4fcc8
   __TEXT.__auth_stubs: 0x790
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x103c4
+  __TEXT.__cstring: 0x1041d
   __TEXT.__unwind_info: 0xb48
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x160

   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__data: 0x360
-  __DATA.__common: 0x414
+  __DATA.__common: 0x418
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 750
+  Functions: 751
   Symbols:   136
-  CStrings:  1307
+  CStrings:  1309
 
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "btree_node_compact"
```
