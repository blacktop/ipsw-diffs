## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/slurpAPFSMeta`

```diff

-  __TEXT.__text: 0x371c4
+  __TEXT.__text: 0x374ec
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x8a74
+  __TEXT.__cstring: 0x8b8d
   __TEXT.__const: 0x1b0
   __TEXT.__unwind_info: 0x6b0
   __DATA_CONST.__const: 0x470

   - /usr/lib/libSystem.B.dylib
   Functions: 533
   Symbols:   144
-  CStrings:  758
+  CStrings:  763
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10000916c : 572 -> 576
~ sub_1000159e4 -> sub_1000159e8 : 1200 -> 1332
~ sub_100018c28 -> sub_100018cb0 : 408 -> 424
~ sub_100019bb8 -> sub_100019c50 : 5248 -> 5364
~ sub_10001ec10 -> sub_10001ed1c : 292 -> 308
~ sub_1000238f4 -> sub_100023a10 : 3380 -> 3600
~ sub_100026374 -> sub_10002656c : 172 -> 180
~ sub_10002b360 -> sub_10002b560 : 2368 -> 2380
~ sub_10002bda0 -> sub_10002bfac : 988 -> 1204
~ sub_10002f66c -> sub_10002f950 : 128 -> 136
~ sub_10003186c -> sub_100031b58 : 316 -> 332
~ sub_1000319a8 -> sub_100031ca4 : 128 -> 164
~ sub_100034e58 -> sub_100035178 : 1736 -> 1744
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"

```
