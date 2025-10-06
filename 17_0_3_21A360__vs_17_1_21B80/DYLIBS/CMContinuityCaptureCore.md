## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-458.3.12.1.0
-  __TEXT.__text: 0x5ab10
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_methlist: 0x3100
+465.15.2.0.0
+  __TEXT.__text: 0x5c410
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x3158
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x2008
-  __TEXT.__cstring: 0x55c8
-  __TEXT.__oslogstring: 0x6c83
+  __TEXT.__gcc_except_tab: 0x20e0
+  __TEXT.__cstring: 0x5934
+  __TEXT.__oslogstring: 0x6e56
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x1424
+  __TEXT.__unwind_info: 0x1468
   __TEXT.__objc_classname: 0xa62
-  __TEXT.__objc_methname: 0x8c28
-  __TEXT.__objc_methtype: 0x2007
-  __TEXT.__objc_stubs: 0x6c20
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x14c8
+  __TEXT.__objc_methname: 0x8e8c
+  __TEXT.__objc_methtype: 0x202d
+  __TEXT.__objc_stubs: 0x6de0
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x1540
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7470
-  __DATA_CONST.__objc_selrefs: 0x1f40
+  __DATA_CONST.__objc_const: 0x75f0
+  __DATA_CONST.__objc_selrefs: 0x1fb0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__cfstring: 0x3160
+  __AUTH_CONST.__cfstring: 0x33e0
   __AUTH_CONST.__objc_const: 0x1320
-  __AUTH_CONST.__const: 0x780
+  __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__auth_got: 0x5b0
   __AUTH.__objc_data: 0xe10
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x2f8
+  __DATA.__objc_classrefs: 0x310
   __DATA.__objc_superrefs: 0x160
-  __DATA.__objc_ivar: 0x5a0
+  __DATA.__objc_ivar: 0x5b8
   __DATA.__data: 0xae0
   __DATA.__bss: 0x158
   __DATA.__common: 0x60

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCB272C3-A3CB-302A-A07A-EDD98492FB8D
-  Functions: 1591
-  Symbols:   5749
-  CStrings:  3405
+  UUID: 776F8415-929F-3AD6-8972-2EA1CDBA66B0
+  Functions: 1609
+  Symbols:   5818
+  CStrings:  3487
 
