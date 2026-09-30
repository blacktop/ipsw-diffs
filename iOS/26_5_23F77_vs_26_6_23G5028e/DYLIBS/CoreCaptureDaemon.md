## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

 1330.5.0.0.0
-  __TEXT.__text: 0x471cc
-  __TEXT.__auth_stubs: 0x1270
+  __TEXT.__text: 0x47134
+  __TEXT.__auth_stubs: 0x1260
   __TEXT.__const: 0x518
   __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__oslogstring: 0x7ad7

   __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x948
+  __AUTH_CONST.__auth_got: 0x940
   __AUTH_CONST.__const: 0x1168
   __AUTH_CONST.__cfstring: 0xc40
   __DATA.__data: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6A74EE66-2985-3061-9803-B182E43EF548
+  UUID: 2B18FCC1-5FD1-3A77-9FC0-8A601225AFFB
   Functions: 532
-  Symbols:   1164
+  Symbols:   1163
   CStrings:  1463
 
Symbols:
- __ZZ12isSeedAndiOSE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 280 -> 272
~ __ZN8CCDaemon23enablePurgeNotificationEv : 1124 -> 1116
~ __ZN10CCDataFile15openCaptureFileEPKcS1_11CCTimestamp : 1320 -> 1300
~ __ZN10CCDataFile8openFileEPKc : 624 -> 604
~ __ZN9CCDataTap12processEventEP19CCDataPipeInterface : 4680 -> 4676
~ __ZN8CCLogTap11tapLoopImplEv : 3524 -> 3520
~ __ZN8CCLogTap12processEventEP18CCLogPipeInterface : 9200 -> 9192
~ _isSeedAndiOS : 200 -> 180
~ _ifSeedCreateClassCProtectedFile : 128 -> 124
~ _pruneDirectoryOnOSUpgrade : 2340 -> 2332
~ _getSaveLocation : 276 -> 272
~ _getPossibleSaveLocation : 96 -> 88
~ _lowPriorityActivities : 1056 -> 1048
~ __ZN9CCLogFile7addFileEv : 1184 -> 1156

```
