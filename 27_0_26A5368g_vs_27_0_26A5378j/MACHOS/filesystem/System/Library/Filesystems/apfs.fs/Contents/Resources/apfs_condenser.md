## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_condenser`

```diff

-  __TEXT.__text: 0x4d22c
+  __TEXT.__text: 0x4d598
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__cstring: 0xf960
+  __TEXT.__cstring: 0xfa83
   __TEXT.__const: 0x220
   __TEXT.__unwind_info: 0x850
   __DATA_CONST.__const: 0x8f8

   - /usr/lib/libutil.dylib
   Functions: 688
   Symbols:   144
-  CStrings:  1293
+  CStrings:  1298
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000bd0 : 1288 -> 1316
~ sub_100010428 -> sub_100010444 : 408 -> 424
~ sub_100011374 -> sub_1000113a0 : 316 -> 332
~ sub_1000114b0 -> sub_1000114ec : 128 -> 164
~ sub_10001697c -> sub_1000169dc : 5164 -> 5204
~ sub_10002cc64 -> sub_10002ccec : 1200 -> 1332
~ sub_100030ee4 -> sub_100030ff0 : 348 -> 316
~ sub_100031040 -> sub_10003112c : 272 -> 276
~ sub_100036670 -> sub_100036760 : 1572 -> 1592
~ sub_100038de0 -> sub_100038ee4 : 2368 -> 2380
~ sub_100039820 -> sub_100039930 : 988 -> 1204
~ sub_10003d790 -> sub_10003d978 : 128 -> 136
~ sub_10003dff0 -> sub_10003e1e0 : 5248 -> 5364
~ sub_100041824 -> sub_100041a88 : 292 -> 308
~ sub_100047088 -> sub_1000472fc : 3380 -> 3600
~ sub_10004ce60 -> sub_10004d1b0 : 168 -> 176
~ sub_10004d058 -> sub_10004d3b0 : 600 -> 612
~ sub_10004d308 -> sub_10004d66c : 244 -> 252
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
+ "3283.0.9.501.1"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"
- "3283"

```
