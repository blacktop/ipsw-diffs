## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-456.8.10.0.0
-  __TEXT.__text: 0x814b4
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x609c
-  __TEXT.__const: 0x248
-  __TEXT.__gcc_except_tab: 0x27ec
-  __TEXT.__cstring: 0xb931
-  __TEXT.__oslogstring: 0x1df7
-  __TEXT.__dlopen_cstrs: 0x54d
-  __TEXT.__unwind_info: 0x1ca0
-  __TEXT.__objc_classname: 0x628
-  __TEXT.__objc_methname: 0xf9d6
-  __TEXT.__objc_methtype: 0x1b2b
-  __TEXT.__objc_stubs: 0xb6a0
-  __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x2a28
-  __DATA_CONST.__objc_classlist: 0x158
-  __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xa8
+485.3.0.0.0
+  __TEXT.__text: 0xa1340
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x7a3c
+  __TEXT.__const: 0x34c
+  __TEXT.__gcc_except_tab: 0x2f00
+  __TEXT.__cstring: 0xdd13
+  __TEXT.__oslogstring: 0x3496
+  __TEXT.__dlopen_cstrs: 0x73d
+  __TEXT.__unwind_info: 0x2408
+  __TEXT.__objc_classname: 0x83f
+  __TEXT.__objc_methname: 0x138f5
+  __TEXT.__objc_methtype: 0x216d
+  __TEXT.__objc_stubs: 0xe7e0
+  __DATA_CONST.__got: 0x640
+  __DATA_CONST.__const: 0x32a0
+  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3970
-  __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_arraydata: 0x2f0
-  __AUTH_CONST.__auth_got: 0x6b8
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x7980
-  __AUTH_CONST.__objc_const: 0x81c0
-  __AUTH_CONST.__objc_intobj: 0x6c0
-  __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__objc_arrayobj: 0x168
+  __DATA_CONST.__objc_selrefs: 0x4790
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_arraydata: 0x438
+  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH_CONST.__const: 0xca0
+  __AUTH_CONST.__cfstring: 0x8b00
+  __AUTH_CONST.__objc_const: 0xa1f0
+  __AUTH_CONST.__objc_intobj: 0xab0
+  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_doubleobj: 0xed0
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x718
-  __DATA.__data: 0x908
-  __DATA.__bss: 0x300
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x140
+  __AUTH.__objc_data: 0xe10
+  __DATA.__objc_ivar: 0x8bc
+  __DATA.__data: 0xc08
+  __DATA.__bss: 0x3a0
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13662BBF-CF1E-32AF-8B39-F2265B633CDB
-  Functions: 2644
-  Symbols:   8751
-  CStrings:  5431
+  UUID: CEFADB44-8AA8-3AF2-BE33-49185FBE8628
+  Functions: 3389
+  Symbols:   11033
+  CStrings:  6664
 
