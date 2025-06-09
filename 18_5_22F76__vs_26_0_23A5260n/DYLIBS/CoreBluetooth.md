## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-185.7.0.0.0
-  __TEXT.__text: 0x96e94
-  __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x8d64
-  __TEXT.__const: 0x2503
-  __TEXT.__oslogstring: 0x260f
-  __TEXT.__cstring: 0x12048
-  __TEXT.__gcc_except_tab: 0x23d0
-  __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x1be0
-  __TEXT.__objc_classname: 0x6db
-  __TEXT.__objc_methname: 0x14c61
-  __TEXT.__objc_methtype: 0x2271
-  __TEXT.__objc_stubs: 0x8dc0
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x4870
-  __DATA_CONST.__objc_classlist: 0x1d8
+190.40.1.2.0
+  __TEXT.__text: 0xb3c90
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_methlist: 0xa044
+  __TEXT.__const: 0x2703
+  __TEXT.__oslogstring: 0x2b1b
+  __TEXT.__cstring: 0x14ecf
+  __TEXT.__gcc_except_tab: 0x2f30
+  __TEXT.__ustring: 0x82
+  __TEXT.__unwind_info: 0x21d8
+  __TEXT.__eh_frame: 0x98
+  __TEXT.__objc_classname: 0x805
+  __TEXT.__objc_methname: 0x16b50
+  __TEXT.__objc_methtype: 0x24e8
+  __TEXT.__objc_stubs: 0xb600
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0x5578
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4608
+  __DATA_CONST.__objc_selrefs: 0x4fd8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0xaf40
-  __AUTH_CONST.__objc_const: 0x10a48
-  __AUTH_CONST.__objc_intobj: 0x8d0
+  __AUTH_CONST.__auth_got: 0x9b8
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0xdba0
+  __AUTH_CONST.__objc_const: 0x11dc8
+  __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xef8
-  __DATA.__data: 0xd80
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0xf64
+  __DATA.__data: 0xe68
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1130
+  __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__data: 0x1d0
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B91BDC02-1B05-3F5A-BFB3-23A2EE72D141
-  Functions: 3722
-  Symbols:   12012
-  CStrings:  9049
+  UUID: D9775BC6-948C-360F-BC28-403CDE608F19
+  Functions: 4234
+  Symbols:   13766
+  CStrings:  10423
 
