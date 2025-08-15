## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-406.1.13.0.0
-  __TEXT.__text: 0x7e52c
+406.16.1.0.0
+  __TEXT.__text: 0x807e8
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x5870
+  __TEXT.__objc_methlist: 0x5a48
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x1adc
-  __TEXT.__cstring: 0xac53
-  __TEXT.__oslogstring: 0x1a25
+  __TEXT.__gcc_except_tab: 0x1b04
+  __TEXT.__cstring: 0xb0a4
+  __TEXT.__oslogstring: 0x1aa7
   __TEXT.__dlopen_cstrs: 0x4dc
-  __TEXT.__unwind_info: 0x1ba4
-  __TEXT.__objc_classname: 0x6ca
-  __TEXT.__objc_methname: 0xf0ab
-  __TEXT.__objc_methtype: 0x1b48
-  __TEXT.__objc_stubs: 0xb120
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x25d0
+  __TEXT.__unwind_info: 0x1c30
+  __TEXT.__objc_classname: 0x6cc
+  __TEXT.__objc_methname: 0xf64d
+  __TEXT.__objc_methtype: 0x1bb1
+  __TEXT.__objc_stubs: 0xb480
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x26b0
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc730
-  __DATA_CONST.__objc_selrefs: 0x3548
+  __DATA_CONST.__objc_const: 0xc840
+  __DATA_CONST.__objc_selrefs: 0x3678
+  __DATA_CONST.__objc_classrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x330
   __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0x74e0
+  __AUTH_CONST.__cfstring: 0x7740
   __AUTH_CONST.__objc_const: 0x15c8
-  __AUTH_CONST.__objc_intobj: 0x738
+  __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x1450
   __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_classrefs: 0x340
-  __DATA.__objc_superrefs: 0x160
-  __DATA.__objc_ivar: 0x760
-  __DATA.__data: 0x9e0
-  __DATA.__bss: 0x210
+  __DATA.__objc_ivar: 0x778
+  __DATA.__data: 0x9f8
+  __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A43B16FE-7F8A-3CEB-B990-49745A2E3B8F
-  Functions: 2620
-  Symbols:   8770
-  CStrings:  5241
+  UUID: A0DBFCC7-EB1D-35D5-94D5-70DCAD37C471
+  Functions: 2680
+  Symbols:   8932
+  CStrings:  5353
 
