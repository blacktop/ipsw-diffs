## sm_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x43920
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xce8a
+3288.40.13.0.0
+  __TEXT.__text: 0x43ba0
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__cstring: 0xcefe
   __TEXT.__const: 0x1c8
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__unwind_info: 0x8f8
   __DATA_CONST.__const: 0x6f8
-  __DATA_CONST.__cfstring: 0x120
-  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__cfstring: 0x160
+  __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__data: 0x210
-  __DATA.__common: 0x418
+  __DATA.__common: 0x41c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 595
-  Symbols:   129
-  CStrings:  1053
+  Functions: 597
+  Symbols:   130
+  CStrings:  1057
 
Symbols:
+ _IORegistryEntryCreateCFProperty
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "IOMatchCategory"
+ "btree_node_compact"
+ "mount_apfs"
```
