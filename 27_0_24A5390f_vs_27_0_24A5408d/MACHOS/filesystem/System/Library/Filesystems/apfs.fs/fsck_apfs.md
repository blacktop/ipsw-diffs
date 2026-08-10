## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-3283.0.13.0.0
-  __TEXT.__text: 0x5687c
+3288.2.1.0.0
+  __TEXT.__text: 0x56a7c
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__cstring: 0x1a6d9
+  __TEXT.__cstring: 0x1a6d8
   __TEXT.__const: 0x8730
-  __TEXT.__unwind_info: 0xba0
+  __TEXT.__unwind_info: 0xba8
   __DATA_CONST.__const: 0x620
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__auth_got: 0x600

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 988
+  Functions: 989
   Symbols:   209
   CStrings:  2002
 
CStrings:
+ "3288.2.1"
- "3283.0.13"
```
