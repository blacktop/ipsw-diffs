## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-495.0.0.0.0
-  __TEXT.__text: 0xa8838
+496.2.0.0.0
+  __TEXT.__text: 0x991a0
   __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x7d4c
-  __TEXT.__const: 0x3da
-  __TEXT.__gcc_except_tab: 0x31a8
-  __TEXT.__cstring: 0xe61b
-  __TEXT.__oslogstring: 0x35fd
+  __TEXT.__objc_methlist: 0x7d6c
+  __TEXT.__const: 0x40a
+  __TEXT.__gcc_except_tab: 0x2938
+  __TEXT.__cstring: 0x4eab
+  __TEXT.__oslogstring: 0x7e38
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__unwind_info: 0x25d0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x841
-  __TEXT.__objc_methname: 0x141ff
+  __TEXT.__objc_methname: 0x14230
   __TEXT.__objc_methtype: 0x2183
-  __TEXT.__objc_stubs: 0xed40
-  __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x3430
+  __TEXT.__objc_stubs: 0xed60
+  __DATA_CONST.__got: 0x620
+  __DATA_CONST.__const: 0x3458
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4970
+  __DATA_CONST.__objc_selrefs: 0x4980
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
   __AUTH_CONST.__auth_got: 0x898
   __AUTH_CONST.__const: 0xd98
-  __AUTH_CONST.__cfstring: 0x8e80
+  __AUTH_CONST.__cfstring: 0x5200
   __AUTH_CONST.__objc_const: 0xa5d8
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x410
-  __AUTH_CONST.__objc_doubleobj: 0x1240
+  __AUTH_CONST.__objc_doubleobj: 0x1290
   __AUTH.__objc_data: 0xfa8
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x8f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0E589D58-EEDF-3DB4-AB95-6F2C22F00D99
-  Functions: 3531
-  Symbols:   11395
-  CStrings:  6844
+  UUID: 5C2EA768-6CEA-31EF-824D-480D4E03CB0A
+  Functions: 3585
+  Symbols:   11533
+  CStrings:  6025
 
