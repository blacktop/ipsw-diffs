## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1438.40.5.0.0
-  __TEXT.__text: 0x34608
+1438.42.2.0.0
+  __TEXT.__text: 0x34958
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0x508
-  __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0x7c0
-  __TEXT.__oslogstring: 0x1fa9
-  __TEXT.__cstring: 0x2b6d8
+  __TEXT.__objc_stubs: 0x13e0
+  __TEXT.__objc_methlist: 0x514
+  __TEXT.__const: 0x3c8
+  __TEXT.__gcc_except_tab: 0x7e8
+  __TEXT.__oslogstring: 0x202b
+  __TEXT.__cstring: 0x2b6f2
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x13eb
-  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__objc_methname: 0x1434
+  __TEXT.__unwind_info: 0x500
   __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x1a40
+  __DATA_CONST.__cfstring: 0x1a60
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x718
-  __DATA.__objc_selrefs: 0x558
+  __DATA.__objc_selrefs: 0x568
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions
   - /System/Library/PrivateFrameworks/Proximity.framework/Proximity
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  Functions: 307
-  Symbols:   243
-  CStrings:  3765
+  Functions: 312
+  Symbols:   244
+  CStrings:  3771
 
Symbols:
+ _OBJC_CLASS_$_SSRSysdiagnoseFileHandler
CStrings:
+ "Siri Enrollment SPI returned error: %!{(MISSING)public}@"
+ "Siri Enrollment SPI timed out"
+ "Siri Enrollment SpeakerRecognition SPI not available"
+ "TASK_TYPE_SIRI_ENROLLMENT"
+ "fetchSiriEnrollmentLogsWithTimeout:"
+ "fetchVoiceProfileFilePathsWithError:"

```
