## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x55c08
+3288.40.13.0.0
+  __TEXT.__text: 0x55d08
   __TEXT.__auth_stubs: 0xb90
-  __TEXT.__cstring: 0x1a750
+  __TEXT.__cstring: 0x1a75d
   __TEXT.__const: 0x8720
-  __TEXT.__unwind_info: 0xee8
+  __TEXT.__unwind_info: 0xef0
   __DATA_CONST.__const: 0x620
-  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 994
+  Functions: 995
   Symbols:   202
-  CStrings:  1998
+  CStrings:  1999
 
CStrings:
+ "3288.40.13"
+ "mount_apfs"
- "3288.1.3"
```
