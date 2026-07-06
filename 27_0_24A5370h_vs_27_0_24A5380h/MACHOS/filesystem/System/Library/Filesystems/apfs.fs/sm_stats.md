## sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

-  __TEXT.__text: 0x43b0c
+  __TEXT.__text: 0x43e4c
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xcc12
+  __TEXT.__cstring: 0xcd2b
   __TEXT.__const: 0x1c8
   __TEXT.__unwind_info: 0x720
   __DATA_CONST.__const: 0x6f8

   - /usr/lib/libutil.dylib
   Functions: 595
   Symbols:   129
-  CStrings:  1051
+  CStrings:  1056
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000047d4 : 316 -> 332
~ sub_100004910 -> sub_100004920 : 128 -> 164
~ sub_100007ec8 -> sub_100007efc : 1728 -> 1756
~ sub_100009920 -> sub_100009970 : 292 -> 308
~ sub_10000f3ac -> sub_10000f40c : 3380 -> 3604
~ sub_10001efec -> sub_10001f12c : 1208 -> 1364
~ sub_100024d40 -> sub_100024f1c : 512 -> 516
~ sub_100025d90 -> sub_100025f70 : 408 -> 424
~ sub_1000311b8 -> sub_1000313a8 : 332 -> 300
~ sub_100032c08 -> sub_100032dd8 : 1572 -> 1592
~ sub_100035380 -> sub_100035564 : 2548 -> 2556
~ sub_100035e74 -> sub_100036060 : 988 -> 1204
~ sub_100039dbc -> sub_10003a080 : 128 -> 136
~ sub_10003a5fc -> sub_10003a8c8 : 5264 -> 5380
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"

```
