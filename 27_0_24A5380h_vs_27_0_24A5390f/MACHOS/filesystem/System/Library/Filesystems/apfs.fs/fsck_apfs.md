## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-3283.0.9.502.1
+3283.0.13.0.0
   __TEXT.__text: 0x5687c
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__cstring: 0x1a6cc
+  __TEXT.__cstring: 0x1a6d9
   __TEXT.__const: 0x8730
   __TEXT.__unwind_info: 0xba0
   __DATA_CONST.__const: 0x620
CStrings:
+ "3283.0.13"
+ "reap list object 0x%llx first index %u larger than max index %u\n"
+ "reap list object 0x%llx free index %u larger than max index %u\n"
+ "reap list object 0x%llx last index %u larger than max index %u\n"
- "3283.0.9.502.1"
- "reap list object 0x%llx first index %u larger than max %u\n"
- "reap list object 0x%llx free index %u larger than max %u\n"
- "reap list object 0x%llx last index %u larger than max %u\n"
```
