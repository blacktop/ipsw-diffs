## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.42.1.0.0
-  __TEXT.__text: 0x518f8
+3288.60.7.0.0
+  __TEXT.__text: 0x51874
   __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__cstring: 0xfa4d
+  __TEXT.__cstring: 0xfa9f
   __TEXT.__const: 0x8480
-  __TEXT.__unwind_info: 0xad0
+  __TEXT.__unwind_info: 0xae0
   __DATA_CONST.__const: 0x570
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__auth_got: 0x470

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 717
+  Functions: 720
   Symbols:   157
-  CStrings:  1321
+  CStrings:  1322
 
CStrings:
+ "%s:%d: %s error: chunk info index %u out of range for cib %u chunk info count %u\n"
+ "3288.60.7"
- "3288.42.1"
```
