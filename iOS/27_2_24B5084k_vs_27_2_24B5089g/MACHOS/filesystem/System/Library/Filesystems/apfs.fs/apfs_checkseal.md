## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.40.13.0.0
-  __TEXT.__text: 0x4fafc
+3288.40.14.0.0
+  __TEXT.__text: 0x4fc18
   __TEXT.__auth_stubs: 0x760
   __TEXT.__const: 0x4c0
   __TEXT.__cstring: 0x10117
Functions:
~ sub_100020698 : 572 -> 596
~ sub_100041b7c -> sub_100041b94 : 1028 -> 1040
~ sub_100041f80 -> sub_100041fa4 : 3792 -> 3856
~ sub_100044dc0 -> sub_100044e24 : 3480 -> 3524
~ sub_100045b58 -> sub_100045be8 : 3596 -> 3720
~ sub_100048de4 -> sub_100048ef0 : 68 -> 84
```
