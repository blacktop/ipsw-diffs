## sm_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

```diff

-  __TEXT.__text: 0x43818
+  __TEXT.__text: 0x43b4c
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xcc84
+  __TEXT.__cstring: 0xcd9d
   __TEXT.__const: 0x1c8
   __TEXT.__unwind_info: 0x728
   __DATA_CONST.__const: 0x6f8

   - /usr/lib/libutil.dylib
   Functions: 595
   Symbols:   129
-  CStrings:  1053
+  CStrings:  1058
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10000479c : 316 -> 332
~ sub_1000048d8 -> sub_1000048e8 : 128 -> 164
~ sub_100007e9c -> sub_100007ed0 : 1696 -> 1732
~ sub_1000098a8 -> sub_100009900 : 292 -> 308
~ sub_10000f310 -> sub_10000f378 : 3380 -> 3600
~ sub_10001ef08 -> sub_10001f04c : 1200 -> 1332
~ sub_100024c80 -> sub_100024e48 : 512 -> 520
~ sub_100025cd4 -> sub_100025ea4 : 408 -> 424
~ sub_100030f3c -> sub_10003111c : 348 -> 316
~ sub_100032964 -> sub_100032b24 : 1572 -> 1592
~ sub_1000350d4 -> sub_1000352a8 : 2368 -> 2380
~ sub_100035b14 -> sub_100035cf4 : 988 -> 1204
~ sub_100039a34 -> sub_100039cec : 128 -> 136
~ sub_10003a274 -> sub_10003a534 : 5248 -> 5364
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
