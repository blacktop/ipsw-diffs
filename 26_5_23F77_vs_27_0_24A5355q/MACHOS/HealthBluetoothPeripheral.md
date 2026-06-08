## HealthBluetoothPeripheral

> `/System/Library/Health/Plugins/HealthBluetoothPeripheral.bundle/HealthBluetoothPeripheral`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0x3bd60
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0x5ba0
-  __TEXT.__objc_methlist: 0x3cec
+7027.0.52.2.6
+  __TEXT.__text: 0x3e7b8
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x6280
+  __TEXT.__objc_methlist: 0x3e44
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x2273
-  __TEXT.__oslogstring: 0x4599
-  __TEXT.__objc_classname: 0xb31
-  __TEXT.__objc_methname: 0x9224
-  __TEXT.__objc_methtype: 0x2b51
-  __TEXT.__gcc_except_tab: 0xb88
-  __TEXT.__unwind_info: 0x1010
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0x11c8
-  __DATA_CONST.__cfstring: 0x1f60
+  __TEXT.__cstring: 0x25e3
+  __TEXT.__oslogstring: 0x57dd
+  __TEXT.__objc_classname: 0xb5f
+  __TEXT.__objc_methname: 0x9b82
+  __TEXT.__objc_methtype: 0x2e57
+  __TEXT.__gcc_except_tab: 0xad0
+  __TEXT.__unwind_info: 0x1088
+  __DATA_CONST.__const: 0x1298
+  __DATA_CONST.__cfstring: 0x2260
   __DATA_CONST.__objc_classlist: 0x1b8
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_intobj: 0x600
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x7580
-  __DATA.__objc_selrefs: 0x2058
-  __DATA.__objc_ivar: 0x578
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0x438
+  __DATA.__objc_const: 0x77e8
+  __DATA.__objc_selrefs: 0x2260
+  __DATA.__objc_ivar: 0x5a4
   __DATA.__objc_data: 0x1130
-  __DATA.__data: 0x1160
+  __DATA.__data: 0x1280
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
+  - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DE6A81F-2A23-3E06-B54F-464F816E8C1D
-  Functions: 1626
-  Symbols:   407
-  CStrings:  2720
+  UUID: EAE9B200-0FCC-3191-9E42-628FC6C2B54D
+  Functions: 1701
+  Symbols:   434
+  CStrings:  2944
 
