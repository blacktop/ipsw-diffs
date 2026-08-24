## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.13.501.1
-  __TEXT.__text: 0x4ff50
+3288.1.3.0.0
+  __TEXT.__text: 0x4ff8c
   __TEXT.__auth_stubs: 0x790
   __TEXT.__const: 0x4c0
   __TEXT.__cstring: 0x103c4
Functions:
~ sub_100013fe8 : 488 -> 524
~ sub_10001d128 -> sub_10001d14c : 520 -> 516
~ sub_100024810 -> sub_100024830 : 492 -> 520
```
