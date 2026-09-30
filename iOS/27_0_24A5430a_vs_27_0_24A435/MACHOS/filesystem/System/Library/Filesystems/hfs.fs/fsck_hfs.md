## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

 751.0.0.0.0
-  __TEXT.__text: 0x34ba8
+  __TEXT.__text: 0x34bbc
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x10b4
   __TEXT.__cstring: 0x6e74
Functions:
~ sub_100005314 : 852 -> 816
~ sub_100008fec -> sub_100008fc8 : 1000 -> 1004
~ sub_10000c618 -> sub_10000c5f8 : 2208 -> 2240
~ sub_100011a44 : 6892 -> 6912
~ sub_10002f28c -> sub_10002f2a0 : 736 -> 740
~ sub_100033fbc -> sub_100033fd4 : 2220 -> 2216
```
