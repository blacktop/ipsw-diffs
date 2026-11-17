## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-561.60.2.0.0
-  __TEXT.__text: 0xceb0
+561.60.3.0.0
+  __TEXT.__text: 0xcf28
   __TEXT.__auth_stubs: 0x610
   __TEXT.__const: 0x280
   __TEXT.__cstring: 0x35da
Functions:
~ sub_100007ca0 : 736 -> 856
```
