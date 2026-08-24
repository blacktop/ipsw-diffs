## apfs_prepare_cryptex

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.13.501.1
-  __TEXT.__text: 0x6ff5c
+3288.1.3.0.0
+  __TEXT.__text: 0x6ffc8
   __TEXT.__auth_stubs: 0x840
   __TEXT.__const: 0xc4fa
-  __TEXT.__cstring: 0x1847c
+  __TEXT.__cstring: 0x18478
   __TEXT.__unwind_info: 0xc78
   __DATA_CONST.__const: 0x1140
   __DATA_CONST.__cfstring: 0x160
Functions:
~ sub_10001fb04 : 488 -> 524
~ sub_10002a01c -> sub_10002a040 : 516 -> 512
~ sub_100035d44 -> sub_100035d64 : 492 -> 520
~ sub_10003976c -> sub_1000397a8 : 776 -> 780
~ sub_10003b9d0 -> sub_10003ba10 : 1068 -> 1112
CStrings:
+ "3288.1.3"
+ "decrement_dstream_id_for_deletion_ex"
- "3283.0.13.501.1"
- "decrement_dstream_id_for_deletion"
```