Symbols:
+ -[CMContinuityCaptureAVCaptureBaseSession dealloc].cold.1
+ -[CMContinuityCaptureDeviceBase postDeferredEvent:data:]
+ -[CMContinuityCaptureDeviceBase restartSendingInvalidFramesIfApplicable]
+ -[CMContinuityCaptureDeviceBase scheduleInvalidFramesNotification:]
+ -[CMContinuityCaptureDeviceBase scheduleSendingInvalidFramesAfterTimeout:]
+ -[CMContinuityCaptureDeviceBase startSendingInvalidFrames]
+ -[CMContinuityCaptureDeviceBase stopSendingInvalidFrames]
+ -[CMContinuityCaptureRapportServer parseAndActOnStreamsSetupInfo:]
+ -[CMContinuityCaptureRemoteAudioDevice invalidate]
+ -[CMContinuityCaptureRemoteVideoDevice invalidate]
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table19
+ GCC_except_table42
+ GCC_except_table46
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table95
+ _CFUserNotificationReceiveResponse
+ _CMContinuityCaptureGetDateFromTimeString
+ _CMContinuityCapturePromptOpenTapToRadar
+ _CMContinuityCapturePromptOpenTapToRadar.cold.1
+ _ContinuityCaptureRapportClientStreamsSetupKey
+ _MGCopyAnswer
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._dispatchingInvalidFrames
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._ignoreSendingInvalidFrames
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._invalidFrameBlock
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._invalidFrameNotificationScheduled
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._invalidFrameTimeoutBlock
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._maxInvalidFramesDurationWhenConnectingInSec
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._timeToWaitBeforeSendingInvalidFramesWhenConnectingInSec
+ _OBJC_IVAR_$_CMContinuityCaptureRapportServer._createdIdentifiers
+ ___60-[CMContinuityCaptureDeviceBase _handleAVCNegotiation:data:]_block_invoke.26
+ ___60-[CMContinuityCaptureRapportServer relayTerminationComplete]_block_invoke.42
+ ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.44
+ ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.47
+ ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.48
+ ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.50
+ ___63-[CMContinuityCaptureDeviceBase _stopStream:option:completion:]_block_invoke.41
+ ___66-[CMContinuityCaptureRapportServer parseAndActOnStreamsSetupInfo:]_block_invoke
+ ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.53
+ ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.55
+ ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke_2.56
+ ___71-[CMContinuityCaptureDeviceBase stateMachineStartStreamOnEvent:option:]_block_invoke.52
+ ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.389
+ ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.391
+ ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.49
+ ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.50
+ ___74-[CMContinuityCaptureDeviceBase scheduleSendingInvalidFramesAfterTimeout:]_block_invoke
+ ___74-[CMContinuityCaptureDeviceBase scheduleSendingInvalidFramesAfterTimeout:]_block_invoke_2
+ ___74-[CMContinuityCaptureTransportRapportDevice enqueueReactionEffect:entity:]_block_invoke.189
+ ___81-[CMContinuityCaptureRapportServer parseAndNotifySessionStartInfo:transportInfo:]_block_invoke.39
+ ___81-[CMContinuityCaptureRapportServer parseAndNotifySessionStartInfo:transportInfo:]_block_invoke.40
+ ___81-[CMContinuityCaptureTransportRapportDevice captureStillImage:entity:completion:]_block_invoke.186
+ ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.173
+ ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.174
+ ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.178
+ ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.179
+ ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.31
+ ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.32
+ ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.33
+ ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.35
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.401
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.407
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.408
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.409
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.409.cold.1
+ ___95+[CMContinuityCaptureTransportRapportDevice queryCameraCapabilitiesFromRemoteDevice:transport:]_block_invoke.170
+ ___CMContinuityCapturePromptOpenTapToRadar_block_invoke
+ ___CMContinuityCapturePromptOpenTapToRadar_block_invoke.260
+ ___CMContinuityCapturePromptOpenTapToRadar_block_invoke.260.cold.1
+ ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_literal_global.117
+ ___block_literal_global.119
+ ___block_literal_global.191
+ ___block_literal_global.198
+ ___block_literal_global.263
+ ___block_literal_global.393
+ ___block_literal_global.43
+ ___block_literal_global.45
+ ___block_literal_global.48
+ __unnamed_array_storage.38
+ _kCFUserNotificationAlternateButtonTitleKey
+ _objc_msgSend$URL
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$parseAndActOnStreamsSetupInfo:
+ _objc_msgSend$postDeferredEvent:data:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$scheduleInvalidFramesNotification:
+ _objc_msgSend$scheduleSendingInvalidFramesAfterTimeout:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$startSendingInvalidFrames
+ _objc_msgSend$stopSendingInvalidFrames
+ _os_variant_has_internal_ui
- -[CMContinuityCaptureDeviceBase _debugInfo]
- GCC_except_table103
- GCC_except_table111
- GCC_except_table118
- GCC_except_table26
- GCC_except_table35
- GCC_except_table36
- GCC_except_table38
- GCC_except_table47
- GCC_except_table50
- GCC_except_table62
- GCC_except_table64
- GCC_except_table84
- GCC_except_table86
- GCC_except_table91
- _OBJC_IVAR_$_CMContinuityCaptureRemoteAudioDevice._transportDevice
- _OBJC_IVAR_$_CMContinuityCaptureRemoteVideoDevice._transportDevice
- ___60-[CMContinuityCaptureDeviceBase _handleAVCNegotiation:data:]_block_invoke.20
- ___60-[CMContinuityCaptureRapportServer relayTerminationComplete]_block_invoke.37
- ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.39
- ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.42
- ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.43
- ___62-[CMContinuityCaptureRapportServer setupRemoteDisplaySession:]_block_invoke.45
- ___63-[CMContinuityCaptureDeviceBase _stopStream:option:completion:]_block_invoke.35
- ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.47
- ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.49
- ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke_2.50
- ___71-[CMContinuityCaptureDeviceBase stateMachineStartStreamOnEvent:option:]_block_invoke.46
- ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.385
- ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.386
- ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.43
- ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.44
- ___74-[CMContinuityCaptureTransportRapportDevice enqueueReactionEffect:entity:]_block_invoke.186
- ___81-[CMContinuityCaptureRapportServer parseAndNotifySessionStartInfo:transportInfo:]_block_invoke.34
- ___81-[CMContinuityCaptureRapportServer parseAndNotifySessionStartInfo:transportInfo:]_block_invoke.35
- ___81-[CMContinuityCaptureTransportRapportDevice captureStillImage:entity:completion:]_block_invoke.183
- ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.170
- ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.171
- ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.175
- ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.176
- ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.26
- ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.27
- ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.28
- ___88-[CMContinuityCaptureRapportServer createStreamWithIdentifier:isMediaStream:completion:]_block_invoke.30
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.398
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.404
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.405
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.406
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.406.cold.1
- ___95+[CMContinuityCaptureTransportRapportDevice queryCameraCapabilitiesFromRemoteDevice:transport:]_block_invoke.167
- ___block_literal_global.106
- ___block_literal_global.188
- ___block_literal_global.195
- ___block_literal_global.37
- ___block_literal_global.39
- ___block_literal_global.390
- ___block_literal_global.42
- ___block_literal_global.80
- ___block_literal_global.85
- ___block_literal_global.88
- ___block_literal_global.93
- ___block_literal_global.98
- __unnamed_array_storage.32
CStrings:
+ "\x01\x11\x11\x14&R"
+ "\x04AA\x12\x11"
+ "\x1b\x11\"\x11!"
+ "%@ deallocated in state CMContinuityCaptureAVCaptureSessionStateRunning. Timestamp:%@"
+ "%@/%@: %@"
+ "%{public}@ %s name:%{pubic}@"
+ "%{public}@ %s no frames after timeout"
+ "%{public}@ %s schedule"
+ "%{public}@ %{public}@ already created, skip"
+ "%{public}@ [sessionID:%llx] Early setup for %{public}@"
+ "&\x11\x14"
+ "-[CMContinuityCaptureDeviceBase postDeferredEvent:data:]"
+ "-[CMContinuityCaptureDeviceBase restartSendingInvalidFramesIfApplicable]"
+ "-[CMContinuityCaptureDeviceBase scheduleSendingInvalidFramesAfterTimeout:]"
+ "-[CMContinuityCaptureDeviceBase scheduleSendingInvalidFramesAfterTimeout:]_block_invoke_2"
+ "-[CMContinuityCaptureDeviceBase startSendingInvalidFrames]"
+ "-[CMContinuityCaptureDeviceBase stopSendingInvalidFrames]"
+ "989213"
+ "BuildVersion"
+ "CMContinuityCaptureAVCaptureSession is deallocated in invalid state Running"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Continuity Camera session ended in an invalid state. Please file a radar"
+ "ContinuityCaptureRapportClientStreamsSetupKey"
+ "CoreMedia Capture"
+ "Description"
+ "Error creating Tap-to-Radar notification: %d"
+ "Error opening Tap-To-Radar URL: %@"
+ "File radar"
+ "HWModelStr"
+ "I Didn't Try"
+ "Ignore"
+ "LastStreamFrameDispatched"
+ "Open Tap-to-Radar result: %@"
+ "Opening Tap-to-Radar! Title: \"%@\", Description: \"%@\""
+ "Prompt opening Tap-to-Radar: %@"
+ "Reproducibility"
+ "Response Flags: %ld"
+ "Serious Bug"
+ "Title"
+ "URL"
+ "_createdIdentifiers"
+ "_dispatchingInvalidFrames"
+ "_ignoreSendingInvalidFrames"
+ "_invalidFrameBlock"
+ "_invalidFrameNotificationScheduled"
+ "_invalidFrameTimeoutBlock"
+ "_maxInvalidFramesDurationWhenConnectingInSec"
+ "_timeToWaitBeforeSendingInvalidFramesWhenConnectingInSec"
+ "com.apple.continuitycapture.ignoreSendingInvalidFrames"
+ "dateFromString:"
+ "defaultWorkspace"
+ "iOS"
+ "new"
+ "openURL:configuration:completionHandler:"
+ "parseAndActOnStreamsSetupInfo:"
+ "postDeferredEvent:data:"
+ "queryItemWithName:value:"
+ "restartSendingInvalidFramesIfApplicable"
+ "scheduleInvalidFramesNotification:"
+ "scheduleSendingInvalidFramesAfterTimeout:"
+ "setHost:"
+ "setQueryItems:"
+ "setScheme:"
+ "startSendingInvalidFrames"
+ "stopSendingInvalidFrames"
+ "tap-to-radar"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
+ "\xf0a"
- "\x01\x11\x11\x14&"
- "\x05AA\x12\x11"
- "\x1b\x11\x11\x12\x11!"
- "&\x11\x13"
- "DeferredEvents"
- "LastStreamNumberOfDispatchedFrames"
- "LastStreamStartTime"
- "StreamHistory"
- "_debugInfo"
- "\xf0q"

```
