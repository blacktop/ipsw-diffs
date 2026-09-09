## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

 3288.2.1.0.0
-  __TEXT.__text: 0x56a7c
+  __TEXT.__text: 0x56b04
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__cstring: 0x1a6d8
   __TEXT.__const: 0x8730
Functions:
~ sub_100002f80 : 1980 -> 2108
~ sub_10000640c -> sub_10000648c : 1476 -> 1484
~ sub_100014d1c -> sub_100014da4 : 572 -> 564
~ sub_10001ec94 -> sub_10001ed14 : 132 -> 136
~ sub_10001ed60 -> sub_10001ede4 : 72 -> 76
~ sub_10001eda8 -> sub_10001ee30 : 308 -> 312
~ sub_10001ef74 -> sub_10001f000 : 164 -> 168
~ sub_10002680c -> sub_10002689c : 5036 -> 5028
~ sub_100027c9c -> sub_100027d24 : 356 -> 352
~ sub_10002ce18 -> sub_10002ce9c : 872 -> 864
~ sub_1000305b4 -> sub_100030630 : 480 -> 476
~ sub_100030794 -> sub_10003080c : 444 -> 440
~ sub_100032f20 -> sub_100032f94 : 704 -> 712
~ sub_100037a88 -> sub_100037b04 : 1172 -> 1180
~ sub_10003b9a8 -> sub_10003ba2c : 668 -> 680
~ sub_10003c988 -> sub_10003ca18 : 1096 -> 1088
~ sub_100040cc8 -> sub_100040d50 : 1176 -> 1168
~ sub_100042cb8 -> sub_100042d38 : 480 -> 476
~ sub_100042e98 -> sub_100042f14 : 288 -> 292
~ sub_100045d1c -> sub_100045d9c : 1372 -> 1380
```
