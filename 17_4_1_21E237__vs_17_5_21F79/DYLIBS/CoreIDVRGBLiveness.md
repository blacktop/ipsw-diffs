## CoreIDVRGBLiveness

> `/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness`

```diff

-6.406.0.0.0
-  __TEXT.__text: 0x230fc
+6.504.0.0.0
+  __TEXT.__text: 0x23a9c
   __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x1bbc
+  __TEXT.__objc_methlist: 0x1bdc
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x166a
-  __TEXT.__oslogstring: 0x21b8
-  __TEXT.__gcc_except_tab: 0x6a4
-  __TEXT.__unwind_info: 0x9a0
+  __TEXT.__cstring: 0x1688
+  __TEXT.__oslogstring: 0x21f8
+  __TEXT.__gcc_except_tab: 0x6cc
+  __TEXT.__unwind_info: 0x9e0
   __TEXT.__objc_classname: 0x390
-  __TEXT.__objc_methname: 0x64d7
+  __TEXT.__objc_methname: 0x6539
   __TEXT.__objc_methtype: 0x107f
-  __TEXT.__objc_stubs: 0x6140
+  __TEXT.__objc_stubs: 0x6180
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4108
-  __DATA_CONST.__objc_selrefs: 0x1a70
+  __DATA_CONST.__objc_const: 0x4128
+  __DATA_CONST.__objc_selrefs: 0x1a90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x318
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__cfstring: 0x1340
   __AUTH_CONST.__objc_const: 0x5e0
-  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x3e0
-  __AUTH.__objc_data: 0x4b0
+  __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x464
   __DATA.__data: 0x480
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 947
-  Symbols:   3545
-  CStrings:  1747
+  Functions: 966
+  Symbols:   3588
+  CStrings:  1754
 
Symbols:
+ -[CIDVRGBAVCaptureFileOutput invalidateRecording].cold.1
+ -[CIDVRGBAVCaptureFileOutput recordFrame:].cold.3
+ -[CIDVRGBAVCaptureFileOutput restartRecordingWithCompletionHandler:].cold.1
+ -[CIDVRGBAVCaptureFileOutput startRecording].cold.3
+ -[CIDVRGBAVCaptureFileOutput stopRecording].cold.1
+ -[_CIDVRGBAVSessionManagerBase resumeRecordingWithCompletionHandler:]
+ -[_CIDVRGBCaptureSelfieController _startClassifier]
+ -[_CIDVRGBCaptureSelfieController _startLivenessWithCompletionHandler:]
+ GCC_except_table17
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table74
+ ___37-[_CIDVRGBAVSessionManagerBase setup]_block_invoke.46
+ ___48-[_CIDVRGBCaptureSelfieController startLiveness]_block_invoke
+ ___50-[_CIDVRGBCaptureSelfieController _finishLiveness]_block_invoke_2.200
+ ___50-[_CIDVRGBCaptureSelfieController restartLiveness]_block_invoke.109
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke.183
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke.183.cold.1
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke.183.cold.2
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke_2
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke_3
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke_4
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke_5
+ ___51-[_CIDVRGBCaptureSelfieController _startClassifier]_block_invoke_5.cold.1
+ ___57-[_CIDVRGBCaptureSelfieController didCapturePhoto:error:]_block_invoke.145
+ ___69-[_CIDVRGBAVSessionManagerBase resumeRecordingWithCompletionHandler:]_block_invoke
+ ___71-[_CIDVRGBCaptureSelfieController _startLivenessWithCompletionHandler:]_block_invoke
+ ___71-[_CIDVRGBCaptureSelfieController _startLivenessWithCompletionHandler:]_block_invoke_2
+ ___87-[_CIDVRGBAVSessionManager dataOutputSynchronizer:didOutputSynchronizedDataCollection:]_block_invoke.208
+ ___87-[_CIDVRGBAVSessionManager dataOutputSynchronizer:didOutputSynchronizedDataCollection:]_block_invoke.cold.1
+ ___87-[_CIDVRGBAVSessionManager dataOutputSynchronizer:didOutputSynchronizedDataCollection:]_block_invoke_2.211
+ ___block_literal_global.174
+ _objc_msgSend$_startClassifier
+ _objc_msgSend$_startLivenessWithCompletionHandler:
+ _objc_msgSend$resumeRecordingWithCompletionHandler:
+ _objc_msgSend$time
- GCC_except_table22
- GCC_except_table25
- GCC_except_table41
- GCC_except_table44
- GCC_except_table47
- GCC_except_table52
- GCC_except_table59
- ___37-[_CIDVRGBAVSessionManagerBase setup]_block_invoke.43
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke.180
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke.180.cold.1
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke.180.cold.2
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke_2
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke_3
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke_4
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke_5
- ___49-[_CIDVRGBCaptureSelfieController _startLiveness]_block_invoke_5.cold.1
- ___50-[_CIDVRGBCaptureSelfieController _finishLiveness]_block_invoke_2.197
- ___57-[_CIDVRGBCaptureSelfieController didCapturePhoto:error:]_block_invoke.144
- _objc_msgSend$_startLiveness
- _objc_msgSend$resumeRecording
CStrings:
+ "CIDVPAD.show-padframe-logging"
+ "File output set start time to %lld"
+ "Set PADFrame timestamp: %lld"
+ "_startClassifier"
+ "_startLivenessWithCompletionHandler:"
+ "resumeRecordingWithCompletionHandler:"
+ "time"

```
