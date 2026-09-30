## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4097.100.8.0.0
-  __TEXT.__text: 0x4072e8
+4097.120.3.0.0
+  __TEXT.__text: 0x409568
   __TEXT.__auth_stubs: 0x68a0
-  __TEXT.__objc_methlist: 0x2fd60
-  __TEXT.__const: 0x231e4
-  __TEXT.__gcc_except_tab: 0x30bc
-  __TEXT.__cstring: 0x1c1b5
-  __TEXT.__oslogstring: 0x16514
+  __TEXT.__objc_methlist: 0x2ff48
+  __TEXT.__const: 0x231d4
+  __TEXT.__gcc_except_tab: 0x30cc
+  __TEXT.__cstring: 0x1c405
+  __TEXT.__oslogstring: 0x16a74
   __TEXT.__dlopen_cstrs: 0x3b9
   __TEXT.__ustring: 0x8
-  __TEXT.__constg_swiftt: 0x60f8
-  __TEXT.__swift5_typeref: 0x27e12
-  __TEXT.__swift5_reflstr: 0x640a
-  __TEXT.__swift5_fieldmd: 0x5474
+  __TEXT.__constg_swiftt: 0x6100
+  __TEXT.__swift5_typeref: 0x27de0
+  __TEXT.__swift5_reflstr: 0x64ea
+  __TEXT.__swift5_fieldmd: 0x54c8
   __TEXT.__swift5_builtin: 0x438
   __TEXT.__swift5_assocty: 0x1648
   __TEXT.__swift5_proto: 0xac4

   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0xf9e0
+  __TEXT.__unwind_info: 0xf9c8
   __TEXT.__eh_frame: 0x2a80
-  __TEXT.__objc_classname: 0x61c7
-  __TEXT.__objc_methname: 0xa1767
-  __TEXT.__objc_methtype: 0x10c93
-  __TEXT.__objc_stubs: 0x5c200
-  __DATA_CONST.__got: 0x4458
-  __DATA_CONST.__const: 0x7ed8
-  __DATA_CONST.__objc_classlist: 0x1230
+  __TEXT.__objc_classname: 0x61e7
+  __TEXT.__objc_methname: 0xa1f17
+  __TEXT.__objc_methtype: 0x10d23
+  __TEXT.__objc_stubs: 0x5c5e0
+  __DATA_CONST.__got: 0x4468
+  __DATA_CONST.__const: 0x7f88
+  __DATA_CONST.__objc_classlist: 0x1238
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x7c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a080
+  __DATA_CONST.__objc_selrefs: 0x1a188
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xd98
   __DATA_CONST.__objc_arraydata: 0x1048
   __AUTH_CONST.__auth_got: 0x3460
-  __AUTH_CONST.__const: 0xe528
-  __AUTH_CONST.__cfstring: 0x16740
-  __AUTH_CONST.__objc_const: 0x50ba0
+  __AUTH_CONST.__const: 0xe588
+  __AUTH_CONST.__cfstring: 0x169a0
+  __AUTH_CONST.__objc_const: 0x51010
   __AUTH_CONST.__objc_intobj: 0x1860
   __AUTH_CONST.__objc_doubleobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0xcf0
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0x5e60
-  __AUTH.__data: 0x1048
-  __DATA.__objc_ivar: 0x3c74
-  __DATA.__data: 0xb708
-  __DATA.__bss: 0x117e0
+  __AUTH.__objc_data: 0x5eb8
+  __AUTH.__data: 0x1050
+  __DATA.__objc_ivar: 0x3cd8
+  __DATA.__data: 0xb728
+  __DATA.__bss: 0x11800
   __DATA.__common: 0x179
   __DATA_DIRTY.__objc_data: 0x78e0
-  __DATA_DIRTY.__data: 0x3488
+  __DATA_DIRTY.__data: 0x3480
   __DATA_DIRTY.__bss: 0x4340
   __DATA_DIRTY.__common: 0x128
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 030C1120-EF4E-383C-821D-53231E8A078E
-  Functions: 26327
-  Symbols:   60679
-  CStrings:  31463
+  UUID: C05F97A5-F56A-314D-BED8-54494D8D02DA
+  Functions: 26365
+  Symbols:   60850
+  CStrings:  31583
 
