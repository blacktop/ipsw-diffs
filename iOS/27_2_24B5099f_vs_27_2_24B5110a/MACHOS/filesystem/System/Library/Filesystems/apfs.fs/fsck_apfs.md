## fsck_apfs

> `System/Library/Filesystems/apfs.fs/fsck_apfs`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.40.17.0.0
+3288.42.1.0.0
   __TEXT.__text: 0x567b0
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__cstring: 0x1a6e0
+  __TEXT.__cstring: 0x1a6df
   __TEXT.__const: 0x8730
   __TEXT.__unwind_info: 0xef0
   __DATA_CONST.__const: 0x620
CStrings:
+ "3288.42.1"
- "3288.40.17"
```
