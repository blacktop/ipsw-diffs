## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.60.7.0.0
-  __TEXT.__text: 0x4cd78
+3288.60.11.0.1
+  __TEXT.__text: 0x4cd80
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0xf816
+  __TEXT.__cstring: 0xf81b
   __TEXT.__const: 0x220
   __TEXT.__unwind_info: 0xa58
   __DATA_CONST.__const: 0x8f8
Functions:
~ sub_10004cd78 : 100 -> 108
CStrings:
+ "3288.60.11.0.1"
- "3288.60.7"
```
