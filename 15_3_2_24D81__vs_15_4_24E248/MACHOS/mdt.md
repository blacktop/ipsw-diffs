## mdt

> `/System/Library/Filesystems/acfs.fs/Contents/bin/mdt`

```diff

-780.80.2.0.1
-  __TEXT.__text: 0x4ac4
+782.100.7.0.0
+  __TEXT.__text: 0x4a30
   __TEXT.__auth_stubs: 0x400
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0xd64
-  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__unwind_info: 0x1a8
   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x28
   __DATA.__data: 0xbc

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: BDD1ABE8-6A92-35BB-9DBB-DBA9722A0138
-  Functions: 136
+  UUID: 28E05924-A517-31DF-8DDC-3AE510784EA4
+  Functions: 134
   Symbols:   823
   CStrings:  118
 
Symbols:
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/vidio/../extapi/libcvextapi.a(cvapi.c.o)
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/vidio/CMakeFiles/mdt_test.dir/mdt.c.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/vidio/CMakeFiles/mdt_test.dir/pio.c.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/vidio/CMakeFiles/mdt_test.dir/vio.c.o
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/extapi/
+ /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/vidio/
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/extapi/libcvextapi.a(cvapi.c.o)
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/vidio/CMakeFiles/mdt_test.dir/mdt.c.o
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/vidio/CMakeFiles/mdt_test.dir/pio.c.o
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/XsanFS/install/TempContent/Objects/snfs/vidio/CMakeFiles/mdt_test.dir/vio.c.o
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/extapi/
- /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/vidio/
Functions:
~ _mdt_run_test : 284 -> 272
~ _mdt_wait_streams_done : 164 -> 148
~ _main : 1268 -> 1360
- sub_100006b18
~ _mdt_do_create_test : 236 -> 232
~ _mdt_do_stat_test : 236 -> 232
~ _mdt_do_chmod_test : 236 -> 232
~ _mdt_do_move_test : 236 -> 232
~ _mdt_do_remove_test : 236 -> 232
~ _mdt_do_cleanup : 192 -> 196
~ _mdt_create_thread : 592 -> 584
~ _mdt_stat_thread : 504 -> 496
~ _mdt_chmod_thread : 424 -> 416
~ _mdt_move_thread : 468 -> 460
~ _mdt_remove_thread : 448 -> 440
~ _pio_popen : 176 -> 172
~ _pio_io : 924 -> 916
- sub_1000090c4
~ _pio_wait_done : 144 -> 132

```