Symbols:
+ -[AXHAController processPropertyUpdates:isLocal:]
+ -[AXHAController sendMessagesPriority:]
+ -[AXHAServer sendMessagesPriorityDefault]
+ -[AXHAServer sendMessagesPriorityHigh]
+ -[HUAccessoryHearingSyncManager _cleanupNearbyDeviceStateDuplicatesForDevice:]
+ -[HUAccessoryHearingSyncManager _registerForNoiseEnabledPreferenceChange]
+ -[HUAccessoryHearingSyncManager noiseDisabled]
+ -[HUAccessoryHearingSyncManager sendNoiseMeasurementsDisabled:]
+ -[HUAccessoryHearingSyncManager sendNoiseMeasurementsDisabledIfNeeded]
+ -[HUAccessoryHearingSyncManager setNoiseDisabled:]
+ -[HUComfortSoundsController liveListenComfortSoundsSwitch]
+ -[HUComfortSoundsController setLiveListenComfortSoundsSwitch:]
+ -[HUComfortSoundsController startComfortSounds]
+ -[HUNearbyController descriptionForPriority:]
+ -[HUNearbyController sendMessage:toDevicesWithDomain:excludingState:withPriority:]
+ -[HUNearbyController sendMessage:toWatchDevicesWithDomain:excludingState:withPriority:]
+ -[HUNearbyController sendMessage:toWatchDevicesWithDomain:withPriority:]
+ -[HUNearbyController service:account:identifier:didSendWithSuccess:error:]
+ -[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]
+ -[HUNearbyHearingAidController checkHandoffAfterTimeout]
+ -[HUNearbyHearingAidController collectPropertyUpdatesFromPayload:]
+ -[HUNearbyHearingAidController collectedPropertyUpdates]
+ -[HUNearbyHearingAidController connectedPeerWithCompletion:]
+ -[HUNearbyHearingAidController connectionStateForDevice:]
+ -[HUNearbyHearingAidController connectionStateForDevice:].cold.1
+ -[HUNearbyHearingAidController defaultDevicesFromDevices:]
+ -[HUNearbyHearingAidController descriptionForCurrentMessagePriority]
+ -[HUNearbyHearingAidController descriptionForHandoffState]
+ -[HUNearbyHearingAidController deviceMessagePriority]
+ -[HUNearbyHearingAidController devicesFromDevices:withMessagePriority:]
+ -[HUNearbyHearingAidController finishHandoff]
+ -[HUNearbyHearingAidController handleSessionMessage:completion:]
+ -[HUNearbyHearingAidController handoffReason]
+ -[HUNearbyHearingAidController handoffTimer]
+ -[HUNearbyHearingAidController isPeerConnectedToHearingDevice]
+ -[HUNearbyHearingAidController lastSentPropertyUpdates]
+ -[HUNearbyHearingAidController logDevices:withTitle:fullInfo:]
+ -[HUNearbyHearingAidController messagePriorityForDevice:]
+ -[HUNearbyHearingAidController messagePriorityForDevice:].cold.1
+ -[HUNearbyHearingAidController processHandoffMessageFromPeer:state:]
+ -[HUNearbyHearingAidController processStateMessageFromPeer:state:]
+ -[HUNearbyHearingAidController processWriteMessageWithValue:]
+ -[HUNearbyHearingAidController processingHandoff]
+ -[HUNearbyHearingAidController relinquishCompleted]
+ -[HUNearbyHearingAidController relinquishConnectionForReason:toDevice:]
+ -[HUNearbyHearingAidController relinquishConnectionWithCompletion:]
+ -[HUNearbyHearingAidController requestConnectionForMedia]
+ -[HUNearbyHearingAidController requestConnectionForMedia].cold.1
+ -[HUNearbyHearingAidController requestHandoff:reason:]
+ -[HUNearbyHearingAidController resetHandoffOnDeviceQueue]
+ -[HUNearbyHearingAidController sendMessage:toDevices:messagePriority:]
+ -[HUNearbyHearingAidController sendMessageToAllDevices:messagePriority:]
+ -[HUNearbyHearingAidController sendMessagesPriorityDefault]
+ -[HUNearbyHearingAidController sendMessagesPriorityHigh]
+ -[HUNearbyHearingAidController sendPropertyUpdatesLowTimer]
+ -[HUNearbyHearingAidController sendStateMessage:toDevices:isUrgent:]
+ -[HUNearbyHearingAidController sendStateMessageToAllDevices:isUrgent:]
+ -[HUNearbyHearingAidController setCollectedPropertyUpdates:]
+ -[HUNearbyHearingAidController setConnectionState:forDevice:]
+ -[HUNearbyHearingAidController setConnectionState:forDevice:].cold.1
+ -[HUNearbyHearingAidController setDeviceMessagePriority:]
+ -[HUNearbyHearingAidController setHandoffReason:]
+ -[HUNearbyHearingAidController setHandoffTimer:]
+ -[HUNearbyHearingAidController setLastSentPropertyUpdates:]
+ -[HUNearbyHearingAidController setMessagePriority:forDevice:]
+ -[HUNearbyHearingAidController setMessagePriority:forDevice:].cold.1
+ -[HUNearbyHearingAidController setProcessingHandoff:]
+ -[HUNearbyHearingAidController setRelinquishCompleted:]
+ -[HUNearbyHearingAidController setSendPropertyUpdatesLowTimer:]
+ -[HUNearbyHearingAidController shouldRoute:]
+ -[HUNearbyHearingAidController urgentDevicesFromDevices:]
+ -[HUNearbySettings sentIDSMessage:domain:priority:priorityDescription:]
+ -[HUNearbySettings sentIDSMessage:domain:priority:priorityDescription:].cold.1
+ -[HUNoiseSettings notificationForNoiseEnabled]
+ GCC_except_table105
+ GCC_except_table13
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table57
+ GCC_except_table81
+ _IDSSendMessageOptionNonWakingKey
+ _IDSSendMessageOptionPushPriorityKey
+ _OBJC_IVAR_$_HUAccessoryHearingSyncManager._noiseDisabled
+ _OBJC_IVAR_$_HUComfortSoundsController._liveListenComfortSoundsSwitch
+ _OBJC_IVAR_$_HUNearbyHearingAidController._collectedPropertyUpdates
+ _OBJC_IVAR_$_HUNearbyHearingAidController._deviceMessagePriority
+ _OBJC_IVAR_$_HUNearbyHearingAidController._handoffReason
+ _OBJC_IVAR_$_HUNearbyHearingAidController._handoffTimer
+ _OBJC_IVAR_$_HUNearbyHearingAidController._lastSentPropertyUpdates
+ _OBJC_IVAR_$_HUNearbyHearingAidController._processingHandoff
+ _OBJC_IVAR_$_HUNearbyHearingAidController._relinquishCompleted
+ _OBJC_IVAR_$_HUNearbyHearingAidController._sendPropertyUpdatesLowTimer
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.470
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.483
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.491
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.500
+ ___25-[HUNoiseController init]_block_invoke.274
+ ___32-[AXHeardController startServer]_block_invoke_29
+ ___33-[HUComfortSoundsController init]_block_invoke.31
+ ___33-[HUComfortSoundsController init]_block_invoke.35
+ ___33-[HUComfortSoundsController init]_block_invoke.42
+ ___33-[HUComfortSoundsController init]_block_invoke.49
+ ___33-[HUComfortSoundsController init]_block_invoke.56
+ ___33-[HUComfortSoundsController init]_block_invoke_2.38
+ ___33-[HUComfortSoundsController init]_block_invoke_2.45
+ ___33-[HUComfortSoundsController init]_block_invoke_2.52
+ ___33-[HUComfortSoundsController init]_block_invoke_2.59
+ ___33-[HUComfortSoundsController init]_block_invoke_4
+ ___36-[HUNearbyHearingAidController stop]_block_invoke_2
+ ___37-[HUNearbyHearingAidController start]_block_invoke.113
+ ___37-[HUNearbyHearingAidController start]_block_invoke.118
+ ___37-[HUNearbyHearingAidController start]_block_invoke.99
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.114
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.346
+ ___40-[AXHAController setPairedHearingAidID:]_block_invoke_3
+ ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.149
+ ___47-[HUComfortSoundsController startComfortSounds]_block_invoke
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.560
+ ___52-[HUNearbyHearingAidController sendWrite:toDevices:]_block_invoke
+ ___53-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke.111
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.374
+ ___54-[HUNearbyHearingAidController sendWriteToAllDevices:]_block_invoke.cold.1
+ ___54-[HUNearbyHearingAidController sendWriteToAllDevices:]_block_invoke.cold.2
+ ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.112
+ ___56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke
+ ___56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke.88
+ ___57-[HUNearbyHearingAidController requestConnectionForMedia]_block_invoke
+ ___57-[HUNearbyHearingAidController requestConnectionForMedia]_block_invoke.46
+ ___60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.161
+ ___60-[HUNearbyHearingAidController connectedPeerWithCompletion:]_block_invoke
+ ___61-[HUNearbyHearingAidController processWriteMessageWithValue:]_block_invoke
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.100
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.104
+ ___66-[HUNearbyHearingAidController collectPropertyUpdatesFromPayload:]_block_invoke
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.106
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.71
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.91
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.98
+ ___67-[HUNearbyHearingAidController relinquishConnectionWithCompletion:]_block_invoke
+ ___68-[HUNearbyHearingAidController processHandoffMessageFromPeer:state:]_block_invoke
+ ___71-[HUNearbyHearingAidController devicesFromDevices:withMessagePriority:]_block_invoke
+ ___72-[HUNearbyController sendMessage:toWatchDevicesWithDomain:withPriority:]_block_invoke
+ ___76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke
+ ___76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke.52
+ ___78-[HUAccessoryHearingSyncManager _cleanupNearbyDeviceStateDuplicatesForDevice:]_block_invoke
+ ___82-[HUNearbyController sendMessage:toDevicesWithDomain:excludingState:withPriority:]_block_invoke
+ ___82-[HUNearbyController sendMessage:toDevicesWithDomain:excludingState:withPriority:]_block_invoke_2
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.414
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.434
+ ___87-[HUNearbyController sendMessage:toWatchDevicesWithDomain:excludingState:withPriority:]_block_invoke
+ ___87-[HUNearbyController sendMessage:toWatchDevicesWithDomain:excludingState:withPriority:]_block_invoke_2
+ ___block_descriptor_32_e18_B16?0"CBDevice"8l
+ ___block_descriptor_40_e8_32w_e20_v20?0B8"NSError"12lw32l8
+ ___block_descriptor_42_e8_32s_e24_v16?0"HUNearbyDevice"8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e25_v32?0"CBDevice"8Q16^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e31_B32?0"HUNearbyDevice"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSArray"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e24_v32?0"AXAsset"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e31_B32?0"HUNearbyDevice"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e25_v32?0"NSNumber"816^B24ls32l8s40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_84_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.101
+ ___block_literal_global.108
+ ___block_literal_global.138
+ ___block_literal_global.193
+ ___block_literal_global.229
+ ___block_literal_global.246
+ ___block_literal_global.330
+ ___block_literal_global.336
+ ___block_literal_global.411
+ ___block_literal_global.485
+ ___block_literal_global.493
+ ___block_literal_global.502
+ ___block_literal_global.520
+ ___block_literal_global.530
+ ___block_literal_global.73
+ ___iteratePairedBluetoothDevicesOnQueueCBv1_block_invoke
+ ___iteratePairedBluetoothDevicesOnQueueCBv1_block_invoke_2
+ __unnamed_array_storage.102
+ __unnamed_array_storage.106
+ __unnamed_array_storage.110
+ __unnamed_array_storage.114
+ __unnamed_array_storage.127
+ __unnamed_array_storage.131
+ __unnamed_array_storage.135
+ __unnamed_array_storage.138
+ __unnamed_array_storage.139
+ __unnamed_array_storage.142
+ __unnamed_array_storage.143
+ __unnamed_array_storage.154
+ __unnamed_array_storage.155
+ __unnamed_array_storage.490
+ __unnamed_array_storage.497
+ __unnamed_array_storage.498
+ __unnamed_array_storage.506
+ __unnamed_array_storage.507
+ __unnamed_array_storage.66
+ __unnamed_array_storage.74
+ __unnamed_array_storage.75
+ __unnamed_array_storage.98
+ _iteratePairedBluetoothDevicesOnQueueCBv1
+ _kAXSNoWakeCountKey
+ _kAXSTotalNoWakeCountKey
+ _objc_msgSend$_cleanupNearbyDeviceStateDuplicatesForDevice:
+ _objc_msgSend$_registerForNoiseEnabledPreferenceChange
+ _objc_msgSend$checkConnectionRequestedForMediaAfterTimeout
+ _objc_msgSend$checkHandoffAfterTimeout
+ _objc_msgSend$collectPropertyUpdatesFromPayload:
+ _objc_msgSend$collectedPropertyUpdates
+ _objc_msgSend$connectedPeerWithCompletion:
+ _objc_msgSend$connectionStateForDevice:
+ _objc_msgSend$defaultDevicesFromDevices:
+ _objc_msgSend$descriptionForCurrentMessagePriority
+ _objc_msgSend$descriptionForHandoffState
+ _objc_msgSend$descriptionForPriority:
+ _objc_msgSend$deviceMessagePriority
+ _objc_msgSend$devicesFromDevices:withMessagePriority:
+ _objc_msgSend$finishHandoff
+ _objc_msgSend$handleSessionMessage:completion:
+ _objc_msgSend$handoffReason
+ _objc_msgSend$handoffTimer
+ _objc_msgSend$isPeerConnectedToHearingDevice
+ _objc_msgSend$lastSentPropertyUpdates
+ _objc_msgSend$logDevices:withTitle:fullInfo:
+ _objc_msgSend$messagePriorityForDevice:
+ _objc_msgSend$processHandoffMessageFromPeer:state:
+ _objc_msgSend$processPropertyUpdates:isLocal:
+ _objc_msgSend$processStateMessageFromPeer:state:
+ _objc_msgSend$processWriteMessageWithValue:
+ _objc_msgSend$processingHandoff
+ _objc_msgSend$relinquishCompleted
+ _objc_msgSend$relinquishConnectionForReason:toDevice:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$requestConnectionForMedia
+ _objc_msgSend$requestHandoff:reason:
+ _objc_msgSend$resetHandoffOnDeviceQueue
+ _objc_msgSend$sendMessage:toDevices:messagePriority:
+ _objc_msgSend$sendMessage:toDevicesWithDomain:excludingState:withPriority:
+ _objc_msgSend$sendMessage:toWatchDevicesWithDomain:excludingState:withPriority:
+ _objc_msgSend$sendMessageToAllDevices:messagePriority:
+ _objc_msgSend$sendMessagesPriority:
+ _objc_msgSend$sendMessagesPriorityDefault
+ _objc_msgSend$sendMessagesPriorityHigh
+ _objc_msgSend$sendPropertyUpdatesLowTimer
+ _objc_msgSend$sendStateMessage:toDevices:isUrgent:
+ _objc_msgSend$sendStateMessageToAllDevices:isUrgent:
+ _objc_msgSend$sentIDSMessage:domain:priority:priorityDescription:
+ _objc_msgSend$setConnectionState:forDevice:
+ _objc_msgSend$setHandoffReason:
+ _objc_msgSend$setLastSentPropertyUpdates:
+ _objc_msgSend$setLiveListenComfortSoundsSwitch:
+ _objc_msgSend$setMessagePriority:forDevice:
+ _objc_msgSend$setProcessingHandoff:
+ _objc_msgSend$setRelinquishCompleted:
+ _objc_msgSend$shouldRoute:
+ _objc_msgSend$startComfortSounds
+ _objc_msgSend$urgentDevicesFromDevices:
+ _sharedInstance.Settings.408
+ _sharedInstance.onceToken.409
- -[HUHearingAidSettings allowHearingAidControlOnLockScreen]
- -[HUHearingAidSettings setAllowHearingAidControlOnLockScreen:]
- -[HUNearbyController sendMessageToWatchDevices:toDevicesWithDomain:withPriority:]
- -[HUNearbyHearingAidController checkConnectionPeers:]
- -[HUNearbyHearingAidController checkConnectionRelinquishedAfterTimeout]
- -[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]
- -[HUNearbyHearingAidController checkConnectionToHearingDevice:]
- -[HUNearbyHearingAidController getConnectedPeer:]
- -[HUNearbyHearingAidController handleSessionMessage:]
- -[HUNearbyHearingAidController logNewDevices:]
- -[HUNearbyHearingAidController peerHasConnectionToHearingDevice]
- -[HUNearbyHearingAidController processStateMessageFromPeer:state:response:]
- -[HUNearbyHearingAidController processWriteMessageWithValue:response:]
- -[HUNearbyHearingAidController processingConnection]
- -[HUNearbyHearingAidController processingTransition]
- -[HUNearbyHearingAidController relinquishConnectionForReason:]
- -[HUNearbyHearingAidController relinquishConnectionForReason:toDevice:sendHandoffMessage:]
- -[HUNearbyHearingAidController relinquishConnectionTimer]
- -[HUNearbyHearingAidController requestConnectionTimer]
- -[HUNearbyHearingAidController requestHandoffForMedia]
- -[HUNearbyHearingAidController requestHandoffForMedia].cold.1
- -[HUNearbyHearingAidController sendMessageToAllDevices:]
- -[HUNearbyHearingAidController sendStateMessage:toDevices:]
- -[HUNearbyHearingAidController sendStateMessageToAllDevices:]
- -[HUNearbyHearingAidController setProcessingConnection:]
- -[HUNearbyHearingAidController setProcessingTransition:]
- -[HUNearbyHearingAidController setRelinquishConnectionTimer:]
- -[HUNearbyHearingAidController setRequestConnectionTimer:]
- -[HUNearbyHearingAidController updateForBluetoothStateChange]
- -[HUNearbyHearingAidController updateStateOnDeviceQueue].cold.1
- -[HUNearbySettings sentIDSMessage:domain:]
- -[HUNearbySettings sentIDSMessage:domain:].cold.1
- GCC_except_table31
- GCC_except_table72
- GCC_except_table74
- _OBJC_IVAR_$_HUNearbyHearingAidController._processingConnection
- _OBJC_IVAR_$_HUNearbyHearingAidController._processingTransition
- _OBJC_IVAR_$_HUNearbyHearingAidController._relinquishConnectionTimer
- _OBJC_IVAR_$_HUNearbyHearingAidController._requestConnectionTimer
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.446
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.459
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.467
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.476
- ___25-[HUNoiseController init]_block_invoke.250
- ___33-[HUComfortSoundsController init]_block_invoke.34
- ___33-[HUComfortSoundsController init]_block_invoke.38
- ___33-[HUComfortSoundsController init]_block_invoke.45
- ___33-[HUComfortSoundsController init]_block_invoke.52
- ___33-[HUComfortSoundsController init]_block_invoke.59
- ___33-[HUComfortSoundsController init]_block_invoke_2.41
- ___33-[HUComfortSoundsController init]_block_invoke_2.48
- ___33-[HUComfortSoundsController init]_block_invoke_2.55
- ___33-[HUComfortSoundsController init]_block_invoke_2.62
- ___37-[HUNearbyHearingAidController start]_block_invoke.101
- ___37-[HUNearbyHearingAidController start]_block_invoke.108
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.109
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.322
- ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.140
- ___44-[AXHAController connectToControllerWithID:]_block_invoke
- ___49-[HUNearbyHearingAidController getConnectedPeer:]_block_invoke
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.536
- ___53-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke.112
- ___53-[HUNearbyHearingAidController checkConnectionPeers:]_block_invoke
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.350
- ___54-[HUNearbyHearingAidController requestHandoffForMedia]_block_invoke
- ___54-[HUNearbyHearingAidController requestHandoffForMedia]_block_invoke.45
- ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.108
- ___57-[HUNearbyHearingAidController device:didReceiveMessage:]_block_invoke.157
- ___59-[HUNearbyHearingAidController requestConnectionForReason:]_block_invoke.58
- ___60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.147
- ___61-[HUNearbyHearingAidController updateForBluetoothStateChange]_block_invoke
- ___63-[HUNearbyHearingAidController checkConnectionToHearingDevice:]_block_invoke
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.103
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.107
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.102
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.83
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.93
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.97
- ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke
- ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke.47
- ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke_2
- ___70-[HUNearbyHearingAidController processWriteMessageWithValue:response:]_block_invoke
- ___71-[HUNearbyHearingAidController checkConnectionRelinquishedAfterTimeout]_block_invoke
- ___71-[HUNearbyHearingAidController checkConnectionRelinquishedAfterTimeout]_block_invoke.72
- ___81-[HUNearbyController sendMessageToWatchDevices:toDevicesWithDomain:withPriority:]_block_invoke
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.390
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.410
- ___block_descriptor_40_e31_B32?0"HUNearbyDevice"8Q16^B24l
- ___block_descriptor_40_e8_32r_e25_v32?0"CBDevice"8Q16^B24lr32l8
- ___block_descriptor_42_e8_32s_e27_v20?0B8"HUNearbyDevice"12ls32l8
- ___block_descriptor_48_e8_32s_e27_v20?0B8"HUNearbyDevice"12ls32l8
- ___block_descriptor_48_e8_32w_e24_v32?0"AXAsset"8Q16^B24lw32l8
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSNumber"816^B24ls32l8s40l8s48l8
- ___block_descriptor_76_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.104
- ___block_literal_global.142
- ___block_literal_global.159
- ___block_literal_global.222
- ___block_literal_global.232
- ___block_literal_global.312
- ___block_literal_global.329
- ___block_literal_global.414
- ___block_literal_global.461
- ___block_literal_global.469
- ___block_literal_global.478
- ___block_literal_global.496
- ___block_literal_global.506
- ___block_literal_global.66
- ___block_literal_global.96
- ___block_literal_global.97
- __unnamed_array_storage.100
- __unnamed_array_storage.104
- __unnamed_array_storage.108
- __unnamed_array_storage.112
- __unnamed_array_storage.125
- __unnamed_array_storage.129
- __unnamed_array_storage.133
- __unnamed_array_storage.145
- __unnamed_array_storage.146
- __unnamed_array_storage.466
- __unnamed_array_storage.473
- __unnamed_array_storage.474
- __unnamed_array_storage.482
- __unnamed_array_storage.483
- __unnamed_array_storage.63
- __unnamed_array_storage.64
- __unnamed_array_storage.71
- __unnamed_array_storage.72
- __unnamed_array_storage.88
- __unnamed_array_storage.89
- __unnamed_array_storage.92
- __unnamed_array_storage.93
- __unnamed_array_storage.96
- _objc_msgSend$checkConnectionRelinquishedAfterTimeout
- _objc_msgSend$checkConnectionRequestedAfterTimeout
- _objc_msgSend$checkConnectionToHearingDevice:
- _objc_msgSend$connectToPairedDevice
- _objc_msgSend$getConnectedPeer:
- _objc_msgSend$handleSessionMessage:
- _objc_msgSend$logNewDevices:
- _objc_msgSend$peerHasConnectionToHearingDevice
- _objc_msgSend$processStateMessageFromPeer:state:response:
- _objc_msgSend$processWriteMessageWithValue:response:
- _objc_msgSend$processingConnection
- _objc_msgSend$processingTransition
- _objc_msgSend$relinquishConnectionForReason:
- _objc_msgSend$relinquishConnectionForReason:toDevice:sendHandoffMessage:
- _objc_msgSend$relinquishConnectionTimer
- _objc_msgSend$requestConnectionTimer
- _objc_msgSend$requestHandoffForMedia
- _objc_msgSend$sendMessageToAllDevices:
- _objc_msgSend$sendMessageToWatchDevices:toDevicesWithDomain:withPriority:
- _objc_msgSend$sendStateMessage:toDevices:
- _objc_msgSend$sendStateMessageToAllDevices:
- _objc_msgSend$sentIDSMessage:domain:
- _objc_msgSend$setProcessingConnection:
- _objc_msgSend$setProcessingTransition:
- _objc_msgSend$shouldRelinquishForPartialConnection
- _objc_msgSend$updateForBluetoothStateChange
- _objc_msgSend$validateResponse:
- _sharedInstance.Settings.411
- _sharedInstance.onceToken.412
CStrings:
+ "\x16"
+ " %@ is LEA 2.0"
+ "%@ devices: %@"
+ "%llu"
+ "-[AXHAController processPropertyUpdates:isLocal:]"
+ "-[AXHAServer _unregisterUpdateListenerHash:]"
+ "-[AXHAServer sendMessagesPriorityDefault]"
+ "-[AXHAServer sendMessagesPriorityHigh]"
+ "-[AXHeardController startServer]_block_invoke_29"
+ "-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2"
+ "-[HUComfortSoundsController init]_block_invoke_4"
+ "-[HUComfortSoundsController startComfortSounds]"
+ "-[HUNearbyHearingAidController processHandoffMessageFromPeer:state:]"
+ "-[HUNearbyHearingAidController processStateMessageFromPeer:state:]"
+ "-[HUNearbyHearingAidController processWriteMessageWithValue:]"
+ "-[HUNearbyHearingAidController processWriteMessageWithValue:]_block_invoke"
+ "-[HUNearbyHearingAidController sendMessagesPriorityDefault]"
+ "-[HUNearbyHearingAidController sendMessagesPriorityHigh]"
+ "-[HUNearbyHearingAidController sendWrite:toDevices:]"
+ "-[HUNearbyHearingAidController sendWrite:toDevices:]_block_invoke"
+ "-[HUNearbyHearingAidController setMessagePriority:forDevice:]"
+ "3\x11\"\x14"
+ "After timeout gave up on Media handoff, transiton connection to peer"
+ "Already Processing Connection, Skip"
+ "Already processing, skip requestHandoff: %@"
+ "Available Devices"
+ "B16@?0@\"CBDevice\"8"
+ "B20@0:8B16"
+ "B32@0:8q16@24"
+ "B32@0:8q16q24"
+ "Check timer fired for handoff %@, reason: %@, connectedPeer: %@"
+ "Connect to %@, Connected peer: %@, Connecting Peer: %@"
+ "ConnectedPeer: %@"
+ "Connection request has been finished"
+ "Connection request interrupted, Nearby started: %d, isPaired: %d, BT available: %d, hasPeers: %d"
+ "Connection transition has been finished"
+ "Couldn't Start handoff for a reason: %@"
+ "Couldn't relinquish connection"
+ "Couldn't request connection"
+ "Devices updated, available devices count: %@"
+ "Did update state new: %@, old: %@, handoff: %@"
+ "Disconnect, Connected peer: %@, Connecting Peer: %@"
+ "Finish handoff %@, reason: %@, connectedPeer: %@"
+ "Handoff is completed"
+ "HandoffState: Connecting, Sending ControllerConnectWithReason %@ to %@, time: %@"
+ "High"
+ "IDS Received HCMessageIdentifierMessagesPriority: %@ from device: %@"
+ "IDS Requesting property %@ from device %@"
+ "IDS Sending MessagesPriority Default"
+ "IDS Sending MessagesPriority Urgent"
+ "IDS Sending(%@) %@ to %@ with %@, priority: %@"
+ "IDS didSendWithSuccess GUID %@, success %d, error: %@"
+ "IDS received Noise Disabled: %@"
+ "Invoking relinquishCompleted callback"
+ "No Handoff"
+ "NoWake"
+ "NoWakeCount"
+ "Peers discovered, sending CheckIn, ControllerConnected: %@ MessagesPriority: %@ to"
+ "Processing state: %@, handoff: %@"
+ "Received CheckIn from device: %@, current state: %@"
+ "Relinquish connection"
+ "Relinquish connection with callback"
+ "Relinquishing connection, holdingMediaForConnection: NO"
+ "Request connection"
+ "Request connection reason %@"
+ "Reset handoff from: %@"
+ "Sending ControllerConnected: %@, isUrgent: YES"
+ "Sending Properties to urgent devices: %@"
+ "Sending Properties:\n%@\nto default devices:\n%@"
+ "Should relinquish: %d Reason: %@, Call: [pending: %d, active: %d, avc: %d, endpoint: %d], inCall: %d"
+ "Should request connection %d, %d, %d, %d, %d, %d, %d"
+ "Skipping sending ControllerConnected: %@"
+ "Start requestHandoff: %@, reason: %@"
+ "Started processing connection"
+ "Started relinquishing connection"
+ "Starting check timer for handoff %@, reason: %@"
+ "Stop LiveListen unit error: %@"
+ "Switching to Background Sounds from Live Listen"
+ "T@\"AXDispatchTimer\",&,N,V_handoffTimer"
+ "T@\"AXDispatchTimer\",&,N,V_sendPropertyUpdatesLowTimer"
+ "T@\"NSDictionary\",&,N,V_lastSentPropertyUpdates"
+ "T@\"NSMutableDictionary\",&,N,V_collectedPropertyUpdates"
+ "T@\"NSMutableDictionary\",C,V_state"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_relinquishCompleted"
+ "TB,N,V_liveListenComfortSoundsSwitch"
+ "TB,N,V_noiseDisabled"
+ "TB,V_hasStarted"
+ "TQ,V_deviceMessagePriority"
+ "TotalNoWakeCount"
+ "Tq,R,N,V_state"
+ "Tq,V_handoffReason"
+ "Tq,V_processingHandoff"
+ "Transition request interrupted, Nearby started: %d, isPaired: %d, BT available: %d, hasPeers: %d"
+ "UPDATE isLocal %d %@"
+ "Unregister from updates listenerHash: %@"
+ "UpdateState BT: %d, Paired: %d, Connected: %d, Connecting: %d"
+ "XPC received MessagesPriority isHigh: %d"
+ "XPC sending messagesPriority: Default"
+ "XPC sending messagesPriority: Urgent"
+ "XPC sending payload %@"
+ "_cleanupNearbyDeviceStateDuplicatesForDevice:"
+ "_collectedPropertyUpdates"
+ "_deviceMessagePriority"
+ "_handoffReason"
+ "_handoffTimer"
+ "_lastSentPropertyUpdates"
+ "_liveListenComfortSoundsSwitch"
+ "_noiseDisabled"
+ "_processingHandoff"
+ "_registerForNoiseEnabledPreferenceChange"
+ "_relinquishCompleted"
+ "_sendPropertyUpdatesLowTimer"
+ "checkConnectionRequestedForMediaAfterTimeout"
+ "checkConnectionRequestedForMediaAfterTimeout setHoldingMediaForConnection: NO"
+ "checkHandoffAfterTimeout"
+ "collectPropertyUpdatesFromPayload:"
+ "collectedPropertyUpdates"
+ "com.apple.hearing.hearingaids.connection"
+ "com.apple.hearing.hearingaids.priority"
+ "connectedPeer: %@, connectingPeer: %@"
+ "connectedPeerWithCompletion:"
+ "connectionStateForDevice %@ %@"
+ "connectionStateForDevice:"
+ "defaultDevicesFromDevices:"
+ "descriptionForCurrentMessagePriority"
+ "descriptionForHandoffState"
+ "descriptionForPriority:"
+ "deviceMessagePriority"
+ "devicesFromDevices:withMessagePriority:"
+ "finishHandoff"
+ "handleSessionMessage:completion:"
+ "handoffReason"
+ "handoffTimer"
+ "isPeerConnectedToHearingDevice"
+ "lastSentPropertyUpdates"
+ "liveListenComfortSoundsSwitch"
+ "logDevices:withTitle:fullInfo:"
+ "messagePriorityForDevice %@ %@"
+ "messagePriorityForDevice:"
+ "noiseDisabled"
+ "notificationForNoiseEnabled"
+ "processHandoffMessageFromPeer:state:"
+ "processPropertyUpdates:isLocal:"
+ "processStateMessageFromPeer:state:"
+ "processWriteMessageWithValue:"
+ "processingHandoff"
+ "relinquishCompleted"
+ "relinquishConnectionForReason: %@ to peer: %@"
+ "relinquishConnectionForReason:toDevice:"
+ "relinquishConnectionWithCompletion:"
+ "removeObjectsForKeys:"
+ "requestConnectionForMedia"
+ "requestHandoff:reason:"
+ "resetHandoffOnDeviceQueue"
+ "sendMessage:toDevices:messagePriority:"
+ "sendMessage:toDevicesWithDomain:excludingState:withPriority:"
+ "sendMessage:toWatchDevicesWithDomain:excludingState:withPriority:"
+ "sendMessage:toWatchDevicesWithDomain:withPriority:"
+ "sendMessageToAllDevices:messagePriority:"
+ "sendMessagesPriority:"
+ "sendMessagesPriorityDefault"
+ "sendMessagesPriorityHigh"
+ "sendNoiseMeasurementsDisabled:"
+ "sendNoiseMeasurementsDisabledIfNeeded"
+ "sendPropertyUpdatesLowTimer"
+ "sendStateMessage:toDevices:isUrgent:"
+ "sendStateMessageToAllDevices:isUrgent:"
+ "sendWriteToAllDevices Skip"
+ "sendWriteToAllDevices payload:\n%@"
+ "sentIDSMessage:domain:priority:priorityDescription:"
+ "setCollectedPropertyUpdates:"
+ "setConnectionState %@ %@"
+ "setConnectionState:forDevice:"
+ "setDeviceMessagePriority:"
+ "setHandoffReason:"
+ "setHandoffTimer:"
+ "setLastSentPropertyUpdates:"
+ "setLiveListenComfortSoundsSwitch:"
+ "setMessagePriority %@ %@"
+ "setMessagePriority: %@ for device: %@"
+ "setMessagePriority:forDevice:"
+ "setNoiseDisabled:"
+ "setProcessingHandoff:"
+ "setRelinquishCompleted:"
+ "setSendPropertyUpdatesLowTimer:"
+ "shouldRoute:"
+ "startComfortSounds"
+ "urgentDevicesFromDevices:"
+ "v28@0:8@16B24"
+ "v32@0:8q16@24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?>24"
+ "v48@0:8@16@24Q32@40"
+ "void pairedWithDevicesSupportingListeningModes(__strong AXBoolBlock _Nonnull)_block_invoke_2"
- "\x06"
- " %@ is LEA 2.0."
- "-[AXHAController setPairedHearingAidID:]_block_invoke"
- "-[AXHAController setPairedHearingAidID:]_block_invoke_2"
- "-[AXHeardController startServer]_block_invoke_28"
- "-[HUComfortSoundsController init]_block_invoke_3"
- "-[HUNearbyHearingAidController device:didReceiveMessage:]_block_invoke_2"
- "-[HUNearbyHearingAidController processStateMessageFromPeer:state:response:]"
- "-[HUNearbyHearingAidController processWriteMessageWithValue:response:]"
- "-[HUNearbyHearingAidController processWriteMessageWithValue:response:]_block_invoke"
- "-[HUNearbyHearingAidController requestConnectionForReason:]_block_invoke"
- "3\x14"
- "After timeout, gave up on media handoff, transiton connection to peer"
- "Already Processing Handoff, Skip"
- "B36@0:8q16@24B32"
- "Bluetooth isn't available. Not requesting connection."
- "Can't connect to paired hearing device: %@ %@ isiCloudPaired: %@"
- "Can't request connection, BT is off"
- "Checking connection"
- "Connect to paired hearing device: %@ %@ isiCloudPaired: %@"
- "Connection processing has been finished"
- "Discovered new devices: %@, all devices: %@"
- "Headphone is selected, processing Accessory info"
- "Hearing Aids connected to 2 devices, state: %@, connectedPeer: %@, Disconnect"
- "Hearing Aids connected, state: %@, PeerState: PeerConnected, Relinquishing connection"
- "IDS Sending(%@) %@ to %@ with %@"
- "NearbyController relinquishConnection"
- "NearbyController requestConnection"
- "No connected/connecting peer. Connecting %@"
- "No peers, connect to paired HA"
- "Peers Discovered, sending CheckIn and ControllerConnected state: %@ to Devices: %@"
- "Received CheckIn for device: %@"
- "Relinquish connection to peer reason: %@"
- "Requesting %@"
- "Requesting connection from %ld - %@"
- "Reset Transitioning State"
- "Sending ConnectWithReason: %@ to all devices"
- "Sending ConnectWithReason: %@ to device: %@"
- "Sending ControllerConnectWithReason %ld to %@, time: %@"
- "Sending ControllerConnected: %@"
- "Sending payload %@"
- "Should relinquish: %d Reason: %@, Call: [pending: %d, active: %d, endpoint: %d]"
- "Should request connection %d, %d, %d, %d, %d, %d"
- "T@\"AXDispatchTimer\",&,N,V_relinquishConnectionTimer"
- "T@\"AXDispatchTimer\",&,N,V_requestConnectionTimer"
- "T@\"NSMutableDictionary\",&,N,V_state"
- "TB,N,V_hasStarted"
- "TB,V_processingConnection"
- "TB,V_processingTransition"
- "Timeout check for requesting connection from Peer, state: %@"
- "Transition didn't happen, Connecting back"
- "Transition didn't happen, but can't connect back BT: %@, HA: %@"
- "Transition processing has been finished"
- "Transition timeout check connectedPeer: %@"
- "UPDATE %@"
- "Update peers, sending ControllerConnected: %@"
- "Update state to Peer and Disconnect, connected peer: %@"
- "Updated state: %@"
- "Updating state to %@"
- "We shouldn't be connected"
- "_processingConnection"
- "_processingTransition"
- "_relinquishConnectionTimer"
- "_requestConnectionTimer"
- "allowHearingAidControlOnLockScreen"
- "checkConnectionPeers:"
- "checkConnectionRelinquishedAfterTimeout"
- "checkConnectionRelinquishedAfterTimeout setHoldingMediaForConnection: NO"
- "checkConnectionRequestedAfterTimeout"
- "checkConnectionRequestedAfterTimeout setHoldingMediaForConnection: NO"
- "checkConnectionToHearingDevice:"
- "getConnectedPeer:"
- "handleSessionMessage:"
- "logNewDevices:"
- "old state: %@, new state: %@"
- "peerHasConnectionToHearingDevice"
- "processStateMessageFromPeer:state:response:"
- "processWriteMessageWithValue:response:"
- "processingConnection"
- "processingTransition"
- "relinquishConnectionForReason:"
- "relinquishConnectionForReason:toDevice:sendHandoffMessage:"
- "relinquishConnectionTimer"
- "requestConnectionTimer"
- "requestHandoffForMedia"
- "screenUnlocked - Sending ControllerConnected: %@"
- "sendConnectionUpdateToPeers, new State: %@"
- "sendConnectionUpdateToPeers, old State: %@"
- "sendMessageToAllDevices:"
- "sendMessageToWatchDevices:toDevicesWithDomain:withPriority:"
- "sendStateMessage:toDevices:"
- "sendStateMessageToAllDevices:"
- "sentIDSMessage:domain:"
- "setAllowHearingAidControlOnLockScreen:"
- "setProcessingConnection:"
- "setProcessingTransition:"
- "setRelinquishConnectionTimer:"
- "setRequestConnectionTimer:"
- "updateForBluetoothStateChange"
- "updateState isPairedAndConnected: %d, isPairedAndConnecting: %d"
- "v20@?0B8@\"HUNearbyDevice\"12"
- "void pairedWithDevicesSupportingListeningModes(__strong AXBoolBlock _Nonnull)_block_invoke"

```
