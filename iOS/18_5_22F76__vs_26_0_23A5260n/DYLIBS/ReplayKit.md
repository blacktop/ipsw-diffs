## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-620.2.1.0.0
-  __TEXT.__text: 0x2402c
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_methlist: 0x2480
-  __TEXT.__const: 0xe0
-  __TEXT.__oslogstring: 0x3368
-  __TEXT.__cstring: 0x4095
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__unwind_info: 0x7f0
-  __TEXT.__objc_classname: 0x630
-  __TEXT.__objc_methname: 0x680a
-  __TEXT.__objc_methtype: 0x1789
-  __TEXT.__objc_stubs: 0x47c0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__objc_classlist: 0x100
+650.38.1.0.0
+  __TEXT.__text: 0x2f08c
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_methlist: 0x2b50
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__oslogstring: 0x4733
+  __TEXT.__cstring: 0x58ef
+  __TEXT.__unwind_info: 0x988
+  __TEXT.__objc_classname: 0x6d9
+  __TEXT.__objc_methname: 0x7ca0
+  __TEXT.__objc_methtype: 0x1adb
+  __TEXT.__objc_stubs: 0x54c0
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__const: 0x9b0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1898
+  __DATA_CONST.__objc_selrefs: 0x1cd8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x4d8
-  __AUTH_CONST.__const: 0x898
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x4f68
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__const: 0x9f8
+  __AUTH_CONST.__cfstring: 0x1700
+  __AUTH_CONST.__objc_const: 0x5c80
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x9c8
-  __DATA.__bss: 0x108
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x28c
+  __DATA.__data: 0xb48
+  __DATA.__bss: 0x118
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AVConference.framework/AVConference
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/Pegasus.framework/Pegasus

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47E56F85-37F2-3E62-A0E8-494898E9F88A
-  Functions: 920
-  Symbols:   3462
-  CStrings:  2040
+  UUID: 1E0AE7D0-042C-36AC-A160-587FF573C246
+  Functions: 1129
+  Symbols:   4113
+  CStrings:  2511
 
