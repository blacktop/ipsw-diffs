## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.40.14.0.0
-  __TEXT.__text: 0x566b8
+3288.40.17.0.0
+  __TEXT.__text: 0x567b0
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__cstring: 0x1a6e0
   __TEXT.__const: 0x8730
-  __TEXT.__unwind_info: 0xee8
+  __TEXT.__unwind_info: 0xef0
   __DATA_CONST.__const: 0x620
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__auth_got: 0x600

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 992
+  Functions: 993
   Symbols:   209
   CStrings:  2003
 
CStrings:
+ "3288.40.17"
- "3288.40.14"
```
