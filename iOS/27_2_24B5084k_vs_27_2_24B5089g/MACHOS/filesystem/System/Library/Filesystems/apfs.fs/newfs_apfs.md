## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.40.13.0.0
-  __TEXT.__text: 0x517cc
+3288.40.14.0.0
+  __TEXT.__text: 0x518f8
   __TEXT.__auth_stubs: 0x8e0
   __TEXT.__cstring: 0xfa4e
   __TEXT.__const: 0x8480
Functions:
~ sub_100013334 : 572 -> 596
~ sub_10002f868 -> sub_10002f880 : 68 -> 84
~ sub_100035f28 -> sub_100035f50 : 280 -> 288
~ sub_1000430ac -> sub_1000430dc : 2596 -> 2604
~ sub_100045e88 -> sub_100045ec0 : 1028 -> 1040
~ sub_10004628c -> sub_1000462d0 : 3792 -> 3856
~ sub_1000490cc -> sub_100049150 : 3480 -> 3524
~ sub_100049e64 -> sub_100049f14 : 3596 -> 3720
CStrings:
+ "3288.40.14"
- "3288.40.13"
```