Symbols:
+ _HBPBluetoothPeripheralPluginIdentifier
+ _HBPConnectedGymPreferencesChanged
+ _HBPFitnessMachineMetricsCollectorDidChangeNotification
+ _HBPFitnessMachineServiceUUIDs_CrossTrainerDataCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_EurotasDataCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_EurotasDataServiceUUID
+ _HBPFitnessMachineServiceUUIDs_EurotasEnhancedFTMSCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_FeatureCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_IndoorBikeDataCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_ServiceUUID
+ _HBPFitnessMachineServiceUUIDs_StairClimberDataCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_StatusCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_StepClimberDataCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_TrainingStatusCharacteristicUUID
+ _HBPFitnessMachineServiceUUIDs_TreadmillDataCharacteristicUUID
+ _HBPHealthPeripheralAllPropertyNames
+ _HBPHealthPeripheralProfiles
+ _HBPHealthServiceClassForCBUUID
+ _HBPHealthServiceDiscoveryIdentifierInvalid
+ _HBPHealthServiceSessionIdentifierInvalid
+ _HBPServiceClassForProfile
+ _HBPWorkoutNotificationTerminalHandoffFieldDetected
+ _NSStringForRapportSchemaIdentifier
+ _OBJC_CLASS_$_BLSAssertion
+ _OBJC_CLASS_$_BLSDisableLowerGestureAttribute
+ _OBJC_CLASS_$_BLSDurationAttribute
+ _OBJC_CLASS_$_BLSForceActiveAttribute
+ _OBJC_CLASS_$_BLSPreventBacklightIdleAttribute
+ _OBJC_CLASS_$_HBPBatteryService
+ _OBJC_CLASS_$_HBPCrossTrainerData
+ _OBJC_CLASS_$_HBPDeviceInformationService
+ _OBJC_CLASS_$_HBPEnhancedFTMSData
+ _OBJC_CLASS_$_HBPEurotasData
+ _OBJC_CLASS_$_HBPEurotasService
+ _OBJC_CLASS_$_HBPFitnessMachineAnalyticsCollector
+ _OBJC_CLASS_$_HBPFitnessMachineCharacteristicDoubleField
+ _OBJC_CLASS_$_HBPFitnessMachineCharacteristicField
+ _OBJC_CLASS_$_HBPFitnessMachineCharacteristicInt16Field
+ _OBJC_CLASS_$_HBPFitnessMachineCharacteristicUInt16Field
+ _OBJC_CLASS_$_HBPFitnessMachineCharacteristicUInt24Field
+ _OBJC_CLASS_$_HBPFitnessMachineCharacteristicUInt8Field
+ _OBJC_CLASS_$_HBPFitnessMachineConnection
+ _OBJC_CLASS_$_HBPFitnessMachineConnectionInitiatorServer
+ _OBJC_CLASS_$_HBPFitnessMachineConnectionServer
+ _OBJC_CLASS_$_HBPFitnessMachineDataCharacteristicBase
+ _OBJC_CLASS_$_HBPFitnessMachineDataCollector
+ _OBJC_CLASS_$_HBPFitnessMachineDataProducer
+ _OBJC_CLASS_$_HBPFitnessMachineManager
+ _OBJC_CLASS_$_HBPFitnessMachineService
+ _OBJC_CLASS_$_HBPFitnessMachineSession
+ _OBJC_CLASS_$_HBPFitnessMachineSessionRecoveryConfiguration
+ _OBJC_CLASS_$_HBPFitnessMachineSimulatorSupport
+ _OBJC_CLASS_$_HBPFitnessMachineStatus
+ _OBJC_CLASS_$_HBPGymKitDataSource
+ _OBJC_CLASS_$_HBPGymKitMetricsDataSource
+ _OBJC_CLASS_$_HBPGymKitPairingManager
+ _OBJC_CLASS_$_HBPGymKitSettings
+ _OBJC_CLASS_$_HBPGymKitWorkoutAnalyticEvent
+ _OBJC_CLASS_$_HBPGymKitWorkoutSessionController
+ _OBJC_CLASS_$_HBPHealthBluetoothPeripheralPluginDaemonExtension
+ _OBJC_CLASS_$_HBPHealthPeripheral
+ _OBJC_CLASS_$_HBPHealthService
+ _OBJC_CLASS_$_HBPHealthServiceCharacteristic
+ _OBJC_CLASS_$_HBPHealthServiceManager
+ _OBJC_CLASS_$_HBPHealthServiceOOBInfo
+ _OBJC_CLASS_$_HBPHealthServicesServer
+ _OBJC_CLASS_$_HBPIdentifierTable
+ _OBJC_CLASS_$_HBPIndoorBikeData
+ _OBJC_CLASS_$_HBPNearFieldInterface
+ _OBJC_CLASS_$_HBPServiceConnectionManager
+ _OBJC_CLASS_$_HBPStairClimberData
+ _OBJC_CLASS_$_HBPStepClimberData
+ _OBJC_CLASS_$_HBPTreadmillData
+ _OBJC_CLASS_$_HBPUnknownHealthService
+ _OBJC_CLASS_$_HDNotificationManager
+ _OBJC_CLASS_$_HDRapportRequestIdentifier
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirements
+ _OBJC_CLASS_$_NPSDomainAccessor
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_SBSRemoteAlertActivationContext
+ _OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
+ _OBJC_CLASS_$_SBSRemoteAlertDefinition
+ _OBJC_CLASS_$_SBSRemoteAlertHandle
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNMutableNotificationSound
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$__HBPHealthServiceDataUpdate
+ _OBJC_METACLASS_$_HBPBatteryService
+ _OBJC_METACLASS_$_HBPCrossTrainerData
+ _OBJC_METACLASS_$_HBPDeviceInformationService
+ _OBJC_METACLASS_$_HBPEnhancedFTMSData
+ _OBJC_METACLASS_$_HBPEurotasData
+ _OBJC_METACLASS_$_HBPEurotasService
+ _OBJC_METACLASS_$_HBPFitnessMachineAnalyticsCollector
+ _OBJC_METACLASS_$_HBPFitnessMachineCharacteristicDoubleField
+ _OBJC_METACLASS_$_HBPFitnessMachineCharacteristicField
+ _OBJC_METACLASS_$_HBPFitnessMachineCharacteristicInt16Field
+ _OBJC_METACLASS_$_HBPFitnessMachineCharacteristicUInt16Field
+ _OBJC_METACLASS_$_HBPFitnessMachineCharacteristicUInt24Field
+ _OBJC_METACLASS_$_HBPFitnessMachineCharacteristicUInt8Field
+ _OBJC_METACLASS_$_HBPFitnessMachineConnection
+ _OBJC_METACLASS_$_HBPFitnessMachineConnectionInitiatorServer
+ _OBJC_METACLASS_$_HBPFitnessMachineConnectionServer
+ _OBJC_METACLASS_$_HBPFitnessMachineDataCharacteristicBase
+ _OBJC_METACLASS_$_HBPFitnessMachineDataCollector
+ _OBJC_METACLASS_$_HBPFitnessMachineDataProducer
+ _OBJC_METACLASS_$_HBPFitnessMachineManager
+ _OBJC_METACLASS_$_HBPFitnessMachineService
+ _OBJC_METACLASS_$_HBPFitnessMachineSession
+ _OBJC_METACLASS_$_HBPFitnessMachineSessionRecoveryConfiguration
+ _OBJC_METACLASS_$_HBPFitnessMachineSimulatorSupport
+ _OBJC_METACLASS_$_HBPFitnessMachineStatus
+ _OBJC_METACLASS_$_HBPGymKitDataSource
+ _OBJC_METACLASS_$_HBPGymKitMetricsDataSource
+ _OBJC_METACLASS_$_HBPGymKitPairingManager
+ _OBJC_METACLASS_$_HBPGymKitSettings
+ _OBJC_METACLASS_$_HBPGymKitWorkoutAnalyticEvent
+ _OBJC_METACLASS_$_HBPGymKitWorkoutSessionController
+ _OBJC_METACLASS_$_HBPHealthBluetoothPeripheralPluginDaemonExtension
+ _OBJC_METACLASS_$_HBPHealthPeripheral
+ _OBJC_METACLASS_$_HBPHealthService
+ _OBJC_METACLASS_$_HBPHealthServiceCharacteristic
+ _OBJC_METACLASS_$_HBPHealthServiceManager
+ _OBJC_METACLASS_$_HBPHealthServiceOOBInfo
+ _OBJC_METACLASS_$_HBPHealthServicesServer
+ _OBJC_METACLASS_$_HBPIdentifierTable
+ _OBJC_METACLASS_$_HBPIndoorBikeData
+ _OBJC_METACLASS_$_HBPNearFieldInterface
+ _OBJC_METACLASS_$_HBPServiceConnectionManager
+ _OBJC_METACLASS_$_HBPStairClimberData
+ _OBJC_METACLASS_$_HBPStepClimberData
+ _OBJC_METACLASS_$_HBPTreadmillData
+ _OBJC_METACLASS_$_HBPUnknownHealthService
+ _OBJC_METACLASS_$__HBPHealthServiceDataUpdate
+ _SBSGetScreenLockStatus
+ _SBSRemoteAlertHandleInvalidationErrorDomain
+ __HBPStringForNearFieldManagerNFCPermission
+ __os_log_fault_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _HDBluetoothPeripheralPluginIdentifier
- _HDConnectedGymPreferencesChanged
- _HDFitnessMachineMetricsCollectorDidChangeNotification
- _HDFitnessMachineServiceUUIDs_CrossTrainerDataCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_EurotasDataCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_EurotasDataServiceUUID
- _HDFitnessMachineServiceUUIDs_EurotasEnhancedFTMSCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_FeatureCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_IndoorBikeDataCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_ServiceUUID
- _HDFitnessMachineServiceUUIDs_StairClimberDataCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_StatusCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_StepClimberDataCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_TrainingStatusCharacteristicUUID
- _HDFitnessMachineServiceUUIDs_TreadmillDataCharacteristicUUID
- _HDHealthPeripheralAllPropertyNames
- _HDHealthPeripheralProfiles
- _HDHealthServiceClassForCBUUID
- _HDHealthServiceDiscoveryIdentifierInvalid
- _HDHealthServiceSessionIdentifierInvalid
- _HDServiceClassForProfile
- _HDWorkoutNotificationTerminalHandoffFieldDetected
- _OBJC_CLASS_$_HDBatteryService
- _OBJC_CLASS_$_HDCrossTrainerData
- _OBJC_CLASS_$_HDDeviceInformationService
- _OBJC_CLASS_$_HDEnhancedFTMSData
- _OBJC_CLASS_$_HDEurotasData
- _OBJC_CLASS_$_HDEurotasService
- _OBJC_CLASS_$_HDFitnessMachineAnalyticsCollector
- _OBJC_CLASS_$_HDFitnessMachineCharacteristicDoubleField
- _OBJC_CLASS_$_HDFitnessMachineCharacteristicField
- _OBJC_CLASS_$_HDFitnessMachineCharacteristicInt16Field
- _OBJC_CLASS_$_HDFitnessMachineCharacteristicUInt16Field
- _OBJC_CLASS_$_HDFitnessMachineCharacteristicUInt24Field
- _OBJC_CLASS_$_HDFitnessMachineCharacteristicUInt8Field
- _OBJC_CLASS_$_HDFitnessMachineConnection
- _OBJC_CLASS_$_HDFitnessMachineConnectionInitiatorServer
- _OBJC_CLASS_$_HDFitnessMachineConnectionServer
- _OBJC_CLASS_$_HDFitnessMachineDataCharacteristicBase
- _OBJC_CLASS_$_HDFitnessMachineDataCollector
- _OBJC_CLASS_$_HDFitnessMachineDataProducer
- _OBJC_CLASS_$_HDFitnessMachineManager
- _OBJC_CLASS_$_HDFitnessMachineService
- _OBJC_CLASS_$_HDFitnessMachineSession
- _OBJC_CLASS_$_HDFitnessMachineSessionRecoveryConfiguration
- _OBJC_CLASS_$_HDFitnessMachineSimulatorSupport
- _OBJC_CLASS_$_HDFitnessMachineStatus
- _OBJC_CLASS_$_HDGymKitDataSource
- _OBJC_CLASS_$_HDGymKitMetricsDataSource
- _OBJC_CLASS_$_HDGymKitPairingManager
- _OBJC_CLASS_$_HDGymKitSettings
- _OBJC_CLASS_$_HDGymKitWorkoutAnalyticEvent
- _OBJC_CLASS_$_HDGymKitWorkoutSessionController
- _OBJC_CLASS_$_HDHealthBluetoothPeripheralPluginDaemonExtension
- _OBJC_CLASS_$_HDHealthPeripheral
- _OBJC_CLASS_$_HDHealthService
- _OBJC_CLASS_$_HDHealthServiceCharacteristic
- _OBJC_CLASS_$_HDHealthServiceManager
- _OBJC_CLASS_$_HDHealthServiceOOBInfo
- _OBJC_CLASS_$_HDHealthServicesServer
- _OBJC_CLASS_$_HDIdentifierTable
- _OBJC_CLASS_$_HDIndoorBikeData
- _OBJC_CLASS_$_HDNearFieldInterface
- _OBJC_CLASS_$_HDServiceConnectionManager
- _OBJC_CLASS_$_HDStairClimberData
- _OBJC_CLASS_$_HDStepClimberData
- _OBJC_CLASS_$_HDTreadmillData
- _OBJC_CLASS_$_HDUnknownHealthService
- _OBJC_CLASS_$__HDHealthServiceDataUpdate
- _OBJC_METACLASS_$_HDBatteryService
- _OBJC_METACLASS_$_HDCrossTrainerData
- _OBJC_METACLASS_$_HDDeviceInformationService
- _OBJC_METACLASS_$_HDEnhancedFTMSData
- _OBJC_METACLASS_$_HDEurotasData
- _OBJC_METACLASS_$_HDEurotasService
- _OBJC_METACLASS_$_HDFitnessMachineAnalyticsCollector
- _OBJC_METACLASS_$_HDFitnessMachineCharacteristicDoubleField
- _OBJC_METACLASS_$_HDFitnessMachineCharacteristicField
- _OBJC_METACLASS_$_HDFitnessMachineCharacteristicInt16Field
- _OBJC_METACLASS_$_HDFitnessMachineCharacteristicUInt16Field
- _OBJC_METACLASS_$_HDFitnessMachineCharacteristicUInt24Field
- _OBJC_METACLASS_$_HDFitnessMachineCharacteristicUInt8Field
- _OBJC_METACLASS_$_HDFitnessMachineConnection
- _OBJC_METACLASS_$_HDFitnessMachineConnectionInitiatorServer
- _OBJC_METACLASS_$_HDFitnessMachineConnectionServer
- _OBJC_METACLASS_$_HDFitnessMachineDataCharacteristicBase
- _OBJC_METACLASS_$_HDFitnessMachineDataCollector
- _OBJC_METACLASS_$_HDFitnessMachineDataProducer
- _OBJC_METACLASS_$_HDFitnessMachineManager
- _OBJC_METACLASS_$_HDFitnessMachineService
- _OBJC_METACLASS_$_HDFitnessMachineSession
- _OBJC_METACLASS_$_HDFitnessMachineSessionRecoveryConfiguration
- _OBJC_METACLASS_$_HDFitnessMachineSimulatorSupport
- _OBJC_METACLASS_$_HDFitnessMachineStatus
- _OBJC_METACLASS_$_HDGymKitDataSource
- _OBJC_METACLASS_$_HDGymKitMetricsDataSource
- _OBJC_METACLASS_$_HDGymKitPairingManager
- _OBJC_METACLASS_$_HDGymKitSettings
- _OBJC_METACLASS_$_HDGymKitWorkoutAnalyticEvent
- _OBJC_METACLASS_$_HDGymKitWorkoutSessionController
- _OBJC_METACLASS_$_HDHealthBluetoothPeripheralPluginDaemonExtension
- _OBJC_METACLASS_$_HDHealthPeripheral
- _OBJC_METACLASS_$_HDHealthService
- _OBJC_METACLASS_$_HDHealthServiceCharacteristic
- _OBJC_METACLASS_$_HDHealthServiceManager
- _OBJC_METACLASS_$_HDHealthServiceOOBInfo
- _OBJC_METACLASS_$_HDHealthServicesServer
- _OBJC_METACLASS_$_HDIdentifierTable
- _OBJC_METACLASS_$_HDIndoorBikeData
- _OBJC_METACLASS_$_HDNearFieldInterface
- _OBJC_METACLASS_$_HDServiceConnectionManager
- _OBJC_METACLASS_$_HDStairClimberData
- _OBJC_METACLASS_$_HDStepClimberData
- _OBJC_METACLASS_$_HDTreadmillData
- _OBJC_METACLASS_$_HDUnknownHealthService
- _OBJC_METACLASS_$__HDHealthServiceDataUpdate
- __HDStringForNearFieldManagerNFCPermission
CStrings:
+ "%@-%@"
+ "%{public}@ handling remote pairing payload"
+ "%{public}@ handling send error"
+ "%{public}@: Acquired backlight assertion %{public}@"
+ "%{public}@: Active paired device found with supported capability. Observing nearby devices"
+ "%{public}@: Clearing SB alert handles"
+ "%{public}@: Connection invalidated, stop observing metrics"
+ "%{public}@: Device is currently locked / Health Data Store is unavailable so attempting to prompt to unlock"
+ "%{public}@: Failed to archive error for remote payload: %{public}@"
+ "%{public}@: Failed to take database assertion with error %{public}@."
+ "%{public}@: Handling OOB info fromRemote:%{public}@"
+ "%{public}@: Incorrect session UUID. expected: %{public}@, connectionUUID: %{public}@"
+ "%{public}@: Invalidating backlight assertion %{public}@"
+ "%{public}@: Launching workout remote view service"
+ "%{public}@: No session exists"
+ "%{public}@: Overwriting existing fitness machine session. Previous session was not properly cleaned up: %{public}@."
+ "%{public}@: Posting user notification to launch app"
+ "%{public}@: Received GymKitRemotePairing rapport request: %{public}@"
+ "%{public}@: Start bluetooth scanning: bluetooth state: %{public}@"
+ "%{public}@: Unable to acquire backlight assertion %{public}@"
+ "%{public}@: Unknown connection UUID: %{public}@"
+ "%{public}@: Waiting for Workout app to be foregrounded before continuing pairing"
+ "%{public}@: Waiting for app launch, so just continue with the handler for now"
+ "%{public}@: Workout app is foregrounded. Will resume pairing"
+ "%{public}@: attempting remote pairing"
+ "%{public}@: background launching workout app"
+ "%{public}@: cleaning up after remote alert handle teardown. _bluetoothState=%{public}@"
+ "%{public}@: clearing _bluetoothState from %{public}@ to Ignore"
+ "%{public}@: continuing with local pairing"
+ "%{public}@: dequeuing state: %{public}@"
+ "%{public}@: device was ineligible for paired handoff. continuing with local pairing"
+ "%{public}@: did read tag"
+ "%{public}@: didAttemptHandoffPairing=%{public}@"
+ "%{public}@: enqueuing state '%{public}@' while waiting for app launch"
+ "%{public}@: error when attempting remote pairing: %{public}@"
+ "%{public}@: failed to decode remote OOB: %{public}@"
+ "%{public}@: failed to decode remote error: %{public}@"
+ "%{public}@: failed to query feature availability due to error: %{public}@"
+ "%{public}@: failed to retrieve remote OOB: %{public}@"
+ "%{public}@: failed to send remote connection payload due to: %{public}@"
+ "%{public}@: failed to send remote error payload due to: %{public}@"
+ "%{public}@: handing off paired device is scanning for bluetooth"
+ "%{public}@: ignoring cleanup for stale alert handle"
+ "%{public}@: no HBPHealthPeripheral found for CBPeripheral %{public}@, so create one: %{public}@"
+ "%{public}@: no error and no OOB. continuing with local pairing"
+ "%{public}@: not able to send payload to remote device. dropping"
+ "%{public}@: not permitting field detect events. _bluetoothState=%{public}@"
+ "%{public}@: not permitting field detect events. _gymKitSettings.nfcPermission=%{public}@"
+ "%{public}@: not permitting field detect events. device is locked"
+ "%{public}@: not permitting field detect events. ndef tag session in progress"
+ "%{public}@: paired device is ignoring field events."
+ "%{public}@: pairing did begin"
+ "%{public}@: performing alert activation completion handler"
+ "%{public}@: posted notification with result=%{public}@, error=%{public}@"
+ "%{public}@: protected data is now available - start bluetooth scanning. BT state: %{public}@"
+ "%{public}@: protectedDataDidBecomeAvailable: %d"
+ "%{public}@: received remote OOB: %{public}@"
+ "%{public}@: remoteAlertHandle:didInvalidateWithError: %{public}@, (isRealError=%{public}@)"
+ "%{public}@: remoteAlertHandleDidActivate"
+ "%{public}@: remoteAlertHandleDidDeactivate:"
+ "%{public}@: retrieving local OOB info with error: %@"
+ "%{public}@: sending remote connection payload"
+ "%{public}@: sending remote error"
+ "%{public}@: shouldPromptToForeground: %{public}@, feature availability: %{public}@, FF enabled: %{public}@"
+ "%{public}@: skipping nfc permission check"
+ "%{public}@: successfully sent remote connection payload"
+ "%{public}@: successfully sent remote error payload"
+ "%{public}@: updateConnectionState: '%{public}@' toState: '%{public}@'"
+ "-[HBPFitnessMachineManager _queue_endFitnessMachineConnectionForFitnessMachineSessionUUID:withConnectionUUID:forcingReset:]"
+ "-[HBPFitnessMachineManager _queue_handleBluetoothDisconnection]"
+ "-[HBPFitnessMachineManager _queue_simulateDisconnect]"
+ "-[HBPFitnessMachineManager pairingManagerWillBeginPairing:fitnessMachineToken:]"
+ "-[HBPGymKitSettings _setNFCAlwaysOnPreferenceIfNecessary]"
+ "-[HBPHealthPeripheral peripheral:didWriteValueForCharacteristic:error:]_block_invoke"
+ "-[HBPHealthServiceManager _removeConnectedPeripheral:withError:]"
+ "@\"<HBPFitnessMachineConnectionInitiatorProtocol>\""
+ "@\"<HBPFitnessMachineStateTimersDelegate>\""
+ "@\"<HBPGymKitPairingManagerDelegate>\""
+ "@\"<HBPGymKitSettingsDelegate>\""
+ "@\"<HBPNearFieldInterfaceDelegate>\""
+ "@\"<HKObservableFeatureAvailabilityRequirement>\""
+ "@\"BLSAssertion\""
+ "@\"HBPEnhancedFTMSData\""
+ "@\"HBPEurotasData\""
+ "@\"HBPFitnessMachineAnalyticsCollector\""
+ "@\"HBPFitnessMachineCharacteristicDoubleField\""
+ "@\"HBPFitnessMachineCharacteristicInt16Field\""
+ "@\"HBPFitnessMachineCharacteristicUInt16Field\""
+ "@\"HBPFitnessMachineCharacteristicUInt24Field\""
+ "@\"HBPFitnessMachineCharacteristicUInt8Field\""
+ "@\"HBPFitnessMachineDataCharacteristicBase\""
+ "@\"HBPFitnessMachineDataCollector\""
+ "@\"HBPFitnessMachineDataProducer\""
+ "@\"HBPFitnessMachineManager\""
+ "@\"HBPFitnessMachineManager\"16@0:8"
+ "@\"HBPFitnessMachineSession\""
+ "@\"HBPFitnessMachineSimulatorSupport\""
+ "@\"HBPFitnessMachineStateTimer\""
+ "@\"HBPFitnessMachineStateTimers\""
+ "@\"HBPFitnessMachineStatus\""
+ "@\"HBPGymKitPairingManager\""
+ "@\"HBPGymKitSettings\""
+ "@\"HBPGymKitWorkoutAnalyticEvent\""
+ "@\"HBPHealthPeripheral\""
+ "@\"HBPHealthServiceCharacteristic\""
+ "@\"HBPHealthServiceManager\""
+ "@\"HBPHealthServiceManager\"16@0:8"
+ "@\"HBPHealthServiceOOBInfo\""
+ "@\"HBPHealthServiceOOBInfo\"24@0:8^@16"
+ "@\"HBPIdentifierTable\""
+ "@\"HBPNearFieldInterface\""
+ "@\"HBPServiceConnectionManager\""
+ "@\"HBPServiceConnectionManager\"16@0:8"
+ "@\"HDAssertion\""
+ "@\"HDNotificationManager\""
+ "@\"SBSRemoteAlertHandle\""
+ "@\"_HBPFTMProducerMetricTracker\""
+ "Attempting to write data (%@) to CBCharacteristic: %@, CBPeripheral: %@, HBPCharacteristic: %@, HBPPeripheral: %@, HBPHealthService: %@ with write type %ld"
+ "B16@?0@\"HBPFitnessMachineConnection\"8"
+ "B24@0:8@\"_HKBehavior\"16"
+ "CheckingForPairedHandoff"
+ "Fitness Machine BLE Scanning"
+ "GymKit always on user default setting (NPSDomainAccessor, paired watch): %{public}@"
+ "GymKit always on user default setting (UserDefaults, no paired watch): %{public}@"
+ "GymKit defaulting to always on for current platform"
+ "GymKit preferences (NPSDomainAccessor, paired watch): %{public}@"
+ "GymKit preferences (UserDefaults, no paired watch): %{public}@"
+ "GymKitOOBRequestIdentifier"
+ "GymKitRemotePairingPayloadIdentifier"
+ "GymKitRemotePairingSendErrorIdentifier"
+ "HBPBatteryService"
+ "HBPConnectedGymPreferencesChanged"
+ "HBPCrossTrainerData"
+ "HBPDatumGenerating"
+ "HBPDatumRendering"
+ "HBPDeviceInformationService"
+ "HBPEnhancedFTMSData"
+ "HBPEurotasData"
+ "HBPEurotasService"
+ "HBPFitnessMachineAnalyticsCollector"
+ "HBPFitnessMachineCharacteristicDoubleField"
+ "HBPFitnessMachineCharacteristicField"
+ "HBPFitnessMachineCharacteristicInt16Field"
+ "HBPFitnessMachineCharacteristicUInt16Field"
+ "HBPFitnessMachineCharacteristicUInt24Field"
+ "HBPFitnessMachineCharacteristicUInt8Field"
+ "HBPFitnessMachineConnection"
+ "HBPFitnessMachineConnectionInitiatorProtocol"
+ "HBPFitnessMachineConnectionInitiatorServer"
+ "HBPFitnessMachineConnectionServer"
+ "HBPFitnessMachineDataCharacteristicBase"
+ "HBPFitnessMachineDataCharacteristicBase.m"
+ "HBPFitnessMachineDataCollector"
+ "HBPFitnessMachineDataCollector.m"
+ "HBPFitnessMachineDataProducer"
+ "HBPFitnessMachineManager"
+ "HBPFitnessMachineManager.m"
+ "HBPFitnessMachineMetricsCollectorDidChangeNotification"
+ "HBPFitnessMachineService"
+ "HBPFitnessMachineSession"
+ "HBPFitnessMachineSession.m"
+ "HBPFitnessMachineSessionObserver"
+ "HBPFitnessMachineSessionRecoveryConfiguration"
+ "HBPFitnessMachineSimulatorSupport"
+ "HBPFitnessMachineStateTimer"
+ "HBPFitnessMachineStateTimer: %@ timer already running"
+ "HBPFitnessMachineStateTimer: %@ timer expired"
+ "HBPFitnessMachineStateTimer: Canceling %@ timer"
+ "HBPFitnessMachineStateTimer: Starting %@ timer with %llu seconds"
+ "HBPFitnessMachineStateTimers"
+ "HBPFitnessMachineStateTimersDelegate"
+ "HBPFitnessMachineStatus"
+ "HBPFitnessMachineStatus ignoring fitness machine status op code 0x%02x, returning unknown status."
+ "HBPFitnessMachineTypeOverride"
+ "HBPGymKitDataSource"
+ "HBPGymKitMetricsDataSource"
+ "HBPGymKitPairingManager"
+ "HBPGymKitPairingManager.m"
+ "HBPGymKitPairingManagerDelegate"
+ "HBPGymKitSettings"
+ "HBPGymKitSettingsDelegate"
+ "HBPGymKitWorkoutAnalyticEvent"
+ "HBPGymKitWorkoutSessionController"
+ "HBPHSCharacteristicsDelegate"
+ "HBPHealthBluetoothPeripheralPluginDaemonExtension"
+ "HBPHealthPeripheral"
+ "HBPHealthService"
+ "HBPHealthServiceCharacteristic"
+ "HBPHealthServiceCharacteristic.m"
+ "HBPHealthServiceManager"
+ "HBPHealthServiceManager.m"
+ "HBPHealthServiceOOBInfo"
+ "HBPHealthServicesServer"
+ "HBPIdentifierTable"
+ "HBPIndoorBikeData"
+ "HBPNearFieldInterface"
+ "HBPNearFieldInterfaceDelegate"
+ "HBPServiceConnectionManager"
+ "HBPStairClimberData"
+ "HBPStepClimberData"
+ "HBPTreadmillData"
+ "HBPUnknownHealthService"
+ "HBPWorkoutNotificationTerminalHandoffFieldDetected"
+ "HDPairedDeviceCapabilityProvidingObserver"
+ "HDRapportMessengerObserver"
+ "Localizable"
+ "OSEligibilityDomainIsEligible:"
+ "PAIRING_NOTIFICATION_BODY"
+ "PAIRING_NOTIFICATION_TITLE"
+ "Platform does not remote pairing"
+ "ReadyToScan"
+ "SBSRemoteAlertHandleObserver"
+ "Session confirmation not received"
+ "Session confirmation: client ready"
+ "Session confirmation: confirmed for sessionUUID %{public}@"
+ "Session confirmation: machine running"
+ "Session ended without receiving session confirmation from client."
+ "Setting GymKit machine brand=%{public}@"
+ "Skipping gymkit-workout analytics: session handed off to paired device"
+ "Submitting gymkit-workout analytics: hasError=%{BOOL}d"
+ "T@\"<HBPFitnessMachineConnectionInitiatorProtocol>\",R,N"
+ "T@\"<HBPFitnessMachineStateTimersDelegate>\",W,N,V_delegate"
+ "T@\"<HBPGymKitPairingManagerDelegate>\",W,N,V_delegate"
+ "T@\"<HBPGymKitSettingsDelegate>\",W,N,V_delegate"
+ "T@\"<HBPNearFieldInterfaceDelegate>\",W,N,V_delegate"
+ "T@\"HBPEnhancedFTMSData\",&,N,V_initialEnhancedFTMSData"
+ "T@\"HBPFitnessMachineDataCharacteristicBase\",&,N,V_initialMachineData"
+ "T@\"HBPFitnessMachineDataProducer\",R,N,V_fitnessMachineDataProducer"
+ "T@\"HBPFitnessMachineManager\",R,N"
+ "T@\"HBPFitnessMachineManager\",R,N,V_fitnessManager"
+ "T@\"HBPFitnessMachineSessionRecoveryConfiguration\",R,N"
+ "T@\"HBPFitnessMachineStatus\",&,N,V_initialMachineStatus"
+ "T@\"HBPGymKitWorkoutAnalyticEvent\",&,N,V_gymKitWorkoutEvent"
+ "T@\"HBPHealthPeripheral\",R,W,N,V_healthPeripheral"
+ "T@\"HBPHealthServiceCharacteristic\",R,N,V_characteristic"
+ "T@\"HBPHealthServiceManager\",R,N"
+ "T@\"HBPHealthServiceManager\",R,N,V_serviceManager"
+ "T@\"HBPHealthServiceOOBInfo\",R,N,V_oobInfo"
+ "T@\"HBPServiceConnectionManager\",R,N"
+ "T@\"HBPServiceConnectionManager\",R,N,V_serviceConnectionManager"
+ "T@\"HDAssertion\",&,N,V_databaseAssertion"
+ "TB,R,N,V_oobFromRemote"
+ "TLAlertTopicPassbookNFCScanComplete"
+ "Unexpected schema identifier: %@"
+ "Unknown request"
+ "WorkoutRemoteViewService.FitnessMachinePairingViewController"
+ "_HBPFTMProducerMetricTracker"
+ "_HBPHealthServiceConnectionInfo"
+ "_HBPHealthServiceDataUpdate"
+ "_HBPHealthServiceDiscoveryInfo"
+ "_HBPHealthServiceWriteOperation"
+ "_databaseAssertion"
+ "_dualBacklightAssertion"
+ "_featureAvailabilityRequirement"
+ "_machineRunning"
+ "_notificationManager"
+ "_oobFromRemote"
+ "_queue_activeAlertHandle"
+ "_queue_alertActivationCompletionHandler"
+ "_queue_nearFieldInterfaceDidReadTag:"
+ "_queue_queuedStateChanges"
+ "_queue_waitingForAppLaunch"
+ "_sessionConfirmed"
+ "acquireWithExplanation:observer:attributes:"
+ "activateWithContext:"
+ "activePairedDevice"
+ "addObserver:forSchemaIdentifier:"
+ "allServicesWithProfile:assertion:error:"
+ "b4c83db3-9a78-4c99-8848-2588b9ffab49"
+ "beginNewActivity:insertionType:nodeWrapper:"
+ "bundleForClass:"
+ "clientRemote_receivedRemoteConnectionPayload:"
+ "com.apple.WorkoutRemoteViewService"
+ "com.apple.health.GymKitPairing"
+ "confirmSessionStartedWithConnectionUUID:fitnessMachineSessionUUID:"
+ "currentWorkoutSessionSnapshot"
+ "currentlyConnectedDeviceIDSIdentifiers"
+ "deleteService:assertion:healthDatabase:error:"
+ "dictionaryRepresentation"
+ "didBeginActivity:insertionType:nodeWrapper:dataSource:"
+ "didBeginNewActivity:insertionType:nodeWrapper:"
+ "didEndActivity:nodeWrapper:dataSource:"
+ "didEndCurrentActivity:nodeWrapper:"
+ "disableLowerGesture"
+ "endCurrentActivity:nodeWrapper:"
+ "failed to decode remote error"
+ "features"
+ "forceActive"
+ "handlePostInstall:"
+ "hasExistingWorkoutError"
+ "hk_isGymKitPairedHandoffIgnoredFieldEventError"
+ "hk_isGymKitPairedHandoffIneligibleError"
+ "hoplite"
+ "hopliteOOP"
+ "hopliteOOPThallium"
+ "hoplitePairedHandoff"
+ "hopliteSessionConfirmation"
+ "initWithDomain:"
+ "initWithProfile:bundle:"
+ "initWithSchemaIdentifier:name:"
+ "initWithServiceName:viewControllerClassName:"
+ "isSatisfiedWithDataSource:error:"
+ "localizedStringForKey:value:table:"
+ "nanoRegistryDeviceCapabilityProvider"
+ "newHandleWithDefinition:configurationContext:"
+ "oobFromRemote"
+ "pairedDeviceCapabilitiesDidUpdate:"
+ "pairingManagerRequestsOOBDataWithError:"
+ "peripheral:didCompleteChannelSoundingSession:"
+ "peripheral:didReceiveChannelSoundingProcedureResults:error:"
+ "postNotificationWithRequest:completion:"
+ "preventIdle"
+ "profileExtensionsConformingToProtocol:"
+ "q\xb1"
+ "rapportMessenger"
+ "rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:"
+ "registerObserver:queue:"
+ "remoteAlertHandle:didInvalidateWithError:"
+ "remoteAlertHandleDidActivate:"
+ "remoteAlertHandleDidDeactivate:"
+ "remote_confirmSessionStartedForFitnessMachineSessionUUID:"
+ "remote_sendRemoteConnectionPayload:"
+ "requestWithIdentifier:content:trigger:"
+ "requirementEvaluationDataSource"
+ "schemaIdentifier"
+ "searchForNearbyDevices"
+ "sendRemoteConnectionPayload:withConnectionUUID:"
+ "sendRequest:data:completion:"
+ "setAccessoryImageName:"
+ "setAlertTopic:"
+ "setBody:"
+ "setCategoryIdentifier:"
+ "setDatabaseAssertion:"
+ "setOobInfo:fromRemote:"
+ "setShouldHideDate:"
+ "setShouldIgnoreDoNotDisturb:"
+ "setSound:"
+ "setTitle:"
+ "sharedBehavior"
+ "shouldLoadPluginForBehavior:"
+ "soundWithAlertType:"
+ "supportsCapability:"
+ "synchronize"
+ "takeAccessibilityAssertionWithOwnerIdentifier:contextType:error:"
+ "timeoutAfterInterval:"
+ "v16@?0@\"<HBPFitnessMachineSessionObserver>\"8"
+ "v16@?0@\"HBPFitnessMachineConnection\"8"
+ "v16@?0@\"_HBPHealthServiceConnectionInfo\"8"
+ "v24@0:8@\"<HDPairedDeviceCapabilityProviding>\"16"
+ "v24@0:8@\"HBPFitnessMachineStateTimers\"16"
+ "v24@0:8@\"HBPGymKitPairingManager\"16"
+ "v24@0:8@\"HBPNearFieldInterface\"16"
+ "v24@0:8@\"NSData\"16"
+ "v24@0:8@\"SBSRemoteAlertHandle\"16"
+ "v24@0:8@?<v@?>16"
+ "v24@?0@\"HBPHealthServiceOOBInfo\"8@\"NSError\"16"
+ "v28@0:8@\"HBPGymKitPairingManager\"16B24"
+ "v32@0:8@\"HBPGymKitPairingManager\"16@\"HBPFitnessMachineSession\"24"
+ "v32@0:8@\"HBPGymKitPairingManager\"16@\"NSError\"24"
+ "v32@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionSnapshot\"24"
+ "v32@0:8@\"HKWorkoutActivity\"16@\"HKWorkoutActivityNodeWrapper\"24"
+ "v32@0:8@\"NSData\"16@\"NSUUID\"24"
+ "v32@0:8@\"NSUUID\"16@\"HBPFitnessMachineSessionRecoveryConfiguration\"24"
+ "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
+ "v32@?0@\"HBPHealthService\"8@\"NSData\"16@\"NSError\"24"
+ "v32@?0@\"NSData\"8@\"NSString\"16@\"NSError\"24"
+ "v40@0:8@\"CBPeripheral\"16@\"CBChannelSoundingProcedureResults\"24@\"NSError\"32"
+ "v40@0:8@\"HBPGymKitPairingManager\"16@\"HKHealthService\"24Q32"
+ "v40@0:8@\"HBPGymKitPairingManager\"16Q24Q32"
+ "v40@0:8@\"HBPGymKitSettings\"16Q24Q32"
+ "v40@0:8@\"HKWorkoutActivity\"16@\"HKWorkoutActivityNodeWrapper\"24@\"<HDWorkoutDataSource>\"32"
+ "v40@0:8@\"HKWorkoutActivity\"16Q24@\"HKWorkoutActivityNodeWrapper\"32"
+ "v40@?0Q8@\"HBPHealthServiceCharacteristic\"16@\"HKDevice\"24@\"NSError\"32"
+ "v48@0:8@\"HKWorkoutActivity\"16Q24@\"HKWorkoutActivityNodeWrapper\"32@\"<HDWorkoutDataSource>\"40"
+ "v48@0:8@16Q24@32@40"
+ "v56@0:8@\"HDRapportMessenger\"16@\"HDRapportRequestIdentifier\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "wave.3.forward.circle.fill"
+ "workoutManager:didChangeStateForCurrentSession:"
+ "workoutManager:didUpdateCurrentSession:"
- "%{public}@: no HDHealthPeripheral found for CBPeripheral %{public}@, so create one: %{public}@"
- "-[HDFitnessMachineManager _queue_endFitnessMachineConnectionForFitnessMachineSessionUUID:withConnectionUUID:forcingReset:]"
- "-[HDFitnessMachineManager _queue_handleBluetoothDisconnection]"
- "-[HDFitnessMachineManager _queue_simulateDisconnect]"
- "-[HDFitnessMachineManager pairingManagerWillBeginPairing:fitnessMachineToken:]"
- "-[HDGymKitSettings _setNFCAlwaysOnPreferenceIfNecessary]"
- "-[HDHealthPeripheral peripheral:didWriteValueForCharacteristic:error:]_block_invoke"
- "-[HDHealthServiceManager _removeConnectedPeripheral:withError:]"
- "@\"<HDFitnessMachineConnectionInitiatorProtocol>\""
- "@\"<HDFitnessMachineStateTimersDelegate>\""
- "@\"<HDGymKitPairingManagerDelegate>\""
- "@\"<HDGymKitSettingsDelegate>\""
- "@\"<HDNearFieldInterfaceDelegate>\""
- "@\"HDEnhancedFTMSData\""
- "@\"HDEurotasData\""
- "@\"HDFitnessMachineAnalyticsCollector\""
- "@\"HDFitnessMachineCharacteristicDoubleField\""
- "@\"HDFitnessMachineCharacteristicInt16Field\""
- "@\"HDFitnessMachineCharacteristicUInt16Field\""
- "@\"HDFitnessMachineCharacteristicUInt24Field\""
- "@\"HDFitnessMachineCharacteristicUInt8Field\""
- "@\"HDFitnessMachineDataCharacteristicBase\""
- "@\"HDFitnessMachineDataCollector\""
- "@\"HDFitnessMachineDataProducer\""
- "@\"HDFitnessMachineManager\""
- "@\"HDFitnessMachineManager\"16@0:8"
- "@\"HDFitnessMachineSession\""
- "@\"HDFitnessMachineSimulatorSupport\""
- "@\"HDFitnessMachineStateTimer\""
- "@\"HDFitnessMachineStateTimers\""
- "@\"HDFitnessMachineStatus\""
- "@\"HDGymKitPairingManager\""
- "@\"HDGymKitSettings\""
- "@\"HDGymKitWorkoutAnalyticEvent\""
- "@\"HDHealthPeripheral\""
- "@\"HDHealthServiceCharacteristic\""
- "@\"HDHealthServiceManager\""
- "@\"HDHealthServiceManager\"16@0:8"
- "@\"HDHealthServiceOOBInfo\""
- "@\"HDHealthServiceOOBInfo\"32@0:8@\"HDGymKitPairingManager\"16^@24"
- "@\"HDIdentifierTable\""
- "@\"HDNearFieldInterface\""
- "@\"HDServiceConnectionManager\""
- "@\"HDServiceConnectionManager\"16@0:8"
- "@\"_HDFTMProducerMetricTracker\""
- "Attempting to write data (%@) to CBCharacteristic: %@, CBPeripheral: %@, HDCharacteristic: %@, HDPeripheral: %@, HDHealthService: %@ with write type %ld"
- "B16@?0@\"HDFitnessMachineConnection\"8"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "Disabling NFCAlwaysOn for iPhone"
- "GymKit preferences: %{public}@"
- "HDBatteryService"
- "HDConnectedGymPreferencesChanged"
- "HDCrossTrainerData"
- "HDDatumGenerating"
- "HDDatumRendering"
- "HDDeviceInformationService"
- "HDEnhancedFTMSData"
- "HDEurotasData"
- "HDEurotasService"
- "HDFitnessMachineAnalyticsCollector"
- "HDFitnessMachineCharacteristicDoubleField"
- "HDFitnessMachineCharacteristicField"
- "HDFitnessMachineCharacteristicInt16Field"
- "HDFitnessMachineCharacteristicUInt16Field"
- "HDFitnessMachineCharacteristicUInt24Field"
- "HDFitnessMachineCharacteristicUInt8Field"
- "HDFitnessMachineConnection"
- "HDFitnessMachineConnectionInitiatorProtocol"
- "HDFitnessMachineConnectionInitiatorServer"
- "HDFitnessMachineConnectionServer"
- "HDFitnessMachineDataCharacteristicBase"
- "HDFitnessMachineDataCharacteristicBase.m"
- "HDFitnessMachineDataCollector"
- "HDFitnessMachineDataCollector.m"
- "HDFitnessMachineDataProducer"
- "HDFitnessMachineManager"
- "HDFitnessMachineManager.m"
- "HDFitnessMachineMetricsCollectorDidChangeNotification"
- "HDFitnessMachineService"
- "HDFitnessMachineSession"
- "HDFitnessMachineSession.m"
- "HDFitnessMachineSessionObserver"
- "HDFitnessMachineSessionRecoveryConfiguration"
- "HDFitnessMachineSimulatorSupport"
- "HDFitnessMachineStateTimer"
- "HDFitnessMachineStateTimer: %@ timer already running"
- "HDFitnessMachineStateTimer: %@ timer expired"
- "HDFitnessMachineStateTimer: Canceling %@ timer"
- "HDFitnessMachineStateTimer: Starting %@ timer with %llu seconds"
- "HDFitnessMachineStateTimers"
- "HDFitnessMachineStateTimersDelegate"
- "HDFitnessMachineStatus"
- "HDFitnessMachineStatus ignoring fitness machine status op code 0x%02x, returning unknown status."
- "HDFitnessMachineTypeOverride"
- "HDGymKitDataSource"
- "HDGymKitMetricsDataSource"
- "HDGymKitPairingManager"
- "HDGymKitPairingManager.m"
- "HDGymKitPairingManagerDelegate"
- "HDGymKitSettings"
- "HDGymKitSettingsDelegate"
- "HDGymKitWorkoutAnalyticEvent"
- "HDGymKitWorkoutSessionController"
- "HDHSCharacteristicsDelegate"
- "HDHealthBluetoothPeripheralPluginDaemonExtension"
- "HDHealthPeripheral"
- "HDHealthService"
- "HDHealthServiceCharacteristic"
- "HDHealthServiceCharacteristic.m"
- "HDHealthServiceManager"
- "HDHealthServiceManager.m"
- "HDHealthServiceOOBInfo"
- "HDHealthServicesServer"
- "HDIdentifierTable"
- "HDIndoorBikeData"
- "HDNearFieldInterface"
- "HDNearFieldInterfaceDelegate"
- "HDServiceConnectionManager"
- "HDStairClimberData"
- "HDStepClimberData"
- "HDTreadmillData"
- "HDUnknownHealthService"
- "HDWorkoutNotificationTerminalHandoffFieldDetected"
- "Scanning"
- "T@\"<HDFitnessMachineConnectionInitiatorProtocol>\",R,N"
- "T@\"<HDFitnessMachineStateTimersDelegate>\",W,N,V_delegate"
- "T@\"<HDGymKitPairingManagerDelegate>\",W,N,V_delegate"
- "T@\"<HDGymKitSettingsDelegate>\",W,N,V_delegate"
- "T@\"<HDNearFieldInterfaceDelegate>\",W,N,V_delegate"
- "T@\"HDEnhancedFTMSData\",&,N,V_initialEnhancedFTMSData"
- "T@\"HDFitnessMachineDataCharacteristicBase\",&,N,V_initialMachineData"
- "T@\"HDFitnessMachineDataProducer\",R,N,V_fitnessMachineDataProducer"
- "T@\"HDFitnessMachineManager\",R,N"
- "T@\"HDFitnessMachineManager\",R,N,V_fitnessManager"
- "T@\"HDFitnessMachineSessionRecoveryConfiguration\",R,N"
- "T@\"HDFitnessMachineStatus\",&,N,V_initialMachineStatus"
- "T@\"HDGymKitWorkoutAnalyticEvent\",&,N,V_gymKitWorkoutEvent"
- "T@\"HDHealthPeripheral\",R,W,N,V_healthPeripheral"
- "T@\"HDHealthServiceCharacteristic\",R,N,V_characteristic"
- "T@\"HDHealthServiceManager\",R,N"
- "T@\"HDHealthServiceManager\",R,N,V_serviceManager"
- "T@\"HDHealthServiceOOBInfo\",&,N,V_oobInfo"
- "T@\"HDServiceConnectionManager\",R,N"
- "T@\"HDServiceConnectionManager\",R,N,V_serviceConnectionManager"
- "_HDFTMProducerMetricTracker"
- "_HDHealthServiceConnectionInfo"
- "_HDHealthServiceDataUpdate"
- "_HDHealthServiceDiscoveryInfo"
- "_HDHealthServiceWriteOperation"
- "allServicesWithError:"
- "allServicesWithProfile:error:"
- "beginNewActivity:"
- "currentWorkoutSessionServer"
- "deleteService:healthDatabase:error:"
- "didBeginActivity:dataSource:"
- "didBeginNewActivity:"
- "didEndActivity:dataSource:"
- "didEndCurrentActivity:"
- "endCurrentActivity:"
- "fitnessMachineManager"
- "pairingManagerRequestsOOBData:error:"
- "qQ"
- "setOobInfo:"
- "shouldLoadPluginForDaemon:"
- "v16@?0@\"<HDFitnessMachineSessionObserver>\"8"
- "v16@?0@\"HDFitnessMachineConnection\"8"
- "v16@?0@\"_HDHealthServiceConnectionInfo\"8"
- "v24@0:8@\"HDFitnessMachineStateTimers\"16"
- "v24@0:8@\"HDGymKitPairingManager\"16"
- "v24@0:8@\"HDNearFieldInterface\"16"
- "v28@0:8@\"HDGymKitPairingManager\"16B24"
- "v32@0:8@\"HDGymKitPairingManager\"16@\"HDFitnessMachineSession\"24"
- "v32@0:8@\"HDGymKitPairingManager\"16@\"NSError\"24"
- "v32@0:8@\"NSUUID\"16@\"HDFitnessMachineSessionRecoveryConfiguration\"24"
- "v32@?0@\"HDHealthService\"8@\"NSData\"16@\"NSError\"24"
- "v40@0:8@\"HDGymKitPairingManager\"16@\"HKHealthService\"24Q32"
- "v40@0:8@\"HDGymKitPairingManager\"16Q24Q32"
- "v40@0:8@\"HDGymKitSettings\"16Q24Q32"
- "v40@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionServer\"24@\"<HDWorkoutDataAccumulator>\"32"
- "v40@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionServer\"24q32"
- "v40@0:8@16@24q32"
- "v40@?0Q8@\"HDHealthServiceCharacteristic\"16@\"HKDevice\"24@\"NSError\"32"
- "workoutManager:currentWorkout:didChangeToState:"
- "workoutManager:currentWorkout:didUpdateDataAccumulator:"

```
