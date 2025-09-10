## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

 1301.82.0.0.0
-  __TEXT.__text: 0x43bf0
-  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__text: 0x43c80
+  __TEXT.__auth_stubs: 0x1170
   __TEXT.__const: 0x500
   __TEXT.__gcc_except_tab: 0x268
   __TEXT.__oslogstring: 0x7654

   __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x8c0
+  __AUTH_CONST.__auth_got: 0x8c8
   __AUTH_CONST.__const: 0x10a8
   __AUTH_CONST.__cfstring: 0xa40
   __DATA.__data: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3707835A-44F7-3D5F-83E8-E26D49F7D53C
+  UUID: E4550AEF-8FD4-3CF2-9C1B-02306C5EF979
   Functions: 509
-  Symbols:   1089
+  Symbols:   1090
   CStrings:  1375
 
Symbols:
+ __ZZ12isSeedAndiOSE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 644 -> 652
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