Symbols:
+ +[CBManager checkIfExtension]
+ +[CBManager checkIfExtension].cold.1
+ +[CBPowerSource supportsSecureCoding]
+ +[CBUserNotificationRequest supportsSecureCoding]
+ -[CBAdvertiser nearbyInfoV2NearbyFaceTimeData]
+ -[CBAdvertiser proximityServicePayload]
+ -[CBAdvertiser proximityServiceSubType]
+ -[CBAdvertiser randomData]
+ -[CBAdvertiser setNearbyInfoV2NearbyFaceTimeData:]
+ -[CBAdvertiser setProximityServicePayload:]
+ -[CBAdvertiser setProximityServiceSubType:]
+ -[CBAdvertiser setRandomData:]
+ -[CBApplePayloadTypeInfo maxAge]
+ -[CBApplePayloadTypeInfo setMaxAge:]
+ -[CBCentralManager HandleLESynchronizationEventMsg:]
+ -[CBCentralManager HandleLESynchronizationEventMsg:].cold.1
+ -[CBCentralManager _handleLEAudioXpcEvents:]
+ -[CBCentralManager _handleLEAudioXpcEvents:].cold.1
+ -[CBCentralManager _handleLEAudioXpcEvents:].cold.2
+ -[CBCentralManager _handleLEAudioXpcEvents:].cold.3
+ -[CBCentralManager _handleLEAudioXpcEvents:].cold.4
+ -[CBCentralManager _scanForPeripheralsWithServices:options:completion:]
+ -[CBCentralManager audioSessions]
+ -[CBCentralManager changeMicrophoneGainSettingForSession:forAudioInputType:withMicGain:withResponse:]
+ -[CBCentralManager changeVolumeForSession:withVolume:withResponse:]
+ -[CBCentralManager changeVolumeMuteStateForSession:withVolumeMuteState:withResponse:]
+ -[CBCentralManager changeVolumeOffsetForSession:toLocation:withVolumeOffSet:withResponse:]
+ -[CBCentralManager cisConnectEvent]
+ -[CBCentralManager cisDisconnectEvent]
+ -[CBCentralManager connectCIS:]
+ -[CBCentralManager createSessionEvent:withMsg:]
+ -[CBCentralManager createSessionEvent:withMsg:].cold.1
+ -[CBCentralManager createXPCForLEAudio]
+ -[CBCentralManager createXPCForLEAudio].cold.1
+ -[CBCentralManager createXPCForLEAudio].cold.2
+ -[CBCentralManager createXPCForLEAudio].cold.3
+ -[CBCentralManager disconnectCIS:]
+ -[CBCentralManager handleActivePresetUpdated:]
+ -[CBCentralManager handleConnectCISComplete:]
+ -[CBCentralManager handleConnectLEAudioComplete:]
+ -[CBCentralManager handleDisconnectCISComplete:]
+ -[CBCentralManager handleFeaturesUpdated:]
+ -[CBCentralManager handleLEAudioMsg:]
+ -[CBCentralManager handleLEAudioMsg:].cold.1
+ -[CBCentralManager handleLEAudioMsg:].cold.2
+ -[CBCentralManager handleLEAudioMsg:].cold.3
+ -[CBCentralManager handleLEAudioMsg:].cold.4
+ -[CBCentralManager handleLEAudioSessionEvents:]
+ -[CBCentralManager handleLEAudioSessionEvents:].cold.1
+ -[CBCentralManager handleLEAudioXpcInterrupted]
+ -[CBCentralManager handleLEAudioXpcInterrupted].cold.1
+ -[CBCentralManager handleLEAudioXpcInvalid]
+ -[CBCentralManager handleLEAudioXpcInvalid].cold.1
+ -[CBCentralManager handleMicrophoneGainUpdated:]
+ -[CBCentralManager handleMicrophoneMuteUpdated:]
+ -[CBCentralManager handlePresetNameUpdated:]
+ -[CBCentralManager handlePresetsUpdated:]
+ -[CBCentralManager handleRemoveCIGComplete:]
+ -[CBCentralManager handleSessionCompleted:]
+ -[CBCentralManager handleSessionCompleted:].cold.1
+ -[CBCentralManager handleSessionMicrophoneGainUpdated:]
+ -[CBCentralManager handleSessionMicrophoneGainUpdated:].cold.1
+ -[CBCentralManager handleSessionMicrophoneMuteUpdated:]
+ -[CBCentralManager handleSessionMicrophoneMuteUpdated:].cold.1
+ -[CBCentralManager handleSessionVolumeMuteUpdated:]
+ -[CBCentralManager handleSessionVolumeMuteUpdated:].cold.1
+ -[CBCentralManager handleSessionVolumeOffsetUpdated:]
+ -[CBCentralManager handleSessionVolumeOffsetUpdated:].cold.1
+ -[CBCentralManager handleSessionVolumeUpdated:]
+ -[CBCentralManager handleSessionVolumeUpdated:].cold.1
+ -[CBCentralManager handleSetupCIGComplete:]
+ -[CBCentralManager handleSetupCIGComplete:].cold.1
+ -[CBCentralManager handleSetupCIGComplete:].cold.2
+ -[CBCentralManager handleVolumeInputGainUpdated:]
+ -[CBCentralManager handleVolumeMuteUpdated:]
+ -[CBCentralManager handleVolumeOffsetUpdated:]
+ -[CBCentralManager handleVolumeUpdated:]
+ -[CBCentralManager initCISCentral]
+ -[CBCentralManager leAudioEventHandler]
+ -[CBCentralManager registerLEAudioClient]
+ -[CBCentralManager removeCIG:completion:]
+ -[CBCentralManager removeCIGCompletion]
+ -[CBCentralManager sendLEAudioMsg:args:completion:]
+ -[CBCentralManager sendLEAudioMsg:args:completion:].cold.1
+ -[CBCentralManager setCisConnectEvent:]
+ -[CBCentralManager setCisDisconnectEvent:]
+ -[CBCentralManager setLeAudioEventHandler:]
+ -[CBCentralManager setMicrophoneMuteStateForSession:withMicMuteState:withResponse:]
+ -[CBCentralManager setRemoveCIGCompletion:]
+ -[CBCentralManager setSetupCIGCompletion:]
+ -[CBCentralManager setupCIG:completion:]
+ -[CBCentralManager setupCIGCompletion]
+ -[CBCentralManager startLEAudioXPC]
+ -[CBCentralManager startSecurityRequest]
+ -[CBCharacteristic addExtendedProperties]
+ -[CBCharacteristic setAddExtendedProperties:]
+ -[CBControllerSettings gameControllerAutoSwitchMode]
+ -[CBControllerSettings gameControllerUSBBluetoothPairing]
+ -[CBControllerSettings setGameControllerAutoSwitchMode:]
+ -[CBControllerSettings setGameControllerUSBBluetoothPairing:]
+ -[CBCoordinatedMemberInfo memberRank]
+ -[CBCoordinatedMemberInfo setMemberRank:]
+ -[CBCoordinatedSetInfo .cxx_destruct]
+ -[CBCoordinatedSetInfo connectedIdentifiers]
+ -[CBCoordinatedSetInfo copyWithZone:]
+ -[CBCoordinatedSetInfo initWithInfo:withSize:]
+ -[CBCoordinatedSetInfo setConnectedIdentifiers:]
+ -[CBCoordinatedSetInfo setName]
+ -[CBCoordinatedSetInfo setSetName:]
+ -[CBCoordinatedSetInfo setSetSize:]
+ -[CBCoordinatedSetInfo setSize]
+ -[CBDevice _clearAirplaySourceFlags]
+ -[CBDevice _clearAirplayTargetFlags]
+ -[CBDevice _clearAirplayTargetIPv4]
+ -[CBDevice _clearAirplayTargetIPv6]
+ -[CBDevice _clearDeviceInfoKey:]
+ -[CBDevice _clearDockKitAccessoryPayloadData]
+ -[CBDevice _clearFidoPayloadData]
+ -[CBDevice _clearGfpModelID]
+ -[CBDevice _clearGfpPayloadData]
+ -[CBDevice _clearHomeKitV1CompatibleVersion]
+ -[CBDevice _clearHomeKitV1ConfigurationNumber]
+ -[CBDevice _clearHomeKitV1Flags]
+ -[CBDevice _clearHomeKitV1SetupHash]
+ -[CBDevice _clearHomeKitV1StateNumber]
+ -[CBDevice _clearHomeKitV2AuthTagData]
+ -[CBDevice _clearHomeKitV2InstanceID]
+ -[CBDevice _clearHomeKitV2StateNumber]
+ -[CBDevice _clearHomeKitV2Value]
+ -[CBDevice _clearMspAddressData]
+ -[CBDevice _clearMspDeviceClass]
+ -[CBDevice _clearMspDisplayName]
+ -[CBDevice _clearMspSubScenario]
+ -[CBDevice _clearNearbyActionAuthTag]
+ -[CBDevice _clearNearbyActionDeviceClass]
+ -[CBDevice _clearNearbyActionFlags]
+ -[CBDevice _clearNearbyActionType]
+ -[CBDevice _clearNearbyActionV2Flags]
+ -[CBDevice _clearNearbyActionV2Type]
+ -[CBDevice _clearObjectSetupFlags]
+ -[CBDevice _clearObjectSetupFontCode]
+ -[CBDevice _clearObjectSetupMessage]
+ -[CBDevice _clearProximityServiceData]
+ -[CBDevice _clearProximityServiceFlags]
+ -[CBDevice _clearProximityServiceMeasuredPower]
+ -[CBDevice _clearProximityServicePSM]
+ -[CBDevice _clearProximityServiceSetupHash]
+ -[CBDevice _clearProximityServiceSubType]
+ -[CBDevice _clearProximityServiceVersion]
+ -[CBDevice _clearSpatialInteractionConfigFlags]
+ -[CBDevice _clearSpatialInteractionFlags]
+ -[CBDevice _clearSpatialInteractionIdentifiers]
+ -[CBDevice _clearSpatialInteractionPeerID]
+ -[CBDevice _clearSpatialInteractionPresenceConfigData]
+ -[CBDevice _clearSpatialInteractionTokenData]
+ -[CBDevice _clearSpatialInteractionUWBConfigData]
+ -[CBDevice _clearSpatialInteractionUserInfo]
+ -[CBDevice _matchingFlags:exactMatch:]
+ -[CBDevice airplayTargetIPv6]
+ -[CBDevice decryptNearbyInfoV2PayloadWithIdentity:error:].cold.1
+ -[CBDevice isEqualToDevice:exactMatch:]
+ -[CBDevice isEqualToDevice:exactMatch:].cold.1
+ -[CBDevice isEqualToDevice:exactMatch:].cold.10
+ -[CBDevice isEqualToDevice:exactMatch:].cold.100
+ -[CBDevice isEqualToDevice:exactMatch:].cold.101
+ -[CBDevice isEqualToDevice:exactMatch:].cold.102
+ -[CBDevice isEqualToDevice:exactMatch:].cold.103
+ -[CBDevice isEqualToDevice:exactMatch:].cold.104
+ -[CBDevice isEqualToDevice:exactMatch:].cold.105
+ -[CBDevice isEqualToDevice:exactMatch:].cold.106
+ -[CBDevice isEqualToDevice:exactMatch:].cold.107
+ -[CBDevice isEqualToDevice:exactMatch:].cold.11
+ -[CBDevice isEqualToDevice:exactMatch:].cold.12
+ -[CBDevice isEqualToDevice:exactMatch:].cold.13
+ -[CBDevice isEqualToDevice:exactMatch:].cold.14
+ -[CBDevice isEqualToDevice:exactMatch:].cold.15
+ -[CBDevice isEqualToDevice:exactMatch:].cold.16
+ -[CBDevice isEqualToDevice:exactMatch:].cold.17
+ -[CBDevice isEqualToDevice:exactMatch:].cold.18
+ -[CBDevice isEqualToDevice:exactMatch:].cold.19
+ -[CBDevice isEqualToDevice:exactMatch:].cold.2
+ -[CBDevice isEqualToDevice:exactMatch:].cold.20
+ -[CBDevice isEqualToDevice:exactMatch:].cold.21
+ -[CBDevice isEqualToDevice:exactMatch:].cold.22
+ -[CBDevice isEqualToDevice:exactMatch:].cold.23
+ -[CBDevice isEqualToDevice:exactMatch:].cold.24
+ -[CBDevice isEqualToDevice:exactMatch:].cold.25
+ -[CBDevice isEqualToDevice:exactMatch:].cold.26
+ -[CBDevice isEqualToDevice:exactMatch:].cold.27
+ -[CBDevice isEqualToDevice:exactMatch:].cold.28
+ -[CBDevice isEqualToDevice:exactMatch:].cold.29
+ -[CBDevice isEqualToDevice:exactMatch:].cold.3
+ -[CBDevice isEqualToDevice:exactMatch:].cold.30
+ -[CBDevice isEqualToDevice:exactMatch:].cold.31
+ -[CBDevice isEqualToDevice:exactMatch:].cold.32
+ -[CBDevice isEqualToDevice:exactMatch:].cold.33
+ -[CBDevice isEqualToDevice:exactMatch:].cold.34
+ -[CBDevice isEqualToDevice:exactMatch:].cold.35
+ -[CBDevice isEqualToDevice:exactMatch:].cold.36
+ -[CBDevice isEqualToDevice:exactMatch:].cold.37
+ -[CBDevice isEqualToDevice:exactMatch:].cold.38
+ -[CBDevice isEqualToDevice:exactMatch:].cold.39
+ -[CBDevice isEqualToDevice:exactMatch:].cold.4
+ -[CBDevice isEqualToDevice:exactMatch:].cold.40
+ -[CBDevice isEqualToDevice:exactMatch:].cold.41
+ -[CBDevice isEqualToDevice:exactMatch:].cold.42
+ -[CBDevice isEqualToDevice:exactMatch:].cold.43
+ -[CBDevice isEqualToDevice:exactMatch:].cold.44
+ -[CBDevice isEqualToDevice:exactMatch:].cold.45
+ -[CBDevice isEqualToDevice:exactMatch:].cold.46
+ -[CBDevice isEqualToDevice:exactMatch:].cold.47
+ -[CBDevice isEqualToDevice:exactMatch:].cold.48
+ -[CBDevice isEqualToDevice:exactMatch:].cold.49
+ -[CBDevice isEqualToDevice:exactMatch:].cold.5
+ -[CBDevice isEqualToDevice:exactMatch:].cold.50
+ -[CBDevice isEqualToDevice:exactMatch:].cold.51
+ -[CBDevice isEqualToDevice:exactMatch:].cold.52
+ -[CBDevice isEqualToDevice:exactMatch:].cold.53
+ -[CBDevice isEqualToDevice:exactMatch:].cold.54
+ -[CBDevice isEqualToDevice:exactMatch:].cold.55
+ -[CBDevice isEqualToDevice:exactMatch:].cold.56
+ -[CBDevice isEqualToDevice:exactMatch:].cold.57
+ -[CBDevice isEqualToDevice:exactMatch:].cold.58
+ -[CBDevice isEqualToDevice:exactMatch:].cold.59
+ -[CBDevice isEqualToDevice:exactMatch:].cold.6
+ -[CBDevice isEqualToDevice:exactMatch:].cold.60
+ -[CBDevice isEqualToDevice:exactMatch:].cold.61
+ -[CBDevice isEqualToDevice:exactMatch:].cold.62
+ -[CBDevice isEqualToDevice:exactMatch:].cold.63
+ -[CBDevice isEqualToDevice:exactMatch:].cold.64
+ -[CBDevice isEqualToDevice:exactMatch:].cold.65
+ -[CBDevice isEqualToDevice:exactMatch:].cold.66
+ -[CBDevice isEqualToDevice:exactMatch:].cold.67
+ -[CBDevice isEqualToDevice:exactMatch:].cold.68
+ -[CBDevice isEqualToDevice:exactMatch:].cold.69
+ -[CBDevice isEqualToDevice:exactMatch:].cold.7
+ -[CBDevice isEqualToDevice:exactMatch:].cold.70
+ -[CBDevice isEqualToDevice:exactMatch:].cold.71
+ -[CBDevice isEqualToDevice:exactMatch:].cold.72
+ -[CBDevice isEqualToDevice:exactMatch:].cold.73
+ -[CBDevice isEqualToDevice:exactMatch:].cold.74
+ -[CBDevice isEqualToDevice:exactMatch:].cold.75
+ -[CBDevice isEqualToDevice:exactMatch:].cold.76
+ -[CBDevice isEqualToDevice:exactMatch:].cold.77
+ -[CBDevice isEqualToDevice:exactMatch:].cold.78
+ -[CBDevice isEqualToDevice:exactMatch:].cold.79
+ -[CBDevice isEqualToDevice:exactMatch:].cold.8
+ -[CBDevice isEqualToDevice:exactMatch:].cold.80
+ -[CBDevice isEqualToDevice:exactMatch:].cold.81
+ -[CBDevice isEqualToDevice:exactMatch:].cold.82
+ -[CBDevice isEqualToDevice:exactMatch:].cold.83
+ -[CBDevice isEqualToDevice:exactMatch:].cold.84
+ -[CBDevice isEqualToDevice:exactMatch:].cold.85
+ -[CBDevice isEqualToDevice:exactMatch:].cold.86
+ -[CBDevice isEqualToDevice:exactMatch:].cold.87
+ -[CBDevice isEqualToDevice:exactMatch:].cold.88
+ -[CBDevice isEqualToDevice:exactMatch:].cold.89
+ -[CBDevice isEqualToDevice:exactMatch:].cold.9
+ -[CBDevice isEqualToDevice:exactMatch:].cold.90
+ -[CBDevice isEqualToDevice:exactMatch:].cold.91
+ -[CBDevice isEqualToDevice:exactMatch:].cold.92
+ -[CBDevice isEqualToDevice:exactMatch:].cold.93
+ -[CBDevice isEqualToDevice:exactMatch:].cold.94
+ -[CBDevice isEqualToDevice:exactMatch:].cold.95
+ -[CBDevice isEqualToDevice:exactMatch:].cold.96
+ -[CBDevice isEqualToDevice:exactMatch:].cold.97
+ -[CBDevice isEqualToDevice:exactMatch:].cold.98
+ -[CBDevice isEqualToDevice:exactMatch:].cold.99
+ -[CBDevice isLowerThanAgeLimit:compareTimestamp:]
+ -[CBDevice isLowerThanAgeLimit:compareTimestamp:].cold.1
+ -[CBDevice nearbyInfoV2NearbyFaceTimeData]
+ -[CBDevice nearbyInfoV2NearbyFaceTimeEncryptedData]
+ -[CBDevice setAirplayTargetIPv6:]
+ -[CBDevice setNearbyInfoV2InvitationRouteType:]
+ -[CBDevice setNearbyInfoV2InvitationTypes:]
+ -[CBDevice setNearbyInfoV2NearbyFaceTimeEncryptedData:]
+ -[CBDevice setObjectSetupBatteryPerformance:]
+ -[CBDevice setObjectSetupBatteryState:]
+ -[CBDevice setObjectSetupColorCode:]
+ -[CBDevice setObjectSetupFlags:]
+ -[CBDevice setObjectSetupFontCode:]
+ -[CBDevice setObjectSetupMessage:]
+ -[CBDevice updateWithCBPowerSource:]
+ -[CBDeviceSettings powerSourceMock]
+ -[CBDeviceSettings setPowerSourceMock:]
+ -[CBDiscovery bufferedAdvConfigsForAOP]
+ -[CBDiscovery devicesMatchingPropertiesOn:exactMatch:completionHandler:]
+ -[CBDiscovery injectAOPBufAdv:]
+ -[CBDiscovery setBufferedAdvConfigsForAOP:]
+ -[CBDiscovery setBufferedConfigsForAOP:]
+ -[CBHIDPerformanceMonitor _calculatePercentile:percentile:]
+ -[CBHIDPerformanceMonitor _calculatePercentile:percentile:].cold.1
+ -[CBHIDPerformanceMonitor _showSummaryResult:isFinal:packetMics:statsDelta:deltaMics:countActual:]
+ -[CBHIDPerformanceMonitor excessiveMs]
+ -[CBHIDPerformanceMonitor setExcessiveMs:]
+ -[CBHIDPerformanceMonitor setSlideWindowSec:]
+ -[CBHIDPerformanceMonitor slideWindowSec]
+ -[CBHIDPerformanceSummary P50Max]
+ -[CBHIDPerformanceSummary P50]
+ -[CBHIDPerformanceSummary P90Max]
+ -[CBHIDPerformanceSummary P90]
+ -[CBHIDPerformanceSummary P95Max]
+ -[CBHIDPerformanceSummary P95]
+ -[CBHIDPerformanceSummary P99Max]
+ -[CBHIDPerformanceSummary P99]
+ -[CBHIDPerformanceSummary finalSummary]
+ -[CBHIDPerformanceSummary setFinalSummary:]
+ -[CBHIDPerformanceSummary setP50:]
+ -[CBHIDPerformanceSummary setP50Max:]
+ -[CBHIDPerformanceSummary setP90:]
+ -[CBHIDPerformanceSummary setP90Max:]
+ -[CBHIDPerformanceSummary setP95:]
+ -[CBHIDPerformanceSummary setP95Max:]
+ -[CBHIDPerformanceSummary setP99:]
+ -[CBHIDPerformanceSummary setP99Max:]
+ -[CBISOReadRequest .cxx_destruct]
+ -[CBISOReadRequest completionHandler]
+ -[CBISOReadRequest data]
+ -[CBISOReadRequest error]
+ -[CBISOReadRequest missedReads]
+ -[CBISOReadRequest setCompletionHandler:]
+ -[CBISOReadRequest setData:]
+ -[CBISOReadRequest setError:]
+ -[CBISOReadRequest setMissedReads:]
+ -[CBISOWriteRequest .cxx_destruct]
+ -[CBISOWriteRequest completionHandler]
+ -[CBISOWriteRequest data]
+ -[CBISOWriteRequest error]
+ -[CBISOWriteRequest setCompletionHandler:]
+ -[CBISOWriteRequest setData:]
+ -[CBISOWriteRequest setError:]
+ -[CBISOWriteRequest setStream:]
+ -[CBISOWriteRequest stream]
+ -[CBLEAudioHearingAidPreset .cxx_destruct]
+ -[CBLEAudioHearingAidPreset initWithValues:withProperty:withName:]
+ -[CBLEAudioHearingAidPreset isAvailable]
+ -[CBLEAudioHearingAidPreset isWritable]
+ -[CBLEAudioHearingAidPreset presetIndex]
+ -[CBLEAudioHearingAidPreset presetName]
+ -[CBLEAudioHearingAidUpdateEvent .cxx_destruct]
+ -[CBLEAudioHearingAidUpdateEvent activePreset]
+ -[CBLEAudioHearingAidUpdateEvent initWithEventType:]
+ -[CBLEAudioHearingAidUpdateEvent initWithValue:withValue:]
+ -[CBLEAudioHearingAidUpdateEvent presetResults]
+ -[CBLEAudioHearingAidUpdateEvent setActivePreset:]
+ -[CBLEAudioHearingAidUpdateEvent setPresetResults:]
+ -[CBLEAudioPeripheralUpdateEvent .cxx_destruct]
+ -[CBLEAudioPeripheralUpdateEvent error]
+ -[CBLEAudioPeripheralUpdateEvent eventType]
+ -[CBLEAudioPeripheralUpdateEvent initWithError:withError:]
+ -[CBLEAudioPeripheralUpdateEvent initWithEventType:]
+ -[CBLEAudioPeripheralUpdateEvent initWithValue:withValue:]
+ -[CBLEAudioPeripheralUpdateEvent updatedValue]
+ -[CBLEAudioSessionEvent .cxx_destruct]
+ -[CBLEAudioSessionEvent error]
+ -[CBLEAudioSessionEvent eventType]
+ -[CBLEAudioSessionEvent initWithEventType:withError:]
+ -[CBLEAudioSessionEvent sessionInfo]
+ -[CBLEAudioSessionEvent setError:]
+ -[CBLEAudioSessionEvent setSessionInfo:]
+ -[CBLEAudioSessionEvent setUpdatedValue:]
+ -[CBLEAudioSessionEvent updatedValue]
+ -[CBLEAudioSessionInfo .cxx_destruct]
+ -[CBLEAudioSessionInfo audioSessionIdentifier]
+ -[CBLEAudioSessionInfo connectedIdentifiers]
+ -[CBLEAudioSessionInfo coordinatedSetInfo]
+ -[CBLEAudioSessionInfo copyWithZone:]
+ -[CBLEAudioSessionInfo initWithInfo:withSessionId:withState:withCoordIds:withLocation:]
+ -[CBLEAudioSessionInfo initWithSession:]
+ -[CBLEAudioSessionInfo locations]
+ -[CBLEAudioSessionInfo retrieveConnectedLEAudioPeripheralIdentifiers]
+ -[CBLEAudioSessionInfo sessionState]
+ -[CBPeripheral deviceType]
+ -[CBPeripheral dynamicPresets]
+ -[CBPeripheral getRangingTones:]
+ -[CBPeripheral getRangingTones:].cold.1
+ -[CBPeripheral handleCSProcedureEventForDeviceMsg:]
+ -[CBPeripheral handleLEAudioActivePresetUpdated:]
+ -[CBPeripheral handleLEAudioActivePresetUpdated:].cold.1
+ -[CBPeripheral handleLEAudioConnected:]
+ -[CBPeripheral handleLEAudioConnected:].cold.1
+ -[CBPeripheral handleLEAudioEvents:]
+ -[CBPeripheral handleLEAudioEvents:].cold.1
+ -[CBPeripheral handleLEAudioEvents:].cold.2
+ -[CBPeripheral handleLEAudioEvents:].cold.3
+ -[CBPeripheral handleLEAudioHearingAidFeaturesUpdated:]
+ -[CBPeripheral handleLEAudioHearingAidFeaturesUpdated:].cold.1
+ -[CBPeripheral handleLEAudioMicrophoneGainUpdated:]
+ -[CBPeripheral handleLEAudioMicrophoneGainUpdated:].cold.1
+ -[CBPeripheral handleLEAudioMicrophoneMuteUpdated:]
+ -[CBPeripheral handleLEAudioMicrophoneMuteUpdated:].cold.1
+ -[CBPeripheral handleLEAudioMsg:args:]
+ -[CBPeripheral handleLEAudioMsg:args:].cold.1
+ -[CBPeripheral handleLEAudioMsg:args:].cold.2
+ -[CBPeripheral handleLEAudioPresetNameUpdated:]
+ -[CBPeripheral handleLEAudioPresetNameUpdated:].cold.1
+ -[CBPeripheral handleLEAudioPresetUpdated:]
+ -[CBPeripheral handleLEAudioPresetUpdated:].cold.1
+ -[CBPeripheral handleLEAudioVolumeGainUpdated:]
+ -[CBPeripheral handleLEAudioVolumeGainUpdated:].cold.1
+ -[CBPeripheral handleLEAudioVolumeMuteUpdated:]
+ -[CBPeripheral handleLEAudioVolumeMuteUpdated:].cold.1
+ -[CBPeripheral handleLEAudioVolumeOffsetUpdated:]
+ -[CBPeripheral handleLEAudioVolumeOffsetUpdated:].cold.1
+ -[CBPeripheral handleLEAudioVolumeUpdated:]
+ -[CBPeripheral handleLEAudioVolumeUpdated:].cold.1
+ -[CBPeripheral hearingAidType]
+ -[CBPeripheral independentPresets]
+ -[CBPeripheral isConnectedToSystem].408
+ -[CBPeripheral location]
+ -[CBPeripheral presetSyncSupported]
+ -[CBPeripheral readPresets:]
+ -[CBPeripheral sendLEAudioMsg:args:completion:]
+ -[CBPeripheral setActivePreset:OptionalPresetIndex:withResponse:]
+ -[CBPeripheral setLEAudioDeviceType:]
+ -[CBPeripheral setLEAudioLocation:]
+ -[CBPeripheral setMicrophoneMute:withResponse:]
+ -[CBPeripheral setUpdateHandler:]
+ -[CBPeripheral setVolume:withResponse:]
+ -[CBPeripheral setVolumeMute:withResponse:]
+ -[CBPeripheral setVolumeOffSet:withOffSetValue:withResponse:]
+ -[CBPeripheral updateHandler]
+ -[CBPeripheral writablePresets]
+ -[CBPeripheral writeMicrophoneAudioInput:forAudioInputType:withOptionalGain:withResponse:]
+ -[CBPeripheral writePresetName:withName:withResponse:]
+ -[CBPeripheral writeVolumeAudioInput:forAudioInputType:withOptionalGain:withResponse:]
+ -[CBPeripheralManager cisPeripheralConnectEvent]
+ -[CBPeripheralManager cisPeripheralDisconnectEvent]
+ -[CBPeripheralManager disconnectCISPeripheral:]
+ -[CBPeripheralManager handleConnectCISPeripheralComplete:]
+ -[CBPeripheralManager handleDisconnectCISPeripheralComplete:]
+ -[CBPeripheralManager initCISPeripheral:completion:]
+ -[CBPeripheralManager respondToCISConnectionRequest:]
+ -[CBPeripheralManager setCisPeripheralConnectEvent:]
+ -[CBPeripheralManager setCisPeripheralDisconnectEvent:]
+ -[CBPowerSource .cxx_destruct]
+ -[CBPowerSource _setPartName]
+ -[CBPowerSource _updateAggregateWithComponent:]
+ -[CBPowerSource accessoryCategory]
+ -[CBPowerSource accessoryID]
+ -[CBPowerSource appearanceValue]
+ -[CBPowerSource batteryInfo]
+ -[CBPowerSource changeFlags]
+ -[CBPowerSource combinedPublish]
+ -[CBPowerSource componentWithPartID:]
+ -[CBPowerSource components]
+ -[CBPowerSource copyWithZone:]
+ -[CBPowerSource dealloc]
+ -[CBPowerSource description]
+ -[CBPowerSource deviceType]
+ -[CBPowerSource dictionaryRepresentation]
+ -[CBPowerSource dictionaryRepresentation].cold.1
+ -[CBPowerSource encodeWithCoder:]
+ -[CBPowerSource encodeWithXPCObject:]
+ -[CBPowerSource familyCode]
+ -[CBPowerSource groupID]
+ -[CBPowerSource hasAllComponents]
+ -[CBPowerSource initWithCoder:]
+ -[CBPowerSource initWithDictionary:error:]
+ -[CBPowerSource initWithPowerSourceDetails:internalFlags:]
+ -[CBPowerSource initWithXPCObject:error:]
+ -[CBPowerSource init]
+ -[CBPowerSource internalFlags]
+ -[CBPowerSource invalidateComponentWithPartID:]
+ -[CBPowerSource invalidate]
+ -[CBPowerSource isAggregateComponent]
+ -[CBPowerSource isAppleDevice]
+ -[CBPowerSource lowWarnLevel]
+ -[CBPowerSource maxCapacity]
+ -[CBPowerSource name]
+ -[CBPowerSource partID]
+ -[CBPowerSource partName]
+ -[CBPowerSource present]
+ -[CBPowerSource productID]
+ -[CBPowerSource publish]
+ -[CBPowerSource releaseSource]
+ -[CBPowerSource removeBatteryInfo]
+ -[CBPowerSource removeFlags]
+ -[CBPowerSource setAccessoryCategory:]
+ -[CBPowerSource setAccessoryID:]
+ -[CBPowerSource setAppearanceValue:]
+ -[CBPowerSource setBatteryInfo:]
+ -[CBPowerSource setChangeFlags:]
+ -[CBPowerSource setDeviceType:]
+ -[CBPowerSource setFamilyCode:]
+ -[CBPowerSource setGroupID:]
+ -[CBPowerSource setInternalFlags:]
+ -[CBPowerSource setLowWarnLevel:]
+ -[CBPowerSource setMaxCapacity:]
+ -[CBPowerSource setName:]
+ -[CBPowerSource setPartID:]
+ -[CBPowerSource setPartName:]
+ -[CBPowerSource setPresent:]
+ -[CBPowerSource setProductID:]
+ -[CBPowerSource setSourceID:]
+ -[CBPowerSource setTemperature:]
+ -[CBPowerSource setTransportType:]
+ -[CBPowerSource setType:]
+ -[CBPowerSource setVendorID:]
+ -[CBPowerSource setVendorIDSource:]
+ -[CBPowerSource sourceID]
+ -[CBPowerSource temperature]
+ -[CBPowerSource transportType]
+ -[CBPowerSource type]
+ -[CBPowerSource updatePartID]
+ -[CBPowerSource updateWithCBPowerSource:]
+ -[CBPowerSource updateWithCBPowerSource:].cold.1
+ -[CBPowerSource vendorIDSource]
+ -[CBPowerSource vendorID]
+ -[CBUserController userNotificationEvent:completion:]
+ -[CBUserNotificationRequest .cxx_destruct]
+ -[CBUserNotificationRequest copyWithZone:]
+ -[CBUserNotificationRequest description]
+ -[CBUserNotificationRequest device]
+ -[CBUserNotificationRequest dictionaryRepresentation]
+ -[CBUserNotificationRequest encodeWithCoder:]
+ -[CBUserNotificationRequest encodeWithXPCObject:]
+ -[CBUserNotificationRequest event]
+ -[CBUserNotificationRequest initWithCoder:]
+ -[CBUserNotificationRequest initWithDictionary:error:]
+ -[CBUserNotificationRequest initWithXPCObject:error:]
+ -[CBUserNotificationRequest setDevice:]
+ -[CBUserNotificationRequest setEvent:]
+ -[CBWPDaemonAdvertisingData .cxx_destruct]
+ -[CBWPDaemonAdvertisingData advDataPerType]
+ -[CBWPDaemonAdvertisingData advInstanceType]
+ -[CBWPDaemonAdvertisingData advInterval]
+ -[CBWPDaemonAdvertisingData copyWithZone:]
+ -[CBWPDaemonAdvertisingData descriptionWithLevel:]
+ -[CBWPDaemonAdvertisingData description]
+ -[CBWPDaemonAdvertisingData enableAdvertisingWithPowerAssertion]
+ -[CBWPDaemonAdvertisingData enableEPAForAdvertisement]
+ -[CBWPDaemonAdvertisingData enableObjectLocatorResponseOnAdvertisingInstance]
+ -[CBWPDaemonAdvertisingData isEqual:]
+ -[CBWPDaemonAdvertisingData listOfClients]
+ -[CBWPDaemonAdvertisingData mfgData]
+ -[CBWPDaemonAdvertisingData setAdvDataPerType:]
+ -[CBWPDaemonAdvertisingData setAdvInstanceType:]
+ -[CBWPDaemonAdvertisingData setAdvInterval:]
+ -[CBWPDaemonAdvertisingData setEnableAdvertisingWithPowerAssertion:]
+ -[CBWPDaemonAdvertisingData setEnableEPAForAdvertisement:]
+ -[CBWPDaemonAdvertisingData setEnableObjectLocatorResponseOnAdvertisingInstance:]
+ -[CBWPDaemonAdvertisingData setListOfClients:]
+ -[CBWPDaemonAdvertisingData setMfgData:]
+ -[CBWPDaemonAdvertisingData setStopOnAdvertisingAddressChange:]
+ -[CBWPDaemonAdvertisingData setWiProxUpdateTimestamp:]
+ -[CBWPDaemonAdvertisingData stopOnAdvertisingAddressChange]
+ -[CBWPDaemonAdvertisingData wiProxUpdateTimestamp]
+ -[CBXpcConnection didReceiveForwardedDelegateCallbackMessage:].cold.4
+ -[CBXpcConnection didReceiveForwardedMessage:].cold.4
+ -[CBXpcConnection forwardWhbMsg:args:cnx:].cold.4
+ GCC_except_table100
+ GCC_except_table133
+ GCC_except_table146
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table391
+ GCC_except_table405
+ GCC_except_table41
+ GCC_except_table456
+ GCC_except_table49
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table74
+ GCC_except_table82
+ _CBAdvertisementDataAppleAdvDataPerType
+ _CBCentralManagerControllerBTCLockExceptionStatus
+ _CBCentralManagerControllerCEOffset
+ _CBCentralManagerControllerConnectionInterval
+ _CBCentralManagerControllerConnectionIntervalMicroSec
+ _CBCentralManagerControllerHostTime
+ _CBCentralManagerScanOptionUsecaseOptions
+ _CBConnectPeripheralOptionLESynchronizationEvents
+ _CBDevicePlacementToString
+ _CBDeviceTypeFromAccessoryCategory
+ _CBDeviceTypeToAccessoryCategory
+ _CBGetRangeOptionRunProcedure
+ _CBHeySiriDeviceClassToString
+ _CBHostVersion
+ _CBManagerSessionIsExtension
+ _CBNearbyInfoV2InvitationRouteTypeToString
+ _CBNearbyStatusTypeToString
+ _CBPowerSourceAccessoryCategoryFromString
+ _CBPowerSourceAccessoryCategoryToString
+ _CBPowerSourcePartIDFromString
+ _CBPowerSourcePartIDToString
+ _CBProximityPairingSubTypeToString
+ _CBUUIDAccessoryAttributesCharacteristicString
+ _CBUUIDAccessoryTypeCharacteristicString
+ _CBUUIDActivePresetIndexCharacteristicString
+ _CBUUIDAppleSpatialHIDServiceString
+ _CBUUIDAppleSpatialHIDUniformTypeIdentifierCharacteristicString
+ _CBUUIDAudioInputControlPointCharacteristicString
+ _CBUUIDAudioInputControlServiceString
+ _CBUUIDAudioInputDescriptionCharacteristicString
+ _CBUUIDAudioInputStateCharacteristicString
+ _CBUUIDAudioInputStatusCharacteristicString
+ _CBUUIDAudioInputTypeCharacteristicString
+ _CBUUIDAudioLocationCharacteristicString
+ _CBUUIDAudioOutputDescriptionCharacteristicString
+ _CBUUIDBatteryLevelLeftCharacteristicString
+ _CBUUIDBatteryLevelMainCharacteristicString
+ _CBUUIDBatteryLevelRightCharacteristicString
+ _CBUUIDBatteryLevelStatusCharacteristicString
+ _CBUUIDBearerListCurrentCallsCharacteristicString
+ _CBUUIDBearerProviderNameCharacteristicString
+ _CBUUIDBearerSignalStrengthCharacteristicString
+ _CBUUIDBearerSignalStrengthReportingIntervalCharacteristicString
+ _CBUUIDBearerTechnologyCharacteristicString
+ _CBUUIDBearerUciCharacteristicString
+ _CBUUIDBearerUriSchemesSupportedListCharacteristicString
+ _CBUUIDCallControlPointCharacteristicString
+ _CBUUIDCallControlPointOptionalOpcodesCharacteristicString
+ _CBUUIDCallFriendlyNameCharacteristicString
+ _CBUUIDCallStateCharacteristicString
+ _CBUUIDCommandCharacteristicString
+ _CBUUIDContentControlIdCharacteristicString
+ _CBUUIDCoordinatedSetIdServiceString
+ _CBUUIDCoordinatedSetSizeCharacteristicString
+ _CBUUIDCurrentGroupObjectIDCharacteristicString
+ _CBUUIDCurrentTrackObjectIDCharacteristicString
+ _CBUUIDCurrentTrackSegmentsObjectIDCharacteristicString
+ _CBUUIDGainSettingPropertiesCharacteristicString
+ _CBUUIDGenericMediaControlServiceString
+ _CBUUIDGenericTelephoneBearerServiceString
+ _CBUUIDHearingAccessServiceString
+ _CBUUIDHearingAidFeaturesCharacteristicString
+ _CBUUIDHearingAidPresetControlPointCharacteristicString
+ _CBUUIDHostSelectedVersionCharacteristicString
+ _CBUUIDIncomingCallCharacteristicString
+ _CBUUIDIncomingCallTargetBearerUriCharacteristicString
+ _CBUUIDMFiServiceString
+ _CBUUIDMediaControlPointCharacteristicString
+ _CBUUIDMediaControlPointOpcodesSupportedCharacteristicString
+ _CBUUIDMediaControlServiceString
+ _CBUUIDMediaPlayerIconObjectIDCharacteristicString
+ _CBUUIDMediaPlayerIconURLCharacteristicString
+ _CBUUIDMediaPlayerNameCharacteristicString
+ _CBUUIDMediaStateCharacteristicString
+ _CBUUIDMicrophoneControlServiceString
+ _CBUUIDMuteCharacteristicString
+ _CBUUIDNextTrackObjectIDCharacteristicString
+ _CBUUIDParentGroupObjectIDCharacteristicString
+ _CBUUIDPlaybackSpeedCharacteristicString
+ _CBUUIDPlayingOrderCharacteristicString
+ _CBUUIDPlayingOrdersSupportedCharacteristicString
+ _CBUUIDProtocolStringCharacteristicString
+ _CBUUIDSearchControlPointCharacteristicString
+ _CBUUIDSearchResultsObjectIDCharacteristicString
+ _CBUUIDSecureSensorAudioCharacteristicString
+ _CBUUIDSecureSensorConfigurationCharacteristicString
+ _CBUUIDSecureSensorDebugCharacteristicString
+ _CBUUIDSecureSensorPairingCharacteristicString
+ _CBUUIDSecureSensorServiceString
+ _CBUUIDSeekingSpeedCharacteristicString
+ _CBUUIDSetIdResolvingKeyCharacteristicString
+ _CBUUIDSetMemberLockCharacteristicString
+ _CBUUIDSetMemberRankCharacteristicString
+ _CBUUIDSpatialHIDVersionsCharacteristicString
+ _CBUUIDStatusFlagsCharacteristicString
+ _CBUUIDTMAPRoleCharacteristicString
+ _CBUUIDTeamIDCharacteristicString
+ _CBUUIDTelephoneBearerServiceString
+ _CBUUIDTelephonyMediaAudioServiceString
+ _CBUUIDTerminationReasonCharacteristicString
+ _CBUUIDTrackChangedCharacteristicString
+ _CBUUIDTrackDurationCharacteristicString
+ _CBUUIDTrackPositionCharacteristicString
+ _CBUUIDTrackTitleCharacteristicString
+ _CBUUIDVolumeControlPointCharacteristicString
+ _CBUUIDVolumeControlServiceString
+ _CBUUIDVolumeFlagsCharacteristicString
+ _CBUUIDVolumeOffsetControlPointCharacteristicString
+ _CBUUIDVolumeOffsetControlServiceString
+ _CBUUIDVolumeOffsetStateCharacteristicString
+ _CBUUIDVolumeStateCharacteristicString
+ _CBVendorIDToString
+ _CFArrayGetTypeID
+ _CFDictionaryGetTypeID
+ _IOPSCreatePowerSource
+ _IOPSReleasePowerSource
+ _IOPSSetPowerSourceDetails
+ _NSDictionaryGetNSNumber
+ _OBJC_CLASS_$_CBCoordinatedMemberInfo
+ _OBJC_CLASS_$_CBCoordinatedSetInfo
+ _OBJC_CLASS_$_CBISOReadRequest
+ _OBJC_CLASS_$_CBISOWriteRequest
+ _OBJC_CLASS_$_CBLEAudioHearingAidPreset
+ _OBJC_CLASS_$_CBLEAudioHearingAidUpdateEvent
+ _OBJC_CLASS_$_CBLEAudioPeripheralUpdateEvent
+ _OBJC_CLASS_$_CBLEAudioSessionEvent
+ _OBJC_CLASS_$_CBLEAudioSessionInfo
+ _OBJC_CLASS_$_CBPowerSource
+ _OBJC_CLASS_$_CBUserNotificationRequest
+ _OBJC_CLASS_$_CBWPDaemonAdvertisingData
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_IVAR_$_CBAdvertiser._nearbyInfoV2NearbyFaceTimeData
+ _OBJC_IVAR_$_CBAdvertiser._proximityServicePayload
+ _OBJC_IVAR_$_CBAdvertiser._proximityServiceSubType
+ _OBJC_IVAR_$_CBAdvertiser._randomData
+ _OBJC_IVAR_$_CBApplePayloadTypeInfo._maxAge
+ _OBJC_IVAR_$_CBCentralManager._audioSessions
+ _OBJC_IVAR_$_CBCentralManager._cisConnectEvent
+ _OBJC_IVAR_$_CBCentralManager._cisDisconnectEvent
+ _OBJC_IVAR_$_CBCentralManager._leAudioDevice
+ _OBJC_IVAR_$_CBCentralManager._leAudioEventHandler
+ _OBJC_IVAR_$_CBCentralManager._leAudioXpcConnection
+ _OBJC_IVAR_$_CBCentralManager._removeCIGCompletion
+ _OBJC_IVAR_$_CBCentralManager._setupCIGCompletion
+ _OBJC_IVAR_$_CBCentralManager._validLeAudioXpcCalled
+ _OBJC_IVAR_$_CBCharacteristic._addExtendedProperties
+ _OBJC_IVAR_$_CBControllerSettings._gameControllerAutoSwitchMode
+ _OBJC_IVAR_$_CBControllerSettings._gameControllerUSBBluetoothPairing
+ _OBJC_IVAR_$_CBCoordinatedMemberInfo._memberRank
+ _OBJC_IVAR_$_CBCoordinatedSetInfo._connectedIdentifiers
+ _OBJC_IVAR_$_CBCoordinatedSetInfo._setName
+ _OBJC_IVAR_$_CBCoordinatedSetInfo._setSize
+ _OBJC_IVAR_$_CBDevice._nearbyInfoV2NearbyFaceTimeData
+ _OBJC_IVAR_$_CBDevice._nearbyInfoV2NearbyFaceTimeEncryptedData
+ _OBJC_IVAR_$_CBDeviceSettings._powerSourceMock
+ _OBJC_IVAR_$_CBDiscovery._bufferedAdvConfigsForAOP
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._excessiveMs
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._intrmPacketDeltaMics
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._slideWindowSec
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._slidingWindowDate
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketCountInterim
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketDeltaMics
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketExcessiveInterval
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketMicsStartInterim
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketP50Max
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketP90Max
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketP95Max
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketP99Max
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P50
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P50Max
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P90
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P90Max
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P95
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P95Max
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P99
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P99Max
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._finalSummary
+ _OBJC_IVAR_$_CBISOReadRequest._completionHandler
+ _OBJC_IVAR_$_CBISOReadRequest._data
+ _OBJC_IVAR_$_CBISOReadRequest._error
+ _OBJC_IVAR_$_CBISOReadRequest._missedReads
+ _OBJC_IVAR_$_CBISOWriteRequest._completionHandler
+ _OBJC_IVAR_$_CBISOWriteRequest._data
+ _OBJC_IVAR_$_CBISOWriteRequest._error
+ _OBJC_IVAR_$_CBISOWriteRequest._stream
+ _OBJC_IVAR_$_CBLEAudioHearingAidPreset._isAvailable
+ _OBJC_IVAR_$_CBLEAudioHearingAidPreset._isWritable
+ _OBJC_IVAR_$_CBLEAudioHearingAidPreset._presetIndex
+ _OBJC_IVAR_$_CBLEAudioHearingAidPreset._presetName
+ _OBJC_IVAR_$_CBLEAudioHearingAidUpdateEvent._activePreset
+ _OBJC_IVAR_$_CBLEAudioHearingAidUpdateEvent._presetResults
+ _OBJC_IVAR_$_CBLEAudioPeripheralUpdateEvent._error
+ _OBJC_IVAR_$_CBLEAudioPeripheralUpdateEvent._eventType
+ _OBJC_IVAR_$_CBLEAudioPeripheralUpdateEvent._updatedValue
+ _OBJC_IVAR_$_CBLEAudioSessionEvent._error
+ _OBJC_IVAR_$_CBLEAudioSessionEvent._eventType
+ _OBJC_IVAR_$_CBLEAudioSessionEvent._sessionInfo
+ _OBJC_IVAR_$_CBLEAudioSessionEvent._updatedValue
+ _OBJC_IVAR_$_CBLEAudioSessionInfo._audioSessionIdentifier
+ _OBJC_IVAR_$_CBLEAudioSessionInfo._connectedIdentifiers
+ _OBJC_IVAR_$_CBLEAudioSessionInfo._coordinatedSetInfo
+ _OBJC_IVAR_$_CBLEAudioSessionInfo._locations
+ _OBJC_IVAR_$_CBLEAudioSessionInfo._sessionState
+ _OBJC_IVAR_$_CBPeripheral._deviceType
+ _OBJC_IVAR_$_CBPeripheral._dynamicPresets
+ _OBJC_IVAR_$_CBPeripheral._hearingAidType
+ _OBJC_IVAR_$_CBPeripheral._independentPresets
+ _OBJC_IVAR_$_CBPeripheral._location
+ _OBJC_IVAR_$_CBPeripheral._presetSyncSupported
+ _OBJC_IVAR_$_CBPeripheral._updateHandler
+ _OBJC_IVAR_$_CBPeripheral._writablePresets
+ _OBJC_IVAR_$_CBPeripheralManager._cisPeripheralConnectEvent
+ _OBJC_IVAR_$_CBPeripheralManager._cisPeripheralDisconnectEvent
+ _OBJC_IVAR_$_CBPowerSource._accessoryCategory
+ _OBJC_IVAR_$_CBPowerSource._accessoryID
+ _OBJC_IVAR_$_CBPowerSource._appearanceValue
+ _OBJC_IVAR_$_CBPowerSource._batteryInfo
+ _OBJC_IVAR_$_CBPowerSource._changeFlags
+ _OBJC_IVAR_$_CBPowerSource._componentMap
+ _OBJC_IVAR_$_CBPowerSource._deviceType
+ _OBJC_IVAR_$_CBPowerSource._familyCode
+ _OBJC_IVAR_$_CBPowerSource._groupID
+ _OBJC_IVAR_$_CBPowerSource._internalFlags
+ _OBJC_IVAR_$_CBPowerSource._lowWarnLevel
+ _OBJC_IVAR_$_CBPowerSource._maxCapacity
+ _OBJC_IVAR_$_CBPowerSource._name
+ _OBJC_IVAR_$_CBPowerSource._partID
+ _OBJC_IVAR_$_CBPowerSource._partName
+ _OBJC_IVAR_$_CBPowerSource._present
+ _OBJC_IVAR_$_CBPowerSource._productID
+ _OBJC_IVAR_$_CBPowerSource._psID
+ _OBJC_IVAR_$_CBPowerSource._sourceID
+ _OBJC_IVAR_$_CBPowerSource._temperature
+ _OBJC_IVAR_$_CBPowerSource._transportType
+ _OBJC_IVAR_$_CBPowerSource._type
+ _OBJC_IVAR_$_CBPowerSource._vendorID
+ _OBJC_IVAR_$_CBPowerSource._vendorIDSource
+ _OBJC_IVAR_$_CBUserNotificationRequest._device
+ _OBJC_IVAR_$_CBUserNotificationRequest._event
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._advDataPerType
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._advInstanceType
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._advInterval
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._enableAdvertisingWithPowerAssertion
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._enableEPAForAdvertisement
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._enableObjectLocatorResponseOnAdvertisingInstance
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._listOfClients
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._mfgData
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._stopOnAdvertisingAddressChange
+ _OBJC_IVAR_$_CBWPDaemonAdvertisingData._wiProxUpdateTimestamp
+ _OBJC_METACLASS_$_CBCoordinatedMemberInfo
+ _OBJC_METACLASS_$_CBCoordinatedSetInfo
+ _OBJC_METACLASS_$_CBISOReadRequest
+ _OBJC_METACLASS_$_CBISOWriteRequest
+ _OBJC_METACLASS_$_CBLEAudioHearingAidPreset
+ _OBJC_METACLASS_$_CBLEAudioHearingAidUpdateEvent
+ _OBJC_METACLASS_$_CBLEAudioPeripheralUpdateEvent
+ _OBJC_METACLASS_$_CBLEAudioSessionEvent
+ _OBJC_METACLASS_$_CBLEAudioSessionInfo
+ _OBJC_METACLASS_$_CBPowerSource
+ _OBJC_METACLASS_$_CBUserNotificationRequest
+ _OBJC_METACLASS_$_CBWPDaemonAdvertisingData
+ __OBJC_$_CLASS_METHODS_CBPowerSource
+ __OBJC_$_CLASS_METHODS_CBUserNotificationRequest
+ __OBJC_$_CLASS_PROP_LIST_CBPowerSource
+ __OBJC_$_CLASS_PROP_LIST_CBUserNotificationRequest
+ __OBJC_$_INSTANCE_METHODS_CBCoordinatedMemberInfo
+ __OBJC_$_INSTANCE_METHODS_CBCoordinatedSetInfo
+ __OBJC_$_INSTANCE_METHODS_CBISOReadRequest
+ __OBJC_$_INSTANCE_METHODS_CBISOWriteRequest
+ __OBJC_$_INSTANCE_METHODS_CBLEAudioHearingAidPreset
+ __OBJC_$_INSTANCE_METHODS_CBLEAudioHearingAidUpdateEvent
+ __OBJC_$_INSTANCE_METHODS_CBLEAudioPeripheralUpdateEvent
+ __OBJC_$_INSTANCE_METHODS_CBLEAudioSessionEvent
+ __OBJC_$_INSTANCE_METHODS_CBLEAudioSessionInfo
+ __OBJC_$_INSTANCE_METHODS_CBPowerSource
+ __OBJC_$_INSTANCE_METHODS_CBUserNotificationRequest
+ __OBJC_$_INSTANCE_METHODS_CBWPDaemonAdvertisingData
+ __OBJC_$_INSTANCE_VARIABLES_CBCoordinatedMemberInfo
+ __OBJC_$_INSTANCE_VARIABLES_CBCoordinatedSetInfo
+ __OBJC_$_INSTANCE_VARIABLES_CBISOReadRequest
+ __OBJC_$_INSTANCE_VARIABLES_CBISOWriteRequest
+ __OBJC_$_INSTANCE_VARIABLES_CBLEAudioHearingAidPreset
+ __OBJC_$_INSTANCE_VARIABLES_CBLEAudioHearingAidUpdateEvent
+ __OBJC_$_INSTANCE_VARIABLES_CBLEAudioPeripheralUpdateEvent
+ __OBJC_$_INSTANCE_VARIABLES_CBLEAudioSessionEvent
+ __OBJC_$_INSTANCE_VARIABLES_CBLEAudioSessionInfo
+ __OBJC_$_INSTANCE_VARIABLES_CBPowerSource
+ __OBJC_$_INSTANCE_VARIABLES_CBUserNotificationRequest
+ __OBJC_$_INSTANCE_VARIABLES_CBWPDaemonAdvertisingData
+ __OBJC_$_PROP_LIST_CBCoordinatedMemberInfo
+ __OBJC_$_PROP_LIST_CBCoordinatedSetInfo
+ __OBJC_$_PROP_LIST_CBISOReadRequest
+ __OBJC_$_PROP_LIST_CBISOWriteRequest
+ __OBJC_$_PROP_LIST_CBLEAudioHearingAidPreset
+ __OBJC_$_PROP_LIST_CBLEAudioHearingAidUpdateEvent
+ __OBJC_$_PROP_LIST_CBLEAudioPeripheralUpdateEvent
+ __OBJC_$_PROP_LIST_CBLEAudioSessionEvent
+ __OBJC_$_PROP_LIST_CBLEAudioSessionInfo
+ __OBJC_$_PROP_LIST_CBPowerSource
+ __OBJC_$_PROP_LIST_CBUserNotificationRequest
+ __OBJC_$_PROP_LIST_CBWPDaemonAdvertisingData
+ __OBJC_CLASS_PROTOCOLS_$_CBPowerSource
+ __OBJC_CLASS_PROTOCOLS_$_CBUserNotificationRequest
+ __OBJC_CLASS_PROTOCOLS_$_CBWPDaemonAdvertisingData
+ __OBJC_CLASS_RO_$_CBCoordinatedMemberInfo
+ __OBJC_CLASS_RO_$_CBCoordinatedSetInfo
+ __OBJC_CLASS_RO_$_CBISOReadRequest
+ __OBJC_CLASS_RO_$_CBISOWriteRequest
+ __OBJC_CLASS_RO_$_CBLEAudioHearingAidPreset
+ __OBJC_CLASS_RO_$_CBLEAudioHearingAidUpdateEvent
+ __OBJC_CLASS_RO_$_CBLEAudioPeripheralUpdateEvent
+ __OBJC_CLASS_RO_$_CBLEAudioSessionEvent
+ __OBJC_CLASS_RO_$_CBLEAudioSessionInfo
+ __OBJC_CLASS_RO_$_CBPowerSource
+ __OBJC_CLASS_RO_$_CBUserNotificationRequest
+ __OBJC_CLASS_RO_$_CBWPDaemonAdvertisingData
+ __OBJC_METACLASS_RO_$_CBCoordinatedMemberInfo
+ __OBJC_METACLASS_RO_$_CBCoordinatedSetInfo
+ __OBJC_METACLASS_RO_$_CBISOReadRequest
+ __OBJC_METACLASS_RO_$_CBISOWriteRequest
+ __OBJC_METACLASS_RO_$_CBLEAudioHearingAidPreset
+ __OBJC_METACLASS_RO_$_CBLEAudioHearingAidUpdateEvent
+ __OBJC_METACLASS_RO_$_CBLEAudioPeripheralUpdateEvent
+ __OBJC_METACLASS_RO_$_CBLEAudioSessionEvent
+ __OBJC_METACLASS_RO_$_CBLEAudioSessionInfo
+ __OBJC_METACLASS_RO_$_CBPowerSource
+ __OBJC_METACLASS_RO_$_CBUserNotificationRequest
+ __OBJC_METACLASS_RO_$_CBWPDaemonAdvertisingData
+ ___33+[CBManager preflightCheckForTCC]_block_invoke.cold.1
+ ___35-[CBCentralManager startLEAudioXPC]_block_invoke
+ ___35-[CBDiscovery _activateDirectStart]_block_invoke.174
+ ___35-[CBDiscovery _activateDirectStart]_block_invoke_2.177
+ ___36-[CBDevice updateWithCBPowerSource:]_block_invoke
+ ___38-[CBDevice _matchingFlags:exactMatch:]_block_invoke
+ ___38-[CBXpcConnection setWhbReplyHandler:]_block_invoke.cold.4
+ ___39-[CBCentralManager createXPCForLEAudio]_block_invoke
+ ___40-[CBDiscovery setBufferedConfigsForAOP:]_block_invoke
+ ___41-[CBCentralManager handlePresetsUpdated:]_block_invoke
+ ___41-[CBCentralManager handlePresetsUpdated:]_block_invoke_2
+ ___41-[CBCentralManager handlePresetsUpdated:]_block_invoke_3
+ ___41-[CBCentralManager registerLEAudioClient]_block_invoke
+ ___41-[CBCentralManager registerLEAudioClient]_block_invoke.cold.1
+ ___41-[CBCentralManager registerLEAudioClient]_block_invoke.cold.2
+ ___43-[CBAdvertiser setProximityServicePayload:]_block_invoke
+ ___43-[CBAdvertiser setProximityServiceSubType:]_block_invoke
+ ___47-[CBCentralManager createSessionEvent:withMsg:]_block_invoke
+ ___49-[CBDevice isLowerThanAgeLimit:compareTimestamp:]_block_invoke
+ ___50-[CBAdvertiser setNearbyInfoV2NearbyFaceTimeData:]_block_invoke
+ ___51-[CBCentralManager sendLEAudioMsg:args:completion:]_block_invoke
+ ___53-[CBUserController userNotificationEvent:completion:]_block_invoke
+ ___53-[CBUserController userNotificationEvent:completion:]_block_invoke_2
+ ___53-[CBUserController userNotificationEvent:completion:]_block_invoke_3
+ ___53-[CBUserController userNotificationEvent:completion:]_block_invoke_4
+ ___58-[CBHIDPerformanceMonitor _packetLoggerProcessPacketData:]_block_invoke
+ ___58-[CBHIDPerformanceMonitor _packetLoggerProcessPacketData:]_block_invoke_2
+ ___59-[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:]_block_invoke.216
+ ___59-[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:]_block_invoke.216.cold.1
+ ___72-[CBDiscovery devicesMatchingPropertiesOn:exactMatch:completionHandler:]_block_invoke
+ ___72-[CBDiscovery devicesMatchingPropertiesOn:exactMatch:completionHandler:]_block_invoke_2
+ ___72-[CBDiscovery devicesMatchingPropertiesOn:exactMatch:completionHandler:]_block_invoke_2.cold.1
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
+ ___block_descriptor_41_e8_32r_e11_B24?0Q8Q16lr32l8
+ ___block_descriptor_41_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40r_e40_v32?0"NSNumber"8"CBPowerSource"16^B24ls32l8r40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.127
+ ___block_literal_global.137
+ ___block_literal_global.174
+ ___block_literal_global.278
+ ___block_literal_global.280
+ ___block_literal_global.282
+ ___block_literal_global.284
+ ___block_literal_global.423
+ ___block_literal_global.439
+ ___block_literal_global.457
+ ___block_literal_global.73
+ ___block_literal_global.777
+ ___block_literal_global.832
+ ___block_literal_global.91
+ _dispatch_after
+ _gLogCategory_CBDevice
+ _gLogCategory_CBPowerSource
+ _mach_continuous_time
+ _mach_timebase_info
+ _modf
+ _objc_msgSend$P50
+ _objc_msgSend$P50Max
+ _objc_msgSend$P90
+ _objc_msgSend$P90Max
+ _objc_msgSend$P95
+ _objc_msgSend$P95Max
+ _objc_msgSend$P99
+ _objc_msgSend$P99Max
+ _objc_msgSend$_calculatePercentile:percentile:
+ _objc_msgSend$_clearAirplaySourceFlags
+ _objc_msgSend$_clearAirplayTargetFlags
+ _objc_msgSend$_clearAirplayTargetIPv4
+ _objc_msgSend$_clearAirplayTargetIPv6
+ _objc_msgSend$_clearDeviceInfoKey:
+ _objc_msgSend$_clearDockKitAccessoryPayloadData
+ _objc_msgSend$_clearFidoPayloadData
+ _objc_msgSend$_clearGfpModelID
+ _objc_msgSend$_clearGfpPayloadData
+ _objc_msgSend$_clearHomeKitV1CompatibleVersion
+ _objc_msgSend$_clearHomeKitV1ConfigurationNumber
+ _objc_msgSend$_clearHomeKitV1Flags
+ _objc_msgSend$_clearHomeKitV1SetupHash
+ _objc_msgSend$_clearHomeKitV1StateNumber
+ _objc_msgSend$_clearHomeKitV2AuthTagData
+ _objc_msgSend$_clearHomeKitV2InstanceID
+ _objc_msgSend$_clearHomeKitV2StateNumber
+ _objc_msgSend$_clearHomeKitV2Value
+ _objc_msgSend$_clearMspAddressData
+ _objc_msgSend$_clearMspDeviceClass
+ _objc_msgSend$_clearMspDisplayName
+ _objc_msgSend$_clearMspSubScenario
+ _objc_msgSend$_clearNearbyActionAuthTag
+ _objc_msgSend$_clearNearbyActionDeviceClass
+ _objc_msgSend$_clearNearbyActionFlags
+ _objc_msgSend$_clearNearbyActionType
+ _objc_msgSend$_clearNearbyActionV2Flags
+ _objc_msgSend$_clearNearbyActionV2Type
+ _objc_msgSend$_clearObjectSetupFlags
+ _objc_msgSend$_clearObjectSetupFontCode
+ _objc_msgSend$_clearObjectSetupMessage
+ _objc_msgSend$_clearProximityServiceFlags
+ _objc_msgSend$_clearProximityServiceMeasuredPower
+ _objc_msgSend$_clearProximityServicePSM
+ _objc_msgSend$_clearProximityServiceSetupHash
+ _objc_msgSend$_clearProximityServiceSubType
+ _objc_msgSend$_clearProximityServiceVersion
+ _objc_msgSend$_clearSpatialInteractionConfigFlags
+ _objc_msgSend$_clearSpatialInteractionFlags
+ _objc_msgSend$_clearSpatialInteractionIdentifiers
+ _objc_msgSend$_clearSpatialInteractionPeerID
+ _objc_msgSend$_clearSpatialInteractionPresenceConfigData
+ _objc_msgSend$_clearSpatialInteractionTokenData
+ _objc_msgSend$_clearSpatialInteractionUWBConfigData
+ _objc_msgSend$_clearSpatialInteractionUserInfo
+ _objc_msgSend$_handleLEAudioXpcEvents:
+ _objc_msgSend$_matchingFlags:exactMatch:
+ _objc_msgSend$_scanForPeripheralsWithServices:options:completion:
+ _objc_msgSend$_setPartName
+ _objc_msgSend$_showSummaryResult:isFinal:packetMics:statsDelta:deltaMics:countActual:
+ _objc_msgSend$_updateAggregateWithComponent:
+ _objc_msgSend$accessoryCategory
+ _objc_msgSend$accessoryID
+ _objc_msgSend$addExtendedProperties
+ _objc_msgSend$advDataPerType
+ _objc_msgSend$advInstanceType
+ _objc_msgSend$advInterval
+ _objc_msgSend$airplayTargetIPv6
+ _objc_msgSend$audioSessionIdentifier
+ _objc_msgSend$batteryInfo
+ _objc_msgSend$bufferedAdvConfigsForAOP
+ _objc_msgSend$bundleRecordForCurrentProcess
+ _objc_msgSend$centralManager:didUpdateSynchronizationEventForPeripheral:results:
+ _objc_msgSend$changeFlags
+ _objc_msgSend$checkIfExtension
+ _objc_msgSend$combinedPublish
+ _objc_msgSend$compare:
+ _objc_msgSend$componentWithPartID:
+ _objc_msgSend$components
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$createSessionEvent:withMsg:
+ _objc_msgSend$createXPCForLEAudio
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$enableAdvertisingWithPowerAssertion
+ _objc_msgSend$enableEPAForAdvertisement
+ _objc_msgSend$enableObjectLocatorResponseOnAdvertisingInstance
+ _objc_msgSend$groupID
+ _objc_msgSend$handleActivePresetUpdated:
+ _objc_msgSend$handleConnectCISComplete:
+ _objc_msgSend$handleConnectCISPeripheralComplete:
+ _objc_msgSend$handleConnectLEAudioComplete:
+ _objc_msgSend$handleDisconnectCISComplete:
+ _objc_msgSend$handleDisconnectCISPeripheralComplete:
+ _objc_msgSend$handleFeaturesUpdated:
+ _objc_msgSend$handleLEAudioEvents:
+ _objc_msgSend$handleLEAudioMsg:
+ _objc_msgSend$handleLEAudioMsg:args:
+ _objc_msgSend$handleLEAudioSessionEvents:
+ _objc_msgSend$handleLEAudioXpcInterrupted
+ _objc_msgSend$handleLEAudioXpcInvalid
+ _objc_msgSend$handleMicrophoneGainUpdated:
+ _objc_msgSend$handleMicrophoneMuteUpdated:
+ _objc_msgSend$handlePresetNameUpdated:
+ _objc_msgSend$handlePresetsUpdated:
+ _objc_msgSend$handleRemoveCIGComplete:
+ _objc_msgSend$handleSessionCompleted:
+ _objc_msgSend$handleSessionMicrophoneGainUpdated:
+ _objc_msgSend$handleSessionMicrophoneMuteUpdated:
+ _objc_msgSend$handleSessionVolumeMuteUpdated:
+ _objc_msgSend$handleSessionVolumeOffsetUpdated:
+ _objc_msgSend$handleSessionVolumeUpdated:
+ _objc_msgSend$handleSetupCIGComplete:
+ _objc_msgSend$handleVolumeInputGainUpdated:
+ _objc_msgSend$handleVolumeMuteUpdated:
+ _objc_msgSend$handleVolumeOffsetUpdated:
+ _objc_msgSend$handleVolumeUpdated:
+ _objc_msgSend$hasAllComponents
+ _objc_msgSend$homeKitV1Category
+ _objc_msgSend$homeKitV1CompatibleVersion
+ _objc_msgSend$homeKitV1ConfigurationNumber
+ _objc_msgSend$homeKitV1DeviceIDData
+ _objc_msgSend$homeKitV1Flags
+ _objc_msgSend$homeKitV1SetupHash
+ _objc_msgSend$homeKitV1StateNumber
+ _objc_msgSend$homeKitV2AccessoryIDData
+ _objc_msgSend$homeKitV2AuthTagData
+ _objc_msgSend$homeKitV2InstanceID
+ _objc_msgSend$homeKitV2StateNumber
+ _objc_msgSend$homeKitV2Value
+ _objc_msgSend$initWithEventType:
+ _objc_msgSend$initWithEventType:withError:
+ _objc_msgSend$initWithInfo:withSessionId:withState:withCoordIds:withLocation:
+ _objc_msgSend$initWithInfo:withSize:
+ _objc_msgSend$initWithPowerSourceDetails:internalFlags:
+ _objc_msgSend$initWithSession:
+ _objc_msgSend$initWithValue:withValue:
+ _objc_msgSend$initWithValues:withProperty:withName:
+ _objc_msgSend$int64ValueSafe
+ _objc_msgSend$invalidateComponentWithPartID:
+ _objc_msgSend$isAggregateComponent
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$leAudioEventHandler
+ _objc_msgSend$listOfClients
+ _objc_msgSend$lowWarnLevel
+ _objc_msgSend$maxAge
+ _objc_msgSend$maxCapacity
+ _objc_msgSend$mfgData
+ _objc_msgSend$nearbyActionAuthTag
+ _objc_msgSend$nearbyActionTargetAuthTag
+ _objc_msgSend$nearbyInfoAuthTag
+ _objc_msgSend$nearbyInfoV2NearbyFaceTimeData
+ _objc_msgSend$nearbyInfoV2NearbyFaceTimeEncryptedData
+ _objc_msgSend$objectDiscoveryBatteryState
+ _objc_msgSend$objectDiscoveryMode
+ _objc_msgSend$objectDiscoveryNearOwnerID
+ _objc_msgSend$objectDiscoveryProductID
+ _objc_msgSend$objectSetupBatteryPerformance
+ _objc_msgSend$objectSetupBatteryState
+ _objc_msgSend$objectSetupColorCode
+ _objc_msgSend$objectSetupFlags
+ _objc_msgSend$objectSetupFontCode
+ _objc_msgSend$objectSetupMessage
+ _objc_msgSend$partID
+ _objc_msgSend$partName
+ _objc_msgSend$peerStatusFlag
+ _objc_msgSend$peripheral:didCompleteChannelSoundingProcedure:error:
+ _objc_msgSend$present
+ _objc_msgSend$proximityPairingOtherBudProductID
+ _objc_msgSend$proximityPairingSubType
+ _objc_msgSend$proximityServiceCategory
+ _objc_msgSend$proximityServiceClassicAddress
+ _objc_msgSend$proximityServiceFlags
+ _objc_msgSend$proximityServiceMeasuredPower
+ _objc_msgSend$proximityServicePSM
+ _objc_msgSend$proximityServicePayload
+ _objc_msgSend$proximityServiceProductID
+ _objc_msgSend$proximityServiceSetupHash
+ _objc_msgSend$proximityServiceSubType
+ _objc_msgSend$proximityServiceVendorID
+ _objc_msgSend$proximityServiceVersion
+ _objc_msgSend$publish
+ _objc_msgSend$registerLEAudioClient
+ _objc_msgSend$releaseSource
+ _objc_msgSend$removeFlags
+ _objc_msgSend$sendLEAudioMsg:args:completion:
+ _objc_msgSend$setAdaptiveVolumeCapability:
+ _objc_msgSend$setAdvDataPerType:
+ _objc_msgSend$setAdvInstanceType:
+ _objc_msgSend$setAdvInterval:
+ _objc_msgSend$setAirdropConfigData:
+ _objc_msgSend$setAirdropFlags:
+ _objc_msgSend$setAirdropHash1:
+ _objc_msgSend$setAirdropHash2:
+ _objc_msgSend$setAirdropHash3:
+ _objc_msgSend$setAirdropHash4:
+ _objc_msgSend$setAirdropModel:
+ _objc_msgSend$setAirdropTempAuthTagData:
+ _objc_msgSend$setAirdropVersion:
+ _objc_msgSend$setAirplaySourceAuthTagData:
+ _objc_msgSend$setAirplaySourceFlags:
+ _objc_msgSend$setAirplayTargetConfigSeed:
+ _objc_msgSend$setAirplayTargetFlags:
+ _objc_msgSend$setAirplayTargetIPv4:
+ _objc_msgSend$setAirplayTargetIPv6:
+ _objc_msgSend$setAudioStreamState:
+ _objc_msgSend$setAutoAncCapability:
+ _objc_msgSend$setBatteryInfo:
+ _objc_msgSend$setBatteryInfoCase:
+ _objc_msgSend$setBatteryInfoLeft:
+ _objc_msgSend$setBatteryInfoMain:
+ _objc_msgSend$setBatteryInfoRight:
+ _objc_msgSend$setBleAddressData:
+ _objc_msgSend$setBleAdvertisementData:
+ _objc_msgSend$setBleAdvertisementTimestamp:
+ _objc_msgSend$setBleAdvertisementTimestampMachContinuous:
+ _objc_msgSend$setBleAppleManufacturerData:
+ _objc_msgSend$setBleChannel:
+ _objc_msgSend$setBleRSSI:
+ _objc_msgSend$setBtAddressData:
+ _objc_msgSend$setCaseVersion:
+ _objc_msgSend$setChangeFlags:
+ _objc_msgSend$setClassicRSSI:
+ _objc_msgSend$setColorInfo:
+ _objc_msgSend$setConnectedServices:
+ _objc_msgSend$setConversationDetectCapability:
+ _objc_msgSend$setDeviceFlags:
+ _objc_msgSend$setDoubleTapActionLeft:
+ _objc_msgSend$setDoubleTapActionRight:
+ _objc_msgSend$setEnableAdvertisingWithPowerAssertion:
+ _objc_msgSend$setEnableEPAForAdvertisement:
+ _objc_msgSend$setEnableObjectLocatorResponseOnAdvertisingInstance:
+ _objc_msgSend$setEndCallCapability:
+ _objc_msgSend$setFinalSummary:
+ _objc_msgSend$setGroupID:
+ _objc_msgSend$setHomeKitV1Category:
+ _objc_msgSend$setHomeKitV1CompatibleVersion:
+ _objc_msgSend$setHomeKitV1ConfigurationNumber:
+ _objc_msgSend$setHomeKitV1DeviceIDData:
+ _objc_msgSend$setHomeKitV1Flags:
+ _objc_msgSend$setHomeKitV1SetupHash:
+ _objc_msgSend$setHomeKitV1StateNumber:
+ _objc_msgSend$setHomeKitV2AccessoryIDData:
+ _objc_msgSend$setHomeKitV2AuthTagData:
+ _objc_msgSend$setHomeKitV2InstanceID:
+ _objc_msgSend$setHomeKitV2StateNumber:
+ _objc_msgSend$setHomeKitV2Value:
+ _objc_msgSend$setInternalFlags:
+ _objc_msgSend$setLEAudioDeviceType:
+ _objc_msgSend$setListOfClients:
+ _objc_msgSend$setMfgData:
+ _objc_msgSend$setNearbyActionAuthTag:
+ _objc_msgSend$setNearbyActionFlags:
+ _objc_msgSend$setNearbyActionNoWakeType:
+ _objc_msgSend$setNearbyActionTargetAuthTag:
+ _objc_msgSend$setNearbyActionType:
+ _objc_msgSend$setNearbyAuthTag:
+ _objc_msgSend$setNearbyInfoAuthTag:
+ _objc_msgSend$setNearbyInfoFlags:
+ _objc_msgSend$setNearbyInfoV2AuthIntegrityTagData:
+ _objc_msgSend$setNearbyInfoV2AuthTagData:
+ _objc_msgSend$setNearbyInfoV2DecryptedFlags:
+ _objc_msgSend$setNearbyInfoV2EncryptedData:
+ _objc_msgSend$setNearbyInfoV2EncryptedFlags:
+ _objc_msgSend$setNearbyInfoV2Flags:
+ _objc_msgSend$setObjectSetupBatteryPerformance:
+ _objc_msgSend$setObjectSetupBatteryState:
+ _objc_msgSend$setObjectSetupColorCode:
+ _objc_msgSend$setObjectSetupFlags:
+ _objc_msgSend$setObjectSetupFontCode:
+ _objc_msgSend$setObjectSetupMessage:
+ _objc_msgSend$setP50:
+ _objc_msgSend$setP50Max:
+ _objc_msgSend$setP90:
+ _objc_msgSend$setP90Max:
+ _objc_msgSend$setP95:
+ _objc_msgSend$setP95Max:
+ _objc_msgSend$setP99:
+ _objc_msgSend$setP99Max:
+ _objc_msgSend$setPartID:
+ _objc_msgSend$setPeerStatusFlag:
+ _objc_msgSend$setPresetResults:
+ _objc_msgSend$setProximityServiceCategory:
+ _objc_msgSend$setProximityServiceData:
+ _objc_msgSend$setProximityServiceFlags:
+ _objc_msgSend$setProximityServiceMeasuredPower:
+ _objc_msgSend$setProximityServicePSM:
+ _objc_msgSend$setProximityServiceProductID:
+ _objc_msgSend$setProximityServiceSetupHash:
+ _objc_msgSend$setProximityServiceSubType:
+ _objc_msgSend$setProximityServiceVendorID:
+ _objc_msgSend$setProximityServiceVersion:
+ _objc_msgSend$setSessionInfo:
+ _objc_msgSend$setSourceID:
+ _objc_msgSend$setSpatialInteractionConfigFlags:
+ _objc_msgSend$setSpatialInteractionFlags:
+ _objc_msgSend$setSpatialInteractionIdentifiers:
+ _objc_msgSend$setSpatialInteractionPresenceConfigData:
+ _objc_msgSend$setSpatialInteractionUWBConfigData:
+ _objc_msgSend$setStopOnAdvertisingAddressChange:
+ _objc_msgSend$setUpdatedValue:
+ _objc_msgSend$setWiProxUpdateTimestamp:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$sourceID
+ _objc_msgSend$spatialInteractionConfigFlags
+ _objc_msgSend$spatialInteractionFlags
+ _objc_msgSend$spatialInteractionIdentifiers
+ _objc_msgSend$spatialInteractionPresenceConfigData
+ _objc_msgSend$spatialInteractionTokenData
+ _objc_msgSend$spatialInteractionUWBConfigData
+ _objc_msgSend$spatialInteractionUWBTokenFlags
+ _objc_msgSend$spatialInteractionUserInfo
+ _objc_msgSend$startLEAudioXPC
+ _objc_msgSend$stopOnAdvertisingAddressChange
+ _objc_msgSend$temperature
+ _objc_msgSend$tipiConnectionStatus
+ _objc_msgSend$tipiState
+ _objc_msgSend$transportType
+ _objc_msgSend$updateHandler
+ _objc_msgSend$updatePartID
+ _objc_msgSend$updateWithCBPowerSource:
+ _objc_msgSend$updatedValue
+ _objc_msgSend$userNotificationEvent:completion:
+ _objc_msgSend$wiProxUpdateTimestamp
+ _objc_retain_x5
+ _tcc_authorization_record_get_authorization_reason
+ _xpc_array_create_empty
+ _xpc_array_set_data
+ _xpc_dictionary_get_uuid
+ _xpc_uint64_create
- -[CBCentralManager _scanForPeripheralsWithServices:options:]
- -[CBDiscovery setTypeToRssiThresholds:]
- -[CBDiscovery typeToRssiThresholds]
- -[CBPeripheral isConnectedToSystem].288
- GCC_except_table127
- GCC_except_table13
- GCC_except_table140
- GCC_except_table157
- GCC_except_table27
- GCC_except_table31
- GCC_except_table50
- GCC_except_table54
- GCC_except_table73
- GCC_except_table77
- GCC_except_table99
- _CBCentralManagerScanOptionFilterIdentifier
- _OBJC_IVAR_$_CBDevice._adaptiveVolumeCapability
- _OBJC_IVAR_$_CBDevice._airdropConfigData
- _OBJC_IVAR_$_CBDevice._airdropFlags
- _OBJC_IVAR_$_CBDevice._airdropHash1
- _OBJC_IVAR_$_CBDevice._airdropHash2
- _OBJC_IVAR_$_CBDevice._airdropHash3
- _OBJC_IVAR_$_CBDevice._airdropHash4
- _OBJC_IVAR_$_CBDevice._airdropModel
- _OBJC_IVAR_$_CBDevice._airdropTempAuthTagData
- _OBJC_IVAR_$_CBDevice._airdropVersion
- _OBJC_IVAR_$_CBDevice._airplaySourceAuthTagData
- _OBJC_IVAR_$_CBDevice._airplaySourceFlags
- _OBJC_IVAR_$_CBDevice._airplayTargetConfigSeed
- _OBJC_IVAR_$_CBDevice._airplayTargetFlags
- _OBJC_IVAR_$_CBDevice._airplayTargetIPv4
- _OBJC_IVAR_$_CBDevice._audioStreamState
- _OBJC_IVAR_$_CBDevice._autoAncCapability
- _OBJC_IVAR_$_CBDevice._batteryInfoCase
- _OBJC_IVAR_$_CBDevice._batteryInfoLeft
- _OBJC_IVAR_$_CBDevice._batteryInfoMain
- _OBJC_IVAR_$_CBDevice._batteryInfoRight
- _OBJC_IVAR_$_CBDevice._bleAddressData
- _OBJC_IVAR_$_CBDevice._bleAdvertisementData
- _OBJC_IVAR_$_CBDevice._bleAdvertisementTimestamp
- _OBJC_IVAR_$_CBDevice._bleAdvertisementTimestampMachContinuous
- _OBJC_IVAR_$_CBDevice._bleAppleManufacturerData
- _OBJC_IVAR_$_CBDevice._bleChannel
- _OBJC_IVAR_$_CBDevice._bleRSSI
- _OBJC_IVAR_$_CBDevice._btAddressData
- _OBJC_IVAR_$_CBDevice._caseVersion
- _OBJC_IVAR_$_CBDevice._classicRSSI
- _OBJC_IVAR_$_CBDevice._colorInfo
- _OBJC_IVAR_$_CBDevice._connectedServices
- _OBJC_IVAR_$_CBDevice._conversationDetectCapability
- _OBJC_IVAR_$_CBDevice._doubleTapActionLeft
- _OBJC_IVAR_$_CBDevice._doubleTapActionRight
- _OBJC_IVAR_$_CBDevice._doubleTapCapability
- _OBJC_IVAR_$_CBDevice._endCallCapability
- _OBJC_IVAR_$_CBDevice._homeKitV1Category
- _OBJC_IVAR_$_CBDevice._homeKitV1CompatibleVersion
- _OBJC_IVAR_$_CBDevice._homeKitV1ConfigurationNumber
- _OBJC_IVAR_$_CBDevice._homeKitV1DeviceIDData
- _OBJC_IVAR_$_CBDevice._homeKitV1Flags
- _OBJC_IVAR_$_CBDevice._homeKitV1SetupHash
- _OBJC_IVAR_$_CBDevice._homeKitV1StateNumber
- _OBJC_IVAR_$_CBDevice._homeKitV2AccessoryIDData
- _OBJC_IVAR_$_CBDevice._homeKitV2AuthTagData
- _OBJC_IVAR_$_CBDevice._homeKitV2InstanceID
- _OBJC_IVAR_$_CBDevice._homeKitV2StateNumber
- _OBJC_IVAR_$_CBDevice._homeKitV2Value
- _OBJC_IVAR_$_CBDevice._nearbyActionAuthTag
- _OBJC_IVAR_$_CBDevice._nearbyActionFlags
- _OBJC_IVAR_$_CBDevice._nearbyActionNoWakeType
- _OBJC_IVAR_$_CBDevice._nearbyActionTargetAuthTag
- _OBJC_IVAR_$_CBDevice._nearbyActionType
- _OBJC_IVAR_$_CBDevice._nearbyAuthTag
- _OBJC_IVAR_$_CBDevice._nearbyInfoAuthTag
- _OBJC_IVAR_$_CBDevice._nearbyInfoFlags
- _OBJC_IVAR_$_CBDevice._nearbyInfoV2AuthIntegrityTagData
- _OBJC_IVAR_$_CBDevice._nearbyInfoV2AuthTagData
- _OBJC_IVAR_$_CBDevice._nearbyInfoV2DecryptedFlags
- _OBJC_IVAR_$_CBDevice._nearbyInfoV2EncryptedData
- _OBJC_IVAR_$_CBDevice._nearbyInfoV2EncryptedFlags
- _OBJC_IVAR_$_CBDevice._nearbyInfoV2Flags
- _OBJC_IVAR_$_CBDevice._objectSetupBatteryPerformance
- _OBJC_IVAR_$_CBDevice._objectSetupBatteryState
- _OBJC_IVAR_$_CBDevice._objectSetupColorCode
- _OBJC_IVAR_$_CBDevice._objectSetupFlags
- _OBJC_IVAR_$_CBDevice._objectSetupFontCode
- _OBJC_IVAR_$_CBDevice._objectSetupMessage
- _OBJC_IVAR_$_CBDevice._peerStatusFlag
- _OBJC_IVAR_$_CBDevice._proximityServiceCategory
- _OBJC_IVAR_$_CBDevice._proximityServiceClassicAddress
- _OBJC_IVAR_$_CBDevice._proximityServiceData
- _OBJC_IVAR_$_CBDevice._proximityServiceFlags
- _OBJC_IVAR_$_CBDevice._proximityServiceMeasuredPower
- _OBJC_IVAR_$_CBDevice._proximityServicePSM
- _OBJC_IVAR_$_CBDevice._proximityServiceProductID
- _OBJC_IVAR_$_CBDevice._proximityServiceSetupHash
- _OBJC_IVAR_$_CBDevice._proximityServiceSubType
- _OBJC_IVAR_$_CBDevice._proximityServiceVendorID
- _OBJC_IVAR_$_CBDevice._proximityServiceVersion
- _OBJC_IVAR_$_CBDevice._spatialInteractionConfigFlags
- _OBJC_IVAR_$_CBDevice._spatialInteractionFlags
- _OBJC_IVAR_$_CBDevice._spatialInteractionIdentifiers
- _OBJC_IVAR_$_CBDevice._spatialInteractionPeerID
- _OBJC_IVAR_$_CBDevice._spatialInteractionPresenceConfigData
- _OBJC_IVAR_$_CBDevice._spatialInteractionTokenData
- _OBJC_IVAR_$_CBDevice._spatialInteractionUWBConfigData
- _OBJC_IVAR_$_CBDevice._spatialInteractionUserInfo
- _OBJC_IVAR_$_CBDiscovery._typeToRssiThresholds
- ___25-[CBL2CAPChannel dealloc]_block_invoke
- ___35-[CBDiscovery _activateDirectStart]_block_invoke.171
- ___35-[CBDiscovery _activateDirectStart]_block_invoke_2.174
- ___39-[CBDiscovery setTypeToRssiThresholds:]_block_invoke
- ___59-[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:]_block_invoke.214
- ___59-[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:]_block_invoke.214.cold.1
- ___block_descriptor_40_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
- ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
- ___block_literal_global.125
- ___block_literal_global.135
- ___block_literal_global.258
- ___block_literal_global.260
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.408
- ___block_literal_global.426
- ___block_literal_global.71
- ___block_literal_global.761
- ___block_literal_global.89
- _convertToCBMsgId
- _convertToCBMsgId.cold.1
- _convertToWhbMsgId
- _convertToWhbMsgId.cold.1
- _objc_msgSend$_scanForPeripheralsWithServices:options:
- _objc_msgSend$typeToRssiThresholds
CStrings:
+ " %@ %s%u%%"
+ " Mock"
+ " Nm '%@'"
+ "!&~"
+ "### Error hid usernotification event (%@) due to %@"
+ "### Excessive interval is %llu us"
+ "### Failed to create power source ID for %@"
+ "### Failed to set power source details"
+ "### No battery info exists %@"
+ "### No partID for found aggregate component: %@"
+ "### Snapshot: Packet TS 0x%016llX, Actual %llu, Expected %llu, Delta %lld, ErrorRate %.2f%%, Interval %.3f ms, MaxInterval %.3f ms, RSSI %d, P50 %.2fms, P90 %.2fms, P95 %.2fms, P99 %.2fms"
+ "### Summary: Packet TS 0x%016llX, Actual %llu, Expected %llu, Delta %lld, ErrorRate %.2f%%, Interval %.3f ms, MaxInterval %.3f ms, RSSI %d, P50 %.2fms(%.2fms), P90 %.2fms(%.2fms), P95 %.2fms(%.2fms), P99 %.2fms(%.2fms)"
+ "%@ %@"
+ "%@: device %@, event %s"
+ "%s: %u -> %u"
+ "%s: <%@> -> <%@>"
+ "&"
+ ","
+ ", %s %u"
+ ", %s <%@>"
+ ", AcCa %@"
+ ", AggC %s"
+ ", Battery %s%u%%"
+ ", Battery %u%% (%s)"
+ ", CID 0x%X"
+ ", Components (%@):"
+ ", FC %ld"
+ ", GID %@"
+ ", IF %@"
+ ", MaxC %hhu%%"
+ ", PaID %@"
+ ", Present %s"
+ ", SID %ld"
+ ", TPT %@"
+ ", Temp %ld"
+ ", Type '%@'"
+ ", VID 0x%04X (%s)"
+ ", VIDSrc %s"
+ ", advDataPerType: %@"
+ ", apTI6 %@"
+ ", bfTC %@"
+ ", clients: %@"
+ ", enable EPA: %d"
+ ", gAsM %s"
+ ", gUbP %s"
+ ", interval: %.2f ms"
+ ", mfgData: %@"
+ ", nb2FT %@"
+ ", nb2FT <%@>"
+ ", object locator: %d"
+ ", power assertion: %d"
+ ", stop on address change: %d"
+ ", update timestamp: %@"
+ "-%@"
+ "-[CBDevice _matchingFlags:exactMatch:]"
+ "-[CBDevice isEqualToDevice:exactMatch:]"
+ "-[CBDevice isLowerThanAgeLimit:compareTimestamp:]"
+ "-[CBDiscovery injectAOPBufAdv:]"
+ "-[CBHIDPerformanceMonitor _calculatePercentile:percentile:]"
+ "-[CBHIDPerformanceMonitor _showSummaryResult:isFinal:packetMics:statsDelta:deltaMics:countActual:]"
+ "-[CBPowerSource _updateAggregateWithComponent:]"
+ "-[CBPowerSource dictionaryRepresentation]"
+ "-[CBPowerSource publish]"
+ "-[CBPowerSource releaseSource]"
+ "-[CBPowerSource updateWithCBPowerSource:]"
+ "-[CBUserController userNotificationEvent:completion:]_block_invoke_2"
+ "0106"
+ "010D"
+ "010E"
+ "1843"
+ "1844"
+ "1845"
+ "1846"
+ "1848"
+ "1849"
+ "184B"
+ "184C"
+ "184D"
+ "1854"
+ "1855"
+ "1b8d9548-c066-4fbf-bc7e-cf3e5a3fabbf"
+ "24F3F235-12C9-477A-9F13-063C68504F97"
+ "2B51"
+ "2B77"
+ "2B78"
+ "2B79"
+ "2B7A"
+ "2B7B"
+ "2B7C"
+ "2B7D"
+ "2B7E"
+ "2B7F"
+ "2B80"
+ "2B81"
+ "2B82"
+ "2B83"
+ "2B84"
+ "2B85"
+ "2B86"
+ "2B87"
+ "2B93"
+ "2B94"
+ "2B95"
+ "2B96"
+ "2B97"
+ "2B98"
+ "2B99"
+ "2B9A"
+ "2B9B"
+ "2B9C"
+ "2B9D"
+ "2B9E"
+ "2B9F"
+ "2BA0"
+ "2BA1"
+ "2BA2"
+ "2BA3"
+ "2BA4"
+ "2BA5"
+ "2BA6"
+ "2BA7"
+ "2BB3"
+ "2BB4"
+ "2BB5"
+ "2BB6"
+ "2BB7"
+ "2BB8"
+ "2BB9"
+ "2BBA"
+ "2BBB"
+ "2BBC"
+ "2BBD"
+ "2BBE"
+ "2BBF"
+ "2BC0"
+ "2BC1"
+ "2BC2"
+ "2BC3"
+ "2BDA"
+ "2BDB"
+ "2BDC"
+ "2BED"
+ "3C7F9BDC-3BCB-A75F-C969-9BBD7F058F2B"
+ "6.0"
+ "8640382C-DF0A-4E46-9CAB-36C05467949E"
+ "8D79E060-DA4C-45A5-B668-B4B5352D41FF"
+ "96E14983-7845-49FE-B8BF-E25F686943C6"
+ ": Peer %@"
+ "="
+ "@\"<CBStackISOStream>\""
+ "@\"CBCoordinatedSetInfo\""
+ "@\"CBLEAudioHearingAidPreset\""
+ "@\"CBLEAudioSessionInfo\""
+ "@\"CBPowerSource\""
+ "@\"NSDate\""
+ "@28@0:8@16C24"
+ "@28@0:8@16I24"
+ "@32@0:8C16C20@24"
+ "@32@0:8q16@24"
+ "@56@0:8@16@24q32@40@48"
+ "AC Power"
+ "Accessory Category"
+ "Accessory Identifier"
+ "Accessory Source"
+ "Active Preset Index"
+ "AdHocPairedDevice"
+ "AdHocPairing"
+ "AirPlayTargetIPv6"
+ "Audio Battery Case"
+ "Audio Input Control Point"
+ "Audio Input Control Service"
+ "Audio Input Description"
+ "Audio Input State"
+ "Audio Input Status"
+ "Audio Input Type"
+ "Audio Location"
+ "Audio Output Description"
+ "B24@?0Q8Q16"
+ "B28@0:8@16B24"
+ "B32@0:8@16Q24"
+ "BAA597B6-CFA9-405D-A489-158874B6F584"
+ "BAS"
+ "BLE MFi"
+ "BT_CBNearbyInfoV2EncryptedNearbyFaceTimePayloadV1"
+ "Battery Case"
+ "Battery Level Left"
+ "Battery Level Main"
+ "Battery Level Right"
+ "Battery Level Status"
+ "Battery Power"
+ "Bearer List Current Calls"
+ "Bearer Provider Name"
+ "Bearer Signal Strength"
+ "Bearer Signal Strength Reporting Interval"
+ "Bearer Technology"
+ "Bearer UCI"
+ "Bearer URI Schemes Supported List"
+ "CBCoordinatedMemberInfo"
+ "CBCoordinatedSetInfo"
+ "CBDiscovery _bufferedTypeConfigs set without appropriate discovery types, _bufferedTypeConfigs not sent to AOP"
+ "CBISOReadRequest"
+ "CBISOWriteRequest"
+ "CBLEAudioHearingAidPreset"
+ "CBLEAudioHearingAidUpdateEvent"
+ "CBLEAudioPeripheralUpdateEvent"
+ "CBLEAudioSessionEvent"
+ "CBLEAudioSessionInfo"
+ "CBPowerSource"
+ "CBPowerSource convert XPC dict failed"
+ "CBPowerSource super init failed"
+ "CBUserNotificationRequest"
+ "CBUserNotificationRequest convert XPC dict failed"
+ "CBWPDaemonAdvertisingData"
+ "Call Control Point"
+ "Call Control Point Optional Opcodes"
+ "Call Friendly Name"
+ "Call State"
+ "Calling LE audio event handler"
+ "Case"
+ "Charging"
+ "Classic GC USBBT Pairing: %s\n"
+ "Classic GC autoswitch mode: %s\n"
+ "Combined"
+ "Combined Parts"
+ "Content Control Id"
+ "Coordinated Set Identification Service"
+ "Coordinated Set Size"
+ "Create LE audio XPC"
+ "Current Group Object ID"
+ "Current Track Object ID"
+ "Current Track Segments Object ID"
+ "DGDv"
+ "DOD"
+ "DOS"
+ "Discharging"
+ "DovePeace2"
+ "DsIA"
+ "E277E685-64CB-4A32-BF65-8766E708A037"
+ "E3AB6C3D-3E94-7A2C-DB59-B8B91723CAD4"
+ "EC7CC9FE-667F-41C6-8B79-663A1F08C39A"
+ "F299FC19-5898-4F68-ACE6-E036ABE50781"
+ "Failed to create LE audio XPC"
+ "Failed to send LE audio register message over XPC, %@"
+ "FindMyPair"
+ "FindMyTemporaryAggressiveLegacyExtendedRange"
+ "FullyCharged"
+ "Gain Setting Properties"
+ "Game Controller"
+ "GameControllerConnected"
+ "Generated event: %@"
+ "Generic Media Control Service"
+ "Generic Telephone Bearer Service"
+ "Group Identifier"
+ "HIDUSBPairingComplete"
+ "HandleLESynchronizationEventMsg:"
+ "Headphone"
+ "Hearing Access Service"
+ "Hearing Aid Features"
+ "Hearing Aid Preset Control Point"
+ "Host version:       %s\n"
+ "Incoming Call"
+ "Incoming Call Target Bearer URI"
+ "InternalTestAdvWithHigherPower"
+ "InternalTestAdvWithHigherPowerServiceDataConnectable"
+ "InternalTestAdvWithHigherPowerServiceDataNonConnectable"
+ "InternalTestAdvWithHigherPowerServiceDataS2"
+ "InternalTestAdvWithHigherPowerServiceDataS8"
+ "InternalTestDiscoveryScanCodedPHY"
+ "InternalTestDiscoveryScanWithMRC"
+ "InternalTestScanLowDutyCycleMCOnly"
+ "InternalTestUUIDScanWithMinRSSI"
+ "InternalTestUUIDScanWithMinRSSIMediumLow"
+ "Is Present"
+ "LE audio XPC interrupted"
+ "LE audio XPC invalid"
+ "LE audio message is nil"
+ "LE audio unregistered"
+ "Low Warn Level"
+ "MFi Accessory Attributes"
+ "MFi Accessory Type"
+ "MFi Command"
+ "MFi Protocol String"
+ "MFi Team ID"
+ "Media Control Point"
+ "Media Control Point Opcodes Supported"
+ "Media Control Service"
+ "Media Player Icon Object ID"
+ "Media Player Icon URL"
+ "Media Player Name"
+ "Media State"
+ "MiLoBuffer"
+ "Microphone Control Service"
+ "MobileBluetooth-190.40.1.1"
+ "Mock"
+ "Mute"
+ "N"
+ "Name"
+ "NearbyActionBuffer"
+ "NearbyFaceTime"
+ "NearbyFaceTimeData"
+ "NearbyInfoBuffer"
+ "NearbyInfoV2NearbyFaceTime"
+ "NearbyInfoV2NearbyFaceTimeData"
+ "Next Track Object ID"
+ "No LE audio event handher found"
+ "No change flags, skipping publish: %@"
+ "No devices found matching device %@"
+ "No peripheral found in HandleLESynchronizationEventMsg for args %@"
+ "Not LE audio XPC allowed"
+ "Not able calculate percentile %.2f"
+ "OBC"
+ "Optimized Battery Charging Engaged"
+ "Other"
+ "P50"
+ "P50Max"
+ "P90"
+ "P90Max"
+ "P95"
+ "P95Max"
+ "P99"
+ "P99Max"
+ "Parent Group Object ID"
+ "Part Identifier"
+ "Part Name"
+ "Pencil"
+ "Playback Speed"
+ "Playing Order"
+ "Playing Orders Supported"
+ "Power Source ID"
+ "Power Source State"
+ "Power source updated %@"
+ "Powerb3,1"
+ "Product ID"
+ "ProximityServiceDeviceSetup"
+ "Publishing %@"
+ "Ready to use LE audio"
+ "Received XPC message for LE audio - %s: %@"
+ "Releasing power source %@"
+ "SIMTransfer3"
+ "SITD"
+ "SOSBeaconActivateAdvA"
+ "SOSBeaconActivateAdvB"
+ "SOSBeaconActivateScan"
+ "SOSBeaconPartA"
+ "SOSBeaconPartB"
+ "SOSBeaconPrecisionFindRequest"
+ "SOSBeaconPrecisionFindResponse"
+ "SOSBeaconScan"
+ "Search Control Point"
+ "Search Results Object ID"
+ "Secure Sensor"
+ "Secure Sensor Audio"
+ "Secure Sensor Configuration"
+ "Secure Sensor Debug"
+ "Secure Sensor Pairing"
+ "Seeking Speed"
+ "Session is an extension"
+ "Set Identity Resolving Key"
+ "Set LE Audio device type: %@"
+ "Set Member Lock"
+ "Set Member Rank"
+ "SharingHomePodSetup"
+ "Single"
+ "SmartTech"
+ "Spatial HID Service"
+ "Status Flags"
+ "T@\"<CBStackISOStream>\",&,N,V_stream"
+ "T@\"CBCoordinatedSetInfo\",R,N,V_coordinatedSetInfo"
+ "T@\"CBLEAudioHearingAidPreset\",C,N,V_activePreset"
+ "T@\"CBLEAudioSessionInfo\",C,N,V_sessionInfo"
+ "T@\"CBPowerSource\",C,N,V_powerSourceMock"
+ "T@\"NSArray\",C,N,V_bufferedAdvConfigsForAOP"
+ "T@\"NSArray\",C,N,V_listOfClients"
+ "T@\"NSData\",C,N,V_mfgData"
+ "T@\"NSData\",C,N,V_nearbyInfoV2NearbyFaceTimeData"
+ "T@\"NSData\",C,N,V_nearbyInfoV2NearbyFaceTimeEncryptedData"
+ "T@\"NSData\",C,N,V_proximityServicePayload"
+ "T@\"NSData\",C,N,V_randomData"
+ "T@\"NSData\",R,C,N,V_nearbyInfoV2NearbyFaceTimeData"
+ "T@\"NSDictionary\",C,N"
+ "T@\"NSDictionary\",C,N,V_advDataPerType"
+ "T@\"NSError\",R,C,N,V_error"
+ "T@\"NSMutableArray\",&,N,V_connectedIdentifiers"
+ "T@\"NSMutableArray\",C,N,V_presetResults"
+ "T@\"NSMutableArray\",R,N,V_audioSessions"
+ "T@\"NSMutableArray\",R,N,V_connectedIdentifiers"
+ "T@\"NSMutableDictionary\",R,N"
+ "T@\"NSMutableDictionary\",R,N,V_locations"
+ "T@\"NSNumber\",C,N,V_updatedValue"
+ "T@\"NSNumber\",C,N,V_wiProxUpdateTimestamp"
+ "T@\"NSNumber\",R,C,N,V_updatedValue"
+ "T@\"NSString\",&,N,V_setName"
+ "T@\"NSString\",C,N,V_accessoryID"
+ "T@\"NSString\",C,N,V_groupID"
+ "T@\"NSString\",C,N,V_partName"
+ "T@\"NSString\",C,N,V_transportType"
+ "T@\"NSString\",C,N,V_type"
+ "T@\"NSString\",R,&,N,V_presetName"
+ "T@\"NSUUID\",R,N,V_audioSessionIdentifier"
+ "T@?,C,N,V_cisConnectEvent"
+ "T@?,C,N,V_cisDisconnectEvent"
+ "T@?,C,N,V_cisPeripheralConnectEvent"
+ "T@?,C,N,V_cisPeripheralDisconnectEvent"
+ "T@?,C,N,V_completionHandler"
+ "T@?,C,N,V_leAudioEventHandler"
+ "T@?,C,N,V_removeCIGCompletion"
+ "T@?,C,N,V_setupCIGCompletion"
+ "T@?,C,N,V_updateHandler"
+ "TB,N,V_addExtendedProperties"
+ "TB,N,V_enableAdvertisingWithPowerAssertion"
+ "TB,N,V_enableEPAForAdvertisement"
+ "TB,N,V_enableObjectLocatorResponseOnAdvertisingInstance"
+ "TB,N,V_finalSummary"
+ "TB,N,V_present"
+ "TB,N,V_stopOnAdvertisingAddressChange"
+ "TB,R,N,V_dynamicPresets"
+ "TB,R,N,V_independentPresets"
+ "TB,R,N,V_isAvailable"
+ "TB,R,N,V_isWritable"
+ "TB,R,N,V_presetSyncSupported"
+ "TB,R,N,V_writablePresets"
+ "TC,N,V_advInstanceType"
+ "TC,N,V_maxAge"
+ "TC,N,V_memberRank"
+ "TC,N,V_setSize"
+ "TC,R,N,V_hearingAidType"
+ "TC,R,N,V_presetIndex"
+ "TI,N,V_appearanceValue"
+ "TI,N,V_changeFlags"
+ "TI,N,V_event"
+ "TI,N,V_missedReads"
+ "TI,R,N,V_location"
+ "TMAP Role"
+ "TQ,N"
+ "TS,N,V_accessoryCategory"
+ "TS,N,V_advInterval"
+ "TS,N,V_batteryInfo"
+ "TS,N,V_partID"
+ "Tc,N,V_gameControllerAutoSwitchMode"
+ "Tc,N,V_gameControllerUSBBluetoothPairing"
+ "Td,N,V_P50"
+ "Td,N,V_P50Max"
+ "Td,N,V_P90"
+ "Td,N,V_P90Max"
+ "Td,N,V_P95"
+ "Td,N,V_P95Max"
+ "Td,N,V_P99"
+ "Td,N,V_P99Max"
+ "Td,N,V_excessiveMs"
+ "Td,N,V_maxCapacity"
+ "Td,N,V_slideWindowSec"
+ "Telephone Bearer Service"
+ "Telephony and Media Audio Service"
+ "Temperature"
+ "Termination Reason"
+ "Time to Full Charge"
+ "Tq,N,V_familyCode"
+ "Tq,N,V_lowWarnLevel"
+ "Tq,N,V_sourceID"
+ "Tq,N,V_temperature"
+ "Tq,R,N,V_deviceType"
+ "Tq,R,N,V_eventType"
+ "Tq,R,N,V_sessionState"
+ "Track Changed"
+ "Track Duration"
+ "Track Position"
+ "Track Title"
+ "Trackpad"
+ "Transport Type"
+ "Type"
+ "Unable to decrypt NearbyInfoV2 sensitive data1"
+ "Unable to decrypt NearbyInfoV2 sensitive data2"
+ "Unexpected LE audio XPC error: %@"
+ "Unexpected LE audio XPC event: %@"
+ "Unhandled message: %d"
+ "Unsupported message for LE audio"
+ "Vendor ID"
+ "Vendor ID Source"
+ "Volume Control Point"
+ "Volume Control Service"
+ "Volume Flags"
+ "Volume Offset Control Point"
+ "Volume Offset Control Service"
+ "Volume Offset State"
+ "Volume State"
+ "WARNING: No LE audio event handler registered:%@"
+ "Y"
+ "^{OpaqueIOPSPowerSourceID=}"
+ "_P50"
+ "_P50Max"
+ "_P90"
+ "_P90Max"
+ "_P95"
+ "_P95Max"
+ "_P99"
+ "_P99Max"
+ "_accessoryCategory"
+ "_accessoryID"
+ "_activePreset"
+ "_addExtendedProperties"
+ "_advDataPerType"
+ "_advInstanceType"
+ "_advInterval"
+ "_appearanceValue"
+ "_audioSessionIdentifier"
+ "_audioSessions"
+ "_batteryInfo"
+ "_bufferedAdvConfigsForAOP"
+ "_calculatePercentile:percentile:"
+ "_cisConnectEvent"
+ "_cisDisconnectEvent"
+ "_cisPeripheralConnectEvent"
+ "_cisPeripheralDisconnectEvent"
+ "_clearAirplaySourceFlags"
+ "_clearAirplayTargetFlags"
+ "_clearAirplayTargetIPv4"
+ "_clearAirplayTargetIPv6"
+ "_clearDeviceInfoKey:"
+ "_clearDockKitAccessoryPayloadData"
+ "_clearFidoPayloadData"
+ "_clearGfpModelID"
+ "_clearGfpPayloadData"
+ "_clearHomeKitV1CompatibleVersion"
+ "_clearHomeKitV1ConfigurationNumber"
+ "_clearHomeKitV1Flags"
+ "_clearHomeKitV1SetupHash"
+ "_clearHomeKitV1StateNumber"
+ "_clearHomeKitV2AuthTagData"
+ "_clearHomeKitV2InstanceID"
+ "_clearHomeKitV2StateNumber"
+ "_clearHomeKitV2Value"
+ "_clearMspAddressData"
+ "_clearMspDeviceClass"
+ "_clearMspDisplayName"
+ "_clearMspSubScenario"
+ "_clearNearbyActionAuthTag"
+ "_clearNearbyActionDeviceClass"
+ "_clearNearbyActionFlags"
+ "_clearNearbyActionType"
+ "_clearNearbyActionV2Flags"
+ "_clearNearbyActionV2Type"
+ "_clearObjectSetupFlags"
+ "_clearObjectSetupFontCode"
+ "_clearObjectSetupMessage"
+ "_clearProximityServiceData"
+ "_clearProximityServiceFlags"
+ "_clearProximityServiceMeasuredPower"
+ "_clearProximityServicePSM"
+ "_clearProximityServiceSetupHash"
+ "_clearProximityServiceSubType"
+ "_clearProximityServiceVersion"
+ "_clearSpatialInteractionConfigFlags"
+ "_clearSpatialInteractionFlags"
+ "_clearSpatialInteractionIdentifiers"
+ "_clearSpatialInteractionPeerID"
+ "_clearSpatialInteractionPresenceConfigData"
+ "_clearSpatialInteractionTokenData"
+ "_clearSpatialInteractionUWBConfigData"
+ "_clearSpatialInteractionUserInfo"
+ "_completionHandler"
+ "_componentMap"
+ "_connectedIdentifiers"
+ "_coordinatedSetInfo"
+ "_dynamicPresets"
+ "_enableAdvertisingWithPowerAssertion"
+ "_enableEPAForAdvertisement"
+ "_enableObjectLocatorResponseOnAdvertisingInstance"
+ "_event"
+ "_eventType"
+ "_excessiveMs"
+ "_familyCode"
+ "_finalSummary"
+ "_gameControllerAutoSwitchMode"
+ "_gameControllerUSBBluetoothPairing"
+ "_groupID"
+ "_handleLEAudioXpcEvents:"
+ "_hearingAidType"
+ "_independentPresets"
+ "_intrmPacketDeltaMics"
+ "_isAvailable"
+ "_isWritable"
+ "_leAudioDevice"
+ "_leAudioEventHandler"
+ "_leAudioXpcConnection"
+ "_listOfClients"
+ "_location"
+ "_locations"
+ "_lowWarnLevel"
+ "_matchingFlags:exactMatch:"
+ "_maxAge"
+ "_maxCapacity"
+ "_memberRank"
+ "_mfgData"
+ "_missedReads"
+ "_nearbyInfoV2NearbyFaceTimeData"
+ "_nearbyInfoV2NearbyFaceTimeEncryptedData"
+ "_partID"
+ "_partName"
+ "_powerSourceMock"
+ "_present"
+ "_presetIndex"
+ "_presetName"
+ "_presetResults"
+ "_presetSyncSupported"
+ "_proximityServicePayload"
+ "_psID"
+ "_randomData"
+ "_removeCIGCompletion"
+ "_scanForPeripheralsWithServices:options:completion:"
+ "_sessionInfo"
+ "_sessionState"
+ "_setName"
+ "_setPartName"
+ "_setSize"
+ "_setupCIGCompletion"
+ "_showSummaryResult:isFinal:packetMics:statsDelta:deltaMics:countActual:"
+ "_slideWindowSec"
+ "_slidingWindowDate"
+ "_sourceID"
+ "_statsPacketCountInterim"
+ "_statsPacketDeltaMics"
+ "_statsPacketExcessiveInterval"
+ "_statsPacketMicsStartInterim"
+ "_statsPacketP50Max"
+ "_statsPacketP90Max"
+ "_statsPacketP95Max"
+ "_statsPacketP99Max"
+ "_stopOnAdvertisingAddressChange"
+ "_stream"
+ "_temperature"
+ "_transportType"
+ "_updateAggregateWithComponent:"
+ "_updateHandler"
+ "_updatedValue"
+ "_validLeAudioXpcCalled"
+ "_wiProxUpdateTimestamp"
+ "_writablePresets"
+ "aCat"
+ "accessoryCategory"
+ "accessoryID"
+ "accessoryStatusFlags %@: %@ %@"
+ "accountID %@ = %@"
+ "activePreset"
+ "adAT"
+ "adCD"
+ "adMO"
+ "adSt"
+ "adVC"
+ "adVE"
+ "adaptiveVolumeCapability %s = %s"
+ "adaptiveVolumeConfig %@ = %@"
+ "addExtendedProperties"
+ "advDataPerType"
+ "advInstanceType"
+ "advInterval"
+ "airdropFlags %@: %@ %@"
+ "airplaySourceFlags %@: %@ %@"
+ "airplayTargetFlags %@: %@ %@"
+ "airplayTargetIPv6"
+ "apTD"
+ "apTI6"
+ "appearanceValue %@ = %@"
+ "aprV"
+ "audioSessionIdentifier"
+ "audioSessions"
+ "audioStreamState %s = %s"
+ "autoAncCapability %s = %s"
+ "bAMD"
+ "bATm"
+ "bAdv"
+ "bTMC"
+ "batI"
+ "batteryInfo"
+ "bfCA"
+ "blCH"
+ "bleAddressData %@ = %@"
+ "btAD"
+ "btAddressData %@ = %@"
+ "btVe"
+ "bufferedAdvConfigsForAOP"
+ "bufferedTypeConfigs"
+ "bufferedTypeConfigs: %@ -> %@"
+ "bundleRecordForCurrentProcess"
+ "caseVersion %@ = %@"
+ "cbPC"
+ "cbPS"
+ "cdCA"
+ "centralManager:didUpdateSynchronizationEventForPeripheral:results:"
+ "changeMicrophoneGainSettingForSession:forAudioInputType:withMicGain:withResponse:"
+ "changeVolumeForSession:withVolume:withResponse:"
+ "changeVolumeMuteStateForSession:withVolumeMuteState:withResponse:"
+ "changeVolumeOffsetForSession:toLocation:withVolumeOffSet:withResponse:"
+ "checkIfExtension"
+ "cisConnectEvent"
+ "cisDisconnectEvent"
+ "cisPeripheralConnectEvent"
+ "cisPeripheralDisconnectEvent"
+ "clIN"
+ "clickHoldModeLeft %@ = %@"
+ "clickHoldModeRight %@ = %@"
+ "coSE"
+ "com.apple.bluetoothaudiod.cb"
+ "com.apple.bluetoothaudiod.leaudio-extension"
+ "combinedPublish"
+ "compare:"
+ "completionHandler"
+ "componentWithPartID:"
+ "components"
+ "connectCIS:"
+ "connectedIdentifiers"
+ "connectedServices %@: %@ %@"
+ "contactID %@ = %@"
+ "conversationDetectCapability %s = %s"
+ "conversationDetectConfig %@ = %@"
+ "coordinatedSetInfo"
+ "createSessionEvent:withMsg:"
+ "createXPCForLEAudio"
+ "crownRotationDirection %@ = %@"
+ "d32@0:8@16d24"
+ "dateWithTimeIntervalSinceNow:"
+ "deviceFlags %@: %@ %@"
+ "deviceType %s = %s"
+ "devicesMatchingPropertiesOn:exactMatch:completionHandler:"
+ "df970112-e36f-4b5e-a9af-02a16d9a1400"
+ "df970212-e36f-4b5e-a9af-02a16d9a1400"
+ "df970312-e36f-4b5e-a9af-02a16d9a1400"
+ "df970412-e36f-4b5e-a9af-02a16d9a1400"
+ "disconnectCIS:"
+ "disconnectCISPeripheral:"
+ "discoveryFlags %@: %@ %@"
+ "doubleTapActionLeft %s = %s"
+ "doubleTapActionRight %s = %s"
+ "doubleTapCapability %s = %s"
+ "dsActionFlags %@: %@ %@"
+ "dsInfoVehicleState %s = %s"
+ "dtCA"
+ "dynamicPresets"
+ "ecCA"
+ "enableAdvertisingWithPowerAssertion"
+ "enableEPAForAdvertisement"
+ "enableObjectLocatorResponseOnAdvertisingInstance"
+ "enabled"
+ "endCallCapability %s = %s"
+ "endCallConfig %@ = %@"
+ "event"
+ "eventType"
+ "excessiveMs"
+ "famC"
+ "familyCode"
+ "finalSummary"
+ "findMyCaseIdentifier %@ = %@"
+ "findMyGroupIdentifier %@ = %@"
+ "firmwareVersion %@ = %@"
+ "fmPS"
+ "frequencyBand %s = %s"
+ "gAsM"
+ "gDvE"
+ "gUbP"
+ "gameControllerAutoSwitchMode"
+ "gameControllerUSBBluetoothPairing"
+ "gapaFlags %@: %@ %@"
+ "getRangingTones:"
+ "gfpModelID %s = %s"
+ "grID"
+ "groupID"
+ "h1CN"
+ "h1CV"
+ "h1Ca"
+ "h1DI"
+ "h1Fl"
+ "h1SH"
+ "h1SN"
+ "h2AI"
+ "h2AT"
+ "h2II"
+ "h2SN"
+ "h2Va"
+ "handleActivePresetUpdated:"
+ "handleCSProcedureEventForDeviceMsg:"
+ "handleConnectCISComplete:"
+ "handleConnectCISPeripheralComplete:"
+ "handleConnectLEAudioComplete:"
+ "handleDisconnectCISComplete:"
+ "handleDisconnectCISPeripheralComplete:"
+ "handleFeaturesUpdated:"
+ "handleLEAudioActivePresetUpdated, %@"
+ "handleLEAudioActivePresetUpdated:"
+ "handleLEAudioConnected:"
+ "handleLEAudioEvents:"
+ "handleLEAudioHearingAidFeaturesUpdated, %@"
+ "handleLEAudioHearingAidFeaturesUpdated:"
+ "handleLEAudioMicrophoneGainUpdated, %@"
+ "handleLEAudioMicrophoneGainUpdated:"
+ "handleLEAudioMicrophoneMuteUpdated, %@"
+ "handleLEAudioMicrophoneMuteUpdated:"
+ "handleLEAudioMsg:"
+ "handleLEAudioMsg:args:"
+ "handleLEAudioPresetNameUpdated:"
+ "handleLEAudioPresetUpdated, size:%d, %@, %@, %@"
+ "handleLEAudioPresetUpdated:"
+ "handleLEAudioSessionEvents:"
+ "handleLEAudioVolumeGainUpdated, %@"
+ "handleLEAudioVolumeGainUpdated:"
+ "handleLEAudioVolumeMuteUpdated, %@"
+ "handleLEAudioVolumeMuteUpdated:"
+ "handleLEAudioVolumeOffsetUpdated, %@"
+ "handleLEAudioVolumeOffsetUpdated:"
+ "handleLEAudioVolumeUpdated, %@"
+ "handleLEAudioVolumeUpdated:"
+ "handleLEAudioXpcInterrupted"
+ "handleLEAudioXpcInvalid"
+ "handleMicrophoneGainUpdated:"
+ "handleMicrophoneMuteUpdated:"
+ "handlePresetNameUpdated:"
+ "handlePresetsUpdated:"
+ "handleRemoveCIGComplete:"
+ "handleSessionCompleted"
+ "handleSessionCompleted:"
+ "handleSessionMicrophoneGainUpdated - %@"
+ "handleSessionMicrophoneGainUpdated:"
+ "handleSessionMicrophoneMuteUpdated - %@"
+ "handleSessionMicrophoneMuteUpdated:"
+ "handleSessionVolumeMuteUpdated - %@"
+ "handleSessionVolumeMuteUpdated:"
+ "handleSessionVolumeOffsetUpdated - %@"
+ "handleSessionVolumeOffsetUpdated:"
+ "handleSessionVolumeUpdated - %@"
+ "handleSessionVolumeUpdated:"
+ "handleSetupCIGComplete"
+ "handleSetupCIGComplete:"
+ "handleVolumeInputGainUpdated:"
+ "handleVolumeMuteUpdated:"
+ "handleVolumeOffsetUpdated:"
+ "handleVolumeUpdated:"
+ "hasAllComponents"
+ "hearingAidSupport %s = %s"
+ "hearingAidType"
+ "heySiriDeviceClass %s = %s"
+ "heySiriProductType %s = %s"
+ "homeKitV1Flags %@: %@ %@"
+ "identifier %@ = %@"
+ "idsDeviceID %@ = %@"
+ "independentPresets"
+ "initCISCentral"
+ "initCISPeripheral:completion:"
+ "initWithError:withError:"
+ "initWithEventType:"
+ "initWithEventType:withError:"
+ "initWithInfo:withSessionId:withState:withCoordIds:withLocation:"
+ "initWithInfo:withSize:"
+ "initWithPowerSourceDetails:internalFlags:"
+ "initWithSession:"
+ "initWithValue:withValue:"
+ "initWithValues:withProperty:withName:"
+ "injectAOPBufAdv count:%lu"
+ "injectAOPBufAdv no advertisements"
+ "injectAOPBufAdv:"
+ "instance: %@"
+ "int64ValueSafe"
+ "interval %hu = %hu"
+ "invalidateComponentWithPartID:"
+ "isAggregateComponent"
+ "isAvailable"
+ "isEqualToArray:"
+ "isEqualToData:"
+ "isEqualToDevice:exactMatch:"
+ "isEqualToDictionary:"
+ "isLowerThanAgeLimit:compareTimestamp:"
+ "isWritable"
+ "kCBAdvDataAppleAdvDataPerType"
+ "kCBConnectOptionGetLESynchronizationEvent"
+ "kCBGetControllerBTClockCEOffset"
+ "kCBGetControllerBTClockConnectionInterval"
+ "kCBGetControllerBTClockConnectionIntervalMicroSec"
+ "kCBGetControllerBTClockExceptionStatus"
+ "kCBGetControllerBTClockHostTime"
+ "kCBGetRangeOptionRunProcedure"
+ "kCBManagerSessionIsExtension"
+ "kCBMsgArgAddExtendedProperties"
+ "kCBMsgArgLEAudioAudioInputOpcode"
+ "kCBMsgArgLEAudioAudioInputType"
+ "kCBMsgArgLEAudioClient"
+ "kCBMsgArgLEAudioCoordinatedSetIds"
+ "kCBMsgArgLEAudioCoordinatedSetSize"
+ "kCBMsgArgLEAudioDevicePresetIndexes"
+ "kCBMsgArgLEAudioDevicePresetNames"
+ "kCBMsgArgLEAudioDevicePresetProperties"
+ "kCBMsgArgLEAudioDeviceUUID"
+ "kCBMsgArgLEAudioHearingAidDynamic"
+ "kCBMsgArgLEAudioHearingAidIndependent"
+ "kCBMsgArgLEAudioHearingAidSyncSupported"
+ "kCBMsgArgLEAudioHearingAidType"
+ "kCBMsgArgLEAudioHearingAidWritable"
+ "kCBMsgArgLEAudioLocation"
+ "kCBMsgArgLEAudioMicrophoneGain"
+ "kCBMsgArgLEAudioMicrophoneMuteState"
+ "kCBMsgArgLEAudioPresetIndex"
+ "kCBMsgArgLEAudioPresetName"
+ "kCBMsgArgLEAudioPresetType"
+ "kCBMsgArgLEAudioServiceID"
+ "kCBMsgArgLEAudioSessionID"
+ "kCBMsgArgLEAudioVolume"
+ "kCBMsgArgLEAudioVolumeGain"
+ "kCBMsgArgLEAudioVolumeMuteState"
+ "kCBMsgArgLEAudioVolumeOffset"
+ "kCBMsgChangeSessionMicrophoneGain"
+ "kCBMsgChangeSessionMicrophoneMuteState"
+ "kCBMsgChangeSessionVolume"
+ "kCBMsgChangeSessionVolumeMuteState"
+ "kCBMsgChangeSessionVolumeOffset"
+ "kCBMsgLEAudioActivePresetUpdated"
+ "kCBMsgLEAudioHearingAidFeaturesUpdated"
+ "kCBMsgLEAudioMicrophoneGainUpdated"
+ "kCBMsgLEAudioMicrophoneMuteUpdated"
+ "kCBMsgLEAudioPresetNameUpdated"
+ "kCBMsgLEAudioReadPresetUpdated"
+ "kCBMsgLEAudioRegister"
+ "kCBMsgLEAudioSessionCompleted"
+ "kCBMsgLEAudioSessionMicrophoneGainUpdated"
+ "kCBMsgLEAudioSessionMicrophoneMuteUpdated"
+ "kCBMsgLEAudioSessionVolumeMuteUpdated"
+ "kCBMsgLEAudioSessionVolumeOffsetUpdated"
+ "kCBMsgLEAudioSessionVolumeUpdated"
+ "kCBMsgLEAudioUnregistered"
+ "kCBMsgLEAudioVolumeInputGainUpdated"
+ "kCBMsgLEAudioVolumeMuteUpdated"
+ "kCBMsgLEAudioVolumeOffsetUpdated"
+ "kCBMsgLEAudioVolumeUpdated"
+ "kCBMsgReadPresets"
+ "kCBMsgSetActivePreset"
+ "kCBMsgSetMicrophoneMute"
+ "kCBMsgSetVolume"
+ "kCBMsgSetVolumeMute"
+ "kCBMsgSetVolumeOffSet"
+ "kCBMsgWriteMicrophoneAudioInput"
+ "kCBMsgWritePresetName"
+ "kCBMsgWriteVolumeAudioInput"
+ "leAdvName %@ = %@"
+ "leAudioEventHandler"
+ "listOfClients"
+ "listeningMode %s = %s"
+ "listeningModeConfigs %@ = %@"
+ "location"
+ "locations"
+ "lowWarnLevel"
+ "lwLv"
+ "maxAge"
+ "maxAgeForDiscovery %d, currentTimestampUsec %llu maxTimestampUsec %llu inCompareTimestamp %llu"
+ "maxCapacity"
+ "memberRank"
+ "mfgData"
+ "microphoneMode %s = %s"
+ "missedReads"
+ "model %@ = %@"
+ "modelUser %@ = %@"
+ "mspAddressData %@ = %@"
+ "mspDeviceClass %u = %u"
+ "mspDisplayName %@ = %@"
+ "mspSubScenario %s = %s"
+ "muteControlCapability %s = %s"
+ "muteControlConfig %@ = %@"
+ "mxAg"
+ "mxCp"
+ "n2AI"
+ "n2AT"
+ "n2DF"
+ "n2ED"
+ "n2EF"
+ "n2Fl"
+ "nATa"
+ "naAT"
+ "naFl"
+ "naTD"
+ "naTy"
+ "name %@ = %@"
+ "nant"
+ "nb2FT"
+ "nb2FT: <%@> -> <%@>"
+ "nearbyActionDeviceClass %u = %u"
+ "nearbyActionFlags %@: %@ %@"
+ "nearbyActionNoWakeType %s = %s"
+ "nearbyActionType %s = %s"
+ "nearbyActionV2Flags %@: %@ %@"
+ "nearbyActionV2Type %s = %s"
+ "nearbyInfoFlags %@: %@ %@"
+ "nearbyInfoStatusType %s = %s"
+ "nearbyInfoV2Flags %@: %@ %@"
+ "nearbyInfoV2InvitationRouteType %s = %s"
+ "nearbyInfoV2InvitationTypes %@: %@ %@"
+ "nearbyInfoV2NearbyFaceTimeData"
+ "nearbyInfoV2NearbyFaceTimeEncryptedData"
+ "niAT"
+ "niIF"
+ "objectDiscoveryBatteryState %s = %s"
+ "objectDiscoveryMode %s = %s"
+ "objectDiscoveryNearOwnerID %@ = %@"
+ "objectDiscoveryProductID %s = %s"
+ "options != nil"
+ "osBP"
+ "osBS"
+ "osCC"
+ "osFC"
+ "osFl"
+ "osMe"
+ "pTmp"
+ "pTyp"
+ "partID"
+ "partName"
+ "peerStatusFlag %@: %@ %@"
+ "percentile %.2f, rankIntegral %.2f, rankFraction %.2f, elementValue %.2f, element_+1_Value %.2f"
+ "peripheral:didCompleteChannelSoundingProcedure:error:"
+ "placementMode %s = %s"
+ "powerSourceMock"
+ "preflight ext:%d userAuth:%llu reason:%llu response:%d"
+ "present"
+ "presetIndex"
+ "presetName"
+ "presetResults"
+ "presetSyncSupported"
+ "primaryBudSide %s = %s"
+ "primaryPlacement %s = %s"
+ "productID %s = %s"
+ "productName %@ = %@"
+ "proximityPairingOtherBudProductID %s = %s"
+ "proximityPairingPrimaryPlacement %s = %s"
+ "proximityPairingProductID %s = %s"
+ "proximityPairingSecondaryPlacement %s = %s"
+ "proximityPairingSubType %s = %s"
+ "proximityServiceCategory %s = %s"
+ "proximityServiceClassicAddress %@ = %@"
+ "proximityServiceFlags %@: %@ %@"
+ "proximityServicePayload"
+ "proximityServiceSubType %s = %s"
+ "proximityServiceVendorID %s = %s"
+ "proximityServiceVersion %u = %u"
+ "psDA"
+ "psID"
+ "psPr"
+ "psVE"
+ "ptID"
+ "ptNm"
+ "publish"
+ "pxSP"
+ "pxSS"
+ "q24@?0@8@16"
+ "rAdv"
+ "randomData"
+ "readPresets:"
+ "registerLEAudioClient"
+ "releaseSource"
+ "removeBatteryInfo"
+ "removeCIG:completion:"
+ "removeCIGCompletion"
+ "removeFlags"
+ "respondToCISConnectionRequest:"
+ "retrieveConnectedLEAudioPeripheralIdentifiers"
+ "secondaryPlacement %s = %s"
+ "selectiveSpeechListeningCapability %@ = %@"
+ "selectiveSpeechListeningConfig %@ = %@"
+ "sendLEAudioMsg:args:completion:"
+ "serialNumber %@ = %@"
+ "serialNumberLeft %@ = %@"
+ "serialNumberRight %@ = %@"
+ "sessionInfo"
+ "sessionState"
+ "setAccessoryCategory:"
+ "setAccessoryID:"
+ "setActivePreset:"
+ "setActivePreset:OptionalPresetIndex:withResponse:"
+ "setAddExtendedProperties:"
+ "setAdvDataPerType:"
+ "setAdvInstanceType:"
+ "setAdvInterval:"
+ "setAirplayTargetIPv6:"
+ "setBatteryInfo:"
+ "setBufferedAdvConfigsForAOP:"
+ "setBufferedConfigsForAOP:"
+ "setCisConnectEvent:"
+ "setCisDisconnectEvent:"
+ "setCisPeripheralConnectEvent:"
+ "setCisPeripheralDisconnectEvent:"
+ "setCompletionHandler:"
+ "setConnectedIdentifiers:"
+ "setEnableAdvertisingWithPowerAssertion:"
+ "setEnableEPAForAdvertisement:"
+ "setEnableObjectLocatorResponseOnAdvertisingInstance:"
+ "setEvent:"
+ "setExcessiveMs:"
+ "setFamilyCode:"
+ "setFinalSummary:"
+ "setGameControllerAutoSwitchMode:"
+ "setGameControllerUSBBluetoothPairing:"
+ "setGroupID:"
+ "setLEAudioDeviceType:"
+ "setLEAudioLocation:"
+ "setLeAudioEventHandler:"
+ "setListOfClients:"
+ "setLowWarnLevel:"
+ "setMaxAge:"
+ "setMaxCapacity:"
+ "setMemberRank:"
+ "setMfgData:"
+ "setMicrophoneMute:withResponse:"
+ "setMicrophoneMuteStateForSession:withMicMuteState:withResponse:"
+ "setMissedReads:"
+ "setName"
+ "setNearbyInfoV2NearbyFaceTimeData:"
+ "setNearbyInfoV2NearbyFaceTimeEncryptedData:"
+ "setObjectSetupBatteryPerformance:"
+ "setObjectSetupBatteryState:"
+ "setObjectSetupColorCode:"
+ "setObjectSetupFlags:"
+ "setObjectSetupFontCode:"
+ "setObjectSetupMessage:"
+ "setP50:"
+ "setP50Max:"
+ "setP90:"
+ "setP90Max:"
+ "setP95:"
+ "setP95Max:"
+ "setP99:"
+ "setP99Max:"
+ "setPartID:"
+ "setPartName:"
+ "setPowerSourceMock:"
+ "setPresent:"
+ "setPresetResults:"
+ "setProximityServicePayload:"
+ "setRandomData:"
+ "setRemoveCIGCompletion:"
+ "setSessionInfo:"
+ "setSetName:"
+ "setSetSize:"
+ "setSetupCIGCompletion:"
+ "setSize"
+ "setSlideWindowSec:"
+ "setSourceID:"
+ "setStopOnAdvertisingAddressChange:"
+ "setStream:"
+ "setTemperature:"
+ "setTransportType:"
+ "setUpdateHandler:"
+ "setUpdatedValue:"
+ "setVolume:withResponse:"
+ "setVolumeMute:withResponse:"
+ "setVolumeOffSet:withOffSetValue:withResponse:"
+ "setWiProxUpdateTimestamp:"
+ "setupCIG:completion:"
+ "setupCIGCompletion"
+ "siID"
+ "siUI"
+ "slideWindowSec"
+ "smartRoutingMode %s = %s"
+ "sortUsingComparator:"
+ "sourceID"
+ "spatialAudioMode %s = %s"
+ "spatialInteractionFlags %@: %@ %@"
+ "startLEAudioXPC"
+ "startSecurityRequest"
+ "stopOnAdvertisingAddressChange"
+ "stream"
+ "supportedServices %@: %@ %@"
+ "temperature"
+ "tipiConnectionStatus %s = %s"
+ "tipiState %@ = %@"
+ "transportType"
+ "txAddressData %@ = %@"
+ "type %d rssiThreshold %d maxAge %d"
+ "unEv"
+ "unRe"
+ "updateHandler"
+ "updatePartID"
+ "updateWithCBPowerSource:"
+ "updatedValue"
+ "userNotificationEvent:completion:"
+ "v28@0:8C16@?20"
+ "v32@0:8@\"CBUserNotificationRequest\"16@?<v@?@\"NSError\">24"
+ "v32@0:8I16s20@?24"
+ "v32@?0@\"NSNumber\"8@\"CBPowerSource\"16^B24"
+ "v36@0:8@16B24@?28"
+ "v36@0:8@16f24@?28"
+ "v36@0:8C16@20@?28"
+ "v36@0:8q16C24@?28"
+ "v40@0:8@16C24c28@?32"
+ "v40@0:8@16I24s28@?32"
+ "v40@0:8@16q24@?32"
+ "v40@0:8q16C24c28@?32"
+ "v60@0:8@16B24Q28@36Q44Q52"
+ "vendorID %s = %s"
+ "vendorIDSource %s = %s"
+ "wiProxUpdateTimestamp"
+ "writablePresets"
+ "writeMicrophoneAudioInput:forAudioInputType:withOptionalGain:withResponse:"
+ "writePresetName:withName:withResponse:"
+ "writeVolumeAudioInput:forAudioInputType:withOptionalGain:withResponse:"
+ "{?=\"didUpdateName\"b1\"didModifyServices\"b1\"didReadRSSI\"b1\"didUpdateRSSI\"b1\"didDiscoverServices\"b1\"didDiscoverIncludedServices\"b1\"didDiscoverCharacteristics\"b1\"didUpdateCharacteristicValue\"b1\"didWriteCharacteristicValue\"b1\"didNotifyCharacteristicValue\"b1\"didDiscoverDescriptors\"b1\"didUpdateDescriptorValue\"b1\"didWriteDescriptorValue\"b1\"didReceiveTimeSync\"b1\"didReceiveChannelSoundingProcedure\"b1\"didOpenL2CAPChannel\"b1\"didCloseL2CAPChannel\"b1}"
+ "{?=\"willRestoreState\"b1\"didDiscoverPeripheral\"b1\"didConnectPeripheral\"b1\"didFailToConnectPeripheral\"b1\"didDisconnectPeripheral\"b1\"didDisconnectPeripheralWithTimestamp\"b1\"didUpdatePeripheralConnectionState\"b1\"didFindPeripheral\"b1\"didLosePeripheral\"b1\"didLoseZone\"b1\"didUpdateConnectionParameters\"b1\"connectionEventDidOccur\"b1\"didSendBytesToPeripheralWithError\"b1\"didReceiveDataFromPeripheral\"b1\"didDiscoverMultiplePeripherals\"b1\"didUpdateANCSAuthorizationForPeripheral\"b1\"canSendDataToPeripheral\"b1\"didFailToStartScanWithError\"b1\"didUpdateControllerBTClockForPeripheral\"b1\"didUpdateControllerBTClockDictForPeripheral\"b1\"didUpdateSynchronizationEventForPeripheral\"b1\"didUpdateMTUForPeripheral\"b1\"didUpdateRSSIStatisticsDetectionForPeripheral\"b1\"didUpdateUsageStatisticEvent\"b1\"didUpdatePhyStatisticEvent\"b1\"didChannelSoundingProcedureEvent\"b1\"didUpdateScanParams\"b1\"didUpdateFindMyPeripherals\"b1}"
- "'"
- ", ttRt %@"
- "AppleTV11,2"
- "CBAdvertiser: CID 0x%X"
- "CBConnection: Peer %@"
- "CBController, CID 0x%X"
- "CBDiscovery _typeToRssiThresholds set without Discovery types being set, _typeToRssiThresholds might not be sent to AOP"
- "CBDiscovery, CID 0x%X"
- "CnS"
- "Device1,8221"
- "Packet TS 0x%016llX, Actual %llu, Expected %llu, Delta %lld, ErrorRate %.2f%%, Interval %.3f ms, MaxInterval %.3f ms, RSSI %d"
- "T@\"NSArray\",C,N,V_spatialInteractionIdentifiers"
- "T@\"NSArray\",C,N,V_typeToRssiThresholds"
- "T@\"NSData\",C,N,V_bleAddressData"
- "T@\"NSData\",C,N,V_bleAdvertisementData"
- "T@\"NSData\",C,N,V_bleAppleManufacturerData"
- "T@\"NSData\",C,N,V_homeKitV1DeviceIDData"
- "T@\"NSData\",C,N,V_homeKitV2AccessoryIDData"
- "T@\"NSData\",C,N,V_homeKitV2AuthTagData"
- "T@\"NSData\",C,N,V_nearbyActionAuthTag"
- "T@\"NSData\",C,N,V_nearbyActionTargetAuthTag"
- "T@\"NSData\",C,N,V_nearbyAuthTag"
- "T@\"NSData\",C,N,V_nearbyInfoAuthTag"
- "T@\"NSData\",C,N,V_nearbyInfoV2EncryptedData"
- "T@\"NSData\",C,N,V_proximityServiceClassicAddress"
- "T@\"NSData\",C,N,V_proximityServiceData"
- "T@\"NSData\",C,N,V_proximityServiceSetupHash"
- "T@\"NSData\",C,N,V_spatialInteractionPresenceConfigData"
- "T@\"NSData\",C,N,V_spatialInteractionTokenData"
- "T@\"NSData\",C,N,V_spatialInteractionUWBConfigData"
- "T@\"NSDictionary\",C,N,V_spatialInteractionUserInfo"
- "T@\"NSString\",C,N,V_caseVersion"
- "T@\"NSString\",R,C,N,V_objectSetupFontCode"
- "T@\"NSString\",R,C,N,V_objectSetupMessage"
- "TC,N,V_adaptiveVolumeCapability"
- "TC,N,V_autoAncCapability"
- "TC,N,V_conversationDetectCapability"
- "TC,N,V_endCallCapability"
- "TC,N,V_homeKitV1CompatibleVersion"
- "TC,N,V_homeKitV1ConfigurationNumber"
- "TC,N,V_homeKitV1Flags"
- "TC,N,V_nearbyInfoV2EncryptedFlags"
- "TC,N,V_peerStatusFlag"
- "TC,N,V_proximityServiceCategory"
- "TC,N,V_proximityServiceFlags"
- "TC,N,V_proximityServiceVersion"
- "TC,N,V_spatialInteractionConfigFlags"
- "TC,N,V_spatialInteractionFlags"
- "TC,R,N,V_nearbyInfoV2InvitationRouteType"
- "TC,R,N,V_nearbyInfoV2InvitationTypes"
- "TC,R,N,V_objectSetupBatteryPerformance"
- "TC,R,N,V_objectSetupBatteryState"
- "TC,R,N,V_objectSetupColorCode"
- "TI,N,V_connectedServices"
- "TI,N,V_homeKitV1SetupHash"
- "TI,N,V_proximityServiceProductID"
- "TI,N,V_spatialInteractionPeerID"
- "TI,R,N,V_objectSetupFlags"
- "TQ,N,V_bleAdvertisementTimestampMachContinuous"
- "TQ,N,V_homeKitV2Value"
- "TS,N,V_batteryInfoCase"
- "TS,N,V_batteryInfoLeft"
- "TS,N,V_batteryInfoMain"
- "TS,N,V_batteryInfoRight"
- "TS,N,V_colorInfo"
- "TS,N,V_homeKitV1Category"
- "TS,N,V_homeKitV1StateNumber"
- "TS,N,V_homeKitV2InstanceID"
- "TS,N,V_homeKitV2StateNumber"
- "TS,N,V_proximityServicePSM"
- "TS,N,V_proximityServiceVendorID"
- "Tc,N,V_classicRSSI"
- "Tc,N,V_doubleTapCapability"
- "Tc,N,V_proximityServiceMeasuredPower"
- "Td,N,V_bleAdvertisementTimestamp"
- "Ti,N,V_audioStreamState"
- "Ti,N,V_bleChannel"
- "Ti,N,V_bleRSSI"
- "Unable to decrypt NearbyInfoV2 sensitive data"
- "_adaptiveVolumeCapability"
- "_audioStreamState"
- "_autoAncCapability"
- "_batteryInfoCase"
- "_batteryInfoLeft"
- "_batteryInfoMain"
- "_batteryInfoRight"
- "_bleAddressData"
- "_bleAdvertisementData"
- "_bleAdvertisementTimestamp"
- "_bleAdvertisementTimestampMachContinuous"
- "_bleAppleManufacturerData"
- "_bleChannel"
- "_bleRSSI"
- "_caseVersion"
- "_classicRSSI"
- "_colorInfo"
- "_connectedServices"
- "_conversationDetectCapability"
- "_endCallCapability"
- "_homeKitV1Category"
- "_homeKitV1CompatibleVersion"
- "_homeKitV1ConfigurationNumber"
- "_homeKitV1DeviceIDData"
- "_homeKitV1Flags"
- "_homeKitV1SetupHash"
- "_homeKitV1StateNumber"
- "_homeKitV2AccessoryIDData"
- "_homeKitV2AuthTagData"
- "_homeKitV2InstanceID"
- "_homeKitV2StateNumber"
- "_homeKitV2Value"
- "_nearbyActionAuthTag"
- "_nearbyActionTargetAuthTag"
- "_nearbyAuthTag"
- "_nearbyInfoAuthTag"
- "_nearbyInfoV2EncryptedData"
- "_nearbyInfoV2EncryptedFlags"
- "_objectSetupBatteryPerformance"
- "_objectSetupBatteryState"
- "_objectSetupColorCode"
- "_objectSetupFlags"
- "_objectSetupFontCode"
- "_objectSetupMessage"
- "_peerStatusFlag"
- "_proximityServiceCategory"
- "_proximityServiceClassicAddress"
- "_proximityServiceData"
- "_proximityServiceFlags"
- "_proximityServiceMeasuredPower"
- "_proximityServicePSM"
- "_proximityServiceProductID"
- "_proximityServiceSetupHash"
- "_proximityServiceVendorID"
- "_proximityServiceVersion"
- "_scanForPeripheralsWithServices:options:"
- "_spatialInteractionConfigFlags"
- "_spatialInteractionFlags"
- "_spatialInteractionIdentifiers"
- "_spatialInteractionPeerID"
- "_spatialInteractionPresenceConfigData"
- "_spatialInteractionTokenData"
- "_spatialInteractionUWBConfigData"
- "_spatialInteractionUserInfo"
- "_typeToRssiThresholds"
- "aStS"
- "avCp"
- "blAM"
- "blATM"
- "blAt"
- "blCh"
- "btV"
- "cdCp"
- "clrI"
- "dtCa"
- "eCCp"
- "hkAI"
- "hkAT"
- "hkCN"
- "hkCV"
- "hkCa"
- "hkDI"
- "hkFl"
- "hkII"
- "hkS1"
- "hkS2"
- "hkSH"
- "hkVa"
- "kCBScanOptionFilterIdentifier"
- "prSt"
- "psCa"
- "psDa"
- "psVs"
- "setTypeToRssiThresholds:"
- "siCl"
- "siId"
- "ttRt"
- "type %d rssiThreshold %d"
- "typeToRssiThreasholds: %@ -> %@"
- "typeToRssiThreshold"
- "typeToRssiThresholds"
- "{?=\"didUpdateName\"b1\"didModifyServices\"b1\"didReadRSSI\"b1\"didUpdateRSSI\"b1\"didDiscoverServices\"b1\"didDiscoverIncludedServices\"b1\"didDiscoverCharacteristics\"b1\"didUpdateCharacteristicValue\"b1\"didWriteCharacteristicValue\"b1\"didNotifyCharacteristicValue\"b1\"didDiscoverDescriptors\"b1\"didUpdateDescriptorValue\"b1\"didWriteDescriptorValue\"b1\"didReceiveTimeSync\"b1\"didOpenL2CAPChannel\"b1\"didCloseL2CAPChannel\"b1}"
- "{?=\"willRestoreState\"b1\"didDiscoverPeripheral\"b1\"didConnectPeripheral\"b1\"didFailToConnectPeripheral\"b1\"didDisconnectPeripheral\"b1\"didDisconnectPeripheralWithTimestamp\"b1\"didUpdatePeripheralConnectionState\"b1\"didFindPeripheral\"b1\"didLosePeripheral\"b1\"didLoseZone\"b1\"didUpdateConnectionParameters\"b1\"connectionEventDidOccur\"b1\"didSendBytesToPeripheralWithError\"b1\"didReceiveDataFromPeripheral\"b1\"didDiscoverMultiplePeripherals\"b1\"didUpdateANCSAuthorizationForPeripheral\"b1\"canSendDataToPeripheral\"b1\"didFailToStartScanWithError\"b1\"didUpdateControllerBTClockForPeripheral\"b1\"didUpdateControllerBTClockDictForPeripheral\"b1\"didUpdateMTUForPeripheral\"b1\"didUpdateRSSIStatisticsDetectionForPeripheral\"b1\"didUpdateUsageStatisticEvent\"b1\"didUpdatePhyStatisticEvent\"b1\"didChannelSoundingProcedureEvent\"b1\"didUpdateScanParams\"b1\"didUpdateFindMyPeripherals\"b1}"

```
