## slurpAPFSMeta

> `System/Library/Filesystems/apfs.fs/Contents/Resources/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.701.3
-  __TEXT.__text: 0x36628
+2811.160.7.702.4
+  __TEXT.__text: 0x36820
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x8b80
+  __TEXT.__cstring: 0x8b93
   __TEXT.__const: 0x1e0
-  __TEXT.__unwind_info: 0x680
+  __TEXT.__unwind_info: 0x688
   __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x28

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 520
+  Functions: 521
   Symbols:   144
-  CStrings:  756
+  CStrings:  757
 
CStrings:
+ "btree_node_compact"
```
