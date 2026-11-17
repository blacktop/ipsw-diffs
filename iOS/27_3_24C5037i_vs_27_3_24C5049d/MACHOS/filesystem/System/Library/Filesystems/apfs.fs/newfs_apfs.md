## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.60.7.0.0
-  __TEXT.__text: 0x51874
+3288.60.11.0.1
+  __TEXT.__text: 0x5187c
   __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__cstring: 0xfa9f
+  __TEXT.__cstring: 0xfaa4
   __TEXT.__const: 0x8480
   __TEXT.__unwind_info: 0xae0
   __DATA_CONST.__const: 0x570
Functions:
~ sub_100050700 : 100 -> 108
CStrings:
+ "3288.60.11.0.1"
- "3288.60.7"
```
