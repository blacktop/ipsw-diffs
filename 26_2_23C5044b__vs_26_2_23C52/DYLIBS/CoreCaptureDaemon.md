## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

 1310.13.0.0.0
-  __TEXT.__text: 0x4483c
-  __TEXT.__auth_stubs: 0x1190
+  __TEXT.__text: 0x448cc
+  __TEXT.__auth_stubs: 0x11a0
   __TEXT.__const: 0x500
   __TEXT.__gcc_except_tab: 0x268
   __TEXT.__oslogstring: 0x7695

   __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x8d8
+  __AUTH_CONST.__auth_got: 0x8e0
   __AUTH_CONST.__const: 0x10e8
   __AUTH_CONST.__cfstring: 0xb60
   __DATA.__data: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 50418B9B-72CD-3A43-983A-5008E4D55A54
+  UUID: 9A9399B5-08AC-30C8-AE1B-8AF11B61382C
   Functions: 513
-  Symbols:   1105
+  Symbols:   1106
   CStrings:  1397
 
Symbols:
+ __ZZ12isSeedAndiOSE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 272 -> 280
~ __ZN10CCDataFile15openCaptureFileEPKcS1_11CCTimestamp : 736 -> 756
~ __ZN10CCDataFile8openFileEPKc : 612 -> 632
~ __ZN9CCDataTap12processEventEv : 4496 -> 4500
~ ____ZN8CCLogTap11tapLoopImplEv_block_invoke : 3344 -> 3348
~ __ZN8CCLogTap12processEventEv : 9324 -> 9332
~ _isSeedAndiOS : 180 -> 200
~ _ifSeedCreateClassCProtectedFile : 124 -> 128
~ _pruneDirectoryOnOSUpgrade : 2332 -> 2340
~ _getSaveLocation : 272 -> 276
~ _getPossibleSaveLocation : 88 -> 96
~ _lowPriorityActivities : 1048 -> 1056
~ __ZN9CCLogFile7addFileEv : 1188 -> 1216

```
