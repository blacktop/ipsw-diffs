## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/Versions/A/HearingModeService_Private`

```diff

-23.1.0.0.0
-  __TEXT.__text: 0x1165c
+24.26.0.0.0
+  __TEXT.__text: 0x12438
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x82c
+  __TEXT.__objc_methlist: 0xb2c
   __TEXT.__const: 0x86
-  __TEXT.__gcc_except_tab: 0x4d8
+  __TEXT.__gcc_except_tab: 0x4c4
   __TEXT.__cstring: 0x45ba
-  __TEXT.__unwind_info: 0x468
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_classname: 0x135
   __TEXT.__objc_methname: 0x30ff
   __TEXT.__objc_methtype: 0x823

   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc20
+  __DATA_CONST.__objc_selrefs: 0xd38
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x860
   __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x18e8
+  __AUTH_CONST.__objc_const: 0x1360
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0xb0

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/Versions/A/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F071B37-1A22-3F6B-AD6B-B613DDFF390C
-  Functions: 278
-  Symbols:   964
+  UUID: FE13A3AE-DEC4-363B-942D-B398665DC0E9
+  Functions: 414
+  Symbols:   1102
   CStrings:  987
 
Symbols:
+ +[HMDeviceManager sharedInstance].cold.1
+ +[HMHealthKitUtilities sharedInstance].cold.1
+ +[HMOcclusionNotification sharedInstance].cold.1
+ +[HMServiceDaemon sharedHMServiceDaemon].cold.1
+ -[HMDeviceAHPSConnectionManager _activateWithBluetoothDeviceUUID:].cold.1
+ -[HMDeviceAHPSConnectionManager _centralManagerEnsureStarted].cold.1
+ -[HMDeviceAHPSConnectionManager _centralManagerEnsureStopped].cold.1
+ -[HMDeviceAHPSConnectionManager _discoverAccessory].cold.1
+ -[HMDeviceAHPSConnectionManager _discoverAccessory].cold.2
+ -[HMDeviceAHPSConnectionManager _triggerOnDemandDiagnosticCheckWithCompletionHandler:].cold.1
+ -[HMDeviceAHPSConnectionManager _writeHMSettingsConfigsData:completion:].cold.1
+ -[HMDeviceAHPSConnectionManager centralManager:connectionEventDidOccur:forPeripheral:].cold.1
+ -[HMDeviceAHPSConnectionManager centralManager:connectionEventDidOccur:forPeripheral:].cold.2
+ -[HMDeviceAHPSConnectionManager centralManager:didConnectPeripheral:].cold.1
+ -[HMDeviceAHPSConnectionManager centralManager:didConnectPeripheral:].cold.2
+ -[HMDeviceAHPSConnectionManager centralManager:didDisconnectPeripheral:error:].cold.1
+ -[HMDeviceAHPSConnectionManager centralManager:didDisconnectPeripheral:error:].cold.2
+ -[HMDeviceAHPSConnectionManager centralManagerDidUpdateState:].cold.1
+ -[HMDeviceAHPSConnectionManager peripheral:didDiscoverCharacteristicsForService:error:].cold.1
+ -[HMDeviceAHPSConnectionManager peripheral:didDiscoverCharacteristicsForService:error:].cold.2
+ -[HMDeviceAHPSConnectionManager peripheral:didDiscoverCharacteristicsForService:error:].cold.3
+ -[HMDeviceAHPSConnectionManager peripheral:didDiscoverCharacteristicsForService:error:].cold.4
+ -[HMDeviceAHPSConnectionManager peripheral:didDiscoverServices:].cold.1
+ -[HMDeviceAHPSConnectionManager peripheral:didUpdateValueForCharacteristic:error:].cold.1
+ -[HMDeviceAHPSConnectionManager peripheral:didUpdateValueForCharacteristic:error:].cold.2
+ -[HMDeviceAHPSConnectionManager peripheral:didUpdateValueForCharacteristic:error:].cold.3
+ -[HMDeviceAHPSConnectionManager peripheral:didUpdateValueForCharacteristic:error:].cold.4
+ -[HMDeviceManager _aaControllerEnsureStarted].cold.1
+ -[HMDeviceManager _accessoryDiscoveryEnsureStarted].cold.1
+ -[HMDeviceManager _activateAHPSConnectionForDevice:].cold.1
+ -[HMDeviceManager _activate].cold.1
+ -[HMDeviceManager _cloudServicesClientEnsureStopped].cold.1
+ -[HMDeviceManager _constructPMEConfigDataBytesForDevice:fromConfig:].cold.1
+ -[HMDeviceManager _deviceFound:].cold.1
+ -[HMDeviceManager _deviceFound:].cold.2
+ -[HMDeviceManager _deviceLost:].cold.1
+ -[HMDeviceManager _deviceLost:].cold.2
+ -[HMDeviceManager _deviceRescindHearingAssist:].cold.1
+ -[HMDeviceManager _deviceUpdateRegionStatus:].cold.1
+ -[HMDeviceManager _diagnosticDataReceived:identifier:isInternal:].cold.1
+ -[HMDeviceManager _diagnosticDataReceived:identifier:isInternal:].cold.2
+ -[HMDeviceManager _diagnosticDataReceived:identifier:isInternal:].cold.3
+ -[HMDeviceManager _fetchOcclusionResultForDeviceIdentifier:featureID:completion:].cold.1
+ -[HMDeviceManager _fetchOcclusionResultForDeviceIdentifier:featureID:completion:].cold.2
+ -[HMDeviceManager _fetchOcclusionResultForDeviceIdentifier:featureID:completion:].cold.3
+ -[HMDeviceManager _fetchOcclusionResultForDeviceIdentifier:featureID:completion:].cold.4
+ -[HMDeviceManager _hearingAidConfigDataReceived:identifier:].cold.1
+ -[HMDeviceManager _hearingAidConfigDataReceived:identifier:].cold.2
+ -[HMDeviceManager _hearingProtectionValueReceived:identifier:].cold.1
+ -[HMDeviceManager _invalidate].cold.1
+ -[HMDeviceManager _modifyDeviceConfiguration:identifier:completion:].cold.1
+ -[HMDeviceManager _performActionsOnRecordChange:].cold.1
+ -[HMDeviceManager _pmeConfigDataReceived:identifier:].cold.1
+ -[HMDeviceManager _pmeConfigDataReceived:identifier:].cold.2
+ -[HMDeviceManager _registerForInternalDistributedNotification].cold.1
+ -[HMDeviceManager _resetFaultCountForDevice:].cold.1
+ -[HMDeviceManager _resetFaultCountForDevice:].cold.2
+ -[HMDeviceManager _saveCloudRecordForDevice:withConfig:].cold.1
+ -[HMDeviceManager _saveCloudRecordForDevice:withConfig:].cold.2
+ -[HMDeviceManager _saveCloudRecordForDevice:withConfig:].cold.3
+ -[HMDeviceManager _sendConfigOverDeviceManager:identifier:completion:].cold.1
+ -[HMDeviceManager _sendConfigOverDeviceManager:identifier:completion:].cold.2
+ -[HMDeviceManager _sendConfigOverDeviceManager:identifier:completion:].cold.3
+ -[HMDeviceManager _sendConfigOverDeviceManager:identifier:completion:].cold.4
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.1
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.10
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.2
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.3
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.4
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.5
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.6
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.7
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.8
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.9
+ -[HMDeviceManager _sendPMEConfigOverAAController:identifier:completion:].cold.1
+ -[HMDeviceManager _sendPMEConfigOverAAController:identifier:completion:].cold.2
+ -[HMDeviceManager _triggerDiagnosticCheckForIdentifier:completion:].cold.1
+ -[HMDeviceManager _unregisterFromInternalDistributedNotification].cold.1
+ -[HMDeviceManager _updatePersonalAudioConfigForIdentifier:].cold.1
+ -[HMDeviceManager _updatePersonalAudioConfigForIdentifier:].cold.2
+ -[HMDeviceManager _updatePersonalAudioConfigForIdentifier:].cold.3
+ -[HMDeviceManager _updatePersonalAudioConfigForIdentifier:].cold.4
+ -[HMHealthKitUtilities _activate].cold.1
+ -[HMHealthKitUtilities _audiogramsQueryHandler:results:error:].cold.1
+ -[HMHealthKitUtilities _invalidate].cold.1
+ -[HMHealthKitUtilities _isAudiogramValid:].cold.1
+ -[HMHealthKitUtilities _startAudiogramQuery].cold.1
+ -[HMHealthKitUtilities getRegionSupportStatusForFeatureID:].cold.1
+ -[HMHealthKitUtilities updateHMSettingsStruct:fromAudiogram:].cold.1
+ -[HMOcclusionNotification _hasOcclusionNotificationsThresholdMet].cold.1
+ -[HMOcclusionNotification _showHearingProtectionOcclusionNotification:].cold.1
+ -[HMServiceDaemon _xpcConnectionInvalidated:].cold.1
+ -[HMServiceDaemon listener:shouldAcceptNewConnection:].cold.1
+ -[HMServiceXPCConnection _entitledAndReturnError:].cold.1
+ -[HMServiceXPCConnection xpcConnectionInvalidated].cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __27-[HMServiceDaemon activate]_block_invoke.cold.1
+ __39-[HMDeviceManager _updateCloudRecords:]_block_invoke.cold.1
+ __45-[HMDeviceManager _aaControllerEnsureStarted]_block_invoke.cold.1
+ __45-[HMDeviceManager _aaControllerEnsureStarted]_block_invoke_2.339.cold.1
+ __45-[HMDeviceManager _aaControllerEnsureStarted]_block_invoke_2.339.cold.2
+ __45-[HMDeviceManager _loadCloudRecordForDevice:]_block_invoke.cold.1
+ __45-[HMDeviceManager _loadCloudRecordForDevice:]_block_invoke.cold.2
+ __45-[HMDeviceManager _loadCloudRecordForDevice:]_block_invoke.cold.3
+ __45-[HMDeviceManager _loadCloudRecordForDevice:]_block_invoke.cold.4
+ __45-[HMDeviceManager _resetFaultCountForDevice:]_block_invoke.cold.1
+ __47-[HMDeviceManager _deviceRescindHearingAssist:]_block_invoke.cold.1
+ __51-[HMDeviceAHPSConnectionManager _discoverAccessory]_block_invoke.cold.1
+ __51-[HMDeviceManager _accessoryDiscoveryEnsureStarted]_block_invoke.307.cold.1
+ __51-[HMDeviceManager _accessoryDiscoveryEnsureStarted]_block_invoke.cold.1
+ __51-[HMDeviceManager _accessoryDiscoveryEnsureStarted]_block_invoke_2.310.cold.1
+ __51-[HMDeviceManager _accessoryDiscoveryEnsureStarted]_block_invoke_2.310.cold.2
+ __51-[HMDeviceManager _accessoryDiscoveryEnsureStarted]_block_invoke_2.cold.1
+ __52-[HMDeviceManager _cloudServicesClientEnsureStarted]_block_invoke.402.cold.1
+ __52-[HMDeviceManager _cloudServicesClientEnsureStarted]_block_invoke.402.cold.2
+ __52-[HMDeviceManager _cloudServicesClientEnsureStarted]_block_invoke.cold.1
+ __52-[HMDeviceManager _cloudServicesClientEnsureStarted]_block_invoke_2.cold.1
+ __52-[HMDeviceManager _distributedNotificationReceived:]_block_invoke.cold.1
+ __52-[HMDeviceManager _distributedNotificationReceived:]_block_invoke.cold.2
+ __61-[HMDeviceManager _deviceSetOffListeningModeAllowedIfNeeded:]_block_invoke.cold.1
+ __64-[HMDeviceAHPSConnectionManager peripheral:didDiscoverServices:]_block_invoke.cold.1
+ __66-[HMDeviceManager _checkForOcclusionInDiagnosticRecord:forDevice:]_block_invoke.cold.1
+ __68-[HMDeviceManager _modifyDeviceConfiguration:identifier:completion:]_block_invoke.cold.1
+ __70-[HMDeviceManager _sendConfigOverDeviceManager:identifier:completion:]_block_invoke.cold.1
+ __71-[HMOcclusionNotification _showHearingProtectionOcclusionNotification:]_block_invoke.cold.1
+ __72-[HMDeviceAHPSConnectionManager _writeHMSettingsConfigsData:completion:]_block_invoke_2.cold.1
+ __72-[HMDeviceManager _sendPMEConfigOverAAController:identifier:completion:]_block_invoke.cold.1
+ __72-[HMDeviceManager _sendPMEConfigOverAAController:identifier:completion:]_block_invoke.cold.2
+ __77-[HMDeviceManager _throttleUpdatesForHearingAidConfig:identifier:completion:]_block_invoke.cold.1
+ __86-[HMDeviceAHPSConnectionManager _triggerOnDemandDiagnosticCheckWithCompletionHandler:]_block_invoke_2.cold.1
+ __87-[HMDeviceAHPSConnectionManager peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke_2.cold.1

```