Symbols:
+ +[RPAppAudioCaptureManager descriptionForHQLR]
+ +[RPControlCenterClient getSystemBroadcastExtensionInfo:]
+ +[RPControlCenterClient sharedInstance]
+ +[RPControlCenterClient sharedInstance].cold.1
+ +[RPScreenRecorder validateHQLRSessionInfo:]
+ -[RPAppAudioCaptureManager newAudioTapForAudioCaptureConfig:].cold.5
+ -[RPBackgroundActivity .cxx_destruct]
+ -[RPBackgroundActivity activateWithUserInteractionHandler:]
+ -[RPBackgroundActivity backgroundActivityIdentifier]
+ -[RPBackgroundActivity currentAttribution]
+ -[RPBackgroundActivity deactivate]
+ -[RPBackgroundActivity initWithBackgroundActivityIdentifier:]
+ -[RPBackgroundActivity isBackgroundActivityActive]
+ -[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]
+ -[RPBackgroundActivity publisher]
+ -[RPBackgroundActivity setCurrentAttribution:]
+ -[RPBackgroundActivity setPublisher:]
+ -[RPControlCenterAngelProxy requestToCancelReadyToRecord]
+ -[RPControlCenterAngelProxy startReadyToRecord]
+ -[RPControlCenterAngelProxy startRecordingCountdownWithSessionType:]
+ -[RPControlCenterAngelProxy stopReadyToRecord]
+ -[RPControlCenterClient .cxx_destruct]
+ -[RPControlCenterClient addDegate:]
+ -[RPControlCenterClient broadcastController:didFinishWithError:]
+ -[RPControlCenterClient broadcastController:didUpdateBroadcastURL:]
+ -[RPControlCenterClient broadcastController:didUpdateServiceInfo:]
+ -[RPControlCenterClient broadcastMode]
+ -[RPControlCenterClient callDelegate:]
+ -[RPControlCenterClient cameraOn]
+ -[RPControlCenterClient cancelReadyToRecord]
+ -[RPControlCenterClient cancelRecordingCountdown]
+ -[RPControlCenterClient countdownInterruptWithStatus:]
+ -[RPControlCenterClient currentAppUsingCamera]
+ -[RPControlCenterClient currentTimerString]
+ -[RPControlCenterClient dealloc]
+ -[RPControlCenterClient endReadyToRecord]
+ -[RPControlCenterClient extensionBundleID]
+ -[RPControlCenterClient extensionWithBundleIDExists:handler:]
+ -[RPControlCenterClient fetchIsCallActive]
+ -[RPControlCenterClient getSessionType]
+ -[RPControlCenterClient getSystemBroadcastPickerInfo]
+ -[RPControlCenterClient highQualityLocalRecordingOn]
+ -[RPControlCenterClient highQualityLocalRecordingReady]
+ -[RPControlCenterClient hqlrContentModuleContext]
+ -[RPControlCenterClient hqlrCountdownStarted]
+ -[RPControlCenterClient imageForBundleID:extensionInfo:]
+ -[RPControlCenterClient initAndFetchAVSystemControllerState]
+ -[RPControlCenterClient init]
+ -[RPControlCenterClient isAvailableAndInitialized]
+ -[RPControlCenterClient isClientRecordingTypeHQLR]
+ -[RPControlCenterClient isClientRecordingTypeSystemRecording]
+ -[RPControlCenterClient isCountingDown]
+ -[RPControlCenterClient isInitialized]
+ -[RPControlCenterClient isScreenRecorderAvailable]
+ -[RPControlCenterClient loadAvailableExtensionsWithHandler:]
+ -[RPControlCenterClient lockUIControls]
+ -[RPControlCenterClient microphoneOn]
+ -[RPControlCenterClient mixedRealityCameraOn]
+ -[RPControlCenterClient notifyClientDelegatesStart:]
+ -[RPControlCenterClient notifyClientDelegatesStart:withRecordingType:]
+ -[RPControlCenterClient preferredExtension]
+ -[RPControlCenterClient recordingOn]
+ -[RPControlCenterClient recordingTimerDidUpdate:]
+ -[RPControlCenterClient recordingType]
+ -[RPControlCenterClient removeDelegate:]
+ -[RPControlCenterClient replayKitAngelDisconnected]
+ -[RPControlCenterClient requestToCancelReadyToRecord]
+ -[RPControlCenterClient resetBroadcastPickerPreferredExt]
+ -[RPControlCenterClient screenRecorder:didStopRecordingWithPreviewViewController:error:]
+ -[RPControlCenterClient screenRecorderDidChangeAvailability:]
+ -[RPControlCenterClient screenRecorderDidUpdateState:]
+ -[RPControlCenterClient screenRecordingSupportedOnDevice]
+ -[RPControlCenterClient setBroadcastMode:]
+ -[RPControlCenterClient setCameraOn:]
+ -[RPControlCenterClient setCountdown:]
+ -[RPControlCenterClient setCurrentTimerString:]
+ -[RPControlCenterClient setExtensionBundleID:]
+ -[RPControlCenterClient setHighQualityLocalRecordingOn:]
+ -[RPControlCenterClient setHighQualityLocalRecordingReady:]
+ -[RPControlCenterClient setHqlrContentModuleContext:]
+ -[RPControlCenterClient setHqlrCountdownStarted:]
+ -[RPControlCenterClient setMicrophoneOn:]
+ -[RPControlCenterClient setMixedRealityCameraOn:]
+ -[RPControlCenterClient setPreferredExtension:]
+ -[RPControlCenterClient setRecordingType:]
+ -[RPControlCenterClient setSystemCountdownStarted:]
+ -[RPControlCenterClient setUpFrontBoardServices]
+ -[RPControlCenterClient shouldShowMicButton]
+ -[RPControlCenterClient showRecordingBanner]
+ -[RPControlCenterClient startBroadcastWithBroadcastController:handler:]
+ -[RPControlCenterClient startBroadcastWithExtensionBundleID:handler:]
+ -[RPControlCenterClient startBroadcastWithHandler:]
+ -[RPControlCenterClient startHQLRReadyToRecord:]
+ -[RPControlCenterClient startHQLRWithHandler:]
+ -[RPControlCenterClient startObservingCallIsActiveState]
+ -[RPControlCenterClient startReadyToRecordBanner]
+ -[RPControlCenterClient startRecordingCountdown]
+ -[RPControlCenterClient startRecordingWithHandler:]
+ -[RPControlCenterClient stopCurrentSession:]
+ -[RPControlCenterClient stopCurrentSession]
+ -[RPControlCenterClient stopHQLRRecordingWithHandler:]
+ -[RPControlCenterClient stopObservingCallIsActiveState]
+ -[RPControlCenterClient stopReadyToRecordBanner]
+ -[RPControlCenterClient stopRecordingCalled]
+ -[RPControlCenterClient stopSystemRecordingWithHandler:]
+ -[RPControlCenterClient systemCountdownStarted]
+ -[RPControlCenterClient terminateAngelRecordingSession]
+ -[RPControlCenterClient updateCallActive:]
+ -[RPControlCenterClient updateClientState]
+ -[RPControlCenterClient updateStatusIsCountingDown:IsRecording:]
+ -[RPDaemonProxy resumeHQLRWithCompletionHandler:]
+ -[RPDaemonProxy startHQLRWithSessionInfo:windowSize:handler:]
+ -[RPDaemonProxy startHQLRWithSessionInfo:windowSize:handler:].cold.1
+ -[RPDaemonProxy startHQLRWithSessionInfo:windowSize:handler:].cold.2
+ -[RPDaemonProxy startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:listenerEndpoint:withHandler:]
+ -[RPDaemonProxy startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:withHandler:]
+ -[RPDaemonProxy stopHQLRWithHandler:]
+ -[RPFeatureFlagUtility highQualityLocalRecordingEnabled]
+ -[RPFeatureFlagUtility recordingSDRToneMapping]
+ -[RPFeatureFlagUtility replayKitSDRToneMapping]
+ -[RPFeatureFlagUtility replayKitScreenRecordingHDR]
+ -[RPFeatureFlagUtility screenRecordingPassthroughCamera]
+ -[RPFeatureFlagUtility solariumEnabled]
+ -[RPFeatureFlagUtility toneMappedSDREnabled]
+ -[RPFeatureFlagUtility windowServerScreenshots]
+ -[RPScreenRecorder isMixedRealityCameraEnabled]
+ -[RPScreenRecorder resumeHQLR]
+ -[RPScreenRecorder setMixedRealityCameraEnabled:]
+ -[RPScreenRecorder startHQLRWithSessionInfo:handler:]
+ -[RPScreenRecorder startHQLRWithSessionInfo:handler:].cold.1
+ -[RPScreenRecorder startHQLRWithSessionInfo:handler:].cold.2
+ -[RPScreenRecorder stopHQLR:]
+ -[RPScreenRecorder stopHQLR:].cold.1
+ GCC_except_table3
+ _AVSystemController_CallIsActive
+ _AVSystemController_CallIsActiveDidChangeNotification
+ _AVSystemController_CallIsActiveNotificationParameter
+ _AVSystemController_SubscribeToNotificationsAttribute
+ _BSAuditTokenForCurrentProcess
+ _CFPreferencesGetAppBooleanValue
+ _CMClockGetHostTimeClock
+ _CMClockGetTime
+ _CMSampleBufferGetImageBuffer
+ _CVPixelBufferCreate
+ _CVPixelBufferGetBaseAddress
+ _CVPixelBufferGetBytesPerRow
+ _CVPixelBufferGetIOSurface
+ _CVPixelBufferLockBaseAddress
+ _CVPixelBufferUnlockBaseAddress
+ _IOSurfaceCopyValue
+ _OBJC_CLASS_$_AVSystemController
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitor
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_RPBackgroundActivity
+ _OBJC_CLASS_$_RPControlCenterClient
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STBackgroundActivitiesStatusDomainBackgroundActivityAttribution
+ _OBJC_CLASS_$_STBackgroundActivitiesStatusDomainPublisher
+ _OBJC_IVAR_$_RPAppAudioCaptureManager._hqlrBasicDescription
+ _OBJC_IVAR_$_RPAppAudioCaptureManager._hqlrCapture
+ _OBJC_IVAR_$_RPBackgroundActivity._backgroundActivityActive
+ _OBJC_IVAR_$_RPBackgroundActivity._backgroundActivityIdentifier
+ _OBJC_IVAR_$_RPBackgroundActivity._currentAttribution
+ _OBJC_IVAR_$_RPBackgroundActivity._publisher
+ _OBJC_IVAR_$_RPControlCenterClient._availableExtensions
+ _OBJC_IVAR_$_RPControlCenterClient._broadcastController
+ _OBJC_IVAR_$_RPControlCenterClient._broadcastMode
+ _OBJC_IVAR_$_RPControlCenterClient._cameraDeviceID
+ _OBJC_IVAR_$_RPControlCenterClient._cameraOn
+ _OBJC_IVAR_$_RPControlCenterClient._countdownPaused
+ _OBJC_IVAR_$_RPControlCenterClient._countdownState
+ _OBJC_IVAR_$_RPControlCenterClient._currentTimerString
+ _OBJC_IVAR_$_RPControlCenterClient._delegates
+ _OBJC_IVAR_$_RPControlCenterClient._extensionBundleID
+ _OBJC_IVAR_$_RPControlCenterClient._extensionCacheTime
+ _OBJC_IVAR_$_RPControlCenterClient._fetchQueue
+ _OBJC_IVAR_$_RPControlCenterClient._highQualityLocalRecordingOn
+ _OBJC_IVAR_$_RPControlCenterClient._highQualityLocalRecordingReady
+ _OBJC_IVAR_$_RPControlCenterClient._hqlrContentModuleContext
+ _OBJC_IVAR_$_RPControlCenterClient._hqlrCountdownStarted
+ _OBJC_IVAR_$_RPControlCenterClient._iconImageCache
+ _OBJC_IVAR_$_RPControlCenterClient._isCallActive
+ _OBJC_IVAR_$_RPControlCenterClient._isCountingDown
+ _OBJC_IVAR_$_RPControlCenterClient._isInitialized
+ _OBJC_IVAR_$_RPControlCenterClient._layoutMonitor
+ _OBJC_IVAR_$_RPControlCenterClient._lockUIControls
+ _OBJC_IVAR_$_RPControlCenterClient._microphoneDeviceID
+ _OBJC_IVAR_$_RPControlCenterClient._microphoneOn
+ _OBJC_IVAR_$_RPControlCenterClient._mixedRealityCameraOn
+ _OBJC_IVAR_$_RPControlCenterClient._pickerInfoCacheTime
+ _OBJC_IVAR_$_RPControlCenterClient._preferredExtension
+ _OBJC_IVAR_$_RPControlCenterClient._readyToRecordBackgroundActivity
+ _OBJC_IVAR_$_RPControlCenterClient._readyToRecordTimer
+ _OBJC_IVAR_$_RPControlCenterClient._recordingOn
+ _OBJC_IVAR_$_RPControlCenterClient._recordingType
+ _OBJC_IVAR_$_RPControlCenterClient._screenRecorder
+ _OBJC_IVAR_$_RPControlCenterClient._shouldShowMicButton
+ _OBJC_IVAR_$_RPControlCenterClient._systemController
+ _OBJC_IVAR_$_RPControlCenterClient._systemCountdownStarted
+ _OBJC_IVAR_$_RPFeatureFlagUtility._highQualityLocalRecordingEnabled
+ _OBJC_IVAR_$_RPFeatureFlagUtility._recordingSDRToneMapping
+ _OBJC_IVAR_$_RPFeatureFlagUtility._replayKitSDRToneMapping
+ _OBJC_IVAR_$_RPFeatureFlagUtility._replayKitScreenRecordingHDR
+ _OBJC_IVAR_$_RPFeatureFlagUtility._screenRecordingPassthroughCamera
+ _OBJC_IVAR_$_RPFeatureFlagUtility._solariumEnabled
+ _OBJC_IVAR_$_RPFeatureFlagUtility._windowServerScreenshots
+ _OBJC_IVAR_$_RPScreenRecorder._mixedRealityCameraEnabled
+ _OBJC_METACLASS_$_RPBackgroundActivity
+ _OBJC_METACLASS_$_RPControlCenterClient
+ _RPSampleBufferUtilities_CreateBlankPixelBuffer
+ _RPSampleBufferUtilities_CreateBlankPixelBuffer.cold.1
+ _RPSampleBufferUtilities_getContentHeadroom
+ __OBJC_$_CLASS_METHODS_RPControlCenterClient
+ __OBJC_$_INSTANCE_METHODS_RPBackgroundActivity
+ __OBJC_$_INSTANCE_METHODS_RPControlCenterClient
+ __OBJC_$_INSTANCE_VARIABLES_RPBackgroundActivity
+ __OBJC_$_INSTANCE_VARIABLES_RPControlCenterClient
+ __OBJC_$_PROP_LIST_RPBackgroundActivity
+ __OBJC_$_PROP_LIST_RPControlCenterClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_RPBroadcastControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_RPScreenRecorderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RPControlCenterAngelProxyDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RPScreenRecorderPrivateDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPBroadcastControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPControlCenterAngelProxyDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPScreenRecorderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPScreenRecorderPrivateDelegate
+ __OBJC_$_PROTOCOL_REFS_RPBroadcastControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_RPScreenRecorderDelegate
+ __OBJC_CLASS_PROTOCOLS_$_RPControlCenterClient
+ __OBJC_CLASS_RO_$_RPBackgroundActivity
+ __OBJC_CLASS_RO_$_RPControlCenterClient
+ __OBJC_LABEL_PROTOCOL_$_RPBroadcastControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_RPControlCenterAngelProxyDelegate
+ __OBJC_LABEL_PROTOCOL_$_RPScreenRecorderDelegate
+ __OBJC_LABEL_PROTOCOL_$_RPScreenRecorderPrivateDelegate
+ __OBJC_METACLASS_RO_$_RPBackgroundActivity
+ __OBJC_METACLASS_RO_$_RPControlCenterClient
+ __OBJC_PROTOCOL_$_RPBroadcastControllerDelegate
+ __OBJC_PROTOCOL_$_RPControlCenterAngelProxyDelegate
+ __OBJC_PROTOCOL_$_RPScreenRecorderDelegate
+ __OBJC_PROTOCOL_$_RPScreenRecorderPrivateDelegate
+ ___132-[RPDaemonProxy startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:withHandler:]_block_invoke
+ ___132-[RPDaemonProxy startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:withHandler:]_block_invoke.cold.1
+ ___149-[RPDaemonProxy startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:listenerEndpoint:withHandler:]_block_invoke
+ ___149-[RPDaemonProxy startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:listenerEndpoint:withHandler:]_block_invoke.cold.1
+ ___21-[RPDaemonProxy init]_block_invoke.150
+ ___29-[RPScreenRecorder stopHQLR:]_block_invoke
+ ___30-[RPScreenRecorder resumeHQLR]_block_invoke
+ ___30-[RPScreenRecorder resumeHQLR]_block_invoke.cold.1
+ ___37-[RPDaemonProxy stopHQLRWithHandler:]_block_invoke
+ ___37-[RPDaemonProxy stopHQLRWithHandler:]_block_invoke.cold.1
+ ___38-[RPControlCenterClient callDelegate:]_block_invoke
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke.88
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke.91
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke_2
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke_3
+ ___39+[RPControlCenterClient sharedInstance]_block_invoke
+ ___41-[RPControlCenterClient endReadyToRecord]_block_invoke
+ ___42-[RPControlCenterClient fetchIsCallActive]_block_invoke
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke.102
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke.103
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke.cold.1
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke_2
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke_3
+ ___42-[RPControlCenterClient updateClientState]_block_invoke
+ ___42-[RPControlCenterClient updateClientState]_block_invoke.76
+ ___42-[RPControlCenterClient updateClientState]_block_invoke_2
+ ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke.90
+ ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke.97
+ ___44-[RPControlCenterClient cancelReadyToRecord]_block_invoke
+ ___44-[RPControlCenterClient stopCurrentSession:]_block_invoke
+ ___44-[RPControlCenterClient stopCurrentSession:]_block_invoke.58
+ ___44-[RPControlCenterClient stopCurrentSession:]_block_invoke_2
+ ___46-[RPControlCenterClient startHQLRWithHandler:]_block_invoke
+ ___46-[RPControlCenterClient startHQLRWithHandler:]_block_invoke.57
+ ___46-[RPControlCenterClient startHQLRWithHandler:]_block_invoke_2
+ ___48-[RPControlCenterClient setUpFrontBoardServices]_block_invoke
+ ___48-[RPControlCenterClient setUpFrontBoardServices]_block_invoke.25
+ ___48-[RPControlCenterClient startHQLRReadyToRecord:]_block_invoke
+ ___49-[RPControlCenterClient recordingTimerDidUpdate:]_block_invoke
+ ___49-[RPControlCenterClient startReadyToRecordBanner]_block_invoke
+ ___49-[RPControlCenterClient startReadyToRecordBanner]_block_invoke_2
+ ___49-[RPDaemonProxy resumeHQLRWithCompletionHandler:]_block_invoke
+ ___49-[RPDaemonProxy resumeHQLRWithCompletionHandler:]_block_invoke.cold.1
+ ___51-[RPControlCenterClient replayKitAngelDisconnected]_block_invoke
+ ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke
+ ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke.42
+ ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke_2
+ ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke_3
+ ___51-[RPControlCenterClient startRecordingWithHandler:]_block_invoke
+ ___51-[RPControlCenterClient startRecordingWithHandler:]_block_invoke.40
+ ___51-[RPControlCenterClient startRecordingWithHandler:]_block_invoke_2
+ ___52-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke
+ ___52-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke.39
+ ___53-[RPControlCenterClient getSystemBroadcastPickerInfo]_block_invoke
+ ___53-[RPControlCenterClient requestToCancelReadyToRecord]_block_invoke
+ ___53-[RPScreenRecorder startHQLRWithSessionInfo:handler:]_block_invoke
+ ___53-[RPScreenRecorder startHQLRWithSessionInfo:handler:]_block_invoke.38
+ ___53-[RPScreenRecorder startHQLRWithSessionInfo:handler:]_block_invoke.38.cold.1
+ ___53-[RPScreenRecorder startHQLRWithSessionInfo:handler:]_block_invoke_2
+ ___53-[RPScreenRecorder startHQLRWithSessionInfo:handler:]_block_invoke_2.cold.1
+ ___54-[RPControlCenterClient countdownInterruptWithStatus:]_block_invoke
+ ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke
+ ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke.60
+ ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke_2
+ ___55-[RPControlCenterClient stopObservingCallIsActiveState]_block_invoke
+ ___55-[RPScreenRecorder recordingDidStopWithError:movieURL:]_block_invoke.88
+ ___56-[RPControlCenterClient startObservingCallIsActiveState]_block_invoke
+ ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke
+ ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke.64
+ ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke_2
+ ___57+[RPControlCenterClient getSystemBroadcastExtensionInfo:]_block_invoke
+ ___60-[RPControlCenterClient initAndFetchAVSystemControllerState]_block_invoke
+ ___60-[RPControlCenterClient loadAvailableExtensionsWithHandler:]_block_invoke
+ ___60-[RPControlCenterClient loadAvailableExtensionsWithHandler:]_block_invoke.30
+ ___60-[RPScreenRecorder startClipBufferingWithCompletionHandler:]_block_invoke.50
+ ___60-[RPScreenRecorder startClipBufferingWithCompletionHandler:]_block_invoke.50.cold.1
+ ___61-[RPControlCenterClient extensionWithBundleIDExists:handler:]_block_invoke
+ ___61-[RPControlCenterClient screenRecorderDidChangeAvailability:]_block_invoke
+ ___61-[RPDaemonProxy startHQLRWithSessionInfo:windowSize:handler:]_block_invoke
+ ___61-[RPDaemonProxy startHQLRWithSessionInfo:windowSize:handler:]_block_invoke.cold.1
+ ___64-[RPControlCenterClient broadcastController:didFinishWithError:]_block_invoke
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.3
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.4
+ ___69-[RPControlCenterClient startBroadcastWithExtensionBundleID:handler:]_block_invoke
+ ___71-[RPControlCenterClient startBroadcastWithBroadcastController:handler:]_block_invoke
+ ___88-[RPControlCenterClient screenRecorder:didStopRecordingWithPreviewViewController:error:]_block_invoke
+ ___block_descriptor_32_e8_v16?08l
+ ___block_descriptor_40_e8_32bs_e59_v16?0"STBackgroundActivitiesStatusDomainUserInteraction"8ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8B16ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_40_e8_32s_e92_v32?0"FBSDisplayLayoutMonitor"8"FBSDisplayLayout"16"FBSDisplayLayoutTransitionContext"24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e118_v24?0"STMutableBackgroundActivitiesStatusDomainData"8"STMutableBackgroundActivitiesStatusDomainDataChangeContext"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e8_v16?08ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.158
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.170
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.190
+ ___block_literal_global.192
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.204
+ ___block_literal_global.220
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.226
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.244
+ ___block_literal_global.246
+ ___block_literal_global.248
+ ___block_literal_global.254
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.260
+ ___block_literal_global.262
+ ___block_literal_global.57
+ ___block_literal_global.60
+ ___block_literal_global.62
+ ___block_literal_global.63
+ ___block_literal_global.66
+ ___block_literal_global.89
+ ___block_literal_global.90
+ _bzero
+ _kCVPixelBufferIOSurfacePropertiesKey
+ _kIOSurfaceContentHeadroom
+ _objc_msgSend$activateWithUserInteractionHandler:
+ _objc_msgSend$addAttribution:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$allObjects
+ _objc_msgSend$alwaysOnDisplayEnabled
+ _objc_msgSend$attributeForKey:
+ _objc_msgSend$attributionWithAuditToken:
+ _objc_msgSend$callDelegate:
+ _objc_msgSend$configurationForDefaultMainDisplayMonitor
+ _objc_msgSend$currentAppUsingCamera
+ _objc_msgSend$deactivate
+ _objc_msgSend$descriptionForHQLR
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$didChangeAvailability:
+ _objc_msgSend$didStartRecordingOrBroadcast
+ _objc_msgSend$didStopRecordingOrBroadcast
+ _objc_msgSend$didUpdateClientStateWithAvailableExtensions:completionHandler:
+ _objc_msgSend$displayBacklightLevel
+ _objc_msgSend$distantPast
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$endReadyToRecord
+ _objc_msgSend$extensionWithBundleIDExists:handler:
+ _objc_msgSend$fetchIsCallActive
+ _objc_msgSend$finishSystemBroadcastWithHandler:
+ _objc_msgSend$floatValue
+ _objc_msgSend$getSessionType
+ _objc_msgSend$getSystemBroadcastPickerInfo
+ _objc_msgSend$handleUserInteractionsWithBlock:
+ _objc_msgSend$highQualityLocalRecordingOn
+ _objc_msgSend$highQualityLocalRecordingReady
+ _objc_msgSend$hqlrCountdownStarted
+ _objc_msgSend$initAndFetchAVSystemControllerState
+ _objc_msgSend$initWithBackgroundActivityIdentifier:
+ _objc_msgSend$initWithBackgroundActivityIdentifier:activityAttribution:
+ _objc_msgSend$initWithCommonFormat:sampleRate:channels:interleaved:
+ _objc_msgSend$initWithCurrentSession
+ _objc_msgSend$isAvailable
+ _objc_msgSend$isClientRecordingTypeHQLR
+ _objc_msgSend$isClientRecordingTypeSystemRecording
+ _objc_msgSend$isCountingDown
+ _objc_msgSend$isMixedRealityCameraEnabled
+ _objc_msgSend$loadAvailableExtensionsWithHandler:
+ _objc_msgSend$microphoneOn
+ _objc_msgSend$mixedRealityCameraOn
+ _objc_msgSend$monitorWithConfiguration:
+ _objc_msgSend$notifyClientDelegatesStart:
+ _objc_msgSend$notifyClientDelegatesStart:withRecordingType:
+ _objc_msgSend$now
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$presentCancelReadyToRecord
+ _objc_msgSend$publishNewDataWithUserInteractionHandler:
+ _objc_msgSend$recordingOn
+ _objc_msgSend$recordingTimerDidUpdate
+ _objc_msgSend$removeAttribution:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$removePointerAtIndex:
+ _objc_msgSend$requestToCancelReadyToRecord
+ _objc_msgSend$resumeHQLR
+ _objc_msgSend$resumeHQLRWithCompletionHandler:
+ _objc_msgSend$scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
+ _objc_msgSend$screenRecordingPassthroughCamera
+ _objc_msgSend$sensorActivityDataForActiveSensorType:
+ _objc_msgSend$sessionDidFailToStart
+ _objc_msgSend$sessionIsStarting
+ _objc_msgSend$setAttribute:forKey:error:
+ _objc_msgSend$setCountdown:
+ _objc_msgSend$setCurrentAttribution:
+ _objc_msgSend$setHighQualityLocalRecordingReady:
+ _objc_msgSend$setHqlrCountdownStarted:
+ _objc_msgSend$setMixedRealityCameraEnabled:
+ _objc_msgSend$setNeedsUserInteractivePriority:
+ _objc_msgSend$setPrivateDelegate:
+ _objc_msgSend$setPublisher:
+ _objc_msgSend$setRecordingType:
+ _objc_msgSend$setSystemCountdownStarted:
+ _objc_msgSend$setTransitionHandler:
+ _objc_msgSend$setUpFrontBoardServices
+ _objc_msgSend$setUserInitiated:
+ _objc_msgSend$setupSystemBroadcastWithExtension:handler:
+ _objc_msgSend$sharedAVSystemController
+ _objc_msgSend$startBroadcastWithBroadcastController:handler:
+ _objc_msgSend$startBroadcastWithExtensionBundleID:handler:
+ _objc_msgSend$startHQLRWithHandler:
+ _objc_msgSend$startHQLRWithSessionInfo:handler:
+ _objc_msgSend$startHQLRWithSessionInfo:windowSize:handler:
+ _objc_msgSend$startObservingCallIsActiveState
+ _objc_msgSend$startReadyToRecord
+ _objc_msgSend$startReadyToRecordBanner
+ _objc_msgSend$startRecordingCountdownWithSessionType:
+ _objc_msgSend$startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:listenerEndpoint:withHandler:
+ _objc_msgSend$startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:withHandler:
+ _objc_msgSend$startSystemRecordingWithMicrophoneEnabled:handler:
+ _objc_msgSend$stopHQLR:
+ _objc_msgSend$stopHQLRRecordingWithHandler:
+ _objc_msgSend$stopHQLRWithHandler:
+ _objc_msgSend$stopReadyToRecord
+ _objc_msgSend$stopReadyToRecordBanner
+ _objc_msgSend$stopSystemRecording:
+ _objc_msgSend$streamDescription
+ _objc_msgSend$systemBannerEnabled
+ _objc_msgSend$terminateAngelRecordingSession
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$updateStatusIsCountingDown:IsRecording:
+ _objc_msgSend$updateVolatileData:completion:
+ _objc_msgSend$userInfo
+ _objc_msgSend$validateHQLRSessionInfo:
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_opt_new
+ _sharedInstance._sharedClient
- -[RPControlCenterAngelProxy startRecordingCountdown]
- -[RPDaemonProxy startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:listenerEndpoint:withHandler:]
- -[RPDaemonProxy startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:withHandler:]
- -[RPFeatureFlagUtility screenCaptureKitRecordingHDR]
- GCC_except_table14
- _OBJC_IVAR_$_RPFeatureFlagUtility._screenCaptureKitRecordingHDR
- _OUTLINED_FUNCTION_7
- ___106-[RPDaemonProxy startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:withHandler:]_block_invoke
- ___106-[RPDaemonProxy startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:withHandler:]_block_invoke.cold.1
- ___123-[RPDaemonProxy startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:listenerEndpoint:withHandler:]_block_invoke
- ___123-[RPDaemonProxy startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:listenerEndpoint:withHandler:]_block_invoke.cold.1
- ___21-[RPDaemonProxy init]_block_invoke.143
- ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke.87
- ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke.94
- ___55-[RPScreenRecorder recordingDidStopWithError:movieURL:]_block_invoke.72
- ___60-[RPScreenRecorder startClipBufferingWithCompletionHandler:]_block_invoke.37
- ___60-[RPScreenRecorder startClipBufferingWithCompletionHandler:]_block_invoke.37.cold.1
- ___block_literal_global.147
- ___block_literal_global.149
- ___block_literal_global.151
- ___block_literal_global.153
- ___block_literal_global.155
- ___block_literal_global.157
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.163
- ___block_literal_global.165
- ___block_literal_global.167
- ___block_literal_global.169
- ___block_literal_global.171
- ___block_literal_global.173
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.181
- ___block_literal_global.183
- ___block_literal_global.185
- ___block_literal_global.187
- ___block_literal_global.189
- ___block_literal_global.191
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.201
- ___block_literal_global.203
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.219
- ___block_literal_global.221
- ___block_literal_global.227
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.44
- ___block_literal_global.47
- ___block_literal_global.50
- ___block_literal_global.86
- _objc_msgSend$startRecordingCountdown
- _objc_msgSend$startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:listenerEndpoint:withHandler:
- _objc_msgSend$startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:withHandler:
CStrings:
+ " [ERROR] %{public}s:%d Could not create pixel buffer for blank frame"
+ " [ERROR] %{public}s:%d could not issue sandbox extension for client file=%@"
+ " [ERROR] %{public}s:%d failed to retrieve CallIsActive from AVSystemController_CallIsActiveDidChangeNotification"
+ " [ERROR] %{public}s:%d failed to start because destination file URL is unspecified"
+ " [ERROR] %{public}s:%d save to file expected, but file url is nil"
+ " [INFO] %{public}s:%d %p Display layout updated displayBacklightLevel=%d"
+ " [INFO] %{public}s:%d %p Display layout updated to minimum backlight"
+ " [INFO] %{public}s:%d %p Stopped HQLR recording"
+ " [INFO] %{public}s:%d %p Stopped system broadcast"
+ " [INFO] %{public}s:%d %p Stopped system recording"
+ " [INFO] %{public}s:%d %p Stopping HQLR recording"
+ " [INFO] %{public}s:%d %p Stopping system broadcast"
+ " [INFO] %{public}s:%d %p Stopping system recording"
+ " [INFO] %{public}s:%d %p broadcastURL=%@"
+ " [INFO] %{public}s:%d %p cameraOn=%d"
+ " [INFO] %{public}s:%d %p connection=%p"
+ " [INFO] %{public}s:%d %p delegate=%p"
+ " [INFO] %{public}s:%d %p delegate=%p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i"
+ " [INFO] %{public}s:%d %p delegate=%p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i highQualityLocalRecordingOn:%i"
+ " [INFO] %{public}s:%d %p delegate=%p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i, highQualityLocalRecordingOn:%i"
+ " [INFO] %{public}s:%d %p delegate=%p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i, highQualityLocalRecordingOn:%i highQualityLocalRecordingReady:%i"
+ " [INFO] %{public}s:%d %p failed to start"
+ " [INFO] %{public}s:%d %p failed to start HQLR"
+ " [INFO] %{public}s:%d %p failed to start system broadcast"
+ " [INFO] %{public}s:%d %p failed to start system recording"
+ " [INFO] %{public}s:%d %p fetched new copy of broadcast extensions"
+ " [INFO] %{public}s:%d %p fetching new copy of broadcast extensions."
+ " [INFO] %{public}s:%d %p fetching new copy of system broadcast picker info"
+ " [INFO] %{public}s:%d %p get cached _preferredExtension and _shouldShowMicButton"
+ " [INFO] %{public}s:%d %p get cached availableExtensions"
+ " [INFO] %{public}s:%d %p is starting"
+ " [INFO] %{public}s:%d %p isCountingDown:%i, recordingOn:%i highQualityLocalRecordingOn:%d"
+ " [INFO] %{public}s:%d %p isCountingDown=%d recordingOn=%d highQualityLocalRecordingOn=%d lockUIControls=%d recordingType=%d"
+ " [INFO] %{public}s:%d %p microphoneOn=%d"
+ " [INFO] %{public}s:%d %p mixedRealityCameraOn=%d"
+ " [INFO] %{public}s:%d %p preferredExtension=%@ showsMicButton=%d"
+ " [INFO] %{public}s:%d %p recordingOn:%d microphoneOn:%d mixedRealityCameraOn:%d highQualityLocalRecordingOn:%d"
+ " [INFO] %{public}s:%d %p recordingType=%d"
+ " [INFO] %{public}s:%d %p started HQLR with no errors"
+ " [INFO] %{public}s:%d %p started system broadcast with no errors"
+ " [INFO] %{public}s:%d %p started system recording with no errors"
+ " [INFO] %{public}s:%d %p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i"
+ " [INFO] %{public}s:%d %p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i highQualityLocalRecordingOn:%i"
+ " [INFO] %{public}s:%d :%d from current mixed reality camera state:%d"
+ " [INFO] %{public}s:%d AVSystemController notification: %@"
+ " [INFO] %{public}s:%d Available Extensions: %lu"
+ " [INFO] %{public}s:%d Call became active during ready to record"
+ " [INFO] %{public}s:%d Dismissing Ready to Record banner state"
+ " [INFO] %{public}s:%d Fetching AVSystemController"
+ " [INFO] %{public}s:%d HQLR start completed"
+ " [INFO] %{public}s:%d RPControlCenterClient=%p RPScreenRecorder=%p"
+ " [INFO] %{public}s:%d Returning nil audio tap for none type"
+ " [INFO] %{public}s:%d Showing Ready to Record banner state"
+ " [INFO] %{public}s:%d Started HQLR via ready to record"
+ " [INFO] %{public}s:%d Subscribed to AVSystemController_CallIsActiveDidChangeNotification"
+ " [INFO] %{public}s:%d Timeout for Ready to Record. Cancelling"
+ " [INFO] %{public}s:%d Unsubscribe to AVSystemController_CallIsActiveDidChangeNotification"
+ " [INFO] %{public}s:%d Will start HQLR recording"
+ " [INFO] %{public}s:%d Will start system recording"
+ " [INFO] %{public}s:%d adding background activity attribution=%@"
+ " [INFO] %{public}s:%d attempting to start system broadcast with mic:%d cam:%d mixed reality cam:%d"
+ " [INFO] %{public}s:%d attempting to start system recording with mic:%d cam:%d mixed reality cam:%d"
+ " [INFO] %{public}s:%d checking if recordingType %d is HQLR"
+ " [INFO] %{public}s:%d checking if recordingType %d is system recording"
+ " [INFO] %{public}s:%d context=%@"
+ " [INFO] %{public}s:%d created new background activity attribution=%@"
+ " [INFO] %{public}s:%d fetched AVSystemController. AVSystemController_CallIsActive=%@"
+ " [INFO] %{public}s:%d image not found for extension"
+ " [INFO] %{public}s:%d isAvailable %d isInitialized %d"
+ " [INFO] %{public}s:%d recording start completed"
+ " [INFO] %{public}s:%d removing background activity attribution=%@"
+ " [INFO] %{public}s:%d returning call active=%d"
+ " [INFO] %{public}s:%d sessionInfo %@"
+ " [INFO] %{public}s:%d sessionInfo=%@"
+ " [INFO] %{public}s:%d setting user interaction block"
+ " [INFO] %{public}s:%d time since cache = %f"
+ " [INFO] %{public}s:%d using cached image for extension"
+ "%@/LocalCapture_%@.mp4"
+ "-[RPBackgroundActivity activateWithUserInteractionHandler:]"
+ "-[RPBackgroundActivity deactivate]"
+ "-[RPBackgroundActivity initWithBackgroundActivityIdentifier:]"
+ "-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]"
+ "-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke"
+ "-[RPControlCenterAngelProxy requestToCancelReadyToRecord]"
+ "-[RPControlCenterAngelProxy startReadyToRecord]"
+ "-[RPControlCenterAngelProxy startRecordingCountdownWithSessionType:]"
+ "-[RPControlCenterAngelProxy stopReadyToRecord]"
+ "-[RPControlCenterClient addDegate:]"
+ "-[RPControlCenterClient broadcastController:didFinishWithError:]"
+ "-[RPControlCenterClient broadcastController:didUpdateBroadcastURL:]"
+ "-[RPControlCenterClient broadcastController:didUpdateServiceInfo:]"
+ "-[RPControlCenterClient cancelReadyToRecord]_block_invoke"
+ "-[RPControlCenterClient cancelRecordingCountdown]"
+ "-[RPControlCenterClient countdownInterruptWithStatus:]"
+ "-[RPControlCenterClient currentAppUsingCamera]"
+ "-[RPControlCenterClient dealloc]"
+ "-[RPControlCenterClient endReadyToRecord]"
+ "-[RPControlCenterClient endReadyToRecord]_block_invoke"
+ "-[RPControlCenterClient extensionWithBundleIDExists:handler:]"
+ "-[RPControlCenterClient fetchIsCallActive]_block_invoke"
+ "-[RPControlCenterClient getSystemBroadcastPickerInfo]"
+ "-[RPControlCenterClient getSystemBroadcastPickerInfo]_block_invoke"
+ "-[RPControlCenterClient imageForBundleID:extensionInfo:]"
+ "-[RPControlCenterClient initAndFetchAVSystemControllerState]_block_invoke"
+ "-[RPControlCenterClient init]"
+ "-[RPControlCenterClient isAvailableAndInitialized]"
+ "-[RPControlCenterClient isClientRecordingTypeHQLR]"
+ "-[RPControlCenterClient isClientRecordingTypeSystemRecording]"
+ "-[RPControlCenterClient isScreenRecorderAvailable]"
+ "-[RPControlCenterClient loadAvailableExtensionsWithHandler:]"
+ "-[RPControlCenterClient loadAvailableExtensionsWithHandler:]_block_invoke"
+ "-[RPControlCenterClient notifyClientDelegatesStart:]"
+ "-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke"
+ "-[RPControlCenterClient removeDelegate:]"
+ "-[RPControlCenterClient replayKitAngelDisconnected]_block_invoke"
+ "-[RPControlCenterClient requestToCancelReadyToRecord]"
+ "-[RPControlCenterClient resetBroadcastPickerPreferredExt]"
+ "-[RPControlCenterClient screenRecorder:didStopRecordingWithPreviewViewController:error:]"
+ "-[RPControlCenterClient screenRecorderDidChangeAvailability:]"
+ "-[RPControlCenterClient screenRecorderDidUpdateState:]"
+ "-[RPControlCenterClient setCameraOn:]"
+ "-[RPControlCenterClient setCountdown:]_block_invoke"
+ "-[RPControlCenterClient setCountdown:]_block_invoke_3"
+ "-[RPControlCenterClient setMicrophoneOn:]"
+ "-[RPControlCenterClient setMixedRealityCameraOn:]"
+ "-[RPControlCenterClient setRecordingType:]"
+ "-[RPControlCenterClient setUpFrontBoardServices]_block_invoke"
+ "-[RPControlCenterClient setUpFrontBoardServices]_block_invoke_2"
+ "-[RPControlCenterClient startBroadcastWithBroadcastController:handler:]"
+ "-[RPControlCenterClient startBroadcastWithExtensionBundleID:handler:]"
+ "-[RPControlCenterClient startBroadcastWithHandler:]"
+ "-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke"
+ "-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke_3"
+ "-[RPControlCenterClient startHQLRReadyToRecord:]_block_invoke"
+ "-[RPControlCenterClient startHQLRWithHandler:]"
+ "-[RPControlCenterClient startHQLRWithHandler:]_block_invoke"
+ "-[RPControlCenterClient startHQLRWithHandler:]_block_invoke_2"
+ "-[RPControlCenterClient startObservingCallIsActiveState]_block_invoke"
+ "-[RPControlCenterClient startReadyToRecordBanner]"
+ "-[RPControlCenterClient startRecordingCountdown]"
+ "-[RPControlCenterClient startRecordingWithHandler:]"
+ "-[RPControlCenterClient startRecordingWithHandler:]_block_invoke"
+ "-[RPControlCenterClient startRecordingWithHandler:]_block_invoke_2"
+ "-[RPControlCenterClient stopCurrentSession:]"
+ "-[RPControlCenterClient stopCurrentSession:]_block_invoke"
+ "-[RPControlCenterClient stopCurrentSession:]_block_invoke_2"
+ "-[RPControlCenterClient stopCurrentSession]"
+ "-[RPControlCenterClient stopHQLRRecordingWithHandler:]"
+ "-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke"
+ "-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke_2"
+ "-[RPControlCenterClient stopObservingCallIsActiveState]_block_invoke"
+ "-[RPControlCenterClient stopReadyToRecordBanner]"
+ "-[RPControlCenterClient stopSystemRecordingWithHandler:]"
+ "-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke"
+ "-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke_2"
+ "-[RPControlCenterClient updateCallActive:]"
+ "-[RPControlCenterClient updateCallActive:]_block_invoke"
+ "-[RPControlCenterClient updateCallActive:]_block_invoke_3"
+ "-[RPControlCenterClient updateClientState]"
+ "-[RPControlCenterClient updateClientState]_block_invoke"
+ "-[RPControlCenterClient updateStatusIsCountingDown:IsRecording:]"
+ "-[RPDaemonProxy resumeHQLRWithCompletionHandler:]"
+ "-[RPDaemonProxy resumeHQLRWithCompletionHandler:]_block_invoke"
+ "-[RPDaemonProxy startHQLRWithSessionInfo:windowSize:handler:]"
+ "-[RPScreenRecorder resumeHQLR]"
+ "-[RPScreenRecorder resumeHQLR]_block_invoke"
+ "-[RPScreenRecorder setMixedRealityCameraEnabled:]"
+ "-[RPScreenRecorder startHQLRWithSessionInfo:handler:]"
+ "-[RPScreenRecorder startHQLRWithSessionInfo:handler:]_block_invoke"
+ "-[RPScreenRecorder startHQLRWithSessionInfo:handler:]_block_invoke_2"
+ "-[RPScreenRecorder stopHQLR:]"
+ "@\"AVSystemController\""
+ "@\"CCUIContentModuleContext\""
+ "@\"FBSDisplayLayoutMonitor\""
+ "@\"NSArray\""
+ "@\"NSPointerArray\""
+ "@\"NSTimer\""
+ "@\"RPBackgroundActivity\""
+ "@\"RPScreenRecorder\""
+ "@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\""
+ "@\"STBackgroundActivitiesStatusDomainPublisher\""
+ "Countdown1"
+ "Countdown2"
+ "Countdown3"
+ "CountdownComplete"
+ "RPBackgroundActivity"
+ "RPBroadcastControllerDelegate"
+ "RPControlCenterAngelProxyDelegate"
+ "RPControlCenterClient"
+ "RPDaemonProxy: startHQLRWithContextID: proxy error: %d"
+ "RPDaemonProxy: startHQLRWithContextID:withHandler:"
+ "RPHQLR"
+ "RPSampleBufferUtilities_CreateBlankPixelBuffer"
+ "RPScreenRecorderDelegate"
+ "RPScreenRecorderPrivateDelegate"
+ "Solarium"
+ "SwiftUI"
+ "T@\"CCUIContentModuleContext\",&,N,V_hqlrContentModuleContext"
+ "T@\"NSString\",&,N,V_currentTimerString"
+ "T@\"NSString\",&,N,V_extensionBundleID"
+ "T@\"NSString\",R,C,N,V_backgroundActivityIdentifier"
+ "T@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\",&,N,V_currentAttribution"
+ "T@\"STBackgroundActivitiesStatusDomainPublisher\",&,N,V_publisher"
+ "TB,N,GisMixedRealityCameraEnabled,V_mixedRealityCameraEnabled"
+ "TB,N,V_broadcastMode"
+ "TB,N,V_cameraOn"
+ "TB,N,V_highQualityLocalRecordingOn"
+ "TB,N,V_highQualityLocalRecordingReady"
+ "TB,N,V_hqlrCountdownStarted"
+ "TB,N,V_microphoneOn"
+ "TB,N,V_mixedRealityCameraOn"
+ "TB,N,V_systemCountdownStarted"
+ "TB,R,N,GisBackgroundActivityActive,V_backgroundActivityActive"
+ "TB,R,N,V_isCountingDown"
+ "TB,R,N,V_isInitialized"
+ "TB,R,N,V_lockUIControls"
+ "TB,R,N,V_recordingOn"
+ "TB,R,N,V_replayKitSDRToneMapping"
+ "TB,R,N,V_shouldShowMicButton"
+ "TQ,N,V_recordingType"
+ "VirtualAudio"
+ "Vv48@0:8@\"NSDictionary\"16{CGSize=dd}24@?<v@?@\"NSError\">40"
+ "Vv48@0:8@16{CGSize=dd}24@?40"
+ "Vv60@0:8@\"NSString\"16{CGSize=dd}24B40B44B48@?<v@?@\"NSError\">52"
+ "Vv60@0:8@16{CGSize=dd}24B40B44B48@?52"
+ "Vv68@0:8@\"NSString\"16{CGSize=dd}24B40B44B48@\"NSXPCListenerEndpoint\"52@?<v@?@\"NSError\">60"
+ "Vv68@0:8@16{CGSize=dd}24B40B44B48@52@?60"
+ "WindowServerScreenshots"
+ "_availableExtensions"
+ "_backgroundActivityActive"
+ "_backgroundActivityIdentifier"
+ "_broadcastController"
+ "_broadcastMode"
+ "_cameraDeviceID"
+ "_cameraOn"
+ "_countdownPaused"
+ "_countdownState"
+ "_currentAttribution"
+ "_currentTimerString"
+ "_delegates"
+ "_extensionBundleID"
+ "_extensionCacheTime"
+ "_fetchQueue"
+ "_highQualityLocalRecordingEnabled"
+ "_highQualityLocalRecordingOn"
+ "_highQualityLocalRecordingReady"
+ "_hqlrBasicDescription"
+ "_hqlrCapture"
+ "_hqlrContentModuleContext"
+ "_hqlrCountdownStarted"
+ "_iconImageCache"
+ "_isCallActive"
+ "_isCountingDown"
+ "_isInitialized"
+ "_layoutMonitor"
+ "_lockUIControls"
+ "_microphoneDeviceID"
+ "_microphoneOn"
+ "_mixedRealityCameraEnabled"
+ "_mixedRealityCameraOn"
+ "_pickerInfoCacheTime"
+ "_publisher"
+ "_readyToRecordBackgroundActivity"
+ "_readyToRecordTimer"
+ "_recordingOn"
+ "_recordingSDRToneMapping"
+ "_recordingType"
+ "_replayKitSDRToneMapping"
+ "_replayKitScreenRecordingHDR"
+ "_screenRecorder"
+ "_screenRecordingPassthroughCamera"
+ "_shouldShowMicButton"
+ "_solariumEnabled"
+ "_systemController"
+ "_systemCountdownStarted"
+ "_windowServerScreenshots"
+ "activateWithUserInteractionHandler:"
+ "addAttribution:"
+ "addDegate:"
+ "addPointer:"
+ "allObjects"
+ "attributeForKey:"
+ "attributionWithAuditToken:"
+ "backgroundActivityActive"
+ "backgroundActivityIdentifier"
+ "broadcastMode"
+ "callDelegate:"
+ "cameraDeviceID"
+ "cameraOn"
+ "cancelReadyToRecord"
+ "com.apple.replaykit.controlcenterclient"
+ "com.apple.replaykit.recordToCameraRoll"
+ "com.apple.replaykit.saveToFiles"
+ "com.apple.replaykit.saveToURL"
+ "com.apple.systemstatus.background-activity.replaykit.callrecording.ready"
+ "configurationForDefaultMainDisplayMonitor"
+ "countdownStatusPause"
+ "countdownStatusResume"
+ "currentAppUsingCamera"
+ "currentAttribution"
+ "currentTimerString"
+ "deactivate"
+ "defaultAudio"
+ "descriptionForHQLR"
+ "dictionaryWithDictionary:"
+ "didChangeAvailability:"
+ "didStartRecordingOrBroadcast"
+ "didStopRecordingOrBroadcast"
+ "didUpdateClientStateWithAvailableExtensions:completionHandler:"
+ "displayBacklightLevel"
+ "distantPast"
+ "drawInRect:"
+ "endReadyToRecord"
+ "extAppImgData"
+ "extBundleID"
+ "extensionBundleID"
+ "extensionWithBundleIDExists:handler:"
+ "fetchIsCallActive"
+ "fileURL"
+ "floatValue"
+ "getSessionType"
+ "getSystemBroadcastPickerInfo"
+ "handleUserInteractionsWithBlock:"
+ "highQualityLocalRecordingEnabled"
+ "highQualityLocalRecordingOn"
+ "highQualityLocalRecordingReady"
+ "hqlr"
+ "hqlrContentModuleContext"
+ "hqlrCountdownStarted"
+ "hqlrSandboxTokenForFileURL"
+ "imageForBundleID:extensionInfo:"
+ "initAndFetchAVSystemControllerState"
+ "initWithBackgroundActivityIdentifier:"
+ "initWithBackgroundActivityIdentifier:activityAttribution:"
+ "initWithCommonFormat:sampleRate:channels:interleaved:"
+ "ios_high_quality_local_recording"
+ "isAvailableAndInitialized"
+ "isBackgroundActivityActive"
+ "isClientRecordingTypeHQLR"
+ "isClientRecordingTypeSystemRecording"
+ "isCountingDown"
+ "isInitialized"
+ "isMixedRealityCameraEnabled"
+ "isScreenRecorderAvailable"
+ "loadAvailableExtensionsWithHandler:"
+ "lockUIControls"
+ "microphoneDeviceID"
+ "microphoneOn"
+ "mixedRealityCameraEnabled"
+ "mixedRealityCameraOn"
+ "monitorWithConfiguration:"
+ "none"
+ "notifyClientDelegatesStart:"
+ "notifyClientDelegatesStart:withRecordingType:"
+ "now"
+ "pointerAtIndex:"
+ "presentCancelReadyToRecord"
+ "publishNewDataWithUserInteractionHandler:"
+ "publisher"
+ "recordingOn"
+ "recordingSDRToneMapping"
+ "recordingTimerDidUpdate"
+ "recordingType"
+ "removeAttribution:"
+ "removeDelegate:"
+ "removeObserver:name:object:"
+ "removePointerAtIndex:"
+ "replayKitSDRToneMapping"
+ "replayKitScreenRecordingHDR"
+ "requestToCancelReadyToRecord"
+ "resetBroadcastPickerPreferredExt"
+ "resumeHQLR"
+ "resumeHQLRWithCompletionHandler:"
+ "saveToDestination"
+ "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
+ "screen"
+ "screenRecordingPassthroughCamera"
+ "sensorActivityDataForActiveSensorType:"
+ "sessionDidFailToStart"
+ "sessionIsStarting"
+ "setAttribute:forKey:error:"
+ "setBroadcastMode:"
+ "setCameraOn:"
+ "setCountdown:"
+ "setCurrentAttribution:"
+ "setCurrentTimerString:"
+ "setExtensionBundleID:"
+ "setHighQualityLocalRecordingOn:"
+ "setHighQualityLocalRecordingReady:"
+ "setHqlrContentModuleContext:"
+ "setHqlrCountdownStarted:"
+ "setMicrophoneOn:"
+ "setMixedRealityCameraEnabled:"
+ "setMixedRealityCameraOn:"
+ "setNeedsUserInteractivePriority:"
+ "setPublisher:"
+ "setRecordingType:"
+ "setSystemCountdownStarted:"
+ "setTransitionHandler:"
+ "setUpFrontBoardServices"
+ "setUserInitiated:"
+ "sharedAVSystemController"
+ "shouldShowMicButton"
+ "showBannerWithURL:identifier:sessionID:completionHandler:"
+ "solariumEnabled"
+ "startBroadcastWithBroadcastController:handler:"
+ "startBroadcastWithExtensionBundleID:handler:"
+ "startHQLRReadyToRecord:"
+ "startHQLRWithHandler:"
+ "startHQLRWithSessionInfo:handler:"
+ "startHQLRWithSessionInfo:windowSize:handler:"
+ "startObservingCallIsActiveState"
+ "startReadyToRecord"
+ "startReadyToRecordBanner"
+ "startRecordingCountdownWithSessionType:"
+ "startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:listenerEndpoint:withHandler:"
+ "startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:mixedRealityCameraEnabled:withHandler:"
+ "stopCurrentSession:"
+ "stopHQLR:"
+ "stopHQLRRecordingWithHandler:"
+ "stopHQLRWithHandler:"
+ "stopObservingCallIsActiveState"
+ "stopReadyToRecord"
+ "stopReadyToRecordBanner"
+ "streamDescription"
+ "system"
+ "systemCountdownStarted"
+ "terminateAngelRecordingSession"
+ "timeIntervalSinceNow"
+ "toneMappedSDREnabled"
+ "updateCallActive:"
+ "updateClientState"
+ "updateStatusIsCountingDown:IsRecording:"
+ "updateVolatileData:completion:"
+ "userInfo"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"STBackgroundActivitiesStatusDomainUserInteraction\"8"
+ "v16@?0@8"
+ "v20@?0@\"NSString\"8B16"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@\"RPScreenRecorder\"16"
+ "v24@0:8B16B20"
+ "v24@?0@\"STMutableBackgroundActivitiesStatusDomainData\"8@\"STMutableBackgroundActivitiesStatusDomainDataChangeContext\"16"
+ "v28@0:8B16Q20"
+ "v32@0:8@\"RPBroadcastController\"16@\"NSDictionary\"24"
+ "v32@0:8@\"RPBroadcastController\"16@\"NSError\"24"
+ "v32@0:8@\"RPBroadcastController\"16@\"NSURL\"24"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
+ "v40@0:8@\"RPScreenRecorder\"16@\"NSError\"24@\"RPPreviewViewController\"32"
+ "v40@0:8@\"RPScreenRecorder\"16@\"RPPreviewViewController\"24@\"NSError\"32"
+ "validateHQLRSessionInfo:"
+ "weakObjectsPointerArray"
+ "windowServerScreenshots"
+ "{AudioStreamBasicDescription=dIIIIIIII}16@0:8"
- " [INFO] %{public}s:%d attempting to start system broadcast with mic:%d cam:%d"
- " [INFO] %{public}s:%d attempting to start system recording with mic:%d cam:%d"
- "-[RPControlCenterAngelProxy startRecordingCountdown]"
- "Vv56@0:8@\"NSString\"16{CGSize=dd}24B40B44@?<v@?@\"NSError\">48"
- "Vv64@0:8@\"NSString\"16{CGSize=dd}24B40B44@\"NSXPCListenerEndpoint\"48@?<v@?@\"NSError\">56"
- "_screenCaptureKitRecordingHDR"
- "screenCaptureKitRecordingHDR"
- "showSavedToPhotosBannerWithPhotosURL:identifier:sessionID:completionHandler:"
- "startSystemBroadcastWithContextID:windowSize:microphoneEnabled:cameraEnabled:listenerEndpoint:withHandler:"
- "startSystemRecordingWithContextID:windowSize:microphoneEnabled:cameraEnabled:withHandler:"

```
