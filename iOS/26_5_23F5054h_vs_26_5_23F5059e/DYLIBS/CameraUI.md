## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4097.120.3.0.0
-  __TEXT.__text: 0x409568
+4097.120.4.0.0
+  __TEXT.__text: 0x4095f0
   __TEXT.__auth_stubs: 0x68a0
-  __TEXT.__objc_methlist: 0x2ff48
+  __TEXT.__objc_methlist: 0x2fed8
   __TEXT.__const: 0x231d4
-  __TEXT.__gcc_except_tab: 0x30cc
-  __TEXT.__cstring: 0x1c405
-  __TEXT.__oslogstring: 0x16a74
+  __TEXT.__gcc_except_tab: 0x30d8
+  __TEXT.__cstring: 0x1c425
+  __TEXT.__oslogstring: 0x16a94
   __TEXT.__dlopen_cstrs: 0x3b9
   __TEXT.__ustring: 0x8
   __TEXT.__constg_swiftt: 0x6100

   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0xf9c8
+  __TEXT.__unwind_info: 0xf9c0
   __TEXT.__eh_frame: 0x2a80
   __TEXT.__objc_classname: 0x61e7
-  __TEXT.__objc_methname: 0xa1f17
-  __TEXT.__objc_methtype: 0x10d23
-  __TEXT.__objc_stubs: 0x5c5e0
+  __TEXT.__objc_methname: 0xa1df7
+  __TEXT.__objc_methtype: 0x10cd3
+  __TEXT.__objc_stubs: 0x5c520
   __DATA_CONST.__got: 0x4468
   __DATA_CONST.__const: 0x7f88
   __DATA_CONST.__objc_classlist: 0x1238
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x7c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a188
+  __DATA_CONST.__objc_selrefs: 0x1a160
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xd98
   __DATA_CONST.__objc_arraydata: 0x1048
   __AUTH_CONST.__auth_got: 0x3460
-  __AUTH_CONST.__const: 0xe588
-  __AUTH_CONST.__cfstring: 0x169a0
-  __AUTH_CONST.__objc_const: 0x51010
+  __AUTH_CONST.__const: 0xe608
+  __AUTH_CONST.__cfstring: 0x169c0
+  __AUTH_CONST.__objc_const: 0x51000
   __AUTH_CONST.__objc_intobj: 0x1860
   __AUTH_CONST.__objc_doubleobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0x258

   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x5eb8
   __AUTH.__data: 0x1050
-  __DATA.__objc_ivar: 0x3cd8
+  __DATA.__objc_ivar: 0x3cdc
   __DATA.__data: 0xb728
   __DATA.__bss: 0x11800
   __DATA.__common: 0x179
   __DATA_DIRTY.__objc_data: 0x78e0
   __DATA_DIRTY.__data: 0x3480
-  __DATA_DIRTY.__bss: 0x4340
+  __DATA_DIRTY.__bss: 0x4350
   __DATA_DIRTY.__common: 0x128
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C05F97A5-F56A-314D-BED8-54494D8D02DA
-  Functions: 26365
-  Symbols:   60850
-  CStrings:  31583
+  UUID: 0EF05C39-0148-37B4-83E4-FF9D81C67073
+  Functions: 26367
+  Symbols:   60856
+  CStrings:  31578
 
