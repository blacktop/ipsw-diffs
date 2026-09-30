## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.40.13.0.0
-  __TEXT.__text: 0x5a2d4
+3288.40.14.0.0
+  __TEXT.__text: 0x5a3f0
   __TEXT.__auth_stubs: 0xa10
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x750
Functions:
~ sub_1000342d4 : 572 -> 596
~ sub_10004c690 -> sub_10004c6a8 : 1028 -> 1040
~ sub_10004ca94 -> sub_10004cab8 : 3792 -> 3856
~ sub_10004f8d4 -> sub_10004f938 : 3480 -> 3524
~ sub_10005066c -> sub_1000506fc : 3596 -> 3720
~ sub_1000538f8 -> sub_100053a04 : 68 -> 84
CStrings:
+ "3288.40.14"
- "3288.40.13"
```
