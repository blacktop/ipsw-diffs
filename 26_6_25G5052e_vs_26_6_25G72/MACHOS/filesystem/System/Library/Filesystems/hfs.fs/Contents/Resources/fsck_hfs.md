## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/Contents/Resources/fsck_hfs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`
- `__DATA.__common`

```diff

-715.160.7.0.0
-  __TEXT.__text: 0x2fe64
+715.160.9.0.0
+  __TEXT.__text: 0x2fea4
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__const: 0x110c
   __TEXT.__cstring: 0x6e7e
Functions:
~ sub_100006f74 : 392 -> 400
~ sub_1000095c4 -> sub_1000095cc : 3572 -> 3628
```
