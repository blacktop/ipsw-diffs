## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

```diff

-  __TEXT.__text: 0x4f9c8
+  __TEXT.__text: 0x4fd38
   __TEXT.__auth_stubs: 0x790
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x101bd
-  __TEXT.__unwind_info: 0x910
+  __TEXT.__cstring: 0x102d6
+  __TEXT.__unwind_info: 0x908
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__auth_got: 0x3c8

   - /usr/lib/libutil.dylib
   Functions: 750
   Symbols:   136
-  CStrings:  1309
+  CStrings:  1314
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000167f0 : 1200 -> 1332
~ sub_10001d078 -> sub_10001d0fc : 520 -> 516
~ sub_10001e0e4 -> sub_10001e164 : 408 -> 424
~ sub_1000218b0 -> sub_100021940 : 5164 -> 5204
~ sub_1000296e0 -> sub_100029798 : 316 -> 332
~ sub_10002981c -> sub_1000298e4 : 128 -> 164
~ sub_100032ef8 -> sub_100032fe4 : 348 -> 316
~ sub_100034920 -> sub_1000349ec : 1572 -> 1592
~ sub_100037090 -> sub_100037170 : 2368 -> 2380
~ sub_100037ad0 -> sub_100037bbc : 988 -> 1204
~ sub_10003ba40 -> sub_10003bc04 : 128 -> 136
~ sub_10003c390 -> sub_10003c55c : 5248 -> 5364
~ sub_10003ef5c -> sub_10003f19c : 1288 -> 1316
~ sub_1000405b0 -> sub_10004080c : 292 -> 308
~ sub_100045b5c -> sub_100045dc8 : 3380 -> 3600
~ sub_10004f6ac -> sub_10004f9f4 : 168 -> 176
~ sub_10004f8a4 -> sub_10004fbf4 : 600 -> 612
~ sub_10004fb54 -> sub_10004feb0 : 244 -> 252
~ sub_10004fc48 -> sub_10004ffac : 136 -> 148
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"

```
