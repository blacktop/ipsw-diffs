## fsck_apfs

> `System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.701.3
-  __TEXT.__text: 0x53568
+2811.160.7.702.4
+  __TEXT.__text: 0x535b8
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__cstring: 0x19f86
   __TEXT.__const: 0x8700
Functions:
~ sub_10003b8dc : 408 -> 480
~ sub_10003ddf8 -> sub_10003de40 : 1160 -> 1168
CStrings:
+ "2811.160.7.702.4"
- "2811.160.7.701.3"
```
