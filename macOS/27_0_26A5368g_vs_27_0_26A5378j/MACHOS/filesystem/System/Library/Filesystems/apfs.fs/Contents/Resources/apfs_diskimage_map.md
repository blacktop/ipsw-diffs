## apfs_diskimage_map

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_diskimage_map`

```diff

-  __TEXT.__text: 0x4badc
+  __TEXT.__text: 0x4be40
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__cstring: 0xeed3
+  __TEXT.__cstring: 0xefec
   __TEXT.__const: 0x210
   __TEXT.__unwind_info: 0x888
   __DATA_CONST.__const: 0x798

   - /usr/lib/libutil.dylib
   Functions: 696
   Symbols:   138
-  CStrings:  1241
+  CStrings:  1246
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000135f0 : 1200 -> 1332
~ sub_100019e78 -> sub_100019efc : 520 -> 516
~ sub_10001b60c -> sub_10001b68c : 408 -> 424
~ sub_10001ed84 -> sub_10001ee14 : 5164 -> 5204
~ sub_100025ed0 -> sub_100025f88 : 316 -> 332
~ sub_10002600c -> sub_1000260d4 : 128 -> 164
~ sub_10002f6e8 -> sub_10002f7d4 : 348 -> 316
~ sub_100031110 -> sub_1000311dc : 1572 -> 1592
~ sub_100033880 -> sub_100033960 : 2368 -> 2380
~ sub_1000342c0 -> sub_1000343ac : 988 -> 1204
~ sub_100038230 -> sub_1000383f4 : 128 -> 136
~ sub_100038b80 -> sub_100038d4c : 5248 -> 5364
~ sub_10003b5bc -> sub_10003b7fc : 1288 -> 1316
~ sub_10003cc10 -> sub_10003ce6c : 292 -> 308
~ sub_1000421bc -> sub_100042428 : 3380 -> 3600
~ sub_10004bd0c -> sub_10004c054 : 168 -> 176
~ sub_10004bf04 -> sub_10004c254 : 600 -> 612
~ sub_10004c1b4 -> sub_10004c510 : 244 -> 252
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"

```