Symbols:
+ +[HUComfortSoundsFilterPoint supportsSecureCoding]
+ +[HUNearbyLiveListenController sharedInstance]
+ +[HUNearbyLiveListenController sharedInstance].cold.1
+ -[AXHAController _liveListenPayloadWithState:audioLevel:isPlayingBack:transcription:]
+ -[AXHAController _registerForLiveListenUpdates_enumValue:]
+ -[AXHAController _registerForLiveListenUpdates_enumValue:].cold.1
+ -[AXHAController _toggleLiveListen_enumValue:]
+ -[AXHAController _toggleLiveListen_enumValue:].cold.1
+ -[AXHAController liveListenCountsPerClient]
+ -[AXHAController observeRemoteLiveListenUpdates:]
+ -[AXHAController setLiveListenCountsPerClient:]
+ -[AXHAController toggleLiveListenRewind:]
+ -[AXHAServer _liveListenDidUpdate_enumValue:]
+ -[AXHAServer backgroundSoundsPlaying]
+ -[AXHAServer registerListener:forLiveListenHandler:]
+ -[AXHAServer requestNoiseBuffersForTimeInterval:withHandler:]
+ -[AXHAServer startLiveListenRewind]
+ -[AXHAServer startObservingRemoteLiveListenUpdates]
+ -[AXHAServer stopLiveListenRewind]
+ -[AXHAServer stopObservingRemoteLiveListenUpdates]
+ -[AXHAServer unregisterLiveListenListener:]
+ -[AXHearingAidDevice RSSI]
+ -[AXHearingAidDevice _initCharacteristicsForPeripheral:]
+ -[AXHearingAidDevice descriptiveProperties]
+ -[AXHearingAidDevice deviceProtocol]
+ -[AXHearingAidDevice didAddPeripheral:]
+ -[AXHearingAidDevice didAddPeripheral:].cold.1
+ -[AXHearingAidDevice discoveringServiceUUIDs]
+ -[AXHearingAidDevice discoveringServiceUUIDs].cold.1
+ -[AXHearingAidDevice leftRSSI]
+ -[AXHearingAidDevice peripheral:didDiscoverServices:].cold.1
+ -[AXHearingAidDevice peripheral:didReadRSSI:error:]
+ -[AXHearingAidDevice peripheralDidUpdateDeviceInfo]
+ -[AXHearingAidDevice propertyForCharacteristic:]
+ -[AXHearingAidDevice rightRSSI]
+ -[AXHearingAidDevice serviceTypeDescription]
+ -[AXHearingAidDevice sessionDidUpdateLocations:]
+ -[AXHearingAidDevice sessionDidUpdateValue:forProperty:]
+ -[AXHearingAidDevice setBasicPropertiesLoaded]
+ -[AXHearingAidDevice setLeftRSSI:]
+ -[AXHearingAidDevice setRightRSSI:]
+ -[AXHearingAidDevice setupLoadingProperties]
+ -[AXHearingAidDevice swapPeripheral:toEar:]
+ -[AXHearingAidDevice valueForProperty:].cold.2
+ -[AXHearingAidDevice valueForProperty:].cold.3
+ -[AXHearingAidDeviceController addPeripheral:toDevice:]
+ -[AXHearingAidDeviceController centralManager:didConnectPeripheral:].cold.1
+ -[AXHearingAidDeviceController centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.1
+ -[AXHearingAidDeviceController clearPairedHearingAids]
+ -[AXHearingAidDeviceController hearingAidForPeripheralID:]
+ -[AXHearingAidDeviceController isLEAudioServiceInServiceUUIDs:]
+ -[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]
+ -[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:].cold.1
+ -[AXHearingAidDeviceController scanningServiceUUIDs]
+ -[AXHearingAidDeviceController scanningServiceUUIDs].cold.1
+ -[AXHearingAidDeviceController setupCentralManagerForLEAudio]
+ -[AXHearingAidLEAudioDevice _initCharacteristicsForPeripheral:]
+ -[AXHearingAidLEAudioDevice addPeripheral:]
+ -[AXHearingAidLEAudioDevice addPeripheral:asLeft:]
+ -[AXHearingAidLEAudioDevice availablePropertiesForPeripheral:]
+ -[AXHearingAidLEAudioDevice availablePropertiesForPeripheral:].cold.1
+ -[AXHearingAidLEAudioDevice availablePropertiesFromDISForPeripheral:]
+ -[AXHearingAidLEAudioDevice connect]
+ -[AXHearingAidLEAudioDevice connectionDidChange]
+ -[AXHearingAidLEAudioDevice dealloc]
+ -[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]
+ -[AXHearingAidLEAudioDevice descriptiveProperties]
+ -[AXHearingAidLEAudioDevice deviceProtocol]
+ -[AXHearingAidLEAudioDevice didAddPeripheral:]
+ -[AXHearingAidLEAudioDevice didLoadPersistentProperties]
+ -[AXHearingAidLEAudioDevice didLoadPersistentProperties].cold.1
+ -[AXHearingAidLEAudioDevice disconnectAndUnpair:]
+ -[AXHearingAidLEAudioDevice discoveringServiceUUIDs]
+ -[AXHearingAidLEAudioDevice discoveringServiceUUIDs].cold.1
+ -[AXHearingAidLEAudioDevice earForPeripheral:]
+ -[AXHearingAidLEAudioDevice earForPeripheral:].cold.1
+ -[AXHearingAidLEAudioDevice isLeftEventHandlerSet]
+ -[AXHearingAidLEAudioDevice isRightEventHandlerSet]
+ -[AXHearingAidLEAudioDevice leftLoadedProperties]
+ -[AXHearingAidLEAudioDevice loadBasicProperties]
+ -[AXHearingAidLEAudioDevice loadProperties:forPeripheral:withRetryPeriod:]
+ -[AXHearingAidLEAudioDevice loadProperties:forPeripheral:withRetryPeriod:].cold.1
+ -[AXHearingAidLEAudioDevice loadRequiredProperties]
+ -[AXHearingAidLEAudioDevice peripheral:characteristicForUUID:]
+ -[AXHearingAidLEAudioDevice peripheral:characteristicForUUID:].cold.1
+ -[AXHearingAidLEAudioDevice peripheralDidUpdateDeviceInfo]
+ -[AXHearingAidLEAudioDevice processBTPresetsUpdate:activePreset:forEar:]
+ -[AXHearingAidLEAudioDevice rightLoadedProperties]
+ -[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]
+ -[AXHearingAidLEAudioDevice sessionDidUpdateValue:forProperty:]
+ -[AXHearingAidLEAudioDevice sessionDidUpdateValue:forProperty:].cold.1
+ -[AXHearingAidLEAudioDevice setBasicPropertiesLoaded]
+ -[AXHearingAidLEAudioDevice setIsLeftEventHandlerSet:]
+ -[AXHearingAidLEAudioDevice setIsRightEventHandlerSet:]
+ -[AXHearingAidLEAudioDevice setLeftLoadedProperties:]
+ -[AXHearingAidLEAudioDevice setNotify:forPeripheral:]
+ -[AXHearingAidLEAudioDevice setNotify:forPeripheral:].cold.1
+ -[AXHearingAidLEAudioDevice setRightLoadedProperties:]
+ -[AXHearingAidLEAudioDevice setValue:forProperty:]
+ -[AXHearingAidLEAudioDevice setupLoadingProperties]
+ -[AXHearingAidLEAudioDevice setupUpdatesHandlerForLEAudioPeripheral:]
+ -[AXHearingAidLEAudioDevice setupUpdatesHandlerForLEAudioPeripheral:].cold.1
+ -[AXHearingAidLEAudioDevice updateName]
+ -[AXHearingAidLEAudioDevice writeValueForProperty:]
+ -[AXHearingAidLEAudioDevice writeValueForProperty:].cold.1
+ -[AXRemoteHearingAidDevice RSSI]
+ -[AXRemoteHearingAidDevice deviceProtocol]
+ -[AXRemoteHearingAidDevice setDeviceProtocol:]
+ -[AXRemoteHearingAidDevice setRSSI:]
+ -[CBDevice(_HUAccessory_) productCode]
+ -[HUAccessoryManager aaDeviceManager]
+ -[HUAccessoryManager attributeUpdateUpdates]
+ -[HUAccessoryManager bluetoothListeningModeFromHearingListeningMode:]
+ -[HUAccessoryManager enumerateAudioBluetoothDevicesUsingBlock:]
+ -[HUAccessoryManager enumerateAvailableDevicesWithBlock:andCompletion:]
+ -[HUAccessoryManager enumerateAvailablePSEDevicesWithBlock:andCompletion:]
+ -[HUAccessoryManager enumerateConnectedBluetoothDevices:usingBlock:andCompletion:]
+ -[HUAccessoryManager enumerateProductCodesforAddresses:withBlock:]
+ -[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]
+ -[HUAccessoryManager getCurrentRouteListeningModeWithCompletion:]
+ -[HUAccessoryManager getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:]
+ -[HUAccessoryManager getHearingProtectionSupportforAddress:withCompletion:]
+ -[HUAccessoryManager getPMEEverywhereSupportStateForAddress:withCompletion:]
+ -[HUAccessoryManager getPSEVersionForAddress:withCompletion:]
+ -[HUAccessoryManager getPairedDeviceSupportsPSE:]
+ -[HUAccessoryManager getProductCodeforAddress:withCompletion:]
+ -[HUAccessoryManager getSSLEnabledForAddress:withCompletion:]
+ -[HUAccessoryManager getSSLSupportStateForAddress:withCompletion:]
+ -[HUAccessoryManager hearingListeningModeFromBluetoothListeningMode:]
+ -[HUAccessoryManager pmeEverywhereSupportedForAddress:]
+ -[HUAccessoryManager pseVersionForAddress:]
+ -[HUAccessoryManager registerAttributeUpdateBlock:withListener:]
+ -[HUAccessoryManager setAaDeviceManager:]
+ -[HUAccessoryManager setAttributeUpdateUpdates:]
+ -[HUAccessoryManager setCurrentRouteListeningMode:]
+ -[HUAccessoryManager setSSLEnabled:forAddress:]
+ -[HUAccessoryManager turnBluetoothOnWithCompletion:]
+ -[HUAudioBuffer bufferList]
+ -[HUAudioBuffer copyWithZone:]
+ -[HUAudioBuffer dealloc]
+ -[HUAudioBuffer initWithBuffer:]
+ -[HUAudioBuffer setBufferList:]
+ -[HUComfortSound canBeDeleted]
+ -[HUComfortSound canBeEdited]
+ -[HUComfortSound isInstalled]
+ -[HUComfortSound setVolume:]
+ -[HUComfortSound volume]
+ -[HUComfortSoundsController _remainingTimeUntilTimestamp:]
+ -[HUComfortSoundsController activeDurationTimerEndTimeStampCache]
+ -[HUComfortSoundsController applyBypassForFiltersAtIndexes:shouldBypass:]
+ -[HUComfortSoundsController applyTinnitusBalance]
+ -[HUComfortSoundsController attachNodesToEngine]
+ -[HUComfortSoundsController audioPlayerFilterNode]
+ -[HUComfortSoundsController audioPlayerMixerNode]
+ -[HUComfortSoundsController calculateVolumeForSessionWithCompletion:]
+ -[HUComfortSoundsController comfortSoundsEnabledCache]
+ -[HUComfortSoundsController configureBandWithType:frequency:bandwidth:atIndex:]
+ -[HUComfortSoundsController configureBandWithType:frequency:bandwidth:gain:atIndex:]
+ -[HUComfortSoundsController configureBandsForCoarseFilter]
+ -[HUComfortSoundsController configureBandsForFineFilter]
+ -[HUComfortSoundsController configureTinnitusEqualizer]
+ -[HUComfortSoundsController connectNodesToEngine:]
+ -[HUComfortSoundsController endTimeStamp]
+ -[HUComfortSoundsController handlePlaybackForDifferentCategory]
+ -[HUComfortSoundsController handlePlaybackForSameCategory]
+ -[HUComfortSoundsController invalidateTimer]
+ -[HUComfortSoundsController isSameCategoryAsSelectedSound:]
+ -[HUComfortSoundsController isSettingUpPreviewComfortSounds]
+ -[HUComfortSoundsController isSettingUpPreviewTimer]
+ -[HUComfortSoundsController listenForChangesInEqualizer]
+ -[HUComfortSoundsController listenForChangesInTimer]
+ -[HUComfortSoundsController logMessageForTimer:]
+ -[HUComfortSoundsController playbackTimer]
+ -[HUComfortSoundsController processAutomationRequest:]
+ -[HUComfortSoundsController scheduleTimer:]
+ -[HUComfortSoundsController setActiveDurationTimerEndTimeStampCache:]
+ -[HUComfortSoundsController setAudioPlayerFilterNode:]
+ -[HUComfortSoundsController setAudioPlayerMixerNode:]
+ -[HUComfortSoundsController setComfortSoundsEnabledCache:]
+ -[HUComfortSoundsController setFilterBoost:]
+ -[HUComfortSoundsController setIsSettingUpPreviewComfortSounds:]
+ -[HUComfortSoundsController setIsSettingUpPreviewTimer:]
+ -[HUComfortSoundsController setPlaybackTimer:]
+ -[HUComfortSoundsController setTimerEnabledCache:]
+ -[HUComfortSoundsController setupTimerIfEnabled]
+ -[HUComfortSoundsController setupTimerIfNeeded]
+ -[HUComfortSoundsController stopComfortSound:]
+ -[HUComfortSoundsController timerEnabledCache]
+ -[HUComfortSoundsController validateTimerDuration]
+ -[HUComfortSoundsController validateTimerEndInterval]
+ -[HUComfortSoundsFilterPoint encodeWithCoder:]
+ -[HUComfortSoundsFilterPoint frequencyForBandPass]
+ -[HUComfortSoundsFilterPoint gainForHighResonance]
+ -[HUComfortSoundsFilterPoint gainForLeftBellFilters]
+ -[HUComfortSoundsFilterPoint gainForLowResonance]
+ -[HUComfortSoundsFilterPoint gainForRightBellFilters]
+ -[HUComfortSoundsFilterPoint hash]
+ -[HUComfortSoundsFilterPoint initWithCoder:]
+ -[HUComfortSoundsFilterPoint initWithPoint:]
+ -[HUComfortSoundsFilterPoint isEqual:]
+ -[HUComfortSoundsFilterPoint linearTransformation:inputMin:inputMax:outputMin:outputMax:]
+ -[HUComfortSoundsFilterPoint setXValue:]
+ -[HUComfortSoundsFilterPoint setYValue:]
+ -[HUComfortSoundsFilterPoint widthForBandPass]
+ -[HUComfortSoundsFilterPoint xValue]
+ -[HUComfortSoundsFilterPoint yValue]
+ -[HUComfortSoundsSettings activeTimerEndTimeStamp]
+ -[HUComfortSoundsSettings previewEnabled]
+ -[HUComfortSoundsSettings resetTimers]
+ -[HUComfortSoundsSettings setActiveTimerEndTimeStamp:]
+ -[HUComfortSoundsSettings setPreviewEnabled:]
+ -[HUComfortSoundsSettings setTimerDurationInSeconds:]
+ -[HUComfortSoundsSettings setTimerEnabled:]
+ -[HUComfortSoundsSettings setTimerEndInterval:]
+ -[HUComfortSoundsSettings setTimerInHoursAndMinutes:minutes:]
+ -[HUComfortSoundsSettings setTimerOnlyOnFirstSession:]
+ -[HUComfortSoundsSettings setTimerOption:]
+ -[HUComfortSoundsSettings setTinnitusBalance:]
+ -[HUComfortSoundsSettings setTinnitusFilterEnabled:]
+ -[HUComfortSoundsSettings setTinnitusFilterMode:]
+ -[HUComfortSoundsSettings setTinnitusFilterPoint:]
+ -[HUComfortSoundsSettings timerDurationInSeconds]
+ -[HUComfortSoundsSettings timerEnabled]
+ -[HUComfortSoundsSettings timerEndInterval]
+ -[HUComfortSoundsSettings timerOnlyOnFirstSession]
+ -[HUComfortSoundsSettings timerOption]
+ -[HUComfortSoundsSettings tinnitusBalance]
+ -[HUComfortSoundsSettings tinnitusFilterEnabled]
+ -[HUComfortSoundsSettings tinnitusFilterMode]
+ -[HUComfortSoundsSettings tinnitusFilterPoint]
+ -[HUHearingSettings liveListenRemoteControlEnabled]
+ -[HUHearingSettings liveListenRemoteStartHistory]
+ -[HUHearingSettings setLiveListenRemoteControlEnabled:]
+ -[HUHearingSettings setLiveListenRemoteStartHistory:]
+ -[HULiveListenController _sampleRate]
+ -[HULiveListenController audioQueue]
+ -[HULiveListenController audioRingBuffer]
+ -[HULiveListenController combinedSessionTranscription]
+ -[HULiveListenController isPlayingBack]
+ -[HULiveListenController playbackQueue]
+ -[HULiveListenController sessionTranscriptions]
+ -[HULiveListenController setAudioQueue:]
+ -[HULiveListenController setAudioRingBuffer:]
+ -[HULiveListenController setIsPlayingBack:]
+ -[HULiveListenController setPlaybackQueue:]
+ -[HULiveListenController setSessionTranscriptions:]
+ -[HULiveListenController setTranscriber:]
+ -[HULiveListenController setTranscription:]
+ -[HULiveListenController startLiveListenRewind]
+ -[HULiveListenController stopLiveListenRewind]
+ -[HULiveListenController transcriber]
+ -[HULiveListenController transcriptionDidStart]
+ -[HULiveListenController transcriptionDidUpdate:]
+ -[HULiveListenController transcription]
+ -[HULiveListenObserver .cxx_destruct]
+ -[HULiveListenObserver _notifyListenersAndPollAudioLevelIfLiveListenIsRunning]
+ -[HULiveListenObserver _notifyListenersWithIsListening:audioLevel:isPlayingBack:transcription:]
+ -[HULiveListenObserver _pollLiveListenAudioLevelAfterDelay]
+ -[HULiveListenObserver controller]
+ -[HULiveListenObserver initWithController:]
+ -[HULiveListenObserver liveListenControllerStateDidChange]
+ -[HULiveListenObserver liveListenLevelsTimer]
+ -[HULiveListenObserver registerUpdateBlock:withListener:]
+ -[HULiveListenObserver removeListener:]
+ -[HULiveListenObserver setController:]
+ -[HULiveListenObserver setLiveListenLevelsTimer:]
+ -[HULiveListenObserver setUpdateBlocks:]
+ -[HULiveListenObserver setUpdateLock:]
+ -[HULiveListenObserver updateBlocks]
+ -[HULiveListenObserver updateLock]
+ -[HULiveListenTranscriptionController .cxx_destruct]
+ -[HULiveListenTranscriptionController currentTranscription]
+ -[HULiveListenTranscriptionController delegate]
+ -[HULiveListenTranscriptionController initWithDelegate:]
+ -[HULiveListenTranscriptionController init]
+ -[HULiveListenTranscriptionController isTranscribing]
+ -[HULiveListenTranscriptionController sessionTranscriptions]
+ -[HULiveListenTranscriptionController setCurrentTranscription:]
+ -[HULiveListenTranscriptionController setDelegate:]
+ -[HULiveListenTranscriptionController setIsTranscribing:]
+ -[HULiveListenTranscriptionController setSessionTranscriptions:]
+ -[HULiveListenTranscriptionController setTranscriber:]
+ -[HULiveListenTranscriptionController startTranscribing]
+ -[HULiveListenTranscriptionController stopTranscribing]
+ -[HULiveListenTranscriptionController transcriber]
+ -[HUNearbyController checkSCIDSServiceDevices]
+ -[HUNearbyController checkSCIDSServiceDevices].cold.1
+ -[HUNearbyController messagesCount]
+ -[HUNearbyController nearbyDeviceWithSCIDSDevice:justCreated:]
+ -[HUNearbyController setMessagesCount:]
+ -[HUNearbyDevice isiPad]
+ -[HUNearbyDevice isiPhone]
+ -[HUNearbyHearingAidController scIDSServiceDidAddDevices:]
+ -[HUNearbyLiveListenController .cxx_destruct]
+ -[HUNearbyLiveListenController _updateState:audioLevel:isPlayingBack:transcription:]
+ -[HUNearbyLiveListenController audioLevel]
+ -[HUNearbyLiveListenController deviceImplementation]
+ -[HUNearbyLiveListenController init]
+ -[HUNearbyLiveListenController isPlayingBack]
+ -[HUNearbyLiveListenController registerUpdateBlock:withListener:]
+ -[HUNearbyLiveListenController removeListener:]
+ -[HUNearbyLiveListenController setAudioLevel:]
+ -[HUNearbyLiveListenController setDeviceImplementation:]
+ -[HUNearbyLiveListenController setIsPlayingBack:]
+ -[HUNearbyLiveListenController setState:]
+ -[HUNearbyLiveListenController setTranscription:]
+ -[HUNearbyLiveListenController setUpdateBlocks:]
+ -[HUNearbyLiveListenController setUpdateLock:]
+ -[HUNearbyLiveListenController startLiveListenRewind]
+ -[HUNearbyLiveListenController startLiveListen]
+ -[HUNearbyLiveListenController state]
+ -[HUNearbyLiveListenController stopLiveListenRewind]
+ -[HUNearbyLiveListenController stopLiveListen]
+ -[HUNearbyLiveListenController transcription]
+ -[HUNearbyLiveListenController updateBlocks]
+ -[HUNearbyLiveListenController updateLock]
+ -[HUNearbyLiveListenControllerWatch .cxx_destruct]
+ -[HUNearbyLiveListenControllerWatch _handleStateChangedMessage:]
+ -[HUNearbyLiveListenControllerWatch _nearbyDevicesChanged]
+ -[HUNearbyLiveListenControllerWatch _receivedMessage:fromDevice:]
+ -[HUNearbyLiveListenControllerWatch _sendMessageToRequestInitialState]
+ -[HUNearbyLiveListenControllerWatch _sendStartObservingMessage]
+ -[HUNearbyLiveListenControllerWatch _sendStartOrStopMessage:]
+ -[HUNearbyLiveListenControllerWatch _sendStartOrStopRewindMessage:]
+ -[HUNearbyLiveListenControllerWatch _sendStopObservingMessage]
+ -[HUNearbyLiveListenControllerWatch _updateState]
+ -[HUNearbyLiveListenControllerWatch cachedIsPlayingBack]
+ -[HUNearbyLiveListenControllerWatch cachedNearbyDevices]
+ -[HUNearbyLiveListenControllerWatch cachedState]
+ -[HUNearbyLiveListenControllerWatch cachedTranscription]
+ -[HUNearbyLiveListenControllerWatch controller]
+ -[HUNearbyLiveListenControllerWatch initWithController:]
+ -[HUNearbyLiveListenControllerWatch setCachedIsPlayingBack:]
+ -[HUNearbyLiveListenControllerWatch setCachedNearbyDevices:]
+ -[HUNearbyLiveListenControllerWatch setCachedState:]
+ -[HUNearbyLiveListenControllerWatch setCachedTranscription:]
+ -[HUNearbyLiveListenControllerWatch setController:]
+ -[HUNearbyLiveListenControllerWatch setUpdateQueue:]
+ -[HUNearbyLiveListenControllerWatch startLiveListenRewind]
+ -[HUNearbyLiveListenControllerWatch startLiveListen]
+ -[HUNearbyLiveListenControllerWatch startObservingRemoteSession]
+ -[HUNearbyLiveListenControllerWatch startObserving]
+ -[HUNearbyLiveListenControllerWatch startObserving].cold.1
+ -[HUNearbyLiveListenControllerWatch stopLiveListenRewind]
+ -[HUNearbyLiveListenControllerWatch stopLiveListen]
+ -[HUNearbyLiveListenControllerWatch stopObservingRemoteSession]
+ -[HUNearbyLiveListenControllerWatch stopObserving]
+ -[HUNearbyLiveListenControllerWatch stopObserving].cold.1
+ -[HUNearbyLiveListenControllerWatch updateQueue]
+ -[HUNearbyLiveListenControlleriOS .cxx_destruct]
+ -[HUNearbyLiveListenControlleriOS _audioRoutesChanged:]
+ -[HUNearbyLiveListenControlleriOS _callsStatusChanged:]
+ -[HUNearbyLiveListenControlleriOS _devicesToMessage]
+ -[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]
+ -[HUNearbyLiveListenControlleriOS _handleRequestCurrentStateMessageFromDevice:]
+ -[HUNearbyLiveListenControlleriOS _handleStartObservingFromRemoteDevice:]
+ -[HUNearbyLiveListenControlleriOS _handleStartOrStopMessageFromRemoteDevice:message:]
+ -[HUNearbyLiveListenControlleriOS _handleStartOrStopRewindMessageFromRemoteDevice:message:]
+ -[HUNearbyLiveListenControlleriOS _handleStateChangedMessage:fromDevice:]
+ -[HUNearbyLiveListenControlleriOS _handleStopObservingFromRemoteDevice:]
+ -[HUNearbyLiveListenControlleriOS _isListeningChanged:audioLevel:isPlayingBack:orTranscriptionChanged:]
+ -[HUNearbyLiveListenControlleriOS _nearbyDevicesChanged]
+ -[HUNearbyLiveListenControlleriOS _nearbyDevices]
+ -[HUNearbyLiveListenControlleriOS _notifyAboutAllObservingDevices]
+ -[HUNearbyLiveListenControlleriOS _notifyAboutObservingDevice:]
+ -[HUNearbyLiveListenControlleriOS _receivedMessage:fromDevice:]
+ -[HUNearbyLiveListenControlleriOS _scheduleStateUpdate]
+ -[HUNearbyLiveListenControlleriOS _sendEmptyStateToUnauthorizedDevice:]
+ -[HUNearbyLiveListenControlleriOS _sendLatestNearbyUpdate]
+ -[HUNearbyLiveListenControlleriOS _sendMessageToRequestInitialState]
+ -[HUNearbyLiveListenControlleriOS _sendStartObservingMessage]
+ -[HUNearbyLiveListenControlleriOS _sendStartOrStopMessage:]
+ -[HUNearbyLiveListenControlleriOS _sendStartOrStopRewindMessage:]
+ -[HUNearbyLiveListenControlleriOS _sendStopObservingMessage]
+ -[HUNearbyLiveListenControlleriOS _startLiveListenFromRemoteDevice:]
+ -[HUNearbyLiveListenControlleriOS _startLiveListenRewind]
+ -[HUNearbyLiveListenControlleriOS _stopLiveListenFromRemoteDevice:]
+ -[HUNearbyLiveListenControlleriOS _stopLiveListenRewind]
+ -[HUNearbyLiveListenControlleriOS _updateRemoteStartHistoryForDevice:didStart:]
+ -[HUNearbyLiveListenControlleriOS _updateRemoteStartHistoryForDevice:didStart:].cold.1
+ -[HUNearbyLiveListenControlleriOS _updateState]
+ -[HUNearbyLiveListenControlleriOS _wirelessSplitterEnabledChanged:]
+ -[HUNearbyLiveListenControlleriOS cachedAudioLevel]
+ -[HUNearbyLiveListenControlleriOS cachedCurrentCallsCount]
+ -[HUNearbyLiveListenControlleriOS cachedHasHearingAidRoute]
+ -[HUNearbyLiveListenControlleriOS cachedHasLiveListenRoute]
+ -[HUNearbyLiveListenControlleriOS cachedIsListening]
+ -[HUNearbyLiveListenControlleriOS cachedIsPlayingBack]
+ -[HUNearbyLiveListenControlleriOS cachedNearbyDevices]
+ -[HUNearbyLiveListenControlleriOS cachedNearbyIsPlayingBack]
+ -[HUNearbyLiveListenControlleriOS cachedNearbyState]
+ -[HUNearbyLiveListenControlleriOS cachedNearbyTranscription]
+ -[HUNearbyLiveListenControlleriOS cachedTranscription]
+ -[HUNearbyLiveListenControlleriOS cachedWirelessSplitterEnabled]
+ -[HUNearbyLiveListenControlleriOS controller]
+ -[HUNearbyLiveListenControlleriOS currentAudioDeviceName]
+ -[HUNearbyLiveListenControlleriOS currentAudioDeviceType]
+ -[HUNearbyLiveListenControlleriOS deviceDiscoveryManager:updatedDevices:]
+ -[HUNearbyLiveListenControlleriOS discoveredNearbyDeviceIdentifiers]
+ -[HUNearbyLiveListenControlleriOS discoveryManager]
+ -[HUNearbyLiveListenControlleriOS initWithController:]
+ -[HUNearbyLiveListenControlleriOS lastUpdateStateTimestamp]
+ -[HUNearbyLiveListenControlleriOS liveListenObserver]
+ -[HUNearbyLiveListenControlleriOS notifiedDevices]
+ -[HUNearbyLiveListenControlleriOS observingDevices]
+ -[HUNearbyLiveListenControlleriOS pendingMessage]
+ -[HUNearbyLiveListenControlleriOS remoteStartDevice]
+ -[HUNearbyLiveListenControlleriOS setCachedAudioLevel:]
+ -[HUNearbyLiveListenControlleriOS setCachedCurrentCallsCount:]
+ -[HUNearbyLiveListenControlleriOS setCachedHasHearingAidRoute:]
+ -[HUNearbyLiveListenControlleriOS setCachedHasLiveListenRoute:]
+ -[HUNearbyLiveListenControlleriOS setCachedIsListening:]
+ -[HUNearbyLiveListenControlleriOS setCachedIsPlayingBack:]
+ -[HUNearbyLiveListenControlleriOS setCachedNearbyDevices:]
+ -[HUNearbyLiveListenControlleriOS setCachedNearbyIsPlayingBack:]
+ -[HUNearbyLiveListenControlleriOS setCachedNearbyState:]
+ -[HUNearbyLiveListenControlleriOS setCachedNearbyTranscription:]
+ -[HUNearbyLiveListenControlleriOS setCachedTranscription:]
+ -[HUNearbyLiveListenControlleriOS setCachedWirelessSplitterEnabled:]
+ -[HUNearbyLiveListenControlleriOS setController:]
+ -[HUNearbyLiveListenControlleriOS setCurrentAudioDeviceName:]
+ -[HUNearbyLiveListenControlleriOS setCurrentAudioDeviceType:]
+ -[HUNearbyLiveListenControlleriOS setDiscoveredNearbyDeviceIdentifiers:]
+ -[HUNearbyLiveListenControlleriOS setDiscoveryManager:]
+ -[HUNearbyLiveListenControlleriOS setLastUpdateStateTimestamp:]
+ -[HUNearbyLiveListenControlleriOS setLiveListenObserver:]
+ -[HUNearbyLiveListenControlleriOS setNotifiedDevices:]
+ -[HUNearbyLiveListenControlleriOS setObservingDevices:]
+ -[HUNearbyLiveListenControlleriOS setPendingMessage:]
+ -[HUNearbyLiveListenControlleriOS setRemoteStartDevice:]
+ -[HUNearbyLiveListenControlleriOS setUpdateQueue:]
+ -[HUNearbyLiveListenControlleriOS setUpdateStateTimer:]
+ -[HUNearbyLiveListenControlleriOS startLiveListenRewind]
+ -[HUNearbyLiveListenControlleriOS startLiveListen]
+ -[HUNearbyLiveListenControlleriOS startObservingRemoteSession]
+ -[HUNearbyLiveListenControlleriOS startObserving]
+ -[HUNearbyLiveListenControlleriOS stopLiveListenRewind]
+ -[HUNearbyLiveListenControlleriOS stopLiveListen]
+ -[HUNearbyLiveListenControlleriOS stopObservingRemoteSession]
+ -[HUNearbyLiveListenControlleriOS stopObserving]
+ -[HUNearbyLiveListenControlleriOS updateQueue]
+ -[HUNearbyLiveListenControlleriOS updateStateTimer]
+ -[HUNoiseController _initializeInternalDataCollectionIfNeeded]
+ -[HUNoiseController _internalDataCollectionLogSPLValue:metaData:]
+ -[HUNoiseController addNoiseSample:toCircularBuffer:forMinTime:]
+ -[HUNoiseController internalDataCollectionEnabled]
+ -[HUNoiseController internalDataCollectionQueue]
+ -[HUNoiseController latestNoiseSampleWasBuffered]
+ -[HUNoiseController setInternalDataCollectionEnabled:]
+ -[HUNoiseController setInternalDataCollectionQueue:]
+ -[HUNoiseController setLatestNoiseSampleWasBuffered:]
+ -[HUNoiseController shouldEnableNoiseMeasurements]
+ -[HUNoiseSample description]
+ -[HUNoiseSample initWithRepresentation:]
+ -[HUNoiseSample transportRepresentation]
+ -[HUNoiseSettings contextualVolumeNeedsEnvironmentalMeasurements]
+ -[HUNoiseSettings internalDataCollectionEnabled]
+ -[HURingBuffer .cxx_destruct]
+ -[HURingBuffer addObject:]
+ -[HURingBuffer content]
+ -[HURingBuffer copyWithZone:]
+ -[HURingBuffer count]
+ -[HURingBuffer initWithCount:]
+ -[HURingBuffer reset]
+ -[HURoutesManager fetchCurrentPickableAudioRoutesIfNeeded].cold.1
+ -[HURoutesManager fetchCurrentPickableAudioRoutesIfNeeded].cold.2
+ -[HUWrappedAudioQueue .cxx_destruct]
+ -[HUWrappedAudioQueue _attemptQueueStart]
+ -[HUWrappedAudioQueue _buildAudioQueue]
+ -[HUWrappedAudioQueue _minimumBufferByteSize]
+ -[HUWrappedAudioQueue _rebuildAudioQueue]
+ -[HUWrappedAudioQueue _reconfigureQueueFormatForMultiChannelOutputIfNecessary]
+ -[HUWrappedAudioQueue _scheduleDeferredStop]
+ -[HUWrappedAudioQueue _startQueueWithRetry]
+ -[HUWrappedAudioQueue _tearDownAudioQueue]
+ -[HUWrappedAudioQueue aqRef]
+ -[HUWrappedAudioQueue aqTimeline]
+ -[HUWrappedAudioQueue audioDevice]
+ -[HUWrappedAudioQueue audioQueueActive]
+ -[HUWrappedAudioQueue audioQueueFlags]
+ -[HUWrappedAudioQueue availableBuffers]
+ -[HUWrappedAudioQueue bufferCallback:]
+ -[HUWrappedAudioQueue buffersAvailable]
+ -[HUWrappedAudioQueue cachedAudioConverter]
+ -[HUWrappedAudioQueue convertBufferIfNecessary:]
+ -[HUWrappedAudioQueue dealloc]
+ -[HUWrappedAudioQueue deferredStopQueue]
+ -[HUWrappedAudioQueue deferredStopSource]
+ -[HUWrappedAudioQueue format]
+ -[HUWrappedAudioQueue handleMediaServicesReset]
+ -[HUWrappedAudioQueue inflightBuffers]
+ -[HUWrappedAudioQueue initWithSampleRate:]
+ -[HUWrappedAudioQueue init]
+ -[HUWrappedAudioQueue isRunning]
+ -[HUWrappedAudioQueue pause]
+ -[HUWrappedAudioQueue play]
+ -[HUWrappedAudioQueue queueFormat]
+ -[HUWrappedAudioQueue scheduleBuffer:completionHandler:]
+ -[HUWrappedAudioQueue scheduleBuffer:completionHandler:lastBuffer:]
+ -[HUWrappedAudioQueue setAqRef:]
+ -[HUWrappedAudioQueue setAqTimeline:]
+ -[HUWrappedAudioQueue setAudioDevice:]
+ -[HUWrappedAudioQueue setAudioQueueActive:]
+ -[HUWrappedAudioQueue setAudioQueueFlags:]
+ -[HUWrappedAudioQueue setAvailableBuffers:]
+ -[HUWrappedAudioQueue setBuffersAvailable:]
+ -[HUWrappedAudioQueue setCachedAudioConverter:]
+ -[HUWrappedAudioQueue setDeferredStopQueue:]
+ -[HUWrappedAudioQueue setDeferredStopSource:]
+ -[HUWrappedAudioQueue setFormat:]
+ -[HUWrappedAudioQueue setInflightBuffers:]
+ -[HUWrappedAudioQueue setOutputFormat:]
+ -[HUWrappedAudioQueue setQueueFormat:]
+ -[HUWrappedAudioQueue setShouldRebuildAudioQueue:]
+ -[HUWrappedAudioQueue setStartedOn:]
+ -[HUWrappedAudioQueue setState:]
+ -[HUWrappedAudioQueue shouldRebuildAudioQueue]
+ -[HUWrappedAudioQueue startedOn]
+ -[HUWrappedAudioQueue state]
+ -[HUWrappedAudioQueue stop]
+ -[HUWrappedAudioQueueBuffer .cxx_destruct]
+ -[HUWrappedAudioQueueBuffer aqBuffer]
+ -[HUWrappedAudioQueueBuffer byteSize]
+ -[HUWrappedAudioQueueBuffer completionHandler]
+ -[HUWrappedAudioQueueBuffer setAqBuffer:]
+ -[HUWrappedAudioQueueBuffer setCompletionHandler:]
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table123
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table135
+ GCC_except_table141
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table154
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table18
+ GCC_except_table57
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table89
+ GCC_except_table90
+ GCC_except_table94
+ GCC_except_table96
+ GCC_except_table97
+ _AXIsInternalInstall
+ _AXLEAudioServiceUUIDString
+ _AccessibilityRemoteServicesLibraryCore.frameworkLibrary
+ _AudioAccessoryServicesLibraryCore
+ _AudioAccessoryServicesLibraryCore.frameworkLibrary
+ _AudioObjectGetPropertyData
+ _AudioQueueAddPropertyListener
+ _AudioQueueAllocateBuffer
+ _AudioQueueCreateTimeline
+ _AudioQueueDispose
+ _AudioQueueEnqueueBuffer
+ _AudioQueueFlush
+ _AudioQueueFreeBuffer
+ _AudioQueueGetProperty
+ _AudioQueueNewOutput
+ _AudioQueuePause
+ _AudioQueueRemovePropertyListener
+ _AudioQueueReset
+ _AudioQueueSetProperty
+ _AudioQueueStart
+ _AudioQueueStop
+ _AudioServicesPlaySystemSoundWithOptions
+ _CBAdvertisementDataServiceDataKey
+ _HCMessageUUIDKey
+ _HUEDSampleIntervalKey
+ _HULiveListenIDSDomain
+ _HULiveListenIDSMessageIsPlayingBackKey
+ _HULiveListenIDSMessageShouldStartKey
+ _HULiveListenIDSMessageStateKey
+ _HULiveListenIDSMessageTranscriptionKey
+ _HULiveListenIDSMessageTypeKey
+ _HULiveListenRemoteDeviceEndDateKey
+ _HULiveListenRemoteDeviceNameKey
+ _HULiveListenRemoteDeviceStartDateKey
+ _LiveListenNotificationCenter
+ _LiveListenNotificationCenter.cold.1
+ _LiveListenNotificationCenter.liveListenNotificationCenter
+ _LiveListenNotificationCenter.onceToken
+ _LiveListenRequestNotificationAuthorization
+ _LiveListenSendObservingNotificationForDevice
+ _LiveListenSendStartedNotificationForDevice
+ _LiveTranscriptionLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_AVAudioConverter
+ _OBJC_CLASS_$_AVAudioMixerNode
+ _OBJC_CLASS_$_AVAudioPCMBuffer
+ _OBJC_CLASS_$_AVAudioUnitEQ
+ _OBJC_CLASS_$_AXHearingAidLEAudioDevice
+ _OBJC_CLASS_$_CBDevice
+ _OBJC_CLASS_$_CBDeviceSettings
+ _OBJC_CLASS_$_HUAudioBuffer
+ _OBJC_CLASS_$_HUComfortSoundsFilterPoint
+ _OBJC_CLASS_$_HULiveListenObserver
+ _OBJC_CLASS_$_HULiveListenTranscriptionController
+ _OBJC_CLASS_$_HUNearbyLiveListenController
+ _OBJC_CLASS_$_HUNearbyLiveListenControllerWatch
+ _OBJC_CLASS_$_HUNearbyLiveListenControlleriOS
+ _OBJC_CLASS_$_HURingBuffer
+ _OBJC_CLASS_$_HUWrappedAudioQueue
+ _OBJC_CLASS_$_HUWrappedAudioQueueBuffer
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_NSDateComponentsFormatter
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_TUCallCenter
+ _OBJC_IVAR_$_AXHAController._liveListenCountsPerClient
+ _OBJC_IVAR_$_AXHearingAidDevice._leftRSSI
+ _OBJC_IVAR_$_AXHearingAidDevice._rightRSSI
+ _OBJC_IVAR_$_AXHearingAidDeviceController._leAudioSessionInfo
+ _OBJC_IVAR_$_AXHearingAidDeviceController._stoppedScanningForLEAudio
+ _OBJC_IVAR_$_AXHearingAidLEAudioDevice._isLeftEventHandlerSet
+ _OBJC_IVAR_$_AXHearingAidLEAudioDevice._isRightEventHandlerSet
+ _OBJC_IVAR_$_AXHearingAidLEAudioDevice._leftLoadedProperties
+ _OBJC_IVAR_$_AXHearingAidLEAudioDevice._rightLoadedProperties
+ _OBJC_IVAR_$_AXRemoteHearingAidDevice._RSSI
+ _OBJC_IVAR_$_AXRemoteHearingAidDevice._deviceProtocol
+ _OBJC_IVAR_$_HUAccessoryManager._aaDeviceManager
+ _OBJC_IVAR_$_HUAccessoryManager._attributeUpdateUpdates
+ _OBJC_IVAR_$_HUAudioBuffer._bufferList
+ _OBJC_IVAR_$_HUComfortSound._volume
+ _OBJC_IVAR_$_HUComfortSoundsController._activeDurationTimerEndTimeStampCache
+ _OBJC_IVAR_$_HUComfortSoundsController._audioPlayerFilterNode
+ _OBJC_IVAR_$_HUComfortSoundsController._audioPlayerMixerNode
+ _OBJC_IVAR_$_HUComfortSoundsController._comfortSoundsEnabledCache
+ _OBJC_IVAR_$_HUComfortSoundsController._isSettingUpPreviewComfortSounds
+ _OBJC_IVAR_$_HUComfortSoundsController._isSettingUpPreviewTimer
+ _OBJC_IVAR_$_HUComfortSoundsController._playbackTimer
+ _OBJC_IVAR_$_HUComfortSoundsController._timerEnabledCache
+ _OBJC_IVAR_$_HUComfortSoundsFilterPoint._xValue
+ _OBJC_IVAR_$_HUComfortSoundsFilterPoint._yValue
+ _OBJC_IVAR_$_HULiveListenController._audioQueue
+ _OBJC_IVAR_$_HULiveListenController._audioRingBuffer
+ _OBJC_IVAR_$_HULiveListenController._isPlayingBack
+ _OBJC_IVAR_$_HULiveListenController._playbackQueue
+ _OBJC_IVAR_$_HULiveListenController._sessionTranscriptions
+ _OBJC_IVAR_$_HULiveListenController._transcriber
+ _OBJC_IVAR_$_HULiveListenController._transcription
+ _OBJC_IVAR_$_HULiveListenObserver._controller
+ _OBJC_IVAR_$_HULiveListenObserver._liveListenLevelsTimer
+ _OBJC_IVAR_$_HULiveListenObserver._updateBlocks
+ _OBJC_IVAR_$_HULiveListenObserver._updateLock
+ _OBJC_IVAR_$_HULiveListenTranscriptionController._currentTranscription
+ _OBJC_IVAR_$_HULiveListenTranscriptionController._delegate
+ _OBJC_IVAR_$_HULiveListenTranscriptionController._isTranscribing
+ _OBJC_IVAR_$_HULiveListenTranscriptionController._sessionTranscriptions
+ _OBJC_IVAR_$_HULiveListenTranscriptionController._transcriber
+ _OBJC_IVAR_$_HUNearbyController._messagesCount
+ _OBJC_IVAR_$_HUNearbyLiveListenController._audioLevel
+ _OBJC_IVAR_$_HUNearbyLiveListenController._deviceImplementation
+ _OBJC_IVAR_$_HUNearbyLiveListenController._isPlayingBack
+ _OBJC_IVAR_$_HUNearbyLiveListenController._state
+ _OBJC_IVAR_$_HUNearbyLiveListenController._transcription
+ _OBJC_IVAR_$_HUNearbyLiveListenController._updateBlocks
+ _OBJC_IVAR_$_HUNearbyLiveListenController._updateLock
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._cachedIsPlayingBack
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._cachedNearbyDevices
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._cachedState
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._cachedTranscription
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._controller
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._updateQueue
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedAudioLevel
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedCurrentCallsCount
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedHasHearingAidRoute
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedHasLiveListenRoute
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedIsListening
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedIsPlayingBack
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedNearbyDevices
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedNearbyIsPlayingBack
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedNearbyState
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedNearbyTranscription
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedTranscription
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._cachedWirelessSplitterEnabled
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._controller
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._currentAudioDeviceName
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._currentAudioDeviceType
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._discoveredNearbyDeviceIdentifiers
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._discoveryManager
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._lastUpdateStateTimestamp
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._liveListenObserver
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._notifiedDevices
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._observingDevices
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._pendingMessage
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._remoteStartDevice
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._updateQueue
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._updateStateTimer
+ _OBJC_IVAR_$_HUNoiseController._internalDataCollectionEnabled
+ _OBJC_IVAR_$_HUNoiseController._internalDataCollectionQueue
+ _OBJC_IVAR_$_HUNoiseController._latestNoiseSampleWasBuffered
+ _OBJC_IVAR_$_HURingBuffer._bufferArray
+ _OBJC_IVAR_$_HURingBuffer._head
+ _OBJC_IVAR_$_HURingBuffer._size
+ _OBJC_IVAR_$_HUWrappedAudioQueue._aqRef
+ _OBJC_IVAR_$_HUWrappedAudioQueue._aqTimeline
+ _OBJC_IVAR_$_HUWrappedAudioQueue._audioDevice
+ _OBJC_IVAR_$_HUWrappedAudioQueue._audioQueueActive
+ _OBJC_IVAR_$_HUWrappedAudioQueue._audioQueueFlags
+ _OBJC_IVAR_$_HUWrappedAudioQueue._audioQueueLock
+ _OBJC_IVAR_$_HUWrappedAudioQueue._availableBuffers
+ _OBJC_IVAR_$_HUWrappedAudioQueue._bufferLock
+ _OBJC_IVAR_$_HUWrappedAudioQueue._buffersAvailable
+ _OBJC_IVAR_$_HUWrappedAudioQueue._cachedAudioConverter
+ _OBJC_IVAR_$_HUWrappedAudioQueue._deferredStopQueue
+ _OBJC_IVAR_$_HUWrappedAudioQueue._deferredStopSource
+ _OBJC_IVAR_$_HUWrappedAudioQueue._format
+ _OBJC_IVAR_$_HUWrappedAudioQueue._inflightBuffers
+ _OBJC_IVAR_$_HUWrappedAudioQueue._queueFormat
+ _OBJC_IVAR_$_HUWrappedAudioQueue._shouldRebuildAudioQueue
+ _OBJC_IVAR_$_HUWrappedAudioQueue._startedOn
+ _OBJC_IVAR_$_HUWrappedAudioQueue._state
+ _OBJC_IVAR_$_HUWrappedAudioQueueBuffer._aqBuffer
+ _OBJC_IVAR_$_HUWrappedAudioQueueBuffer._completionHandler
+ _OBJC_METACLASS_$_AXHearingAidLEAudioDevice
+ _OBJC_METACLASS_$_HUAudioBuffer
+ _OBJC_METACLASS_$_HUComfortSoundsFilterPoint
+ _OBJC_METACLASS_$_HULiveListenObserver
+ _OBJC_METACLASS_$_HULiveListenTranscriptionController
+ _OBJC_METACLASS_$_HUNearbyLiveListenController
+ _OBJC_METACLASS_$_HUNearbyLiveListenControllerWatch
+ _OBJC_METACLASS_$_HUNearbyLiveListenControlleriOS
+ _OBJC_METACLASS_$_HURingBuffer
+ _OBJC_METACLASS_$_HUWrappedAudioQueue
+ _OBJC_METACLASS_$_HUWrappedAudioQueueBuffer
+ _UserNotificationsLibrary
+ _UserNotificationsLibraryCore.frameworkLibrary
+ _WrappedAudioQueueCallback
+ _WrappedAudioQueueRunningStateChanged
+ __AXSUpdateAccessibilityEnabled
+ __LiveListenSendUserNotification
+ __OBJC_$_CATEGORY_CBDevice_$__HUAccessory_
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CBDevice_$__HUAccessory_
+ __OBJC_$_CLASS_METHODS_HUComfortSoundsFilterPoint
+ __OBJC_$_CLASS_METHODS_HUNearbyLiveListenController
+ __OBJC_$_CLASS_PROP_LIST_HUComfortSoundsFilterPoint
+ __OBJC_$_CLASS_PROP_LIST_HUNearbyLiveListenController
+ __OBJC_$_INSTANCE_METHODS_AXHearingAidLEAudioDevice
+ __OBJC_$_INSTANCE_METHODS_HUAudioBuffer
+ __OBJC_$_INSTANCE_METHODS_HUComfortSoundsFilterPoint
+ __OBJC_$_INSTANCE_METHODS_HULiveListenObserver
+ __OBJC_$_INSTANCE_METHODS_HULiveListenTranscriptionController
+ __OBJC_$_INSTANCE_METHODS_HUNearbyLiveListenController
+ __OBJC_$_INSTANCE_METHODS_HUNearbyLiveListenControllerWatch
+ __OBJC_$_INSTANCE_METHODS_HUNearbyLiveListenControlleriOS
+ __OBJC_$_INSTANCE_METHODS_HURingBuffer
+ __OBJC_$_INSTANCE_METHODS_HUWrappedAudioQueue
+ __OBJC_$_INSTANCE_METHODS_HUWrappedAudioQueueBuffer
+ __OBJC_$_INSTANCE_VARIABLES_AXHearingAidLEAudioDevice
+ __OBJC_$_INSTANCE_VARIABLES_HUAudioBuffer
+ __OBJC_$_INSTANCE_VARIABLES_HUComfortSoundsFilterPoint
+ __OBJC_$_INSTANCE_VARIABLES_HULiveListenObserver
+ __OBJC_$_INSTANCE_VARIABLES_HULiveListenTranscriptionController
+ __OBJC_$_INSTANCE_VARIABLES_HUNearbyLiveListenController
+ __OBJC_$_INSTANCE_VARIABLES_HUNearbyLiveListenControllerWatch
+ __OBJC_$_INSTANCE_VARIABLES_HUNearbyLiveListenControlleriOS
+ __OBJC_$_INSTANCE_VARIABLES_HURingBuffer
+ __OBJC_$_INSTANCE_VARIABLES_HUWrappedAudioQueue
+ __OBJC_$_INSTANCE_VARIABLES_HUWrappedAudioQueueBuffer
+ __OBJC_$_PROP_LIST_AXHearingAidLEAudioDevice
+ __OBJC_$_PROP_LIST_HUAudioBuffer
+ __OBJC_$_PROP_LIST_HUComfortSoundProtocol
+ __OBJC_$_PROP_LIST_HUComfortSoundsFilterPoint
+ __OBJC_$_PROP_LIST_HULiveListenObserver
+ __OBJC_$_PROP_LIST_HULiveListenTranscriptionController
+ __OBJC_$_PROP_LIST_HUNearbyLiveListenController
+ __OBJC_$_PROP_LIST_HUNearbyLiveListenControllerWatch
+ __OBJC_$_PROP_LIST_HUNearbyLiveListenControlleriOS
+ __OBJC_$_PROP_LIST_HURingBuffer
+ __OBJC_$_PROP_LIST_HUWrappedAudioQueue
+ __OBJC_$_PROP_LIST_HUWrappedAudioQueueBuffer
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HUNearbyLiveListenDeviceImplementation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXRDeviceDiscoveryObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HUComfortSoundProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HUComfortSoundsDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HUListenerHelperDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HULiveListenTranscriptionControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HUNearbyLiveListenDeviceImplementation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HUSynthesisProviderAudioOutput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HUComfortSoundsDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HUSynthesisProviderAudioOutput
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXRDeviceDiscoveryObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HUComfortSoundProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HUComfortSoundsDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HUListenerHelperDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HULiveListenTranscriptionControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HUNearbyLiveListenDeviceImplementation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HUSynthesisProviderAudioOutput
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_REFS_AXRDeviceDiscoveryObserver
+ __OBJC_$_PROTOCOL_REFS_HUComfortSoundProtocol
+ __OBJC_$_PROTOCOL_REFS_HUComfortSoundsDelegate
+ __OBJC_$_PROTOCOL_REFS_HUListenerHelperDelegate
+ __OBJC_$_PROTOCOL_REFS_HUNearbyLiveListenDeviceImplementation
+ __OBJC_CLASS_PROTOCOLS_$_HUAudioBuffer
+ __OBJC_CLASS_PROTOCOLS_$_HUComfortSoundsFilterPoint
+ __OBJC_CLASS_PROTOCOLS_$_HULiveListenController
+ __OBJC_CLASS_PROTOCOLS_$_HULiveListenObserver
+ __OBJC_CLASS_PROTOCOLS_$_HUNearbyLiveListenController
+ __OBJC_CLASS_PROTOCOLS_$_HUNearbyLiveListenControllerWatch
+ __OBJC_CLASS_PROTOCOLS_$_HUNearbyLiveListenControlleriOS
+ __OBJC_CLASS_PROTOCOLS_$_HURingBuffer
+ __OBJC_CLASS_PROTOCOLS_$_HUWrappedAudioQueue
+ __OBJC_CLASS_RO_$_AXHearingAidLEAudioDevice
+ __OBJC_CLASS_RO_$_HUAudioBuffer
+ __OBJC_CLASS_RO_$_HUComfortSoundsFilterPoint
+ __OBJC_CLASS_RO_$_HULiveListenObserver
+ __OBJC_CLASS_RO_$_HULiveListenTranscriptionController
+ __OBJC_CLASS_RO_$_HUNearbyLiveListenController
+ __OBJC_CLASS_RO_$_HUNearbyLiveListenControllerWatch
+ __OBJC_CLASS_RO_$_HUNearbyLiveListenControlleriOS
+ __OBJC_CLASS_RO_$_HURingBuffer
+ __OBJC_CLASS_RO_$_HUWrappedAudioQueue
+ __OBJC_CLASS_RO_$_HUWrappedAudioQueueBuffer
+ __OBJC_LABEL_PROTOCOL_$_AXRDeviceDiscoveryObserver
+ __OBJC_LABEL_PROTOCOL_$_HUComfortSoundProtocol
+ __OBJC_LABEL_PROTOCOL_$_HUComfortSoundsDelegate
+ __OBJC_LABEL_PROTOCOL_$_HUListenerHelperDelegate
+ __OBJC_LABEL_PROTOCOL_$_HULiveListenTranscriptionControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_HUNearbyLiveListenDeviceImplementation
+ __OBJC_LABEL_PROTOCOL_$_HUSynthesisProviderAudioOutput
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_AXHearingAidLEAudioDevice
+ __OBJC_METACLASS_RO_$_HUAudioBuffer
+ __OBJC_METACLASS_RO_$_HUComfortSoundsFilterPoint
+ __OBJC_METACLASS_RO_$_HULiveListenObserver
+ __OBJC_METACLASS_RO_$_HULiveListenTranscriptionController
+ __OBJC_METACLASS_RO_$_HUNearbyLiveListenController
+ __OBJC_METACLASS_RO_$_HUNearbyLiveListenControllerWatch
+ __OBJC_METACLASS_RO_$_HUNearbyLiveListenControlleriOS
+ __OBJC_METACLASS_RO_$_HURingBuffer
+ __OBJC_METACLASS_RO_$_HUWrappedAudioQueue
+ __OBJC_METACLASS_RO_$_HUWrappedAudioQueueBuffer
+ __OBJC_PROTOCOL_$_AXRDeviceDiscoveryObserver
+ __OBJC_PROTOCOL_$_HUComfortSoundProtocol
+ __OBJC_PROTOCOL_$_HUComfortSoundsDelegate
+ __OBJC_PROTOCOL_$_HUListenerHelperDelegate
+ __OBJC_PROTOCOL_$_HULiveListenTranscriptionControllerDelegate
+ __OBJC_PROTOCOL_$_HUNearbyLiveListenDeviceImplementation
+ __OBJC_PROTOCOL_$_HUSynthesisProviderAudioOutput
+ __OBJC_PROTOCOL_$_NSCopying
+ ___103-[HUNearbyLiveListenControlleriOS _isListeningChanged:audioLevel:isPlayingBack:orTranscriptionChanged:]_block_invoke
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.533
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.546
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.554
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.563
+ ___25-[HUNoiseController init]_block_invoke.322
+ ___27-[HUWrappedAudioQueue play]_block_invoke
+ ___27-[HUWrappedAudioQueue stop]_block_invoke
+ ___28-[HUWrappedAudioQueue pause]_block_invoke
+ ___32-[AXHeardController startServer]_block_invoke_30
+ ___32-[AXHeardController startServer]_block_invoke_31
+ ___32-[AXHeardController startServer]_block_invoke_32
+ ___32-[AXHeardController startServer]_block_invoke_33
+ ___32-[AXHeardController startServer]_block_invoke_34
+ ___33-[HUComfortSoundsController init]_block_invoke.21
+ ___33-[HUComfortSoundsController init]_block_invoke.34
+ ___33-[HUComfortSoundsController init]_block_invoke.38
+ ___33-[HUComfortSoundsController init]_block_invoke.45
+ ___33-[HUComfortSoundsController init]_block_invoke.52
+ ___33-[HUComfortSoundsController init]_block_invoke.59
+ ___33-[HUComfortSoundsController init]_block_invoke.72
+ ___33-[HUComfortSoundsController init]_block_invoke_2.41
+ ___33-[HUComfortSoundsController init]_block_invoke_2.48
+ ___33-[HUComfortSoundsController init]_block_invoke_2.55
+ ___33-[HUComfortSoundsController init]_block_invoke_2.62
+ ___33-[HUComfortSoundsController init]_block_invoke_3.63
+ ___34-[AXHeardController continueSetup]_block_invoke.137
+ ___34-[AXHeardController continueSetup]_block_invoke.141
+ ___34-[AXHeardController continueSetup]_block_invoke.176
+ ___34-[AXHeardController continueSetup]_block_invoke_2.144
+ ___36-[AXHeardController updateAnalytics]_block_invoke.246
+ ___37-[HUNearbyHearingAidController start]_block_invoke.101
+ ___37-[HUNearbyHearingAidController start]_block_invoke.115
+ ___37-[HUNearbyHearingAidController start]_block_invoke.120
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.116
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.121
+ ___37-[HUNearbyHearingAidController start]_block_invoke_3.123
+ ___37-[HUNearbyHearingAidController start]_block_invoke_4.124
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.411
+ ___38-[HUWrappedAudioQueue bufferCallback:]_block_invoke
+ ___39-[HULiveListenObserver removeListener:]_block_invoke
+ ___39-[HUWrappedAudioQueue _buildAudioQueue]_block_invoke
+ ___40-[AXHeardController _shutdownIfPossible]_block_invoke.193
+ ___41-[AXHeardController handleNewConnection:]_block_invoke.285
+ ___41-[AXHeardController handleNewConnection:]_block_invoke_2.286
+ ___41-[HUWrappedAudioQueue _attemptQueueStart]_block_invoke
+ ___42-[HUWrappedAudioQueue _tearDownAudioQueue]_block_invoke
+ ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.166
+ ___43-[HUAccessoryManager pseVersionForAddress:]_block_invoke
+ ___43-[HUComfortSoundsController scheduleTimer:]_block_invoke
+ ___44-[AXHearingAidDevice loadRequiredProperties]_block_invoke.224
+ ___44-[HUWrappedAudioQueue _scheduleDeferredStop]_block_invoke
+ ___44-[HUWrappedAudioQueue _scheduleDeferredStop]_block_invoke_2
+ ___44-[HUWrappedAudioQueue _scheduleDeferredStop]_block_invoke_3
+ ___45-[AXHAServer _liveListenDidUpdate_enumValue:]_block_invoke
+ ___45-[AXHearingAidDevice discoveringServiceUUIDs]_block_invoke
+ ___45-[HUNearbyHearingAidController finishHandoff]_block_invoke
+ ___46+[HUNearbyLiveListenController sharedInstance]_block_invoke
+ ___46-[AXHearingAidDevice updateInputTagsAndReset:]_block_invoke.319
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_10
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_11
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_12
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_12.cold.1
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_13
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_14
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_15
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_16
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_9
+ ___46-[HUNearbyController checkSCIDSServiceDevices]_block_invoke
+ ___47-[HUAccessoryManager setSSLEnabled:forAddress:]_block_invoke
+ ___47-[HUAccessoryManager setSSLEnabled:forAddress:]_block_invoke_2
+ ___47-[HULiveListenController startLiveListenRewind]_block_invoke
+ ___47-[HULiveListenController startLiveListenRewind]_block_invoke_2
+ ___47-[HULiveListenController startLiveListenRewind]_block_invoke_3
+ ___47-[HUNearbyLiveListenController removeListener:]_block_invoke
+ ___47-[HUWrappedAudioQueue handleMediaServicesReset]_block_invoke
+ ___48-[AXHearingAidDevice propertyForCharacteristic:]_block_invoke
+ ___48-[HUWrappedAudioQueue convertBufferIfNecessary:]_block_invoke
+ ___49-[HUAccessoryManager getPairedDeviceSupportsPSE:]_block_invoke
+ ___49-[HUAccessoryManager getPairedDeviceSupportsPSE:]_block_invoke_2
+ ___49-[HUHeadphoneLevelController _startIDSConnection]_block_invoke.cold.1
+ ___49-[HUNearbyController stopDiscoveringSCIDSService]_block_invoke.154
+ ___49-[HUNearbyLiveListenControlleriOS _nearbyDevices]_block_invoke
+ ___49-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke
+ ___49-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke_2
+ ___49-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke_3
+ ___49-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke_4
+ ___51-[HUAccessoryManager setCurrentRouteListeningMode:]_block_invoke
+ ___51-[HUAccessoryManager setCurrentRouteListeningMode:]_block_invoke_2
+ ___51-[HUNearbyLiveListenControllerWatch startObserving]_block_invoke
+ ___51-[HUNearbyLiveListenControllerWatch startObserving]_block_invoke_2
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.638
+ ___52-[AXHearingAidDeviceController connectToPeripheral:]_block_invoke.84
+ ___52-[AXHearingAidDeviceController scanningServiceUUIDs]_block_invoke
+ ___52-[AXHearingAidLEAudioDevice discoveringServiceUUIDs]_block_invoke
+ ___52-[HUAccessoryManager turnBluetoothOnWithCompletion:]_block_invoke
+ ___52-[HUAccessoryManager turnBluetoothOnWithCompletion:]_block_invoke_2
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.79
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.88
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.92
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke.95
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke_2
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke_3
+ ___52-[HUComfortSoundsController listenForChangesInTimer]_block_invoke_4
+ ___52-[HUNearbyLiveListenControlleriOS _devicesToMessage]_block_invoke
+ ___53-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke.116
+ ___53-[AXHeardController updateHearingControlCenterModule]_block_invoke.111
+ ___53-[AXHearingAidLEAudioDevice setNotify:forPeripheral:]_block_invoke
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.437
+ ___54-[AXHearingAidDeviceController clearPairedHearingAids]_block_invoke
+ ___54-[AXHearingAidDeviceController clearPairedHearingAids]_block_invoke_2
+ ___54-[HUNearbyLiveListenControlleriOS initWithController:]_block_invoke
+ ___54-[HUNearbyLiveListenControlleriOS initWithController:]_block_invoke_2
+ ___55-[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]_block_invoke
+ ___55-[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]_block_invoke.cold.1
+ ___55-[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]_block_invoke.cold.2
+ ___55-[HUAccessoryManager pmeEverywhereSupportedForAddress:]_block_invoke
+ ___55-[HULiveListenTranscriptionController stopTranscribing]_block_invoke
+ ___55-[HULiveListenTranscriptionController stopTranscribing]_block_invoke.cold.1
+ ___55-[HUNearbyLiveListenControlleriOS _audioRoutesChanged:]_block_invoke
+ ___55-[HUNearbyLiveListenControlleriOS _callsStatusChanged:]_block_invoke
+ ___55-[HUNearbyLiveListenControlleriOS _callsStatusChanged:]_block_invoke_2
+ ___55-[HUNearbyLiveListenControlleriOS _scheduleStateUpdate]_block_invoke
+ ___55-[HUNearbyLiveListenControlleriOS _scheduleStateUpdate]_block_invoke_2
+ ___56-[AXHearingAidDevice _initCharacteristicsForPeripheral:]_block_invoke
+ ___56-[AXHearingAidDevice _initCharacteristicsForPeripheral:]_block_invoke_2
+ ___56-[AXHearingAidDeviceController cancelPendingConnections]_block_invoke.92
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke.103
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke.113
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke_2
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke_3
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke_4
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke_5
+ ___56-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke_6
+ ___56-[HULiveListenTranscriptionController startTranscribing]_block_invoke
+ ___56-[HULiveListenTranscriptionController startTranscribing]_block_invoke.cold.1
+ ___56-[HULiveListenTranscriptionController startTranscribing]_block_invoke_2
+ ___56-[HUNearbyLiveListenControlleriOS _nearbyDevicesChanged]_block_invoke
+ ___56-[HUWrappedAudioQueue scheduleBuffer:completionHandler:]_block_invoke
+ ___56-[HUWrappedAudioQueue scheduleBuffer:completionHandler:]_block_invoke_2
+ ___56-[HUWrappedAudioQueue scheduleBuffer:completionHandler:]_block_invoke_3
+ ___56-[HUWrappedAudioQueue scheduleBuffer:completionHandler:]_block_invoke_4
+ ___56-[HUWrappedAudioQueue scheduleBuffer:completionHandler:]_block_invoke_5
+ ___58-[AXHAController _registerForLiveListenUpdates_enumValue:]_block_invoke
+ ___58-[AXHAController _registerForLiveListenUpdates_enumValue:]_block_invoke.cold.1
+ ___58-[AXHAServer registerListener:forLiveListenLevelsHandler:]_block_invoke
+ ___58-[AXHearingAidDeviceController hearingAidForPeripheralID:]_block_invoke
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.256
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.260
+ ___58-[HUNearbyLiveListenControllerWatch _nearbyDevicesChanged]_block_invoke
+ ___58-[HUNearbyLiveListenControllerWatch _nearbyDevicesChanged]_block_invoke_2
+ ___58-[HUNearbyLiveListenControlleriOS _sendLatestNearbyUpdate]_block_invoke
+ ___58-[HURoutesManager fetchCurrentPickableAudioRoutesIfNeeded]_block_invoke.24
+ ___59-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke.42
+ ___59-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke_2
+ ___59-[HULiveListenObserver _pollLiveListenAudioLevelAfterDelay]_block_invoke
+ ___59-[HUNearbyHearingAidController sendMessagesPriorityDefault]_block_invoke.173
+ ___61-[AXHAServer requestNoiseBuffersForTimeInterval:withHandler:]_block_invoke
+ ___61-[AXHAServer requestNoiseBuffersForTimeInterval:withHandler:]_block_invoke_2
+ ___61-[AXHAServer requestNoiseBuffersForTimeInterval:withHandler:]_block_invoke_3
+ ___61-[AXHearingAidDeviceController setupCentralManagerForLEAudio]_block_invoke
+ ___61-[HUAccessoryManager getPSEVersionForAddress:withCompletion:]_block_invoke
+ ___61-[HUAccessoryManager getSSLEnabledForAddress:withCompletion:]_block_invoke
+ ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke
+ ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.48
+ ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.48.cold.1
+ ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.cold.1
+ ___62-[HUAccessoryManager getProductCodeforAddress:withCompletion:]_block_invoke
+ ___62-[HUNoiseController _initializeInternalDataCollectionIfNeeded]_block_invoke
+ ___63-[AXHearingAidDeviceController isLEAudioServiceInServiceUUIDs:]_block_invoke
+ ___63-[HUAccessoryManager enumerateAudioBluetoothDevicesUsingBlock:]_block_invoke
+ ___63-[HUAccessoryManager enumerateAudioBluetoothDevicesUsingBlock:]_block_invoke_2
+ ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke
+ ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke_2
+ ___63-[HUAccessoryManager getCBDeviceForCurrentRouteWithCompletion:]_block_invoke_3
+ ___63-[HUAccessoryManager registerBluetoothStateBlock:withListener:]_block_invoke_2
+ ___63-[HUNearbyLiveListenControlleriOS _notifyAboutObservingDevice:]_block_invoke
+ ___64-[HUAccessoryManager registerAttributeUpdateBlock:withListener:]_block_invoke
+ ___65-[HUAccessoryManager getCurrentRouteListeningModeWithCompletion:]_block_invoke
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.179
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.183
+ ___65-[HUNearbyLiveListenControllerWatch _receivedMessage:fromDevice:]_block_invoke
+ ___65-[HUNoiseController _internalDataCollectionLogSPLValue:metaData:]_block_invoke
+ ___65-[HUNoiseController _internalDataCollectionLogSPLValue:metaData:]_block_invoke.cold.1
+ ___65-[HUNoiseController _internalDataCollectionLogSPLValue:metaData:]_block_invoke.cold.2
+ ___66-[HUAccessoryManager enumerateProductCodesforAddresses:withBlock:]_block_invoke
+ ___66-[HUAccessoryManager getSSLSupportStateForAddress:withCompletion:]_block_invoke
+ ___67-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]_block_invoke.219
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.53
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.54
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.62
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2.64
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.108
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.91
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.99
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.103
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.92
+ ___67-[HUNearbyLiveListenControlleriOS _stopLiveListenFromRemoteDevice:]_block_invoke
+ ___67-[HUNearbyLiveListenControlleriOS _stopLiveListenFromRemoteDevice:]_block_invoke.cold.1
+ ___67-[HUNearbyLiveListenControlleriOS _wirelessSplitterEnabledChanged:]_block_invoke
+ ___67-[HUWrappedAudioQueue scheduleBuffer:completionHandler:lastBuffer:]_block_invoke
+ ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke
+ ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke.80
+ ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke_2
+ ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke_3
+ ___68-[HUNearbyLiveListenControlleriOS _startLiveListenFromRemoteDevice:]_block_invoke
+ ___68-[HUNearbyLiveListenControlleriOS _startLiveListenFromRemoteDevice:]_block_invoke.cold.1
+ ___69-[AXHearingAidLEAudioDevice availablePropertiesFromDISForPeripheral:]_block_invoke
+ ___69-[AXHearingAidLEAudioDevice availablePropertiesFromDISForPeripheral:]_block_invoke_2
+ ___69-[AXHearingAidLEAudioDevice setupUpdatesHandlerForLEAudioPeripheral:]_block_invoke
+ ___69-[HUComfortSoundsController calculateVolumeForSessionWithCompletion:]_block_invoke
+ ___69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke.219
+ ___71-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke.145
+ ___71-[HUAccessoryManager enumerateAvailableDevicesWithBlock:andCompletion:]_block_invoke
+ ___71-[HUNoiseController shouldShowHearingProtectionSuggestionForAlertType:]_block_invoke_2
+ ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke
+ ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.1
+ ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.2
+ ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.3
+ ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.4
+ ___73-[HUNearbyLiveListenControlleriOS _handleStartObservingFromRemoteDevice:]_block_invoke
+ ___73-[HUNearbyLiveListenControlleriOS _handleStateChangedMessage:fromDevice:]_block_invoke
+ ___73-[HUNearbyLiveListenControlleriOS deviceDiscoveryManager:updatedDevices:]_block_invoke
+ ___73-[HUNearbyLiveListenControlleriOS deviceDiscoveryManager:updatedDevices:]_block_invoke_2
+ ___74-[HUAccessoryManager enumerateAvailablePSEDevicesWithBlock:andCompletion:]_block_invoke
+ ___74-[HUNearbyController discoverSCIDSServiceWithDevicesUpdates:messageBlock:]_block_invoke.153
+ ___75-[HUAccessoryManager getHearingProtectionSupportforAddress:withCompletion:]_block_invoke
+ ___76-[HUAccessoryManager getPMEEverywhereSupportStateForAddress:withCompletion:]_block_invoke
+ ___79-[HUNearbyLiveListenControlleriOS _handleRequestCurrentStateMessageFromDevice:]_block_invoke
+ ___82-[HUAccessoryManager enumerateConnectedBluetoothDevices:usingBlock:andCompletion:]_block_invoke
+ ___82-[HUAccessoryManager enumerateConnectedBluetoothDevices:usingBlock:andCompletion:]_block_invoke_2
+ ___85-[HUAccessoryManager getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:]_block_invoke
+ ___85-[HUAccessoryManager getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:]_block_invoke.cold.1
+ ___85-[HUAccessoryManager getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:]_block_invoke.cold.2
+ ___85-[HUNearbyLiveListenControlleriOS _handleStartOrStopMessageFromRemoteDevice:message:]_block_invoke
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.477
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.497
+ ___91-[HUNearbyLiveListenControlleriOS _handleStartOrStopRewindMessageFromRemoteDevice:message:]_block_invoke
+ ___AccessibilityRemoteServicesLibraryCore_block_invoke
+ ___AudioAccessoryServicesLibraryCore_block_invoke
+ ___Block_byref_object_copy_.36
+ ___Block_byref_object_dispose_.37
+ ___LiveListenNotificationCenter_block_invoke
+ ___LiveListenRequestNotificationAuthorization_block_invoke
+ ___LiveTranscriptionLibraryCore_block_invoke
+ ___UserNotificationsLibraryCore_block_invoke
+ ____LiveListenSendUserNotification_block_invoke
+ ____LiveListenSendUserNotification_block_invoke.53
+ ___block_descriptor_32_e27_24?0"AXRemoteDevice"8Q16l
+ ___block_descriptor_32_e32_v16?0"UNNotificationSettings"8l
+ ___block_descriptor_32_e44_v44?0"NSDictionary"8Q16"NSString"24B32Q36l
+ ___block_descriptor_32_e49_v16?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8l
+ ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32bs_e25_v32?0"CBDevice"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e27_v36?0d8q16B24"NSString"28ls32l8
+ ___block_descriptor_40_e8_32bs_e37_v32?0"AudioAccessoryDevice"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e38_v40?0"NSString"8"NSString"16Q24^B32ls32l8
+ ___block_descriptor_40_e8_32r_e25_v32?0"CBDevice"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32r_e25_v32?0"NSString"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32r_e47_v64?0"NSString"8"NSString"16Q24Q32Q40Q48^B56lr32l8
+ ___block_descriptor_40_e8_32s_e27_v32?0q8f16B20"NSString"24ls32l8
+ ___block_descriptor_40_e8_32s_e29_v16?0"AXLTTranscribedData"8ls32l8
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSArray"16ls32l8
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSUUID"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e41_B32?0"HUIdentifierAndBlockPair"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?0d8ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e18_v16?0"NSString"8lw32l8
+ ___block_descriptor_40_e8_32w_e27_v28?0B8f12B16"NSString"20lw32l8
+ ___block_descriptor_40_e8_32w_e30_v16?0"AudioAccessoryDevice"8lw32l8
+ ___block_descriptor_40_e8_32w_e38_v40?0"NSString"8"NSString"16Q24^B32lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_41_e8_32s_e8_v16?0d8ls32l8
+ ___block_descriptor_42_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e25_v32?0"CBDevice"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e35_v24?0"CBDevice"8"NSDictionary"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e37_v32?0"AudioAccessoryDevice"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e23_v32?0"CBUUID"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"CBDevice"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e27_"AVAudioBuffer"20?0I8^q12lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e33_v32?0"CBCharacteristic"8Q16^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e37_v32?0"AudioAccessoryDevice"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e38_v40?0"NSString"8"NSString"16Q24^B32ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e31_v16?0"CBLEAudioSessionEvent"8ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e57_v24?0"CBPeripheral"8"CBLEAudioPeripheralUpdateEvent"16ls32l8w40l8
+ ___block_descriptor_48_e8_32s_e35_v24?0"CBDevice"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_49_e8_32bs40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e25_v32?0"CBDevice"8Q16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e26_v32?0"CBService"8Q16^B24ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e17_v16?0"NSArray"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56r_e23_v32?0"CBUUID"8Q16^B24ls32l8r56l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.100
+ ___block_literal_global.102
+ ___block_literal_global.107
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.114
+ ___block_literal_global.128
+ ___block_literal_global.13
+ ___block_literal_global.140
+ ___block_literal_global.146
+ ___block_literal_global.148
+ ___block_literal_global.16
+ ___block_literal_global.179
+ ___block_literal_global.197
+ ___block_literal_global.198
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.218
+ ___block_literal_global.221
+ ___block_literal_global.224
+ ___block_literal_global.227
+ ___block_literal_global.244
+ ___block_literal_global.251
+ ___block_literal_global.259
+ ___block_literal_global.261
+ ___block_literal_global.263
+ ___block_literal_global.270
+ ___block_literal_global.294
+ ___block_literal_global.301
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.309
+ ___block_literal_global.321
+ ___block_literal_global.340
+ ___block_literal_global.349
+ ___block_literal_global.362
+ ___block_literal_global.401
+ ___block_literal_global.420
+ ___block_literal_global.47
+ ___block_literal_global.49
+ ___block_literal_global.5
+ ___block_literal_global.548
+ ___block_literal_global.556
+ ___block_literal_global.56
+ ___block_literal_global.565
+ ___block_literal_global.595
+ ___block_literal_global.605
+ ___block_literal_global.66
+ ___block_literal_global.684
+ ___block_literal_global.74
+ ___block_literal_global.75
+ ___block_literal_global.77
+ ___block_literal_global.82
+ ___block_literal_global.91
+ ___block_literal_global.97
+ ___comfortSoundsCountdownString_block_invoke
+ ___comfortSoundsDurationString_block_invoke
+ ___comfortSoundsTimeString_block_invoke
+ ___getAADeviceManagerClass_block_invoke
+ ___getAADeviceManagerClass_block_invoke.cold.1
+ ___getAXLTLiveTranscriptionClass_block_invoke
+ ___getAXLTLiveTranscriptionClass_block_invoke.cold.1
+ ___getAXRDeviceDiscoveryManagerClass_block_invoke
+ ___getAXRDeviceDiscoveryManagerClass_block_invoke.cold.1
+ ___getPAYodelConfigDidUpdateSymbolLoc_block_invoke
+ ___getUNMutableNotificationContentClass_block_invoke
+ ___getUNMutableNotificationContentClass_block_invoke.cold.1
+ ___getUNNotificationRequestClass_block_invoke
+ ___getUNNotificationRequestClass_block_invoke.cold.1
+ ___getUNUserNotificationCenterClass_block_invoke
+ ___getUNUserNotificationCenterClass_block_invoke.cold.1
+ ___getpaSupportedWiredRoutesSymbolLoc_block_invoke
+ ___getpaSupportedWirelessRoutesSymbolLoc_block_invoke
+ __dispatch_source_type_timer
+ _audit_stringAccessibilityRemoteServices
+ _audit_stringAudioAccessoryServices
+ _audit_stringLiveTranscription
+ _audit_stringUserNotifications
+ _bzero
+ _calculateState
+ _comfortSoundsCountdownString
+ _comfortSoundsCountdownString.cold.1
+ _comfortSoundsCountdownString.durationFormatter
+ _comfortSoundsCountdownString.formatterOnceToken
+ _comfortSoundsDurationString
+ _comfortSoundsDurationString.cold.1
+ _comfortSoundsDurationString.durationFormatter
+ _comfortSoundsDurationString.formatterOnceToken
+ _comfortSoundsLocString
+ _comfortSoundsTimeString
+ _comfortSoundsTimeString.cold.1
+ _comfortSoundsTimeString.formatterOnceToken
+ _comfortSoundsTimeString.timeFormatter
+ _discoveringServiceUUIDs.discoveringServiceUUIDs
+ _discoveringServiceUUIDs.onceToken
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _getAADeviceManagerClass.softClass
+ _getAXLTLiveTranscriptionClass.softClass
+ _getAXRDeviceDiscoveryManagerClass.softClass
+ _getPAYodelConfigDidUpdateSymbolLoc.ptr
+ _getUNMutableNotificationContentClass.softClass
+ _getUNNotificationRequestClass.softClass
+ _getUNUserNotificationCenterClass.softClass
+ _getpaSupportedWiredRoutesSymbolLoc.ptr
+ _getpaSupportedWirelessRoutesSymbolLoc.ptr
+ _getpid
+ _handleInternalDataCollectionDidChangeNotification
+ _isLiveListenAvailableForState
+ _isLiveListenEnabledForState
+ _isLiveListenEnabledNearbyForState
+ _isLiveListenNearbyForState
+ _kAudioServicesPlaySystemSoundOptionBehaviorKey
+ _kAudioServicesPlaySystemSoundOptionIgnoreRingerSwitchKey
+ _kAudioServicesPlaySystemSoundOptionVolumeKey
+ _liveListenStateDescription
+ _memcpy
+ _objc_exception_rethrow
+ _objc_msgSend$RSSI
+ _objc_msgSend$_attemptQueueStart
+ _objc_msgSend$_buildAudioQueue
+ _objc_msgSend$_devicesToMessage
+ _objc_msgSend$_handleRemoteControlSettingChange
+ _objc_msgSend$_handleRequestCurrentStateMessageFromDevice:
+ _objc_msgSend$_handleStartObservingFromRemoteDevice:
+ _objc_msgSend$_handleStartOrStopMessageFromRemoteDevice:message:
+ _objc_msgSend$_handleStartOrStopRewindMessageFromRemoteDevice:message:
+ _objc_msgSend$_handleStateChangedMessage:
+ _objc_msgSend$_handleStateChangedMessage:fromDevice:
+ _objc_msgSend$_handleStopObservingFromRemoteDevice:
+ _objc_msgSend$_initCharacteristicsForPeripheral:
+ _objc_msgSend$_initializeInternalDataCollectionIfNeeded
+ _objc_msgSend$_internalDataCollectionLogSPLValue:metaData:
+ _objc_msgSend$_isListeningChanged:audioLevel:isPlayingBack:orTranscriptionChanged:
+ _objc_msgSend$_liveListenDidUpdate_enumValue:
+ _objc_msgSend$_liveListenPayloadWithState:audioLevel:isPlayingBack:transcription:
+ _objc_msgSend$_minimumBufferByteSize
+ _objc_msgSend$_nearbyDevices
+ _objc_msgSend$_nearbyDevicesChanged
+ _objc_msgSend$_notifyAboutAllObservingDevices
+ _objc_msgSend$_notifyAboutObservingDevice:
+ _objc_msgSend$_notifyListenersAndPollAudioLevelIfLiveListenIsRunning
+ _objc_msgSend$_pollLiveListenAudioLevelAfterDelay
+ _objc_msgSend$_rebuildAudioQueue
+ _objc_msgSend$_receivedMessage:fromDevice:
+ _objc_msgSend$_reconfigureQueueFormatForMultiChannelOutputIfNecessary
+ _objc_msgSend$_registerForLiveListenUpdates_enumValue:
+ _objc_msgSend$_remainingTimeUntilTimestamp:
+ _objc_msgSend$_sampleRate
+ _objc_msgSend$_scheduleDeferredStop
+ _objc_msgSend$_scheduleStateUpdate
+ _objc_msgSend$_sendEmptyStateToUnauthorizedDevice:
+ _objc_msgSend$_sendLatestNearbyUpdate
+ _objc_msgSend$_sendMessageToRequestInitialState
+ _objc_msgSend$_sendStartObservingMessage
+ _objc_msgSend$_sendStartOrStopMessage:
+ _objc_msgSend$_sendStartOrStopRewindMessage:
+ _objc_msgSend$_sendStopObservingMessage
+ _objc_msgSend$_startLiveListenFromRemoteDevice:
+ _objc_msgSend$_startLiveListenRewind
+ _objc_msgSend$_startQueueWithRetry
+ _objc_msgSend$_stopLiveListenFromRemoteDevice:
+ _objc_msgSend$_stopLiveListenRewind
+ _objc_msgSend$_tearDownAudioQueue
+ _objc_msgSend$_toggleLiveListen_enumValue:
+ _objc_msgSend$_updateRemoteStartHistoryForDevice:didStart:
+ _objc_msgSend$_updateState
+ _objc_msgSend$_updateState:audioLevel:isPlayingBack:transcription:
+ _objc_msgSend$aaDeviceManager
+ _objc_msgSend$activeDurationTimerEndTimeStampCache
+ _objc_msgSend$activePreset
+ _objc_msgSend$activeTimerEndTimeStamp
+ _objc_msgSend$addNoiseSample:toCircularBuffer:forMinTime:
+ _objc_msgSend$addPeripheral:toDevice:
+ _objc_msgSend$applyBypassForFiltersAtIndexes:shouldBypass:
+ _objc_msgSend$applyTinnitusBalance
+ _objc_msgSend$aqBuffer
+ _objc_msgSend$aqRef
+ _objc_msgSend$arrayByExcludingObjectsInArray:
+ _objc_msgSend$attachNodesToEngine
+ _objc_msgSend$audioBufferList
+ _objc_msgSend$audioDevice
+ _objc_msgSend$audioPlayerFilterNode
+ _objc_msgSend$audioPlayerMixerNode
+ _objc_msgSend$audioQueueActive
+ _objc_msgSend$audioQueueFlags
+ _objc_msgSend$audioRingBuffer
+ _objc_msgSend$audioSessionIdentifier
+ _objc_msgSend$authorizationStatus
+ _objc_msgSend$availableBuffers
+ _objc_msgSend$axMapObjectsUsingBlock:
+ _objc_msgSend$axSafelyAddObject:
+ _objc_msgSend$bands
+ _objc_msgSend$bluetoothAddress
+ _objc_msgSend$bluetoothListeningModeFromHearingListeningMode:
+ _objc_msgSend$broadcast
+ _objc_msgSend$bufferCallback:
+ _objc_msgSend$bufferList
+ _objc_msgSend$buffersAvailable
+ _objc_msgSend$byteSize
+ _objc_msgSend$cachedAudioConverter
+ _objc_msgSend$cachedAudioLevel
+ _objc_msgSend$cachedCurrentCallsCount
+ _objc_msgSend$cachedDiscoveredDevices
+ _objc_msgSend$cachedHasHearingAidRoute
+ _objc_msgSend$cachedHasLiveListenRoute
+ _objc_msgSend$cachedIsListening
+ _objc_msgSend$cachedIsPlayingBack
+ _objc_msgSend$cachedNearbyDevices
+ _objc_msgSend$cachedState
+ _objc_msgSend$cachedTranscription
+ _objc_msgSend$cachedWirelessSplitterEnabled
+ _objc_msgSend$calculateVolumeForSessionWithCompletion:
+ _objc_msgSend$checkSCIDSServiceDevices
+ _objc_msgSend$clearPairedHearingAids
+ _objc_msgSend$closeFile
+ _objc_msgSend$combinedSessionTranscription
+ _objc_msgSend$comfortSoundsAudioQueue
+ _objc_msgSend$comfortSoundsEnabledCache
+ _objc_msgSend$completionHandler
+ _objc_msgSend$configureBandWithType:frequency:bandwidth:atIndex:
+ _objc_msgSend$configureBandWithType:frequency:bandwidth:gain:atIndex:
+ _objc_msgSend$configureBandsForCoarseFilter
+ _objc_msgSend$configureBandsForFineFilter
+ _objc_msgSend$configureTinnitusEqualizer
+ _objc_msgSend$connectNodesToEngine:
+ _objc_msgSend$connectedIdentifiers
+ _objc_msgSend$content
+ _objc_msgSend$contextualVolumeNeedsEnvironmentalMeasurements
+ _objc_msgSend$controller
+ _objc_msgSend$convertBufferIfNecessary:
+ _objc_msgSend$convertToBuffer:error:withInputFromBlock:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentCallCount
+ _objc_msgSend$currentTranscription
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dateByAddingUnit:value:toDate:options:
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$deferredStopQueue
+ _objc_msgSend$deferredStopSource
+ _objc_msgSend$descriptiveProperties
+ _objc_msgSend$deviceDiscoveryManager:updatedDevices:
+ _objc_msgSend$deviceImplementation
+ _objc_msgSend$deviceProtocol
+ _objc_msgSend$didAddPeripheral:
+ _objc_msgSend$didUpdateDevices:
+ _objc_msgSend$discoveredDevices
+ _objc_msgSend$discoveredNearbyDeviceIdentifiers
+ _objc_msgSend$discoveringServiceUUIDs
+ _objc_msgSend$discoveryManager
+ _objc_msgSend$earForPeripheral:
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$endTimeStamp
+ _objc_msgSend$enhancedTransparencyVersion
+ _objc_msgSend$enumerateAudioBluetoothDevicesUsingBlock:
+ _objc_msgSend$enumerateAvailableDevicesWithBlock:andCompletion:
+ _objc_msgSend$enumerateConnectedBluetoothDevices:usingBlock:andCompletion:
+ _objc_msgSend$enumerateProductCodesforAddresses:withBlock:
+ _objc_msgSend$error
+ _objc_msgSend$eventType
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileHandleForUpdatingAtPath:
+ _objc_msgSend$format
+ _objc_msgSend$frameLength
+ _objc_msgSend$frequencyForBandPass
+ _objc_msgSend$gainForHighResonance
+ _objc_msgSend$gainForLeftBellFilters
+ _objc_msgSend$gainForLowResonance
+ _objc_msgSend$gainForRightBellFilters
+ _objc_msgSend$gapaFlags
+ _objc_msgSend$getBluetoothState:
+ _objc_msgSend$getCBDeviceForCurrentRouteWithCompletion:
+ _objc_msgSend$getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:
+ _objc_msgSend$getHearingProtectionSupportforAddress:withCompletion:
+ _objc_msgSend$getNotificationSettingsWithCompletionHandler:
+ _objc_msgSend$handlePlaybackForDifferentCategory
+ _objc_msgSend$handlePlaybackForSameCategory
+ _objc_msgSend$handleRTTMessageInjection:
+ _objc_msgSend$handleRTTTranslationLocaleMessage:
+ _objc_msgSend$hash
+ _objc_msgSend$hearingListeningModeFromBluetoothListeningMode:
+ _objc_msgSend$hearingProtectionCapability
+ _objc_msgSend$holdingForCall
+ _objc_msgSend$indexSetWithIndexesInRange:
+ _objc_msgSend$inflightBuffers
+ _objc_msgSend$initFromFormat:toFormat:
+ _objc_msgSend$initWithBuffer:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithController:
+ _objc_msgSend$initWithCount:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithIdentifier:andBlock:
+ _objc_msgSend$initWithNumberOfBands:
+ _objc_msgSend$initWithPCMFormat:bufferListNoCopy:deallocator:
+ _objc_msgSend$initWithPCMFormat:frameCapacity:
+ _objc_msgSend$initWithPoint:
+ _objc_msgSend$initWithSampleRate:
+ _objc_msgSend$initWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$inputFormat
+ _objc_msgSend$internalDataCollectionEnabled
+ _objc_msgSend$internalDataCollectionQueue
+ _objc_msgSend$invalidateTimer
+ _objc_msgSend$isAvailable
+ _objc_msgSend$isInstalled
+ _objc_msgSend$isLEAudioEnabled
+ _objc_msgSend$isLEAudioServiceInServiceUUIDs:
+ _objc_msgSend$isLeftEventHandlerSet
+ _objc_msgSend$isLocallyPaired
+ _objc_msgSend$isNearby
+ _objc_msgSend$isPlayingBack
+ _objc_msgSend$isRightEventHandlerSet
+ _objc_msgSend$isSameCategoryAsSelectedSound:
+ _objc_msgSend$isSettingUpPreviewComfortSounds
+ _objc_msgSend$isSettingUpPreviewTimer
+ _objc_msgSend$isTranscribing
+ _objc_msgSend$isWritable
+ _objc_msgSend$isiPad
+ _objc_msgSend$lastUpdateStateTimestamp
+ _objc_msgSend$latestNoiseSampleWasBuffered
+ _objc_msgSend$leftRSSI
+ _objc_msgSend$linearTransformation:inputMin:inputMax:outputMin:outputMax:
+ _objc_msgSend$listenForChangesInEqualizer
+ _objc_msgSend$listenForChangesInTimer
+ _objc_msgSend$listenerHelperWithListener:andDelegate:
+ _objc_msgSend$listeningModeConfigs
+ _objc_msgSend$liveListenCountsPerClient
+ _objc_msgSend$liveListenLevelsTimer
+ _objc_msgSend$liveListenObserver
+ _objc_msgSend$liveListenRemoteControlEnabled
+ _objc_msgSend$liveListenRemoteStartHistory
+ _objc_msgSend$locations
+ _objc_msgSend$logMessageForTimer:
+ _objc_msgSend$messagesCount
+ _objc_msgSend$modifyDevice:settings:completion:
+ _objc_msgSend$nearbyDeviceWithSCIDSDevice:justCreated:
+ _objc_msgSend$notifiedDevices
+ _objc_msgSend$observeRemoteLiveListenUpdates:
+ _objc_msgSend$observingDevices
+ _objc_msgSend$orderedSet
+ _objc_msgSend$outputFormat
+ _objc_msgSend$pendingMessage
+ _objc_msgSend$peripheralDidUpdateDeviceInfo
+ _objc_msgSend$playbackTimer
+ _objc_msgSend$pmeEverywhereCapability
+ _objc_msgSend$pmeEverywhereSupportedForAddress:
+ _objc_msgSend$presetIndex
+ _objc_msgSend$presetName
+ _objc_msgSend$presetResults
+ _objc_msgSend$previewEnabled
+ _objc_msgSend$primaryPlacement
+ _objc_msgSend$processAutomationRequest:
+ _objc_msgSend$processBTPresetsUpdate:activePreset:forEar:
+ _objc_msgSend$processConnectedIdentifiers:andLocations:
+ _objc_msgSend$productCode
+ _objc_msgSend$productID
+ _objc_msgSend$propertyForCharacteristic:
+ _objc_msgSend$pseVersionForAddress:
+ _objc_msgSend$queueFormat
+ _objc_msgSend$registerAttributeUpdateBlock:withListener:
+ _objc_msgSend$registerListener:forLiveListenHandler:
+ _objc_msgSend$registerUpdateBlock:withListener:
+ _objc_msgSend$remoteStartDevice
+ _objc_msgSend$requestAuthorizationWithOptions:completionHandler:
+ _objc_msgSend$requestCurrentRoutesWithCompletion:
+ _objc_msgSend$requestWithIdentifier:content:trigger:
+ _objc_msgSend$reset
+ _objc_msgSend$rightRSSI
+ _objc_msgSend$scIDSServiceDidAddDevices:
+ _objc_msgSend$scanningServiceUUIDs
+ _objc_msgSend$scheduleBuffer:completionHandler:
+ _objc_msgSend$scheduleTimer:
+ _objc_msgSend$secondaryPlacement
+ _objc_msgSend$seekToEndOfFile
+ _objc_msgSend$selectiveSpeechListeningCapability
+ _objc_msgSend$selectiveSpeechListeningConfig
+ _objc_msgSend$sendMessageWithPayload:identifier:andResponseBlock:
+ _objc_msgSend$sendSynchronousMessageWithPayloadAndGetResponse:andIdentifier:
+ _objc_msgSend$serviceTypeDescription
+ _objc_msgSend$sessionDidUpdateLocations:
+ _objc_msgSend$sessionDidUpdateValue:forProperty:
+ _objc_msgSend$sessionInfo
+ _objc_msgSend$sessionState
+ _objc_msgSend$sessionTranscriptions
+ _objc_msgSend$setActiveDurationTimerEndTimeStampCache:
+ _objc_msgSend$setActivePreset:OptionalPresetIndex:withResponse:
+ _objc_msgSend$setActiveTimerEndTimeStamp:
+ _objc_msgSend$setAqBuffer:
+ _objc_msgSend$setAqRef:
+ _objc_msgSend$setAqTimeline:
+ _objc_msgSend$setAttributeUpdateUpdates:
+ _objc_msgSend$setAudioLevel:
+ _objc_msgSend$setAudioPlayerFilterNode:
+ _objc_msgSend$setAudioPlayerMixerNode:
+ _objc_msgSend$setAudioQueue:
+ _objc_msgSend$setAudioQueueActive:
+ _objc_msgSend$setAudioRingBuffer:
+ _objc_msgSend$setAvailableBuffers:
+ _objc_msgSend$setBandwidth:
+ _objc_msgSend$setBasicPropertiesLoaded
+ _objc_msgSend$setBufferList:
+ _objc_msgSend$setBypass:
+ _objc_msgSend$setCachedAudioConverter:
+ _objc_msgSend$setCachedAudioLevel:
+ _objc_msgSend$setCachedCurrentCallsCount:
+ _objc_msgSend$setCachedHasHearingAidRoute:
+ _objc_msgSend$setCachedHasLiveListenRoute:
+ _objc_msgSend$setCachedIsListening:
+ _objc_msgSend$setCachedIsPlayingBack:
+ _objc_msgSend$setCachedNearbyDevices:
+ _objc_msgSend$setCachedNearbyIsPlayingBack:
+ _objc_msgSend$setCachedNearbyState:
+ _objc_msgSend$setCachedNearbyTranscription:
+ _objc_msgSend$setCachedState:
+ _objc_msgSend$setCachedTranscription:
+ _objc_msgSend$setCachedWirelessSplitterEnabled:
+ _objc_msgSend$setComfortSoundsEnabledCache:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setCurrentTranscription:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDefaultActionURL:
+ _objc_msgSend$setDeferredStopSource:
+ _objc_msgSend$setDeviceImplementation:
+ _objc_msgSend$setDeviceProtocol:
+ _objc_msgSend$setDiscoveredNearbyDeviceIdentifiers:
+ _objc_msgSend$setDiscoveryManager:
+ _objc_msgSend$setFilterBoost:
+ _objc_msgSend$setFilterType:
+ _objc_msgSend$setFormat:
+ _objc_msgSend$setFrequency:
+ _objc_msgSend$setGain:
+ _objc_msgSend$setGlobalGain:
+ _objc_msgSend$setHoldingForCall:
+ _objc_msgSend$setInflightBuffers:
+ _objc_msgSend$setInternalDataCollectionEnabled:
+ _objc_msgSend$setInternalDataCollectionQueue:
+ _objc_msgSend$setIsLeftEventHandlerSet:
+ _objc_msgSend$setIsPlayingBack:
+ _objc_msgSend$setIsRightEventHandlerSet:
+ _objc_msgSend$setIsSettingUpPreviewComfortSounds:
+ _objc_msgSend$setIsSettingUpPreviewTimer:
+ _objc_msgSend$setIsTranscribing:
+ _objc_msgSend$setLastUpdateStateTimestamp:
+ _objc_msgSend$setLatestNoiseSampleWasBuffered:
+ _objc_msgSend$setLeAudioEventHandler:
+ _objc_msgSend$setLeftRSSI:
+ _objc_msgSend$setListeningMode:
+ _objc_msgSend$setLiveListenCountsPerClient:
+ _objc_msgSend$setLiveListenLevelsTimer:
+ _objc_msgSend$setLiveListenObserver:
+ _objc_msgSend$setLiveListenRemoteStartHistory:
+ _objc_msgSend$setMessagesCount:
+ _objc_msgSend$setNotifiedDevices:
+ _objc_msgSend$setOutputVolume:
+ _objc_msgSend$setPan:
+ _objc_msgSend$setPendingMessage:
+ _objc_msgSend$setPlaybackTimer:
+ _objc_msgSend$setPowerState:completion:
+ _objc_msgSend$setRSSI:
+ _objc_msgSend$setRemoteStartDevice:
+ _objc_msgSend$setRightRSSI:
+ _objc_msgSend$setSelectiveSpeechListeningConfig:
+ _objc_msgSend$setSessionTranscriptions:
+ _objc_msgSend$setShouldRebuildAudioQueue:
+ _objc_msgSend$setShouldSuppressDefaultAction:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTimerDurationInSeconds:
+ _objc_msgSend$setTimerEnabled:
+ _objc_msgSend$setTimerEnabledCache:
+ _objc_msgSend$setTimerEndInterval:
+ _objc_msgSend$setTranscriber:
+ _objc_msgSend$setTranscription:
+ _objc_msgSend$setUnitsStyle:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$setUpdateStateTimer:
+ _objc_msgSend$setVolume:withResponse:
+ _objc_msgSend$setXValue:
+ _objc_msgSend$setYValue:
+ _objc_msgSend$setupCentralManagerForLEAudio
+ _objc_msgSend$setupLoadingProperties
+ _objc_msgSend$setupTimerIfEnabled
+ _objc_msgSend$setupUpdatesHandlerForLEAudioPeripheral:
+ _objc_msgSend$shouldEnableNoiseMeasurements
+ _objc_msgSend$shouldRebuildAudioQueue
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$startLiveListen
+ _objc_msgSend$startLiveListenRewind
+ _objc_msgSend$startObserving
+ _objc_msgSend$startObservingRemoteSession
+ _objc_msgSend$startTranscribing
+ _objc_msgSend$startTranscribing:targetPID:callbackBlock:error:
+ _objc_msgSend$stopComfortSound:
+ _objc_msgSend$stopLiveListen
+ _objc_msgSend$stopLiveListenRewind
+ _objc_msgSend$stopObserving
+ _objc_msgSend$stopObservingRemoteSession
+ _objc_msgSend$stopTranscribing
+ _objc_msgSend$stopTranscribing:targetPID:error:
+ _objc_msgSend$stringFromTimeInterval:
+ _objc_msgSend$swapPeripheral:toEar:
+ _objc_msgSend$timerDurationInSeconds
+ _objc_msgSend$timerEnabled
+ _objc_msgSend$timerEnabledCache
+ _objc_msgSend$timerEndInterval
+ _objc_msgSend$timerOnlyOnFirstSession
+ _objc_msgSend$timerOption
+ _objc_msgSend$tinnitusBalance
+ _objc_msgSend$tinnitusFilterEnabled
+ _objc_msgSend$tinnitusFilterMode
+ _objc_msgSend$tinnitusFilterPoint
+ _objc_msgSend$toggleLiveListenRewind:
+ _objc_msgSend$transcribedText
+ _objc_msgSend$transcriber
+ _objc_msgSend$transcription
+ _objc_msgSend$transcriptionDidStart
+ _objc_msgSend$transcriptionDidUpdate:
+ _objc_msgSend$updateLock
+ _objc_msgSend$updateQueue
+ _objc_msgSend$updateStateTimer
+ _objc_msgSend$updatedValue
+ _objc_msgSend$validateTimerDuration
+ _objc_msgSend$validateTimerEndInterval
+ _objc_msgSend$vendorID
+ _objc_msgSend$wait
+ _objc_msgSend$widthForBandPass
+ _objc_msgSend$writeData:
+ _objc_msgSend$writeToFile:atomically:
+ _objc_msgSend$xValue
+ _objc_msgSend$yValue
+ _objc_terminate
+ _pow
+ _scanningServiceUUIDs.onceToken
+ _scanningServiceUUIDs.scanningServiceUUIDs
+ _sharedInstance.Settings.417
+ _sharedInstance.obj
+ _sharedInstance.onceToken.418
+ _updateStateForNearbyDevice
- -[AXHeardController bluetoothAvailabilityDidChange:]
- -[AXHeardController updateAnalytics].cold.1
- -[AXHearingAidDevice deviceType]
- -[AXHearingAidDevice updateNameWithAdvertisingData:]
- -[AXRemoteHearingAidDevice deviceType]
- -[AXRemoteHearingAidDevice setDeviceType:]
- -[HUAccessoryHearingSyncManager hasPairedDeviceWithHearingProtectionEnabled]
- -[HUComfortSoundsSettings setValue:forPreferenceKey:].cold.1
- -[HUComfortSoundsSettings setValue:forPreferenceKey:].cold.2
- -[HUUtilities liveListenDevice]
- GCC_except_table100
- GCC_except_table115
- GCC_except_table118
- GCC_except_table29
- GCC_except_table31
- GCC_except_table32
- GCC_except_table53
- GCC_except_table56
- GCC_except_table6
- GCC_except_table62
- GCC_except_table64
- GCC_except_table66
- GCC_except_table68
- GCC_except_table80
- GCC_except_table88
- GCC_except_table92
- GCC_except_table98
- _AVSystemController_RouteDescriptionKey_RouteUID
- _BluetoothAccessoryInEarStatusNotification
- _BluetoothAccessorySettingsChanged
- _BluetoothAvailabilityChangedNotification
- _NSLog
- _OBJC_CLASS_$_BluetoothManager
- _OBJC_IVAR_$_AXRemoteHearingAidDevice._deviceType
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.527
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.540
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.548
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.557
- ___25-[HUNoiseController init]_block_invoke.319
- ___31-[HUUtilities liveListenDevice]_block_invoke
- ___31-[HUUtilities liveListenDevice]_block_invoke_2
- ___33-[HUComfortSoundsController init]_block_invoke.18
- ___33-[HUComfortSoundsController init]_block_invoke.31
- ___33-[HUComfortSoundsController init]_block_invoke.35
- ___33-[HUComfortSoundsController init]_block_invoke.42
- ___33-[HUComfortSoundsController init]_block_invoke.49
- ___33-[HUComfortSoundsController init]_block_invoke.56
- ___33-[HUComfortSoundsController init]_block_invoke_2.38
- ___33-[HUComfortSoundsController init]_block_invoke_2.45
- ___33-[HUComfortSoundsController init]_block_invoke_2.52
- ___33-[HUComfortSoundsController init]_block_invoke_2.59
- ___34-[AXHeardController continueSetup]_block_invoke.136
- ___34-[AXHeardController continueSetup]_block_invoke.140
- ___34-[AXHeardController continueSetup]_block_invoke_2.143
- ___36-[AXHeardController updateAnalytics]_block_invoke.235
- ___37-[HUNearbyHearingAidController start]_block_invoke.113
- ___37-[HUNearbyHearingAidController start]_block_invoke.118
- ___37-[HUNearbyHearingAidController start]_block_invoke.99
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.114
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.119
- ___37-[HUNearbyHearingAidController start]_block_invoke_3.120
- ___37-[HUNearbyHearingAidController start]_block_invoke_4.121
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.405
- ___40-[AXHeardController _shutdownIfPossible]_block_invoke.182
- ___41-[AXHeardController handleNewConnection:]_block_invoke.269
- ___41-[AXHeardController handleNewConnection:]_block_invoke_2.270
- ___41-[AXHearingAidDevice initWithPeripheral:]_block_invoke
- ___41-[AXHearingAidDevice initWithPeripheral:]_block_invoke_2
- ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.132
- ___44-[AXHearingAidDevice loadRequiredProperties]_block_invoke.218
- ___46-[AXHearingAidDevice updateInputTagsAndReset:]_block_invoke.313
- ___49-[HUNearbyController stopDiscoveringSCIDSService]_block_invoke.153
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.623
- ___52-[AXHearingAidDeviceController connectToPeripheral:]_block_invoke.74
- ___53-[AXHAController registerForAvailableDevicesUpdates:]_block_invoke.111
- ___53-[AXHeardController updateHearingControlCenterModule]_block_invoke.110
- ___53-[HUComfortSoundsSettings setValue:forPreferenceKey:]_block_invoke
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.431
- ___56-[AXHearingAidDeviceController cancelPendingConnections]_block_invoke.82
- ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke_2
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.240
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.246
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke_2.241
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke_3.242
- ___58-[HURoutesManager fetchCurrentPickableAudioRoutesIfNeeded]_block_invoke.6
- ___59-[AXHearingAidDevice peripheral:propertyForCharacteristic:]_block_invoke
- ___59-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke.54
- ___59-[HUNearbyHearingAidController sendMessagesPriorityDefault]_block_invoke.167
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.105
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.109
- ___67-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]_block_invoke.213
- ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.68
- ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.69
- ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.76
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.104
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.112
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.121
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.105
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.116
- ___69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke.216
- ___71-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke.157
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.471
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.491
- ___block_descriptor_32_e17_v16?0"NSArray"8l
- ___block_descriptor_32_e25_v16?0"BluetoothDevice"8l
- ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32bs40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32bs40r_e32_v32?0"BluetoothDevice"8Q16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32s40r_e23_v32?0"CBUUID"8Q16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e25_B16?0"BluetoothDevice"8ls32l8r40l8
- ___block_descriptor_49_e8_32s40r_e8_v12?0B8lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSArray"8lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40bs48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48bs56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_descriptor_84_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.136
- ___block_literal_global.137
- ___block_literal_global.138
- ___block_literal_global.149
- ___block_literal_global.150
- ___block_literal_global.169
- ___block_literal_global.187
- ___block_literal_global.189
- ___block_literal_global.194
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.231
- ___block_literal_global.240
- ___block_literal_global.246
- ___block_literal_global.248
- ___block_literal_global.255
- ___block_literal_global.285
- ___block_literal_global.290
- ___block_literal_global.291
- ___block_literal_global.292
- ___block_literal_global.303
- ___block_literal_global.315
- ___block_literal_global.342
- ___block_literal_global.350
- ___block_literal_global.395
- ___block_literal_global.411
- ___block_literal_global.542
- ___block_literal_global.559
- ___block_literal_global.57
- ___block_literal_global.583
- ___block_literal_global.593
- ___block_literal_global.79
- ___block_literal_global.87
- ___block_literal_global.90
- ___block_literal_global.95
- ___get_AXSUpdateAccessibilityEnabledSymbolLoc_block_invoke
- ___getpaCurrentBluetoothDeviceSupportingTransparencyAccommodationsAsyncSymbolLoc_block_invoke
- ___iteratePairedBluetoothDevicesOnQueueCBv1_block_invoke
- ___iteratePairedBluetoothDevicesOnQueueCBv1_block_invoke_2
- ___libAccessibilityLibraryCore_block_invoke
- _get_AXSUpdateAccessibilityEnabledSymbolLoc.ptr
- _getpaCurrentBluetoothDeviceSupportingTransparencyAccommodationsAsyncSymbolLoc.ptr
- _iteratePairedBluetoothDevicesOnQueueCBv1
- _libAccessibilityLibrary
- _libAccessibilityLibraryCore.frameworkLibrary
- _objc_msgSend$_registerMediaNotification
- _objc_msgSend$adaptiveTransparencySupportedDevices
- _objc_msgSend$address
- _objc_msgSend$deviceFromAddressString:
- _objc_msgSend$featureCapability:
- _objc_msgSend$getAACPCapabilityInteger:
- _objc_msgSend$handleRTTVoicemailMessage:
- _objc_msgSend$hasPairedDeviceWithHearingProtectionEnabled
- _objc_msgSend$hasPeers
- _objc_msgSend$inEarStatusPrimary:secondary:
- _objc_msgSend$logSCIDSDeviceFromDevices:
- _objc_msgSend$pairedDevices
- _objc_msgSend$productId
- _objc_msgSend$setSharedInstanceQueue:
- _objc_msgSend$updateNameWithAdvertisingData:
- _objc_msgSend$vendorId
- _sendMessage:withDomain:toDevices:withPriority:.MessageCount
- _setValue:forPreferenceKey:.HasFunction
- _setValue:forPreferenceKey:.sOnce
- _sharedInstance.Settings.408
- _sharedInstance.onceToken.409
CStrings:
+ "\n"
+ "#"
+ "$"
+ "%@ (%ld)"
+ "%@,%@\n"
+ "%@,%@,%@\n"
+ "%@: Firmware version found: %@"
+ "%@: Hardware version found: %@"
+ "%@: HearingDevice (paired: %d %d) didAddPeripheral: %p %@, left: %@, right: %@"
+ "%@: HearingDevice Swapped to Left %@, Right %@"
+ "%@: HearingDevice Swapped to Right %@, Left %@"
+ "%@: HearingDevice valueForProperty %@"
+ "%@: HearingDevice valueForProperty value %@"
+ "%@: Manufacturer found: |%@|"
+ "%@: Model Number found: |%@|"
+ "%@: peripheral %@ didDiscoverCharacteristicsForService %@ - %@"
+ "%@: peripheral %@ didDiscoverServices %@"
+ "%@: peripheral %@ didUpdateCharacteristic %@"
+ "%@: peripheral %@ didUpdateCharacteristic DIS value: %@, ear: %@, L: %@, R: %@"
+ "-"
+ "-[AXHAController _registerForLiveListenUpdates_enumValue:]"
+ "-[AXHeardController startServer]_block_invoke_34"
+ "-[AXHearingAidDevice swapPeripheral:toEar:]"
+ "-[AXHearingAidDevice updateName]"
+ "-[AXHearingAidDeviceController scanningServiceUUIDs]_block_invoke"
+ "-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2"
+ "-[HUAccessoryHearingSyncManager listeningModeDidChange:]"
+ "-[HUAccessoryHearingSyncManager readHearingProtectionState]_block_invoke_2"
+ "-[HUAccessoryManager pseVersionForAddress:]"
+ "-[HUAccessoryManager pseVersionForAddress:]_block_invoke"
+ "-[HUComfortSoundsController calculateVolumeForSessionWithCompletion:]_block_invoke"
+ "-[HUComfortSoundsController endTimeStamp]"
+ "-[HUComfortSoundsController handlePlaybackForDifferentCategory]"
+ "-[HUComfortSoundsController handlePlaybackForSameCategory]"
+ "-[HUComfortSoundsController init]_block_invoke_3"
+ "-[HUComfortSoundsController invalidateTimer]"
+ "-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke"
+ "-[HUComfortSoundsController listenForChangesInEqualizer]_block_invoke_6"
+ "-[HUComfortSoundsController listenForChangesInTimer]_block_invoke"
+ "-[HUComfortSoundsController listenForChangesInTimer]_block_invoke_4"
+ "-[HUComfortSoundsController logMessageForTimer:]"
+ "-[HUComfortSoundsController scheduleTimer:]"
+ "-[HUComfortSoundsController scheduleTimer:]_block_invoke"
+ "-[HUComfortSoundsController setupTimerIfEnabled]"
+ "-[HUComfortSoundsController setupTimerIfNeeded]"
+ "-[HUComfortSoundsController stopComfortSound:]"
+ "-[HUComfortSoundsController stop]_block_invoke"
+ "-[HUComfortSoundsSettings setTimerInHoursAndMinutes:minutes:]"
+ "-[HUComfortSoundsSettings setTinnitusFilterPoint:]"
+ "-[HUComfortSoundsSettings tinnitusFilterPoint]"
+ "-[HUHearingAidSettings _initializeICloudSetup]"
+ "-[HUHearingAidSettings icloudHearingSettingsDidChange:]_block_invoke"
+ "-[HUHearingAidSettings setLocalHearingAidsFromiCloud:]"
+ "-[HUNearbyLiveListenControllerWatch _receivedMessage:fromDevice:]_block_invoke"
+ "-[HUNearbyLiveListenControllerWatch _sendMessageToRequestInitialState]"
+ "-[HUNearbyLiveListenControllerWatch _sendStartObservingMessage]"
+ "-[HUNearbyLiveListenControllerWatch _sendStartOrStopMessage:]"
+ "-[HUNearbyLiveListenControllerWatch _sendStartOrStopRewindMessage:]"
+ "-[HUNearbyLiveListenControllerWatch _sendStopObservingMessage]"
+ "-[HUNearbyLiveListenControlleriOS _audioRoutesChanged:]_block_invoke"
+ "-[HUNearbyLiveListenControlleriOS _callsStatusChanged:]_block_invoke_2"
+ "-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke_2"
+ "-[HUNearbyLiveListenControlleriOS _handleRequestCurrentStateMessageFromDevice:]_block_invoke"
+ "-[HUNearbyLiveListenControlleriOS _handleStartObservingFromRemoteDevice:]_block_invoke"
+ "-[HUNearbyLiveListenControlleriOS _handleStartOrStopMessageFromRemoteDevice:message:]_block_invoke"
+ "-[HUNearbyLiveListenControlleriOS _handleStartOrStopRewindMessageFromRemoteDevice:message:]_block_invoke"
+ "-[HUNearbyLiveListenControlleriOS _handleStopObservingFromRemoteDevice:]"
+ "-[HUNearbyLiveListenControlleriOS _nearbyDevices]"
+ "-[HUNearbyLiveListenControlleriOS _nearbyDevices]_block_invoke"
+ "-[HUNearbyLiveListenControlleriOS _receivedMessage:fromDevice:]"
+ "-[HUNearbyLiveListenControlleriOS _sendEmptyStateToUnauthorizedDevice:]"
+ "-[HUNearbyLiveListenControlleriOS _sendMessageToRequestInitialState]"
+ "-[HUNearbyLiveListenControlleriOS _sendStartObservingMessage]"
+ "-[HUNearbyLiveListenControlleriOS _sendStartOrStopMessage:]"
+ "-[HUNearbyLiveListenControlleriOS _sendStartOrStopRewindMessage:]"
+ "-[HUNearbyLiveListenControlleriOS _sendStopObservingMessage]"
+ "-[HUNearbyLiveListenControlleriOS _startLiveListenFromRemoteDevice:]"
+ "-[HUNearbyLiveListenControlleriOS _startLiveListenRewind]"
+ "-[HUNearbyLiveListenControlleriOS _stopLiveListenFromRemoteDevice:]"
+ "-[HUNearbyLiveListenControlleriOS _stopLiveListenRewind]"
+ "-[HUNearbyLiveListenControlleriOS _wirelessSplitterEnabledChanged:]_block_invoke"
+ "-[HUNearbyLiveListenControlleriOS startObserving]"
+ "-[HUNearbyLiveListenControlleriOS stopObserving]"
+ "-[HUNoiseController shouldShowHearingProtectionSuggestionForAlertType:]_block_invoke_2"
+ "/var/mobile/tmp/com.apple.heard/fast_spl.csv"
+ "/var/mobile/tmp/com.apple.heard/slow_spl.csv"
+ "1854"
+ ":"
+ "@\"<HULiveListenTranscriptionControllerDelegate>\""
+ "@\"<HUNearbyLiveListenDeviceImplementation>\""
+ "@\"AADeviceManager\""
+ "@\"AVAudioBuffer\"20@?0I8^q12"
+ "@\"AVAudioConverter\""
+ "@\"AVAudioFormat\""
+ "@\"AVAudioMixerNode\""
+ "@\"AVAudioUnitEQ\""
+ "@\"AXLTLiveTranscription\""
+ "@\"AXRDeviceDiscoveryManager\""
+ "@\"CBLEAudioSessionInfo\""
+ "@\"HULiveListenController\""
+ "@\"HULiveListenObserver\""
+ "@\"HULiveListenTranscriptionController\""
+ "@\"HUNearbyDevice\""
+ "@\"HUNearbyLiveListenController\""
+ "@\"HURingBuffer\""
+ "@\"HUWrappedAudioQueue\""
+ "@\"NSCondition\""
+ "@\"NSMutableOrderedSet\""
+ "@\"NSNumber\"16@0:8"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@24@0:8@\"HUNearbyLiveListenController\"16"
+ "@24@0:8^{AudioBufferList=I[1{AudioBuffer=II^v}]}16"
+ "@24@0:8^{_NSZone=}16"
+ "@24@0:8d16"
+ "@24@?0@\"AXRemoteDevice\"8Q16"
+ "@32@0:8{CGPoint=dd}16"
+ "@40@0:8q16f24B28@32"
+ "AA controller found %@"
+ "AADeviceManager"
+ "AXHearingAidDevice:%p [%@] [%@] [%@, %@, %@, %@] L:%d R:%d, l-uuid: %@ r-uuid: %@ - [%@, %@] [%@, %@]"
+ "AXHearingAidLEAudioDevice"
+ "AXLTLiveTranscription"
+ "AXRDeviceDiscoveryManager"
+ "AXRDeviceDiscoveryObserver"
+ "Activated aa controller with error %@"
+ "After timeout gave up on Media handoff, transition connection to peer"
+ "Airplane"
+ "Attributes updated %@ = %@"
+ "B32@?0@\"HUIdentifierAndBlockPair\"8Q16^B24"
+ "B40@0:8q16f24B28@32"
+ "BT state updated %@"
+ "Babble"
+ "BackCenter"
+ "BackLeft"
+ "BackRight"
+ "Boat"
+ "BottomFrontCenter"
+ "BottomFrontLeft"
+ "BottomFrontRight"
+ "Bus"
+ "Caching comfort sounds enablement while playing preview - %d"
+ "Caching timer enablement while playing preview - %d"
+ "CentralManager: %@ in %@"
+ "CentralManager: OFF"
+ "CentralManager: ON"
+ "CentralManager: Starting scan services: %@ persistent uuids: %@"
+ "CentralManager: Stopping scan"
+ "CentralManager: connectPeripheral state: %ld, %@"
+ "CentralManager: didConnectPeripheral %@\n Connected device: %@"
+ "CentralManager: didConnectPeripheral state: %ld %@"
+ "CentralManager: didDisconnectPeripheral, Connect"
+ "CentralManager: didDiscoverPeripheral %@\nserviceUUIDs: %@\nadvertisementData: %@"
+ "CentralManager: didDiscoverPeripheral, Connect to device %@"
+ "CentralManager: disconnectFromPeripheral from %@"
+ "CentralManager: peripheral unpair %@"
+ "Checking address %@"
+ "Checking device %@. idsNearby: %@, rapportNearby: %@"
+ "Contextual volume is enabled. Do not disable noise measurements."
+ "Created Hearing Aids device %@"
+ "Device Protocol"
+ "EndDate"
+ "Error starting Live Listen: %{public}@"
+ "Error stopping Live Listen: %{public}@"
+ "Error turning on Bluetooth %@"
+ "Failed to start transcribing: %{public}@"
+ "Failed to stop transcribing: %{public}@"
+ "Found devices %@ - %@"
+ "Found pse version %@ for address %@"
+ "FrontCenter"
+ "FrontLeft"
+ "FrontLeftOfCenter"
+ "FrontLeftWide"
+ "FrontRight"
+ "FrontRightOfCenter"
+ "FrontRightWide"
+ "HP supported %@ for accessory %@"
+ "HUAccessoryManagerAttributesUpdateKey"
+ "HUAudioBuffer"
+ "HUComfortSoundProtocol"
+ "HUComfortSoundsDelegate"
+ "HUComfortSoundsFilterPoint"
+ "HUComfortSoundsFilterPointKey"
+ "HUEDSampleIntervalKey"
+ "HUListenerHelperDelegate"
+ "HULiveListenObserver"
+ "HULiveListenTranscriptionController"
+ "HULiveListenTranscriptionControllerDelegate"
+ "HUNearbyLiveListenController"
+ "HUNearbyLiveListenControllerWatch"
+ "HUNearbyLiveListenControlleriOS"
+ "HUNearbyLiveListenDeviceImplementation"
+ "HUNoiseSampleDateKey"
+ "HUNoiseSampleDurationKey"
+ "HUNoiseSampleSPLKey"
+ "HURingBuffer"
+ "HUSynthesisProviderAudioOutput"
+ "HUWrappedAudioQueue"
+ "HUWrappedAudioQueueBuffer"
+ "Had stored that device %@ started live listen, but no info in remote start history dict"
+ "Handling incoming message %@"
+ "Handling playback for a different catagory."
+ "Handling playback for same catagory."
+ "HeadphoneLevel starting IDS failed, IDS service is not available"
+ "HeadphoneLevelController is starting IDS %@"
+ "HeadphoneLevelController starting IDS skipped, no Watches with enabled"
+ "HeadphoneLevelController will start IDS"
+ "Hearing Aids handoff completed"
+ "HearingAidLiveListenRemoteObserverNotification"
+ "HearingAidLiveListenRemoteStartNotification"
+ "HearingAidLiveListenStatusbar"
+ "Ignoring message from non-locally paired device"
+ "Ignoring request current state message from unauthorized device %@"
+ "Ignoring start/stop message from unauthorized device %@"
+ "Ignoring start/stop rewind message from unauthorized device %@"
+ "InternalDataCollectionEnabled"
+ "Invalid playback duration. Therefore, timer can not be scheduled."
+ "Invalidating timer."
+ "L"
+ "LEA 3"
+ "LEA 3: HearingDevice %@ setValue %@ %@"
+ "LEA 3: HearingDevice (paired: %d %d) device info updated: %p %@, left: %@, right: %@"
+ "LEA 3: HearingDevice (paired: %d %d) name updated: %p %@, left: %@, right: %@"
+ "LEA 3: HearingDevice Basic Properties Loaded for %@"
+ "LEA 3: HearingDevice Connect to %@"
+ "LEA 3: HearingDevice SKIP disconnecting/unpairing from %@ %@\n%@"
+ "LEA 3: HearingDevice connectionDidChange isConnecting %d %@"
+ "LEA 3: HearingDevice didLoadPersistentProperties %d %@, Left %@, Right %@"
+ "LEA 3: HearingDevice disconnecting/unpairing(%d) from \n%@"
+ "LEA 3: HearingDevice name updated, saving persistent representation - %@"
+ "LEA 3: HearingDevice newName %@"
+ "LEA 3: HearingDevice setupLoadingProperties for %@"
+ "LEA 3: Peripheral discovered %@, created Hearing Aids device %@"
+ "LEA 3: addPeripheral: %@, didAdd: %d\n%@"
+ "LEA 3: addPeripheral: %@, isLeft: %d, didAdd: %d\n%@"
+ "LEA 3: availablePropertiesForPeripheral SKIP for %@"
+ "LEA 3: characteristicForUUID SKIP for %@"
+ "LEA 3: loadBasicProperties SKIP for %@"
+ "LEA 3: loadProperties SKIP for %@ %@"
+ "LEA 3: loadRequiredProperties SKIP for %@"
+ "LEA 3: peripheral %@ deviceType: %@, event type: %@, event: %@\n %@device: %@"
+ "LEA 3: peripheral BT setActivePreset %@"
+ "LEA 3: peripheral BT setVolume %@ adjusted %@"
+ "LEA 3: peripheral DIS"
+ "LEA 3: peripheral LeftPrograms %@"
+ "LEA 3: peripheral RightPrograms %@"
+ "LEA 3: peripheral availablePropertiesFromDIS %@ for Peripheral %@"
+ "LEA 3: peripheral discovered %@\n device: %@"
+ "LEA 3: peripheral is unknown - %@"
+ "LEA 3: peripheral leftSelectedProgram %@"
+ "LEA 3: peripheral preset - %@ "
+ "LEA 3: peripheral preset available %d"
+ "LEA 3: peripheral preset index: %d"
+ "LEA 3: peripheral preset name: %s"
+ "LEA 3: peripheral preset writable: %d"
+ "LEA 3: peripheral property write %@ ear %@ for %@ id %@"
+ "LEA 3: peripheral rightSelectedProgram %@"
+ "LEA 3: peripheral setActivePreset error %@"
+ "LEA 3: peripheral setVolume error %@"
+ "LEA 3: peripheral setting notify %d for peripheral: %@ - %@"
+ "LEA 3: peripheral setup update handler -  %@"
+ "LEA 3: peripheral setup update handler fail, device has no such peripheral - %@"
+ "LEA 3: peripheral update - HA features %@"
+ "LEA 3: peripheral update - active preset %@"
+ "LEA 3: peripheral update - name preset at index: %@"
+ "LEA 3: peripheral update - presets %@, active preset index %@"
+ "LEA 3: peripheral update - volume %@"
+ "LEA 3: session DeviceIdentifier - %@"
+ "LEA 3: session added the second peripheral %@ to %@"
+ "LEA 3: session connected peripherals %@"
+ "LEA 3: session device %@"
+ "LEA 3: session device already has both peripherals %@"
+ "LEA 3: session device is not found"
+ "LEA 3: session left %@ connection requested %d"
+ "LEA 3: session location %@ %@ %s"
+ "LEA 3: session location for unknown peripheral identifier %@"
+ "LEA 3: session no connected identifiers"
+ "LEA 3: session no peripherals for identifiers %@"
+ "LEA 3: session not all peripherals retrieved for identifiers %@"
+ "LEA 3: session peripheral1 %@\n found device %@"
+ "LEA 3: session peripheral2 %@\n found device %@"
+ "LEA 3: session right %@ connection requested %d"
+ "LEA 3: session setup"
+ "LEA 3: session unknown location %@ for %@"
+ "LEA 3: session update - ID %@, new state %@"
+ "LEA 3: session update - ID %@, state %@"
+ "LEA 3: session update - connected, connectedIdentifiers %@, locations %@"
+ "LEA 3: session update - event %@ error %@"
+ "LEA 3: session update - eventType %@, connectedIdentifiers %@, locations %@"
+ "LEA 3: session update - mic gain %@, paired HearingDevice: %@"
+ "LEA 3: session update - mic mute %@"
+ "LEA 3: session update - peripheral ready, connectedIdentifiers %@"
+ "LEA 3: session update - unknown event %@"
+ "LEA 3: session update - volume %@, paired HearingDevice: %@"
+ "LEA 3: session update - volume mute %@"
+ "LEA 3: session update - volume offset %@"
+ "LEA 3: session updating persistent representation - %@"
+ "LEA 3: setNotify SKIP for %@"
+ "LEA 3: writeValueForProperty SKIP for %@"
+ "LeftSurround"
+ "Listening modes current: %@ new: %@ forcing update %@"
+ "Live Listen sending state change message: %{public}@"
+ "Live listen not enabled, ignoring rewind message"
+ "LiveListenControls"
+ "LowFrequencyEffects1"
+ "LowFrequencyEffects2"
+ "MFI"
+ "NSCopying"
+ "New device started observing, send update? %@ - %@"
+ "New device stopped observing %@"
+ "Not sending an XPC reply. The initial state value hasn't been set yet."
+ "Not starting live listen, already listening"
+ "NotAllowed"
+ "NotNearby"
+ "Off"
+ "On"
+ "OnNearbyPad"
+ "OnNearbyPhone"
+ "PAYodelConfigDidUpdate"
+ "Paired Hearing Aids from iCloud %@"
+ "Paired Hearing Aids from local %@"
+ "Playing comfort sounds preview"
+ "Posted notification with authorization status: %i"
+ "Posting connecting/transitioning handoff finished notification"
+ "Posting local notification: %@"
+ "Q20@0:8i16"
+ "Queued live listen state change message ( %{public}@ ) to %lu nearby devices: %{public}@"
+ "QuietNight"
+ "R"
+ "RSSI"
+ "RainOnRoof"
+ "Registering for Live Listen state updates"
+ "Registering for device availability %d, %d, %lf"
+ "Removing cached active timer timestamp"
+ "Removing listener for Live Listen state updates"
+ "Replying with %@"
+ "Replying with current Live Listen state: %{public}@"
+ "Requested authorization to show notification: %d %@"
+ "Resuming the timer after playing preview. activeDurationTimerEndTimeStamp is %f"
+ "RightSurround"
+ "SC IDS Service Added devices: %@"
+ "SC IDS Service Added, current state %@"
+ "SC IDS Service Lost connected device: %@"
+ "SC IDS Service Nearby device %@"
+ "SC IDS Service Sending PeerConnected to %@"
+ "SC IDS Service Sending PeerConnected to all"
+ "SC IDS Service Updated Devices: %@"
+ "SC IDS Service device: %@"
+ "SC IDS Service has devices %@"
+ "SC IDS Service sending message %@ to device: %@"
+ "Scanning LEA 3"
+ "Scanning MFi"
+ "Scheduling timer with duration: %f"
+ "Selected sound is the same catagory as the current sound %d"
+ "Sending Live Listen message ( state: %{public}@ :: level: %.5f )"
+ "Sending SC IDS device state %@"
+ "Sending empty state message %@ to unauthorized device %@"
+ "Sending message to update state on %lu nearby devices: %@"
+ "Sending request current state message to %lu paired devices: %@"
+ "Sending start observing message to %lu paired devices: %@"
+ "Sending start/stop message to %lu paired devices: %@"
+ "Sending start/stop rewind message to %lu paired devices: %@"
+ "Sending stop observing message to %lu paired devices: %@"
+ "Set Paired Hearing Aids from iCloud %@"
+ "Setting back the timer call back."
+ "Setting timer for duration - %f."
+ "Setting up timer."
+ "SideLeft"
+ "SideRight"
+ "Skipping device because not supported %@ %@, %@ %@"
+ "Skipping pairing because not a hearing device %@"
+ "Start observing"
+ "StartDate"
+ "Starting live listen from device %@"
+ "Starting live listen rewind"
+ "Steam"
+ "Stop observing"
+ "Stopping comfort sounds preview"
+ "Stopping live listen from device %@"
+ "Stopping live listen rewind"
+ "T@\"<HUComfortSoundProtocol>\",&,N"
+ "T@\"<HULiveListenTranscriptionControllerDelegate>\",W,N,V_delegate"
+ "T@\"<HUNearbyLiveListenDeviceImplementation>\",&,N,V_deviceImplementation"
+ "T@\"AADeviceManager\",&,N,V_aaDeviceManager"
+ "T@\"AVAudioConverter\",&,N,V_cachedAudioConverter"
+ "T@\"AVAudioFormat\",&,N,V_format"
+ "T@\"AVAudioFormat\",&,N,V_queueFormat"
+ "T@\"AVAudioMixerNode\",&,N,V_audioPlayerMixerNode"
+ "T@\"AVAudioUnitEQ\",&,N,V_audioPlayerFilterNode"
+ "T@\"AXDispatchTimer\",&,N,V_liveListenLevelsTimer"
+ "T@\"AXDispatchTimer\",&,N,V_playbackTimer"
+ "T@\"AXHearingAidMode\",&,D"
+ "T@\"AXLTLiveTranscription\",&,N,V_transcriber"
+ "T@\"AXRDeviceDiscoveryManager\",&,N,V_discoveryManager"
+ "T@\"HUComfortSoundsFilterPoint\",&,N"
+ "T@\"HULiveListenController\",&,N,V_controller"
+ "T@\"HULiveListenObserver\",&,N,V_liveListenObserver"
+ "T@\"HULiveListenTranscriptionController\",&,N,V_transcriber"
+ "T@\"HUNearbyDevice\",&,N,V_remoteStartDevice"
+ "T@\"HUNearbyLiveListenController\",R,N"
+ "T@\"HUNearbyLiveListenController\",W,N,V_controller"
+ "T@\"HURingBuffer\",&,N,V_audioRingBuffer"
+ "T@\"HUWrappedAudioQueue\",&,N,V_audioQueue"
+ "T@\"NSArray\",C,D"
+ "T@\"NSArray\",C,N,V_cachedNearbyDevices"
+ "T@\"NSArray\",C,N,V_discoveredNearbyDeviceIdentifiers"
+ "T@\"NSCondition\",&,N,V_buffersAvailable"
+ "T@\"NSDate\",&,N,V_lastUpdateStateTimestamp"
+ "T@\"NSDictionary\",&,N,V_pendingMessage"
+ "T@\"NSLock\",&,N,V_updateLock"
+ "T@\"NSMutableArray\",&,N,V_notifiedDevices"
+ "T@\"NSMutableArray\",&,N,V_observingDevices"
+ "T@\"NSMutableArray\",&,N,V_sessionTranscriptions"
+ "T@\"NSMutableArray\",&,N,V_updateBlocks"
+ "T@\"NSMutableDictionary\",&,N,V_liveListenCountsPerClient"
+ "T@\"NSMutableDictionary\",&,V_attributeUpdateUpdates"
+ "T@\"NSMutableOrderedSet\",&,N,V_availableBuffers"
+ "T@\"NSMutableOrderedSet\",&,N,V_inflightBuffers"
+ "T@\"NSNumber\",&,N,V_RSSI"
+ "T@\"NSNumber\",&,N,V_leftRSSI"
+ "T@\"NSNumber\",&,N,V_rightRSSI"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_deferredStopQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalDataCollectionQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_playbackQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_updateQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_deferredStopSource"
+ "T@\"NSString\",&,D"
+ "T@\"NSString\",&,N,V_cachedNearbyTranscription"
+ "T@\"NSString\",&,N,V_cachedTranscription"
+ "T@\"NSString\",&,N,V_currentTranscription"
+ "T@\"NSString\",&,N,V_transcription"
+ "T@\"NSString\",C,N,V_currentAudioDeviceName"
+ "T@\"NSString\",C,N,V_currentAudioDeviceType"
+ "T@\"NSTimer\",&,N,V_updateStateTimer"
+ "T@,&,N,V_selectedSound"
+ "T@?,C,N,V_completionHandler"
+ "TB,N,V_cachedHasHearingAidRoute"
+ "TB,N,V_cachedHasLiveListenRoute"
+ "TB,N,V_cachedIsListening"
+ "TB,N,V_cachedIsPlayingBack"
+ "TB,N,V_cachedNearbyIsPlayingBack"
+ "TB,N,V_cachedWirelessSplitterEnabled"
+ "TB,N,V_comfortSoundsEnabledCache"
+ "TB,N,V_internalDataCollectionEnabled"
+ "TB,N,V_isLeftEventHandlerSet"
+ "TB,N,V_isPlayingBack"
+ "TB,N,V_isRightEventHandlerSet"
+ "TB,N,V_isSettingUpPreviewComfortSounds"
+ "TB,N,V_isSettingUpPreviewTimer"
+ "TB,N,V_isTranscribing"
+ "TB,N,V_latestNoiseSampleWasBuffered"
+ "TB,N,V_shouldRebuildAudioQueue"
+ "TB,N,V_timerEnabledCache"
+ "TB,V_audioQueueActive"
+ "TI,N,V_audioDevice"
+ "TI,N,V_audioQueueFlags"
+ "TQ,N,V_cachedCurrentCallsCount"
+ "TQ,N,V_deviceProtocol"
+ "TQ,N,V_leftLoadedProperties"
+ "TQ,N,V_rightLoadedProperties"
+ "TQ,N,V_state"
+ "T^{AudioBufferList=I[1{AudioBuffer=II^v}]},V_bufferList"
+ "T^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I},N,V_aqBuffer"
+ "T^{OpaqueAudioQueue=},N,V_aqRef"
+ "T^{OpaqueAudioQueueTimeline=},N,V_aqTimeline"
+ "Td,N,V_activeDurationTimerEndTimeStampCache"
+ "Td,N,V_startedOn"
+ "Td,N,V_volume"
+ "Td,N,V_xValue"
+ "Td,N,V_yValue"
+ "Tf,N,V_audioLevel"
+ "Tf,N,V_cachedAudioLevel"
+ "The time set is invalid."
+ "The timer is enabled - %d"
+ "The timer option is %lu"
+ "The tinnitus balance is %f"
+ "The tinnitus gain is %d"
+ "Ti,D,N"
+ "Timer is called, but playback has already stopped."
+ "Timer is called. Turning background sounds off."
+ "Timer is set to %@"
+ "Toggle Live Listen: %{BOOL}d -> %{BOOL}d"
+ "TopBackCenter"
+ "TopBackLeft"
+ "TopBackRight"
+ "TopCenter"
+ "TopFrontCenter"
+ "TopFrontLeft"
+ "TopFrontRight"
+ "TopSideLeft"
+ "TopSideRight"
+ "Tq,N,V_cachedNearbyState"
+ "Tq,N,V_cachedState"
+ "Tq,N,V_state"
+ "Tq,V_messagesCount"
+ "Train"
+ "Turning off timer as it is only enabled on the first session."
+ "UNMutableNotificationContent"
+ "UNNotificationRequest"
+ "UNUserNotificationCenter"
+ "Unable to send notification: %@"
+ "Unavailable(SharedAudio)"
+ "Unavailable(Unspecified)"
+ "UpdateState BT: %d, Paired: %d iCloudPaired %d, Connected: %d, Connecting: %d"
+ "Updated SSL mode %@ for %@ with error %@"
+ "Updated for audio route change: LL stream selected %@, HA stream avaialble %@"
+ "Updated for call status change: %lu"
+ "Updated for wireless splitter change: %@"
+ "Updated listening mode %@ for %@ with error %@"
+ "Updating nearby devices"
+ "[Internal] Error opening file %@ for appending. Error: %@"
+ "[Internal] Exception while appending: %@"
+ "[Internal] Failed to create log file: %@"
+ "^{AudioBufferList=I[1{AudioBuffer=II^v}]}"
+ "^{AudioBufferList=I[1{AudioBuffer=II^v}]}16@0:8"
+ "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}"
+ "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16@0:8"
+ "^{OpaqueAudioQueue=}"
+ "^{OpaqueAudioQueue=}16@0:8"
+ "^{OpaqueAudioQueueTimeline=}"
+ "^{OpaqueAudioQueueTimeline=}16@0:8"
+ "_HUAccessory_"
+ "_RSSI"
+ "_aaDeviceManager"
+ "_activeDurationTimerEndTimeStampCache"
+ "_aqBuffer"
+ "_aqRef"
+ "_aqTimeline"
+ "_attemptQueueStart"
+ "_attributeUpdateUpdates"
+ "_audioDevice"
+ "_audioLevel"
+ "_audioPlayerFilterNode"
+ "_audioPlayerMixerNode"
+ "_audioQueueActive"
+ "_audioQueueFlags"
+ "_audioQueueLock"
+ "_audioRingBuffer"
+ "_audioRoutesChanged:"
+ "_availableBuffers"
+ "_bufferArray"
+ "_bufferList"
+ "_bufferLock"
+ "_buffersAvailable"
+ "_buildAudioQueue"
+ "_cachedAudioConverter"
+ "_cachedAudioLevel"
+ "_cachedCurrentCallsCount"
+ "_cachedHasHearingAidRoute"
+ "_cachedHasLiveListenRoute"
+ "_cachedIsListening"
+ "_cachedIsPlayingBack"
+ "_cachedNearbyDevices"
+ "_cachedNearbyIsPlayingBack"
+ "_cachedNearbyState"
+ "_cachedNearbyTranscription"
+ "_cachedState"
+ "_cachedTranscription"
+ "_cachedWirelessSplitterEnabled"
+ "_callsStatusChanged:"
+ "_comfortSoundsEnabledCache"
+ "_completionHandler"
+ "_controller"
+ "_currentAudioDeviceName"
+ "_currentAudioDeviceType"
+ "_currentTranscription"
+ "_deferredStopQueue"
+ "_deferredStopSource"
+ "_deviceImplementation"
+ "_deviceProtocol"
+ "_devicesToMessage"
+ "_discoveredNearbyDeviceIdentifiers"
+ "_discoveryManager"
+ "_format"
+ "_handleRemoteControlSettingChange"
+ "_handleRequestCurrentStateMessageFromDevice:"
+ "_handleStartObservingFromRemoteDevice:"
+ "_handleStartOrStopMessageFromRemoteDevice:message:"
+ "_handleStartOrStopRewindMessageFromRemoteDevice:message:"
+ "_handleStateChangedMessage:"
+ "_handleStateChangedMessage:fromDevice:"
+ "_handleStopObservingFromRemoteDevice:"
+ "_head"
+ "_inflightBuffers"
+ "_initCharacteristicsForPeripheral:"
+ "_initializeInternalDataCollectionIfNeeded"
+ "_internalDataCollectionEnabled"
+ "_internalDataCollectionLogSPLValue:metaData:"
+ "_internalDataCollectionQueue"
+ "_isLeftEventHandlerSet"
+ "_isListeningChanged:audioLevel:isPlayingBack:orTranscriptionChanged:"
+ "_isPlayingBack"
+ "_isRightEventHandlerSet"
+ "_isSettingUpPreviewComfortSounds"
+ "_isSettingUpPreviewTimer"
+ "_isTranscribing"
+ "_lastUpdateStateTimestamp"
+ "_latestNoiseSampleWasBuffered"
+ "_leAudioSessionInfo"
+ "_leftLoadedProperties"
+ "_leftRSSI"
+ "_liveListenCountsPerClient"
+ "_liveListenDidUpdate_enumValue:"
+ "_liveListenObserver"
+ "_liveListenPayloadWithState:audioLevel:isPlayingBack:transcription:"
+ "_messagesCount"
+ "_minimumBufferByteSize"
+ "_nearbyDevices"
+ "_nearbyDevicesChanged"
+ "_notifiedDevices"
+ "_notifyAboutAllObservingDevices"
+ "_notifyAboutObservingDevice:"
+ "_notifyListenersAndPollAudioLevelIfLiveListenIsRunning"
+ "_notifyListenersWithIsListening:audioLevel:isPlayingBack:transcription:"
+ "_observingDevices"
+ "_pendingMessage"
+ "_playbackQueue"
+ "_playbackTimer"
+ "_pollLiveListenAudioLevelAfterDelay"
+ "_queueFormat"
+ "_rebuildAudioQueue"
+ "_receivedMessage:fromDevice:"
+ "_reconfigureQueueFormatForMultiChannelOutputIfNecessary"
+ "_registerForLiveListenUpdates_enumValue:"
+ "_remainingTimeUntilTimestamp:"
+ "_remoteStartDevice"
+ "_rightLoadedProperties"
+ "_rightRSSI"
+ "_sampleRate"
+ "_scheduleDeferredStop"
+ "_scheduleStateUpdate"
+ "_sendEmptyStateToUnauthorizedDevice:"
+ "_sendLatestNearbyUpdate"
+ "_sendMessageToRequestInitialState"
+ "_sendStartObservingMessage"
+ "_sendStartOrStopMessage:"
+ "_sendStartOrStopRewindMessage:"
+ "_sendStopObservingMessage"
+ "_sessionTranscriptions"
+ "_shouldRebuildAudioQueue"
+ "_size"
+ "_startLiveListenFromRemoteDevice:"
+ "_startLiveListenRewind"
+ "_startQueueWithRetry"
+ "_startedOn"
+ "_stopLiveListenFromRemoteDevice:"
+ "_stopLiveListenRewind"
+ "_stoppedScanningForLEAudio"
+ "_tearDownAudioQueue"
+ "_timerEnabledCache"
+ "_toggleLiveListen_enumValue:"
+ "_transcriber"
+ "_transcription"
+ "_updateLock"
+ "_updateQueue"
+ "_updateRemoteStartHistoryForDevice:didStart:"
+ "_updateState"
+ "_updateState:audioLevel:isPlayingBack:transcription:"
+ "_updateStateTimer"
+ "_volume"
+ "_wirelessSplitterEnabledChanged:"
+ "_xValue"
+ "_yValue"
+ "aaDeviceManager"
+ "activeDurationTimerEndTimeStampCache"
+ "activePreset"
+ "activeTimerEndTimeStamp"
+ "addNoiseSample:toCircularBuffer:forMinTime:"
+ "addPeripheral:toDevice:"
+ "applyBypassForFiltersAtIndexes:shouldBypass:"
+ "applyTinnitusBalance"
+ "aqBuffer"
+ "aqRef"
+ "aqTimeline"
+ "arrayByExcludingObjectsInArray:"
+ "attachNodesToEngine"
+ "attributeUpdateUpdates"
+ "audioBufferList"
+ "audioDevice"
+ "audioPlayerFilterNode"
+ "audioPlayerMixerNode"
+ "audioQueueActive"
+ "audioQueueFlags"
+ "audioRingBuffer"
+ "audioSessionIdentifier"
+ "authorizationStatus"
+ "availableBuffers"
+ "availablePropertiesFromDISForPeripheral:"
+ "axMapObjectsUsingBlock:"
+ "axSafelyAddObject:"
+ "ax_automation_is_background_sounds_playing"
+ "ax_hearing_device_protocol_key"
+ "backgroundSoundsPlaying"
+ "bands"
+ "bluetoothAddress"
+ "bluetoothListeningModeFromHearingListeningMode:"
+ "broadcast"
+ "bufferCallback:"
+ "bufferList"
+ "buffersAvailable"
+ "byteSize"
+ "cachedAudioConverter"
+ "cachedAudioLevel"
+ "cachedCurrentCallsCount"
+ "cachedDiscoveredDevices"
+ "cachedHasHearingAidRoute"
+ "cachedHasLiveListenRoute"
+ "cachedIsListening"
+ "cachedIsPlayingBack"
+ "cachedNearbyDevices"
+ "cachedNearbyIsPlayingBack"
+ "cachedNearbyState"
+ "cachedNearbyTranscription"
+ "cachedState"
+ "cachedTranscription"
+ "cachedWirelessSplitterEnabled"
+ "calculateVolumeForSessionWithCompletion:"
+ "canBeDeleted"
+ "canBeEdited"
+ "checkSCIDSServiceDevices"
+ "clearPairedHearingAids"
+ "closeFile"
+ "com.apple.HearingUtilities.HUNoiseController.InternalDataCollectionQueue"
+ "com.apple.LiveListenNotifications"
+ "com.apple.accessibility.hearing.internal.data.collection.changed"
+ "com.apple.springboard.passcodeLockedOrBlocked"
+ "com.hearing.LiveListen"
+ "com.hearing.LiveListen.NearbyStateUpdates"
+ "combinedSessionTranscription"
+ "comfortSoundsAudioQueue"
+ "comfortSoundsEnabledCache"
+ "completionHandler"
+ "configureBandWithType:frequency:bandwidth:atIndex:"
+ "configureBandWithType:frequency:bandwidth:gain:atIndex:"
+ "configureBandsForCoarseFilter"
+ "configureBandsForFineFilter"
+ "configureTinnitusEqualizer"
+ "connectNodesToEngine:"
+ "connectedIdentifiers"
+ "content"
+ "contextualVolumeNeedsEnvironmentalMeasurements"
+ "convertBufferIfNecessary:"
+ "convertToBuffer:error:withInputFromBlock:"
+ "copyWithZone:"
+ "currentAudioDeviceName"
+ "currentAudioDeviceType"
+ "currentCalendar"
+ "currentCallCount"
+ "currentTranscription"
+ "d24@0:8d16"
+ "d56@0:8d16d24d32d40d48"
+ "dataUsingEncoding:"
+ "dateByAddingUnit:value:toDate:options:"
+ "decodeFloatForKey:"
+ "deferredStopQueue"
+ "deferredStopSource"
+ "deleteAssets"
+ "descriptiveProperties"
+ "deviceDiscoveryManager:updatedDevices:"
+ "deviceImplementation"
+ "deviceName"
+ "deviceProtocol"
+ "didAddPeripheral:"
+ "discoveredDevices"
+ "discoveredNearbyDeviceIdentifiers"
+ "discoveringServiceUUIDs"
+ "discoveryManager"
+ "earForPeripheral:"
+ "encodeFloat:forKey:"
+ "endDate"
+ "endTimeStamp"
+ "enhancedTransparencyVersion"
+ "enumerateAudioBluetoothDevicesUsingBlock:"
+ "enumerateAvailableDevicesWithBlock:andCompletion:"
+ "enumerateAvailablePSEDevicesWithBlock:andCompletion:"
+ "enumerateConnectedBluetoothDevices:usingBlock:andCompletion:"
+ "enumerateProductCodesforAddresses:withBlock:"
+ "error"
+ "eventType"
+ "fileExistsAtPath:"
+ "fileHandleForUpdatingAtPath:"
+ "format"
+ "frameLength"
+ "frequencyForBandPass"
+ "gainForHighResonance"
+ "gainForLeftBellFilters"
+ "gainForLowResonance"
+ "gainForRightBellFilters"
+ "gapaFlags"
+ "getCBDeviceForCurrentRouteWithCompletion:"
+ "getCurrentRouteListeningModeWithCompletion:"
+ "getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:"
+ "getHearingProtectionSupportforAddress:withCompletion:"
+ "getNotificationSettingsWithCompletionHandler:"
+ "getPMEEverywhereSupportStateForAddress:withCompletion:"
+ "getPSEVersionForAddress:withCompletion:"
+ "getPairedDeviceSupportsPSE:"
+ "getProductCodeforAddress:withCompletion:"
+ "getSSLEnabledForAddress:withCompletion:"
+ "getSSLSupportStateForAddress:withCompletion:"
+ "handleMediaServicesReset"
+ "handlePlaybackForDifferentCategory"
+ "handlePlaybackForSameCategory"
+ "handleRTTMessageInjection:"
+ "handleRTTTranslationLocaleMessage:"
+ "hearingAidForPeripheralID:"
+ "hearingListeningModeFromBluetoothListeningMode:"
+ "hearingProtectionCapability"
+ "hustopqueue"
+ "i24@0:8@16"
+ "i24@0:8Q16"
+ "indexSetWithIndexesInRange:"
+ "inflightBuffers"
+ "initFromFormat:toFormat:"
+ "initWithBuffer:"
+ "initWithCapacity:"
+ "initWithController:"
+ "initWithCount:"
+ "initWithDelegate:"
+ "initWithNumberOfBands:"
+ "initWithPCMFormat:bufferListNoCopy:deallocator:"
+ "initWithPCMFormat:frameCapacity:"
+ "initWithPoint:"
+ "initWithSampleRate:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "inputFormat"
+ "internalDataCollectionEnabled"
+ "internalDataCollectionQueue"
+ "invalidateTimer"
+ "isAvailable"
+ "isInstalled"
+ "isLEAudioEnabled"
+ "isLEAudioServiceInServiceUUIDs:"
+ "isLeftEventHandlerSet"
+ "isLocallyPaired"
+ "isNearby"
+ "isPlayingBack"
+ "isRightEventHandlerSet"
+ "isSameCategoryAsSelectedSound:"
+ "isSettingUpPreviewComfortSounds"
+ "isSettingUpPreviewTimer"
+ "isTranscribing"
+ "isWritable"
+ "isiPad"
+ "isiPhone"
+ "lastUpdateStateTimestamp"
+ "latestNoiseSampleWasBuffered"
+ "leftRSSI"
+ "linearTransformation:inputMin:inputMax:outputMin:outputMax:"
+ "listenForChangesInEqualizer"
+ "listenForChangesInTimer"
+ "listeningModeConfigs"
+ "liveListenCountsPerClient"
+ "liveListenLevelsTimer"
+ "liveListenObserver"
+ "liveListenRemoteControlEnabled"
+ "liveListenRemoteStartHistory"
+ "locations"
+ "logMessageForTimer:"
+ "messagesCount"
+ "modifyDevice:settings:completion:"
+ "nearbyDeviceWithSCIDSDevice:justCreated:"
+ "new"
+ "notifiedDevices"
+ "observeRemoteLiveListenUpdates:"
+ "observingDevices"
+ "orderedSet"
+ "outputFormat"
+ "paSupportedWiredRoutes"
+ "paSupportedWirelessRoutes"
+ "pause"
+ "pendingMessage"
+ "peripheralDidUpdateDeviceInfo"
+ "pickableRoutes: %@"
+ "playbackQueue"
+ "playbackTimer"
+ "playback_audio_queue"
+ "pmeEverywhereCapability"
+ "pmeEverywhereSupportedForAddress:"
+ "prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXLLEnableSpecID"
+ "presetIndex"
+ "presetName"
+ "presetResults"
+ "previewEnabled"
+ "primaryPlacement"
+ "processAutomationRequest:"
+ "processBTPresetsUpdate:activePreset:forEar:"
+ "processConnectedIdentifiers:andLocations:"
+ "productCode"
+ "productID"
+ "propertyForCharacteristic:"
+ "pseVersionForAddress:"
+ "queueFormat"
+ "registerAttributeUpdateBlock:withListener:"
+ "registerListener:forLiveListenHandler:"
+ "registerUpdateBlock:withListener:"
+ "remoteStartDevice"
+ "requestAuthorizationWithOptions:completionHandler:"
+ "requestNoiseBuffersForTimeInterval:withHandler:"
+ "requestWithIdentifier:content:trigger:"
+ "resetTimers"
+ "rightRSSI"
+ "routesPlayAndRecord: %@"
+ "scIDSServiceDidAddDevices:"
+ "scanningServiceUUIDs"
+ "scheduleBuffer:completionHandler:"
+ "scheduleBuffer:completionHandler:lastBuffer:"
+ "scheduleTimer:"
+ "secondaryPlacement"
+ "seekToEndOfFile"
+ "selectiveSpeechListeningCapability"
+ "selectiveSpeechListeningConfig"
+ "sendMessageWithPayload:identifier:andResponseBlock:"
+ "sendSynchronousMessageWithPayloadAndGetResponse:andIdentifier:"
+ "serviceTypeDescription"
+ "sessionDidUpdateLocations:"
+ "sessionDidUpdateValue:forProperty:"
+ "sessionInfo"
+ "sessionState"
+ "sessionTranscriptions"
+ "setAaDeviceManager:"
+ "setActiveDurationTimerEndTimeStampCache:"
+ "setActivePreset:OptionalPresetIndex:withResponse:"
+ "setActiveTimerEndTimeStamp:"
+ "setAqBuffer:"
+ "setAqRef:"
+ "setAqTimeline:"
+ "setAttributeUpdateUpdates:"
+ "setAudioDevice:"
+ "setAudioLevel:"
+ "setAudioPlayerFilterNode:"
+ "setAudioPlayerMixerNode:"
+ "setAudioQueueActive:"
+ "setAudioQueueFlags:"
+ "setAudioRingBuffer:"
+ "setAvailableBuffers:"
+ "setBandwidth:"
+ "setBasicPropertiesLoaded"
+ "setBufferList:"
+ "setBuffersAvailable:"
+ "setBypass:"
+ "setCachedAudioConverter:"
+ "setCachedAudioLevel:"
+ "setCachedCurrentCallsCount:"
+ "setCachedHasHearingAidRoute:"
+ "setCachedHasLiveListenRoute:"
+ "setCachedIsListening:"
+ "setCachedIsPlayingBack:"
+ "setCachedNearbyDevices:"
+ "setCachedNearbyIsPlayingBack:"
+ "setCachedNearbyState:"
+ "setCachedNearbyTranscription:"
+ "setCachedState:"
+ "setCachedTranscription:"
+ "setCachedWirelessSplitterEnabled:"
+ "setComfortSoundsEnabledCache:"
+ "setCompletionHandler:"
+ "setController:"
+ "setCurrentAudioDeviceName:"
+ "setCurrentAudioDeviceType:"
+ "setCurrentRouteListeningMode:"
+ "setCurrentTranscription:"
+ "setDateStyle:"
+ "setDefaultActionURL:"
+ "setDeferredStopQueue:"
+ "setDeferredStopSource:"
+ "setDeviceImplementation:"
+ "setDeviceProtocol:"
+ "setDiscoveredNearbyDeviceIdentifiers:"
+ "setDiscoveryManager:"
+ "setFilterBoost:"
+ "setFilterType:"
+ "setFormat:"
+ "setFrequency:"
+ "setGain:"
+ "setGlobalGain:"
+ "setInflightBuffers:"
+ "setInternalDataCollectionEnabled:"
+ "setInternalDataCollectionQueue:"
+ "setIsLeftEventHandlerSet:"
+ "setIsPlayingBack:"
+ "setIsRightEventHandlerSet:"
+ "setIsSettingUpPreviewComfortSounds:"
+ "setIsSettingUpPreviewTimer:"
+ "setIsTranscribing:"
+ "setLastUpdateStateTimestamp:"
+ "setLatestNoiseSampleWasBuffered:"
+ "setLeAudioEventHandler:"
+ "setLeftRSSI:"
+ "setListeningMode:"
+ "setLiveListenCountsPerClient:"
+ "setLiveListenLevelsTimer:"
+ "setLiveListenObserver:"
+ "setLiveListenRemoteControlEnabled:"
+ "setLiveListenRemoteStartHistory:"
+ "setMessagesCount:"
+ "setNotifiedDevices:"
+ "setObservingDevices:"
+ "setOutputFormat:"
+ "setOutputVolume:"
+ "setPan:"
+ "setPendingMessage:"
+ "setPlaybackQueue:"
+ "setPlaybackTimer:"
+ "setPowerState:completion:"
+ "setPreviewEnabled:"
+ "setQueueFormat:"
+ "setRSSI:"
+ "setRemoteStartDevice:"
+ "setRightRSSI:"
+ "setSSLEnabled:forAddress:"
+ "setSelectiveSpeechListeningConfig:"
+ "setSessionTranscriptions:"
+ "setShouldRebuildAudioQueue:"
+ "setShouldSuppressDefaultAction:"
+ "setStartedOn:"
+ "setTimeStyle:"
+ "setTimerDurationInSeconds:"
+ "setTimerEnabled:"
+ "setTimerEnabledCache:"
+ "setTimerEndInterval:"
+ "setTimerInHoursAndMinutes:minutes:"
+ "setTimerOnlyOnFirstSession:"
+ "setTimerOption:"
+ "setTinnitusBalance:"
+ "setTinnitusFilterEnabled:"
+ "setTinnitusFilterMode:"
+ "setTinnitusFilterPoint:"
+ "setTranscriber:"
+ "setTranscription:"
+ "setUnitsStyle:"
+ "setUpdateHandler:"
+ "setUpdateLock:"
+ "setUpdateQueue:"
+ "setUpdateStateTimer:"
+ "setVolume:withResponse:"
+ "setXValue:"
+ "setYValue:"
+ "setupCentralManagerForLEAudio"
+ "setupLoadingProperties"
+ "setupTimerIfEnabled"
+ "setupTimerIfNeeded"
+ "setupUpdatesHandlerForLEAudioPeripheral:"
+ "shouldEnableNoiseMeasurements"
+ "shouldRebuildAudioQueue"
+ "shouldStart"
+ "sleepForTimeInterval:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices"
+ "softlink:r:path:/System/Library/Frameworks/UserNotifications.framework/UserNotifications"
+ "softlink:r:path:/System/Library/PrivateFrameworks//AccessibilityRemoteServices.framework/AccessibilityRemoteServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription"
+ "startDate"
+ "startLiveListenRewind"
+ "startObserving"
+ "startObservingRemoteLiveListenUpdates"
+ "startObservingRemoteSession"
+ "startTranscribing"
+ "startTranscribing:targetPID:callbackBlock:error:"
+ "startedOn"
+ "stopComfortSound:"
+ "stopLiveListenRewind"
+ "stopObserving"
+ "stopObservingRemoteLiveListenUpdates"
+ "stopObservingRemoteSession"
+ "stopTranscribing"
+ "stopTranscribing:targetPID:error:"
+ "stringFromTimeInterval:"
+ "swapPeripheral:toEar:"
+ "timerDurationInSeconds"
+ "timerEnabled"
+ "timerEnabledCache"
+ "timerEndInterval"
+ "timerOnlyOnFirstSession"
+ "timerOption"
+ "tinnitusBalance"
+ "tinnitusFilterEnabled"
+ "tinnitusFilterMode"
+ "tinnitusFilterPoint"
+ "toggleLiveListenRewind:"
+ "transcribedText"
+ "transcriber"
+ "transcription"
+ "transcriptionDidStart"
+ "transcriptionDidUpdate:"
+ "transparencyAutobeamformer"
+ "transparencyOwnVoice"
+ "turnBluetoothOnWithCompletion:"
+ "unregisterLiveListenListener:"
+ "updateLock"
+ "updateQueue"
+ "updateStateTimer"
+ "updatedValue"
+ "v16@?0@\"AXLTTranscribedData\"8"
+ "v16@?0@\"AudioAccessoryDevice\"8"
+ "v16@?0@\"CBLEAudioSessionEvent\"8"
+ "v16@?0@\"UNNotificationSettings\"8"
+ "v16@?0d8"
+ "v16@?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8"
+ "v24@0:8@\"AVAudioFormat\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8^{AudioBufferList=I[1{AudioBuffer=II^v}]}16"
+ "v24@0:8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16"
+ "v24@0:8^{OpaqueAudioQueue=}16"
+ "v24@0:8^{OpaqueAudioQueueTimeline=}16"
+ "v24@?0@\"CBDevice\"8@\"NSDictionary\"16"
+ "v24@?0@\"CBPeripheral\"8@\"CBLEAudioPeripheralUpdateEvent\"16"
+ "v28@?0B8f12B16@\"NSString\"20"
+ "v32@0:8@\"AVAudioPCMBuffer\"16@?<v@?>24"
+ "v32@0:8@\"AXRDeviceDiscoveryManager\"16@\"NSArray\"24"
+ "v32@0:8d16@?24"
+ "v32@0:8q16q24"
+ "v32@?0@\"AudioAccessoryDevice\"8Q16^B24"
+ "v32@?0@\"NSUUID\"8@\"NSNumber\"16^B24"
+ "v32@?0q8f16B20@\"NSString\"24"
+ "v36@0:8@\"AVAudioPCMBuffer\"16@?<v@?>24B32"
+ "v36@0:8@16@24f32"
+ "v36@0:8@16@24i32"
+ "v36@0:8B16@?20@?28"
+ "v36@0:8B16f20B24@28"
+ "v36@?0d8q16B24@\"NSString\"28"
+ "v40@?0@\"NSString\"8@\"NSString\"16Q24^B32"
+ "v44@?0@\"NSDictionary\"8Q16@\"NSString\"24B32Q36"
+ "v48@0:8q16d24d32q40"
+ "v56@0:8q16d24d32d40q48"
+ "v64@?0@\"NSString\"8@\"NSString\"16Q24Q32Q40Q48^B56"
+ "validateTimerDuration"
+ "validateTimerEndInterval"
+ "vendorID"
+ "void LiveListenRequestNotificationAuthorization(void)_block_invoke"
+ "void _LiveListenSendUserNotification(NSString *__strong, BOOL)"
+ "void _LiveListenSendUserNotification(NSString *__strong, BOOL)_block_invoke"
+ "volume"
+ "wait"
+ "widthForBandPass"
+ "writeData:"
+ "writeToFile:atomically:"
+ "x"
+ "xValue"
+ "y"
+ "yValue"
+ "yyyy-MM-dd HH:mm:ss"
+ "\x812y($d\"\""
+ "\xf0;)Q"
- "%@ in %@"
- "-[AXHeardController startServer]_block_invoke_29"
- "-[AXHearingAidDevice updateNameWithAdvertisingData:]"
- "-[HUAccessoryHearingSyncManager hasPairedDeviceWithHearingProtectionEnabled]"
- "-[HUComfortSoundsController stopOnQueueAndClearRoute:]"
- "-[HUComfortSoundsController updateVolumeForSessionAndRamp:]_block_invoke"
- "/usr/lib/libAccessibility.dylib"
- "/usr/local/lib/libAccessibility.dylib"
- "@\"HUComfortSound\""
- "AXHearingAidDevice:%p:[%@] [%@, %@, %@, %@] L:%d R:%d,  l-uuid: %@ r-uuid: %@ - [%@, %@] [%@, %@]"
- "After timeout gave up on Media handoff, transiton connection to peer"
- "B16@?0@\"BluetoothDevice\"8"
- "BT connectPeripheral state: %ld, %@"
- "CS sound changed. Starting"
- "CentralManager didConnectPeripheral state: %ld %@"
- "CentralManager didDisconnectPeripheral, Connect"
- "CentralManager didDiscoverPeripheral, Connect"
- "CentralManager didRetrievePeripherals"
- "Device Type"
- "Firmware version found: %@"
- "HP version %@, product code %@, supported %@, for accessory %@"
- "Hardware version found: %@"
- "Hearing aid Manufacturer found: %@"
- "Hearing aid Model Number found: %@"
- "Hearing aid left firmware version found: %@"
- "Hearing aid left hardware version found: %@"
- "Hearing aid right firmware version found: %@"
- "Hearing aid right hardware version found: %@"
- "Listening modes current: %@ new: %@"
- "Manufacturer found: |%@|"
- "Model Number found: |%@|"
- "No paired hearing protection device is found"
- "Registing for device availability %d, %d, %lf"
- "SC IDS Service removed devices: %@, updated devices: %@"
- "SC IDS Service sending message %@"
- "Skipping device because not supported %@ [%d, %d] {%d, %d} %@"
- "Skipping pairing becuase not a hearing device %@"
- "Starting scan %@"
- "Stopping scan"
- "T@\"HUComfortSound\",&,N"
- "T@\"HUComfortSound\",&,N,V_selectedSound"
- "TQ,N,V_deviceType"
- "UpdateState BT: %d, Paired: %d, Connected: %d, Connecting: %d"
- "User requested handoff complete"
- "_AXSUpdateAccessibilityEnabled"
- "_startIDSConnection %@"
- "address"
- "bluetoothAvailabilityDidChange:"
- "ccom.apple.springboard.passcodeLockedOrBlocked"
- "comfort_sounds_audio"
- "deviceFromAddressString:"
- "disconnectFromPeripheral from %@"
- "featureCapability:"
- "getAACPCapabilityInteger:"
- "handleRTTVoicemailMessage:"
- "hasPairedDeviceWithHearingProtectionEnabled"
- "hasPeers"
- "inEarStatusPrimary:secondary:"
- "liveListenDevice"
- "paCurrentBluetoothDeviceSupportingTransparencyAccommodationsAsync"
- "pairedDevices"
- "productId"
- "setSharedInstanceQueue:"
- "updateNameWithAdvertisingData:"
- "v16@?0@\"BluetoothDevice\"8"
- "v32@?0@\"BluetoothDevice\"8Q16^B24"
- "vendorId"
- "\x812y($dB"
- "\xf0!"
- "\xf0;)"

```
