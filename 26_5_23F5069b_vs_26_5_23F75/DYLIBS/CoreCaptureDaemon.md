## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

 1330.5.0.0.0
-  __TEXT.__text: 0x47134
-  __TEXT.__auth_stubs: 0x1260
+  __TEXT.__text: 0x471cc
+  __TEXT.__auth_stubs: 0x1270
   __TEXT.__const: 0x518
   __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__oslogstring: 0x7ad7

   __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x940
+  __AUTH_CONST.__auth_got: 0x948
   __AUTH_CONST.__const: 0x1168
   __AUTH_CONST.__cfstring: 0xc40
   __DATA.__data: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 41A45CDC-D45C-3F96-A728-5729E8A88DC1
+  UUID: 6A74EE66-2985-3061-9803-B182E43EF548
   Functions: 532
-  Symbols:   1163
+  Symbols:   1164
   CStrings:  1463
 
Symbols:
+ __ZZ12isSeedAndiOSE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 272 -> 280
~ __ZN8CCDaemon23enablePurgeNotificationEv : 1116 -> 1124
~ __ZN10CCDataFile15openCaptureFileEPKcS1_11CCTimestamp : 1300 -> 1320
~ __ZN10CCDataFile8openFileEPKc : 604 -> 624
~ __ZN9CCDataTap12processEventEP19CCDataPipeInterface : 4676 -> 4680
~ __ZN8CCLogTap11tapLoopImplEv : 3520 -> 3524
~ __ZN8CCLogTap12processEventEP18CCLogPipeInterface : 9192 -> 9200
~ _isSeedAndiOS : 180 -> 200
~ _ifSeedCreateClassCProtectedFile : 124 -> 128
~ _pruneDirectoryOnOSUpgrade : 2332 -> 2340
~ _getSaveLocation : 272 -> 276
~ _getPossibleSaveLocation : 88 -> 96
~ _lowPriorityActivities : 1048 -> 1056
~ __ZN9CCLogFile7addFileEv : 1156 -> 1184

```
