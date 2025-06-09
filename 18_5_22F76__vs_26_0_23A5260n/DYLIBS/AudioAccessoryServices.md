## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-25.4.0.0.0
-  __TEXT.__text: 0x29d94
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x32bc
-  __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__cstring: 0x8208
-  __TEXT.__unwind_info: 0xb78
-  __TEXT.__objc_classname: 0x37e
-  __TEXT.__objc_methname: 0x6e27
-  __TEXT.__objc_methtype: 0xfed
-  __TEXT.__objc_stubs: 0x2b40
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0xa48
-  __DATA_CONST.__objc_classlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x58
+30.45.3.0.0
+  __TEXT.__text: 0x3d270
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0x4e0c
+  __TEXT.__const: 0x290
+  __TEXT.__gcc_except_tab: 0xec4
+  __TEXT.__cstring: 0xb546
+  __TEXT.__unwind_info: 0x1000
+  __TEXT.__objc_classname: 0x620
+  __TEXT.__objc_methname: 0xab17
+  __TEXT.__objc_methtype: 0x133c
+  __TEXT.__objc_stubs: 0x5860
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0xe80
+  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15f0
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x410
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x5a18
-  __AUTH.__objc_data: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x22e0
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x2100
+  __AUTH_CONST.__objc_const: 0x8f48
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0x780
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5ec
-  __DATA.__data: 0x970
+  __DATA.__objc_ivar: 0x880
+  __DATA.__data: 0xbf8
   __DATA.__common: 0x8
-  __DATA.__bss: 0x34
-  __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__data: 0x1c0
-  __DATA_DIRTY.__bss: 0x10
+  __DATA.__bss: 0x38
+  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA_DIRTY.__data: 0x230
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F57FFCD-8D1A-3F39-A88D-5CBB68A82427
-  Functions: 1447
-  Symbols:   4309
-  CStrings:  2579
+  UUID: 8F7CCEAE-AA98-3863-BD25-637C277DA3F5
+  Functions: 2091
+  Symbols:   6340
+  CStrings:  3917
 
