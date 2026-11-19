## fsck_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/fsck_udf`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-331.0.0.0.0
-  __TEXT.__text: 0x10d00
+331.40.5.0.0
+  __TEXT.__text: 0x10d2c
   __TEXT.__auth_stubs: 0x420
   __TEXT.__init_offsets: 0x8
   __TEXT.__gcc_except_tab: 0x604
Functions:
~ sub_100007e3c : 1664 -> 1580
~ sub_1000084bc -> sub_100008468 : 128 -> 256
```