Symbols:
+ -[AXHeardController isTransparencyUpdatePending]
+ -[AXHearingAidDevice peripheral:didDiscoverCharacteristicsForService:error:].cold.1
+ -[AXHearingAidDevice peripheral:didDiscoverServices:].cold.2
+ -[AXHearingAidDevice peripheral:didWriteValueForCharacteristic:error:].cold.1
+ -[AXHearingAidDevice updateBatteryServiceForPeripheral:].cold.1
+ -[AXHearingAidDevice updateBatteryServiceForPeripheral:].cold.2
+ -[AXHearingAidDevice writeValueForProperty:].cold.1
+ -[AXHearingAidDevice writeValueForProperty:].cold.2
+ -[AXHearingAidDeviceController centralManager:didFailToConnectPeripheral:error:].cold.1
+ -[HANanoSettings _valueForPreferenceKey:].cold.1
+ -[HANanoSettings setValue:forPreferenceKey:].cold.1
+ -[HUComfortSound nextFilePath].cold.2
+ -[HUComfortSoundsAssetManager assetController:didFinishRefreshingAssets:wasSuccessful:error:].cold.1
+ -[HUComfortSoundsController assetDownloadDidUpdate].cold.1
+ -[HUComfortSoundsController availableAssetsDidUpdate].cold.1
+ -[HUComfortSoundsController mediaServerDied].cold.1
+ -[HUComfortSoundsController nextFileToPlay].cold.1
+ -[HUComfortSoundsController nextFileToPlay].cold.2
+ -[HUComfortSoundsController playOnQueue].cold.1
+ -[HUComfortSoundsController playOnQueue].cold.2
+ -[HUComfortSoundsController playOnQueue].cold.3
+ -[HUComfortSoundsController playOnQueue].cold.4
+ -[HUComfortSoundsController playOnQueue].cold.5
+ -[HUComfortSoundsController playOnQueue].cold.6
+ -[HUComfortSoundsController playOnQueue].cold.7
+ -[HUComfortSoundsController scheduleFile].cold.1
+ -[HUComfortSoundsController scheduleFile].cold.2
+ -[HUComfortSoundsController setupTimerIfEnabled].cold.1
+ -[HUComfortSoundsController setupTimerIfNeeded].cold.1
+ -[HUComfortSoundsSettings selectedComfortSound].cold.1
+ -[HUComfortSoundsSettings setSelectedComfortSound:].cold.1
+ -[HUComfortSoundsSettings setTimerInHoursAndMinutes:minutes:].cold.1
+ -[HUComfortSoundsSettings setTinnitusFilterPoint:].cold.1
+ -[HUComfortSoundsSettings tinnitusFilterPoint].cold.1
+ -[HUHearingAidSettings shouldUseiCloud].cold.1
+ -[HUHearingSettings hearingControlCenterOrder].cold.1
+ -[HUHearingSettings hearingControlCenterOrder].cold.2
+ -[HUHearingSettings setHearingControlCenterOrder:].cold.1
+ -[HUNearbyHearingAidController mediaServerDied].cold.1
+ -[HUNearbyLiveListenControllerWatch _handleStateChangedMessage:].cold.1
+ -[HUNoiseController calculateLeqForBuffer:].cold.1
+ -[HUNoiseController checkToResetAnalyticsNotificationsForSPL:withDuration:andBuffer:forTime:andThreshold:].cold.1
+ -[HUNoiseController checkToResetNotificationsForSPL:withDuration:andBuffer:forTime:].cold.1
+ -[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:].cold.1
+ -[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:].cold.1
+ -[HUNoiseController maintainCircularBuffer:forTime:].cold.1
+ -[HUUtilities deviceIsCounterfeit:]
+ -[HUUtilities deviceIsCounterfeit:].cold.1
+ GCC_except_table152
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table93
+ _HCLogAudioAccommodations
+ _HCLogComfortSounds
+ _HCLogHearing
+ _HCLogHearingAids
+ _HCLogHearingProtection
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.428
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.432
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.440
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.449
+ ___22-[AXHAController init]_block_invoke.21
+ ___25-[HUNoiseController init]_block_invoke.312
+ ___28-[HUHearingAidSettings init]_block_invoke.76
+ ___32-[AXHeardController startServer]_block_invoke_35.cold.1
+ ___33-[HUComfortSoundsController init]_block_invoke.16
+ ___33-[HUComfortSoundsController init]_block_invoke.21
+ ___33-[HUComfortSoundsController init]_block_invoke.25
+ ___33-[HUComfortSoundsController init]_block_invoke.29
+ ___33-[HUComfortSoundsController init]_block_invoke.6
+ ___33-[HUComfortSoundsController init]_block_invoke.8
+ ___33-[HUComfortSoundsController init]_block_invoke_2.20
+ ___33-[HUComfortSoundsController init]_block_invoke_2.24
+ ___33-[HUComfortSoundsController init]_block_invoke_2.28
+ ___33-[HUComfortSoundsController init]_block_invoke_2.32
+ ___33-[HUComfortSoundsController init]_block_invoke_2.9
+ ___34-[AXHeardController continueSetup]_block_invoke.115
+ ___34-[AXHeardController continueSetup]_block_invoke.116
+ ___34-[AXHeardController continueSetup]_block_invoke.147
+ ___34-[AXHeardController continueSetup]_block_invoke_2.119
+ ___34-[HURoutesManager mediaServerDied]_block_invoke.cold.1
+ ___36-[AXHeardController updateAnalytics]_block_invoke.197
+ ___37-[HUNearbyHearingAidController start]_block_invoke.100
+ ___37-[HUNearbyHearingAidController start]_block_invoke.83
+ ___37-[HUNearbyHearingAidController start]_block_invoke.95
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.101
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.96
+ ___37-[HUNearbyHearingAidController start]_block_invoke_3.103
+ ___37-[HUNearbyHearingAidController start]_block_invoke_4.104
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.390
+ ___40-[AXHeardController _shutdownIfPossible]_block_invoke.152
+ ___41-[AXHeardController handleNewConnection:]_block_invoke.224
+ ___41-[AXHeardController handleNewConnection:]_block_invoke_2.225
+ ___41-[AXHeardController handleNewConnection:]_block_invoke_2.cold.1
+ ___41-[AXHeardController handleNewConnection:]_block_invoke_2.cold.2
+ ___41-[AXHearingAidDevice connectionDidChange]_block_invoke.148
+ ___41-[AXHearingAidDevice connectionDidChange]_block_invoke.152
+ ___41-[AXHearingAidDevice connectionDidChange]_block_invoke.155
+ ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.139
+ ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.cold.1
+ ___43-[AXHeardController sendMessage:withError:]_block_invoke.cold.1
+ ___44-[AXHearingAidDevice loadRequiredProperties]_block_invoke.170
+ ___46-[AXHearingAidDevice updateInputTagsAndReset:]_block_invoke.244
+ ___47-[HUDeviceController device:didUpdateProperty:]_block_invoke.11
+ ___47-[HUDeviceController device:didUpdateProperty:]_block_invoke.14
+ ___49-[AXRemoteHearingAidDevice setValue:forProperty:]_block_invoke.72
+ ___49-[HUNearbyLiveListenControlleriOS _nearbyDevices]_block_invoke.34
+ ___49-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke.21
+ ___50-[HUNoiseController showNotificationForAlertType:]_block_invoke.cold.1
+ ___51-[HUNearbyLiveListenControllerWatch startObserving]_block_invoke.6
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.485
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.485.cold.1
+ ___52-[AXHearingAidDeviceController connectToPeripheral:]_block_invoke.35
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.33
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.36
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.37
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.40
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.43
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke_2.44
+ ___52-[HUNoiseController writeAttentuationSampleToHealth]_block_invoke.cold.1
+ ___53-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke.63
+ ___53-[AXHeardController sendUpdateMessage:forIdentifier:]_block_invoke_2.cold.1
+ ___53-[AXHeardController updateHearingControlCenterModule]_block_invoke.101
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.401
+ ___54-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke.76
+ ___54-[HULiveListenController stopListeningWithCompletion:]_block_invoke.cold.1
+ ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke.25
+ ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_2.26
+ ___56-[AXHearingAidDeviceController cancelPendingConnections]_block_invoke.37
+ ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.74
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke.47
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke.54
+ ___56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke.74
+ ___57-[AXHeardController connection:hasEntitlementForMessage:]_block_invoke.cold.1
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.290
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.294
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.299
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.291
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.295
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_3.292
+ ___57-[HUNearbyHearingAidController requestConnectionForMedia]_block_invoke.28
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.96
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.97
+ ___59-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke.26
+ ___61-[AXHeardController sendClientsMessageWithPayload:excluding:]_block_invoke_2.cold.1
+ ___61-[AXHearingAidDeviceController setupCentralManagerForLEAudio]_block_invoke.cold.1
+ ___63-[HUAccessoryManager getPairedDeviceSupportsHearingProtection:]_block_invoke.69
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.103
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.104
+ ___65-[HUNearbyLiveListenControllerWatch _receivedMessage:fromDevice:]_block_invoke.cold.1
+ ___67-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]_block_invoke.168
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.31
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.32
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.37
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2.39
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.45
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.55
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.56
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.61
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.60
+ ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke.45
+ ___69-[HUAccessoryHearingSyncManager sendListeningModesIDSMessageIfNeeded]_block_invoke.79
+ ___69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke.154
+ ___69-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke.138
+ ___69-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke.138.cold.1
+ ___71-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke.78
+ ___73-[HUNearbyLiveListenControlleriOS _handleStateChangedMessage:fromDevice:]_block_invoke.cold.1
+ ___74-[HUNoiseController writeNotificationSampleToHKWithSPL:startDate:endDate:]_block_invoke.cold.1
+ ___76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke.38
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.411
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.416
+ ___93-[HUComfortSoundsAssetManager assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.10
+ ____LiveListenSendUserNotification_block_invoke.41
+ ____LiveListenSendUserNotification_block_invoke.cold.1
+ ___block_descriptor_56_e8_32s40bs48r_e25_v32?0"CBDevice"8Q16^B24ls32l8s40l8r48l8
+ ___block_literal_global.104
+ ___block_literal_global.109
+ ___block_literal_global.112
+ ___block_literal_global.119
+ ___block_literal_global.12
+ ___block_literal_global.132
+ ___block_literal_global.150
+ ___block_literal_global.178
+ ___block_literal_global.199
+ ___block_literal_global.200
+ ___block_literal_global.208
+ ___block_literal_global.210
+ ___block_literal_global.217
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.236
+ ___block_literal_global.237
+ ___block_literal_global.238
+ ___block_literal_global.24
+ ___block_literal_global.246
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.366
+ ___block_literal_global.389
+ ___block_literal_global.39
+ ___block_literal_global.40
+ ___block_literal_global.41
+ ___block_literal_global.42
+ ___block_literal_global.434
+ ___block_literal_global.44
+ ___block_literal_global.442
+ ___block_literal_global.451
+ ___block_literal_global.461
+ ___block_literal_global.465
+ ___block_literal_global.47
+ ___block_literal_global.501
+ ___block_literal_global.51
+ ___block_literal_global.55
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___block_literal_global.70
+ ___block_literal_global.71
+ ___block_literal_global.76
+ ___block_literal_global.82
+ ___block_literal_global.88
+ _objc_msgSend$deviceIsCounterfeit:
+ _sharedInstance.Settings.363
+ _sharedInstance.onceToken.364
- GCC_except_table151
- GCC_except_table85
- GCC_except_table91
- _CSEngineeringLog
- _CSInitializeLogging
- _HAEngineeringLog
- _HAInitializeLogging
- _HCHPEngineeringLog
- _HCHPInitializeLogging
- _HearingEngineeringLog
- _HearingInitializeLogging
- _PAEngineeringLog
- _PAInitializeLogging
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.536
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.549
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.557
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.566
- ___22-[AXHAController init]_block_invoke.28
- ___25-[HUNoiseController init]_block_invoke.325
- ___28-[HUHearingAidSettings init]_block_invoke.83
- ___33-[HUComfortSoundsController init]_block_invoke.22
- ___33-[HUComfortSoundsController init]_block_invoke.36
- ___33-[HUComfortSoundsController init]_block_invoke.40
- ___33-[HUComfortSoundsController init]_block_invoke.47
- ___33-[HUComfortSoundsController init]_block_invoke.54
- ___33-[HUComfortSoundsController init]_block_invoke.61
- ___33-[HUComfortSoundsController init]_block_invoke_2.23
- ___33-[HUComfortSoundsController init]_block_invoke_2.43
- ___33-[HUComfortSoundsController init]_block_invoke_2.50
- ___33-[HUComfortSoundsController init]_block_invoke_2.57
- ___33-[HUComfortSoundsController init]_block_invoke_2.64
- ___34-[AXHeardController continueSetup]_block_invoke.137
- ___34-[AXHeardController continueSetup]_block_invoke.141
- ___34-[AXHeardController continueSetup]_block_invoke.176
- ___34-[AXHeardController continueSetup]_block_invoke_2.144
- ___36-[AXHeardController updateAnalytics]_block_invoke.246
- ___37-[HUNearbyHearingAidController start]_block_invoke.102
- ___37-[HUNearbyHearingAidController start]_block_invoke.116
- ___37-[HUNearbyHearingAidController start]_block_invoke.121
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.117
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.122
- ___37-[HUNearbyHearingAidController start]_block_invoke_3.124
- ___37-[HUNearbyHearingAidController start]_block_invoke_4.125
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.414
- ___40-[AXHeardController _shutdownIfPossible]_block_invoke.193
- ___41-[AXHeardController handleNewConnection:]_block_invoke.288
- ___41-[AXHeardController handleNewConnection:]_block_invoke_2.289
- ___41-[AXHearingAidDevice connectionDidChange]_block_invoke.160
- ___41-[AXHearingAidDevice connectionDidChange]_block_invoke.167
- ___41-[AXHearingAidDevice connectionDidChange]_block_invoke.170
- ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.172
- ___44-[AXHearingAidDevice loadRequiredProperties]_block_invoke.224
- ___46-[AXHearingAidDevice updateInputTagsAndReset:]_block_invoke.319
- ___47-[HUDeviceController device:didUpdateProperty:]_block_invoke.19
- ___47-[HUDeviceController device:didUpdateProperty:]_block_invoke.22
- ___49-[AXRemoteHearingAidDevice setValue:forProperty:]_block_invoke.102
- ___49-[HUNearbyLiveListenControlleriOS _nearbyDevices]_block_invoke.68
- ___49-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke.46
- ___51-[HUNearbyLiveListenControllerWatch startObserving]_block_invoke.16
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.639
- ___52-[AXHearingAidDeviceController connectToPeripheral:]_block_invoke.84
- ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.71
- ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.80
- ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.84
- ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.87
- ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.90
- ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke_2.91
- ___53-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke.116
- ___53-[AXHeardController updateHearingControlCenterModule]_block_invoke.111
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.440
- ___54-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke.135
- ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke.50
- ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_2.51
- ___56-[AXHearingAidDeviceController cancelPendingConnections]_block_invoke.92
- ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.127
- ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke.107
- ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke.97
- ___56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke.90
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.470
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.477
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.488
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.471
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.478
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_3.472
- ___57-[HUNearbyHearingAidController requestConnectionForMedia]_block_invoke.44
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.256
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.260
- ___59-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke.42
- ___63-[HUAccessoryManager getPairedDeviceSupportsHearingProtection:]_block_invoke.74
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.170
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.174
- ___67-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]_block_invoke.219
- ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.53
- ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.54
- ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.62
- ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2.64
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.108
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.91
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.99
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.103
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.92
- ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke.88
- ___69-[HUAccessoryHearingSyncManager sendListeningModesIDSMessageIfNeeded]_block_invoke.153
- ___69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke.220
- ___69-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke.174
- ___69-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke.174.cold.1
- ___71-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke.146
- ___76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke.54
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.480
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.500
- ___93-[HUComfortSoundsAssetManager assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.26
- ____LiveListenSendUserNotification_block_invoke.53
- ___block_literal_global.100
- ___block_literal_global.102
- ___block_literal_global.108
- ___block_literal_global.114
- ___block_literal_global.126
- ___block_literal_global.128
- ___block_literal_global.140
- ___block_literal_global.146
- ___block_literal_global.151
- ___block_literal_global.179
- ___block_literal_global.209
- ___block_literal_global.224
- ___block_literal_global.227
- ___block_literal_global.244
- ___block_literal_global.25
- ___block_literal_global.259
- ___block_literal_global.261
- ___block_literal_global.263
- ___block_literal_global.265
- ___block_literal_global.272
- ___block_literal_global.29
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.321
- ___block_literal_global.334
- ___block_literal_global.349
- ___block_literal_global.362
- ___block_literal_global.404
- ___block_literal_global.420
- ___block_literal_global.49
- ___block_literal_global.550
- ___block_literal_global.551
- ___block_literal_global.559
- ___block_literal_global.56
- ___block_literal_global.568
- ___block_literal_global.596
- ___block_literal_global.606
- ___block_literal_global.66
- ___block_literal_global.685
- ___block_literal_global.74
- ___block_literal_global.83
- ___block_literal_global.86
- ___block_literal_global.90
- ___block_literal_global.92
- ___block_literal_global.97
- ___block_literal_global.98
- _sharedInstance.Settings.417
- _sharedInstance.onceToken.418
CStrings:
+ "Couldn't find SSL state for address %@"
+ "Device is nil. Can't check for counterfeit status."
+ "Found SSL Enabled %d for address %@"
+ "Found device: %@ for current route: %@"
+ "Ignoring IDS message to update hearing protection: %@"
+ "deviceIsCounterfeit:"
+ "isTransparencyUpdatePending"
- "%s:%d %@"
- "%{public}s"
- "-[AVAudioSession(HUAudioSession) setActive:forFeature:error:]"
- "-[AXFakeHearingAidDevice writeInt:toEar:forProperty:]"
- "-[AXHAController _registerForLiveListenUpdates_enumValue:]"
- "-[AXHAController currentDeviceController]"
- "-[AXHAController hearingAidsIsLEA2:]"
- "-[AXHAController hearingAidsPaired]"
- "-[AXHAController init]_block_invoke"
- "-[AXHAController processPropertyUpdates:isLocal:]"
- "-[AXHAController readAvailableControllers:]"
- "-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke"
- "-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke_2"
- "-[AXHAController registerForDeviceUpdates:]"
- "-[AXHAController setListenForAvailableDeviceUpdates:]_block_invoke"
- "-[AXHAController setListenForAvailableDeviceUpdates:]_block_invoke_2"
- "-[AXHAController setPairedHearingAidID:]"
- "-[AXHAController writeDeviceProperty:]"
- "-[AXHAServer _unregisterUpdateListenerHash:]"
- "-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke"
- "-[AXHAServer handleMessageWithPayload:forIdentifier:]"
- "-[AXHAServer reregisterForComfortSoundsAssetsUpdatesIfNeeded]"
- "-[AXHAServer sendMessagesPriorityDefault]"
- "-[AXHAServer sendMessagesPriorityHigh]"
- "-[AXHAServer unregisterAvailableDevicesListener:]"
- "-[AXHAServer unregisterPropertyUpdateListener:]"
- "-[AXHAServer writeValue:forProperty:andDeviceID:]"
- "-[AXHeardController _shutdownIfPossible]_block_invoke"
- "-[AXHeardController boostPriority:]"
- "-[AXHeardController connection:hasEntitlementForMessage:]_block_invoke"
- "-[AXHeardController continueSetup]_block_invoke"
- "-[AXHeardController continueSetup]_block_invoke_3"
- "-[AXHeardController continueSetup]_block_invoke_4"
- "-[AXHeardController countOfClientsListeningForIdentifier:]"
- "-[AXHeardController handleMessage:forIdentifier:]"
- "-[AXHeardController handleNewConnection:]_block_invoke"
- "-[AXHeardController handleNewConnection:]_block_invoke_2"
- "-[AXHeardController handleNewConnection:]_block_invoke_5"
- "-[AXHeardController sendClientsMessageWithPayload:excluding:]_block_invoke_2"
- "-[AXHeardController sendMessage:withError:]_block_invoke"
- "-[AXHeardController sendUpdateMessage:forIdentifier:]_block_invoke_2"
- "-[AXHeardController shutdownIfPossible]"
- "-[AXHeardController startServer]_block_invoke_35"
- "-[AXHeardController updateAnalytics]"
- "-[AXHeardController updateAnalytics]_block_invoke_2"
- "-[AXHeardController updateHearingControlCenterModule]"
- "-[AXHeardController updateHearingControlCenterModule]_block_invoke"
- "-[AXHeardController updatePersonalAudioSettingsOnAccessories]"
- "-[AXHearingAidDevice _sendDelayedWrites]"
- "-[AXHearingAidDevice addPeripheral:]"
- "-[AXHearingAidDevice addPeripheral:asLeft:]"
- "-[AXHearingAidDevice connectionDidChange]_block_invoke"
- "-[AXHearingAidDevice delayWriteProperty:forPeripheral:]_block_invoke"
- "-[AXHearingAidDevice deviceDescription]"
- "-[AXHearingAidDevice didLoadBasicProperties]"
- "-[AXHearingAidDevice didLoadOptionalBasicProperties]"
- "-[AXHearingAidDevice didLoadOptionalBasicProperties]_block_invoke"
- "-[AXHearingAidDevice didLoadRequiredProperties]"
- "-[AXHearingAidDevice initWithLeftDevice:andRightDevice:]"
- "-[AXHearingAidDevice loadFailedProperties]"
- "-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]"
- "-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]_block_invoke_2"
- "-[AXHearingAidDevice loadRequiredProperties]_block_invoke"
- "-[AXHearingAidDevice mateWithDevice:]"
- "-[AXHearingAidDevice pairingDidCompleteForPeripheral:]_block_invoke"
- "-[AXHearingAidDevice peripheral:didDiscoverCharacteristicsForService:error:]"
- "-[AXHearingAidDevice peripheral:didDiscoverServices:]"
- "-[AXHearingAidDevice peripheral:didDiscoverServices:]_block_invoke"
- "-[AXHearingAidDevice peripheral:didInvalidateServices:]"
- "-[AXHearingAidDevice peripheral:didModifyServices:]"
- "-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]"
- "-[AXHearingAidDevice peripheral:didUpdateValueForCharacteristic:error:]"
- "-[AXHearingAidDevice peripheral:didWriteValueForCharacteristic:error:]"
- "-[AXHearingAidDevice peripheralDidUnpair:]"
- "-[AXHearingAidDevice readValueForCharacteristic:fromPeripheral:]"
- "-[AXHearingAidDevice setKeepInSync:]"
- "-[AXHearingAidDevice setNotify:forPeripheral:]"
- "-[AXHearingAidDevice setValue:forProperty:]"
- "-[AXHearingAidDevice swapPeripheral:toEar:]"
- "-[AXHearingAidDevice updateBatteryServiceForPeripheral:]"
- "-[AXHearingAidDevice updateInputTagsAndReset:]_block_invoke"
- "-[AXHearingAidDevice updateName]"
- "-[AXHearingAidDevice valueForProperty:]"
- "-[AXHearingAidDevice watchWristOrientationDidChange:]"
- "-[AXHearingAidDevice writeInt:toEar:forProperty:]"
- "-[AXHearingAidDevice writeSignedInt:toEar:forProperty:]"
- "-[AXHearingAidDevice writeValueForProperty:]"
- "-[AXHearingAidDeviceController cancelPendingConnections]"
- "-[AXHearingAidDeviceController centralManager:didConnectPeripheral:]"
- "-[AXHearingAidDeviceController centralManager:didDiscoverPeripheral:advertisementData:RSSI:]"
- "-[AXHearingAidDeviceController centralManager:didFailToConnectPeripheral:error:]"
- "-[AXHearingAidDeviceController centralManager:didRetrieveConnectedPeripherals:]"
- "-[AXHearingAidDeviceController centralManager:didRetrievePeripherals:]"
- "-[AXHearingAidDeviceController centralManagerDidUpdateState:]"
- "-[AXHearingAidDeviceController checkPartiallyPairedWithCompletion:]"
- "-[AXHearingAidDeviceController checkPartiallyPairedWithCompletion:]_block_invoke_2"
- "-[AXHearingAidDeviceController clearMissingHearingAids]_block_invoke_3"
- "-[AXHearingAidDeviceController connectToPeripheral:]_block_invoke"
- "-[AXHearingAidDeviceController deviceDidFinishLoading:]"
- "-[AXHearingAidDeviceController disconnectFromPeripheral:]"
- "-[AXHearingAidDeviceController isConnected]_block_invoke"
- "-[AXHearingAidDeviceController isConnecting]_block_invoke"
- "-[AXHearingAidDeviceController mergeDevice:withDevice:]"
- "-[AXHearingAidDeviceController pairedHearingAidsDidChange]"
- "-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke"
- "-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke_4"
- "-[AXHearingAidDeviceController pairingAgent:peerDidCompletePairing:]"
- "-[AXHearingAidDeviceController pairingAgent:peerDidFailToCompletePairing:error:]"
- "-[AXHearingAidDeviceController pairingAgent:peerDidUnpair:]"
- "-[AXHearingAidDeviceController replaceDevice:withDevice:]"
- "-[AXHearingAidDeviceController resetConnectionToPeripheral:]"
- "-[AXHearingAidDeviceController scanningServiceUUIDs]_block_invoke"
- "-[AXHearingAidDeviceController searchForAvailableDevices]"
- "-[AXHearingAidDeviceController searchForAvailableDevices]_block_invoke_2"
- "-[AXHearingAidDeviceController sendRequestToCentralManager:]"
- "-[AXHearingAidDeviceController shouldRelinquishForPartialConnection]"
- "-[AXHearingAidDeviceController stopSearching]"
- "-[AXHearingAidDeviceController unpairPeripheralWithUUID:]"
- "-[AXHearingAidDeviceController unpairPeripheralWithUUID:]_block_invoke"
- "-[AXRemoteHearingAidDevice _updateSelectedProgramsProperties]"
- "-[AXRemoteHearingAidDevice _valueForProperty:]"
- "-[AXRemoteHearingAidDevice _writeAllProgramSelectionsToPeripheral]"
- "-[AXRemoteHearingAidDevice checkDidLoadProperties:]"
- "-[AXRemoteHearingAidDevice connect]"
- "-[AXRemoteHearingAidDevice disconnectAndUnpair:]"
- "-[AXRemoteHearingAidDevice setKeepInSync:]"
- "-[AXRemoteHearingAidDevice setValue:forProperty:]"
- "-[CBPeripheral(_AX_HA_) axTag:]"
- "-[CBPeripheral(_AX_HA_) axUntag:]"
- "-[HANanoSettings _valueForPreferenceKey:]"
- "-[HANanoSettings setValue:forPreferenceKey:]"
- "-[HUAccessoryHearingSettings activeHearingProtectionAvailableForAddress:]"
- "-[HUAccessoryHearingSettings logMessage:]"
- "-[HUAccessoryHearingSyncManager _initCachedEnabled]"
- "-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke"
- "-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2"
- "-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_3"
- "-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke"
- "-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2"
- "-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_3"
- "-[HUAccessoryHearingSyncManager _sendIDSMessageIfNeededForListeningModes:addresses:force:]"
- "-[HUAccessoryHearingSyncManager deviceState]"
- "-[HUAccessoryHearingSyncManager hasPairedDevicesWithListeningModes]"
- "-[HUAccessoryHearingSyncManager init]_block_invoke_3"
- "-[HUAccessoryHearingSyncManager listeningModeDidChange:]"
- "-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke"
- "-[HUAccessoryHearingSyncManager processNoiseMeasurementsDisabledMessage:fromDevice:]"
- "-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke"
- "-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke_2"
- "-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke_2"
- "-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]"
- "-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke"
- "-[HUAccessoryManager getPairedDeviceSupportsHearingProtection:]_block_invoke"
- "-[HUAccessoryManager pseVersionForAddress:]"
- "-[HUAccessoryManager pseVersionForAddress:]_block_invoke"
- "-[HUComfortSound nextFilePath]"
- "-[HUComfortSoundsAssetManager assetController:didFinishDownloadingAsset:wasSuccessful:error:hasRemainingDownloads:]"
- "-[HUComfortSoundsAssetManager assetController:didFinishPurgingAssets:wasSuccessful:error:]"
- "-[HUComfortSoundsAssetManager assetController:didFinishRefreshingAssets:wasSuccessful:error:]"
- "-[HUComfortSoundsAssetManager assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke"
- "-[HUComfortSoundsAssetManager downloadAssetWithId:]_block_invoke"
- "-[HUComfortSoundsAssetManager refreshAssets]"
- "-[HUComfortSoundsController assetDownloadDidUpdate]"
- "-[HUComfortSoundsController audioEngineWasInterrupted:]"
- "-[HUComfortSoundsController audioEngineWasInterrupted:]_block_invoke"
- "-[HUComfortSoundsController audioSessionWasInterrupted:]"
- "-[HUComfortSoundsController availableAssetsDidUpdate]"
- "-[HUComfortSoundsController calculateVolumeForSessionWithCompletion:]_block_invoke"
- "-[HUComfortSoundsController callStatusDidChange:]_block_invoke"
- "-[HUComfortSoundsController clearActiveRoute]"
- "-[HUComfortSoundsController deviceScreenStatusDidChange:systemLocked:]"
- "-[HUComfortSoundsController endTimeStamp]"
- "-[HUComfortSoundsController handlePlaybackForDifferentCategory]"
- "-[HUComfortSoundsController handlePlaybackForSameCategory]"
- "-[HUComfortSoundsController hasCurrentCall]"
- "-[HUComfortSoundsController init]"
- "-[HUComfortSoundsController init]_block_invoke"
- "-[HUComfortSoundsController init]_block_invoke_2"
- "-[HUComfortSoundsController init]_block_invoke_4"
- "-[HUComfortSoundsController invalidateTimer]"
- "-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke"
- "-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke_6"
- "-[HUComfortSoundsController listenForChangesInTimer]_block_invoke"
- "-[HUComfortSoundsController listenForChangesInTimer]_block_invoke_2"
- "-[HUComfortSoundsController logMessageForTimer:]"
- "-[HUComfortSoundsController mediaPlaybackDidChange:]"
- "-[HUComfortSoundsController mediaServerDied]"
- "-[HUComfortSoundsController mediaServerDied]_block_invoke"
- "-[HUComfortSoundsController nextFileToPlay]"
- "-[HUComfortSoundsController playOnQueue]"
- "-[HUComfortSoundsController processComfortSoundsControlRequest:]_block_invoke_2"
- "-[HUComfortSoundsController rampNodeVolume:from:to:fadeDuration:withProgress:]"
- "-[HUComfortSoundsController registerHasBlankedScreenNotification]"
- "-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke"
- "-[HUComfortSoundsController routesDidChange:]"
- "-[HUComfortSoundsController scheduleFile]"
- "-[HUComfortSoundsController scheduleFile]_block_invoke"
- "-[HUComfortSoundsController scheduleFile]_block_invoke_2"
- "-[HUComfortSoundsController scheduleTimer:]"
- "-[HUComfortSoundsController scheduleTimer:]_block_invoke"
- "-[HUComfortSoundsController setPreviewEnabled:]"
- "-[HUComfortSoundsController setVolume:forNode:andRamp:]"
- "-[HUComfortSoundsController setupTimerIfEnabled]"
- "-[HUComfortSoundsController setupTimerIfNeeded]"
- "-[HUComfortSoundsController startComfortSounds]"
- "-[HUComfortSoundsController stopComfortSound:]"
- "-[HUComfortSoundsController stop]_block_invoke"
- "-[HUComfortSoundsController updateAnalytics]"
- "-[HUComfortSoundsSettings logMessage:]"
- "-[HUComfortSoundsSettings selectedComfortSound]"
- "-[HUComfortSoundsSettings setSelectedComfortSound:]"
- "-[HUComfortSoundsSettings setTimerInHoursAndMinutes:minutes:]"
- "-[HUComfortSoundsSettings setTinnitusFilterPoint:]"
- "-[HUComfortSoundsSettings tinnitusFilterPoint]"
- "-[HUDeviceController device:didUpdateProperty:]"
- "-[HUDeviceController device:didUpdateProperty:]_block_invoke"
- "-[HUDeviceController stopPropertyUpdates]"
- "-[HUHearingAidSettings _initializeICloudSetup]"
- "-[HUHearingAidSettings _initializeICloudSetup]_block_invoke"
- "-[HUHearingAidSettings accountCredentialChanged:]"
- "-[HUHearingAidSettings accountWasAdded:]"
- "-[HUHearingAidSettings accountWasModified:]"
- "-[HUHearingAidSettings accountWasRemoved:]"
- "-[HUHearingAidSettings iCloudAccountDidChange:]_block_invoke"
- "-[HUHearingAidSettings icloudHearingSettingsDidChange:]_block_invoke"
- "-[HUHearingAidSettings init]"
- "-[HUHearingAidSettings logMessage:]"
- "-[HUHearingAidSettings pushLocalHearingAidsToiCloud]"
- "-[HUHearingAidSettings setLocalHearingAidsFromiCloud:]"
- "-[HUHearingAidSettings setPairedHearingAids:]"
- "-[HUHearingAidSettings shouldUseiCloud]"
- "-[HUHearingSettings hearingControlCenterOrder]"
- "-[HUHearingSettings logMessage:]"
- "-[HUHearingSettings setHearingControlCenterOrder:]"
- "-[HULiveListenController _setupSession]"
- "-[HULiveListenController audioRouteDidChange:]_block_invoke"
- "-[HULiveListenController audioSessionWasInterrupted:]_block_invoke"
- "-[HULiveListenController init]_block_invoke_2"
- "-[HULiveListenController mediaServicesWereReset:]_block_invoke"
- "-[HULiveListenController setPersonalAudioMediaAccommodationsEnabled:]"
- "-[HULiveListenController startListeningWithCompletion:]_block_invoke"
- "-[HULiveListenController stopListeningWithCompletion:]_block_invoke"
- "-[HUNearbyHearingAidController device:didReceiveMessage:]"
- "-[HUNearbyHearingAidController device:didReceiveMessage:]_block_invoke"
- "-[HUNearbyHearingAidController init]_block_invoke"
- "-[HUNearbyHearingAidController logAvailableDevicesWithTitle:]"
- "-[HUNearbyHearingAidController mediaServerDied]"
- "-[HUNearbyHearingAidController processHandoffMessageFromPeer:state:]"
- "-[HUNearbyHearingAidController processReadMessageFromPeerDevice:value:]"
- "-[HUNearbyHearingAidController processStateMessageFromPeer:state:]"
- "-[HUNearbyHearingAidController processWriteMessageWithValue:]"
- "-[HUNearbyHearingAidController processWriteMessageWithValue:]_block_invoke"
- "-[HUNearbyHearingAidController registerMediaNotifications]"
- "-[HUNearbyHearingAidController sendMessagesPriority:]"
- "-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke"
- "-[HUNearbyHearingAidController sendMessagesPriorityHighForClient:]_block_invoke"
- "-[HUNearbyHearingAidController sendWrite:toDevices:]"
- "-[HUNearbyHearingAidController sendWrite:toDevices:]_block_invoke"
- "-[HUNearbyHearingAidController setMessagePriority:forDevice:]"
- "-[HUNearbyHearingAidController start]_block_invoke"
- "-[HUNearbyHearingAidController unregisterMediaNotifications]"
- "-[HUNearbyHearingAidController updateProperty:forDeviceID:]"
- "-[HUNearbyHearingAidController updateProperty:forDeviceID:]_block_invoke"
- "-[HUNearbyHearingAidController writeValue:forProperty:andDeviceID:]"
- "-[HUNearbyLiveListenControllerWatch _handleStateChangedMessage:]"
- "-[HUNearbyLiveListenControllerWatch _receivedMessage:fromDevice:]_block_invoke"
- "-[HUNearbyLiveListenControllerWatch _sendMessageToRequestInitialState]"
- "-[HUNearbyLiveListenControllerWatch _sendStartObservingMessageToDevices:]"
- "-[HUNearbyLiveListenControllerWatch _sendStartOrStopMessage:]"
- "-[HUNearbyLiveListenControllerWatch _sendStartOrStopRewindMessage:]"
- "-[HUNearbyLiveListenControllerWatch _sendStopObservingMessage]"
- "-[HUNearbyLiveListenControllerWatch startObserving]"
- "-[HUNearbyLiveListenControllerWatch startObserving]_block_invoke"
- "-[HUNearbyLiveListenControllerWatch stopObserving]"
- "-[HUNearbyLiveListenControlleriOS _audioRoutesChanged:]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS _callsStatusChanged:]_block_invoke_2"
- "-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke_2"
- "-[HUNearbyLiveListenControlleriOS _handleRequestCurrentStateMessageFromDevice:]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS _handleStartObservingFromRemoteDevice:]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS _handleStartOrStopMessageFromRemoteDevice:message:]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS _handleStartOrStopRewindMessageFromRemoteDevice:message:]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS _handleStateChangedMessage:fromDevice:]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS _handleStopObservingFromRemoteDevice:]"
- "-[HUNearbyLiveListenControlleriOS _nearbyDevices]"
- "-[HUNearbyLiveListenControlleriOS _nearbyDevices]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS _receivedMessage:fromDevice:]"
- "-[HUNearbyLiveListenControlleriOS _sendEmptyStateToUnauthorizedDevice:]"
- "-[HUNearbyLiveListenControlleriOS _sendStartObservingMessageToDevices:]"
- "-[HUNearbyLiveListenControlleriOS _sendStartOrStopMessage:]"
- "-[HUNearbyLiveListenControlleriOS _sendStartOrStopRewindMessage:]"
- "-[HUNearbyLiveListenControlleriOS _sendStopObservingMessage]"
- "-[HUNearbyLiveListenControlleriOS _startLiveListenFromRemoteDevice:]"
- "-[HUNearbyLiveListenControlleriOS _startLiveListenRewind]"
- "-[HUNearbyLiveListenControlleriOS _stopLiveListenFromRemoteDevice:]"
- "-[HUNearbyLiveListenControlleriOS _stopLiveListenRewind]"
- "-[HUNearbyLiveListenControlleriOS _wirelessSplitterEnabledChanged:]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS startObserving]"
- "-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke"
- "-[HUNearbyLiveListenControlleriOS stopObserving]"
- "-[HUNoiseController applyNotificationLogicForSPL:withDuration:]"
- "-[HUNoiseController calculateLeqForBuffer:]"
- "-[HUNoiseController checkToResetAnalyticsNotificationsForSPL:withDuration:andBuffer:forTime:andThreshold:]"
- "-[HUNoiseController checkToResetNotificationsForSPL:withDuration:andBuffer:forTime:]"
- "-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]"
- "-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke"
- "-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]"
- "-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke"
- "-[HUNoiseController init]"
- "-[HUNoiseController init]_block_invoke"
- "-[HUNoiseController logNoiseBuffer:calculatedLeq:]"
- "-[HUNoiseController logThresholdTransitionForSample:]"
- "-[HUNoiseController lowPowerModeChanged:]"
- "-[HUNoiseController maintainCircularBuffer:forTime:]"
- "-[HUNoiseController processMeasurement:withMetadata:]_block_invoke"
- "-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke"
- "-[HUNoiseController restartADAMTimer]_block_invoke"
- "-[HUNoiseController shouldShowHearingProtectionSuggestionForAlertType:]"
- "-[HUNoiseController showNotificationForAlertType:]"
- "-[HUNoiseController showNotificationForAlertType:]_block_invoke"
- "-[HUNoiseController stopReceivingAudioDosageSamples]"
- "-[HUNoiseController subscribeToSharedNotifications]_block_invoke"
- "-[HUNoiseController subscribeToSharedNotifications]_block_invoke_2"
- "-[HUNoiseController writeAttentuationSampleToHealth]"
- "-[HUNoiseController writeAttentuationSampleToHealth]_block_invoke"
- "-[HUNoiseController writeNotificationSampleToHKWithSPL:startDate:endDate:]"
- "-[HUNoiseController writeNotificationSampleToHKWithSPL:startDate:endDate:]_block_invoke"
- "-[HUNoiseSettings setHearingProtectionDeviceAvailable:]"
- "-[HURoutesManager mediaServerDied]_block_invoke"
- "-[HUUtilities backgroundSoundsRouteDecision]"
- "-[HUUtilities hearingAidRouteAvailableForAvailableRoutes:]"
- "-[HUUtilities liveListenRouteSelectedForAvailableRoutes:]"
- "-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke"
- "-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_2"
- "-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_3"
- "-[HUUtilities updateWirelessSplitterState]"
- "-[NSArray(_AX_HA_PROGRAMS_ARRAY_) setProgram:withOtherSidePrograms:selected:]"
- "void LiveListenRequestNotificationAuthorization(void)_block_invoke"
- "void _LiveListenSendUserNotification(NSString *__strong, BOOL)"
- "void _LiveListenSendUserNotification(NSString *__strong, BOOL)_block_invoke"
- "void _hearingTestStarted(CFNotificationCenterRef, void *, CFStringRef, const void *, CFDictionaryRef)"
- "void hearingDeamonShouldBeRunning(__strong AXBoolBlock _Nonnull)"
- "void pairedWithDevicesSupportingListeningModes(__strong AXBoolBlock _Nonnull)_block_invoke_2"
- "void shouldHandleServerStarting(CFNotificationCenterRef, void *, CFStringRef, const void *, CFDictionaryRef)"

```
