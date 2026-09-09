## BootCampFormatter

> `/System/Library/Filesystems/ntfs.fs/BootCampFormatter`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA.__data`

```diff

 170.0.0.0.0
-  __TEXT.__text: 0x16dac
+  __TEXT.__text: 0x16da0
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__const: 0x2028
   __TEXT.__cstring: 0x5812
Functions:
~ sub_10000c830 : 248 -> 244
~ sub_10000c95c -> sub_10000c958 : 2988 -> 2980
```
