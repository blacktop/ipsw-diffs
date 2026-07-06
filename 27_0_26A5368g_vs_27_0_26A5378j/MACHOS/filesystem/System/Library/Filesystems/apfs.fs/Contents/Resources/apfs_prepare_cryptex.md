## apfs_prepare_cryptex

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex`

```diff

-  __TEXT.__text: 0x6f9bc
+  __TEXT.__text: 0x6fd44
   __TEXT.__auth_stubs: 0x840
   __TEXT.__const: 0xc4fa
-  __TEXT.__cstring: 0x1826a
+  __TEXT.__cstring: 0x1838d
   __TEXT.__unwind_info: 0xc78
   __DATA_CONST.__const: 0x1140
   __DATA_CONST.__cfstring: 0x160

   - /usr/lib/libutil.dylib
   Functions: 1024
   Symbols:   148
-  CStrings:  2095
+  CStrings:  2100
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000060e0 : 196 -> 188
~ sub_1000223ec -> sub_1000223e4 : 1200 -> 1332
~ sub_100029f74 -> sub_100029ff0 : 508 -> 512
~ sub_10002da84 -> sub_10002db04 : 408 -> 424
~ sub_10002ef74 -> sub_10002f004 : 348 -> 344
~ sub_10002f0d8 -> sub_10002f164 : 300 -> 308
~ sub_100031664 -> sub_1000316f8 : 5164 -> 5204
~ sub_1000376d8 -> sub_100037794 : 292 -> 296
~ sub_10003c964 -> sub_10003ca24 : 4672 -> 4676
~ sub_100047464 -> sub_100047528 : 316 -> 332
~ sub_1000475a0 -> sub_100047674 : 128 -> 164
~ sub_100050d84 -> sub_100050e7c : 348 -> 316
~ sub_1000527ac -> sub_100052884 : 1572 -> 1592
~ sub_100054f38 -> sub_100055024 : 2368 -> 2380
~ sub_100055978 -> sub_100055a70 : 988 -> 1204
~ sub_100059934 -> sub_100059b04 : 128 -> 136
~ sub_10005c040 -> sub_10005c218 : 5248 -> 5364
~ sub_10005eb18 -> sub_10005ed64 : 1288 -> 1316
~ sub_10006027c -> sub_1000604e4 : 292 -> 308
~ sub_100065bb8 -> sub_100065e30 : 3380 -> 3600
~ sub_10006f874 -> sub_10006fbc8 : 168 -> 176
~ sub_10006fb1c -> sub_10006fe78 : 600 -> 612
~ sub_10006fdcc -> sub_100070134 : 244 -> 252
~ sub_10006fec0 -> sub_100070230 : 136 -> 148
~ sub_10006ff48 -> sub_1000702c4 : 240 -> 252
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/fscommon/purging.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
+ "3283.0.9.501.1"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/fscommon/purging.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"
- "3283"

```
