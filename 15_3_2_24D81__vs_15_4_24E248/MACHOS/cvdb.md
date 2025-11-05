## cvdb

> `/System/Library/Filesystems/acfs.fs/Contents/bin/cvdb`

```diff

-780.80.2.0.1
-  __TEXT.__text: 0x4a2c
+782.100.7.0.0
+  __TEXT.__text: 0x4ab4
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x223a
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x2234
+  __TEXT.__unwind_info: 0x110
   __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0x28
   __DATA.__data: 0x830
   __DATA.__bss: 0x18c
-  __DATA.__common: 0x28
+  __DATA.__common: 0x2c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libedit.3.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: FF6935C0-398B-3A7D-90DD-97620186316A
-  Functions: 67
+  UUID: 5E953160-80B8-33E1-9B3C-2C23C8AD82AF
+  Functions: 66
   Symbols:   444
-  CStrings:  297
+  CStrings:  295
 
Symbols:
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/../../libutil/libsnutil-static.a(dopanic.c.o)
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/../../libutil/libsnutil-static.a(logger.c.o)
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/../../libutil/libsnutil-static.a(resolvshim.c.o)
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/../../libutil/libsnutil-static.a(snprintf.c.o)
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/CMakeFiles/cvdb.dir/cvdb_common.c.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/client/util/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/libutil/
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/CMakeFiles/cvdb.dir/cvdb_common.c.o
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/libutil/libsnutil-static.a(dopanic.c.o)
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/libutil/libsnutil-static.a(logger.c.o)
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/libutil/libsnutil-static.a(resolvshim.c.o)
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/libutil/libsnutil-static.a(snprintf.c.o)
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/client/util/
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/libutil/
Functions:
~ _get_log_buffer : 1276 -> 1296
~ _cacheinfo_init : 100 -> 104
~ _fmt_odd_size : 468 -> 536
~ _main : 4496 -> 4504
~ _PanicCheckedWriteLog : 312 -> 328
~ _mylog : 400 -> 440
- sub_100009104
~ _CvVsnprintf : 112 -> 124
~ get_log_buffer.cold.1 : 64 -> 68
~ get_log_buffer.cold.2 : 68 -> 64
~ main.cold.1 : 92 -> 64
~ main.cold.2 : 56 -> 64
~ main.cold.3 : 64 -> 56
~ main.cold.4 : 64 -> 92
CStrings:
- "@@"
- "on"

```
