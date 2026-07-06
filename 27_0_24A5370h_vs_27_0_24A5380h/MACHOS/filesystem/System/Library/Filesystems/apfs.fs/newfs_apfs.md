## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-  __TEXT.__text: 0x51390
+  __TEXT.__text: 0x516fc
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0xf7d9
+  __TEXT.__cstring: 0xf937
   __TEXT.__const: 0x8480
   __TEXT.__unwind_info: 0x848
   __DATA_CONST.__const: 0x570

   - /usr/lib/libutil.dylib
   Functions: 715
   Symbols:   156
-  CStrings:  1318
+  CStrings:  1324
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10000482c : 160 -> 168
~ sub_10000ddfc -> sub_10000de04 : 316 -> 332
~ sub_10000df38 -> sub_10000df50 : 128 -> 164
~ sub_10001167c -> sub_1000116b8 : 572 -> 576
~ sub_100014d30 -> sub_100014d70 : 5164 -> 5204
~ sub_100027ef8 -> sub_100027f60 : 1208 -> 1364
~ sub_100035aec -> sub_100035bf0 : 340 -> 304
~ sub_100038058 -> sub_100038138 : 1572 -> 1592
~ sub_10003a7d0 -> sub_10003a8c4 : 2548 -> 2556
~ sub_10003b2c4 -> sub_10003b3c0 : 988 -> 1204
~ sub_10003f20c -> sub_10003f3e0 : 128 -> 136
~ sub_10003fa4c -> sub_10003fc28 : 5264 -> 5380
~ sub_1000444a8 -> sub_1000446f8 : 292 -> 308
~ sub_100049a78 -> sub_100049cd8 : 3380 -> 3604
~ sub_10004fcd0 -> sub_100050010 : 168 -> 176
~ sub_10004ff90 -> sub_1000502d8 : 616 -> 628
~ sub_10005025c -> sub_1000505b0 : 244 -> 252
~ sub_100050b04 -> sub_100050e60 : 408 -> 424
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "3283.0.9.502.1"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "3283"

```
