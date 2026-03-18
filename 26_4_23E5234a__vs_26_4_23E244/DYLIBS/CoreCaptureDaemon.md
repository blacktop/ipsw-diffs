## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

 1325.18.0.0.0
-  __TEXT.__text: 0x472e8
-  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__text: 0x47380
+  __TEXT.__auth_stubs: 0x1260
   __TEXT.__const: 0x518
   __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__oslogstring: 0x7c39

   __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__auth_got: 0x940
   __AUTH_CONST.__const: 0x1168
   __AUTH_CONST.__cfstring: 0xc40
   __DATA.__data: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 56113CA2-D368-3571-9919-D3E0719B9395
+  UUID: 4B82F087-B611-33FE-84E8-6FA57E591BA1
   Functions: 530
-  Symbols:   1158
+  Symbols:   1159
   CStrings:  1467
 
Symbols:
+ __ZZ12isSeedAndiOSE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 272 -> 280
~ __ZN8CCDaemon23enablePurgeNotificationEv : 1116 -> 1124
~ __ZN10CCDataFile15openCaptureFileEPKcS1_11CCTimestamp : 1300 -> 1320
~ __ZN10CCDataFile8openFileEPKc : 604 -> 624
~ __ZN9CCDataTap12processEventEv : 4464 -> 4468
~ __ZN8CCLogTap11tapLoopImplEv : 3516 -> 3520
~ __ZN8CCLogTap12processEventEv : 9276 -> 9284
~ _isSeedAndiOS : 180 -> 200
~ _ifSeedCreateClassCProtectedFile : 124 -> 128
~ _pruneDirectoryOnOSUpgrade : 2332 -> 2340
~ _getSaveLocation : 272 -> 276
~ _getPossibleSaveLocation : 88 -> 96
~ _lowPriorityActivities : 1048 -> 1056
~ __ZN9CCLogFile7addFileEv : 1156 -> 1184

```
