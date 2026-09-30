## ReplayKitModule

> `/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule`

```diff

-620.2.1.0.0
-  __TEXT.__text: 0xebd0
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x2120
-  __TEXT.__objc_methlist: 0xf00
-  __TEXT.__const: 0xb8
-  __TEXT.__objc_methname: 0x2dab
-  __TEXT.__oslogstring: 0xe64
-  __TEXT.__cstring: 0x22ec
-  __TEXT.__objc_classname: 0x211
-  __TEXT.__objc_methtype: 0xa21
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x670
-  __DATA_CONST.__cfstring: 0x660
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x60
+650.38.1.0.0
+  __TEXT.__text: 0x8d14
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x1820
+  __TEXT.__objc_methlist: 0xaf8
+  __TEXT.__const: 0xb0
+  __TEXT.__objc_methname: 0x26d1
+  __TEXT.__oslogstring: 0x6b8
+  __TEXT.__cstring: 0x16a7
+  __TEXT.__objc_classname: 0x14d
+  __TEXT.__objc_methtype: 0x75b
+  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__unwind_info: 0x280
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA.__objc_const: 0x2308
-  __DATA.__objc_selrefs: 0xc28
-  __DATA.__objc_ivar: 0xec
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x480
-  __DATA.__bss: 0x50
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA.__objc_const: 0x1990
+  __DATA.__objc_selrefs: 0xa18
+  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x240
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 347B39FE-0540-3EB7-804E-FCA09E5CC1A5
-  Functions: 264
-  Symbols:   157
-  CStrings:  915
+  UUID: 3368C5D6-BCDE-3E28-A7F3-0941013D0DDD
+  Functions: 166
+  Symbols:   135
+  CStrings:  694
 
Symbols:
+ _BSAuditTokenForCurrentProcess
+ _OBJC_CLASS_$_RPBackgroundActivity
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STBackgroundActivitiesStatusDomainBackgroundActivityAttribution
+ _OBJC_CLASS_$_STBackgroundActivitiesStatusDomainPublisher
+ _OBJC_METACLASS_$_RPBackgroundActivity
- _CFPreferencesCopyAppValue
- _OBJC_CLASS_$_BSMutableServiceInterface
- _OBJC_CLASS_$_BSObjCProtocol
- _OBJC_CLASS_$_BSServiceConnection
- _OBJC_CLASS_$_BSServiceConnectionEndpoint
- _OBJC_CLASS_$_BSServiceQuality
- _OBJC_CLASS_$_FBSDisplayLayoutMonitor
- _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSPointerArray
- _OBJC_CLASS_$_RBSDomainAttribute
- _OBJC_CLASS_$_RPBroadcastController
- _OBJC_CLASS_$_RPControlCenterAngelProxy
- _OBJC_CLASS_$_RPDaemonProxy
- _OBJC_CLASS_$_RPScreenRecorder
- _OBJC_METACLASS_$_RPControlCenterAngelProxy
- _OBJC_METACLASS_$_RPControlCenterClient
- _UIGraphicsBeginImageContextWithOptions
- _UIGraphicsEndImageContext
- _UIGraphicsGetImageFromCurrentImageContext
- _dispatch_after
- _dispatch_queue_create
- _dispatch_time
- _objc_opt_new
- _objc_retain_x9
- _os_variant_allows_internal_security_policies
CStrings:
+ " [INFO] %{public}s:%d [_HQLRButton setEnabled:NO];"
+ " [INFO] %{public}s:%d [_HQLRButton setEnabled:YES];"
+ " [INFO] %{public}s:%d adding background activity attribution=%@"
+ " [INFO] %{public}s:%d created new background activity attribution=%@"
+ " [INFO] %{public}s:%d removing background activity attribution=%@"
+ " [INFO] %{public}s:%d set highQualityLocalRecordingOn set %i"
+ " [INFO] %{public}s:%d setting user interaction block"
+ "-[RPBackgroundActivity activateWithUserInteractionHandler:]"
+ "-[RPBackgroundActivity deactivate]"
+ "-[RPBackgroundActivity initWithBackgroundActivityIdentifier:]"
+ "-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]"
+ "-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke"
+ "-[RPControlCenterModuleBackgroundViewController hqlrButtonPressed:]"
+ "-[RPControlCenterModuleBackgroundViewController updateHQLRButtonConstraints]"
+ "-[RPControlCenterModuleBackgroundViewController updateHQLRState]"
+ "@\"NSArray\"16@0:8"
+ "@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\""
+ "@\"STBackgroundActivitiesStatusDomainPublisher\""
+ "CONTROL_CENTER_HQLR"
+ "CONTROL_CENTER_HQLR_ALERT_DESCRIPTION"
+ "CONTROL_CENTER_HQLR_ALERT_TITLE"
+ "CONTROL_CENTER_RECORDING_ALERT_CANCEL"
+ "CONTROL_CENTER_RECORDING_ALERT_STOP"
+ "RPBackgroundActivity"
+ "Solarium"
+ "SwiftUI"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSString\",R,C,N,V_backgroundActivityIdentifier"
+ "T@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\",&,N,V_currentAttribution"
+ "T@\"STBackgroundActivitiesStatusDomainPublisher\",&,N,V_publisher"
+ "TB,R,N,GisBackgroundActivityActive,V_backgroundActivityActive"
+ "TB,R,N,V_replayKitSDRToneMapping"
+ "VirtualAudio"
+ "WindowServerScreenshots"
+ "_HQLRButton"
+ "_backgroundActivityActive"
+ "_backgroundActivityIdentifier"
+ "_currentAttribution"
+ "_highQualityLocalRecordingEnabled"
+ "_publisher"
+ "_recordingSDRToneMapping"
+ "_replayKitSDRToneMapping"
+ "_replayKitScreenRecordingHDR"
+ "_screenRecordingPassthroughCamera"
+ "_solariumEnabled"
+ "_windowServerScreenshots"
+ "activateWithUserInteractionHandler:"
+ "addAttribution:"
+ "attributionWithAuditToken:"
+ "backgroundActivityActive"
+ "backgroundActivityIdentifier"
+ "containerViewsForPlatterTreatment"
+ "currentAttribution"
+ "deactivate"
+ "didChangeCountdownState:"
+ "handleUserInteractionsWithBlock:"
+ "highQualityLocalRecordingEnabled"
+ "highQualityLocalRecordingOn"
+ "hqlrButtonPressed:"
+ "initWithBackgroundActivityIdentifier:"
+ "initWithBackgroundActivityIdentifier:activityAttribution:"
+ "ios_high_quality_local_recording"
+ "isBackgroundActivityActive"
+ "isClientRecordingTypeSystemRecording"
+ "notifyClientDelegatesStart:withRecordingType:"
+ "person.circle"
+ "presentCancelReadyToRecord"
+ "presentRecordingAlert"
+ "publishNewDataWithUserInteractionHandler:"
+ "publisher"
+ "recordingSDRToneMapping"
+ "removeAttribution:"
+ "replayKitSDRToneMapping"
+ "replayKitScreenRecordingHDR"
+ "screenRecordingPassthroughCamera"
+ "setCurrentAttribution:"
+ "setHQLRButtonSubtitle:"
+ "setHighQualityLocalRecordingOn:"
+ "setPublisher:"
+ "setRecordingType:"
+ "setSuppressesContentTransitions:"
+ "setSystemCountdownStarted:"
+ "setUserInitiated:"
+ "setupHQLRButton"
+ "solariumEnabled"
+ "startSystemRecordingOrBroadcastWithDelay:"
+ "suppressesContentTransitions"
+ "systemCountdownStarted"
+ "toneMappedSDREnabled"
+ "updateHQLRButtonConstraints"
+ "updateHQLRState"
+ "updateVolatileData:completion:"
+ "v16@?0@\"STBackgroundActivitiesStatusDomainUserInteraction\"8"
+ "v16@?0@\"UIAlertAction\"8"
+ "v24@?0@\"STMutableBackgroundActivitiesStatusDomainData\"8@\"STMutableBackgroundActivitiesStatusDomainDataChangeContext\"16"
+ "windowServerScreenshots"
- " [INFO] %{public}s:%d %p Display layout updated displayBacklightLevel=%d"
- " [INFO] %{public}s:%d %p Display layout updated to minimum backlight"
- " [INFO] %{public}s:%d %p Stopped system broadcast"
- " [INFO] %{public}s:%d %p Stopped system recording"
- " [INFO] %{public}s:%d %p Stopping system broadcast"
- " [INFO] %{public}s:%d %p Stopping system recording"
- " [INFO] %{public}s:%d %p broadcastURL=%@"
- " [INFO] %{public}s:%d %p cameraOn=%d"
- " [INFO] %{public}s:%d %p delegate=%p"
- " [INFO] %{public}s:%d %p delegate=%p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i"
- " [INFO] %{public}s:%d %p failed to start"
- " [INFO] %{public}s:%d %p failed to start system broadcast"
- " [INFO] %{public}s:%d %p failed to start system recording"
- " [INFO] %{public}s:%d %p fetched new copy of broadcast extensions"
- " [INFO] %{public}s:%d %p fetching new copy of broadcast extensions."
- " [INFO] %{public}s:%d %p fetching new copy of system broadcast picker info"
- " [INFO] %{public}s:%d %p get cached _preferredExtension and _shouldShowMicButton"
- " [INFO] %{public}s:%d %p get cached availableExtensions"
- " [INFO] %{public}s:%d %p is starting"
- " [INFO] %{public}s:%d %p isCountingDown:%i, recordingOn:%i"
- " [INFO] %{public}s:%d %p isCountingDown=%d recordingOn=%d lockUIControls=%d"
- " [INFO] %{public}s:%d %p microphoneOn=%d"
- " [INFO] %{public}s:%d %p preferredExtension=%@ showsMicButton=%d"
- " [INFO] %{public}s:%d %p recordingOn:%d microphoneOn:%d"
- " [INFO] %{public}s:%d %p started system broadcast with no errors"
- " [INFO] %{public}s:%d %p started system recording with no errors"
- " [INFO] %{public}s:%d %p updated status to isCountingDown:%i lockUIControls:%i, recordingOn:%i"
- " [INFO] %{public}s:%d Activation handler"
- " [INFO] %{public}s:%d Available Extensions: %lu"
- " [INFO] %{public}s:%d Interruption handler"
- " [INFO] %{public}s:%d Invalidation handler"
- " [INFO] %{public}s:%d RPAngel endpoint nil"
- " [INFO] %{public}s:%d RPAngelServerProtocol nil"
- " [INFO] %{public}s:%d RPControlCenterClient=%p RPScreenRecorder=%p"
- " [INFO] %{public}s:%d [_camButton setEnabled:NO];"
- " [INFO] %{public}s:%d [_camButton setEnabled:YES];"
- " [INFO] %{public}s:%d completed"
- " [INFO] %{public}s:%d hideStatusBar=%d"
- " [INFO] %{public}s:%d image not found for extension"
- " [INFO] %{public}s:%d isAvailable %d isInitialized %d"
- " [INFO] %{public}s:%d set cameraOn set %i"
- " [INFO] %{public}s:%d time since cache = %f"
- " [INFO] %{public}s:%d using cached image for extension"
- "-[RPControlCenterAngelProxy cancelRecordingCountdown]"
- "-[RPControlCenterAngelProxy countdownInterruptWithStatus:]"
- "-[RPControlCenterAngelProxy hideAndStopRecordingBanner]"
- "-[RPControlCenterAngelProxy setCountdownState:]"
- "-[RPControlCenterAngelProxy setupConnection]"
- "-[RPControlCenterAngelProxy setupConnection]_block_invoke"
- "-[RPControlCenterAngelProxy setupConnection]_block_invoke_2"
- "-[RPControlCenterAngelProxy showReactionsTipForApplication:bundleID:]"
- "-[RPControlCenterAngelProxy showRecordingBanner]"
- "-[RPControlCenterAngelProxy startRecordingCountdown]"
- "-[RPControlCenterAngelProxy stopCurrentSession]"
- "-[RPControlCenterAngelProxy stopRecordingCalled]"
- "-[RPControlCenterClient addDegate:]"
- "-[RPControlCenterClient broadcastController:didFinishWithError:]"
- "-[RPControlCenterClient broadcastController:didUpdateBroadcastURL:]"
- "-[RPControlCenterClient broadcastController:didUpdateServiceInfo:]"
- "-[RPControlCenterClient cancelRecordingCountdown]"
- "-[RPControlCenterClient countdownInterruptWithStatus:]"
- "-[RPControlCenterClient dealloc]"
- "-[RPControlCenterClient extensionWithBundleIDExists:handler:]"
- "-[RPControlCenterClient getSystemBroadcastPickerInfo]"
- "-[RPControlCenterClient getSystemBroadcastPickerInfo]_block_invoke"
- "-[RPControlCenterClient imageForBundleID:extensionInfo:]"
- "-[RPControlCenterClient init]"
- "-[RPControlCenterClient isAvailableAndInitialized]"
- "-[RPControlCenterClient loadAvailableExtensionsWithHandler:]"
- "-[RPControlCenterClient loadAvailableExtensionsWithHandler:]_block_invoke"
- "-[RPControlCenterClient notifyClientDelegatesStart:]"
- "-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke"
- "-[RPControlCenterClient removeDelegate:]"
- "-[RPControlCenterClient replayKitAngelDisconnected]_block_invoke"
- "-[RPControlCenterClient resetBroadcastPickerPreferredExt]"
- "-[RPControlCenterClient screenRecorder:didStopRecordingWithPreviewViewController:error:]"
- "-[RPControlCenterClient screenRecorderDidChangeAvailability:]"
- "-[RPControlCenterClient screenRecorderDidUpdateState:]"
- "-[RPControlCenterClient setCameraOn:]"
- "-[RPControlCenterClient setCountdown:]_block_invoke_4"
- "-[RPControlCenterClient setMicrophoneOn:]"
- "-[RPControlCenterClient setUpFrontBoardServices]_block_invoke"
- "-[RPControlCenterClient setUpFrontBoardServices]_block_invoke_2"
- "-[RPControlCenterClient startBroadcastWithBroadcastController:handler:]"
- "-[RPControlCenterClient startBroadcastWithExtensionBundleID:handler:]"
- "-[RPControlCenterClient startBroadcastWithHandler:]"
- "-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke"
- "-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke_3"
- "-[RPControlCenterClient startRecordingCountdown]"
- "-[RPControlCenterClient startRecordingWithHandler:]"
- "-[RPControlCenterClient startRecordingWithHandler:]_block_invoke"
- "-[RPControlCenterClient startRecordingWithHandler:]_block_invoke_2"
- "-[RPControlCenterClient stopCurrentSession:]"
- "-[RPControlCenterClient stopCurrentSession:]_block_invoke"
- "-[RPControlCenterClient stopCurrentSession:]_block_invoke_2"
- "-[RPControlCenterClient stopCurrentSession]"
- "-[RPControlCenterClient stopSystemRecordingWithHandler:]"
- "-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke"
- "-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke_2"
- "-[RPControlCenterClient updateClientState]"
- "-[RPControlCenterClient updateClientState]_block_invoke"
- "-[RPControlCenterClient updateStatusIsCountingDown:IsRecording:]"
- "-[RPControlCenterModuleBackgroundViewController camButtonPressed:]"
- "-[RPControlCenterModuleBackgroundViewController updateCameraButtonConstraints]"
- "-[RPControlCenterModuleBackgroundViewController updateCameraState]"
- "@\"<RPControlCenterAngelProxyDelegate>\""
- "@\"BSServiceConnection<BSServiceConnectionClient>\""
- "@\"FBSDisplayLayoutMonitor\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSPointerArray\""
- "@\"RPBroadcastController\""
- "@\"RPScreenRecorder\""
- "@32@0:8@16@24"
- "BasicAngelIPC"
- "CONTROL_CENTER_CAMERA"
- "Countdown1"
- "Countdown2"
- "Countdown3"
- "CountdownComplete"
- "RPAngelClientProtocol"
- "RPAngelServerProtocol"
- "RPBroadcastControllerDelegate"
- "RPControlCenterAngelProxy"
- "RPControlCenterAngelProxyDelegate"
- "RPControlCenterClient"
- "RPHideStatusBar"
- "RPScreenRecorderDelegate"
- "RPScreenRecorderPrivateDelegate"
- "T@\"<RPControlCenterAngelProxyDelegate>\",&,N,V_delegate"
- "T@\"NSString\",&,N,V_currentTimerString"
- "T@\"NSString\",&,N,V_extensionBundleID"
- "T@\"NSString\",&,N,V_preferredExtension"
- "TB,N,V_broadcastMode"
- "TB,N,V_cameraOn"
- "TB,N,V_microphoneOn"
- "TB,R,N,V_isCountingDown"
- "TB,R,N,V_isInitialized"
- "TB,R,N,V_lockUIControls"
- "TB,R,N,V_recordingOn"
- "TB,R,N,V_shouldShowMicButton"
- "UTF8String"
- "VB32@0:8@\"NSString\"16@\"NSString\"24"
- "VB32@0:8@16@24"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@16"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "Vv32@0:8@\"NSString\"16@\"NSString\"24"
- "Vv32@0:8@16@24"
- "Vv48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@16@24@32@?40"
- "_broadcastController"
- "_broadcastMode"
- "_camButton"
- "_cameraOn"
- "_connection"
- "_countdownPaused"
- "_countdownState"
- "_currentTimerString"
- "_delegate"
- "_delegates"
- "_extensionBundleID"
- "_extensionCacheTime"
- "_iconImageCache"
- "_isCountingDown"
- "_isInitialized"
- "_layoutMonitor"
- "_lockUIControls"
- "_microphoneOn"
- "_pickerInfoCacheTime"
- "_preferredExtension"
- "_recordingOn"
- "_rpUserErrorForCode:userInfo:"
- "_screenCaptureKitRecordingHDR"
- "_screenRecorder"
- "_shouldShowMicButton"
- "activate"
- "addPointer:"
- "allObjects"
- "attributeWithDomain:name:"
- "broadcastController:didFinishWithError:"
- "broadcastController:didUpdateBroadcastURL:"
- "broadcastController:didUpdateServiceInfo:"
- "broadcastMode"
- "callDelegate:"
- "camButtonPressed:"
- "camera"
- "cameraOn"
- "code"
- "com.apple.ReplayKitAngel.mach"
- "com.apple.ReplayKitAngel.session"
- "com.apple.common"
- "com.apple.replayd"
- "com.replaykitangel.angelProxyConnectionQueue"
- "configurationForDefaultMainDisplayMonitor"
- "configureConnection:"
- "connectToAngelWithCompletionHandler:"
- "connectionManagerQueue"
- "connectionWithEndpoint:"
- "countdownInterruptWithStatus:"
- "countdownStatusPause"
- "countdownStatusResume"
- "daemonProxy"
- "delegate"
- "disableCameraPip"
- "dismissReactionsTipForApplication:bundleID:"
- "displayBacklightLevel"
- "distantPast"
- "drawInRect:"
- "enableCameraPip"
- "endpointForMachName:service:instance:"
- "extensionWithBundleIDExists:handler:"
- "finishSystemBroadcastWithHandler:"
- "getBSServiceInterface"
- "getSystemBroadcastExtensionInfo:"
- "getSystemBroadcastPickerInfo"
- "getSystemBroadcastPickerInfo:"
- "hideAndStopRecordingBanner"
- "imageWithData:"
- "initWithCurrentSession"
- "initWithExtensionBundleID:broadcastURL:"
- "interfaceWithIdentifier:"
- "isAvailable"
- "isInitialized"
- "isMicrophoneEnabled"
- "isRecording"
- "loadAvailableExtensionsWithHandler:"
- "monitorWithConfiguration:"
- "now"
- "objectForKeyedSubscript:"
- "pauseCurrentSystemSession"
- "pointerAtIndex:"
- "protocolForProtocol:"
- "recordingTimerDidUpdate:"
- "remoteTargetWithLaunchingAssertionAttributes:"
- "removePointerAtIndex:"
- "replayKitAngelDisconnected"
- "resetBroadcastPickerPreferredExt"
- "resumeCurrentSystemSession"
- "screenCaptureKitRecordingHDR"
- "screenRecorder:didStopRecordingWithError:previewViewController:"
- "screenRecorder:didStopRecordingWithPreviewViewController:error:"
- "screenRecorderDidChangeAvailability:"
- "screenRecorderDidUpdateState:"
- "screenRecordingSupportedOnDevice"
- "setActivationHandler:"
- "setBroadcastMode:"
- "setBroadcastPickerPreferredExt:showsMicButton:"
- "setCamButtonSubtitle:"
- "setCameraEnabled:"
- "setCameraOn:"
- "setClientMessagingExpectation:"
- "setCountdown:"
- "setCountdownState:"
- "setDelegate:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMicrophoneEnabled:"
- "setNeedsUserInteractivePriority:"
- "setPrefersExpandedContentSizeMatchesGridSize:"
- "setPrivateDelegate:"
- "setServer:"
- "setServiceQuality:"
- "setSystemRecording:"
- "setTargetQueue:"
- "setTransitionHandler:"
- "setUpFrontBoardServices"
- "setValue:forKey:"
- "setupCameraButton"
- "setupConnection"
- "setupSystemBroadcastWithExtension:handler:"
- "sharedRecorder"
- "showReactionsTipForApplication:bundleID:"
- "showSavedToPhotosBannerWithPhotosURL:identifier:sessionID:completionHandler:"
- "startBroadcastWithBroadcastController:handler:"
- "startBroadcastWithExtensionBundleID:handler:"
- "startSystemBroadcastWithHandler:"
- "startSystemRecordingWithMicrophoneEnabled:handler:"
- "stopCurrentSession"
- "stopRecordingCalled"
- "stopSystemRecording:"
- "stopSystemRecordingWithHandler:"
- "terminateAngelRecordingSession"
- "timeIntervalSinceNow"
- "updateCameraButtonConstraints"
- "updateCameraState"
- "updateStatusIsCountingDown:IsRecording:"
- "updateTimer:"
- "userInitiated"
- "v16@?0@\"<BSServiceConnectionConfiguring>\"8"
- "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
- "v16@?0@\"NSArray\"8"
- "v16@?0@\"NSError\"8"
- "v16@?0@8"
- "v20@?0@\"NSString\"8B16"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@\"RPScreenRecorder\"16"
- "v24@0:8B16B20"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v32@0:8@\"RPBroadcastController\"16@\"NSDictionary\"24"
- "v32@0:8@\"RPBroadcastController\"16@\"NSError\"24"
- "v32@0:8@\"RPBroadcastController\"16@\"NSURL\"24"
- "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
- "v40@0:8@\"RPScreenRecorder\"16@\"NSError\"24@\"RPPreviewViewController\"32"
- "v40@0:8@\"RPScreenRecorder\"16@\"RPPreviewViewController\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "weakObjectsPointerArray"

```
