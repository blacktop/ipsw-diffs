## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x4cb10
+3288.40.13.0.0
+  __TEXT.__text: 0x4ccf8
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0xf7b0
+  __TEXT.__cstring: 0xf7c5
   __TEXT.__const: 0x220
-  __TEXT.__unwind_info: 0xa40
+  __TEXT.__unwind_info: 0xa48
   __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__auth_got: 0x3c0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 681
+  Functions: 682
   Symbols:   134
-  CStrings:  1265
+  CStrings:  1266
 
CStrings:
+ "3288.40.13"
+ "btree_node_compact"
- "3288.2.1"
```
