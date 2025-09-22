## HRTFEnrollment

> `/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment`

```diff

-24.0.0.0.0
-  __TEXT.__text: 0x9164
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__init_offsets: 0x4
+31.5.2.1.2
+  __TEXT.__text: 0x9464
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_methlist: 0x8d8
   __TEXT.__const: 0xd4
-  __TEXT.__cstring: 0x939
-  __TEXT.__oslogstring: 0x4fb
+  __TEXT.__cstring: 0x971
+  __TEXT.__oslogstring: 0x4e7
   __TEXT.__gcc_except_tab: 0x390
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__unwind_info: 0x330
   __TEXT.__objc_classname: 0x21d
   __TEXT.__objc_methname: 0x2000
   __TEXT.__objc_methtype: 0xacc

   __DATA_CONST.__objc_selrefs: 0x828
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0xb40
   __AUTH_CONST.__objc_const: 0x1ea8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x3a8
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__common: 0x8
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31E9D171-ED97-3221-B8DA-5252FF8176CD
-  Functions: 193
-  Symbols:   1057
+  UUID: 13B7F272-C5BB-3A33-84CA-9C73DD61AF32
+  Functions: 178
+  Symbols:   1103
   CStrings:  751
 
Symbols:
+ -[HRTFEnrollmentSession _verifyCaptureDevice:].cold.3
+ -[HRTFEnrollmentSession _verifyCaptureDevice:].cold.4
+ -[HRTFEnrollmentSession stopSession:].cold.1
+ -[HRTFEnrollmentSession updateResultSize:].cold.1
+ -[HRTFSyncedCaptureSource _handleCaptureSessionNotification:].cold.1
+ -[HRTFSyncedCaptureSource _verifyCaptureDevice:].cold.3
+ -[HRTFSyncedCaptureSource _verifyCaptureDevice:].cold.4
+ -[HRTFSyncedCaptureSource startCaptureSession].cold.1
+ -[HRTFSyncedCaptureSource stopCaptureSession].cold.1
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table26
+ GCC_except_table33
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table49
+ _HRTFLogObjectForCategory_HRTFEnrollmentSession
+ _HRTFLogObjectForCategory_HRTFEnrollmentSession.cold.1
+ _HRTFLogObjectForCategory_HRTFSerializableCaptureData
+ _HRTFLogObjectForCategory_HRTFSerializableCaptureData.cold.1
+ _HRTFLogObjectForCategory_HRTFSyncedCaptureSource
+ _HRTFLogObjectForCategory_HRTFSyncedCaptureSource.cold.1
+ ___37-[HRTFEnrollmentSession pauseSession]_block_invoke.cold.1
+ ___37-[HRTFEnrollmentSession stopSession:]_block_invoke_2.cold.1
+ ___38-[HRTFEnrollmentSession resumeSession]_block_invoke.cold.1
+ ___43-[HRTFEnrollmentSession startSession:then:]_block_invoke.180.cold.1
+ ___43-[HRTFEnrollmentSession startSession:then:]_block_invoke.183.cold.1
+ ___46-[HRTFEnrollmentSession sessionStarted:error:]_block_invoke.cold.2
+ ___46-[HRTFEnrollmentSession sessionStarted:error:]_block_invoke.cold.3
+ ___57-[HRTFEnrollmentSession didStartCaptureSessionWithError:]_block_invoke.cold.1
+ ___57-[HRTFEnrollmentSession didStartCaptureSessionWithError:]_block_invoke.cold.2
+ ___58-[HRTFEnrollmentSession downloadHRTFAsset:withCompletion:]_block_invoke_2.202.cold.1
+ ___60-[HRTFEnrollmentSession downloadHRTFAssetV2:withCompletion:]_block_invoke_2.193.cold.1
+ ___HRTFLogObjectForCategory_HRTFEnrollmentSession_block_invoke
+ ___HRTFLogObjectForCategory_HRTFSerializableCaptureData_block_invoke
+ ___HRTFLogObjectForCategory_HRTFSyncedCaptureSource_block_invoke
+ ___block_literal_global.297
+ ___chkstk_darwin
+ _logObjHRTFEnrollmentSession
+ _logObjHRTFSerializableCaptureData
+ _logObjHRTFSyncedCaptureSource
+ _objc_retainAutoreleaseReturnValue
+ _onceTokenHRTFEnrollmentSession
+ _onceTokenHRTFSerializableCaptureData
+ _onceTokenHRTFSyncedCaptureSource
- -[HRTFEnrollmentSession didReceiveVideoData:colorData:depthData:faceObject:].cold.6
- -[HRTFSyncedCaptureSource _initialize].cold.5
- -[_SerializableCVPixelBuffer initWithCoder:].cold.1
- -[_SerializableCVPixelBuffer initWithCoder:].cold.2
- GCC_except_table12
- GCC_except_table16
- GCC_except_table24
- GCC_except_table31
- GCC_except_table38
- GCC_except_table42
- GCC_except_table48
- _HRTFEnrollmentLog
- _HRTFEnrollmentLogInit
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- ___initLogging
- __os_log_debug_impl
- __os_log_error_impl
- __os_log_fault_impl
CStrings:
- "Framework"
- "Service"
- "logging initialized"

```
