## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

 1255.32.0.0.0
-  __TEXT.__text: 0x39a6c
-  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__text: 0x3997c
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__const: 0x4f0
   __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__oslogstring: 0x6377
   __TEXT.__cstring: 0x7638
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__unwind_info: 0x598
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x9f
   __TEXT.__objc_stubs: 0x100

   __DATA_CONST.__const: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__const: 0xff8
   __AUTH_CONST.__cfstring: 0x960
   __DATA.__data: 0x1
   __DATA.__common: 0x4c
-  __DATA.__bss: 0x11b
+  __DATA.__bss: 0x11a
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1A5DBB47-DB36-3C8B-AFAF-3845C227A22A
+  UUID: 2DA781F0-2C05-315D-8199-E8E043CB84C3
   Functions: 470
-  Symbols:   976
+  Symbols:   975
   CStrings:  1173
 
Symbols:
- __ZZ12isSeedAndiOSvE10bootArgSet
Functions:
~ __ZN5CCTap23cleanCaptureDirectoriesEv : 704 -> 672
~ __Z12isSeedAndiOSv : 196 -> 176
~ __ZN19CCIOReportDumpQueue16_processorThreadEv : 3748 -> 3744
~ __ZN9CCLogFile7addFileEv : 1212 -> 1184
~ __ZN10CCDataFile15openCaptureFileEPKcS1_11CCTimestamp : 696 -> 676
~ __ZN10CCDataFile16generateFileNameEPKc : 260 -> 252
~ __ZN10CCDataFile8openFileEPKc : 632 -> 612
~ __ZN9CCDataTap12processEventEv : 4484 -> 4480
~ __ZN6CCFile22generateCaptureDirPathEPKc11CCTimestamp : 856 -> 848
~ ____ZN8CCLogTap11tapLoopImplEv_block_invoke : 3224 -> 3220
~ __ZN8CCLogTap12processEventEv : 8164 -> 8160
~ __Z25pruneDirectoryOnOSUpgradev : 2392 -> 2368
~ __Z15getSaveLocationv : 96 -> 88
~ __Z23getPossibleSaveLocationv : 96 -> 88
~ __Z21lowPriorityActivitiesv : 1108 -> 1072
~ __Z18writeMetadataFilesPK10__CFStringPKc11CCTimestamp : 2652 -> 2644
~ __Z31ifSeedCreateClassCProtectedFilePc : 128 -> 124

```
