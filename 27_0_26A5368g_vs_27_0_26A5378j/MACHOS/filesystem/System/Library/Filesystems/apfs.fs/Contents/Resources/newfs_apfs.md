## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs`

```diff

-  __TEXT.__text: 0x54178
+  __TEXT.__text: 0x544d4
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__cstring: 0x10470
+  __TEXT.__cstring: 0x105ce
   __TEXT.__const: 0x84a1
   __TEXT.__oslogstring: 0x125
   __TEXT.__unwind_info: 0x8d0

   - /usr/lib/libutil.dylib
   Functions: 806
   Symbols:   161
-  CStrings:  1398
+  CStrings:  1404
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000053c8 : 160 -> 168
~ sub_10000e998 -> sub_10000e9a0 : 316 -> 332
~ sub_10000ead4 -> sub_10000eaec : 128 -> 164
~ sub_10001571c -> sub_100015758 : 5164 -> 5204
~ sub_100028cd4 -> sub_100028d38 : 1200 -> 1332
~ sub_1000367a4 -> sub_10003688c : 348 -> 324
~ sub_100038e68 -> sub_100038f38 : 1572 -> 1592
~ sub_10003b5d8 -> sub_10003b6bc : 2368 -> 2380
~ sub_10003c018 -> sub_10003c108 : 988 -> 1204
~ sub_10003ff38 -> sub_100040100 : 128 -> 136
~ sub_100040778 -> sub_100040948 : 5248 -> 5364
~ sub_100045164 -> sub_1000453a8 : 292 -> 308
~ sub_10004a710 -> sub_10004a964 : 3380 -> 3600
~ sub_1000508b8 -> sub_100050be8 : 168 -> 176
~ sub_100050b60 -> sub_100050e98 : 600 -> 612
~ sub_100050e10 -> sub_100051154 : 244 -> 252
~ sub_1000516b8 -> sub_100051a04 : 408 -> 424
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "3283.0.9.501.1"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"
- "3283"

```
