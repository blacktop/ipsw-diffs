## apfs_invert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert`

```diff

-  __TEXT.__text: 0x51fbc
+  __TEXT.__text: 0x5233c
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0x10da8
+  __TEXT.__cstring: 0x10ecb
   __TEXT.__const: 0x8418
   __TEXT.__unwind_info: 0x928
   __DATA_CONST.__const: 0x838

   - /usr/lib/libutil.dylib
   Functions: 753
   Symbols:   143
-  CStrings:  1402
+  CStrings:  1407
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000b60 : 1288 -> 1316
~ sub_100016790 -> sub_1000167ac : 408 -> 424
~ sub_100017818 -> sub_100017844 : 316 -> 332
~ sub_100017954 -> sub_100017990 : 128 -> 164
~ sub_10001ce30 -> sub_10001ce90 : 5164 -> 5204
~ sub_1000345cc -> sub_100034654 : 1200 -> 1332
~ sub_10003893c -> sub_100038a48 : 356 -> 328
~ sub_10003a714 -> sub_10003a804 : 1572 -> 1592
~ sub_10003ce84 -> sub_10003cf88 : 2368 -> 2380
~ sub_10003d8cc -> sub_10003d9dc : 988 -> 1204
~ sub_10004183c -> sub_100041a24 : 128 -> 136
~ sub_100042318 -> sub_100042508 : 5248 -> 5364
~ sub_100045b4c -> sub_100045db0 : 292 -> 308
~ sub_10004b0f8 -> sub_10004b36c : 3380 -> 3600
~ sub_100050ed0 -> sub_100051220 : 168 -> 176
~ sub_100051178 -> sub_1000514d0 : 600 -> 612
~ sub_100051428 -> sub_10005178c : 244 -> 252
~ sub_10005151c -> sub_100051888 : 136 -> 148
~ sub_100051b50 -> sub_100051ec8 : 144 -> 152
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
+ "3283.0.9.501.1"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"
- "3283"

```