Symbols:
+ +[AAAdvertisementPayload advertisementPayloadWithData:]
+ +[AABattery invalidBattery]
+ +[AABattery supportsSecureCoding]
+ +[AADeviceBatteryInfo supportsSecureCoding]
+ +[AAManufacturerDataAdvertisement manufacturerDataWithData:]
+ +[AAProximityPairingPayload proximityPairingPayloadWithData:]
+ +[AAProximityPairingStatusPayloadB188B288 supportedPID:]
+ +[AAProximityPairingStatusPayloadB444 supportedPID:]
+ +[AAProximityPairingStatusPayloadB463 supportedPID:]
+ +[AAProximityPairingStatusPayloadB515 supportedPID:]
+ +[AAProximityPairingStatusPayloadB515c supportedPID:]
+ +[AAProximityPairingStatusPayloadGeneral proximityPairingStatusPayloadWithData:pid:]
+ +[AAProximityPairingStatusPayloadGeneral supportedPID:]
+ +[AAProximityPairingStatusPayloadOtherTetheredNonCase supportedPID:]
+ +[AASettingsTelemetry sharedInstance]
+ +[AASettingsTelemetry sharedInstance].cold.1
+ +[BTAudioRoutingRequest isSupported]
+ -[AAAdvertisementPayload .cxx_destruct]
+ -[AAAdvertisementPayload describeProperties]
+ -[AAAdvertisementPayload description]
+ -[AAAdvertisementPayload hash]
+ -[AAAdvertisementPayload initLogParseError:]
+ -[AAAdvertisementPayload initLogParseError:].cold.1
+ -[AAAdvertisementPayload initWithData:]
+ -[AAAdvertisementPayload initWithData:].cold.1
+ -[AAAdvertisementPayload isEqual:]
+ -[AAAdvertisementPayload isEqualToPayload:]
+ -[AAAdvertisementPayload payloadData]
+ -[AAAdvertisementPayload type]
+ -[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]
+ -[AABattery chargeStatus]
+ -[AABattery chargingOBCTimeUntilCharged]
+ -[AABattery chargingOBC]
+ -[AABattery charging]
+ -[AABattery copyWithZone:]
+ -[AABattery description]
+ -[AABattery encodeWithCoder:]
+ -[AABattery fullyCharged]
+ -[AABattery hash]
+ -[AABattery inAACP]
+ -[AABattery initWithAACPBatteryInfo:productID:]
+ -[AABattery initWithCoder:]
+ -[AABattery initWithLevel:productID:state:type:]
+ -[AABattery isCaseBattery]
+ -[AABattery isChargingPaused]
+ -[AABattery isEqual:]
+ -[AABattery isEqualToBattery:]
+ -[AABattery isExpired]
+ -[AABattery isLow]
+ -[AABattery lastOrigin]
+ -[AABattery lastSeen]
+ -[AABattery level]
+ -[AABattery lowLevel]
+ -[AABattery productID]
+ -[AABattery setChargingOBCTimeUntilCharged:]
+ -[AABattery setLastOrigin:]
+ -[AABattery setLastSeen:]
+ -[AABattery setLevel:]
+ -[AABattery setProductID:]
+ -[AABattery setSourceFlags:]
+ -[AABattery setState:]
+ -[AABattery setType:]
+ -[AABattery sourceFlags]
+ -[AABattery state]
+ -[AABattery type]
+ -[AABattery updateWithAABattery:]
+ -[AABattery valid]
+ -[AAController _accessoryUsageSummaryMessageReceived:fromDevice:]
+ -[AAController _batteryInfoMessageReceived:fromDevice:]
+ -[AAController _rawGestureMessageReceived:fromDevice:]
+ -[AAController _sleepDetectionMessageReceived:fromDevice:]
+ -[AAController accessoryUsageSummaryMessageHandler]
+ -[AAController batteryInfoMessageHandler]
+ -[AAController rawGestureMessageHandler]
+ -[AAController sendSleepDetectionMessage:destinationIdentifier:completionHandler:]
+ -[AAController setAccessoryUsageSummaryMessageHandler:]
+ -[AAController setBatteryInfoMessageHandler:]
+ -[AAController setRawGestureMessageHandler:]
+ -[AAController setSleepDetectionMessageHandler:]
+ -[AAController sleepDetectionMessageHandler]
+ -[AADeviceBatteryInfo .cxx_destruct]
+ -[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:]
+ -[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:].cold.1
+ -[AADeviceBatteryInfo _clearCombinedBattery]
+ -[AADeviceBatteryInfo _updateBatteriesFromTetheredAdvertisement:]
+ -[AADeviceBatteryInfo _updateBatteriesFromTetheredAdvertisement:].cold.1
+ -[AADeviceBatteryInfo _updateBatteriesFromUntetheredAdvertisement:]
+ -[AADeviceBatteryInfo _updateBatteriesFromUntetheredAdvertisement:].cold.1
+ -[AADeviceBatteryInfo _updateCaseInfo:]
+ -[AADeviceBatteryInfo _updateChargingOBCTimeUntilCharged:]
+ -[AADeviceBatteryInfo _updateCombinedBattery]
+ -[AADeviceBatteryInfo _updateWithAACPBatteryInfo:]
+ -[AADeviceBatteryInfo _updateWithNearbyBattery:forType:withSource:]
+ -[AADeviceBatteryInfo _updateWithProximityPairingPayload:]
+ -[AADeviceBatteryInfo _updateWithProximityPairingPayload:].cold.1
+ -[AADeviceBatteryInfo areAnyBatteriesAvailable]
+ -[AADeviceBatteryInfo batteries]
+ -[AADeviceBatteryInfo batteryCase]
+ -[AADeviceBatteryInfo batteryCombinedLeftRight]
+ -[AADeviceBatteryInfo batteryForType:]
+ -[AADeviceBatteryInfo batteryLeft]
+ -[AADeviceBatteryInfo batteryMain]
+ -[AADeviceBatteryInfo batteryMap]
+ -[AADeviceBatteryInfo batteryRight]
+ -[AADeviceBatteryInfo bluetoothAddress]
+ -[AADeviceBatteryInfo caseIdentifier]
+ -[AADeviceBatteryInfo caseLedColor]
+ -[AADeviceBatteryInfo caseLedStatus]
+ -[AADeviceBatteryInfo caseVersion]
+ -[AADeviceBatteryInfo clearExpiredBatteries]
+ -[AADeviceBatteryInfo color]
+ -[AADeviceBatteryInfo copyWithZone:]
+ -[AADeviceBatteryInfo descriptionWithLevel:]
+ -[AADeviceBatteryInfo description]
+ -[AADeviceBatteryInfo encodeWithCoder:]
+ -[AADeviceBatteryInfo findMyGroupIdentifier]
+ -[AADeviceBatteryInfo identifier]
+ -[AADeviceBatteryInfo initWithCoder:]
+ -[AADeviceBatteryInfo initWithIdentifier:]
+ -[AADeviceBatteryInfo isConnected]
+ -[AADeviceBatteryInfo isNearby]
+ -[AADeviceBatteryInfo model]
+ -[AADeviceBatteryInfo name]
+ -[AADeviceBatteryInfo productID]
+ -[AADeviceBatteryInfo removeBatteryInMap:]
+ -[AADeviceBatteryInfo setBatteryInMap:]
+ -[AADeviceBatteryInfo setBatteryMap:]
+ -[AADeviceBatteryInfo setBluetoothAddress:]
+ -[AADeviceBatteryInfo setCaseIdentifier:]
+ -[AADeviceBatteryInfo setCaseLedColor:]
+ -[AADeviceBatteryInfo setCaseLedStatus:]
+ -[AADeviceBatteryInfo setCaseVersion:]
+ -[AADeviceBatteryInfo setColor:]
+ -[AADeviceBatteryInfo setFindMyGroupIdentifier:]
+ -[AADeviceBatteryInfo setIsConnected:]
+ -[AADeviceBatteryInfo setIsNearby:]
+ -[AADeviceBatteryInfo setModel:]
+ -[AADeviceBatteryInfo setName:]
+ -[AADeviceBatteryInfo setProductID:]
+ -[AADeviceBatteryInfo updateWithAACPBatteryInfoData:]
+ -[AADeviceBatteryInfo updateWithAANearbyDevice:]
+ -[AADeviceBatteryInfo updateWithConnectedDevice:]
+ -[AADeviceBatteryInfo updateWithDisconnectedDevice:]
+ -[AADeviceBatteryInfo visibleBatteryCase]
+ -[AADeviceBatteryInfo visibleBatteryCombinedLeftRight]
+ -[AADeviceBatteryInfo visibleBatteryLeft]
+ -[AADeviceBatteryInfo visibleBatteryMain]
+ -[AADeviceBatteryInfo visibleBatteryRight]
+ -[AADeviceConfig allowHealthKitDataWrite]
+ -[AADeviceConfig allowTemporaryManagedPairing]
+ -[AADeviceConfig changeOptimizedBatteryChargingState]
+ -[AADeviceConfig enableChargingReminder]
+ -[AADeviceConfig enableSleepDetection]
+ -[AADeviceConfig needsUpdateToPairedDevice]
+ -[AADeviceConfig rawGesturesConfigFlags]
+ -[AADeviceConfig remoteCameraControlConfig]
+ -[AADeviceConfig setAllowHealthKitDataWrite:]
+ -[AADeviceConfig setAllowTemporaryManagedPairing:]
+ -[AADeviceConfig setChangeOptimizedBatteryChargingState:]
+ -[AADeviceConfig setEnableChargingReminder:]
+ -[AADeviceConfig setEnableSleepDetection:]
+ -[AADeviceConfig setRawGesturesConfigFlags:]
+ -[AADeviceConfig setRemoteCameraControlConfig:]
+ -[AADeviceManager _activateDirect:]
+ -[AADeviceManager _activateDirect:].cold.1
+ -[AADeviceManager _activateXPC:reactivate:]
+ -[AADeviceManager _activateXPC:reactivate:].cold.1
+ -[AADeviceManager _invalidateDirect]
+ -[AADeviceManager _sendDeviceConfigDirect:identifier:completion:]
+ -[AADeviceManager _sendDeviceConfigXPC:identifier:completion:]
+ -[AADeviceManager deviceBatteryInfoLostHandler]
+ -[AADeviceManager deviceBatteryInfoUpdatedHandler]
+ -[AADeviceManager deviceManagerFoundBatteryInfo:]
+ -[AADeviceManager deviceManagerFoundBatteryInfo:].cold.1
+ -[AADeviceManager deviceManagerLostBatteryInfo:]
+ -[AADeviceManager direct]
+ -[AADeviceManager fetchAADeviceBatteryInfoForAddress:]
+ -[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]
+ -[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:]
+ -[AADeviceManager fetchPairedAudioAccessoryDevices]
+ -[AADeviceManager internalServicesDaemon]
+ -[AADeviceManager isTemporaryPairingConnectionAllowed]
+ -[AADeviceManager setDeviceBatteryInfoLostHandler:]
+ -[AADeviceManager setDeviceBatteryInfoUpdatedHandler:]
+ -[AADeviceManager setInternalServicesDaemon:]
+ -[AAHIDDevice .cxx_destruct]
+ -[AAHIDDevice hidDevice]
+ -[AAHIDDevice initWithHIDDeviceAndSensorInfo:sensorInfo:]
+ -[AAHIDDevice isSetupComplete]
+ -[AAHIDDevice isSubscribed]
+ -[AAHIDDevice sensorInfo]
+ -[AAHIDDevice setIsSetupComplete:]
+ -[AAHIDDevice setIsSubscribed:]
+ -[AAHIDDevice setSensorInfo:]
+ -[AAManufacturerDataAdvertisement .cxx_destruct]
+ -[AAManufacturerDataAdvertisement _parsePayloads]
+ -[AAManufacturerDataAdvertisement companyID]
+ -[AAManufacturerDataAdvertisement hash]
+ -[AAManufacturerDataAdvertisement initWithData:]
+ -[AAManufacturerDataAdvertisement initWithData:].cold.1
+ -[AAManufacturerDataAdvertisement isEqual:]
+ -[AAManufacturerDataAdvertisement isEqualToAdvertisement:]
+ -[AAManufacturerDataAdvertisement manufacturerData]
+ -[AAManufacturerDataAdvertisement payloads]
+ -[AAOVADSensorInfo _calculateOwnVoiceActivityLevel]
+ -[AAOVADSensorInfo clearData]
+ -[AAOVADSensorInfo initWithHIDDevice:]
+ -[AAOVADSensorInfo ownVoiceActivityLevel]
+ -[AAOVADSensorInfo setOwnVoiceActivityLevel:]
+ -[AAOVADSensorInfo update:]
+ -[AAOVADSensorInfo update:].cold.1
+ -[AAOVADSensorInfo update:].cold.2
+ -[AAOVADSensorInfo update:].cold.3
+ -[AAProxCardsInfo chargingRemindersVersion]
+ -[AAProxCardsInfo newChargingStatusVersion]
+ -[AAProxCardsInfo pauseMediaOnSleepVersion]
+ -[AAProxCardsInfo remoteCameraControlVersion]
+ -[AAProxCardsInfo setChargingRemindersVersion:]
+ -[AAProxCardsInfo setNewChargingStatusVersion:]
+ -[AAProxCardsInfo setPauseMediaOnSleepVersion:]
+ -[AAProxCardsInfo setRemoteCameraControlVersion:]
+ -[AAProximityPairingAccessoryStatusPayload battery1]
+ -[AAProximityPairingAccessoryStatusPayload battery2]
+ -[AAProximityPairingAccessoryStatusPayload battery3]
+ -[AAProximityPairingAccessoryStatusPayload caseBatteryCharging]
+ -[AAProximityPairingAccessoryStatusPayload caseBatteryLevel]
+ -[AAProximityPairingAccessoryStatusPayload caseBatteryValid]
+ -[AAProximityPairingAccessoryStatusPayload chargingOBC]
+ -[AAProximityPairingAccessoryStatusPayload connected]
+ -[AAProximityPairingAccessoryStatusPayload describeProperties]
+ -[AAProximityPairingAccessoryStatusPayload faultDetected]
+ -[AAProximityPairingAccessoryStatusPayload firmwareVersionRaw]
+ -[AAProximityPairingAccessoryStatusPayload firmwareVersion]
+ -[AAProximityPairingAccessoryStatusPayload initWithData:]
+ -[AAProximityPairingAccessoryStatusPayload leftBatteryCharging]
+ -[AAProximityPairingAccessoryStatusPayload leftBatteryLevel]
+ -[AAProximityPairingAccessoryStatusPayload leftBatteryValid]
+ -[AAProximityPairingAccessoryStatusPayload lidClosed]
+ -[AAProximityPairingAccessoryStatusPayload lidOpenCount]
+ -[AAProximityPairingAccessoryStatusPayload needsConnection]
+ -[AAProximityPairingAccessoryStatusPayload reserved]
+ -[AAProximityPairingAccessoryStatusPayload rightBatteryCharging]
+ -[AAProximityPairingAccessoryStatusPayload rightBatteryLevel]
+ -[AAProximityPairingAccessoryStatusPayload rightBatteryValid]
+ -[AAProximityPairingAccessoryStatusPayload soundEnabled]
+ -[AAProximityPairingAccessoryStatusPayload status2]
+ -[AAProximityPairingAccessoryStatusPayload statusFlags1]
+ -[AAProximityPairingAccessoryStatusPayload timeUntilCharged]
+ -[AAProximityPairingPayload describeProperties]
+ -[AAProximityPairingPayload initWithData:]
+ -[AAProximityPairingPayload pid]
+ -[AAProximityPairingPayload subType]
+ -[AAProximityPairingStatusPayloadB188B288 caseLedColor]
+ -[AAProximityPairingStatusPayloadB188B288 caseLedStatus]
+ -[AAProximityPairingStatusPayloadB188B288 caseVersion]
+ -[AAProximityPairingStatusPayloadB188B288 color]
+ -[AAProximityPairingStatusPayloadB188B288 describeProperties]
+ -[AAProximityPairingStatusPayloadB188B288 lidClosed]
+ -[AAProximityPairingStatusPayloadB188B288 lidOpenCount]
+ -[AAProximityPairingStatusPayloadB444 caseColor]
+ -[AAProximityPairingStatusPayloadB444 colorBest]
+ -[AAProximityPairingStatusPayloadB444 describeProperties]
+ -[AAProximityPairingStatusPayloadB444 leftColor]
+ -[AAProximityPairingStatusPayloadB444 rightColor]
+ -[AAProximityPairingStatusPayloadB463 colorBest]
+ -[AAProximityPairingStatusPayloadB463 color]
+ -[AAProximityPairingStatusPayloadB463 describeProperties]
+ -[AAProximityPairingStatusPayloadB515 caseLedColor]
+ -[AAProximityPairingStatusPayloadB515 colorBest]
+ -[AAProximityPairingStatusPayloadB515 cupColor]
+ -[AAProximityPairingStatusPayloadB515 describeProperties]
+ -[AAProximityPairingStatusPayloadB515 lidOpenCount]
+ -[AAProximityPairingStatusPayloadB515 mainBatteryCharging]
+ -[AAProximityPairingStatusPayloadB515 mainBatteryLevel]
+ -[AAProximityPairingStatusPayloadB515 mainBatteryValid]
+ -[AAProximityPairingStatusPayloadB515 outOfBoxMode]
+ -[AAProximityPairingStatusPayloadB515 primaryLocation]
+ -[AAProximityPairingStatusPayloadB515 showProxStatus]
+ -[AAProximityPairingStatusPayloadB515 unsupportedAccessoryConnected]
+ -[AAProximityPairingStatusPayloadB515c describeProperties]
+ -[AAProximityPairingStatusPayloadB515c primaryLocation]
+ -[AAProximityPairingStatusPayloadB515c usbAudioConnected]
+ -[AAProximityPairingStatusPayloadBeatsUntethered caseLedColor]
+ -[AAProximityPairingStatusPayloadBeatsUntethered caseLedStatus]
+ -[AAProximityPairingStatusPayloadBeatsUntethered caseVersion]
+ -[AAProximityPairingStatusPayloadBeatsUntethered describeProperties]
+ -[AAProximityPairingStatusPayloadBeatsUntethered lidClosed]
+ -[AAProximityPairingStatusPayloadBeatsUntethered lidOpenCount]
+ -[AAProximityPairingStatusPayloadGeneral .cxx_destruct]
+ -[AAProximityPairingStatusPayloadGeneral audioState]
+ -[AAProximityPairingStatusPayloadGeneral battery1]
+ -[AAProximityPairingStatusPayloadGeneral battery2]
+ -[AAProximityPairingStatusPayloadGeneral battery3]
+ -[AAProximityPairingStatusPayloadGeneral battery4]
+ -[AAProximityPairingStatusPayloadGeneral battery5]
+ -[AAProximityPairingStatusPayloadGeneral caseBatteryCharging]
+ -[AAProximityPairingStatusPayloadGeneral caseBatteryLevel]
+ -[AAProximityPairingStatusPayloadGeneral caseBatteryValid]
+ -[AAProximityPairingStatusPayloadGeneral chargingOBC]
+ -[AAProximityPairingStatusPayloadGeneral colorBest]
+ -[AAProximityPairingStatusPayloadGeneral colorRaw]
+ -[AAProximityPairingStatusPayloadGeneral connectedSourceCount]
+ -[AAProximityPairingStatusPayloadGeneral describeProperties]
+ -[AAProximityPairingStatusPayloadGeneral idleTime]
+ -[AAProximityPairingStatusPayloadGeneral initWithData:]
+ -[AAProximityPairingStatusPayloadGeneral lastBudInCaseWithCurrentBud]
+ -[AAProximityPairingStatusPayloadGeneral lastConnectedHostSignedInToICloud]
+ -[AAProximityPairingStatusPayloadGeneral lastConnectedHost]
+ -[AAProximityPairingStatusPayloadGeneral misc1]
+ -[AAProximityPairingStatusPayloadGeneral myBatteryCharging]
+ -[AAProximityPairingStatusPayloadGeneral myBatteryLevel]
+ -[AAProximityPairingStatusPayloadGeneral myBatteryValid]
+ -[AAProximityPairingStatusPayloadGeneral otherBatteryCharging]
+ -[AAProximityPairingStatusPayloadGeneral otherBatteryLevel]
+ -[AAProximityPairingStatusPayloadGeneral otherBatteryValid]
+ -[AAProximityPairingStatusPayloadGeneral outOfCaseTime]
+ -[AAProximityPairingStatusPayloadGeneral smartRoutingConnected]
+ -[AAProximityPairingStatusPayloadGeneral smartRoutingScoreSource1]
+ -[AAProximityPairingStatusPayloadGeneral smartRoutingScoreSource2]
+ -[AAProximityPairingStatusPayloadGeneral status1]
+ -[AAProximityPairingStatusPayloadGeneral status2]
+ -[AAProximityPairingStatusPayloadGeneral status3]
+ -[AAProximityPairingStatusPayloadGeneral status4]
+ -[AAProximityPairingStatusPayloadGeneral status5]
+ -[AAProximityPairingStatusPayloadGeneral supportWirelessSplitter]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase color]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase describeProperties]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase lidOpenCount]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase mainBatteryCharging]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase mainBatteryLevel]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase mainBatteryValid]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase outOfBoxMode]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase primaryLocation]
+ -[AAProximityPairingStatusPayloadOtherTetheredNonCase showProxStatus]
+ -[AAProximityPairingStatusPayloadUntethered budRole]
+ -[AAProximityPairingStatusPayloadUntethered budSide]
+ -[AAProximityPairingStatusPayloadUntethered describeProperties]
+ -[AAProximityPairingStatusPayloadUntethered leftBatteryCharging]
+ -[AAProximityPairingStatusPayloadUntethered leftBatteryLevel]
+ -[AAProximityPairingStatusPayloadUntethered leftBatteryValid]
+ -[AAProximityPairingStatusPayloadUntethered outOfBoxMode]
+ -[AAProximityPairingStatusPayloadUntethered primaryLocation]
+ -[AAProximityPairingStatusPayloadUntethered rightBatteryCharging]
+ -[AAProximityPairingStatusPayloadUntethered rightBatteryLevel]
+ -[AAProximityPairingStatusPayloadUntethered rightBatteryValid]
+ -[AAProximityPairingStatusPayloadUntethered secondaryLocation]
+ -[AAProximityPairingStatusPayloadUntethered utpConnected]
+ -[AASensorInfo .cxx_destruct]
+ -[AASensorInfo btAddress]
+ -[AASensorInfo clearData]
+ -[AASensorInfo initWithHIDDevice:]
+ -[AASensorInfo pid]
+ -[AASensorInfo setPid:]
+ -[AASensorInfo transport]
+ -[AASensorInfo update:]
+ -[AASensorInfo usagePage]
+ -[AASensorInfo usage]
+ -[AASensorService .cxx_destruct]
+ -[AASensorService _getBTAddressFromHIDDeviceObject:]
+ -[AASensorService _notifyAvailabilityChangedWithForcedUpdate:]
+ -[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]
+ -[AASensorService _sensorDataAvailabilitiesAdded:]
+ -[AASensorService _sensorDataAvailabilitiesLost:]
+ -[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]
+ -[AASensorService activate]
+ -[AASensorService btAddress]
+ -[AASensorService deviceDiscoveryTimeout]
+ -[AASensorService deviceManagerFoundHandler:]
+ -[AASensorService deviceNotificationHandler:added:]
+ -[AASensorService dispatchQueue]
+ -[AASensorService handleHIDReport:data:]
+ -[AASensorService init]
+ -[AASensorService invalidate]
+ -[AASensorService sensorAvailabilityUpdatedHandler]
+ -[AASensorService sensorDataInfoUpdatedHandler]
+ -[AASensorService setBtAddress:]
+ -[AASensorService setDeviceDiscoveryTimeout:]
+ -[AASensorService setDispatchQueue:]
+ -[AASensorService setSensorAvailabilityUpdatedHandler:]
+ -[AASensorService setSensorDataInfoUpdatedHandler:]
+ -[AASensorService setSubscriptionTimeout:]
+ -[AASensorService subscribeWithFlags:]
+ -[AASensorService subscribeWithFlags:rate:]
+ -[AASensorService subscribeWithFlagsWithCompletion:completion:]
+ -[AASensorService subscribeWithFlagsWithCompletion:rate:completion:]
+ -[AASensorService subscribeWithSensorDataFlags:completion:]
+ -[AASensorService subscribeWithSensorDataFlags:rate:completion:]
+ -[AASensorService subscriptionTimeout]
+ -[AASensorService unsubscribeAll]
+ -[AASensorService unsubscribeWithFlags:]
+ -[AASensorService unsubscribeWithSensorDataFlags:]
+ -[AASettingsTelemetry .cxx_destruct]
+ -[AASettingsTelemetry _sendSettingsChanges:device:]
+ -[AASettingsTelemetry _sendSettingsChanges:device:].cold.1
+ -[AASettingsTelemetry _submitFeaturesChangeMetrics:forFeature:forDevice:]
+ -[AASettingsTelemetry dispatchQueue]
+ -[AASettingsTelemetry init]
+ -[AASettingsTelemetry sendSettingsChanges:device:]
+ -[AASettingsTelemetry setDispatchQueue:]
+ -[AASystemStateMonitor _deviceWithIdentifier:]
+ -[AASystemStateMonitor activeHRMDeviceChanged:]
+ -[AASystemStateMonitor activeHRMDeviceChanged:withSREnabled:]
+ -[AASystemStateMonitor activeHRMDevice]
+ -[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]
+ -[AASystemStateMonitor fetchPairedHRMDevices:]
+ -[AASystemStateMonitor fetchPairedHRMDevices:].cold.1
+ -[AASystemStateMonitor fetchPairedHRMDevices:].cold.2
+ -[AASystemStateMonitor hrmCapableDeviceRoutedStateChangedHandler]
+ -[AASystemStateMonitor isSystemEligibleForSiriHijack]
+ -[AASystemStateMonitor setHrmCapableDeviceRoutedStateChangedHandler:]
+ -[AASystemStateMonitor setSiriHijackEligibilityUpdatedHandler:]
+ -[AASystemStateMonitor showFitEducationNotificationForDevice:]
+ -[AASystemStateMonitor showFitEducationNotificationForDevice:].cold.1
+ -[AASystemStateMonitor showFitEducationNotificationForDevice:].cold.2
+ -[AASystemStateMonitor showFitEducationNotificationForDevice:].cold.3
+ -[AASystemStateMonitor siriHijackEligibilityUpdated:]
+ -[AASystemStateMonitor siriHijackEligibilityUpdated:].cold.1
+ -[AASystemStateMonitor siriHijackEligibilityUpdatedHandler]
+ -[AudioAccessoryDevice CBCapToAACap:]
+ -[AudioAccessoryDevice adaptiveVolumeCapability]
+ -[AudioAccessoryDevice adaptiveVolumeConfig]
+ -[AudioAccessoryDevice batteryInfo]
+ -[AudioAccessoryDevice cameraControlCapability]
+ -[AudioAccessoryDevice chargingReminderCapability]
+ -[AudioAccessoryDevice chargingReminderEnabled]
+ -[AudioAccessoryDevice classicRSSI]
+ -[AudioAccessoryDevice clickHoldModeLeft]
+ -[AudioAccessoryDevice clickHoldModeRight]
+ -[AudioAccessoryDevice cloudRecordInfoLoaded]
+ -[AudioAccessoryDevice connectedAADeviceInfoReceived]
+ -[AudioAccessoryDevice connectedCBDeviceReceived]
+ -[AudioAccessoryDevice connectedInfoComplete]
+ -[AudioAccessoryDevice connected]
+ -[AudioAccessoryDevice conversationDetectCapability]
+ -[AudioAccessoryDevice conversationDetectConfig]
+ -[AudioAccessoryDevice copyWithZone:]
+ -[AudioAccessoryDevice crownRotationDirection]
+ -[AudioAccessoryDevice doubleTapActionLeft]
+ -[AudioAccessoryDevice doubleTapActionRight]
+ -[AudioAccessoryDevice doubleTapCapability]
+ -[AudioAccessoryDevice endCallCapability]
+ -[AudioAccessoryDevice endCallConfig]
+ -[AudioAccessoryDevice enhancedTransparencyVersion]
+ -[AudioAccessoryDevice farFieldUplinkCapability]
+ -[AudioAccessoryDevice gapaFlags]
+ -[AudioAccessoryDevice guestPaired]
+ -[AudioAccessoryDevice healthKitDataWriteAllowed]
+ -[AudioAccessoryDevice lastSeenConnectedTime]
+ -[AudioAccessoryDevice microphoneMode]
+ -[AudioAccessoryDevice model]
+ -[AudioAccessoryDevice muteControlCapability]
+ -[AudioAccessoryDevice muteControlConfig]
+ -[AudioAccessoryDevice name]
+ -[AudioAccessoryDevice onConnectionActionsCalled]
+ -[AudioAccessoryDevice optimizedBatteryChargingCapability]
+ -[AudioAccessoryDevice optimizedBatteryChargingState]
+ -[AudioAccessoryDevice ovadStreamingCapability]
+ -[AudioAccessoryDevice pairedAADeviceInfoReceived]
+ -[AudioAccessoryDevice pairedCBDeviceReceived]
+ -[AudioAccessoryDevice pairedInfoComplete]
+ -[AudioAccessoryDevice paired]
+ -[AudioAccessoryDevice peerAutoANCCapability]
+ -[AudioAccessoryDevice pmeEverywhereCapability]
+ -[AudioAccessoryDevice productID]
+ -[AudioAccessoryDevice productName]
+ -[AudioAccessoryDevice rawGesturesConfigFlags]
+ -[AudioAccessoryDevice remoteCameraControlConfig]
+ -[AudioAccessoryDevice selectiveSpeechListeningCapability]
+ -[AudioAccessoryDevice selectiveSpeechListeningConfig]
+ -[AudioAccessoryDevice serialNumberLeft]
+ -[AudioAccessoryDevice serialNumberRight]
+ -[AudioAccessoryDevice serialNumber]
+ -[AudioAccessoryDevice setAdaptiveVolumeCapability:]
+ -[AudioAccessoryDevice setAdaptiveVolumeConfig:]
+ -[AudioAccessoryDevice setBatteryInfo:]
+ -[AudioAccessoryDevice setCameraControlCapability:]
+ -[AudioAccessoryDevice setChargingReminderCapability:]
+ -[AudioAccessoryDevice setChargingReminderEnabled:]
+ -[AudioAccessoryDevice setClassicRSSI:]
+ -[AudioAccessoryDevice setClickHoldModeLeft:]
+ -[AudioAccessoryDevice setClickHoldModeRight:]
+ -[AudioAccessoryDevice setCloudRecordInfoLoaded:]
+ -[AudioAccessoryDevice setConnected:]
+ -[AudioAccessoryDevice setConnectedAADeviceInfoReceived:]
+ -[AudioAccessoryDevice setConnectedCBDeviceReceived:]
+ -[AudioAccessoryDevice setConversationDetectCapability:]
+ -[AudioAccessoryDevice setConversationDetectConfig:]
+ -[AudioAccessoryDevice setCrownRotationDirection:]
+ -[AudioAccessoryDevice setDefaultConfigurationsForCloudSyncedPropertiesIfNeeded]
+ -[AudioAccessoryDevice setDoubleTapActionLeft:]
+ -[AudioAccessoryDevice setDoubleTapActionRight:]
+ -[AudioAccessoryDevice setDoubleTapCapability:]
+ -[AudioAccessoryDevice setEndCallCapability:]
+ -[AudioAccessoryDevice setEndCallConfig:]
+ -[AudioAccessoryDevice setEnhancedTransparencyVersion:]
+ -[AudioAccessoryDevice setFarFieldUplinkCapability:]
+ -[AudioAccessoryDevice setGapaFlags:]
+ -[AudioAccessoryDevice setGuestPaired:]
+ -[AudioAccessoryDevice setHealthKitDataWriteAllowed:]
+ -[AudioAccessoryDevice setLastSeenConnectedTime:]
+ -[AudioAccessoryDevice setMicrophoneMode:]
+ -[AudioAccessoryDevice setModel:]
+ -[AudioAccessoryDevice setMuteControlCapability:]
+ -[AudioAccessoryDevice setMuteControlConfig:]
+ -[AudioAccessoryDevice setName:]
+ -[AudioAccessoryDevice setOnConnectionActionsCalled:]
+ -[AudioAccessoryDevice setOptimizedBatteryChargingCapability:]
+ -[AudioAccessoryDevice setOptimizedBatteryChargingState:]
+ -[AudioAccessoryDevice setOvadStreamingCapability:]
+ -[AudioAccessoryDevice setPaired:]
+ -[AudioAccessoryDevice setPairedAADeviceInfoReceived:]
+ -[AudioAccessoryDevice setPairedCBDeviceReceived:]
+ -[AudioAccessoryDevice setPeerAutoANCCapability:]
+ -[AudioAccessoryDevice setPmeEverywhereCapability:]
+ -[AudioAccessoryDevice setProductID:]
+ -[AudioAccessoryDevice setProductName:]
+ -[AudioAccessoryDevice setRawGesturesConfigFlags:]
+ -[AudioAccessoryDevice setRemoteCameraControlConfig:]
+ -[AudioAccessoryDevice setRouted:]
+ -[AudioAccessoryDevice setSelectiveSpeechListeningCapability:]
+ -[AudioAccessoryDevice setSelectiveSpeechListeningConfig:]
+ -[AudioAccessoryDevice setSerialNumber:]
+ -[AudioAccessoryDevice setSerialNumberLeft:]
+ -[AudioAccessoryDevice setSerialNumberRight:]
+ -[AudioAccessoryDevice setSleepDetectionCapability:]
+ -[AudioAccessoryDevice setSleepDetectionEnabled:]
+ -[AudioAccessoryDevice setSmartRoutingCapability:]
+ -[AudioAccessoryDevice setSmartRoutingMode:]
+ -[AudioAccessoryDevice setSpatialAudioAllowed:]
+ -[AudioAccessoryDevice setTemporaryManagedPairedStatus:]
+ -[AudioAccessoryDevice setVendorID:]
+ -[AudioAccessoryDevice sleepDetectionCapability]
+ -[AudioAccessoryDevice sleepDetectionEnabled]
+ -[AudioAccessoryDevice smartRoutingCapability]
+ -[AudioAccessoryDevice smartRoutingMode]
+ -[AudioAccessoryDevice spatialAudioAllowed]
+ -[AudioAccessoryDevice temporaryManagedPairedStatus]
+ -[AudioAccessoryDevice updateWithAADeviceConfig:]
+ -[AudioAccessoryDevice updateWithConnectedAADeviceInfo:]
+ -[AudioAccessoryDevice updateWithConnectedCBDevice:]
+ -[AudioAccessoryDevice updateWithPairedAADevice:]
+ -[AudioAccessoryDevice updateWithPairedAADeviceInfo:]
+ -[AudioAccessoryDevice updateWithPairedCBDevice:]
+ -[AudioAccessoryDevice vendorID]
+ -[BTAudioRoutingRequest reason]
+ -[BTAudioRoutingRequest setReason:]
+ -[BTServicesClient showHIDConnectedBannerAperture:completion:]
+ GCC_except_table11
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table56
+ _CBDeviceTypeToNSLocalizedString
+ _CUMetricsLog
+ _CUPrintDateCF
+ _NSDataWithHex
+ _NSPrintF
+ _OBJC_CLASS_$_AAAdvertisementPayload
+ _OBJC_CLASS_$_AABattery
+ _OBJC_CLASS_$_AADeviceBatteryInfo
+ _OBJC_CLASS_$_AAHIDDevice
+ _OBJC_CLASS_$_AAManufacturerDataAdvertisement
+ _OBJC_CLASS_$_AAOVADSensorInfo
+ _OBJC_CLASS_$_AAProximityPairingAccessoryStatusPayload
+ _OBJC_CLASS_$_AAProximityPairingPayload
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadB188B288
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadB444
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadB463
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadB515
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadB515c
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadBeatsUntethered
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadGeneral
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ _OBJC_CLASS_$_AAProximityPairingStatusPayloadUntethered
+ _OBJC_CLASS_$_AASensorInfo
+ _OBJC_CLASS_$_AASensorService
+ _OBJC_CLASS_$_AASettingsTelemetry
+ _OBJC_CLASS_$_CBProductInfo
+ _OBJC_CLASS_$_HIDManager
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_IVAR_$_AAAdvertisementPayload._payloadData
+ _OBJC_IVAR_$_AAAdvertisementPayload._type
+ _OBJC_IVAR_$_AABattery._chargingOBCTimeUntilCharged
+ _OBJC_IVAR_$_AABattery._lastOrigin
+ _OBJC_IVAR_$_AABattery._lastSeen
+ _OBJC_IVAR_$_AABattery._level
+ _OBJC_IVAR_$_AABattery._productID
+ _OBJC_IVAR_$_AABattery._sourceFlags
+ _OBJC_IVAR_$_AABattery._state
+ _OBJC_IVAR_$_AABattery._type
+ _OBJC_IVAR_$_AAController._accessoryUsageSummaryMessageHandler
+ _OBJC_IVAR_$_AAController._batteryInfoMessageHandler
+ _OBJC_IVAR_$_AAController._rawGestureMessageHandler
+ _OBJC_IVAR_$_AAController._sleepDetectionMessageHandler
+ _OBJC_IVAR_$_AADeviceBatteryInfo._batteryMap
+ _OBJC_IVAR_$_AADeviceBatteryInfo._bluetoothAddress
+ _OBJC_IVAR_$_AADeviceBatteryInfo._caseIdentifier
+ _OBJC_IVAR_$_AADeviceBatteryInfo._caseLedColor
+ _OBJC_IVAR_$_AADeviceBatteryInfo._caseLedStatus
+ _OBJC_IVAR_$_AADeviceBatteryInfo._caseVersion
+ _OBJC_IVAR_$_AADeviceBatteryInfo._color
+ _OBJC_IVAR_$_AADeviceBatteryInfo._findMyGroupIdentifier
+ _OBJC_IVAR_$_AADeviceBatteryInfo._identifier
+ _OBJC_IVAR_$_AADeviceBatteryInfo._isConnected
+ _OBJC_IVAR_$_AADeviceBatteryInfo._isNearby
+ _OBJC_IVAR_$_AADeviceBatteryInfo._model
+ _OBJC_IVAR_$_AADeviceBatteryInfo._name
+ _OBJC_IVAR_$_AADeviceBatteryInfo._productID
+ _OBJC_IVAR_$_AADeviceConfig._allowHealthKitDataWrite
+ _OBJC_IVAR_$_AADeviceConfig._allowTemporaryManagedPairing
+ _OBJC_IVAR_$_AADeviceConfig._changeOptimizedBatteryChargingState
+ _OBJC_IVAR_$_AADeviceConfig._enableChargingReminder
+ _OBJC_IVAR_$_AADeviceConfig._enableSleepDetection
+ _OBJC_IVAR_$_AADeviceConfig._rawGesturesConfigFlags
+ _OBJC_IVAR_$_AADeviceConfig._remoteCameraControlConfig
+ _OBJC_IVAR_$_AADeviceManager._batteryDictionary
+ _OBJC_IVAR_$_AADeviceManager._deviceBatteryInfoLostHandler
+ _OBJC_IVAR_$_AADeviceManager._deviceBatteryInfoUpdatedHandler
+ _OBJC_IVAR_$_AADeviceManager._internalServicesDaemon
+ _OBJC_IVAR_$_AAHIDDevice._hidDevice
+ _OBJC_IVAR_$_AAHIDDevice._isSetupComplete
+ _OBJC_IVAR_$_AAHIDDevice._isSubscribed
+ _OBJC_IVAR_$_AAHIDDevice._sensorInfo
+ _OBJC_IVAR_$_AAManufacturerDataAdvertisement._companyID
+ _OBJC_IVAR_$_AAManufacturerDataAdvertisement._manufacturerData
+ _OBJC_IVAR_$_AAManufacturerDataAdvertisement._payloads
+ _OBJC_IVAR_$_AAOVADSensorInfo._ownVoiceActivityLevel
+ _OBJC_IVAR_$_AAOVADSensorInfo._rawOwnVoiceActivityLevel
+ _OBJC_IVAR_$_AAOVADSensorInfo._threshold
+ _OBJC_IVAR_$_AAProxCardsInfo._chargingRemindersVersion
+ _OBJC_IVAR_$_AAProxCardsInfo._newChargingStatusVersion
+ _OBJC_IVAR_$_AAProxCardsInfo._pauseMediaOnSleepVersion
+ _OBJC_IVAR_$_AAProxCardsInfo._remoteCameraControlVersion
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._battery1
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._battery2
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._battery3
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._firmwareVersionRaw
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._reserved
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._status2
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._statusFlags1
+ _OBJC_IVAR_$_AAProximityPairingAccessoryStatusPayload._timeUntilCharged
+ _OBJC_IVAR_$_AAProximityPairingPayload._pid
+ _OBJC_IVAR_$_AAProximityPairingPayload._subType
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._battery1
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._battery2
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._battery3
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._battery4
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._battery5
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._colorRaw
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._lastBudInCaseWithCurrentBud
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._lastConnectedHost
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._misc1
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._status1
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._status2
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._status3
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._status4
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadGeneral._status5
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadOtherTetheredNonCase._lidOpenCount
+ _OBJC_IVAR_$_AAProximityPairingStatusPayloadOtherTetheredNonCase._showProxStatus
+ _OBJC_IVAR_$_AASensorInfo._btAddress
+ _OBJC_IVAR_$_AASensorInfo._pid
+ _OBJC_IVAR_$_AASensorInfo._transport
+ _OBJC_IVAR_$_AASensorInfo._usage
+ _OBJC_IVAR_$_AASensorInfo._usagePage
+ _OBJC_IVAR_$_AASensorService._aaDeviceManager
+ _OBJC_IVAR_$_AASensorService._activateCalled
+ _OBJC_IVAR_$_AASensorService._availableSensors
+ _OBJC_IVAR_$_AASensorService._availableSensorsLastNotified
+ _OBJC_IVAR_$_AASensorService._availableSensorsLostDelayedNotificationTimer
+ _OBJC_IVAR_$_AASensorService._btAddress
+ _OBJC_IVAR_$_AASensorService._btAddressToPIDDict
+ _OBJC_IVAR_$_AASensorService._deviceDiscoveryTimeout
+ _OBJC_IVAR_$_AASensorService._discoveryTimer
+ _OBJC_IVAR_$_AASensorService._dispatchQueue
+ _OBJC_IVAR_$_AASensorService._hidManager
+ _OBJC_IVAR_$_AASensorService._ovadAAHIDDeviceDict
+ _OBJC_IVAR_$_AASensorService._requestedSensorRates
+ _OBJC_IVAR_$_AASensorService._sensorAvailabilityUpdatedHandler
+ _OBJC_IVAR_$_AASensorService._sensorDataInfoUpdatedHandler
+ _OBJC_IVAR_$_AASensorService._subscriptionErrorHandler
+ _OBJC_IVAR_$_AASensorService._subscriptionTimeout
+ _OBJC_IVAR_$_AASensorService._subscriptionTimer
+ _OBJC_IVAR_$_AASettingsTelemetry._dispatchQueue
+ _OBJC_IVAR_$_AASystemStateMonitor._activeHRMDevice
+ _OBJC_IVAR_$_AASystemStateMonitor._hrmCapableDeviceRoutedStateChangedHandler
+ _OBJC_IVAR_$_AASystemStateMonitor._isSREnabled
+ _OBJC_IVAR_$_AASystemStateMonitor._isSystemEligibleForSiriHijack
+ _OBJC_IVAR_$_AASystemStateMonitor._siriHijackEligibilityUpdatedHandler
+ _OBJC_IVAR_$_AudioAccessoryDevice._adaptiveVolumeCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._adaptiveVolumeConfig
+ _OBJC_IVAR_$_AudioAccessoryDevice._batteryInfo
+ _OBJC_IVAR_$_AudioAccessoryDevice._cameraControlCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._chargingReminderCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._chargingReminderEnabled
+ _OBJC_IVAR_$_AudioAccessoryDevice._classicRSSI
+ _OBJC_IVAR_$_AudioAccessoryDevice._clickHoldModeLeft
+ _OBJC_IVAR_$_AudioAccessoryDevice._clickHoldModeRight
+ _OBJC_IVAR_$_AudioAccessoryDevice._cloudRecordInfoLoaded
+ _OBJC_IVAR_$_AudioAccessoryDevice._connected
+ _OBJC_IVAR_$_AudioAccessoryDevice._connectedAADeviceInfoReceived
+ _OBJC_IVAR_$_AudioAccessoryDevice._connectedCBDeviceReceived
+ _OBJC_IVAR_$_AudioAccessoryDevice._conversationDetectCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._conversationDetectConfig
+ _OBJC_IVAR_$_AudioAccessoryDevice._crownRotationDirection
+ _OBJC_IVAR_$_AudioAccessoryDevice._doubleTapActionLeft
+ _OBJC_IVAR_$_AudioAccessoryDevice._doubleTapActionRight
+ _OBJC_IVAR_$_AudioAccessoryDevice._doubleTapCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._endCallCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._endCallConfig
+ _OBJC_IVAR_$_AudioAccessoryDevice._enhancedTransparencyVersion
+ _OBJC_IVAR_$_AudioAccessoryDevice._farFieldUplinkCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._gapaFlags
+ _OBJC_IVAR_$_AudioAccessoryDevice._guestPaired
+ _OBJC_IVAR_$_AudioAccessoryDevice._healthKitDataWriteAllowed
+ _OBJC_IVAR_$_AudioAccessoryDevice._lastSeenConnectedTime
+ _OBJC_IVAR_$_AudioAccessoryDevice._microphoneMode
+ _OBJC_IVAR_$_AudioAccessoryDevice._model
+ _OBJC_IVAR_$_AudioAccessoryDevice._muteControlCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._muteControlConfig
+ _OBJC_IVAR_$_AudioAccessoryDevice._name
+ _OBJC_IVAR_$_AudioAccessoryDevice._onConnectionActionsCalled
+ _OBJC_IVAR_$_AudioAccessoryDevice._optimizedBatteryChargingCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._optimizedBatteryChargingState
+ _OBJC_IVAR_$_AudioAccessoryDevice._ovadStreamingCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._paired
+ _OBJC_IVAR_$_AudioAccessoryDevice._pairedAADeviceInfoReceived
+ _OBJC_IVAR_$_AudioAccessoryDevice._pairedCBDeviceReceived
+ _OBJC_IVAR_$_AudioAccessoryDevice._peerAutoANCCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._pmeEverywhereCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._productID
+ _OBJC_IVAR_$_AudioAccessoryDevice._productName
+ _OBJC_IVAR_$_AudioAccessoryDevice._rawGesturesConfigFlags
+ _OBJC_IVAR_$_AudioAccessoryDevice._remoteCameraControlConfig
+ _OBJC_IVAR_$_AudioAccessoryDevice._routed
+ _OBJC_IVAR_$_AudioAccessoryDevice._selectiveSpeechListeningCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._selectiveSpeechListeningConfig
+ _OBJC_IVAR_$_AudioAccessoryDevice._serialNumber
+ _OBJC_IVAR_$_AudioAccessoryDevice._serialNumberLeft
+ _OBJC_IVAR_$_AudioAccessoryDevice._serialNumberRight
+ _OBJC_IVAR_$_AudioAccessoryDevice._sleepDetectionCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._sleepDetectionEnabled
+ _OBJC_IVAR_$_AudioAccessoryDevice._smartRoutingCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._smartRoutingMode
+ _OBJC_IVAR_$_AudioAccessoryDevice._spatialAudioAllowed
+ _OBJC_IVAR_$_AudioAccessoryDevice._temporaryManagedPairedStatus
+ _OBJC_IVAR_$_AudioAccessoryDevice._vendorID
+ _OBJC_IVAR_$_BTAudioRoutingRequest._reason
+ _OBJC_METACLASS_$_AAAdvertisementPayload
+ _OBJC_METACLASS_$_AABattery
+ _OBJC_METACLASS_$_AADeviceBatteryInfo
+ _OBJC_METACLASS_$_AAHIDDevice
+ _OBJC_METACLASS_$_AAManufacturerDataAdvertisement
+ _OBJC_METACLASS_$_AAOVADSensorInfo
+ _OBJC_METACLASS_$_AAProximityPairingAccessoryStatusPayload
+ _OBJC_METACLASS_$_AAProximityPairingPayload
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadB188B288
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadB444
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadB463
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadB515
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadB515c
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadBeatsUntethered
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadGeneral
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ _OBJC_METACLASS_$_AAProximityPairingStatusPayloadUntethered
+ _OBJC_METACLASS_$_AASensorInfo
+ _OBJC_METACLASS_$_AASensorService
+ _OBJC_METACLASS_$_AASettingsTelemetry
+ _ShorthandString
+ __OBJC_$_CLASS_METHODS_AAAdvertisementPayload
+ __OBJC_$_CLASS_METHODS_AABattery
+ __OBJC_$_CLASS_METHODS_AADeviceBatteryInfo
+ __OBJC_$_CLASS_METHODS_AAManufacturerDataAdvertisement
+ __OBJC_$_CLASS_METHODS_AAProximityPairingPayload
+ __OBJC_$_CLASS_METHODS_AAProximityPairingStatusPayloadB188B288
+ __OBJC_$_CLASS_METHODS_AAProximityPairingStatusPayloadB444
+ __OBJC_$_CLASS_METHODS_AAProximityPairingStatusPayloadB463
+ __OBJC_$_CLASS_METHODS_AAProximityPairingStatusPayloadB515
+ __OBJC_$_CLASS_METHODS_AAProximityPairingStatusPayloadB515c
+ __OBJC_$_CLASS_METHODS_AAProximityPairingStatusPayloadGeneral
+ __OBJC_$_CLASS_METHODS_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ __OBJC_$_CLASS_METHODS_AASettingsTelemetry
+ __OBJC_$_CLASS_PROP_LIST_AABattery
+ __OBJC_$_CLASS_PROP_LIST_AADeviceBatteryInfo
+ __OBJC_$_INSTANCE_METHODS_AAAdvertisementPayload
+ __OBJC_$_INSTANCE_METHODS_AABattery
+ __OBJC_$_INSTANCE_METHODS_AADeviceBatteryInfo
+ __OBJC_$_INSTANCE_METHODS_AAHIDDevice
+ __OBJC_$_INSTANCE_METHODS_AAManufacturerDataAdvertisement
+ __OBJC_$_INSTANCE_METHODS_AAOVADSensorInfo
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingAccessoryStatusPayload
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingPayload
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadB188B288
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadB444
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadB463
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadB515
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadB515c
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadBeatsUntethered
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadGeneral
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ __OBJC_$_INSTANCE_METHODS_AAProximityPairingStatusPayloadUntethered
+ __OBJC_$_INSTANCE_METHODS_AASensorInfo
+ __OBJC_$_INSTANCE_METHODS_AASensorService
+ __OBJC_$_INSTANCE_METHODS_AASettingsTelemetry
+ __OBJC_$_INSTANCE_VARIABLES_AAAdvertisementPayload
+ __OBJC_$_INSTANCE_VARIABLES_AABattery
+ __OBJC_$_INSTANCE_VARIABLES_AADeviceBatteryInfo
+ __OBJC_$_INSTANCE_VARIABLES_AAHIDDevice
+ __OBJC_$_INSTANCE_VARIABLES_AAManufacturerDataAdvertisement
+ __OBJC_$_INSTANCE_VARIABLES_AAOVADSensorInfo
+ __OBJC_$_INSTANCE_VARIABLES_AAProximityPairingAccessoryStatusPayload
+ __OBJC_$_INSTANCE_VARIABLES_AAProximityPairingPayload
+ __OBJC_$_INSTANCE_VARIABLES_AAProximityPairingStatusPayloadGeneral
+ __OBJC_$_INSTANCE_VARIABLES_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ __OBJC_$_INSTANCE_VARIABLES_AASensorInfo
+ __OBJC_$_INSTANCE_VARIABLES_AASensorService
+ __OBJC_$_INSTANCE_VARIABLES_AASettingsTelemetry
+ __OBJC_$_PROP_LIST_AAAdvertisementPayload
+ __OBJC_$_PROP_LIST_AABattery
+ __OBJC_$_PROP_LIST_AADeviceBatteryInfo
+ __OBJC_$_PROP_LIST_AAHIDDevice
+ __OBJC_$_PROP_LIST_AAManufacturerDataAdvertisement
+ __OBJC_$_PROP_LIST_AAOVADSensorInfo
+ __OBJC_$_PROP_LIST_AAProximityPairingAccessoryStatusPayload
+ __OBJC_$_PROP_LIST_AAProximityPairingPayload
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadB188B288
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadB444
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadB463
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadB515
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadB515c
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadBeatsUntethered
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadGeneral
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ __OBJC_$_PROP_LIST_AAProximityPairingStatusPayloadUntethered
+ __OBJC_$_PROP_LIST_AASensorInfo
+ __OBJC_$_PROP_LIST_AASensorService
+ __OBJC_$_PROP_LIST_AASettingsTelemetry
+ __OBJC_$_PROP_LIST_AATetheredProximityPairingPayload
+ __OBJC_$_PROP_LIST_AAUntetheredProximityPairingPayload
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AATetheredProximityPairingPayload
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAUntetheredProximityPairingPayload
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AATetheredProximityPairingPayload
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAUntetheredProximityPairingPayload
+ __OBJC_$_PROTOCOL_REFS_AATetheredProximityPairingPayload
+ __OBJC_$_PROTOCOL_REFS_AAUntetheredProximityPairingPayload
+ __OBJC_CLASS_PROTOCOLS_$_AABattery
+ __OBJC_CLASS_PROTOCOLS_$_AADeviceBatteryInfo
+ __OBJC_CLASS_PROTOCOLS_$_AAProximityPairingAccessoryStatusPayload
+ __OBJC_CLASS_PROTOCOLS_$_AAProximityPairingStatusPayloadB515
+ __OBJC_CLASS_PROTOCOLS_$_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ __OBJC_CLASS_PROTOCOLS_$_AAProximityPairingStatusPayloadUntethered
+ __OBJC_CLASS_RO_$_AAAdvertisementPayload
+ __OBJC_CLASS_RO_$_AABattery
+ __OBJC_CLASS_RO_$_AADeviceBatteryInfo
+ __OBJC_CLASS_RO_$_AAHIDDevice
+ __OBJC_CLASS_RO_$_AAManufacturerDataAdvertisement
+ __OBJC_CLASS_RO_$_AAOVADSensorInfo
+ __OBJC_CLASS_RO_$_AAProximityPairingAccessoryStatusPayload
+ __OBJC_CLASS_RO_$_AAProximityPairingPayload
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadB188B288
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadB444
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadB463
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadB515
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadB515c
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadBeatsUntethered
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadGeneral
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ __OBJC_CLASS_RO_$_AAProximityPairingStatusPayloadUntethered
+ __OBJC_CLASS_RO_$_AASensorInfo
+ __OBJC_CLASS_RO_$_AASensorService
+ __OBJC_CLASS_RO_$_AASettingsTelemetry
+ __OBJC_LABEL_PROTOCOL_$_AATetheredProximityPairingPayload
+ __OBJC_LABEL_PROTOCOL_$_AAUntetheredProximityPairingPayload
+ __OBJC_METACLASS_RO_$_AAAdvertisementPayload
+ __OBJC_METACLASS_RO_$_AABattery
+ __OBJC_METACLASS_RO_$_AADeviceBatteryInfo
+ __OBJC_METACLASS_RO_$_AAHIDDevice
+ __OBJC_METACLASS_RO_$_AAManufacturerDataAdvertisement
+ __OBJC_METACLASS_RO_$_AAOVADSensorInfo
+ __OBJC_METACLASS_RO_$_AAProximityPairingAccessoryStatusPayload
+ __OBJC_METACLASS_RO_$_AAProximityPairingPayload
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadB188B288
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadB444
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadB463
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadB515
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadB515c
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadBeatsUntethered
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadGeneral
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadOtherTetheredNonCase
+ __OBJC_METACLASS_RO_$_AAProximityPairingStatusPayloadUntethered
+ __OBJC_METACLASS_RO_$_AASensorInfo
+ __OBJC_METACLASS_RO_$_AASensorService
+ __OBJC_METACLASS_RO_$_AASettingsTelemetry
+ __OBJC_PROTOCOL_$_AATetheredProximityPairingPayload
+ __OBJC_PROTOCOL_$_AAUntetheredProximityPairingPayload
+ __OBJC_PROTOCOL_REFERENCE_$_AATetheredProximityPairingPayload
+ __OBJC_PROTOCOL_REFERENCE_$_AAUntetheredProximityPairingPayload
+ ___23-[AASensorService init]_block_invoke
+ ___23-[AASensorService init]_block_invoke.cold.1
+ ___23-[AASensorService init]_block_invoke_2
+ ___23-[AASensorService init]_block_invoke_2.cold.1
+ ___23-[AASensorService init]_block_invoke_3
+ ___23-[AASensorService init]_block_invoke_4
+ ___27-[AASensorService activate]_block_invoke
+ ___27-[AASensorService activate]_block_invoke.cold.1
+ ___27-[AASensorService activate]_block_invoke.cold.2
+ ___27-[AASensorService activate]_block_invoke.cold.3
+ ___27-[AASensorService activate]_block_invoke.cold.4
+ ___27-[AASensorService activate]_block_invoke.cold.5
+ ___27-[AASensorService activate]_block_invoke_2
+ ___27-[AASensorService activate]_block_invoke_2.cold.1
+ ___27-[AASensorService activate]_block_invoke_2.cold.2
+ ___27-[AASensorService activate]_block_invoke_3
+ ___27-[AASensorService activate]_block_invoke_4
+ ___27-[AASensorService activate]_block_invoke_4.cold.1
+ ___29-[AASensorService invalidate]_block_invoke
+ ___29-[AASensorService invalidate]_block_invoke.cold.1
+ ___29-[AASensorService invalidate]_block_invoke.cold.2
+ ___29-[AASensorService invalidate]_block_invoke.cold.3
+ ___29-[AASensorService invalidate]_block_invoke.cold.4
+ ___37+[AASettingsTelemetry sharedInstance]_block_invoke
+ ___38-[AASensorService subscribeWithFlags:]_block_invoke
+ ___40-[AASensorService handleHIDReport:data:]_block_invoke
+ ___43-[AADeviceManager _activateXPC:reactivate:]_block_invoke
+ ___43-[AADeviceManager _activateXPC:reactivate:]_block_invoke.cold.1
+ ___43-[AADeviceManager _activateXPC:reactivate:]_block_invoke.cold.2
+ ___43-[AADeviceManager _activateXPC:reactivate:]_block_invoke_2
+ ___43-[AASensorService subscribeWithFlags:rate:]_block_invoke
+ ___45-[AASensorService deviceManagerFoundHandler:]_block_invoke
+ ___46-[AASystemStateMonitor fetchPairedHRMDevices:]_block_invoke
+ ___46-[AASystemStateMonitor fetchPairedHRMDevices:]_block_invoke.cold.1
+ ___46-[AASystemStateMonitor fetchPairedHRMDevices:]_block_invoke_2
+ ___46-[AASystemStateMonitor fetchPairedHRMDevices:]_block_invoke_2.cold.1
+ ___50-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke
+ ___50-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke.cold.1
+ ___50-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke.cold.2
+ ___50-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke.cold.3
+ ___50-[AASettingsTelemetry sendSettingsChanges:device:]_block_invoke
+ ___51-[AADeviceManager fetchPairedAudioAccessoryDevices]_block_invoke
+ ___51-[AADeviceManager fetchPairedAudioAccessoryDevices]_block_invoke.cold.1
+ ___51-[AADeviceManager fetchPairedAudioAccessoryDevices]_block_invoke_2
+ ___51-[AADeviceManager fetchPairedAudioAccessoryDevices]_block_invoke_2.cold.1
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.1
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.2
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.3
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.4
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.5
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.6
+ ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.7
+ ___54-[AAController _rawGestureMessageReceived:fromDevice:]_block_invoke
+ ___54-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke
+ ___54-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke_2
+ ___54-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke_2.cold.1
+ ___54-[AADeviceManager isTemporaryPairingConnectionAllowed]_block_invoke
+ ___54-[AADeviceManager isTemporaryPairingConnectionAllowed]_block_invoke.cold.1
+ ___54-[AADeviceManager isTemporaryPairingConnectionAllowed]_block_invoke_2
+ ___54-[AADeviceManager isTemporaryPairingConnectionAllowed]_block_invoke_2.cold.1
+ ___54-[AADeviceManager isTemporaryPairingConnectionAllowed]_block_invoke_2.cold.2
+ ___55-[AAController _batteryInfoMessageReceived:fromDevice:]_block_invoke
+ ___55-[BTCloudServicesClient createDeviceRecord:completion:]_block_invoke.102
+ ___57-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke
+ ___57-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2
+ ___57-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2.cold.1
+ ___57-[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:]_block_invoke
+ ___57-[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:]_block_invoke_2
+ ___57-[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:]_block_invoke_2.cold.1
+ ___58-[AAController _sleepDetectionMessageReceived:fromDevice:]_block_invoke
+ ___62-[AADeviceManager _sendDeviceConfigXPC:identifier:completion:]_block_invoke
+ ___62-[AADeviceManager _sendDeviceConfigXPC:identifier:completion:]_block_invoke.cold.1
+ ___62-[AADeviceManager _sendDeviceConfigXPC:identifier:completion:]_block_invoke_2
+ ___62-[AADeviceManager _sendDeviceConfigXPC:identifier:completion:]_block_invoke_2.cold.1
+ ___62-[AASystemStateMonitor showFitEducationNotificationForDevice:]_block_invoke
+ ___62-[AASystemStateMonitor showFitEducationNotificationForDevice:]_block_invoke.cold.1
+ ___62-[AASystemStateMonitor showFitEducationNotificationForDevice:]_block_invoke_2
+ ___62-[AASystemStateMonitor showFitEducationNotificationForDevice:]_block_invoke_2.cold.1
+ ___62-[BTServicesClient showHIDConnectedBannerAperture:completion:]_block_invoke
+ ___62-[BTServicesClient showHIDConnectedBannerAperture:completion:]_block_invoke_2
+ ___64-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke
+ ___64-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke.cold.1
+ ___64-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke_2
+ ___64-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke_2.cold.1
+ ___64-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]_block_invoke
+ ___64-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]_block_invoke.cold.1
+ ___64-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]_block_invoke_2
+ ___64-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]_block_invoke_2.cold.1
+ ___65-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke
+ ___65-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke.cold.1
+ ___65-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke.cold.2
+ ___65-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke.cold.3
+ ___65-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke_2
+ ___65-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke_2.cold.1
+ ___65-[AAController _accessoryUsageSummaryMessageReceived:fromDevice:]_block_invoke
+ ___65-[AADeviceManager _sendDeviceConfigDirect:identifier:completion:]_block_invoke
+ ___65-[AADeviceManager _sendDeviceConfigDirect:identifier:completion:]_block_invoke.cold.1
+ ___67-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]_block_invoke
+ ___67-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]_block_invoke.cold.1
+ ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke
+ ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke.cold.1
+ ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke.cold.2
+ ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke.cold.3
+ ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke_2
+ ___82-[AAController sendSleepDetectionMessage:destinationIdentifier:completionHandler:]_block_invoke
+ ___82-[AAController sendSleepDetectionMessage:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12lr32l8
+ ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0c8lr32l8
+ ___block_descriptor_40_e8_32s_e22_v20?0"HIDDevice"8B16ls32l8
+ ___block_descriptor_40_e8_32s_e39_v48?0"HIDDevice"8Q16q24q32"NSData"40ls32l8
+ ___block_descriptor_48_e8_32s40r_e29_v16?0"AADeviceBatteryInfo"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e30_v16?0"AudioAccessoryDevice"8lr40l8s32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_53_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.110
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.16
+ ___block_literal_global.366
+ ___block_literal_global.67
+ ___block_literal_global.71
+ _gLogCategory_AADeviceBatteryInfo
+ _gLogCategory_AAManufacturerDataAdvertisement
+ _gLogCategory_AASensorService
+ _gLogCategory_AASettingsTelemetry
+ _isValidBtAddress
+ _kAASensorServiceErrorDomain
+ _memcmp
+ _objc_msgSend$CBCapToAACap:
+ _objc_msgSend$_accessoryUsageSummaryMessageReceived:fromDevice:
+ _objc_msgSend$_batteryInfoMessageReceived:fromDevice:
+ _objc_msgSend$_batteryStateFromCharging:chargingOBC:
+ _objc_msgSend$_calculateOwnVoiceActivityLevel
+ _objc_msgSend$_clearCombinedBattery
+ _objc_msgSend$_getBTAddressFromHIDDeviceObject:
+ _objc_msgSend$_notifyAvailabilityChangedWithForcedUpdate:
+ _objc_msgSend$_ovadSubscriptionHelperWithCompletion:completion:
+ _objc_msgSend$_parsePayloads
+ _objc_msgSend$_rawGestureMessageReceived:fromDevice:
+ _objc_msgSend$_sendDeviceConfigDirect:identifier:completion:
+ _objc_msgSend$_sendDeviceConfigXPC:identifier:completion:
+ _objc_msgSend$_sendSettingsChanges:device:
+ _objc_msgSend$_sensorDataAvailabilitiesAdded:
+ _objc_msgSend$_sensorDataAvailabilitiesLost:
+ _objc_msgSend$_sensorDataAvailabilitiesLostDelayedNotification
+ _objc_msgSend$_sleepDetectionMessageReceived:fromDevice:
+ _objc_msgSend$_submitFeaturesChangeMetrics:forFeature:forDevice:
+ _objc_msgSend$_updateBatteriesFromTetheredAdvertisement:
+ _objc_msgSend$_updateBatteriesFromUntetheredAdvertisement:
+ _objc_msgSend$_updateCaseInfo:
+ _objc_msgSend$_updateChargingOBCTimeUntilCharged:
+ _objc_msgSend$_updateCombinedBattery
+ _objc_msgSend$_updateWithAACPBatteryInfo:
+ _objc_msgSend$_updateWithNearbyBattery:forType:withSource:
+ _objc_msgSend$_updateWithProximityPairingPayload:
+ _objc_msgSend$acceptReplyPlayPauseConfig
+ _objc_msgSend$activate
+ _objc_msgSend$adaptiveVolumeCapability
+ _objc_msgSend$adaptiveVolumeConfig
+ _objc_msgSend$advertisementPayloadWithData:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$allowHealthKitDataWrite
+ _objc_msgSend$allowTemporaryManagedPairing
+ _objc_msgSend$audioState
+ _objc_msgSend$audiogramEnrolledTimestamp
+ _objc_msgSend$autoAncCapability
+ _objc_msgSend$batteries
+ _objc_msgSend$battery1
+ _objc_msgSend$battery2
+ _objc_msgSend$battery3
+ _objc_msgSend$battery4
+ _objc_msgSend$battery5
+ _objc_msgSend$batteryCase
+ _objc_msgSend$batteryCombinedLeftRight
+ _objc_msgSend$batteryForType:
+ _objc_msgSend$batteryLeft
+ _objc_msgSend$batteryMain
+ _objc_msgSend$batteryRight
+ _objc_msgSend$bluetoothAddressData
+ _objc_msgSend$btAddress
+ _objc_msgSend$budRole
+ _objc_msgSend$budSide
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$cameraControlCapability
+ _objc_msgSend$cancel
+ _objc_msgSend$caseBatteryCharging
+ _objc_msgSend$caseBatteryLevel
+ _objc_msgSend$caseBatteryValid
+ _objc_msgSend$caseColor
+ _objc_msgSend$caseIdentifier
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$caseLedColor
+ _objc_msgSend$caseLedStatus
+ _objc_msgSend$caseVersion
+ _objc_msgSend$changeOptimizedBatteryChargingState
+ _objc_msgSend$chargeStatus
+ _objc_msgSend$charging
+ _objc_msgSend$chargingOBC
+ _objc_msgSend$chargingOBCTimeUntilCharged
+ _objc_msgSend$chargingReminderCapability
+ _objc_msgSend$chargingReminderEnabled
+ _objc_msgSend$classicRSSI
+ _objc_msgSend$clearExpiredBatteries
+ _objc_msgSend$clickHoldModeLeft
+ _objc_msgSend$clickHoldModeRight
+ _objc_msgSend$close
+ _objc_msgSend$cloudRecordInfoLoaded
+ _objc_msgSend$colorBest
+ _objc_msgSend$colorRaw
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$connected
+ _objc_msgSend$connectedAADeviceInfoReceived
+ _objc_msgSend$connectedCBDeviceReceived
+ _objc_msgSend$connectedSourceCount
+ _objc_msgSend$conversationDetectCapability
+ _objc_msgSend$conversationDetectConfig
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$crownRotationDirection
+ _objc_msgSend$cupColor
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$declineDismissSkipConfig
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$describeProperties
+ _objc_msgSend$deviceFlags
+ _objc_msgSend$deviceManagerActivateDirect:completion:
+ _objc_msgSend$deviceManagerFetchAADeviceBatteryInfoForAddress:deviceHandler:
+ _objc_msgSend$deviceManagerFetchAADeviceBatteryInfoForIdentifier:deviceHandler:
+ _objc_msgSend$deviceManagerFetchAudioAccessoryDeviceForBTAddress:deviceHandler:
+ _objc_msgSend$deviceManagerFetchPairedAudioAccessoryDevices:
+ _objc_msgSend$deviceManagerFoundHandler:
+ _objc_msgSend$deviceManagerInvalidateDirect:
+ _objc_msgSend$deviceManagerSendDeviceConfigDirect:identifier:completion:
+ _objc_msgSend$deviceManagerUpdateDirect:
+ _objc_msgSend$deviceNotificationHandler:added:
+ _objc_msgSend$dictionary
+ _objc_msgSend$doubleTapActionLeft
+ _objc_msgSend$doubleTapActionRight
+ _objc_msgSend$doubleTapCapability
+ _objc_msgSend$enableChargingReminder
+ _objc_msgSend$enableHearingAidGainSwipe
+ _objc_msgSend$enableSleepDetection
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$endCallCapability
+ _objc_msgSend$endCallConfig
+ _objc_msgSend$enhancedTransparencyVersion
+ _objc_msgSend$farFieldUplinkCapability
+ _objc_msgSend$faultDetected
+ _objc_msgSend$findMyGroupIdentifier
+ _objc_msgSend$firmwareVersionRaw
+ _objc_msgSend$fullyCharged
+ _objc_msgSend$gapaFlags
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$guestPaired
+ _objc_msgSend$handleHIDReport:data:
+ _objc_msgSend$hash
+ _objc_msgSend$headGestureToggle
+ _objc_msgSend$healthKitDataWriteAllowed
+ _objc_msgSend$hearingAidToggle
+ _objc_msgSend$hidDevice
+ _objc_msgSend$idleTime
+ _objc_msgSend$inAACP
+ _objc_msgSend$initLogParseError:
+ _objc_msgSend$initWithAACPBatteryInfo:productID:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithHIDDevice:
+ _objc_msgSend$initWithHIDDeviceAndSensorInfo:sensorInfo:
+ _objc_msgSend$initWithLevel:productID:state:type:
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$invalidBattery
+ _objc_msgSend$isCase
+ _objc_msgSend$isCaseBattery
+ _objc_msgSend$isConnected
+ _objc_msgSend$isEqualToAdvertisement:
+ _objc_msgSend$isEqualToBattery:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isEqualToPayload:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isExpired
+ _objc_msgSend$isNearby
+ _objc_msgSend$isSetupComplete
+ _objc_msgSend$isSubscribed
+ _objc_msgSend$isTemporaryPairingConnectionAllowed:
+ _objc_msgSend$lastBudInCaseWithCurrentBud
+ _objc_msgSend$lastConnectedHost
+ _objc_msgSend$lastConnectedHostSignedInToICloud
+ _objc_msgSend$lastOrigin
+ _objc_msgSend$lastSeen
+ _objc_msgSend$lastSeenConnectedTime
+ _objc_msgSend$lastSeenTime
+ _objc_msgSend$leftBatteryCharging
+ _objc_msgSend$leftBatteryLevel
+ _objc_msgSend$leftBatteryValid
+ _objc_msgSend$leftColor
+ _objc_msgSend$level
+ _objc_msgSend$lidClosed
+ _objc_msgSend$lidOpenCount
+ _objc_msgSend$listeningModeOffAllowed
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$lowLevel
+ _objc_msgSend$mainBatteryCharging
+ _objc_msgSend$mainBatteryLevel
+ _objc_msgSend$mainBatteryValid
+ _objc_msgSend$manufacturerData
+ _objc_msgSend$microphoneMode
+ _objc_msgSend$misc1
+ _objc_msgSend$model
+ _objc_msgSend$muteControlCapability
+ _objc_msgSend$muteControlConfig
+ _objc_msgSend$myBatteryCharging
+ _objc_msgSend$myBatteryLevel
+ _objc_msgSend$myBatteryValid
+ _objc_msgSend$needsConnection
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$open
+ _objc_msgSend$optimizedBatteryChargingCapability
+ _objc_msgSend$otherBatteryCharging
+ _objc_msgSend$otherBatteryLevel
+ _objc_msgSend$otherBatteryValid
+ _objc_msgSend$outOfBoxMode
+ _objc_msgSend$outOfCaseTime
+ _objc_msgSend$ovadStreamingCapability
+ _objc_msgSend$paired
+ _objc_msgSend$pairedAADeviceInfoReceived
+ _objc_msgSend$pairedCBDeviceReceived
+ _objc_msgSend$pairedInfoComplete
+ _objc_msgSend$payloadData
+ _objc_msgSend$peerAutoANCCapability
+ _objc_msgSend$pid
+ _objc_msgSend$pmeEverywhereCapability
+ _objc_msgSend$prewarmAudioAccessoriesForFitnessWorkout:
+ _objc_msgSend$primaryBluetoothAddress
+ _objc_msgSend$primaryLocation
+ _objc_msgSend$primaryProductID
+ _objc_msgSend$productInfoWithProductID:
+ _objc_msgSend$productName
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$proximityPairingPayload
+ _objc_msgSend$proximityPairingPayloadWithData:
+ _objc_msgSend$proximityPairingStatusPayloadWithData:pid:
+ _objc_msgSend$rawGesturesConfigFlags
+ _objc_msgSend$remoteCameraControlConfig
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$removeBatteryInMap:
+ _objc_msgSend$rightBatteryCharging
+ _objc_msgSend$rightBatteryLevel
+ _objc_msgSend$rightBatteryValid
+ _objc_msgSend$rightColor
+ _objc_msgSend$rssi
+ _objc_msgSend$secondaryLocation
+ _objc_msgSend$secondsFromGMT
+ _objc_msgSend$selectiveSpeechListeningCapability
+ _objc_msgSend$selectiveSpeechListeningConfig
+ _objc_msgSend$sensorInfo
+ _objc_msgSend$serialNumber
+ _objc_msgSend$serialNumberLeft
+ _objc_msgSend$serialNumberRight
+ _objc_msgSend$setAcceptReplyPlayPauseConfig:
+ _objc_msgSend$setAdaptiveVolumeCapability:
+ _objc_msgSend$setAdaptiveVolumeConfig:
+ _objc_msgSend$setAudiogramEnrolledTimestamp:
+ _objc_msgSend$setBatteryInMap:
+ _objc_msgSend$setBatteryInfo:
+ _objc_msgSend$setBobbleConfig:
+ _objc_msgSend$setCameraControlCapability:
+ _objc_msgSend$setCaseIdentifier:
+ _objc_msgSend$setCaseLedColor:
+ _objc_msgSend$setCaseLedStatus:
+ _objc_msgSend$setCaseVersion:
+ _objc_msgSend$setChargingOBCTimeUntilCharged:
+ _objc_msgSend$setChargingReminderCapability:
+ _objc_msgSend$setChargingReminderEnabled:
+ _objc_msgSend$setClassicRSSI:
+ _objc_msgSend$setClickHoldModeLeft:
+ _objc_msgSend$setClickHoldModeRight:
+ _objc_msgSend$setConnectedAADeviceInfoReceived:
+ _objc_msgSend$setConnectedCBDeviceReceived:
+ _objc_msgSend$setConversationDetectCapability:
+ _objc_msgSend$setConversationDetectConfig:
+ _objc_msgSend$setCoreBluetoothDevice:
+ _objc_msgSend$setCrownRotationDirection:
+ _objc_msgSend$setDeclineDismissSkipConfig:
+ _objc_msgSend$setDetectedHeadGesture:
+ _objc_msgSend$setDeviceMatching:
+ _objc_msgSend$setDeviceNotificationHandler:
+ _objc_msgSend$setDoubleTapActionLeft:
+ _objc_msgSend$setDoubleTapActionRight:
+ _objc_msgSend$setDoubleTapCapability:
+ _objc_msgSend$setEndCallCapability:
+ _objc_msgSend$setEndCallConfig:
+ _objc_msgSend$setEnhancedTransparencyVersion:
+ _objc_msgSend$setFarFieldUplinkCapability:
+ _objc_msgSend$setFindMyGroupIdentifier:
+ _objc_msgSend$setGapaFlags:
+ _objc_msgSend$setGuestPaired:
+ _objc_msgSend$setHeadGestureToggle:
+ _objc_msgSend$setHealthKitDataWriteAllowed:
+ _objc_msgSend$setInputReportHandler:
+ _objc_msgSend$setIsConnected:
+ _objc_msgSend$setIsNearby:
+ _objc_msgSend$setIsSetupComplete:
+ _objc_msgSend$setIsSubscribed:
+ _objc_msgSend$setLastOrigin:
+ _objc_msgSend$setLastSeen:
+ _objc_msgSend$setLastSeenConnectedTime:
+ _objc_msgSend$setLevel:
+ _objc_msgSend$setListeningModeOffAllowed:
+ _objc_msgSend$setMicrophoneMode:
+ _objc_msgSend$setModel:
+ _objc_msgSend$setMuteControlCapability:
+ _objc_msgSend$setMuteControlConfig:
+ _objc_msgSend$setOptimizedBatteryChargingCapability:
+ _objc_msgSend$setOptimizedBatteryChargingState:
+ _objc_msgSend$setOvadStreamingCapability:
+ _objc_msgSend$setPaired:
+ _objc_msgSend$setPairedAADeviceInfoReceived:
+ _objc_msgSend$setPairedCBDeviceReceived:
+ _objc_msgSend$setPeerAutoANCCapability:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setPmeEverywhereCapability:
+ _objc_msgSend$setProductName:
+ _objc_msgSend$setRawGesturesConfigFlags:
+ _objc_msgSend$setRemoteCameraControlConfig:
+ _objc_msgSend$setReport:reportLength:withIdentifier:forType:error:
+ _objc_msgSend$setRouted:
+ _objc_msgSend$setSelectiveSpeechListeningCapability:
+ _objc_msgSend$setSelectiveSpeechListeningConfig:
+ _objc_msgSend$setSensorInfo:
+ _objc_msgSend$setSerialNumber:
+ _objc_msgSend$setSerialNumberLeft:
+ _objc_msgSend$setSerialNumberRight:
+ _objc_msgSend$setSiriMultitoneEnabled:
+ _objc_msgSend$setSleepDetectionCapability:
+ _objc_msgSend$setSleepDetectionEnabled:
+ _objc_msgSend$setSmartRoutingCapability:
+ _objc_msgSend$setSmartRoutingMode:
+ _objc_msgSend$setSmartRoutingStateFlags:
+ _objc_msgSend$setSourceFlags:
+ _objc_msgSend$setSpatialAudioAllowed:
+ _objc_msgSend$setState:
+ _objc_msgSend$setTemporaryManagedPairedStatus:
+ _objc_msgSend$setType:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$showHIDConnectedBannerAperture:completion:
+ _objc_msgSend$showProxStatus
+ _objc_msgSend$sleepDetectionCapability
+ _objc_msgSend$sleepDetectionEnabled
+ _objc_msgSend$smartRoutingCapability
+ _objc_msgSend$smartRoutingConnected
+ _objc_msgSend$smartRoutingMode
+ _objc_msgSend$smartRoutingScoreSource1
+ _objc_msgSend$smartRoutingScoreSource2
+ _objc_msgSend$soundEnabled
+ _objc_msgSend$sourceFlags
+ _objc_msgSend$spatialAudioAllowed
+ _objc_msgSend$status1
+ _objc_msgSend$status2
+ _objc_msgSend$status3
+ _objc_msgSend$status4
+ _objc_msgSend$status5
+ _objc_msgSend$statusFlags1
+ _objc_msgSend$subType
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$subscribeWithSensorDataFlags:rate:completion:
+ _objc_msgSend$supportWirelessSplitter
+ _objc_msgSend$supportedPID:
+ _objc_msgSend$systemStateMonitorFetchHealthKitDataWriteAllowedForDevice:completionHandler:
+ _objc_msgSend$systemStateMonitorFetchPairedHRMDevices:
+ _objc_msgSend$systemStateMonitorShowFitEducationNotificationForIdentifier:completionHandler:
+ _objc_msgSend$temporaryManagedPairedStatus
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timeUntilCharged
+ _objc_msgSend$type
+ _objc_msgSend$unsubscribeAll
+ _objc_msgSend$unsubscribeWithSensorDataFlags:
+ _objc_msgSend$unsupportedAccessoryConnected
+ _objc_msgSend$update:
+ _objc_msgSend$updateWithAABattery:
+ _objc_msgSend$usbAudioConnected
+ _objc_msgSend$utpConnected
+ _objc_msgSend$valid
+ _objc_opt_isKindOfClass
+ _objc_retain_x9
+ _sharedInstance.sOnce
+ _sharedInstance.sSelf
- -[AADeviceConfig needsUpdateToDeviceCloudRecord]
- -[AASystemStateMonitor HRMCapableDeviceChangedHandler]
- -[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:].cold.2
- -[AASystemStateMonitor isHRMCapableDevicePresent]
- -[AASystemStateMonitor setHRMCapableDeviceChangedHandler:]
- -[AudioAccessoryDevice setDefaultConfigurationsIfNeeded]
- -[AudioAccessoryDevice updateWithAADeviceInfo:]
- -[AudioAccessoryDevice updateWithCBDevice:]
- GCC_except_table14
- GCC_except_table21
- _OBJC_IVAR_$_AASystemStateMonitor._HRMCapableDeviceChangedHandler
- _OBJC_IVAR_$_AASystemStateMonitor._isHRMCapableDevicePresent
- ___29-[AADeviceManager _activate:]_block_invoke_2
- ___29-[AADeviceManager _activate:]_block_invoke_2.cold.1
- ___29-[AADeviceManager _activate:]_block_invoke_2.cold.2
- ___37-[BTAudioRoutingRequest activateSync]_block_invoke
- ___55-[BTCloudServicesClient createDeviceRecord:completion:]_block_invoke.84
- ___58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke_2
- ___58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke_2.cold.1
- ___58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke_3
- ___58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke_3.cold.1
- ___block_literal_global.348
- ___block_literal_global.62
- _dispatch_sync
CStrings:
+ "\n%@"
+ "### Activate not called!"
+ "### Direct: sendDeviceConfig Error: %{error}"
+ "### Fetch for paired HRM devices failed with XPC error: %{error}"
+ "### Fetch for paired HRM devices failed with error: %{error}"
+ "### Invalid %@: %s"
+ "### Invalid %@: Payload data missing data, expected %u bytes, got %u bytes."
+ "### Invalid Manufacturer Data: Missing data from Company ID bytes."
+ "### Show fit education failed with XPC error: %{error}"
+ "### Sync fetch for HK Data write property failed with XPC error: %{error}"
+ "### Sync fetch for temporaryPairingConnectionAllowed Error: %{error}"
+ "### Sync fetch for temporaryPairingConnectionAllowed failed with XPC error: %{error}"
+ "### XPC receive AccessoryUsageSummary message failed: %@"
+ "### XPC receive BatteryInfo message failed: %@"
+ "### XPC receive Raw Gestures message failed: %@"
+ "### XPC receive Sleep Detection message failed: %@"
+ "### pairedDevices failed with XPC %{error}"
+ "### pairedDevices failed with XPC error: %{error}"
+ "### prewarmAudioAccessoriesForFitnessWorkout failed to start XPC"
+ "### prewarmAudioAccessoriesForFitnessWorkout no XPC"
+ "### sync fetch for AADeviceBatteryInfo address: %@ failed with XPC %{error}"
+ "### sync fetch for AADeviceBatteryInfo address: %@ failed with XPC error: %{error}"
+ "### sync fetch for AADeviceBatteryInfo id: %@ failed with XPC %{error}"
+ "### sync fetch for AADeviceBatteryInfo id: %@ failed with XPC error: %{error}"
+ "### sync fetch for AudioAccessoryDevice id: %@ failed with XPC %{error}"
+ "### sync fetch for AudioAccessoryDevice id: %@ failed with XPC error: %{error}"
+ "%@, "
+ "%u.%u.%u"
+ "+"
+ ", Adv Data: <%@>"
+ ", Audio St: %s"
+ ", Bt Addr '%@'"
+ ", C Batt: %s%d"
+ ", C Batt: %s%d%%"
+ ", C Batt: invalid"
+ ", C col: %d"
+ ", Ch Rmd %llu"
+ ", Col '%u'"
+ ", En Chr R %s"
+ ", En SlDt %s"
+ ", HK Wr En %s "
+ ", Idle time: %s"
+ ", L Batt: %s%d%%"
+ ", L Batt: invalid"
+ ", L col: %d"
+ ", Loc: %s"
+ ", M Batt: %s%d%%"
+ ", M Batt: invalid"
+ ", Md '%@'"
+ ", My Batt: %s%d"
+ ", My Batt: invalid"
+ ", Nm '%@'"
+ ", Nw Ch %llu"
+ ", OBC %s"
+ ", OBC on: %s"
+ ", OBC until: %u min"
+ ", Oth Batt: %s%d"
+ ", Oth Batt: invalid"
+ ", Out of Box: %s"
+ ", PID %d"
+ ", PT: %u"
+ ", Pid '%u'"
+ ", Pu Md %llu"
+ ", R Batt: %s%d%%"
+ ", R Batt: invalid"
+ ", R col: %d"
+ ", RcamCC %s"
+ ", Rm CC %llu"
+ ", SR Conn: %s"
+ ", SR score 1: %s"
+ ", SR score 2: %s"
+ ", ST: %u"
+ ", Src count: %d"
+ ", Sup Wir Split: %s"
+ ", Temp Mg Paired %s"
+ ", UTP: %s"
+ ", Unsup acc conn: %s"
+ ", case led col: %s"
+ ", case led status: %s"
+ ", case ver: %s"
+ ", col: %d"
+ ", color: %d"
+ ", combined lt rt %@"
+ ", connected: %s"
+ ", cup col: %d"
+ ", fault detect: %s"
+ ", fmCI '%@'"
+ ", fmGI '%@'"
+ ", fw ver: %@"
+ ", led col: %s"
+ ", lid closed: %s"
+ ", lid open count: %d"
+ ", lst bud in C w/curr bud: %@"
+ ", lst conn host iCloud signed in: %s"
+ ", lst conn hst: %@"
+ ", need conn: %s"
+ ", rgCg %@"
+ ", sFL: %@"
+ ", show prox: %s"
+ ", sound En: %s"
+ ", time out of case: %s"
+ ", time till charged: %d"
+ ", usb aud conn: %s"
+ "-"
+ "-[AAAdvertisementPayload initLogParseError:]"
+ "-[AAAdvertisementPayload initWithData:]"
+ "-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke"
+ "-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout]_block_invoke_2"
+ "-[AAController _accessoryUsageSummaryMessageReceived:fromDevice:]"
+ "-[AAController _accessoryUsageSummaryMessageReceived:fromDevice:]_block_invoke"
+ "-[AAController _batteryInfoMessageReceived:fromDevice:]"
+ "-[AAController _batteryInfoMessageReceived:fromDevice:]_block_invoke"
+ "-[AAController _rawGestureMessageReceived:fromDevice:]"
+ "-[AAController _rawGestureMessageReceived:fromDevice:]_block_invoke"
+ "-[AAController _sleepDetectionMessageReceived:fromDevice:]"
+ "-[AAController _sleepDetectionMessageReceived:fromDevice:]_block_invoke"
+ "-[AAController sendSleepDetectionMessage:destinationIdentifier:completionHandler:]_block_invoke"
+ "-[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:]"
+ "-[AADeviceBatteryInfo _updateBatteriesFromTetheredAdvertisement:]"
+ "-[AADeviceBatteryInfo _updateBatteriesFromUntetheredAdvertisement:]"
+ "-[AADeviceBatteryInfo _updateWithAACPBatteryInfo:]"
+ "-[AADeviceBatteryInfo _updateWithProximityPairingPayload:]"
+ "-[AADeviceBatteryInfo updateWithConnectedDevice:]"
+ "-[AADeviceManager _activateDirect:]"
+ "-[AADeviceManager _activateXPC:reactivate:]"
+ "-[AADeviceManager _activateXPC:reactivate:]_block_invoke"
+ "-[AADeviceManager _sendDeviceConfigDirect:identifier:completion:]_block_invoke"
+ "-[AADeviceManager _sendDeviceConfigXPC:identifier:completion:]_block_invoke"
+ "-[AADeviceManager _sendDeviceConfigXPC:identifier:completion:]_block_invoke_2"
+ "-[AADeviceManager deviceManagerFoundBatteryInfo:]"
+ "-[AADeviceManager deviceManagerLostBatteryInfo:]"
+ "-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]"
+ "-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke"
+ "-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke_2"
+ "-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]"
+ "-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke"
+ "-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2"
+ "-[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:]"
+ "-[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:]_block_invoke"
+ "-[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:]_block_invoke_2"
+ "-[AADeviceManager fetchPairedAudioAccessoryDevices]"
+ "-[AADeviceManager fetchPairedAudioAccessoryDevices]_block_invoke"
+ "-[AADeviceManager fetchPairedAudioAccessoryDevices]_block_invoke_2"
+ "-[AADeviceManager isTemporaryPairingConnectionAllowed]"
+ "-[AADeviceManager isTemporaryPairingConnectionAllowed]_block_invoke"
+ "-[AADeviceManager isTemporaryPairingConnectionAllowed]_block_invoke_2"
+ "-[AAManufacturerDataAdvertisement initWithData:]"
+ "-[AAOVADSensorInfo update:]"
+ "-[AASensorService _notifyAvailabilityChangedWithForcedUpdate:]"
+ "-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke"
+ "-[AASensorService _sensorDataAvailabilitiesAdded:]"
+ "-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]"
+ "-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]_block_invoke"
+ "-[AASensorService activate]_block_invoke"
+ "-[AASensorService activate]_block_invoke_2"
+ "-[AASensorService activate]_block_invoke_4"
+ "-[AASensorService deviceManagerFoundHandler:]_block_invoke"
+ "-[AASensorService deviceNotificationHandler:added:]_block_invoke"
+ "-[AASensorService handleHIDReport:data:]_block_invoke"
+ "-[AASensorService init]_block_invoke"
+ "-[AASensorService init]_block_invoke_2"
+ "-[AASensorService invalidate]_block_invoke"
+ "-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke"
+ "-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke_2"
+ "-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke"
+ "-[AASettingsTelemetry _sendSettingsChanges:device:]"
+ "-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]"
+ "-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]_block_invoke"
+ "-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:]_block_invoke_2"
+ "-[AASystemStateMonitor fetchPairedHRMDevices:]"
+ "-[AASystemStateMonitor fetchPairedHRMDevices:]_block_invoke"
+ "-[AASystemStateMonitor fetchPairedHRMDevices:]_block_invoke_2"
+ "-[AASystemStateMonitor showFitEducationNotificationForDevice:]"
+ "-[AASystemStateMonitor showFitEducationNotificationForDevice:]_block_invoke"
+ "-[AASystemStateMonitor showFitEducationNotificationForDevice:]_block_invoke_2"
+ "-[AASystemStateMonitor siriHijackEligibilityUpdated:]"
+ "0"
+ "2xNod"
+ "2xShake"
+ "30-60s"
+ "5-30s"
+ "<5s"
+ ">60s"
+ "@\"AADeviceBatteryInfo\""
+ "@\"AASensorInfo\""
+ "@\"AudioAccessoryDevice\""
+ "@\"HIDDevice\""
+ "@\"HIDManager\""
+ "@\"NSArray\""
+ "@24@0:8^{_NSZone=}16"
+ "@24@0:8q16"
+ "@25@0:8{?=CCCCC}16I21"
+ "@28@0:8@16S24"
+ "@32@0:8@16@24"
+ "@44@0:8d16I24q28q36"
+ "AAAdvertisementPayload"
+ "AABattery"
+ "AADeviceBatteryInfo"
+ "AADeviceBatteryInfo identifier: %@"
+ "AADeviceBatteryInfo lost for clientID 0x%X, battery object: %@"
+ "AADeviceBatteryInfo now connected: %@"
+ "AADeviceManager activation failed with error %@"
+ "AADeviceManager interrupted"
+ "AADeviceManager invalidated"
+ "AADeviceManager succesfully activated"
+ "AAHIDDevice"
+ "AAManufacturerDataAdvertisement"
+ "AAOVADSensorInfo"
+ "AAProximityPairingAccessoryStatusPayload"
+ "AAProximityPairingPayload"
+ "AAProximityPairingStatusPayloadB188B288"
+ "AAProximityPairingStatusPayloadB444"
+ "AAProximityPairingStatusPayloadB463"
+ "AAProximityPairingStatusPayloadB515"
+ "AAProximityPairingStatusPayloadB515c"
+ "AAProximityPairingStatusPayloadBeatsUntethered"
+ "AAProximityPairingStatusPayloadGeneral"
+ "AAProximityPairingStatusPayloadOtherTetheredNonCase"
+ "AAProximityPairingStatusPayloadUntethered"
+ "AASensorInfo"
+ "AASensorService"
+ "AASensorServiceQueue"
+ "AASettingsTelemetry"
+ "AATetheredProximityPairingPayload"
+ "AAUntetheredProximityPairingPayload"
+ "AG EnrolledTime '%@', "
+ "AStS %s, "
+ "Absent"
+ "Accessory Usage Summary message received: source %@, data <%@>"
+ "AccessoryUsageSummary"
+ "Activate already called. Cannot activate again."
+ "Activate not called"
+ "AdaptiveTransparency"
+ "AirPodsCameraControl"
+ "AirPodsInEducation"
+ "Airplane"
+ "AppleTV"
+ "AudioAccessoryDevice identifier: %@, "
+ "Available devices count: %d"
+ "Available sensors data lost delayed notification"
+ "B20@0:8C16"
+ "B20@0:8S16"
+ "B21@0:8{?=CCCCC}16"
+ "B235"
+ "B36@0:8@16q24I32"
+ "B435"
+ "BT_ADDR"
+ "Batt %s '%c%.2f%%'[%@]"
+ "Battery Info message received: source %@, data <%@>"
+ "BatteryChargingReminder"
+ "BatteryInfo"
+ "BatteryOBC"
+ "Bkgd"
+ "Blinking"
+ "C20@0:8C16"
+ "CBCapToAACap:"
+ "CBLocalizable"
+ "Cached device %@ PID = %@"
+ "CameraControl"
+ "Case"
+ "Charging"
+ "ChargingReminders"
+ "Cleared delayed notifcation for lost sensor data availability"
+ "Closed and cancelled all OVAD HID devices"
+ "Combined"
+ "CombinedLeftRightBatteryStatus"
+ "Critical"
+ "Data packet is not the correct length for parsing"
+ "DeviceUsage"
+ "DeviceUsagePage"
+ "Discharging"
+ "Disconnected"
+ "Error"
+ "FeatureName"
+ "FeatureNewValue"
+ "Fetch for paired HRM devices called, starting xpc"
+ "First OVAD capable device found"
+ "Found device: %@"
+ "Fully Charged"
+ "FutureDevice"
+ "Good"
+ "Green"
+ "H"
+ "HFPCall"
+ "HFPOther"
+ "HIDManager activated for sensor discovery"
+ "HIDManager initialization failed"
+ "HRM En %s, "
+ "HT Cap %s, "
+ "HeadGestureToggle"
+ "HeadGesturesAccept"
+ "HeadGesturesDecline"
+ "HeadphoneDeeplinkingV1"
+ "HeadphoneFeatures"
+ "HearingAidEnrolled"
+ "HearingAidGainSwipe"
+ "HearingAidToggle"
+ "HkWr"
+ "In Case"
+ "In Ear"
+ "Invalid Battery status, not charging, but OBC engaged."
+ "Invalid OVAD data packet received"
+ "Invalid data"
+ "L"
+ "LR"
+ "Last OVAD capable device lost"
+ "Left"
+ "Lost device matches stored device -- removing"
+ "Lost device: %@"
+ "LsMC %@, "
+ "LsMd Off %s, "
+ "LsnM %s, "
+ "Lst Conn '%@', "
+ "M"
+ "Main"
+ "Max"
+ "Md %@, "
+ "Misc Caps: "
+ "Misc info: "
+ "Nm %@, "
+ "No battery info found handler for client ID 0x%X"
+ "No matching AAHIDDevice found for BT address %@"
+ "Notify about sensor data availablibity change, flags: %d, force %s"
+ "OBC Cap %s, "
+ "OBC En %s, "
+ "OBCc"
+ "OBCs"
+ "Orange"
+ "P1x"
+ "PHld"
+ "PID"
+ "Parsed OVAD Data: threshold=%d ovad=%d"
+ "PauseMediaWhenSleep"
+ "Present"
+ "Press Hold"
+ "Press Once"
+ "Primary"
+ "PrimaryUsage"
+ "PrimaryUsagePage"
+ "R"
+ "Raw Gestures message received: source %@, data <%@>"
+ "RawGesture"
+ "Received HID report with unknown ID=%d"
+ "Received/updated BT address is invalid"
+ "Red"
+ "Registered change in OVAD status: %s -> %s"
+ "Reserved"
+ "Reserved1"
+ "Reserved2"
+ "Right"
+ "S"
+ "S16@0:8"
+ "S2S"
+ "SRDisabled"
+ "SRScore3"
+ "SRScore5"
+ "Secondary"
+ "Sensor discovery timeout"
+ "SensorService invalidation complete"
+ "Set device matching and notification handlers"
+ "Show fit education called, starting xpc"
+ "Show fit education failed with error: %{error}"
+ "Show fit education notification returning with error %{error}"
+ "Sleep Detection message received: source %@, data <%@>"
+ "SleepDetection"
+ "Solid"
+ "SourceConnecting"
+ "Started %.1f s timeout for sensor availability"
+ "Started %.1f s timeout for subscription"
+ "Subscription timeout"
+ "Succesfully fetched HK Data write property %s"
+ "Succesfully setReport for HID device"
+ "Successfully fetched %d paired HRM devices"
+ "Successfully sent stop packet"
+ "Sync fetch for HK Data write property called, starting xpc"
+ "Sync fetch for temporaryPairingConnectionAllowed returned: %d "
+ "T@\"AABattery\",R,N"
+ "T@\"AADeviceBatteryInfo\",&,N,V_batteryInfo"
+ "T@\"AASensorInfo\",C,N,V_sensorInfo"
+ "T@\"AudioAccessoryDevice\",R,C,N,V_activeHRMDevice"
+ "T@\"HIDDevice\",R,C,N,V_hidDevice"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,V_payloads"
+ "T@\"NSData\",R,C,N,V_lastBudInCaseWithCurrentBud"
+ "T@\"NSData\",R,C,N,V_lastConnectedHost"
+ "T@\"NSData\",R,N,V_manufacturerData"
+ "T@\"NSData\",R,N,V_payloadData"
+ "T@\"NSDate\",C,N,V_lastSeenConnectedTime"
+ "T@\"NSMutableDictionary\",C,N"
+ "T@\"NSString\",C,N,V_bluetoothAddress"
+ "T@\"NSString\",C,N,V_btAddress"
+ "T@\"NSString\",C,N,V_caseIdentifier"
+ "T@\"NSString\",C,N,V_findMyGroupIdentifier"
+ "T@\"NSString\",C,N,V_model"
+ "T@\"NSString\",C,N,V_productName"
+ "T@\"NSString\",C,N,V_serialNumber"
+ "T@\"NSString\",C,N,V_serialNumberLeft"
+ "T@\"NSString\",C,N,V_serialNumberRight"
+ "T@\"NSString\",R,C,N,V_btAddress"
+ "T@\"NSString\",R,C,N,V_transport"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@?,C,N,V_accessoryUsageSummaryMessageHandler"
+ "T@?,C,N,V_batteryInfoMessageHandler"
+ "T@?,C,N,V_deviceBatteryInfoLostHandler"
+ "T@?,C,N,V_deviceBatteryInfoUpdatedHandler"
+ "T@?,C,N,V_rawGestureMessageHandler"
+ "T@?,C,N,V_sensorAvailabilityUpdatedHandler"
+ "T@?,C,N,V_sensorDataInfoUpdatedHandler"
+ "T@?,C,N,V_sleepDetectionMessageHandler"
+ "T@?,C,V_hrmCapableDeviceRoutedStateChangedHandler"
+ "T@?,C,V_siriHijackEligibilityUpdatedHandler"
+ "TB,N,V_cloudRecordInfoLoaded"
+ "TB,N,V_connectedAADeviceInfoReceived"
+ "TB,N,V_connectedCBDeviceReceived"
+ "TB,N,V_isSetupComplete"
+ "TB,N,V_isSubscribed"
+ "TB,N,V_onConnectionActionsCalled"
+ "TB,N,V_pairedAADeviceInfoReceived"
+ "TB,N,V_pairedCBDeviceReceived"
+ "TB,N,V_routed"
+ "TB,R,V_isSystemEligibleForSiriHijack"
+ "TB,R,V_showProxStatus"
+ "TB,V_isConnected"
+ "TB,V_isNearby"
+ "TC,N,V_adaptiveVolumeCapability"
+ "TC,N,V_cameraControlCapability"
+ "TC,N,V_chargingReminderCapability"
+ "TC,N,V_conversationDetectCapability"
+ "TC,N,V_endCallCapability"
+ "TC,N,V_enhancedTransparencyVersion"
+ "TC,N,V_farFieldUplinkCapability"
+ "TC,N,V_muteControlCapability"
+ "TC,N,V_optimizedBatteryChargingCapability"
+ "TC,N,V_ovadStreamingCapability"
+ "TC,N,V_peerAutoANCCapability"
+ "TC,N,V_pmeEverywhereCapability"
+ "TC,N,V_remoteCameraControlConfig"
+ "TC,N,V_selectiveSpeechListeningCapability"
+ "TC,N,V_sleepDetectionCapability"
+ "TC,N,V_smartRoutingCapability"
+ "TC,R"
+ "TC,R,V_battery1"
+ "TC,R,V_battery2"
+ "TC,R,V_battery3"
+ "TC,R,V_battery4"
+ "TC,R,V_battery5"
+ "TC,R,V_colorRaw"
+ "TC,R,V_lidOpenCount"
+ "TC,R,V_misc1"
+ "TC,R,V_reserved"
+ "TC,R,V_status1"
+ "TC,R,V_status2"
+ "TC,R,V_status3"
+ "TC,R,V_status4"
+ "TC,R,V_status5"
+ "TC,R,V_statusFlags1"
+ "TC,R,V_subType"
+ "TC,R,V_timeUntilCharged"
+ "TC,R,V_type"
+ "TC,V_caseLedColor"
+ "TC,V_caseLedStatus"
+ "TC,V_caseVersion"
+ "TC,V_chargingOBCTimeUntilCharged"
+ "TC,V_color"
+ "TC,V_lastOrigin"
+ "TI,N,V_gapaFlags"
+ "TI,N,V_ownVoiceActivityLevel"
+ "TI,N,V_productID"
+ "TI,R,V_firmwareVersionRaw"
+ "TI,V_productID"
+ "TI,V_sourceFlags"
+ "TQ,R,N,V_usage"
+ "TQ,R,N,V_usagePage"
+ "TQ,V_chargingRemindersVersion"
+ "TQ,V_newChargingStatusVersion"
+ "TQ,V_pauseMediaOnSleepVersion"
+ "TQ,V_remoteCameraControlVersion"
+ "TR"
+ "TS,N,V_rawGesturesConfigFlags"
+ "TS,N,V_vendorID"
+ "TS,R,V_companyID"
+ "TS,R,V_pid"
+ "Tc,N,V_allowHealthKitDataWrite"
+ "Tc,N,V_allowTemporaryManagedPairing"
+ "Tc,N,V_changeOptimizedBatteryChargingState"
+ "Tc,N,V_chargingReminderEnabled"
+ "Tc,N,V_classicRSSI"
+ "Tc,N,V_connected"
+ "Tc,N,V_doubleTapCapability"
+ "Tc,N,V_enableChargingReminder"
+ "Tc,N,V_enableSleepDetection"
+ "Tc,N,V_guestPaired"
+ "Tc,N,V_healthKitDataWriteAllowed"
+ "Tc,N,V_optimizedBatteryChargingState"
+ "Tc,N,V_paired"
+ "Tc,N,V_sleepDetectionEnabled"
+ "Tc,N,V_temporaryManagedPairedStatus"
+ "Td,N,V_deviceDiscoveryTimeout"
+ "Td,N,V_level"
+ "Td,N,V_subscriptionTimeout"
+ "Td,R,N"
+ "Td,V_lastSeen"
+ "TemporarilyDisabled"
+ "TemporaryManagedPairing"
+ "This: %s - %s - %s, Other: %s"
+ "Ti,N,V_pid"
+ "Tq,R,N"
+ "Tq,V_state"
+ "Tq,V_type"
+ "Transport"
+ "Triggered %.1fs delayed notifcation for lost sensor data availability"
+ "Trnsp"
+ "Unable to determine HIDReport sender address"
+ "Unable to send stop packet to headphones"
+ "Unsubscribed from all OVAD HID devices"
+ "Unsupported proximity pairing payload[%@]: %@"
+ "UpDn"
+ "Update with AACP battery info[%@]: id-%d(%s) level-%d state-%d(%s) status-%d(%s)"
+ "Update with tethered payload[%@]: %@"
+ "Update with untethered payload[%@]: %@"
+ "Updated device address %@ does not match requested address %@"
+ "V1"
+ "V2"
+ "V3"
+ "V4"
+ "Warning"
+ "Watch"
+ "White"
+ "XPC error %{error}"
+ "_aaDeviceManager"
+ "_accessoryUsageSummaryMessageHandler"
+ "_accessoryUsageSummaryMessageReceived:fromDevice:"
+ "_activeHRMDevice"
+ "_adaptiveVolumeCapability"
+ "_allowHealthKitDataWrite"
+ "_allowTemporaryManagedPairing"
+ "_availableSensors"
+ "_availableSensorsLastNotified"
+ "_availableSensorsLostDelayedNotificationTimer"
+ "_battery1"
+ "_battery2"
+ "_battery3"
+ "_battery4"
+ "_battery5"
+ "_batteryDictionary"
+ "_batteryInfo"
+ "_batteryInfoMessageHandler"
+ "_batteryInfoMessageReceived:fromDevice:"
+ "_batteryMap"
+ "_batteryStateFromCharging:chargingOBC:"
+ "_btAddress"
+ "_btAddressToPIDDict"
+ "_calculateOwnVoiceActivityLevel"
+ "_cameraControlCapability"
+ "_caseIdentifier"
+ "_caseLedColor"
+ "_caseLedStatus"
+ "_caseVersion"
+ "_changeOptimizedBatteryChargingState"
+ "_chargingOBCTimeUntilCharged"
+ "_chargingReminderCapability"
+ "_chargingReminderEnabled"
+ "_chargingRemindersVersion"
+ "_classicRSSI"
+ "_clearCombinedBattery"
+ "_cloudRecordInfoLoaded"
+ "_colorRaw"
+ "_companyID"
+ "_connectedAADeviceInfoReceived"
+ "_connectedCBDeviceReceived"
+ "_conversationDetectCapability"
+ "_deviceBatteryInfoLostHandler"
+ "_deviceBatteryInfoUpdatedHandler"
+ "_deviceDiscoveryTimeout"
+ "_deviceWithIdentifier:"
+ "_discoveryTimer"
+ "_doubleTapCapability"
+ "_enableChargingReminder"
+ "_enableSleepDetection"
+ "_endCallCapability"
+ "_enhancedTransparencyVersion"
+ "_farFieldUplinkCapability"
+ "_findMyGroupIdentifier"
+ "_firmwareVersionRaw"
+ "_gapaFlags"
+ "_getBTAddressFromHIDDeviceObject:"
+ "_guestPaired"
+ "_healthKitDataWriteAllowed"
+ "_hidDevice"
+ "_hidManager"
+ "_hrmCapableDeviceRoutedStateChangedHandler"
+ "_isConnected"
+ "_isNearby"
+ "_isSREnabled"
+ "_isSetupComplete"
+ "_isSubscribed"
+ "_isSystemEligibleForSiriHijack"
+ "_lastBudInCaseWithCurrentBud"
+ "_lastConnectedHost"
+ "_lastOrigin"
+ "_lastSeen"
+ "_lastSeenConnectedTime"
+ "_level"
+ "_lidOpenCount"
+ "_manufacturerData"
+ "_misc1"
+ "_model"
+ "_muteControlCapability"
+ "_newChargingStatusVersion"
+ "_notifyAvailabilityChangedWithForcedUpdate:"
+ "_onConnectionActionsCalled"
+ "_optimizedBatteryChargingCapability"
+ "_optimizedBatteryChargingState"
+ "_ovadAAHIDDeviceDict"
+ "_ovadStreamingCapability"
+ "_ovadSubscriptionHelperWithCompletion:completion:"
+ "_ownVoiceActivityLevel"
+ "_paired"
+ "_pairedAADeviceInfoReceived"
+ "_pairedCBDeviceReceived"
+ "_parsePayloads"
+ "_pauseMediaOnSleepVersion"
+ "_payloadData"
+ "_payloads"
+ "_peerAutoANCCapability"
+ "_pid"
+ "_pmeEverywhereCapability"
+ "_productName"
+ "_rawGestureMessageHandler"
+ "_rawGestureMessageReceived:fromDevice:"
+ "_rawGesturesConfigFlags"
+ "_rawOwnVoiceActivityLevel"
+ "_remoteCameraControlConfig"
+ "_remoteCameraControlVersion"
+ "_requestedSensorRates"
+ "_routed"
+ "_selectiveSpeechListeningCapability"
+ "_sendDeviceConfigDirect:identifier:completion:"
+ "_sendDeviceConfigXPC:identifier:completion:"
+ "_sendSettingsChanges:device:"
+ "_sensorAvailabilityUpdatedHandler"
+ "_sensorDataAvailabilitiesAdded:"
+ "_sensorDataAvailabilitiesLost:"
+ "_sensorDataAvailabilitiesLostDelayedNotification"
+ "_sensorDataInfoUpdatedHandler"
+ "_sensorInfo"
+ "_serialNumber"
+ "_serialNumberLeft"
+ "_serialNumberRight"
+ "_showProxStatus"
+ "_siriHijackEligibilityUpdatedHandler"
+ "_sleepDetectionCapability"
+ "_sleepDetectionEnabled"
+ "_sleepDetectionMessageHandler"
+ "_sleepDetectionMessageReceived:fromDevice:"
+ "_smartRoutingCapability"
+ "_sourceFlags"
+ "_status1"
+ "_status2"
+ "_status3"
+ "_status4"
+ "_status5"
+ "_statusFlags1"
+ "_subType"
+ "_submitFeaturesChangeMetrics:forFeature:forDevice:"
+ "_subscriptionErrorHandler"
+ "_subscriptionTimeout"
+ "_subscriptionTimer"
+ "_temporaryManagedPairedStatus"
+ "_threshold"
+ "_timeUntilCharged"
+ "_transport"
+ "_type"
+ "_updateBatteriesFromTetheredAdvertisement:"
+ "_updateBatteriesFromUntetheredAdvertisement:"
+ "_updateCaseInfo:"
+ "_updateChargingOBCTimeUntilCharged:"
+ "_updateCombinedBattery"
+ "_updateWithAACPBatteryInfo:"
+ "_updateWithNearbyBattery:forType:withSource:"
+ "_updateWithProximityPairingPayload:"
+ "_usage"
+ "_usagePage"
+ "aabs"
+ "abrt"
+ "acceptReplyPlayPause Cfg %s, "
+ "accessoryUsageSummaryMessageHandler"
+ "activeHRMDevice"
+ "activeHRMDeviceChanged:"
+ "activeHRMDeviceChanged:withSREnabled:"
+ "adaptiveVolumeCapability"
+ "advertisementPayloadWithData:"
+ "allocWithZone:"
+ "allowHealthKitDataWrite"
+ "allowTemporaryManagedPairing"
+ "apCp"
+ "apple_airpods_case"
+ "apple_magic_keyboard"
+ "apple_magic_keyboard_keypad"
+ "apple_magic_keyboard_touch"
+ "apple_magic_keyboard_touch_keypad"
+ "apple_magic_mouse"
+ "apple_magic_trackpad"
+ "apple_mighty_mouse"
+ "apple_wireless_keyboard"
+ "apple_wireless_mouse"
+ "areAnyBatteriesAvailable"
+ "audioState"
+ "autoANC Cap %s, "
+ "autoANC strength %s, "
+ "autoAncCapability"
+ "avCg"
+ "avCp"
+ "baIn"
+ "baca"
+ "baco"
+ "bad source address: %@"
+ "bale"
+ "bama"
+ "bari"
+ "batteries"
+ "battery1"
+ "battery2"
+ "battery3"
+ "battery4"
+ "battery5"
+ "batteryCase"
+ "batteryCombinedLeftRight"
+ "batteryForType:"
+ "batteryInfo"
+ "batteryInfoMessageHandler"
+ "batteryLeft"
+ "batteryMain"
+ "batteryMap"
+ "batteryRight"
+ "bbl Cap %s, "
+ "bbl Cfg %s, "
+ "bipd"
+ "btAddress"
+ "bta"
+ "btyl"
+ "budRole"
+ "budSide"
+ "bundleWithIdentifier:"
+ "c24@0:8@16"
+ "cOBC"
+ "cOTC"
+ "cREn"
+ "cRcp"
+ "cam ctl Cap %s, "
+ "cam ctl Cfg %s, "
+ "cameraControlCapability"
+ "cancel"
+ "cas snd %s, "
+ "caseBatteryCharging"
+ "caseBatteryLevel"
+ "caseBatteryValid"
+ "caseColor"
+ "caseIdentifier"
+ "caseInsensitiveCompare:"
+ "caseLedColor"
+ "caseLedStatus"
+ "caseVersion"
+ "ccCg"
+ "ccCp"
+ "cdCg"
+ "cdCp"
+ "chR"
+ "changeOptimizedBatteryChargingState"
+ "chargeStatus"
+ "charging"
+ "chargingOBC"
+ "chargingOBCTimeUntilCharged"
+ "chargingReminderCapability"
+ "chargingReminderEnabled"
+ "chargingRemindersVersion"
+ "chr rem Cap %s, "
+ "chr rem En %s, "
+ "clHl"
+ "clHr"
+ "classicRSSI"
+ "clearData"
+ "clearExpiredBatteries"
+ "close"
+ "cloudRecordInfoLoaded"
+ "colorBest"
+ "colorRaw"
+ "colr"
+ "com.apple.CoreBluetooth"
+ "com.apple.HeadphoneFeaturesChange"
+ "companyID"
+ "connected"
+ "connectedAADeviceInfoReceived"
+ "connectedCBDeviceReceived"
+ "connectedInfoComplete"
+ "connectedSourceCount"
+ "conversationDetectCapability"
+ "copyWithZone:"
+ "crDr"
+ "cupColor"
+ "dataWithBytes:length:"
+ "dateWithTimeIntervalSince1970:"
+ "declineDismissSkip Cfg %s, "
+ "decodeDoubleForKey:"
+ "decodeIntegerForKey:"
+ "describeProperties"
+ "detected hgs %s, "
+ "deviceBatteryInfoLostHandler"
+ "deviceBatteryInfoUpdatedHandler"
+ "deviceDiscoveryTimeout"
+ "deviceFlags"
+ "deviceManagerActivateDirect:completion:"
+ "deviceManagerFetchAADeviceBatteryInfoForAddress:deviceHandler:"
+ "deviceManagerFetchAADeviceBatteryInfoForIdentifier:deviceHandler:"
+ "deviceManagerFetchAudioAccessoryDeviceForBTAddress:deviceHandler:"
+ "deviceManagerFetchPairedAudioAccessoryDevices:"
+ "deviceManagerFoundBatteryInfo:"
+ "deviceManagerFoundHandler:"
+ "deviceManagerInvalidateDirect:"
+ "deviceManagerLostBatteryInfo:"
+ "deviceManagerSendDeviceConfigDirect:identifier:completion:"
+ "deviceManagerUpdateDirect:"
+ "deviceNotificationHandler:added:"
+ "dictionary"
+ "doubleTapCapability"
+ "dtAL"
+ "dtAR"
+ "dtCp"
+ "eCC"
+ "eChR"
+ "ear fit %s, "
+ "ecCp"
+ "enableChargingReminder"
+ "enableSleepDetection"
+ "encodeDouble:forKey:"
+ "endCallCapability"
+ "enh trn Ver %s,"
+ "enhancedTransparencyVersion"
+ "entv"
+ "esld"
+ "farFieldUplinkCapability"
+ "faultDetected"
+ "fbin"
+ "fetchAADeviceBatteryInfoForAddress:"
+ "fetchAADeviceBatteryInfoForIdentifier:"
+ "fetchAudioAccessoryDeviceForBTAddress:"
+ "fetchHealthKitDataWriteAllowedForDevice:"
+ "fetchPairedAudioAccessoryDevices"
+ "fetchPairedHRMDevices:"
+ "fetched pairedDevices %@ "
+ "ff upl %s, "
+ "findMyGroupIdentifier"
+ "firmwareVersionRaw"
+ "fqBd %s, "
+ "fuCp"
+ "fullyCharged"
+ "gapa"
+ "gapaFlags"
+ "getBytes:length:"
+ "guPd"
+ "guestPaired"
+ "ha Cap %s, "
+ "ha En %s, "
+ "ha Enr %s, "
+ "ha top lvl %s, "
+ "haGS En %s, "
+ "handleHIDReport:data:"
+ "healthKitDataWriteAllowed"
+ "hg tgl %s, "
+ "hidDevice"
+ "hide er dt %s, "
+ "hide off %s, "
+ "hkWr"
+ "hp Cap %s, "
+ "hrmCapableDeviceRoutedStateChangedHandler"
+ "idfb"
+ "idleTime"
+ "inAACP"
+ "informDRClientSensorDataAvailable:dataTypes:completion:"
+ "informDRClientSensorDataUnavailable:dataTypes:completion:"
+ "initLogParseError:"
+ "initWithAACPBatteryInfo:productID:"
+ "initWithData:"
+ "initWithDomain:code:userInfo:"
+ "initWithFormat:"
+ "initWithHIDDevice:"
+ "initWithHIDDeviceAndSensorInfo:sensorInfo:"
+ "initWithLevel:productID:state:type:"
+ "initWithOptions:"
+ "intValue"
+ "integerValue"
+ "invalidBattery"
+ "isCase"
+ "isCaseBattery"
+ "isChargingPaused"
+ "isConnected"
+ "isEqualToAdvertisement:"
+ "isEqualToBattery:"
+ "isEqualToData:"
+ "isEqualToPayload:"
+ "isEqualToString:"
+ "isExpired"
+ "isLow"
+ "isNearby"
+ "isSetupComplete"
+ "isSubscribed"
+ "isSupported"
+ "isSystemEligibleForSiriHijack"
+ "isTemporaryPairingConnectionAllowed"
+ "isTemporaryPairingConnectionAllowed:"
+ "itbc"
+ "lastBudInCaseWithCurrentBud"
+ "lastConnectedHost"
+ "lastConnectedHostSignedInToICloud"
+ "lastOrigin"
+ "lastSeen"
+ "lastSeenConnectedTime"
+ "lastSeenTime"
+ "leftBatteryCharging"
+ "leftBatteryLevel"
+ "leftBatteryValid"
+ "leftColor"
+ "level"
+ "lidClosed"
+ "lidOpenCount"
+ "localTimeZone"
+ "localizedStringForKey:value:table:"
+ "lowLevel"
+ "ls: %@"
+ "lstS"
+ "mCC"
+ "mCCp"
+ "mainBatteryCharging"
+ "mainBatteryLevel"
+ "mainBatteryValid"
+ "manufacturerData"
+ "manufacturerDataWithData:"
+ "micM"
+ "misc1"
+ "missing data from Firmware Version bytes."
+ "missing data from Payload Length byte."
+ "missing data from Payload Type byte."
+ "missing data from Product Id bytes."
+ "missing data from Sub-type byte."
+ "missing data from Time Until Charged byte."
+ "missing data from battery 1 byte."
+ "missing data from battery 2 byte."
+ "missing data from battery 3 byte."
+ "missing data from battery1 bit."
+ "missing data from battery2 bit."
+ "missing data from battery3 bit."
+ "missing data from battery4 bit."
+ "missing data from battery5 bit."
+ "missing data from color bit."
+ "missing data from lastBudInCaseWithCurrentBud bits."
+ "missing data from lastConnectedHost bits."
+ "missing data from misc1 bit."
+ "missing data from reserved byte."
+ "missing data from status 2 byte."
+ "missing data from status flags 1."
+ "missing data from status1 bit."
+ "missing data from status2 bit."
+ "missing data from status3 bit."
+ "missing data from status4 bit."
+ "missing data from status5 bit."
+ "model"
+ "modl"
+ "muteControlCapability"
+ "myBatteryCharging"
+ "myBatteryLevel"
+ "myBatteryValid"
+ "nCh"
+ "needsConnection"
+ "needsUpdateToPairedDevice"
+ "newChargingStatusVersion"
+ "numberWithDouble:"
+ "numberWithInteger:"
+ "numberWithUnsignedInt:"
+ "onConnectionActionsCalled"
+ "open"
+ "optimizedBatteryChargingCapability"
+ "optimizedBatteryChargingState"
+ "osCp"
+ "otherBatteryCharging"
+ "otherBatteryLevel"
+ "otherBatteryValid"
+ "outOfBoxMode"
+ "outOfCaseTime"
+ "ovadStreamingCapability"
+ "ovd str %s, "
+ "ownVoiceActivityLevel"
+ "pMOS"
+ "paired"
+ "pairedAADeviceInfoReceived"
+ "pairedCBDeviceReceived"
+ "pairedInfoComplete"
+ "pauseMediaOnSleepVersion"
+ "payloadData"
+ "payloads"
+ "peerAutoANCCapability"
+ "pid"
+ "pid %u, "
+ "plmd %s, "
+ "pmeEverywhereCapability"
+ "pmee"
+ "pmee %s, "
+ "prID"
+ "prN"
+ "prewarmAudioAccessoriesForFitnessWorkout"
+ "prewarmAudioAccessoriesForFitnessWorkout:"
+ "prewarmAudioAccessoriesForFitnessWorkout: starting xpc"
+ "primaryBluetoothAddress"
+ "primaryLocation"
+ "primaryProductID"
+ "productInfoWithProductID:"
+ "productName"
+ "propertyForKey:"
+ "proximityPairingPayload"
+ "proximityPairingPayloadWithData:"
+ "proximityPairingStatusPayloadWithData:pid:"
+ "prpl %s, "
+ "q"
+ "q16@0:8"
+ "q24@0:8B16B20"
+ "r"
+ "rCC"
+ "rawGestureMessageHandler"
+ "rawGesturesConfigFlags"
+ "rccc"
+ "remoteCameraControlConfig"
+ "remoteCameraControlVersion"
+ "remoteObjectInterface"
+ "removeBatteryInMap:"
+ "rgCg"
+ "rgCg %@, "
+ "rightBatteryCharging"
+ "rightBatteryLevel"
+ "rightBatteryValid"
+ "rightColor"
+ "rssi"
+ "rutd"
+ "scpl %s, "
+ "sdcp"
+ "secondaryLocation"
+ "secondsFromGMT"
+ "selectiveSpeechListeningCapability"
+ "sendSettingsChanges:device:"
+ "sendSleepDetectionMessage message to destination %@"
+ "sendSleepDetectionMessage:destinationIdentifier:completionHandler:"
+ "sensorAvailabilityUpdatedHandler"
+ "sensorDataInfoUpdatedHandler"
+ "sensorInfo"
+ "serialNumber"
+ "serialNumberLeft"
+ "serialNumberRight"
+ "setAccessoryUsageSummaryMessageHandler:"
+ "setAdaptiveVolumeCapability:"
+ "setAllowHealthKitDataWrite:"
+ "setAllowTemporaryManagedPairing:"
+ "setBatteryInMap:"
+ "setBatteryInfo:"
+ "setBatteryInfoMessageHandler:"
+ "setBatteryMap:"
+ "setBtAddress:"
+ "setCameraControlCapability:"
+ "setCaseIdentifier:"
+ "setCaseLedColor:"
+ "setCaseLedStatus:"
+ "setCaseVersion:"
+ "setChangeOptimizedBatteryChargingState:"
+ "setChargingOBCTimeUntilCharged:"
+ "setChargingReminderCapability:"
+ "setChargingReminderEnabled:"
+ "setChargingRemindersVersion:"
+ "setClassicRSSI:"
+ "setCloudRecordInfoLoaded:"
+ "setConnected:"
+ "setConnectedAADeviceInfoReceived:"
+ "setConnectedCBDeviceReceived:"
+ "setConversationDetectCapability:"
+ "setDefaultConfigurationsForCloudSyncedPropertiesIfNeeded"
+ "setDeviceBatteryInfoLostHandler:"
+ "setDeviceBatteryInfoUpdatedHandler:"
+ "setDeviceDiscoveryTimeout:"
+ "setDeviceMatching:"
+ "setDeviceNotificationHandler:"
+ "setDoubleTapCapability:"
+ "setEnableChargingReminder:"
+ "setEnableSleepDetection:"
+ "setEndCallCapability:"
+ "setEnhancedTransparencyVersion:"
+ "setFarFieldUplinkCapability:"
+ "setFindMyGroupIdentifier:"
+ "setGapaFlags:"
+ "setGuestPaired:"
+ "setHealthKitDataWriteAllowed:"
+ "setHrmCapableDeviceRoutedStateChangedHandler:"
+ "setInputReportHandler:"
+ "setIsConnected:"
+ "setIsNearby:"
+ "setIsSetupComplete:"
+ "setIsSubscribed:"
+ "setLastOrigin:"
+ "setLastSeen:"
+ "setLastSeenConnectedTime:"
+ "setLevel:"
+ "setModel:"
+ "setMuteControlCapability:"
+ "setNewChargingStatusVersion:"
+ "setOnConnectionActionsCalled:"
+ "setOptimizedBatteryChargingCapability:"
+ "setOptimizedBatteryChargingState:"
+ "setOvadStreamingCapability:"
+ "setOwnVoiceActivityLevel:"
+ "setPaired:"
+ "setPairedAADeviceInfoReceived:"
+ "setPairedCBDeviceReceived:"
+ "setPauseMediaOnSleepVersion:"
+ "setPeerAutoANCCapability:"
+ "setPid:"
+ "setPmeEverywhereCapability:"
+ "setProductName:"
+ "setRawGestureMessageHandler:"
+ "setRawGesturesConfigFlags:"
+ "setRemoteCameraControlConfig:"
+ "setRemoteCameraControlVersion:"
+ "setReport failed with error: %@"
+ "setReport:reportLength:withIdentifier:forType:error:"
+ "setRouted:"
+ "setSelectiveSpeechListeningCapability:"
+ "setSensorAvailabilityUpdatedHandler:"
+ "setSensorDataInfoUpdatedHandler:"
+ "setSensorInfo:"
+ "setSerialNumber:"
+ "setSerialNumberLeft:"
+ "setSerialNumberRight:"
+ "setSiriHijackEligibilityUpdatedHandler:"
+ "setSleepDetectionCapability:"
+ "setSleepDetectionEnabled:"
+ "setSleepDetectionMessageHandler:"
+ "setSmartRoutingCapability:"
+ "setSourceFlags:"
+ "setState:"
+ "setSubscriptionTimeout:"
+ "setTemporaryManagedPairedStatus:"
+ "setType:"
+ "setWithObjects:"
+ "sharedInstance"
+ "showFitEducationNotificationForDevice:"
+ "showHIDConnectedBannerAperture:completion:"
+ "showProxStatus"
+ "siriHijackEligibilityUpdated:"
+ "siriHijackEligibilityUpdatedHandler"
+ "sldt Cap %s, "
+ "sldt Tg %s, "
+ "sleepDetectionCapability"
+ "sleepDetectionEnabled"
+ "sleepDetectionMessageHandler"
+ "smRtS %@, "
+ "smartRoutingCapability"
+ "smartRoutingConnected"
+ "smartRoutingScoreSource1"
+ "smartRoutingScoreSource2"
+ "sn"
+ "snLe"
+ "snRi"
+ "soundEnabled"
+ "sourceFlags"
+ "spAl"
+ "srCp"
+ "srMd"
+ "srMt Cap %s, "
+ "srMt Tg %s, "
+ "ssCf"
+ "ssCp"
+ "stAoS %s, "
+ "status1"
+ "status2"
+ "status3"
+ "status4"
+ "status5"
+ "statusFlags1"
+ "subType"
+ "subdataWithRange:"
+ "subscribeWithFlags:"
+ "subscribeWithFlags:rate:"
+ "subscribeWithFlagsWithCompletion:completion:"
+ "subscribeWithFlagsWithCompletion:rate:completion:"
+ "subscribeWithSensorDataFlags:completion:"
+ "subscribeWithSensorDataFlags:rate:completion:"
+ "subscriptionTimeout"
+ "supportWirelessSplitter"
+ "supportedPID:"
+ "sync fetch for AADeviceBatteryInfo address: %@ returned: %@ "
+ "sync fetch for AADeviceBatteryInfo id: %@ returned: %@ "
+ "sync fetch for AudioAccessoryDevice id: %@ returned: %@ "
+ "systemStateMonitorFetchHealthKitDataWriteAllowedForDevice:completionHandler:"
+ "systemStateMonitorFetchPairedHRMDevices:"
+ "systemStateMonitorReportActiveHRMDeviceChanged:withSREnabled:"
+ "systemStateMonitorReportSiriHijackEligibilityChanged:"
+ "systemStateMonitorShowFitEducationNotificationForIdentifier:completionHandler:"
+ "t-"
+ "temp mg paired %s, "
+ "temporaryManagedPairedStatus"
+ "timeIntervalSince1970"
+ "timeUntilCharged"
+ "tmpM"
+ "transport"
+ "type"
+ "unsubscribeAll"
+ "unsubscribeWithFlags:"
+ "unsubscribeWithSensorDataFlags:"
+ "unsupportedAccessoryConnected"
+ "update:"
+ "updateWithAABattery:"
+ "updateWithAACPBatteryInfoData:"
+ "updateWithAADeviceConfig:"
+ "updateWithAANearbyDevice:"
+ "updateWithConnectedAADeviceInfo:"
+ "updateWithConnectedCBDevice:"
+ "updateWithConnectedDevice:"
+ "updateWithDisconnectedDevice:"
+ "updateWithPairedAADevice:"
+ "updateWithPairedAADeviceInfo:"
+ "updateWithPairedCBDevice:"
+ "usage"
+ "usagePage"
+ "usbAudioConnected"
+ "utpConnected"
+ "v12@?0c8"
+ "v16@?0@\"AADeviceBatteryInfo\"8"
+ "v16@?0@\"NSDictionary\"8"
+ "v20@0:8S16"
+ "v20@?0@\"HIDDevice\"8B16"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8*16"
+ "v24@0:8@\"AAAudioRoutingControl\"16"
+ "v24@0:8@\"AADeviceBatteryInfo\"16"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8I16I20"
+ "v24@0:8q16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v28@0:8@\"AudioAccessoryDevice\"16B24"
+ "v28@0:8@16B24"
+ "v28@0:8I16@?20"
+ "v29@0:8{?=CI}16@?21"
+ "v32@0:8@\"CBDevice\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"AADeviceBatteryInfo\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"AudioAccessoryDevice\">24"
+ "v32@0:8@\"NSString\"16@?<v@?c>24"
+ "v32@0:8I16I20@?24"
+ "v36@0:8I16@20@28"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v48@?0@\"HIDDevice\"8Q16q24q32@\"NSData\"40"
+ "valid"
+ "vid"
+ "visibleBatteryCase"
+ "visibleBatteryCombinedLeftRight"
+ "visibleBatteryLeft"
+ "visibleBatteryMain"
+ "visibleBatteryRight"
+ "wibn"
+ "wmib"
+ "\xfe"
- ", AStS %s"
- ", HA Cap %s"
- ", HA GS %s"
- ", HA Top Level %s"
- ", HG Prox Sh %s"
- ", HG Tgl %s"
- ", HP Cap %s"
- ", HRM En %s"
- ", HT Cap %s"
- ", Hide Er Dt Cap %s"
- ", Hide Off Cap %s"
- ", Hr Aid En %s"
- ", LsMd Off %s"
- ", acceptReplyPlayPause Cfg %s"
- ", autoANC Cap %s"
- ", bbl Cap %s"
- ", bbl Cfg %s"
- ", cas snd Cap %s"
- ", declineDismissSkip Cfg %s"
- ", detected hgs %s"
- ", ear fit Cap %s"
- ", fqBd %s"
- ", plmd %s"
- ", prpl %s"
- ", scpl %s"
- ", smRtS %@"
- ", srMt Cap %s"
- ", srMt Tg %s"
- ", stAoS %s"
- "-[AADeviceManager _activate:]_block_invoke_2"
- "-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke_2"
- "-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke_3"
- "AADeviceRecordCloudSync"
- "AudioAccessoryDevice identifier: %@"
- "HRMCapableDeviceChangedHandler"
- "HgPc"
- "Re-activate XPC, CID 0x%X"
- "T@?,C,V_HRMCapableDeviceChangedHandler"
- "TB,R,V_isHRMCapableDevicePresent"
- "_HRMCapableDeviceChangedHandler"
- "_isHRMCapableDevicePresent"
- "b"
- "isHRMCapableDevicePresent"
- "needsUpdateToDeviceCloudRecord"
- "setDefaultConfigurationsIfNeeded"
- "setHRMCapableDeviceChangedHandler:"
- "updateWithAADeviceInfo:"
- "updateWithCBDevice:"
- "\x86"

```
