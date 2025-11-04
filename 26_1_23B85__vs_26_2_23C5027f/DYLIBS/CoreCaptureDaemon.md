## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1310.11.0.0.0
-  __TEXT.__text: 0x448cc
-  __TEXT.__auth_stubs: 0x11a0
+1310.13.0.0.0
+  __TEXT.__text: 0x4483c
+  __TEXT.__auth_stubs: 0x1190
   __TEXT.__const: 0x500
   __TEXT.__gcc_except_tab: 0x268
   __TEXT.__oslogstring: 0x7695

   __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__auth_got: 0x8d8
   __AUTH_CONST.__const: 0x10e8
   __AUTH_CONST.__cfstring: 0xb60
   __DATA.__data: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8C7D0145-871C-3C60-A876-838BF4FD5CDE
+  UUID: 7F195095-7BB1-3B36-B11E-69E20DECDEE5
   Functions: 513
-  Symbols:   1106
+  Symbols:   1105
   CStrings:  1397
 
Symbols:
- __ZZ12isSeedAndiOSE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 280 -> 272
~ __ZN10CCDataFile15openCaptureFileEPKcS1_11CCTimestamp : 756 -> 736
~ __ZN10CCDataFile8openFileEPKc : 632 -> 612
~ __ZN9CCDataTap12processEventEv : 4500 -> 4496
~ ____ZN8CCLogTap11tapLoopImplEv_block_invoke : 3348 -> 3344
~ __ZN8CCLogTap12processEventEv : 9332 -> 9324
~ _isSeedAndiOS : 200 -> 180
~ _ifSeedCreateClassCProtectedFile : 128 -> 124
~ _pruneDirectoryOnOSUpgrade : 2340 -> 2332
~ _getSaveLocation : 276 -> 272
~ _getPossibleSaveLocation : 96 -> 88
~ _lowPriorityActivities : 1056 -> 1048
~ __ZN9CCLogFile7addFileEv : 1216 -> 1188

```
