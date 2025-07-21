## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

 1255.32.0.0.0
-  __TEXT.__text: 0x3997c
-  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__text: 0x39a6c
+  __TEXT.__auth_stubs: 0xf60
   __TEXT.__const: 0x4f0
   __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__oslogstring: 0x6377
   __TEXT.__cstring: 0x7638
-  __TEXT.__unwind_info: 0x598
+  __TEXT.__unwind_info: 0x5a0
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x9f
   __TEXT.__objc_stubs: 0x100

   __DATA_CONST.__const: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0xff8
   __AUTH_CONST.__cfstring: 0x960
   __DATA.__data: 0x1
   __DATA.__common: 0x4c
-  __DATA.__bss: 0x11a
+  __DATA.__bss: 0x11b
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 59E463BA-2F49-3AB5-AA86-596224B311C5
+  UUID: 1B4DD6E4-7664-3962-B4D9-591179B2A394
   Functions: 470
-  Symbols:   975
+  Symbols:   976
   CStrings:  1173
 
Symbols:
+ __ZZ12isSeedAndiOSvE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 672 -> 704
~ __Z12isSeedAndiOSv : 176 -> 196
~ __ZN19CCIOReportDumpQueue16_processorThreadEv : 3744 -> 3748
~ __ZN9CCLogFile7addFileEv : 1184 -> 1212
~ __ZN10CCDataFile15openCaptureFileEPKcS1_11CCTimestamp : 676 -> 696
~ __ZN10CCDataFile16generateFileNameEPKc : 252 -> 260
~ __ZN10CCDataFile8openFileEPKc : 612 -> 632
~ __ZN9CCDataTap12processEventEv : 4480 -> 4484
~ __ZN6CCFile22generateCaptureDirPathEPKc11CCTimestamp : 848 -> 856
~ ____ZN8CCLogTap11tapLoopImplEv_block_invoke : 3220 -> 3224
~ __ZN8CCLogTap12processEventEv : 8160 -> 8164
~ __Z25pruneDirectoryOnOSUpgradev : 2368 -> 2392
~ __Z15getSaveLocationv : 88 -> 96
~ __Z23getPossibleSaveLocationv : 88 -> 96
~ __Z21lowPriorityActivitiesv : 1072 -> 1108
~ __Z18writeMetadataFilesPK10__CFStringPKc11CCTimestamp : 2644 -> 2652
~ __Z31ifSeedCreateClassCProtectedFilePc : 124 -> 128

```