Symbols:
+ +[CAMAnalyticsLaunchAggregator sharedInstance]
+ +[CAMAnalyticsLaunchAggregator sharedInstance].cold.1
+ -[CAMCaptureCapabilities shouldEnableLaunchTelemetry]
+ -[CAMCaptureEngine _handleSessionWasPrewarmedAccidentalLaunchCheck:]
+ -[CAMCaptureEngine _handleSessionWasPrewarmedAccidentalLaunchCheck:].cold.1
+ -[CAMCaptureEngine _handleSessionWasPrewarmedAccidentalLaunchCheck:].cold.2
+ -[CAMViewfinderViewController captureControllerDidStopRunning:]
+ GCC_except_table100
+ GCC_except_table1183
+ GCC_except_table1192
+ GCC_except_table1199
+ GCC_except_table1211
+ GCC_except_table1236
+ GCC_except_table1313
+ GCC_except_table1319
+ GCC_except_table1327
+ GCC_except_table1455
+ GCC_except_table149
+ GCC_except_table162
+ GCC_except_table230
+ GCC_except_table257
+ GCC_except_table261
+ GCC_except_table269
+ GCC_except_table276
+ GCC_except_table280
+ GCC_except_table285
+ GCC_except_table302
+ GCC_except_table336
+ GCC_except_table340
+ GCC_except_table344
+ GCC_except_table72
+ GCC_except_table92
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._hasConfiguredMode
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._modeOrDevicePositionChangeCount
+ __OBJC_$_CLASS_METHODS_CAMAnalyticsLaunchAggregator
+ ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke.341
+ ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke_2.342
+ ___33-[CAMCaptureEngine stopRecording]_block_invoke.327
+ ___35-[CAMCaptureEngine enqueueCommand:]_block_invoke.232
+ ___46+[CAMAnalyticsLaunchAggregator sharedInstance]_block_invoke
+ ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.154
+ ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke_2
+ ___47-[CAMCaptureEngine _handleSessionRuntimeError:]_block_invoke.130
+ ___47-[CAMCaptureEngine _handleSessionWasPrewarmed:]_block_invoke
+ ___49-[CAMCaptureEngine _handleSessionDidStopRunning:]_block_invoke_3
+ ___50-[CAMCaptureEngine _handleSessionDidStartRunning:]_block_invoke_3
+ ___52-[CAMCaptureEngine _handleSessionInterruptionEnded:]_block_invoke_2
+ ___63-[CAMCaptureEngine _captureEngineDeviceForDeviceType:position:]_block_invoke.460
+ ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke.168
+ ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke_2.169
+ ___70-[CAMCaptureEngine captureOutput:willBeginCaptureForResolvedSettings:]_block_invoke.266
+ ___72-[CAMCaptureEngine _commitSessionConfigurationIfNecessaryWithLogReason:]_block_invoke.229
+ ___85-[CAMCaptureEngine captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]_block_invoke.333
+ ___92-[CAMCaptureEngine captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]_block_invoke.431
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.132
+ ___block_literal_global.160
+ ___block_literal_global.164
+ ___block_literal_global.324
+ ___block_literal_global.463
+ ___block_literal_global.506
+ _objc_msgSend$_handleSessionWasPrewarmedAccidentalLaunchCheck:
+ _objc_msgSend$shouldEnableLaunchTelemetry
- -[CAMCaptureEngine _handleSessionWasPrewarmed:].cold.1
- -[CAMCaptureEngine _handleSessionWasPrewarmed:].cold.2
- -[CAMViewfinderViewController _analyticsLaunchAggregator]
- -[CAMViewfinderViewController _setAnalyticsLaunchAggregator:]
- -[CAMViewfinderViewController captureControllerDidBeginGraphBuild:withNotificationPayload:]
- -[CAMViewfinderViewController captureControllerDidStopRunning:withNotificationPayload:]
- -[CAMViewfinderViewController captureControllerReceivedSessionRuntimeError:]
- -[CUCaptureController handleSessionDidBeginGraphBuild:]
- -[CUCaptureController handleSessionRuntimeError]
- GCC_except_table103
- GCC_except_table1185
- GCC_except_table1194
- GCC_except_table1201
- GCC_except_table1213
- GCC_except_table1238
- GCC_except_table1315
- GCC_except_table1321
- GCC_except_table1329
- GCC_except_table143
- GCC_except_table1457
- GCC_except_table156
- GCC_except_table224
- GCC_except_table255
- GCC_except_table263
- GCC_except_table270
- GCC_except_table274
- GCC_except_table279
- GCC_except_table296
- GCC_except_table328
- GCC_except_table330
- GCC_except_table332
- GCC_except_table82
- _OBJC_IVAR_$_CAMViewfinderViewController.__analyticsLaunchAggregator
- ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke.339
- ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke_2.340
- ___33-[CAMCaptureEngine stopRecording]_block_invoke.325
- ___35-[CAMCaptureEngine enqueueCommand:]_block_invoke.230
- ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.152
- ___47-[CAMCaptureEngine _handleSessionRuntimeError:]_block_invoke.127
- ___48-[CUCaptureController handleSessionRuntimeError]_block_invoke
- ___55-[CUCaptureController handleSessionDidBeginGraphBuild:]_block_invoke
- ___63-[CAMCaptureEngine _captureEngineDeviceForDeviceType:position:]_block_invoke.459
- ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke.166
- ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke_2.167
- ___70-[CAMCaptureEngine captureOutput:willBeginCaptureForResolvedSettings:]_block_invoke.264
- ___72-[CAMCaptureEngine _commitSessionConfigurationIfNecessaryWithLogReason:]_block_invoke.227
- ___85-[CAMCaptureEngine captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]_block_invoke.331
- ___92-[CAMCaptureEngine captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]_block_invoke.429
- ___block_literal_global.129
- ___block_literal_global.158
- ___block_literal_global.322
- ___block_literal_global.462
- ___block_literal_global.505
- _objc_msgSend$_analyticsLaunchAggregator
- _objc_msgSend$_setAnalyticsLaunchAggregator:
- _objc_msgSend$captureControllerDidBeginGraphBuild:withNotificationPayload:
- _objc_msgSend$captureControllerDidStopRunning:withNotificationPayload:
- _objc_msgSend$captureControllerReceivedSessionRuntimeError:
- _objc_msgSend$handleSessionDidBeginGraphBuild:
- _objc_msgSend$handleSessionDidStopRunningWithNotificationPayload:
- _objc_msgSend$handleSessionRuntimeError
CStrings:
+ "LaunchAnalytics: Preview start time %lld in DidDisplayFirstPreviewFrame differed from the existing value %lld. Updating to new value"
+ "_handleSessionWasPrewarmedAccidentalLaunchCheck:"
+ "_hasConfiguredMode"
+ "_modeOrDevicePositionChangeCount"
+ "modeOrDevicePositionChangeCount"
+ "qB"
+ "shouldEnableLaunchTelemetry"
- "@\"CAMAnalyticsLaunchAggregator\""
- "LaunchAnalytics: Cancelling launch telemetry due to willEnterForeground without a background notification"
- "T@\"CAMAnalyticsLaunchAggregator\",&,N,S_setAnalyticsLaunchAggregator:,V__analyticsLaunchAggregator"
- "__analyticsLaunchAggregator"
- "_analyticsLaunchAggregator"
- "_setAnalyticsLaunchAggregator:"
- "aB"
- "captureControllerDidBeginGraphBuild:withNotificationPayload:"
- "captureControllerDidStopRunning:withNotificationPayload:"
- "captureControllerReceivedSessionRuntimeError:"
- "handleSessionDidBeginGraphBuild:"
- "handleSessionRuntimeError"
- "v32@0:8@\"CUCaptureController\"16@\"NSDictionary\"24"

```
