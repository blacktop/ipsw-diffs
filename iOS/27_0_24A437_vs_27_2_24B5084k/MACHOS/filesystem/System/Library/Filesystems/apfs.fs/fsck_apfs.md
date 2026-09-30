## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x56420
+3288.40.13.0.0
+  __TEXT.__text: 0x566b8
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__cstring: 0x1a6d8
+  __TEXT.__cstring: 0x1a6e0
   __TEXT.__const: 0x8730
-  __TEXT.__unwind_info: 0xed8
+  __TEXT.__unwind_info: 0xee8
   __DATA_CONST.__const: 0x620
-  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 989
+  Functions: 992
   Symbols:   209
-  CStrings:  2002
+  CStrings:  2003
 
CStrings:
+ "3288.40.13"
+ "The volume %s with UUID %s was found to have minor issues that can be repaired."
+ "mount_apfs"
- "3288.2.1"
- "The volume %s with UUID %s could not be verified completely and can not be repaired."
```
