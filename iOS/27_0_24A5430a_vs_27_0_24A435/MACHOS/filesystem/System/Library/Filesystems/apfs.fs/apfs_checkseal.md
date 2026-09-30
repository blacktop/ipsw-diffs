## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

 3288.2.1.0.0
-  __TEXT.__text: 0x4fd84
+  __TEXT.__text: 0x4fef8
   __TEXT.__auth_stubs: 0x760
   __TEXT.__const: 0x4c0
   __TEXT.__cstring: 0x10104
Functions:
~ sub_100008350 : 636 -> 664
~ sub_10000876c -> sub_100008788 : 844 -> 868
~ sub_10000a1dc -> sub_10000a210 : 244 -> 252
~ sub_10000a2d0 -> sub_10000a30c : 244 -> 248
~ sub_10000a3c4 -> sub_10000a404 : 304 -> 308
~ sub_10000a4f4 -> sub_10000a538 : 364 -> 368
~ sub_10000ab2c -> sub_10000ab74 : 236 -> 240
~ sub_10000b1f4 -> sub_10000b240 : 36 -> 40
~ sub_10000b218 -> sub_10000b268 : 40 -> 44
~ sub_10000b240 -> sub_10000b294 : 44 -> 48
~ sub_10000b3f8 -> sub_10000b450 : 220 -> 224
~ sub_10000d858 -> sub_10000d8b4 : 2480 -> 2640
~ sub_10000e6d8 -> sub_10000e7d4 : 240 -> 244
~ sub_10000e9d0 -> sub_10000ead0 : 8316 -> 8324
~ sub_100015148 -> sub_100015250 : 2688 -> 2696
~ sub_1000168e4 -> sub_1000169f4 : 1364 -> 1368
~ sub_100017964 -> sub_100017a78 : 2136 -> 2156
~ sub_10001befc -> sub_10001c024 : 1276 -> 1280
~ sub_10001d1f4 -> sub_10001d320 : 508 -> 512
~ sub_10002cc3c -> sub_10002cd6c : 10480 -> 10440
~ sub_100042170 -> sub_100042278 : 3728 -> 3796
~ sub_100045d3c -> sub_100045e88 : 3604 -> 3612
~ sub_10004a4b4 -> sub_10004a608 : 1056 -> 1060
~ sub_10004ab7c -> sub_10004acd4 : 268 -> 272
~ sub_10004ac88 -> sub_10004ade4 : 2280 -> 2288
~ sub_10004fc04 -> sub_10004fd68 : 628 -> 640
~ sub_10004fedc -> sub_10005004c : 252 -> 256
```
