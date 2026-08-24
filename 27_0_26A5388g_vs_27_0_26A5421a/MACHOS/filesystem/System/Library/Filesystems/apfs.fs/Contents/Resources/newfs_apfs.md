## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.13.501.1
-  __TEXT.__text: 0x546e0
+3288.1.3.0.0
+  __TEXT.__text: 0x54720
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__cstring: 0x106bc
+  __TEXT.__cstring: 0x106b5
   __TEXT.__const: 0x84a1
   __TEXT.__oslogstring: 0x125
   __TEXT.__unwind_info: 0x8d0
Functions:
~ sub_100018704 : 492 -> 520
~ sub_1000265b8 -> sub_1000265d4 : 488 -> 524
CStrings:
+ "3288.1.3"
- "3283.0.13.501.1"
```
