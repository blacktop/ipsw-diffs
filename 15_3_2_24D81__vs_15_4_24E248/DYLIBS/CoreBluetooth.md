## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth`

```diff

-183.9.1.0.1
-  __TEXT.__text: 0x9d1e4
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x7f60
-  __TEXT.__const: 0x2250
-  __TEXT.__oslogstring: 0x25a0
-  __TEXT.__cstring: 0x11be5
-  __TEXT.__gcc_except_tab: 0x2340
+184.42.0.3.0
+  __TEXT.__text: 0x9fb84
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_methlist: 0x8cc4
+  __TEXT.__const: 0x2503
+  __TEXT.__oslogstring: 0x269a
+  __TEXT.__cstring: 0x12418
+  __TEXT.__gcc_except_tab: 0x2410
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x1b20
-  __TEXT.__objc_classname: 0x685
-  __TEXT.__objc_methname: 0x138f0
-  __TEXT.__objc_methtype: 0x21c1
-  __TEXT.__objc_stubs: 0x89c0
+  __TEXT.__unwind_info: 0x1d00
+  __TEXT.__objc_classname: 0x6c3
+  __TEXT.__objc_methname: 0x14b8c
+  __TEXT.__objc_methtype: 0x2266
+  __TEXT.__objc_stubs: 0x8e20
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x38e0
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0x3b60
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41c0
+  __DATA_CONST.__objc_selrefs: 0x45c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x870
-  __AUTH_CONST.__const: 0x1200
-  __AUTH_CONST.__cfstring: 0xaca0
-  __AUTH_CONST.__objc_const: 0x10ce0
-  __AUTH_CONST.__objc_intobj: 0x8a0
+  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__const: 0x1220
+  __AUTH_CONST.__cfstring: 0xaf20
+  __AUTH_CONST.__objc_const: 0x10958
+  __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0xe38
+  __AUTH.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0xef4
   __DATA.__data: 0xf10
   __DATA.__common: 0x18
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AB226465-3437-36E3-93F0-C0A3478D132B
-  Functions: 3387
-  Symbols:   7220
-  CStrings:  8734
+  UUID: 0ED13376-D469-3997-B727-7CC918FB07D5
+  Functions: 3755
+  Symbols:   8038
+  CStrings:  9060
 
Symbols:
+ +[CBController ardRunning].cold.1
+ +[CBController ardRunning].cold.2
+ +[CBController ardRunning].cold.3
+ +[CBController bluetoothModificationAllowed].cold.1
+ +[CBController featureFlags].cold.1
+ +[CBController getAllowedToPowerOffBluetoothState].cold.1
+ +[CBController getAllowedToPowerOffBluetoothState].cold.2
+ +[CBController getAllowedToPowerOffBluetoothState].cold.3
+ +[CBController getAllowedToPowerOffBluetoothState].cold.4
+ +[CBController getAllowedToPowerOffBluetoothState].cold.5
+ +[CBController getAllowedToPowerOffBluetoothState].cold.6
+ +[CBController readPrefKeys:error:].cold.1
+ +[CBController setOfflineAdvertisingParams:].cold.1
+ +[CBManager authorization].cold.4
+ +[CBManager authorization].cold.5
+ +[CBManager authorization].cold.6
+ +[CBPeripheralManager authorizationStatus].cold.2
+ +[CBSpatialInteractionSession dictionaryWithTokenData:error:].cold.1
+ +[CBUtil decodeApplePayloadByteStream:].cold.1
+ +[CBUtil decodeApplePayloadByteStream:].cold.2
+ +[CBUtil isDeviceSupported:].cold.1
+ +[CBUtil isDeviceSupportedOnWatchOS:].cold.1
+ +[CBUtil isDeviceSupportedOnWatchOS:].cold.2
+ +[CBUtil isDeviceSupportedOnWatchOS:].cold.3
+ +[CBUtil isDeviceSupportedOnWatchOS:].cold.4
+ +[CBUtil isDeviceSupportedOnWatchOS:].cold.5
+ +[CBUtil isDeviceSupportedOnXROS:].cold.2
+ +[CBUtil isDeviceSupportedOnXROS:].cold.3
+ +[CBUtil isDeviceSupportedOnXROS:].cold.4
+ +[CBUtil isDeviceSupportedOnXROS:].cold.5
+ +[CBUtil isDeviceSupportedOnXROS:].cold.6
+ +[CBUtil preSSPPairingCodeToString:].cold.1
+ +[CBUtil preSSPStringToPairingCode:].cold.1
+ +[NSError(CoreBluetooth) errorWithInfo:].cold.3
+ +[NSError(CoreBluetooth) errorWithInfo:].cold.4
+ -[CBAdvertiser _xpcReceivedPowerStateChanged:].cold.1
+ -[CBAdvertiser advertisingSoftwareUpdateDataArrayCountMaximumLimit]
+ -[CBAdvertiser setSoftwareUpdateActionType:]
+ -[CBAdvertiser setSoftwareUpdateDataArray:]
+ -[CBAdvertiser softwareUpdateActionType]
+ -[CBAdvertiser softwareUpdateDataArrayCountMaximumLimit]
+ -[CBAdvertiser softwareUpdateDataArray]
+ -[CBAudioLinkQualityInfo descriptionWithLevel:].cold.1
+ -[CBCentralManager HandleBluetoothUsageEventMsg:].cold.1
+ -[CBCentralManager HandleRssiDetectionUpdateMsg:].cold.1
+ -[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:].cold.2
+ -[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:].cold.3
+ -[CBCentralManager cancelPeripheralConnection:force:].cold.1
+ -[CBCentralManager cancelPeripheralConnection:options:].cold.1
+ -[CBCentralManager connectPeripheral:options:].cold.1
+ -[CBCentralManager connectWhbCBPeripheral:withCompletion:].cold.2
+ -[CBCentralManager connectWhbCBPeripheral:withCompletion:].cold.3
+ -[CBCentralManager createOfflineLEDevices:]
+ -[CBCentralManager csCreateConfig:options:].cold.1
+ -[CBCentralManager csProcedureEnable:options:].cold.1
+ -[CBCentralManager csReadRemoteSupportedCapabilities:].cold.1
+ -[CBCentralManager csRemoveConfig:options:].cold.1
+ -[CBCentralManager csSecurityEnable:].cold.1
+ -[CBCentralManager csSetProcedureParams:options:].cold.1
+ -[CBCentralManager csTest:].cold.1
+ -[CBCentralManager csWriteCachedRemoteSupportedCapabilities:options:].cold.1
+ -[CBCentralManager enableMrc:options:].cold.1
+ -[CBCentralManager handleApplicationConnectionEventDidOccur:].cold.2
+ -[CBCentralManager handleCSProcedureEventMsg:]
+ -[CBCentralManager handleCSProcedureEventMsg:].cold.1
+ -[CBCentralManager handleMsg:args:].cold.3
+ -[CBCentralManager handleMsg:args:].cold.4
+ -[CBCentralManager handlePeerMTUChanged:].cold.2
+ -[CBCentralManager handlePeripheralConnectionCompleted:].cold.3
+ -[CBCentralManager handlePeripheralConnectionCompleted:].cold.4
+ -[CBCentralManager handlePeripheralConnectionCompleted:].cold.5
+ -[CBCentralManager handlePeripheralDisconnectionCompleted:].cold.1
+ -[CBCentralManager handleRestoringState:].cold.1
+ -[CBCentralManager handleScanFailedToStartWithError:].cold.4
+ -[CBCentralManager handleScanFailedToStartWithError:].cold.5
+ -[CBCentralManager handleScanFailedToStartWithError:].cold.6
+ -[CBCentralManager initWithDelegate:queue:options:].cold.2
+ -[CBCentralManager initWithDelegate:queue:options:].cold.3
+ -[CBCentralManager randomizeAFHMapForPeripheral:].cold.1
+ -[CBCentralManager retrieveAddressForPeripheral:].cold.1
+ -[CBCentralManager retrieveConnectedPeripheralsWithServices:].cold.1
+ -[CBCentralManager retrieveConnectionHandleWithIdentifier:completion:].cold.1
+ -[CBCentralManager retrievePairingInfoForPeripheral:].cold.1
+ -[CBCentralManager retrievePeripheralWithAddress:].cold.2
+ -[CBCentralManager retrievePeripheralsWithCustomProperties:completion:].cold.1
+ -[CBCentralManager retrievePeripheralsWithIdentifiers:].cold.1
+ -[CBCentralManager retrievePeripheralsWithIdentifiers:completion:].cold.1
+ -[CBCentralManager retrievePeripheralsWithTags:completion:].cold.1
+ -[CBCentralManager retrieveWhbCBPeripheralWithInfo:].cold.2
+ -[CBCentralManager retrieveWhbCBPeripheralWithInfo:].cold.3
+ -[CBCentralManager retrieveWhbCBPeripheralWithInfo:].cold.4
+ -[CBCentralManager retrieveWhbCBPeripheralWithInfo:].cold.5
+ -[CBCentralManager retrieveWhbCBPeripheralWithInfo:].cold.6
+ -[CBCentralManager setBluetoothPhyStatisticsNotifications:options:].cold.1
+ -[CBCentralManager setBluetoothUsageNotifications:options:].cold.1
+ -[CBCentralManager setDataLengthChange:options:].cold.1
+ -[CBCentralManager setDesiredConnectionLatency:forPeripheral:].cold.1
+ -[CBCentralManager setDesiredConnectionLatency:forPeripheral:completion:].cold.1
+ -[CBCentralManager setLESetPhy:options:].cold.1
+ -[CBCentralManager setLeAFHMap:].cold.1
+ -[CBCentralManager setRSSIStatisticsDetection:options:].cold.1
+ -[CBCentralManager startTrackingPeripheral:options:].cold.1
+ -[CBCentralManager stopTrackingPeripheral:options:].cold.1
+ -[CBCharacteristic handleDescriptorsDiscovered:].cold.2
+ -[CBCharacteristic handleDescriptorsDiscovered:].cold.3
+ -[CBClassicManager addService:].cold.3
+ -[CBClassicManager addService:].cold.4
+ -[CBClassicManager addService:].cold.5
+ -[CBClassicManager addService:sdpRecord:sdpRecordAddedHandler:].cold.3
+ -[CBClassicManager addService:sdpRecord:sdpRecordAddedHandler:].cold.4
+ -[CBClassicManager addService:sdpRecord:sdpRecordAddedHandler:].cold.5
+ -[CBClassicManager addServiceToInquiryList:].cold.3
+ -[CBClassicManager addServiceToInquiryList:].cold.4
+ -[CBClassicManager addServiceToInquiryList:].cold.5
+ -[CBClassicManager addServiceWithData:].cold.1
+ -[CBClassicManager cancelPeerConnection:force:].cold.1
+ -[CBClassicManager cancelPeerConnection:options:].cold.1
+ -[CBClassicManager connectPeer:options:].cold.1
+ -[CBClassicManager connectPeer:options:].cold.2
+ -[CBClassicManager handleMsg:args:].cold.3
+ -[CBClassicManager handleMsg:args:].cold.4
+ -[CBClassicManager handlePeerConnectionCompleted:].cold.2
+ -[CBClassicManager handlePeerConnectionCompleted:].cold.3
+ -[CBClassicManager handlePeerConnectionStateUpdated:].cold.2
+ -[CBClassicManager handlePeerDisconnectionCompleted:].cold.2
+ -[CBClassicManager handlePeerDisconnectionCompleted:].cold.3
+ -[CBClassicManager handlePeerDiscovered:].cold.3
+ -[CBClassicManager handlePeerDiscovered:].cold.4
+ -[CBClassicManager handlePeerDiscovered:].cold.5
+ -[CBClassicManager handleSDPRecordAdded:].cold.2
+ -[CBClassicManager handleServiceAddedToInquiryList:].cold.2
+ -[CBClassicManager handleServiceAddedToSDP:].cold.2
+ -[CBClassicManager removeAllServicesFromInquiryList].cold.2
+ -[CBClassicManager removeAllServices].cold.3
+ -[CBClassicManager removeAllServices].cold.4
+ -[CBClassicManager removeService:].cold.3
+ -[CBClassicManager removeService:].cold.4
+ -[CBClassicManager removeService:].cold.5
+ -[CBClassicManager removeServiceFromInquiryList:].cold.3
+ -[CBClassicManager removeServiceFromInquiryList:].cold.4
+ -[CBClassicManager removeServiceFromInquiryList:].cold.5
+ -[CBClassicManager removeServiceHandle:].cold.3
+ -[CBClassicManager removeServiceHandle:].cold.4
+ -[CBClassicManager removeServiceHandle:].cold.5
+ -[CBClassicManager retrievePairedPeersWithOptions:].cold.3
+ -[CBClassicManager retrievePairedPeersWithOptions:].cold.4
+ -[CBClassicManager retrievePeerWithAddress:].cold.2
+ -[CBClassicManager secureBluetooth:withAuthData:].cold.1
+ -[CBClassicManager startInquiryWithOptions:classicPeerDiscovered:].cold.2
+ -[CBClassicManager startInquiryWithOptions:classicPeerDiscovered:].cold.3
+ -[CBClassicPeer channelWithID:].cold.2
+ -[CBClassicPeer channelWithPSM:].cold.2
+ -[CBClassicPeer closeL2CAPChannel:].cold.2
+ -[CBClassicPeer closeRFCOMMChannel:].cold.2
+ -[CBClassicPeer dealloc].cold.1
+ -[CBClassicPeer getConnectedServices].cold.2
+ -[CBClassicPeer handleL2CAPChannelClosed:].cold.2
+ -[CBClassicPeer handleL2CAPChannelOpened:].cold.2
+ -[CBClassicPeer handleL2CAPChannelOpened:].cold.3
+ -[CBClassicPeer handleMsg:args:].cold.2
+ -[CBClassicPeer handlePeerUpdated:].cold.5
+ -[CBClassicPeer handlePeerUpdated:].cold.6
+ -[CBClassicPeer handlePeerUpdated:].cold.7
+ -[CBClassicPeer handlePeerUpdated:].cold.8
+ -[CBClassicPeer handleRFCOMMChannelClosed:].cold.1
+ -[CBClassicPeer handleRFCOMMChannelOpened:].cold.2
+ -[CBClassicPeer handleRFCOMMChannelOpened:].cold.3
+ -[CBClassicPeer isAACPCapabilityBit:].cold.1
+ -[CBClassicPeer openRFCOMMChannel:options:].cold.2
+ -[CBClassicPeer sendMsg:requiresConnected:args:].cold.3
+ -[CBClassicPeer sendMsg:requiresConnected:args:].cold.4
+ -[CBClassicPeer setName:].cold.1
+ -[CBConnection _prepareWriteRequest:error:].cold.1
+ -[CBConnection _prepareWriteRequest:error:].cold.2
+ -[CBConnection _setupIOAndReturnError:].cold.1
+ -[CBConnection dealloc].cold.1
+ -[CBConnection initWithXPCEventRepresentation:error:].cold.1
+ -[CBConnection pairingAgent:peerDidCompletePairing:].cold.1
+ -[CBConnection pairingAgent:peerDidFailToCompletePairing:error:].cold.1
+ -[CBConnection pairingAgent:peerDidUnpair:].cold.1
+ -[CBConnection xpcReceivedForwardedEvent:].cold.1
+ -[CBConnection xpcReceivedForwardedEvent:].cold.2
+ -[CBConnection xpcReceivedPairingCompleted:].cold.1
+ -[CBConnection xpcReceivedPairingPrompt:].cold.1
+ -[CBController _xpcReceivedDiscoverableStateChanged:].cold.1
+ -[CBController _xpcReceivedInquiryStateChanged:].cold.1
+ -[CBController _xpcReceivedPowerStateChanged:].cold.1
+ -[CBController setLowPowerModeWithParams:params:completion:]
+ -[CBController setLowPowerModeWithParams:params:completion:].cold.1
+ -[CBController setLowPowerModeWithParams:params:completion:].cold.2
+ -[CBController setLowPowerModeWithParams:params:completion:].cold.3
+ -[CBController setLowPowerModeWithParams:params:completion:].cold.4
+ -[CBController setLowPowerModeWithParams:params:completion:].cold.5
+ -[CBController setLowPowerModeWithReason:completion:].cold.1
+ -[CBControllerLowPowerModeParams .cxx_destruct]
+ -[CBControllerLowPowerModeParams actionType]
+ -[CBControllerLowPowerModeParams configFlags]
+ -[CBControllerLowPowerModeParams dataBlob]
+ -[CBControllerLowPowerModeParams dataMask]
+ -[CBControllerLowPowerModeParams description]
+ -[CBControllerLowPowerModeParams deviceIDAdvScanCount]
+ -[CBControllerLowPowerModeParams deviceIDDiagInfo]
+ -[CBControllerLowPowerModeParams deviceIDDiagLength]
+ -[CBControllerLowPowerModeParams deviceIDInfo]
+ -[CBControllerLowPowerModeParams deviceIDInputKeyMaterial]
+ -[CBControllerLowPowerModeParams deviceIDLength]
+ -[CBControllerLowPowerModeParams deviceIDSalt]
+ -[CBControllerLowPowerModeParams deviceIDTimestampEffectiveBits]
+ -[CBControllerLowPowerModeParams deviceIDTimestampFrequency]
+ -[CBControllerLowPowerModeParams deviceIDTimestampLsbsTruncated]
+ -[CBControllerLowPowerModeParams diagnosticTxAdvBackoff]
+ -[CBControllerLowPowerModeParams diagnosticTxAdvDuration]
+ -[CBControllerLowPowerModeParams diagnosticTxAdvInterval]
+ -[CBControllerLowPowerModeParams encodeWithXPCObject:]
+ -[CBControllerLowPowerModeParams gpioAssertionTime]
+ -[CBControllerLowPowerModeParams initWithXPCObject:error:]
+ -[CBControllerLowPowerModeParams macKeyDiagInfo]
+ -[CBControllerLowPowerModeParams macKeyDiagLength]
+ -[CBControllerLowPowerModeParams maxClockDriftSeconds]
+ -[CBControllerLowPowerModeParams nextScanDelay]
+ -[CBControllerLowPowerModeParams numberOfDelayIterations]
+ -[CBControllerLowPowerModeParams packetLength]
+ -[CBControllerLowPowerModeParams rssiThresholdValue]
+ -[CBControllerLowPowerModeParams scanDelayStart]
+ -[CBControllerLowPowerModeParams scanDuration]
+ -[CBControllerLowPowerModeParams scanInterval]
+ -[CBControllerLowPowerModeParams scanWindow]
+ -[CBControllerLowPowerModeParams setActionType:]
+ -[CBControllerLowPowerModeParams setConfigFlags:]
+ -[CBControllerLowPowerModeParams setDataBlob:]
+ -[CBControllerLowPowerModeParams setDataMask:]
+ -[CBControllerLowPowerModeParams setDeviceIDAdvScanCount:]
+ -[CBControllerLowPowerModeParams setDeviceIDDiagInfo:]
+ -[CBControllerLowPowerModeParams setDeviceIDDiagLength:]
+ -[CBControllerLowPowerModeParams setDeviceIDInfo:]
+ -[CBControllerLowPowerModeParams setDeviceIDInputKeyMaterial:]
+ -[CBControllerLowPowerModeParams setDeviceIDLength:]
+ -[CBControllerLowPowerModeParams setDeviceIDSalt:]
+ -[CBControllerLowPowerModeParams setDeviceIDTimestampEffectiveBits:]
+ -[CBControllerLowPowerModeParams setDeviceIDTimestampFrequency:]
+ -[CBControllerLowPowerModeParams setDeviceIDTimestampLsbsTruncated:]
+ -[CBControllerLowPowerModeParams setDiagnosticTxAdvBackoff:]
+ -[CBControllerLowPowerModeParams setDiagnosticTxAdvDuration:]
+ -[CBControllerLowPowerModeParams setDiagnosticTxAdvInterval:]
+ -[CBControllerLowPowerModeParams setGpioAssertionTime:]
+ -[CBControllerLowPowerModeParams setMacKeyDiagInfo:]
+ -[CBControllerLowPowerModeParams setMacKeyDiagLength:]
+ -[CBControllerLowPowerModeParams setMaxClockDriftSeconds:]
+ -[CBControllerLowPowerModeParams setNextScanDelay:]
+ -[CBControllerLowPowerModeParams setNumberOfDelayIterations:]
+ -[CBControllerLowPowerModeParams setPacketLength:]
+ -[CBControllerLowPowerModeParams setRssiThresholdValue:]
+ -[CBControllerLowPowerModeParams setScanDelayStart:]
+ -[CBControllerLowPowerModeParams setScanDuration:]
+ -[CBControllerLowPowerModeParams setScanInterval:]
+ -[CBControllerLowPowerModeParams setScanWindow:]
+ -[CBDevice _parseProximityPairingBattery1:]
+ -[CBDevice _parseProximityPairingBattery2:]
+ -[CBDevice _parseProximityPairingBattery3:]
+ -[CBDevice _parseProximityPairingColor1:]
+ -[CBDevice _parseProximityPairingMisc1:deviceFlags:]
+ -[CBDevice _parseProximityPairingPID2:]
+ -[CBDevice _parseProximityPairingStatus1:deviceFlags:]
+ -[CBDevice _parseProximityPairingStatus3:deviceFlags:]
+ -[CBDevice _parseSoftwareUpdatePtr:end:]
+ -[CBDevice aclLinkState]
+ -[CBDevice bleAdvertisementTimestampString].cold.1
+ -[CBDevice setAclLinkState:]
+ -[CBDevice setSoftwareUpdateActionType:]
+ -[CBDevice setSoftwareUpdateData:]
+ -[CBDevice softwareUpdateActionType]
+ -[CBDevice softwareUpdateData]
+ -[CBDevice updateWithSafetyAlertsSegments:error:].cold.1
+ -[CBDevice updateWithSafetyAlertsSegments:error:].cold.2
+ -[CBDevice xpcEventCompleteRepresentation]
+ -[CBDeviceSettings aclLinkState]
+ -[CBDeviceSettings setAclLinkState:]
+ -[CBDiscovery _xpcReceivedDeviceFound:].cold.1
+ -[CBDiscovery _xpcReceivedDeviceFound:].cold.2
+ -[CBDiscovery _xpcReceivedDeviceFound:].cold.3
+ -[CBDiscovery _xpcReceivedDeviceLost:].cold.1
+ -[CBDiscovery _xpcReceivedDeviceLost:].cold.2
+ -[CBDiscovery _xpcReceivedDeviceLost:].cold.3
+ -[CBDiscovery _xpcReceivedDevicesBuffered:].cold.1
+ -[CBDiscovery _xpcReceivedDevicesBuffered:].cold.2
+ -[CBDiscovery _xpcReceivedDevicesBuffered:].cold.3
+ -[CBDiscovery _xpcReceivedPowerStateChanged:].cold.1
+ -[CBDiscovery _xpcReceivedSystemOverrideChanged:].cold.1
+ -[CBDiscovery authFlags]
+ -[CBDiscovery setAuthFlags:]
+ -[CBDiscovery setSoftwareUpdatePayloads:]
+ -[CBDiscovery setXpcReportCompleteDevice:]
+ -[CBDiscovery softwareUpdatePayloads]
+ -[CBDiscovery xpcAuthFlagsCreateWithDeviceFlags:]
+ -[CBDiscovery xpcReportCompleteDevice]
+ -[CBHIDPerformanceMonitor _activateWithCompletion:].cold.1
+ -[CBHIDPerformanceMonitor _hidSetFeatureWithReportID:value:error:].cold.1
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.1
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.2
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.3
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.4
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.5
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.6
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.7
+ -[CBHIDPerformanceMonitor _hidStartAndReturnError:].cold.8
+ -[CBHIDPerformanceMonitor _invalidate].cold.1
+ -[CBHIDPerformanceMonitor _invalidated].cold.1
+ -[CBHIDPerformanceMonitor _testEnd].cold.1
+ -[CBHIDPerformanceMonitor _testEnded].cold.1
+ -[CBHIDPerformanceMonitor _testStart].cold.1
+ -[CBHIDPerformanceMonitor _testStart].cold.2
+ -[CBHIDPerformanceMonitor _testStart].cold.3
+ -[CBL2CAPChannel cid]
+ -[CBL2CAPChannel handleChannelClosed:]
+ -[CBL2CAPChannel handleDataReceived:]
+ -[CBL2CAPChannel initWithPeer:manager:info:]
+ -[CBL2CAPChannel initWithPeer:manager:info:].cold.1
+ -[CBL2CAPChannel initWithPeer:manager:info:].cold.2
+ -[CBL2CAPChannel initWithPeer:manager:info:].cold.3
+ -[CBL2CAPChannel initWithPeer:manager:info:].cold.4
+ -[CBL2CAPChannel isPacketBased]
+ -[CBL2CAPChannel managePendingData]
+ -[CBL2CAPChannel manager]
+ -[CBL2CAPChannel outgoingMTU]
+ -[CBL2CAPChannel readPacketsWithCompletionHandler:]
+ -[CBL2CAPChannel sendData:withCompletion:]
+ -[CBL2CAPChannel sendData:withCompletion:].cold.1
+ -[CBL2CAPChannel sendData:withCompletion:].cold.2
+ -[CBL2CAPChannel sendData:withCompletion:].cold.3
+ -[CBL2CAPChannel sendMsg:args:withReply:]
+ -[CBL2CAPChannel setCid:]
+ -[CBL2CAPChannel setIsPacketBased:]
+ -[CBL2CAPChannel setManager:]
+ -[CBL2CAPChannel setOutgoingMTU:]
+ -[CBManager closeL2CAPChannelForPeerUUID:withPsm:].cold.2
+ -[CBManager extractLocalDeviceStatesDictionary:].cold.2
+ -[CBManager performTCCCheck:].cold.1
+ -[CBManager performTCCCheck:].cold.2
+ -[CBManager performTCCCheck:].cold.3
+ -[CBManager performTCCCheck:].cold.4
+ -[CBManager performTCCCheck:].cold.5
+ -[CBManager retrieveSupportedResources:subKey:completion:].cold.1
+ -[CBManager retrieveSupportedResources:subKey:completion:].cold.2
+ -[CBManager retrieveSupportedResources:subKey:completion:].cold.3
+ -[CBManager sendMsg:args:].cold.2
+ -[CBManager sendMsg:args:].cold.3
+ -[CBManager sendMsg:args:withReply:].cold.2
+ -[CBManager triggerBTErrorReport:].cold.2
+ -[CBManager xpcConnectionDidReceiveMsg:args:].cold.1
+ -[CBMutableCharacteristic observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[CBMutableCharacteristic observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[CBMutableCharacteristic observeValueForKeyPath:ofObject:change:context:].cold.3
+ -[CBMutableCharacteristic observeValueForKeyPath:ofObject:change:context:].cold.4
+ -[CBMutableDescriptor initWithType:value:].cold.1
+ -[CBMutableDescriptor initWithType:value:].cold.2
+ -[CBMutableDescriptor initWithType:value:].cold.3
+ -[CBMutableDescriptor initWithType:value:].cold.4
+ -[CBPacketLoggerClient _activateXPC:completion:].cold.1
+ -[CBPacketLoggerClient _interrupted].cold.1
+ -[CBPacketLoggerClient _invalidated].cold.1
+ -[CBPacketLoggerClient _xpcReceivedEvent:].cold.1
+ -[CBPacketLoggerClient _xpcReceivedEvent:].cold.2
+ -[CBPacketLoggerClient _xpcReceivedPacket:].cold.1
+ -[CBPacketLoggerClient _xpcReceivedPacket:].cold.2
+ -[CBPairingAgent handlePairingMessage:args:].cold.2
+ -[CBPairingAgent pairPeer:options:].cold.1
+ -[CBPairingAgent pairPeer:useMITM:].cold.1
+ -[CBPairingAgent respondToPairingRequest:type:accept:data:].cold.1
+ -[CBPairingAgent unpairPeer:].cold.1
+ -[CBPeer handleMsg:args:].cold.2
+ -[CBPeripheral dealloc].cold.3
+ -[CBPeripheral dealloc].cold.4
+ -[CBPeripheral discoverCharacteristics:forService:].cold.3
+ -[CBPeripheral discoverCharacteristics:forService:].cold.4
+ -[CBPeripheral discoverCharacteristics:forService:].cold.5
+ -[CBPeripheral discoverDescriptorsForCharacteristic:].cold.3
+ -[CBPeripheral discoverDescriptorsForCharacteristic:].cold.4
+ -[CBPeripheral discoverDescriptorsForCharacteristic:].cold.5
+ -[CBPeripheral discoverIncludedServices:forService:].cold.3
+ -[CBPeripheral discoverIncludedServices:forService:].cold.4
+ -[CBPeripheral discoverIncludedServices:forService:].cold.5
+ -[CBPeripheral discoverServices:].cold.2
+ -[CBPeripheral handleL2CAPChannelDidReceiveData:]
+ -[CBPeripheral handleL2CAPChannelDidReceiveData:].cold.1
+ -[CBPeripheral handleL2CAPChannelOpened:].cold.3
+ -[CBPeripheral handleL2CAPChannelOpened:].cold.4
+ -[CBPeripheral handleMsg:args:].cold.2
+ -[CBPeripheral handleServicesChanged:].cold.2
+ -[CBPeripheral handleServicesDiscovered:].cold.1
+ -[CBPeripheral handleServicesDiscovered:].cold.2
+ -[CBPeripheral isConnectedToSystem].288
+ -[CBPeripheral l2capChannelForPeer:withCID:]
+ -[CBPeripheral l2capChannelForPeer:withCID:].cold.1
+ -[CBPeripheral l2capChannelForPeer:withCID:].cold.2
+ -[CBPeripheral l2capChannelForPeer:withPsm:].cold.2
+ -[CBPeripheral openL2CAPChannel:options:].cold.1
+ -[CBPeripheral openPacketL2CAPChannel:withIncomingMTU:options:]
+ -[CBPeripheral readRSSI].cold.2
+ -[CBPeripheral readValueForCharacteristic:].cold.3
+ -[CBPeripheral readValueForCharacteristic:].cold.4
+ -[CBPeripheral readValueForCharacteristic:].cold.5
+ -[CBPeripheral readValueForDescriptor:].cold.3
+ -[CBPeripheral readValueForDescriptor:].cold.4
+ -[CBPeripheral readValueForDescriptor:].cold.5
+ -[CBPeripheral sendMsg:requiresConnected:args:].cold.3
+ -[CBPeripheral sendMsg:requiresConnected:args:].cold.4
+ -[CBPeripheral setBroadcastValue:forCharacteristic:].cold.2
+ -[CBPeripheral setBroadcastValue:forCharacteristic:].cold.3
+ -[CBPeripheral setNotifyValue:forCharacteristic:].cold.2
+ -[CBPeripheral setNotifyValue:forCharacteristic:].cold.3
+ -[CBPeripheral setPeripheralName:].cold.1
+ -[CBPeripheral writeValue:forCharacteristic:type:].cold.3
+ -[CBPeripheral writeValue:forCharacteristic:type:].cold.4
+ -[CBPeripheral writeValue:forCharacteristic:type:].cold.5
+ -[CBPeripheral writeValue:forCharacteristic:type:].cold.6
+ -[CBPeripheral writeValue:forDescriptor:].cold.2
+ -[CBPeripheral writeValue:forDescriptor:].cold.3
+ -[CBPeripheral writeValue:forDescriptor:].cold.4
+ -[CBPeripheral writeValue:forDescriptor:].cold.5
+ -[CBPeripheralManager addService:].cold.1
+ -[CBPeripheralManager handleAdvertisingStarted:].cold.3
+ -[CBPeripheralManager handleAdvertisingStarted:].cold.4
+ -[CBPeripheralManager handleCSProcedureEventMsg:]
+ -[CBPeripheralManager handleCSProcedureEventMsg:].cold.1
+ -[CBPeripheralManager handleCSProcedureEventMsg:].cold.2
+ -[CBPeripheralManager handleCentralDidUpdateANCSAuthorization:].cold.2
+ -[CBPeripheralManager handleIncomingCISConnectionRequest:].cold.2
+ -[CBPeripheralManager handleL2CAPChannelDidReceiveData:]
+ -[CBPeripheralManager handleL2CAPChannelDidReceiveData:].cold.1
+ -[CBPeripheralManager handleL2CAPChannelOpened:].cold.4
+ -[CBPeripheralManager handleL2CAPChannelOpened:].cold.5
+ -[CBPeripheralManager handleL2CAPChannelOpened:].cold.6
+ -[CBPeripheralManager handleL2CAPChannelPublished:].cold.2
+ -[CBPeripheralManager handleL2CAPChannelUnpublished:].cold.2
+ -[CBPeripheralManager handleMsg:args:].cold.2
+ -[CBPeripheralManager handleRestoringState:].cold.1
+ -[CBPeripheralManager initWithDelegate:queue:options:].cold.2
+ -[CBPeripheralManager initWithDelegate:queue:options:].cold.3
+ -[CBPeripheralManager l2capChannelForPeer:withCID:]
+ -[CBPeripheralManager l2capChannelForPeer:withCID:].cold.1
+ -[CBPeripheralManager l2capChannelForPeer:withCID:].cold.2
+ -[CBPeripheralManager l2capChannelForPeer:withPsm:].cold.2
+ -[CBPeripheralManager overrideLocalLeAddress:].cold.2
+ -[CBPeripheralManager publishL2CAPChannel:requiresEncryption:options:].cold.2
+ -[CBPeripheralManager publishPacketL2CAPChannel:requiresEncryption:withIncomingMTU:options:]
+ -[CBPeripheralManager removeService:].cold.1
+ -[CBPeripheralManager respondToRequest:withResult:].cold.1
+ -[CBPeripheralManager setDesiredConnectionLatency:forCentral:].cold.1
+ -[CBPeripheralManager startAdvertising:].cold.12
+ -[CBPeripheralManager startAdvertising:].cold.13
+ -[CBPeripheralManager startAdvertising:].cold.14
+ -[CBPeripheralManager startAdvertising:].cold.15
+ -[CBPeripheralManager startAdvertising:].cold.16
+ -[CBPeripheralManager startAdvertising:].cold.17
+ -[CBPeripheralManager startAdvertising:].cold.18
+ -[CBPeripheralManager startAdvertising:].cold.19
+ -[CBPeripheralManager startAdvertising:].cold.20
+ -[CBPeripheralManager startAdvertising:].cold.21
+ -[CBPeripheralManager startAdvertising:].cold.22
+ -[CBPeripheralManager startAdvertisingForUsecase:withOptions:]
+ -[CBPeripheralManager supportsMultipleAdvertising].cold.2
+ -[CBPeripheralManager unpublishL2CAPChannel:].cold.2
+ -[CBPeripheralManager unpublishL2CAPChannel:].cold.3
+ -[CBPeripheralManager updateValue:forCharacteristic:onSubscribedCentrals:].cold.1
+ -[CBPeripheralManager updateValue:forCharacteristic:onSubscribedCentrals:].cold.2
+ -[CBRFCOMMChannel configureChannelPortParams:dataBits:parity:stopBits:].cold.1
+ -[CBRFCOMMChannel initWithPeer:info:].cold.3
+ -[CBRFCOMMChannel initWithPeer:info:].cold.4
+ -[CBScalablePipe initWithPipeManager:info:].cold.3
+ -[CBScalablePipe initWithPipeManager:info:].cold.4
+ -[CBScalablePipe initWithPipeManager:info:].cold.5
+ -[CBScalablePipe initWithPipeManager:info:].cold.6
+ -[CBScalablePipeManager handleMsg:args:].cold.3
+ -[CBScalablePipeManager handleMsg:args:].cold.4
+ -[CBScalablePipeManager pipeForName:identifier:].cold.2
+ -[CBScalablePipeManager registerEndpoint:type:priority:options:].cold.1
+ -[CBScalablePipeManager unregisterEndpoint:].cold.1
+ -[CBServer peripheralManager:didOpenL2CAPChannel:error:].cold.1
+ -[CBServer peripheralManager:didOpenL2CAPChannel:error:].cold.2
+ -[CBService handleCharacteristicsDiscovered:].cold.2
+ -[CBService handleCharacteristicsDiscovered:].cold.3
+ -[CBService handleIncludedServicesDiscovered:].cold.2
+ -[CBService handleIncludedServicesDiscovered:].cold.3
+ -[CBSoftwareUpdatePayloadInfo .cxx_destruct]
+ -[CBSoftwareUpdatePayloadInfo description]
+ -[CBSoftwareUpdatePayloadInfo encodeWithXPCObject:]
+ -[CBSoftwareUpdatePayloadInfo initWithXPCObject:error:]
+ -[CBSoftwareUpdatePayloadInfo setSoftwareUpdateActionType:]
+ -[CBSoftwareUpdatePayloadInfo setSoftwareUpdateDataBlob:]
+ -[CBSoftwareUpdatePayloadInfo setSoftwareUpdateDataMask:]
+ -[CBSoftwareUpdatePayloadInfo softwareUpdateActionType]
+ -[CBSoftwareUpdatePayloadInfo softwareUpdateDataBlob]
+ -[CBSoftwareUpdatePayloadInfo softwareUpdateDataMask]
+ -[CBSpatialInteractionDeviceTimestampInfo descriptionWithLevel:].cold.1
+ -[CBSpatialInteractionSession _xpcReceivedAOPData:].cold.1
+ -[CBSpatialInteractionSession _xpcReceivedAOPData:].cold.2
+ -[CBSpatialInteractionSession _xpcReceivedDeviceFound:].cold.1
+ -[CBSpatialInteractionSession _xpcReceivedDeviceFound:].cold.2
+ -[CBSpatialInteractionSession _xpcReceivedDeviceFound:].cold.3
+ -[CBSpatialInteractionSession _xpcReceivedDeviceFound:].cold.4
+ -[CBSpatialInteractionSession _xpcReceivedDeviceLost:].cold.1
+ -[CBSpatialInteractionSession _xpcReceivedDeviceLost:].cold.2
+ -[CBSpatialInteractionSession _xpcReceivedDeviceLost:].cold.3
+ -[CBSpatialInteractionSession _xpcReceivedDeviceLost:].cold.4
+ -[CBSpatialInteractionSession _xpcReceivedPowerStateChanged:].cold.1
+ -[CBSpatialInteractionSession _xpcReceivedSystemOverrideChanged:].cold.1
+ -[CBUUID description].cold.1
+ -[CBUserController _ensureXPCStarted].cold.1
+ -[CBUserController _interrupted].cold.1
+ -[CBUserController _invalidated].cold.1
+ -[CBUserController _invalidated].cold.2
+ -[CBXpcConnection _handleConnectionEvent:].cold.3
+ -[CBXpcConnection _handleConnectionEvent:].cold.4
+ -[CBXpcConnection _handleFinalized].cold.2
+ -[CBXpcConnection _handleInvalid].cold.2
+ -[CBXpcConnection _handleMsg:].cold.1
+ -[CBXpcConnection _handleReset].cold.2
+ -[CBXpcConnection _sendBarrier].cold.2
+ -[CBXpcConnection didReceiveForwardedDelegateCallbackMessage:].cold.2
+ -[CBXpcConnection didReceiveForwardedDelegateCallbackMessage:].cold.3
+ -[CBXpcConnection didReceiveForwardedMessage:].cold.2
+ -[CBXpcConnection didReceiveForwardedMessage:].cold.3
+ -[CBXpcConnection forwardWhbMsg:args:cnx:].cold.2
+ -[CBXpcConnection forwardWhbMsg:args:cnx:].cold.3
+ -[CBXpcConnection removeWhbRemoteId:].cold.1
+ -[CBXpcConnection sendMsg:args:].cold.1
+ -[CBXpcConnection sendMsgWithReply:args:replyBlock:].cold.1
+ -[CBXpcConnection sendSyncMsg:args:].cold.1
+ -[CBXpcConnection sendSyncMsg:args:].cold.2
+ -[CBXpcConnection sendSyncMsg:args:].cold.3
+ -[CBXpcConnection setWhbLocalId:forRemoteId:].cold.1
+ -[NSMutableData(CBLTVExtensions) appendCBLTVType:bytes:length:error:].cold.1
+ CBDiscoveryTypesBLEScan.cold.1
+ CBDiscoveryTypesBuffer.cold.1
+ CBDiscoveryTypesNearbyActionNoWake.cold.1
+ CBDiscoveryTypesNearbyActionV1.cold.1
+ CBDiscoveryTypesNearbyActionV2.cold.1
+ CBDiscoveryTypesNearbyInfoV2.cold.1
+ CBDiscoveryTypesNeedsAdvertisingAddress.cold.1
+ CBDiscoveryTypesNeedsIdentify.cold.1
+ CBDiscoveryTypesNeedsObjectLocator.cold.1
+ CBDiscoveryTypesProximityService.cold.1
+ CBDiscoveryTypesSoftwareUpdate.cold.1
+ CBXPCGetNextClientID.cold.1
+ CBXpcCreateNSObjectWithXpcObject.cold.3
+ CBXpcCreateNSObjectWithXpcObject.cold.4
+ GCC_except_table102
+ GCC_except_table108
+ GCC_except_table133
+ GCC_except_table148
+ GCC_except_table159
+ GCC_except_table41
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table72
+ GCC_except_table79
+ OBJC_IVAR_$_CBAdvertiser._advertisingSoftwareUpdateDataArrayCountMaximumLimit
+ OBJC_IVAR_$_CBAdvertiser._softwareUpdateActionType
+ OBJC_IVAR_$_CBAdvertiser._softwareUpdateDataArray
+ OBJC_IVAR_$_CBAdvertiser._softwareUpdateDataArrayCountMaximumLimit
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._actionType
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._configFlags
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._dataBlob
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._dataMask
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDAdvScanCount
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDDiagInfo
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDDiagLength
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDInfo
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDInputKeyMaterial
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDLength
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDSalt
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDTimestampEffectiveBits
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDTimestampFrequency
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._deviceIDTimestampLsbsTruncated
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._diagnosticTxAdvBackoff
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._diagnosticTxAdvDuration
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._diagnosticTxAdvInterval
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._gpioAssertionTime
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._macKeyDiagInfo
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._macKeyDiagLength
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._maxClockDriftSeconds
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._nextScanDelay
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._numberOfDelayIterations
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._packetLength
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._rssiThresholdValue
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._scanDelayStart
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._scanDuration
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._scanInterval
+ OBJC_IVAR_$_CBControllerLowPowerModeParams._scanWindow
+ OBJC_IVAR_$_CBDevice._softwareUpdateActionType
+ OBJC_IVAR_$_CBDevice._softwareUpdateData
+ OBJC_IVAR_$_CBDeviceSettings._aclLinkState
+ OBJC_IVAR_$_CBDiscovery._authFlags
+ OBJC_IVAR_$_CBDiscovery._softwareUpdatePayloads
+ OBJC_IVAR_$_CBDiscovery._xpcReportCompleteDevice
+ OBJC_IVAR_$_CBL2CAPChannel._cid
+ OBJC_IVAR_$_CBL2CAPChannel._isPacketBased
+ OBJC_IVAR_$_CBL2CAPChannel._manager
+ OBJC_IVAR_$_CBL2CAPChannel._outgoingMTU
+ OBJC_IVAR_$_CBL2CAPChannel.incomingPackets
+ OBJC_IVAR_$_CBL2CAPChannel.maxQueuePayloadSize
+ OBJC_IVAR_$_CBL2CAPChannel.pendingCompletionHandler
+ OBJC_IVAR_$_CBSoftwareUpdatePayloadInfo._softwareUpdateActionType
+ OBJC_IVAR_$_CBSoftwareUpdatePayloadInfo._softwareUpdateDataBlob
+ OBJC_IVAR_$_CBSoftwareUpdatePayloadInfo._softwareUpdateDataMask
+ _CBAssignedL2CAPPSMForDCT
+ _CBAssignedL2CAPPSMForSoftwareUpdate
+ _CBCSProcedureCounter
+ _CBCentralManagerScanOptionScanProcessedAtNsec
+ _CBCentralManagerScanOptionScanRequestedAtNsec
+ _CBDiscoveryTypesSoftwareUpdate
+ _CBManagerL2CAPChannelMaxIncomingPayloadSize
+ _CBOptionUseCaseOptions
+ _OBJC_CLASS_$_CBControllerLowPowerModeParams
+ _OBJC_CLASS_$_CBSoftwareUpdatePayloadInfo
+ _OBJC_METACLASS_$_CBControllerLowPowerModeParams
+ _OBJC_METACLASS_$_CBSoftwareUpdatePayloadInfo
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_9
+ __21-[CBDiscovery finish]_block_invoke.cold.1
+ __30-[CBUserController invalidate]_block_invoke.cold.1
+ __31-[CBManager createCnxWithInfo:]_block_invoke.59.cold.2
+ __31-[CBManager createCnxWithInfo:]_block_invoke.61.cold.2
+ __31-[CBManager createCnxWithInfo:]_block_invoke.cold.1
+ __34-[CBPacketLoggerClient invalidate]_block_invoke.cold.1
+ __35-[CBDiscovery _activateDirectStart]_block_invoke.176
+ __35-[CBDiscovery _activateDirectStart]_block_invoke.181
+ __37-[CBCentralManager orphanPeripherals]_block_invoke.cold.2
+ __37-[CBDiscovery _activateXPCCompleted:]_block_invoke.200
+ __37-[CBDiscovery _activateXPCCompleted:]_block_invoke.203
+ __38-[CBClassicManager orphanClassicPeers]_block_invoke.cold.2
+ __38-[CBHIDPerformanceMonitor _timerStart]_block_invoke.cold.1
+ __38-[CBXpcConnection setWhbReplyHandler:]_block_invoke.cold.2
+ __38-[CBXpcConnection setWhbReplyHandler:]_block_invoke.cold.3
+ __41-[CBController diagnosticLog:completion:]_block_invoke.cold.1
+ __41-[CBController diagnosticLog:completion:]_block_invoke_2.cold.1
+ __42-[CBController diagnosticShow:completion:]_block_invoke.cold.1
+ __42-[CBController diagnosticShow:completion:]_block_invoke_2.cold.1
+ __43-[CBDiscovery updateWithXPCSubscriberInfo:]_block_invoke.141
+ __44-[CBController getPowerStateWithCompletion:]_block_invoke_2.cold.1
+ __44-[CBController getPowerStateWithCompletion:]_block_invoke_2.cold.2
+ __44-[CBPeripheralManager handleRestoringState:]_block_invoke.250
+ __45-[CBController diagnosticControl:completion:]_block_invoke.cold.1
+ __45-[CBController diagnosticControl:completion:]_block_invoke_2.cold.1
+ __45-[CBHIDPerformanceMonitor _packetLoggerStart]_block_invoke.116.cold.1
+ __45-[CBHIDPerformanceMonitor _rssiAndHandleRead]_block_invoke.cold.1
+ __48-[CBController getControllerInfoWithCompletion:]_block_invoke_2.cold.1
+ __48-[CBPacketLoggerClient _activateXPC:completion:]_block_invoke.cold.1
+ __53-[CBController setLowPowerModeWithReason:completion:]_block_invoke.cold.1
+ __54-[CBController getDevicesWithFlags:completionHandler:]_block_invoke_2.cold.1
+ __55-[CBConnection pairingPerformAction:completionHandler:]_block_invoke.cold.1
+ __55-[CBController performDeviceRequest:device:completion:]_block_invoke_2.cold.1
+ __55-[CBManager retrieveBundle:sessionCountWithCompletion:]_block_invoke.cold.2
+ __58-[CBCentralManager connectWhbCBPeripheral:withCompletion:]_block_invoke.cold.1
+ __59-[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:]_block_invoke.187.cold.1
+ __59-[CBCentralManager activateWhbCnxForCBPeripheral:infoDict:]_block_invoke.cold.2
+ __59-[CBController getControllerSettingsWithCompletionHandler:]_block_invoke_2.cold.1
+ __60-[CBController setLowPowerModeWithParams:params:completion:]_block_invoke.cold.1
+ __67-[CBConnection pairingPerformAction:withOptions:completionHandler:]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_CBControllerLowPowerModeParams
+ __OBJC_$_INSTANCE_METHODS_CBSoftwareUpdatePayloadInfo
+ __OBJC_$_INSTANCE_VARIABLES_CBControllerLowPowerModeParams
+ __OBJC_$_INSTANCE_VARIABLES_CBSoftwareUpdatePayloadInfo
+ __OBJC_$_PROP_LIST_CBControllerLowPowerModeParams
+ __OBJC_$_PROP_LIST_CBSoftwareUpdatePayloadInfo
+ __OBJC_CLASS_PROTOCOLS_$_CBControllerLowPowerModeParams
+ __OBJC_CLASS_PROTOCOLS_$_CBSoftwareUpdatePayloadInfo
+ __OBJC_CLASS_RO_$_CBControllerLowPowerModeParams
+ __OBJC_CLASS_RO_$_CBSoftwareUpdatePayloadInfo
+ __OBJC_METACLASS_RO_$_CBControllerLowPowerModeParams
+ __OBJC_METACLASS_RO_$_CBSoftwareUpdatePayloadInfo
+ ___25-[CBL2CAPChannel dealloc]_block_invoke
+ ___28-[CBDiscovery setAuthFlags:]_block_invoke
+ ___33-[CBAdvertiser setAdvertiseRate:]_block_invoke
+ ___37-[CBL2CAPChannel handleDataReceived:]_block_invoke
+ ___41-[CBDiscovery setSoftwareUpdatePayloads:]_block_invoke
+ ___42-[CBL2CAPChannel sendData:withCompletion:]_block_invoke
+ ___43-[CBAdvertiser setSoftwareUpdateDataArray:]_block_invoke
+ ___44-[CBAdvertiser setSoftwareUpdateActionType:]_block_invoke
+ ___51-[CBL2CAPChannel readPacketsWithCompletionHandler:]_block_invoke
+ ___60-[CBController setLowPowerModeWithParams:params:completion:]_block_invoke
+ ___CBDiscoveryTypesSoftwareUpdate_block_invoke
+ __block_literal_global.221
+ __block_literal_global.231
+ __block_literal_global.258
+ __block_literal_global.260
+ __block_literal_global.262
+ __block_literal_global.264
+ __block_literal_global.266
+ __block_literal_global.268
+ __block_literal_global.270
+ __block_literal_global.272
+ __block_literal_global.274
+ __block_literal_global.276
+ __block_literal_global.408
+ __block_literal_global.426
+ __block_literal_global.761
+ _objc_msgSend$_parseProximityPairingBattery1:
+ _objc_msgSend$_parseProximityPairingBattery2:
+ _objc_msgSend$_parseProximityPairingBattery3:
+ _objc_msgSend$_parseProximityPairingColor1:
+ _objc_msgSend$_parseProximityPairingMisc1:deviceFlags:
+ _objc_msgSend$_parseProximityPairingPID2:
+ _objc_msgSend$_parseProximityPairingStatus1:deviceFlags:
+ _objc_msgSend$_parseProximityPairingStatus3:deviceFlags:
+ _objc_msgSend$_parseSoftwareUpdatePtr:end:
+ _objc_msgSend$aclLinkState
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$authFlags
+ _objc_msgSend$cid
+ _objc_msgSend$handleCSProcedureEventMsg:
+ _objc_msgSend$handleChannelClosed:
+ _objc_msgSend$handleDataReceived:
+ _objc_msgSend$handleL2CAPChannelDidReceiveData:
+ _objc_msgSend$initWithPeer:manager:info:
+ _objc_msgSend$l2capChannelForPeer:withCID:
+ _objc_msgSend$managePendingData
+ _objc_msgSend$peripheral:didCloseL2CAPChannel:
+ _objc_msgSend$peripheralManager:didChannelSoundingProcedureEvent:results:error:
+ _objc_msgSend$peripheralManager:didCloseL2CAPChannel:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$rssiThresholdValue
+ _objc_msgSend$scanInterval
+ _objc_msgSend$scanWindow
+ _objc_msgSend$setAclLinkState:
+ _objc_msgSend$setBlobData:
+ _objc_msgSend$setMaskData:
+ _objc_msgSend$softwareUpdateActionType
+ _objc_msgSend$softwareUpdateData
+ _objc_msgSend$softwareUpdateDataArray
+ _objc_msgSend$softwareUpdatePayloads
+ _objc_msgSend$startAdvertising:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$xpcAuthFlagsCreateWithDeviceFlags:
+ _xpc_dictionary_create_empty
+ convertToCBMsgId.cold.1
+ convertToWhbMsgId.cold.1
- -[CBAdvertiser safetyAlertsAlertIndex]
- -[CBAdvertiser setSafetyAlertsAlertIndex:]
- -[CBCentralManager HandleCSProcedureEventMsg:]
- -[CBDevice _parseStatusOne:deviceFlags:primaryPlacement:secondaryPlacement:]
- -[CBDevice safetyAlertsAlertIndex]
- -[CBL2CAPChannel initWithPeer:info:]
- -[CBL2CAPChannel initWithPeer:info:].cold.1
- -[CBL2CAPChannel initWithPeer:info:].cold.2
- -[CBPeripheral isConnectedToSystem].275
- GCC_except_table11
- GCC_except_table127
- GCC_except_table142
- GCC_except_table156
- GCC_except_table27
- GCC_except_table34
- GCC_except_table46
- GCC_except_table52
- GCC_except_table54
- GCC_except_table67
- GCC_except_table74
- GCC_except_table82
- GCC_except_table98
- OBJC_IVAR_$_CBAdvertiser._safetyAlertsAlertIndex
- OBJC_IVAR_$_CBDevice._safetyAlertsAlertIndex
- _CBManagerL2CAPChannelInMPS
- _CBManagerL2CAPChannelInMTU
- __35-[CBDiscovery _activateDirectStart]_block_invoke.154
- __35-[CBDiscovery _activateDirectStart]_block_invoke.159
- __37-[CBDiscovery _activateXPCCompleted:]_block_invoke.178
- __37-[CBDiscovery _activateXPCCompleted:]_block_invoke.181
- __43-[CBDiscovery updateWithXPCSubscriberInfo:]_block_invoke.129
- __44-[CBPeripheralManager handleRestoringState:]_block_invoke.238
- __block_literal_global.214
- __block_literal_global.224
- __block_literal_global.253
- __block_literal_global.255
- __block_literal_global.257
- __block_literal_global.259
- __block_literal_global.261
- __block_literal_global.263
- __block_literal_global.265
- __block_literal_global.267
- __block_literal_global.269
- __block_literal_global.393
- __block_literal_global.411
- __block_literal_global.720
- _objc_msgSend$_parseStatusOne:deviceFlags:primaryPlacement:secondaryPlacement:
- _objc_msgSend$setColorInfo:
CStrings:
+ "### Error writing usecase (%u) event %@"
+ ", %s %@"
+ ", SoftwareUpdatePayloads %@"
+ ", suA %d"
+ ", suD %@"
+ ", suD <%@>"
+ ", suDMs %d"
+ ", xpcReportCompleteDevice %s"
+ "-[CBController setLowPowerModeWithParams:params:completion:]"
+ "-[CBController setLowPowerModeWithParams:params:completion:]_block_invoke"
+ "-[CBDiscovery updateWithXPCSubscriberInfo:]"
+ "177D17F5F0764227B651B5ED28AD502E.chargingcase.fill"
+ "40262ECA475D4CCF9722443885EC78D8"
+ "ActionType: %s, Blob: %@, Mask: %@, Config: 0x%x, DelayStart: %d, ScanW: 0x%x, ScanI: 0x%x, ScanD: %d, NextScan: %d, ClockDrift: %u, RSSI: %d, GPIOAssertTime: %d, dIDSalt: %@, dIDTsFrq: %d, dIDEffectiveBits: %d, dIDTsLsbsTruncated: %d, dIDIKM: %@, dIDInfo: %@, dIDLen: %d, dIDAdvScanCnt: %d, diagTxAdvInt: %d, diagTxAdvDur: %d, diagTxAdvBackoff: %d, dIDDiagInfo: %@, dIDDiagLen: %d, macKeyDiagInfo: %@, macKeyDiagLen: %d"
+ "ActionType: %s, DataBlob: %@, DataMask: %@"
+ "Aliro"
+ "AppleIDSignInFamily"
+ "B24@0:8r^*16"
+ "B24@0:8r^{?=[6C]}16"
+ "B32@0:8r^*16^Q24"
+ "BTWake"
+ "BTWake: Bluetooth LPM Result :%@"
+ "BTWake: Invalid RSSI %d"
+ "BTWake: Invalid scan Interval %d"
+ "BTWake: Invalid scan Window %d"
+ "CBControllerLowPowerModeParams"
+ "CBDiscovery invalid serviceUUID: “%@”"
+ "CBL2CAPChannel.m"
+ "CBPeripheralManager: handleCSProcedureEventMsg for args %@"
+ "CBSoftwareUpdatePayloadInfo"
+ "Cannot find l2CAP channel closed with psm:%u cid:%u and result:%@"
+ "Cannot find l2CAP channel received Data with psm:%u cid:%u and result:%@"
+ "CriticalBattery"
+ "DCTProtocolDataAndTelephony"
+ "DCTProtocolTelephony"
+ "DiagTxAdv"
+ "Failed to send sendData xpc message, invalid manager set"
+ "Family"
+ "FindMyActionExtendedRange"
+ "FindMyActionExtendedRangeLE2M"
+ "FindMyActionExtendedRangeTransient"
+ "FindMyPlaySoundExtendedRange"
+ "Friend"
+ "HomeRepair"
+ "InviteHome"
+ "L2CAP - Error"
+ "L2CAP - Invalid packet size"
+ "MidiV2"
+ "No Params"
+ "No known channel matching peer %@ with cid %u"
+ "No peripheral found in handleCSProcedureEventMsg for args %@"
+ "OutboxControllerAuth"
+ "Power reason %s is not supported"
+ "SameAccount"
+ "SharedHome"
+ "SofrwareUpdateOutboxControllerAuth"
+ "SoftwareUpdate"
+ "SoftwareUpdateBTWake"
+ "SoftwareUpdateOutboxControllerAuth"
+ "SoftwareUpdatePayloads: %@ -> %@"
+ "SystemPaired"
+ "T@\"NSArray\",C,N,V_softwareUpdateDataArray"
+ "T@\"NSArray\",C,N,V_softwareUpdatePayloads"
+ "T@\"NSData\",C,N,V_dataBlob"
+ "T@\"NSData\",C,N,V_dataMask"
+ "T@\"NSData\",C,N,V_deviceIDDiagInfo"
+ "T@\"NSData\",C,N,V_deviceIDInfo"
+ "T@\"NSData\",C,N,V_deviceIDInputKeyMaterial"
+ "T@\"NSData\",C,N,V_deviceIDSalt"
+ "T@\"NSData\",C,N,V_macKeyDiagInfo"
+ "T@\"NSData\",C,N,V_softwareUpdateData"
+ "T@\"NSData\",C,N,V_softwareUpdateDataBlob"
+ "T@\"NSData\",C,N,V_softwareUpdateDataMask"
+ "TB,N,V_isPacketBased"
+ "TB,N,V_xpcReportCompleteDevice"
+ "TC,N,V_aclLinkState"
+ "TC,N,V_actionType"
+ "TC,N,V_deviceIDAdvScanCount"
+ "TC,N,V_deviceIDDiagLength"
+ "TC,N,V_deviceIDLength"
+ "TC,N,V_deviceIDTimestampEffectiveBits"
+ "TC,N,V_deviceIDTimestampFrequency"
+ "TC,N,V_deviceIDTimestampLsbsTruncated"
+ "TC,N,V_diagnosticTxAdvBackoff"
+ "TC,N,V_diagnosticTxAdvDuration"
+ "TC,N,V_macKeyDiagLength"
+ "TC,N,V_packetLength"
+ "TC,N,V_softwareUpdateActionType"
+ "TC,R,N,V_advertisingSoftwareUpdateDataArrayCountMaximumLimit"
+ "TC,R,N,V_softwareUpdateDataArrayCountMaximumLimit"
+ "TI,N,V_maxClockDriftSeconds"
+ "TQ,N,V_authFlags"
+ "TS,N,V_configFlags"
+ "TS,N,V_diagnosticTxAdvInterval"
+ "TS,N,V_gpioAssertionTime"
+ "TS,N,V_nextScanDelay"
+ "TS,N,V_numberOfDelayIterations"
+ "TS,N,V_scanDelayStart"
+ "TS,N,V_scanDuration"
+ "TS,N,V_scanInterval"
+ "TS,N,V_scanWindow"
+ "TS,V_cid"
+ "TS,V_outgoingMTU"
+ "T^{?=[6C]},R,N"
+ "Tc,N,V_rssiThresholdValue"
+ "UserShutDown"
+ "W"
+ "^{?=[6C]}16@0:8"
+ "_aclLinkState"
+ "_actionType"
+ "_advertisingSoftwareUpdateDataArrayCountMaximumLimit"
+ "_authFlags"
+ "_cid"
+ "_configFlags"
+ "_dataBlob"
+ "_dataMask"
+ "_deviceIDAdvScanCount"
+ "_deviceIDDiagInfo"
+ "_deviceIDDiagLength"
+ "_deviceIDInfo"
+ "_deviceIDInputKeyMaterial"
+ "_deviceIDLength"
+ "_deviceIDSalt"
+ "_deviceIDTimestampEffectiveBits"
+ "_deviceIDTimestampFrequency"
+ "_deviceIDTimestampLsbsTruncated"
+ "_diagnosticTxAdvBackoff"
+ "_diagnosticTxAdvDuration"
+ "_diagnosticTxAdvInterval"
+ "_gpioAssertionTime"
+ "_isPacketBased"
+ "_macKeyDiagInfo"
+ "_macKeyDiagLength"
+ "_maxClockDriftSeconds"
+ "_nextScanDelay"
+ "_numberOfDelayIterations"
+ "_outgoingMTU"
+ "_packetLength"
+ "_parseProximityPairingBattery1:"
+ "_parseProximityPairingBattery2:"
+ "_parseProximityPairingBattery3:"
+ "_parseProximityPairingColor1:"
+ "_parseProximityPairingMisc1:deviceFlags:"
+ "_parseProximityPairingPID2:"
+ "_parseProximityPairingStatus1:deviceFlags:"
+ "_parseProximityPairingStatus3:deviceFlags:"
+ "_parseSoftwareUpdatePtr:end:"
+ "_rssiThresholdValue"
+ "_scanDelayStart"
+ "_scanDuration"
+ "_scanInterval"
+ "_scanWindow"
+ "_softwareUpdateActionType"
+ "_softwareUpdateData"
+ "_softwareUpdateDataArray"
+ "_softwareUpdateDataArrayCountMaximumLimit"
+ "_softwareUpdateDataBlob"
+ "_softwareUpdateDataMask"
+ "_softwareUpdatePayloads"
+ "_xpcReportCompleteDevice"
+ "aLS"
+ "aSuda"
+ "aclLinkState"
+ "actionType"
+ "advertisingSoftwareUpdateDataArrayCountMaximumLimit"
+ "arrayByAddingObjectsFromArray:"
+ "auFl"
+ "authFlags"
+ "blb"
+ "bleSensorRssiIncreaseScanThreshold: %u -> %u"
+ "configFlags"
+ "createOfflineLEDevices:"
+ "ctND"
+ "ctcf"
+ "ctds"
+ "ctga"
+ "ctns"
+ "ctpl"
+ "ctri"
+ "ctsd"
+ "ctsi"
+ "ctsw"
+ "dIAS"
+ "dIDI"
+ "dIDL"
+ "dIEb"
+ "dIII"
+ "dIIk"
+ "dILT"
+ "dISt"
+ "dITf"
+ "dIdL"
+ "dataBlob"
+ "dataMask"
+ "deviceIDAdvScanCount"
+ "deviceIDDiagInfo"
+ "deviceIDDiagLength"
+ "deviceIDInfo"
+ "deviceIDInputKeyMaterial"
+ "deviceIDLength"
+ "deviceIDSalt"
+ "deviceIDTimestampEffectiveBits"
+ "deviceIDTimestampFrequency"
+ "deviceIDTimestampLsbsTruncated"
+ "diagnosticTxAdvBackoff"
+ "diagnosticTxAdvDuration"
+ "diagnosticTxAdvInterval"
+ "dtAB"
+ "dtAD"
+ "dtAI"
+ "gpioAssertionTime"
+ "handleCSProcedureEventMsg:"
+ "handleChannelClosed:"
+ "handleDataReceived:"
+ "handleL2CAPChannelDidReceiveData:"
+ "inParams %@"
+ "incomingPackets"
+ "initWithPeer:manager:info:"
+ "isPacketBased"
+ "kCBCSProcedureCounter"
+ "kCBL2CAPChannelMaxIncomingPayloadSize"
+ "kCBManagerRequiresPacketBasedLEL2CAPInterface"
+ "kCBMsgArgCID"
+ "kCBMsgArgDataLength"
+ "kCBMsgArgMaxQueuedPacketLength"
+ "kCBMsgArgOutMTU"
+ "kCBOptionUseCaseOptions"
+ "kCBScanOptionScanProcessedAtNsec"
+ "kCBScanOptionScanRequestedAtNsec"
+ "l2capChannelForPeer:withCID:"
+ "macKeyDiagInfo"
+ "macKeyDiagLength"
+ "managePendingData"
+ "maxClockDriftSeconds"
+ "maxQueuePayloadSize"
+ "mcds"
+ "mkDI"
+ "mkDL"
+ "msk"
+ "nextScanDelay"
+ "numberOfDelayIterations"
+ "openPacketL2CAPChannel:withIncomingMTU:options:"
+ "outgoingMTU"
+ "packetLength"
+ "pendingCompletionHandler"
+ "peripheral:didCloseL2CAPChannel:"
+ "peripheralManager:didChannelSoundingProcedureEvent:results:error:"
+ "peripheralManager:didCloseL2CAPChannel:"
+ "peripheralManager:l2CapChannel:didReceiveData:"
+ "publishPacketL2CAPChannel:requiresEncryption:withIncomingMTU:options:"
+ "readPacketsWithCompletionHandler:"
+ "reverseObjectEnumerator"
+ "rssiThresholdValue"
+ "scanDelayStart"
+ "scanDuration"
+ "scanInterval"
+ "scanWindow"
+ "sendData:withCompletion:"
+ "serviceUUIDsWithBlobMask"
+ "setAclLinkState:"
+ "setActionType:"
+ "setAuthFlags:"
+ "setCid:"
+ "setConfigFlags:"
+ "setDataBlob:"
+ "setDataMask:"
+ "setDeviceIDAdvScanCount:"
+ "setDeviceIDDiagInfo:"
+ "setDeviceIDDiagLength:"
+ "setDeviceIDInfo:"
+ "setDeviceIDInputKeyMaterial:"
+ "setDeviceIDLength:"
+ "setDeviceIDSalt:"
+ "setDeviceIDTimestampEffectiveBits:"
+ "setDeviceIDTimestampFrequency:"
+ "setDeviceIDTimestampLsbsTruncated:"
+ "setDiagnosticTxAdvBackoff:"
+ "setDiagnosticTxAdvDuration:"
+ "setDiagnosticTxAdvInterval:"
+ "setGpioAssertionTime:"
+ "setIsPacketBased:"
+ "setLowPowerModeWithParams:params:completion:"
+ "setMacKeyDiagInfo:"
+ "setMacKeyDiagLength:"
+ "setMaxClockDriftSeconds:"
+ "setNextScanDelay:"
+ "setNumberOfDelayIterations:"
+ "setOutgoingMTU:"
+ "setPacketLength:"
+ "setRssiThresholdValue:"
+ "setScanDelayStart:"
+ "setScanDuration:"
+ "setScanInterval:"
+ "setScanWindow:"
+ "setSoftwareUpdateActionType:"
+ "setSoftwareUpdateData:"
+ "setSoftwareUpdateDataArray:"
+ "setSoftwareUpdateDataBlob:"
+ "setSoftwareUpdateDataMask:"
+ "setSoftwareUpdatePayloads:"
+ "setXpcReportCompleteDevice:"
+ "softwareUpdateActionType"
+ "softwareUpdateData"
+ "softwareUpdateDataArray"
+ "softwareUpdateDataArrayCountMaximumLimit"
+ "softwareUpdateDataBlob"
+ "softwareUpdateDataMask"
+ "softwareUpdatePayloads"
+ "startAdvertisingForUsecase:withOptions:"
+ "suA"
+ "suA: %d -> %d"
+ "suD: %@ -> %@"
+ "suP"
+ "subarrayWithRange:"
+ "v28@0:8I16@20"
+ "v32@0:8S16S20@24"
+ "v36@0:8S16B20S24@28"
+ "xpcAuthFlagsCreateWithDeviceFlags:"
+ "xpcEventCompleteRepresentation"
+ "xpcReportCompleteDevice"
+ "{?=\"bitArray\"[6C]}"
+ "{?=\"didUpdateName\"b1\"didModifyServices\"b1\"didReadRSSI\"b1\"didUpdateRSSI\"b1\"didDiscoverServices\"b1\"didDiscoverIncludedServices\"b1\"didDiscoverCharacteristics\"b1\"didUpdateCharacteristicValue\"b1\"didWriteCharacteristicValue\"b1\"didNotifyCharacteristicValue\"b1\"didDiscoverDescriptors\"b1\"didUpdateDescriptorValue\"b1\"didWriteDescriptorValue\"b1\"didReceiveTimeSync\"b1\"didOpenL2CAPChannel\"b1\"didCloseL2CAPChannel\"b1}"
+ "{?=\"willRestoreState\"b1\"didAddService\"b1\"didReceiveReadRequest\"b1\"didReceiveWriteRequests\"b1\"centralDidSubscribeToCharacteristic\"b1\"centralDidUnsubscribeFromCharacteristic\"b1\"didStartAdvertising\"b1\"didStartPeriodicAdvertising\"b1\"didStopPeriodicAdvertising\"b1\"isReadyToUpdate\"b1\"centralDidConnect\"b1\"centralDidUpdateConnectionParameters\"b1\"didPublishL2CAPChannel\"b1\"didUnpublishL2CAPChannel\"b1\"didOpenL2CAPChannel\"b1\"didStopAdvertisingWithError\"b1\"didUpdateANCSAuthorization\"b1\"didUpdateControllerBTClock\"b1\"didUpdateControllerBTClockDict\"b1\"didRequestOfflineAdvPayloadRequestedWithReason\"b1\"didChannelSoundingProcedureEvent\"b1\"didCloseL2CAPChannel\"b1\"didReceiveL2CAPData\"b1}"
- "### Error writing usecase (%d) event %@"
- "B24@0:8r^{?=[5C]}16"
- "HandleCSProcedureEventMsg:"
- "No peripheral found in HandleCSProcedureEventMsg for args %@"
- "TC,N,V_safetyAlertsAlertIndex"
- "TC,R,N,V_safetyAlertsAlertIndex"
- "T^{?=[5C]},R,N"
- "^{?=[5C]}16@0:8"
- "_parseStatusOne:deviceFlags:primaryPlacement:secondaryPlacement:"
- "_safetyAlertsAlertIndex"
- "kCBL2CAPChannelInMPS"
- "kCBL2CAPChannelInMTU"
- "kCBOptionUsecase"
- "l2CAP channel closed with psm : %u and result : %@"
- "safetyAlertsAlertIndex"
- "setSafetyAlertsAlertIndex:"
- "v44@0:8C16^Q20^i28^i36"
- "{?=\"bitArray\"[5C]}"
- "{?=\"didUpdateName\"b1\"didModifyServices\"b1\"didReadRSSI\"b1\"didUpdateRSSI\"b1\"didDiscoverServices\"b1\"didDiscoverIncludedServices\"b1\"didDiscoverCharacteristics\"b1\"didUpdateCharacteristicValue\"b1\"didWriteCharacteristicValue\"b1\"didNotifyCharacteristicValue\"b1\"didDiscoverDescriptors\"b1\"didUpdateDescriptorValue\"b1\"didWriteDescriptorValue\"b1\"didReceiveTimeSync\"b1\"didOpenL2CAPChannel\"b1}"
- "{?=\"willRestoreState\"b1\"didAddService\"b1\"didReceiveReadRequest\"b1\"didReceiveWriteRequests\"b1\"centralDidSubscribeToCharacteristic\"b1\"centralDidUnsubscribeFromCharacteristic\"b1\"didStartAdvertising\"b1\"didStartPeriodicAdvertising\"b1\"didStopPeriodicAdvertising\"b1\"isReadyToUpdate\"b1\"centralDidConnect\"b1\"centralDidUpdateConnectionParameters\"b1\"didPublishL2CAPChannel\"b1\"didUnpublishL2CAPChannel\"b1\"didOpenL2CAPChannel\"b1\"didStopAdvertisingWithError\"b1\"didUpdateANCSAuthorization\"b1\"didUpdateControllerBTClock\"b1\"didUpdateControllerBTClockDict\"b1\"didRequestOfflineAdvPayloadRequestedWithReason\"b1}"

```