Symbols:
+ +[CAMApplication mainEntryTime]
+ -[CAMAnalyticsLaunchAggregator .cxx_destruct]
+ -[CAMAnalyticsLaunchAggregator _checkLaunchCompletionAndReportIfNeeded]
+ -[CAMAnalyticsLaunchAggregator _checkLaunchCompletionAndReportIfNeeded].cold.1
+ -[CAMAnalyticsLaunchAggregator _checkLaunchCompletionAndReportIfNeeded].cold.2
+ -[CAMAnalyticsLaunchAggregator _checkLaunchCompletionAndReportIfNeeded].cold.3
+ -[CAMAnalyticsLaunchAggregator _clearSessionStats]
+ -[CAMAnalyticsLaunchAggregator _reportLaunchEvent]
+ -[CAMAnalyticsLaunchAggregator _reportLaunchEvent].cold.1
+ -[CAMAnalyticsLaunchAggregator _reportLaunchEvent].cold.2
+ -[CAMAnalyticsLaunchAggregator _reportLaunchEvent].cold.3
+ -[CAMAnalyticsLaunchAggregator _reset]
+ -[CAMAnalyticsLaunchAggregator applicationDidEnterBackground]
+ -[CAMAnalyticsLaunchAggregator applicationWillEnterForeground]
+ -[CAMAnalyticsLaunchAggregator cancelLaunchTelemetry]
+ -[CAMAnalyticsLaunchAggregator didBeginGraphBuild:]
+ -[CAMAnalyticsLaunchAggregator didBeginGraphBuild:].cold.1
+ -[CAMAnalyticsLaunchAggregator didBeginGraphBuild:].cold.2
+ -[CAMAnalyticsLaunchAggregator didConfigureMode:devicePosition:]
+ -[CAMAnalyticsLaunchAggregator didDisplayFirstPreviewFrame:]
+ -[CAMAnalyticsLaunchAggregator didDisplayFirstPreviewFrame:].cold.1
+ -[CAMAnalyticsLaunchAggregator didPrewarmWithNotificationPayload:]
+ -[CAMAnalyticsLaunchAggregator didStartPreviewing:]
+ -[CAMAnalyticsLaunchAggregator didStartRunning]
+ -[CAMAnalyticsLaunchAggregator didStopRunningWithNotificationPayload:]
+ -[CAMAnalyticsLaunchAggregator interruptedForReason:]
+ -[CAMAnalyticsLaunchAggregator interruptionEnded]
+ -[CAMAnalyticsLaunchAggregator receivedSessionRuntimeError]
+ -[CAMAnalyticsLaunchAggregator viewfinderClosedDueToSession:]
+ -[CAMCaptureEngine _handleSessionDidBeginGraphBuild:]
+ -[CAMClosedViewfinderController _closedViewfinderReasonIsDueToSession:]
+ -[CAMClosedViewfinderController viewfinderClosedDueToSession]
+ -[CAMViewfinderViewController _analyticsLaunchAggregator]
+ -[CAMViewfinderViewController _didDisplayFirstPreviewFrame:]
+ -[CAMViewfinderViewController _setAnalyticsLaunchAggregator:]
+ -[CAMViewfinderViewController captureControllerDidBeginGraphBuild:withNotificationPayload:]
+ -[CAMViewfinderViewController captureControllerDidStopRunning:withNotificationPayload:]
+ -[CAMViewfinderViewController captureControllerReceivedSessionRuntimeError:]
+ -[CAMViewfinderViewController captureControllerWasInterrupted:forReason:]
+ -[CAMViewfinderViewController closedViewfinderController:didChangeViewfinderClosedDueToSession:]
+ -[CUCaptureController handleSessionDidBeginGraphBuild:]
+ -[CUCaptureController handleSessionDidStopRunningWithNotificationPayload:]
+ -[CUCaptureController handleSessionRuntimeError]
+ GCC_except_table103
+ GCC_except_table1185
+ GCC_except_table1194
+ GCC_except_table1201
+ GCC_except_table1213
+ GCC_except_table1238
+ GCC_except_table1315
+ GCC_except_table1321
+ GCC_except_table1329
+ GCC_except_table143
+ GCC_except_table1457
+ GCC_except_table156
+ GCC_except_table224
+ GCC_except_table255
+ GCC_except_table263
+ GCC_except_table270
+ GCC_except_table274
+ GCC_except_table279
+ GCC_except_table296
+ GCC_except_table328
+ GCC_except_table330
+ GCC_except_table332
+ GCC_except_table334
+ GCC_except_table338
+ GCC_except_table587
+ GCC_except_table589
+ GCC_except_table652
+ GCC_except_table817
+ GCC_except_table82
+ GCC_except_table837
+ GCC_except_table893
+ _AVCaptureSessionWasPrewarmedNotification
+ _CAMAVCaptureClientBackgroundedKey
+ _CAMAVCaptureHostTimeUsKey
+ _CAMAVCaptureMemoryStatusLevelKey
+ _CAMAVCaptureSessionDidBeginGraphBuildNotification
+ _CAMAVCaptureThermalLevelKey
+ _CAMAVCaptureVideoPreviewLayerDidDisplayFirstPreviewFrameNotification
+ _CAMAVCaptureVideoPreviewLayerDisplayedHostTimeUsKey
+ _CAMAVCaptureVideoPreviewLayerPreviewingHostTimeUsKey
+ _OBJC_CLASS_$_CAMAnalyticsLaunchAggregator
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._applicationBackgrounded
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._devicePosition
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._didDisplayFirstPreviewFrame
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._didDisplayFirstPreviewFrameHostTimeMicroseconds
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._endedViewfinderClosedDueToSessionHostTimeMicroseconds
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._firstGraphBuildHostTimeMicroseconds
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._graphBuildCount
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._graphBuildingForPrewarming
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._lastGraphBuildHostTimeMicroseconds
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._memoryStatusLevel
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._mode
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._previewStartedHostTimeMicroseconds
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._prewarmHostTimeMicroseconds
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._prewarmReason
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._prewarmedLaunch
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._runtimeErrorCount
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._sessionInterrupted
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._sessionRunning
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._thermalLevel
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._viewfinderClosedDueToSession
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._waitingForNewLaunch
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._warmLaunch
+ _OBJC_IVAR_$_CAMAnalyticsLaunchAggregator._willEnterForegroundHostTimeMicroseconds
+ _OBJC_IVAR_$_CAMClosedViewfinderController._wantsViewfinderClosedDueToSessionReasonCount
+ _OBJC_IVAR_$_CAMViewfinderViewController.__analyticsLaunchAggregator
+ _OBJC_METACLASS_$_CAMAnalyticsLaunchAggregator
+ __OBJC_$_INSTANCE_METHODS_CAMAnalyticsLaunchAggregator
+ __OBJC_$_INSTANCE_VARIABLES_CAMAnalyticsLaunchAggregator
+ __OBJC_CLASS_RO_$_CAMAnalyticsLaunchAggregator
+ __OBJC_METACLASS_RO_$_CAMAnalyticsLaunchAggregator
+ ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke.339
+ ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke_2.340
+ ___33-[CAMCaptureEngine stopRecording]_block_invoke.325
+ ___35-[CAMCaptureEngine enqueueCommand:]_block_invoke.230
+ ___39-[CAMCaptureEngine stopWithCompletion:]_block_invoke.111
+ ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.152
+ ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.153
+ ___47-[CAMCaptureEngine _handleSessionRuntimeError:]_block_invoke.127
+ ___48-[CUCaptureController handleSessionRuntimeError]_block_invoke
+ ___50-[CAMAnalyticsLaunchAggregator _reportLaunchEvent]_block_invoke
+ ___53-[CAMCaptureEngine _handleSessionDidBeginGraphBuild:]_block_invoke
+ ___55-[CUCaptureController handleSessionDidBeginGraphBuild:]_block_invoke
+ ___63-[CAMCaptureEngine _captureEngineDeviceForDeviceType:position:]_block_invoke.459
+ ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke.166
+ ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke_2.167
+ ___70-[CAMCaptureEngine captureOutput:willBeginCaptureForResolvedSettings:]_block_invoke.264
+ ___72-[CAMCaptureEngine _commitSessionConfigurationIfNecessaryWithLogReason:]_block_invoke.227
+ ___74-[CUCaptureController handleSessionDidStopRunningWithNotificationPayload:]_block_invoke
+ ___85-[CAMCaptureEngine captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]_block_invoke.331
+ ___92-[CAMCaptureEngine captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]_block_invoke.429
+ ___block_descriptor_81_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_literal_global.114
+ ___block_literal_global.129
+ ___block_literal_global.158
+ ___block_literal_global.322
+ ___block_literal_global.45
+ ___block_literal_global.462
+ ___block_literal_global.49
+ ___block_literal_global.505
+ ___block_literal_global.54
+ ___block_literal_global.59
+ ___block_literal_global.61
+ _getCurrentHostTimeMicroseconds
+ _objc_msgSend$_analyticsLaunchAggregator
+ _objc_msgSend$_checkLaunchCompletionAndReportIfNeeded
+ _objc_msgSend$_clearSessionStats
+ _objc_msgSend$_closedViewfinderReasonIsDueToSession:
+ _objc_msgSend$_reportLaunchEvent
+ _objc_msgSend$_setAnalyticsLaunchAggregator:
+ _objc_msgSend$applicationDidEnterBackground
+ _objc_msgSend$applicationWillEnterForeground
+ _objc_msgSend$cancelLaunchTelemetry
+ _objc_msgSend$captureControllerDidBeginGraphBuild:withNotificationPayload:
+ _objc_msgSend$captureControllerDidStopRunning:withNotificationPayload:
+ _objc_msgSend$captureControllerReceivedSessionRuntimeError:
+ _objc_msgSend$captureControllerWasInterrupted:forReason:
+ _objc_msgSend$closedViewfinderController:didChangeViewfinderClosedDueToSession:
+ _objc_msgSend$didBeginGraphBuild:
+ _objc_msgSend$didConfigureMode:devicePosition:
+ _objc_msgSend$didDisplayFirstPreviewFrame:
+ _objc_msgSend$didPrewarmWithNotificationPayload:
+ _objc_msgSend$didStartPreviewing:
+ _objc_msgSend$didStartRunning
+ _objc_msgSend$didStopRunningWithNotificationPayload:
+ _objc_msgSend$enableLaunchTelemetry
+ _objc_msgSend$handleSessionDidBeginGraphBuild:
+ _objc_msgSend$handleSessionDidStopRunningWithNotificationPayload:
+ _objc_msgSend$handleSessionRuntimeError
+ _objc_msgSend$interruptedForReason:
+ _objc_msgSend$interruptionEnded
+ _objc_msgSend$mainEntryTime
+ _objc_msgSend$receivedSessionRuntimeError
+ _objc_msgSend$updateAnalyticsForUserChangedSemanticStylePreset
+ _objc_msgSend$viewfinderClosedDueToSession
+ _objc_msgSend$viewfinderClosedDueToSession:
+ _sMainEntryTime
+ _symbolic _____Sg So26CAMSemanticStylePresetTypeV
- -[CAMViewfinderViewController captureControllerDidStopRunning:]
- -[CAMViewfinderViewController captureControllerWasInterrupted:]
- -[CUCaptureController handleSessionDidStopRunning]
- GCC_except_table100
- GCC_except_table1181
- GCC_except_table1190
- GCC_except_table1197
- GCC_except_table1209
- GCC_except_table1234
- GCC_except_table1311
- GCC_except_table1317
- GCC_except_table1325
- GCC_except_table140
- GCC_except_table1453
- GCC_except_table153
- GCC_except_table221
- GCC_except_table248
- GCC_except_table252
- GCC_except_table260
- GCC_except_table267
- GCC_except_table271
- GCC_except_table276
- GCC_except_table293
- GCC_except_table325
- GCC_except_table327
- GCC_except_table329
- GCC_except_table331
- GCC_except_table335
- GCC_except_table586
- GCC_except_table588
- GCC_except_table65
- GCC_except_table650
- GCC_except_table79
- GCC_except_table815
- GCC_except_table835
- GCC_except_table85
- GCC_except_table887
- GCC_except_table91
- _CAMAVCaptureSessionWasPrewarmedNotification
- ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke.333
- ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke_2.334
- ___33-[CAMCaptureEngine stopRecording]_block_invoke.319
- ___35-[CAMCaptureEngine enqueueCommand:]_block_invoke.224
- ___39-[CAMCaptureEngine stopWithCompletion:]_block_invoke.112
- ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.148
- ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.149
- ___50-[CUCaptureController handleSessionDidStopRunning]_block_invoke
- ___63-[CAMCaptureEngine _captureEngineDeviceForDeviceType:position:]_block_invoke.453
- ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke.160
- ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke_2.161
- ___70-[CAMCaptureEngine captureOutput:willBeginCaptureForResolvedSettings:]_block_invoke.258
- ___72-[CAMCaptureEngine _commitSessionConfigurationIfNecessaryWithLogReason:]_block_invoke.221
- ___85-[CAMCaptureEngine captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]_block_invoke.325
- ___92-[CAMCaptureEngine captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]_block_invoke.423
- ___block_literal_global.119
- ___block_literal_global.154
- ___block_literal_global.316
- ___block_literal_global.456
- ___block_literal_global.48
- ___block_literal_global.499
- ___block_literal_global.52
- ___block_literal_global.60
- ___block_literal_global.62
- ___block_literal_global.64
- _objc_msgSend$captureControllerWasInterrupted:
CStrings:
+ "@\"CAMAnalyticsLaunchAggregator\""
+ "AVCaptureClientBackgroundedKey"
+ "AVCaptureHostTimeUsKey"
+ "AVCaptureMemoryStatusLevelKey"
+ "AVCaptureSessionDidBeginGraphBuildNotification"
+ "AVCaptureThermalLevelKey"
+ "AVCaptureVideoPreviewLayerDidDisplayFirstPreviewFrameNotification"
+ "AVCaptureVideoPreviewLayerDisplayedHostTimeUsKey"
+ "AVCaptureVideoPreviewLayerPreviewingHostTimeUsKey"
+ "CAMAnalyticsLaunchAggregator"
+ "LaunchAnalytics: Canceling event due to change to mode:%@ devicePosition:%@"
+ "LaunchAnalytics: Canceling event due to explicit request"
+ "LaunchAnalytics: Cancelling launch telemetry due to willEnterForeground without a background notification"
+ "LaunchAnalytics: Got a didBeginGraphBuild notification with no payload. This should never happen. Discarding launch event."
+ "LaunchAnalytics: Got a didDisplayFirstPreviewFrame notification with no payload. This should never happen. Discarding launch event."
+ "LaunchAnalytics: Got a prewarmed graph build notification after a non-prewarmed graph build. This is probably a bug."
+ "LaunchAnalytics: Not clearing prewarming stats because client wasn't backgrounded on session stop."
+ "LaunchAnalytics: Preview frame was displayed at time %lld yet preview start time was later at %lld. Reporting delta as 0"
+ "LaunchAnalytics: attempted to report event with invalid lastGraphBuildHostTimeMicroseconds %lld"
+ "LaunchAnalytics: attempted to report event with invalid launchStartHostTimeMicroseconds %lld"
+ "LaunchAnalytics: attempted to report event with invalid previewStartDurationMicroseconds %lld"
+ "LaunchAnalytics: had invalid preview times didDisplayFirstPreviewFrame %lld previewStarted %lld"
+ "LaunchAnalytics: launch completed but mode was %@ with devicePosition %@. Abandoning telemetry"
+ "LaunchAnalytics: missing memory status / thermal level"
+ "T@\"CAMAnalyticsLaunchAggregator\",&,N,S_setAnalyticsLaunchAggregator:,V__analyticsLaunchAggregator"
+ "__analyticsLaunchAggregator"
+ "_analyticsLaunchAggregator"
+ "_applicationBackgrounded"
+ "_checkLaunchCompletionAndReportIfNeeded"
+ "_clearSessionStats"
+ "_closedViewfinderReasonIsDueToSession:"
+ "_didDisplayFirstPreviewFrame"
+ "_didDisplayFirstPreviewFrame:"
+ "_didDisplayFirstPreviewFrameHostTimeMicroseconds"
+ "_endedViewfinderClosedDueToSessionHostTimeMicroseconds"
+ "_firstGraphBuildHostTimeMicroseconds"
+ "_graphBuildCount"
+ "_graphBuildingForPrewarming"
+ "_handleSessionDidBeginGraphBuild:"
+ "_lastGraphBuildHostTimeMicroseconds"
+ "_memoryStatusLevel"
+ "_previewStartedHostTimeMicroseconds"
+ "_prewarmHostTimeMicroseconds"
+ "_prewarmReason"
+ "_prewarmedLaunch"
+ "_reportLaunchEvent"
+ "_runtimeErrorCount"
+ "_sessionInterrupted"
+ "_sessionRunning"
+ "_setAnalyticsLaunchAggregator:"
+ "_thermalLevel"
+ "_viewfinderClosedDueToSession"
+ "_waitingForNewLaunch"
+ "_wantsViewfinderClosedDueToSessionReasonCount"
+ "_warmLaunch"
+ "_willEnterForegroundHostTimeMicroseconds"
+ "aB"
+ "applicationDidEnterBackground"
+ "applicationWillEnterForeground"
+ "cancelLaunchTelemetry"
+ "captureControllerDidBeginGraphBuild:withNotificationPayload:"
+ "captureControllerDidStopRunning:withNotificationPayload:"
+ "captureControllerReceivedSessionRuntimeError:"
+ "captureControllerWasInterrupted:forReason:"
+ "closedViewfinderController:didChangeViewfinderClosedDueToSession:"
+ "com.apple.CameraCapture.CameraAppLaunch"
+ "didBeginGraphBuild:"
+ "didConfigureMode:devicePosition:"
+ "didDisplayFirstPreviewFrame:"
+ "didPrewarmWithNotificationPayload:"
+ "didStartPreviewing:"
+ "didStartRunning"
+ "didStopRunningWithNotificationPayload:"
+ "enableLaunchTelemetry"
+ "filter"
+ "graphBuildCount"
+ "handleSessionDidBeginGraphBuild:"
+ "handleSessionDidStopRunningWithNotificationPayload:"
+ "handleSessionRuntimeError"
+ "interruptedForReason:"
+ "interruptionEnded"
+ "isColdLaunch"
+ "isPrewarmed"
+ "lastGraphPreviewStartDuration"
+ "lastSemanticStylePreset"
+ "lastSemanticStyleSceneBias"
+ "lastSemanticStyleWarmthBias"
+ "launchMode"
+ "mainEntryTime"
+ "memoryStatusLevel"
+ "previewFrameDisplayDelay"
+ "previewStartDuration"
+ "receivedSessionRuntimeError"
+ "runningLaunchDuration"
+ "runtimeErrorCount"
+ "semanticStyleSceneBias"
+ "thermalLevel"
+ "updateAnalyticsForUserChangedSemanticStylePreset"
+ "v28@0:8@\"CAMClosedViewfinderController\"16B24"
+ "v32@0:8@\"CUCaptureController\"16@\"NSDictionary\"24"
+ "viewfinderClosedDueToSession"
+ "viewfinderClosedDueToSession:"
- "AVCaptureSessionWasPrewarmedNotification"
- "captureControllerWasInterrupted:"

```
