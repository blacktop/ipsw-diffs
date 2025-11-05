## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x56fbc
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__cstring: 0x114c5
-  __TEXT.__const: 0x7fe1
+2332.101.1.0.0
+  __TEXT.__text: 0x56d50
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__cstring: 0x11573
+  __TEXT.__const: 0x8071
   __TEXT.__oslogstring: 0xfd
-  __TEXT.__unwind_info: 0x928
-  __DATA_CONST.__auth_got: 0x448
+  __TEXT.__unwind_info: 0x920
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x598
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__cfstring: 0x1a0
-  __DATA.__data: 0x142
+  __DATA.__data: 0x152
   __DATA.__common: 0x418
   __DATA.__bss: 0x3d
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 9A9BBCB4-2C08-31F4-BFE1-75A2565BB9FD
-  Functions: 783
-  Symbols:   154
-  CStrings:  1474
+  UUID: 46C5A5A1-F8AE-38C2-BA94-430D0F928021
+  Functions: 814
+  Symbols:   160
+  CStrings:  1484
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
CStrings:
+ "!((apfs)->apfs_main_apfs != ((void*)0))"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "((&crypto_cache->free_list)->tqh_first == ((void*)0))"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
+ "2332.101.1"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "sha3_256"
+ "sha3_256_4k"
+ "sha3_384"
+ "sha3_384_4k"
+ "sha3_512"
+ "sha3_512_4k"
+ "spaceman_alloc_iterate_chunks"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "((&crypto_cache->free_list)->tqh_first == ((void *)0))"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "2317.81.2"

```
