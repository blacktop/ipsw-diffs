## hfs_convert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/hfs_convert`

```diff

-  __TEXT.__text: 0xb7384
+  __TEXT.__text: 0xb7748
   __TEXT.__auth_stubs: 0x11a0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1a665
+  __TEXT.__cstring: 0x1a7c3
   __TEXT.__const: 0xa428
   __TEXT.__objc_methname: 0x48
   __TEXT.__unwind_info: 0x1c98

   - /usr/lib/libz.1.dylib
   Functions: 2067
   Symbols:   307
-  CStrings:  2763
+  CStrings:  2769
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000013ec : 1288 -> 1316
~ sub_100006dc0 -> sub_100006ddc : 23924 -> 23928
~ sub_1000105e4 -> sub_100010604 : 776 -> 784
~ sub_100012794 -> sub_1000127bc : 452 -> 428
~ sub_1000180a8 -> sub_1000180b8 : 256 -> 232
~ sub_10001a3e4 -> sub_10001a3dc : 300 -> 276
~ sub_100028a6c -> sub_100028a4c : 1200 -> 1332
~ sub_10002e98c -> sub_10002e9f0 : 144 -> 152
~ sub_10002f49c -> sub_10002f508 : 348 -> 344
~ sub_10002f5f8 -> sub_10002f660 : 300 -> 308
~ sub_100032380 -> sub_1000323f0 : 5164 -> 5204
~ sub_100038c34 -> sub_100038ccc : 4664 -> 4668
~ sub_1000428c8 -> sub_100042964 : 8 -> 12
~ sub_100043090 -> sub_100043130 : 316 -> 332
~ sub_1000431cc -> sub_10004327c : 128 -> 164
~ sub_100047e7c -> sub_100047f50 : 348 -> 316
~ sub_100049804 -> sub_1000498b8 : 1572 -> 1592
~ sub_10004be70 -> sub_10004bf38 : 2368 -> 2380
~ sub_10004c8b0 -> sub_10004c984 : 988 -> 1204
~ sub_10004ff6c -> sub_100050118 : 128 -> 136
~ sub_1000507ac -> sub_100050960 : 5248 -> 5364
~ sub_100059fec -> sub_10005a214 : 292 -> 308
~ sub_10005f554 -> sub_10005f78c : 3380 -> 3600
~ sub_100065fc0 -> sub_1000662d4 : 168 -> 176
~ sub_100066268 -> sub_100066584 : 600 -> 612
~ sub_100066518 -> sub_100066840 : 244 -> 252
~ sub_10006660c -> sub_10006693c : 136 -> 148
~ sub_100066694 -> sub_1000669d0 : 240 -> 252
~ sub_100067a24 -> sub_100067d6c : 7960 -> 8020
~ sub_10006aa74 -> sub_10006adf8 : 1696 -> 1692
~ sub_10006f108 -> sub_10006f488 : 568 -> 580
~ sub_100080eec -> sub_100081278 : 768 -> 780
~ sub_100085360 -> sub_1000856f8 : 860 -> 876
~ sub_100088514 -> sub_1000888bc : 776 -> 792
~ sub_100089fb0 -> sub_10008a368 : 192 -> 184
~ sub_10008a070 -> sub_10008a420 : 228 -> 220
~ sub_10008a4e8 -> sub_10008a890 : 176 -> 160
~ sub_100092600 -> sub_100092998 : 56 -> 48
~ sub_10009b20c -> sub_10009b59c : 724 -> 740
~ sub_10009df44 -> sub_10009e2e4 : 768 -> 780
~ sub_1000a5c7c -> sub_1000a6028 : 768 -> 772
~ sub_1000b56d0 -> sub_1000b5a80 : 1124 -> 1144
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/core-storage/blk_header.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/core-storage/btree_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/core-storage/compositedisk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/core-storage/csconverter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/core-storage/devio_userlevel_context.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/core-storage/lv_readwrite.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/core-storage/txn.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/hfs/hfs_btree.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/hfs/hfs_convert.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/hfs/hfs_dev_io.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/hfs/hfs_stream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/hfs/hfs_vol.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/hfs/lwvm.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
+ "3283.0.9.501.1"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/core-storage/blk_header.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/core-storage/btree_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/core-storage/compositedisk.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/core-storage/csconverter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/core-storage/devio_userlevel_context.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/core-storage/lv_readwrite.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/core-storage/txn.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/hfs/hfs_btree.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/hfs/hfs_convert.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/hfs/hfs_dev_io.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/hfs/hfs_stream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/hfs/hfs_vol.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/hfs/lwvm.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"
- "3283"

```
