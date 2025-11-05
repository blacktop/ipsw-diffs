## HearingModeService

> `/System/Library/PrivateFrameworks/HearingModeService.framework/Versions/A/HearingModeService`

```diff

-23.1.0.0.0
-  __TEXT.__text: 0x13ecc
+24.26.0.0.0
+  __TEXT.__text: 0x14894
   __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x11dc
+  __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x417a
-  __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__unwind_info: 0x430
   __TEXT.__objc_classname: 0x127
   __TEXT.__objc_methname: 0x4f1f
   __TEXT.__objc_methtype: 0x886

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe38
+  __DATA_CONST.__objc_selrefs: 0xf48
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x490
   __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x2ef0
+  __AUTH_CONST.__objc_const: 0x2950
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8ADC5F6-1B6B-3E4A-9989-CF63D33E2471
-  Functions: 447
-  Symbols:   1134
+  UUID: AD95AE6F-10B9-3B00-877A-DF4484C9C95E
+  Functions: 552
+  Symbols:   1243
   CStrings:  1599
 
Symbols:
+ -[HMAccessoryManager _activateWithBluetoothDeviceAddress:].cold.1
+ -[HMAccessoryManager _discoveryAccessory].cold.1
+ -[HMAccessoryManager _discoveryAccessory].cold.2
+ -[HMAccessoryManager _triggerOnDemandFaultCheckWithCompletionHandler:].cold.1
+ -[HMAccessoryManager _writeHearingModeSetting:].cold.1
+ -[HMAccessoryManager centralManager:connectionEventDidOccur:forPeripheral:].cold.1
+ -[HMAccessoryManager centralManager:connectionEventDidOccur:forPeripheral:].cold.2
+ -[HMAccessoryManager centralManager:didConnectPeripheral:].cold.1
+ -[HMAccessoryManager centralManager:didConnectPeripheral:].cold.2
+ -[HMAccessoryManager centralManager:didDisconnectPeripheral:error:].cold.1
+ -[HMAccessoryManager centralManager:didDisconnectPeripheral:error:].cold.2
+ -[HMAccessoryManager centralManagerDidUpdateState:].cold.1
+ -[HMAccessoryManager init].cold.1
+ -[HMAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:].cold.1
+ -[HMAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:].cold.2
+ -[HMAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:].cold.3
+ -[HMAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:].cold.4
+ -[HMAccessoryManager peripheral:didDiscoverServices:].cold.1
+ -[HMAccessoryManager peripheral:didUpdateValueForCharacteristic:error:].cold.1
+ -[HMAccessoryManager peripheral:didUpdateValueForCharacteristic:error:].cold.2
+ -[HMDeviceConfigurations needsUpdateToAHPSConnectionManagerForDevice:].cold.1
+ -[HMDeviceConfigurations needsUpdateToAHPSConnectionManagerForDevice:].cold.2
+ -[HMDeviceConfigurations needsUpdateToAHPSConnectionManagerForDevice:].cold.3
+ -[HMDeviceConfigurations needsUpdateToAHPSConnectionManagerForDevice:].cold.4
+ -[HMDeviceConfigurations needsUpdateToAHPSConnectionManagerForDevice:].cold.5
+ -[HMDeviceConfigurations needsUpdateToDeviceManagerForDevice:].cold.1
+ -[HMDeviceConfigurations needsUpdateToDeviceManagerForDevice:].cold.2
+ -[HMDeviceConfigurations needsUpdateToDeviceManagerForDevice:].cold.3
+ -[HMDeviceConfigurations needsUpdateToDeviceManagerForDevice:].cold.4
+ -[HMDeviceConfigurations needsUpdateToDeviceManagerForDevice:].cold.5
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.1
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.2
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.3
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.4
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.5
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.6
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.7
+ -[HMDeviceConfigurations needsUpdateToPMEConfigurationForDevice:].cold.8
+ -[HMDeviceConfigurations restoreConfigsFromCloudRecordIfNeeded:].cold.1
+ -[HMDeviceConfigurations restoreConfigsFromCloudRecordIfNeeded:].cold.2
+ -[HMDeviceConfigurations setEnableHearingAssistIfNeeded:].cold.1
+ -[HMDeviceDiagnosticRecord _isDate:lesserThanOrEqualToMonths:].cold.1
+ -[HMDeviceDiagnosticRecord _prefsResetOcclusionStatsForFeatureID:type:].cold.1
+ -[HMDeviceDiagnosticRecord occlusionIndicationShownForFeatureID:type:action:].cold.1
+ -[HMDeviceDiagnosticRecord updateWithDiagnosticData:].cold.1
+ -[HMDeviceRecord getOcclusionResultForFeatureID:].cold.1
+ -[HMDeviceRecord setOcclusionResult:forFeatureID:].cold.1
+ -[HMDeviceRecord updateWithPMEConfigData:].cold.1
+ -[HMEnrollmentService _accessoryReceivedHearingModeSettings:].cold.1
+ -[HMEnrollmentService _accessoryReceivedHearingModeSettings:].cold.2
+ -[HMEnrollmentService _accessoryReceivedHearingModeSettings:].cold.3
+ -[HMEnrollmentService _accessoryReceivedHearingModeSettings:].cold.4
+ -[HMEnrollmentService _accessorySendHearingModeSettings].cold.1
+ -[HMEnrollmentService _accessorySendHearingModeSettings].cold.2
+ -[HMEnrollmentService _accessorySendHearingModeSettings].cold.3
+ -[HMEnrollmentService _activate].cold.1
+ -[HMEnrollmentService _activate].cold.2
+ -[HMEnrollmentService _audiogramsQueryHandler:results:error:].cold.1
+ -[HMEnrollmentService _audiogramsQueryHandler:results:error:].cold.2
+ -[HMEnrollmentService _getHearingModeSettings:fromAudiogram:].cold.1
+ -[HMEnrollmentService _isAudiogramValid:].cold.1
+ -[HMEnrollmentService _startAudiogramQuery].cold.1
+ -[HMServiceClient _activate].cold.1
+ -[HMServiceClient _ensureXPCStarted].cold.1
+ -[HMServiceClient _interrupted].cold.1
+ -[HMServiceClient _invalidated].cold.1
+ -[HMServiceClient _invalidated].cold.2
+ -[HMServiceClient _reportError:].cold.1
+ -[HMServiceClient clientHMDeviceDiagnosticRecordFound:].cold.1
+ -[HMServiceClient clientHMDeviceRecordChanged:].cold.1
+ -[HMServiceClient isSystemContext].cold.1
+ HMXPCGetNextClientID.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __28-[HMServiceClient _activate]_block_invoke.13.cold.1
+ __28-[HMServiceClient _activate]_block_invoke.13.cold.2
+ __28-[HMServiceClient _activate]_block_invoke.cold.1
+ __29-[HMServiceClient invalidate]_block_invoke.cold.1
+ __32-[HMEnrollmentService _activate]_block_invoke_2.cold.1
+ __41-[HMAccessoryManager _discoveryAccessory]_block_invoke.cold.1
+ __41-[HMEnrollmentService _isAudiogramValid:]_block_invoke.cold.1
+ __42-[HMServiceClient activateWithCompletion:]_block_invoke.cold.1
+ __47-[HMAccessoryManager _writeHearingModeSetting:]_block_invoke_2.cold.1
+ __53-[HMAccessoryManager peripheral:didDiscoverServices:]_block_invoke.cold.1
+ __56-[HMServiceClient triggerFetchAudiogramsWithCompletion:]_block_invoke.cold.1
+ __56-[HMServiceClient triggerFetchAudiogramsWithCompletion:]_block_invoke_3.cold.1
+ __60-[HMServiceClient modifyDeviceConfig:identifier:completion:]_block_invoke_2.cold.1
+ __60-[HMServiceClient modifyDeviceConfig:identifier:completion:]_block_invoke_3.cold.1
+ __61-[HMDeviceRecord invokePendingOcclusionCompletionsWithError:]_block_invoke.cold.1
+ __70-[HMAccessoryManager _triggerOnDemandFaultCheckWithCompletionHandler:]_block_invoke.cold.1
+ __70-[HMAccessoryManager _triggerOnDemandFaultCheckWithCompletionHandler:]_block_invoke_2.cold.1
+ __76-[HMAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke_2.cold.1
+ __80-[HMServiceClient fetchOcclusionResultForDeviceIdentifier:featureID:completion:]_block_invoke.67.cold.1
+ __80-[HMServiceClient fetchOcclusionResultForDeviceIdentifier:featureID:completion:]_block_invoke.cold.1
+ __80-[HMServiceClient triggerOnDemandDiagnosticCheckForDeviceIdentifier:completion:]_block_invoke.cold.1
+ __80-[HMServiceClient triggerOnDemandDiagnosticCheckForDeviceIdentifier:completion:]_block_invoke_3.cold.1

```
