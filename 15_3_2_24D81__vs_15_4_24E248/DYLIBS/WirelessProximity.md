## WirelessProximity

> `/System/Library/PrivateFrameworks/WirelessProximity.framework/Versions/A/WirelessProximity`

```diff

-183.9.1.0.1
-  __TEXT.__text: 0x35840
+184.42.0.3.0
+  __TEXT.__text: 0x367c8
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x2414
+  __TEXT.__objc_methlist: 0x2964
   __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x32bf
+  __TEXT.__cstring: 0x33b1
   __TEXT.__oslogstring: 0x4661
-  __TEXT.__gcc_except_tab: 0x718
-  __TEXT.__unwind_info: 0xfc8
+  __TEXT.__gcc_except_tab: 0x708
+  __TEXT.__unwind_info: 0x14c0
   __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methname: 0x5185
+  __TEXT.__objc_methname: 0x51f6
   __TEXT.__objc_methtype: 0xe01
-  __TEXT.__objc_stubs: 0x42a0
+  __TEXT.__objc_stubs: 0x4320
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e0
+  __DATA_CONST.__objc_selrefs: 0x1590
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb8
   __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__const: 0x3b50
-  __AUTH_CONST.__cfstring: 0x2ae0
-  __AUTH_CONST.__objc_const: 0x35c0
+  __AUTH_CONST.__cfstring: 0x2b00
+  __AUTH_CONST.__objc_const: 0x2c00
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1c4
+  __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x2a8
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x410

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9F691E1-8D66-3F3A-B79B-F2008587085E
-  Functions: 1488
-  Symbols:   3145
-  CStrings:  2273
+  UUID: 68F8C3FF-41B9-3C19-8002-988E2D1B3002
+  Functions: 1891
+  Symbols:   3557
+  CStrings:  2289
 
Symbols:
+ +[WPAWDL generateDataFromEmails:].cold.1
+ +[WPAWDL hashEmail:].cold.1
+ +[WPClient initialize].cold.2
+ +[WPClient supportsRanging].cold.1
+ +[WPDObjectDiscoveryData applyMaskToAddress:].cold.2
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.10
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.11
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.12
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.13
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.7
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.8
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.9
+ -[WPAWDL deviceDiscovered:].cold.2
+ -[WPAWDL initWithDelegate:queue:machName:].cold.3
+ -[WPAWDL initWithDelegate:queue:machName:].cold.4
+ -[WPAWDL startConnectionlessAWDLServiceAdvertisingWithData:].cold.2
+ -[WPAWDL startConnectionlessAWDLServiceAdvertisingWithData:].cold.3
+ -[WPAWDL updateAdvertisingRequest:withUpdate:].cold.1
+ -[WPAdvertising advertisingStoppedOfType:withError:].cold.2
+ -[WPAdvertising deregisterService:].cold.2
+ -[WPAdvertising parseCompanyData:].cold.2
+ -[WPAdvertising registerService:].cold.2
+ -[WPClient connectToPeer:withOptions:].cold.2
+ -[WPClient dealloc].cold.1
+ -[WPClient initWithQueue:machName:].cold.1
+ -[WPClient initWithQueue:machName:].cold.2
+ -[WPClient initWithQueue:machName:].cold.3
+ -[WPClient listener:shouldAcceptNewConnection:].cold.1
+ -[WPClient notifyNotApprovedUseCase:].cold.2
+ -[WPClient receivedTestResponse:].cold.2
+ -[WPClient registeredWithDaemonAndContinuingSession:].cold.1
+ -[WPClient sendDataToCharacteristic:inService:forPeer:].cold.1
+ -[WPClient setupMachXPCService].cold.1
+ -[WPClient startAdvertising:].cold.4
+ -[WPClient startAdvertising:].cold.5
+ -[WPClient startAdvertising:].cold.6
+ -[WPClient startTrackingPeerWithRequest:].cold.2
+ -[WPClient stateDidChange:].cold.1
+ -[WPClient stateDidChange:].cold.2
+ -[WPClient stateDidChange:].cold.3
+ -[WPClient stateDidChange:].cold.4
+ -[WPClient stateDidChange:].cold.5
+ -[WPClient stopTrackingPeerWithRequest:].cold.3
+ -[WPClient stopTrackingPeerWithRequest:].cold.4
+ -[WPClient updateAdvertisingRequest:withUpdate:].cold.3
+ -[WPClient updateAdvertisingRequest:withUpdate:].cold.4
+ -[WPClient updateScanningRequest:withUpdate:].cold.3
+ -[WPClient updateScanningRequest:withUpdate:].cold.4
+ -[WPContinuity advertisingFailedToStart:ofType:].cold.2
+ -[WPContinuity advertisingPendingOfType:].cold.1
+ -[WPContinuity advertisingStartedOfType:].cold.2
+ -[WPContinuity advertisingStoppedOfType:withError:].cold.1
+ -[WPContinuity advertisingStoppedOfType:withError:].cold.2
+ -[WPContinuity central:subscribed:toCharacteristic:inService:].cold.2
+ -[WPContinuity central:subscribed:toCharacteristic:inService:].cold.3
+ -[WPContinuity central:subscribed:toCharacteristic:inService:].cold.4
+ -[WPContinuity connectToPeer:].cold.3
+ -[WPContinuity connectToPeer:].cold.4
+ -[WPContinuity connectToPeer:].cold.5
+ -[WPContinuity connectedDevice:withError:shouldDiscover:].cold.1
+ -[WPContinuity connectedDevice:withError:shouldDiscover:].cold.2
+ -[WPContinuity connectedDeviceOverLEPipe:].cold.1
+ -[WPContinuity deviceDiscovered:].cold.2
+ -[WPContinuity disconnectFromPeer:].cold.2
+ -[WPContinuity disconnectFromPeer:].cold.3
+ -[WPContinuity disconnectedDevice:withError:].cold.1
+ -[WPContinuity disconnectedDevice:withError:].cold.2
+ -[WPContinuity disconnectedDeviceOverLEPipe:withError:].cold.1
+ -[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:].cold.3
+ -[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:].cold.4
+ -[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:].cold.5
+ -[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:].cold.6
+ -[WPContinuity failedToStartTrackingPeer:error:].cold.1
+ -[WPContinuity initWithDelegate:queue:].cold.2
+ -[WPContinuity initWithDelegate:queue:].cold.3
+ -[WPContinuity invalidate].cold.1
+ -[WPContinuity peerTrackingFull].cold.1
+ -[WPContinuity receivedData:forCharacteristic:inService:forPeripheral:].cold.1
+ -[WPContinuity receivedData:forCharacteristic:inService:forPeripheral:].cold.2
+ -[WPContinuity receivedData:fromEndpoint:forPeripheral:].cold.1
+ -[WPContinuity scanningFailedToStart:ofType:].cold.2
+ -[WPContinuity sendData:toPeer:].cold.4
+ -[WPContinuity sendData:toPeer:].cold.5
+ -[WPContinuity sendData:toPeer:].cold.6
+ -[WPContinuity sendData:toPeer:].cold.7
+ -[WPContinuity sendData:toPeer:].cold.8
+ -[WPContinuity sentData:forCharacteristic:inService:forPeripheral:withError:].cold.1
+ -[WPContinuity sentData:forCharacteristic:inService:forPeripheral:withError:].cold.2
+ -[WPContinuity sentData:toEndpoint:forPeripheral:withError:].cold.1
+ -[WPContinuity startAdvertisingOfType:withData:].cold.1
+ -[WPContinuity startScanningForType:withData:mask:peers:boostedScan:duplicates:].cold.2
+ -[WPContinuity startScanningForType:withData:mask:peers:boostedScan:duplicates:].cold.3
+ -[WPContinuity startTrackingPeer:forType:].cold.2
+ -[WPContinuity stateDidChange:].cold.1
+ -[WPContinuity stopAdvertisingOfType:].cold.1
+ -[WPContinuity stopScanningForType:].cold.1
+ -[WPContinuity stopTrackingPeer:forType:].cold.2
+ -[WPContinuity updateAdvertisingRequest:withUpdate:].cold.1
+ -[WPContinuity updateScanningRequest:withUpdate:].cold.1
+ -[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.3
+ -[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.4
+ -[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.5
+ -[WPDataTransfer addNewData:].cold.10
+ -[WPDataTransfer addNewData:].cold.5
+ -[WPDataTransfer addNewData:].cold.6
+ -[WPDataTransfer addNewData:].cold.7
+ -[WPDataTransfer addNewData:].cold.8
+ -[WPDataTransfer addNewData:].cold.9
+ -[WPDeviceScanner anyDiscoveredDevice:].cold.3
+ -[WPDeviceScanner anyDiscoveredDevice:].cold.4
+ -[WPDeviceScanner deviceDiscovered:].cold.3
+ -[WPDeviceScanner deviceDiscovered:].cold.4
+ -[WPDeviceScanner parseCompanyData:forSize:intoDictionary:].cold.2
+ -[WPDeviceScanner parseCompanyData:forSize:intoDictionary:].cold.3
+ -[WPDeviceScanner registerForAnyScanResults:].cold.1
+ -[WPHeySiri advertisingStartedOfType:].cold.1
+ -[WPHeySiri advertisingStartedOfTypeAt:].cold.1
+ -[WPHeySiri advertisingStoppedOfType:withError:].cold.1
+ -[WPHeySiri deviceDiscovered:].cold.3
+ -[WPHeySiri deviceDiscovered:].cold.4
+ -[WPHeySiri initWithDelegate:queue:].cold.1
+ -[WPHeySiri scanningStartedOfType:].cold.1
+ -[WPHeySiri scanningStoppedOfType:].cold.1
+ -[WPHeySiri startAdvertisingWithData:].cold.1
+ -[WPHeySiri startScanningAndAdvertisingWithData:].cold.1
+ -[WPHeySiri startScanning].cold.1
+ -[WPHeySiri startScanning].cold.2
+ -[WPHeySiri stopAdvertising].cold.1
+ -[WPHeySiri stopScanningAndAdvertising].cold.1
+ -[WPHeySiri stopScanning].cold.1
+ -[WPHeySiri updateAdvertisingRequest:withUpdate:].cold.3
+ -[WPHeySiri updateAdvertisingRequest:withUpdate:].cold.4
+ -[WPHeySiri updateScanningRequest:withUpdate:].cold.3
+ -[WPHeySiri updateScanningRequest:withUpdate:].cold.4
+ -[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:].cold.4
+ -[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:].cold.5
+ -[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:].cold.6
+ -[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:].cold.7
+ -[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:].cold.8
+ -[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:].cold.9
+ -[WPHomeKit deviceFoundHandler:cached:].cold.2
+ -[WPHomeKit deviceLostHandler:].cold.2
+ -[WPHomeKit startCBDiscoveryScan:forType:].cold.1
+ -[WPHomeKit startScanningWithData:forType:].cold.2
+ -[WPHomeKit startScanningWithData:forType:].cold.3
+ -[WPHomeKit startScanningWithData:forType:].cold.4
+ -[WPHomeKit startScanningWithData:forType:].cold.5
+ -[WPHomeKit stopScanningForType:].cold.1
+ -[WPHomeKit stopScanningForType:].cold.2
+ -[WPHomeKit stopScanningForType:].cold.3
+ -[WPMagicSwitch advertisingStoppedOfType:withError:].cold.1
+ -[WPMagicSwitch advertisingStoppedOfType:withError:].cold.2
+ -[WPNearby advertisingFailedToStart:ofType:].cold.2
+ -[WPNearby advertisingPendingOfType:].cold.1
+ -[WPNearby advertisingStartedOfType:].cold.2
+ -[WPNearby advertisingStoppedOfType:withError:].cold.1
+ -[WPNearby advertisingStoppedOfType:withError:].cold.2
+ -[WPNearby central:subscribed:toCharacteristic:inService:].cold.2
+ -[WPNearby central:subscribed:toCharacteristic:inService:].cold.3
+ -[WPNearby central:subscribed:toCharacteristic:inService:].cold.4
+ -[WPNearby clearDuplicatesForType:].cold.1
+ -[WPNearby connectToPeer:withOptions:].cold.3
+ -[WPNearby connectToPeer:withOptions:].cold.4
+ -[WPNearby connectToPeer:withOptions:].cold.5
+ -[WPNearby connectedDevice:withError:shouldDiscover:].cold.1
+ -[WPNearby connectedDevice:withError:shouldDiscover:].cold.2
+ -[WPNearby connectedDeviceOverLEPipe:].cold.1
+ -[WPNearby deviceDiscovered:].cold.2
+ -[WPNearby deviceDiscovered:].cold.3
+ -[WPNearby deviceDiscovered:].cold.4
+ -[WPNearby disconnectFromPeer:].cold.2
+ -[WPNearby disconnectFromPeer:].cold.3
+ -[WPNearby disconnectedDevice:withError:].cold.1
+ -[WPNearby disconnectedDevice:withError:].cold.2
+ -[WPNearby disconnectedDeviceOverLEPipe:withError:].cold.1
+ -[WPNearby discoveredCharacteristicsAndServices:forPeripheral:].cold.3
+ -[WPNearby discoveredCharacteristicsAndServices:forPeripheral:].cold.4
+ -[WPNearby discoveredCharacteristicsAndServices:forPeripheral:].cold.5
+ -[WPNearby discoveredCharacteristicsAndServices:forPeripheral:].cold.6
+ -[WPNearby failedToStartTrackingPeer:error:].cold.2
+ -[WPNearby initWithDelegate:queue:].cold.1
+ -[WPNearby invalidate].cold.1
+ -[WPNearby receivedData:forCharacteristic:inService:forPeripheral:].cold.2
+ -[WPNearby receivedData:forCharacteristic:inService:forPeripheral:].cold.3
+ -[WPNearby scanningFailedToStart:ofType:].cold.2
+ -[WPNearby sendData:toPeer:].cold.5
+ -[WPNearby sendData:toPeer:].cold.6
+ -[WPNearby sendData:toPeer:].cold.7
+ -[WPNearby sendData:toPeer:].cold.8
+ -[WPNearby sentData:forCharacteristic:inService:forPeripheral:withError:].cold.1
+ -[WPNearby sentData:forCharacteristic:inService:forPeripheral:withError:].cold.2
+ -[WPNearby sentData:toEndpoint:forPeripheral:withError:].cold.1
+ -[WPNearby sentData:toEndpoint:forPeripheral:withError:].cold.2
+ -[WPNearby startAdvertisingOfType:data:priority:mode:options:].cold.2
+ -[WPNearby startAdvertisingOfType:data:priority:mode:options:].cold.3
+ -[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:].cold.2
+ -[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:].cold.3
+ -[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:].cold.4
+ -[WPNearby startTrackingPeer:forType:].cold.2
+ -[WPNearby stateDidChange:].cold.1
+ -[WPNearby stopAdvertisingOfType:].cold.1
+ -[WPNearby stopScanningForType:].cold.1
+ -[WPNearby stopTrackingPeer:forType:].cold.2
+ -[WPNearby updateAdvertisingRequest:withUpdate:].cold.1
+ -[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.3
+ -[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.4
+ -[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.5
+ -[WPObjectDiscovery devicesDiscovered:].cold.2
+ -[WPObjectDiscovery initWithDelegate:queue:].cold.2
+ -[WPObjectDiscovery initWithDelegate:queue:].cold.3
+ -[WPObjectDiscovery invalidate].cold.1
+ -[WPObjectDiscovery isValidScanOptions:].cold.2
+ -[WPObjectDiscovery isValidScanRequest:].cold.2
+ -[WPObjectDiscovery scanRequestFromScanMode:UpdateTime:].cold.2
+ -[WPObjectDiscovery scanningFailedToStart:ofType:].cold.2
+ -[WPObjectDiscovery scanningFailedWithError:].cold.2
+ -[WPObjectDiscovery scanningStartedOfType:].cold.2
+ -[WPObjectDiscovery scanningStoppedOfType:].cold.2
+ -[WPObjectDiscovery startScanningWithMode:Timeout:].cold.2
+ -[WPObjectDiscovery startScanningWithMode:Timeout:].cold.3
+ -[WPObjectDiscovery startScanningWithMode:].cold.2
+ -[WPObjectDiscovery startScanningWithOptions:].cold.1
+ -[WPObjectDiscovery startScanningWithOptions:].cold.2
+ -[WPObjectDiscovery startScanning].cold.2
+ -[WPObjectDiscovery stateDidChange:].cold.2
+ -[WPObjectDiscovery stopScanning].cold.1
+ -[WPObjectDiscovery updateScanningRequest:withUpdate:].cold.1
+ -[WPObjectDiscovery(Test) receivedTestResponse:].cold.2
+ -[WPObjectDiscovery(Test) startTest].cold.2
+ -[WPObjectDiscovery(Test) stopTest].cold.2
+ -[WPObjectDiscovery(Test) updateBeaconingExtended:].cold.2
+ -[WPObjectDiscovery(Test) updateBeaconingInterval:].cold.2
+ -[WPObjectDiscovery(Test) updateBeaconingKeys:].cold.2
+ -[WPObjectDiscovery(Test) updateBeaconingState:].cold.2
+ -[WPObjectDiscovery(Test) updateBeaconingStatus:].cold.2
+ -[WPObjectDiscovery(Test) updateNearOwnerTokens:].cold.2
+ -[WPPairing clearProximityPairingServiceDuplicates].cold.1
+ -[WPPairing deviceDiscovered:].cold.2
+ -[WPPairing ignoreDeviceUntilNextUnlock:ignoreDevice:].cold.2
+ -[WPPairing initWithDelegate:queue:machName:].cold.3
+ -[WPPairing initWithDelegate:queue:machName:].cold.4
+ -[WPPairing startProximityPairingServiceScanningWithRSSI:duplicates:scanMode:].cold.1
+ -[WPPairing stopProximityPairingServiceScanning].cold.1
+ -[WPRanging enableRanging:].cold.1
+ -[WPRanging enableRanging:reply:].cold.1
+ -[WPRanging initWithDelegate:queue:].cold.2
+ -[WPRanging isRangingEnabledReply:].cold.1
+ -[WPScanRequest requestedAtNsec]
+ -[WPScanRequest setRequestedAtNsec:]
+ -[WPTest advertisingFailedToStart:ofType:].cold.2
+ -[WPTest advertisingPendingOfType:].cold.1
+ -[WPTest advertisingStartedOfType:].cold.2
+ -[WPTest advertisingStoppedOfType:withError:].cold.2
+ -[WPTest advertisingStoppedOfType:withError:].cold.3
+ -[WPTest advertisingStoppedOfType:withError:].cold.4
+ -[WPTest central:subscribed:toCharacteristic:inService:].cold.2
+ -[WPTest central:subscribed:toCharacteristic:inService:].cold.3
+ -[WPTest central:subscribed:toCharacteristic:inService:].cold.4
+ -[WPTest connectToPeer:withOptions:].cold.3
+ -[WPTest connectToPeer:withOptions:].cold.4
+ -[WPTest connectToPeer:withOptions:].cold.5
+ -[WPTest connectedDevice:withError:shouldDiscover:].cold.1
+ -[WPTest connectedDevice:withError:shouldDiscover:].cold.2
+ -[WPTest connectedDeviceOverLEPipe:].cold.1
+ -[WPTest deviceDiscovered:].cold.2
+ -[WPTest disconnectFromPeer:].cold.2
+ -[WPTest disconnectFromPeer:].cold.3
+ -[WPTest disconnectedDevice:withError:].cold.1
+ -[WPTest disconnectedDevice:withError:].cold.2
+ -[WPTest disconnectedDeviceOverLEPipe:withError:].cold.1
+ -[WPTest initWithDelegate:queue:].cold.1
+ -[WPTest invalidate].cold.1
+ -[WPTest receivedData:forCharacteristic:inService:forPeripheral:].cold.2
+ -[WPTest receivedData:forCharacteristic:inService:forPeripheral:].cold.3
+ -[WPTest scanningFailedToStart:ofType:].cold.2
+ -[WPTest scanningStartedOfType:].cold.2
+ -[WPTest scanningStoppedOfType:].cold.2
+ -[WPTest sendData:toPeer:].cold.5
+ -[WPTest sendData:toPeer:].cold.6
+ -[WPTest sendData:toPeer:].cold.7
+ -[WPTest sendData:toPeer:].cold.8
+ -[WPTest sentData:toEndpoint:forPeripheral:withError:].cold.1
+ -[WPTest sentData:toEndpoint:forPeripheral:withError:].cold.2
+ -[WPTest startAdvertisingOfType:data:priority:mode:options:].cold.2
+ -[WPTest startAdvertisingOfType:data:priority:mode:options:].cold.3
+ -[WPTest startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:].cold.2
+ -[WPTest startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:].cold.3
+ -[WPTest stopAdvertisingOfType:].cold.1
+ -[WPTest stopScanningForType:].cold.1
+ -[WPTransfer advertisingFailedToStart:ofType:].cold.2
+ -[WPTransfer central:subscribed:toCharacteristic:inService:].cold.3
+ -[WPTransfer central:subscribed:toCharacteristic:inService:].cold.4
+ -[WPTransfer central:subscribed:toCharacteristic:inService:].cold.5
+ -[WPTransfer central:subscribed:toCharacteristic:inService:].cold.6
+ -[WPTransfer central:subscribed:toCharacteristic:inService:].cold.7
+ -[WPTransfer central:subscribed:toCharacteristic:inService:].cold.8
+ -[WPTransfer central:subscribed:toCharacteristic:inService:].cold.9
+ -[WPTransfer connectedDevice:withError:shouldDiscover:].cold.2
+ -[WPTransfer connectedDevice:withError:shouldDiscover:].cold.3
+ -[WPTransfer connectedDevice:withError:shouldDiscover:].cold.4
+ -[WPTransfer dealloc].cold.1
+ -[WPTransfer deviceDiscovered:].cold.10
+ -[WPTransfer deviceDiscovered:].cold.11
+ -[WPTransfer deviceDiscovered:].cold.12
+ -[WPTransfer deviceDiscovered:].cold.13
+ -[WPTransfer deviceDiscovered:].cold.6
+ -[WPTransfer deviceDiscovered:].cold.7
+ -[WPTransfer deviceDiscovered:].cold.8
+ -[WPTransfer deviceDiscovered:].cold.9
+ -[WPTransfer disconnectedDevice:withError:].cold.1
+ -[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:].cold.4
+ -[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:].cold.5
+ -[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:].cold.6
+ -[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:].cold.7
+ -[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:].cold.8
+ -[WPTransfer ignoreDevice].cold.1
+ -[WPTransfer initWithDelegate:queue:machName:options:].cold.1
+ -[WPTransfer invalidate].cold.1
+ -[WPTransfer receivedData:].cold.10
+ -[WPTransfer receivedData:].cold.11
+ -[WPTransfer receivedData:].cold.12
+ -[WPTransfer receivedData:].cold.13
+ -[WPTransfer receivedData:].cold.14
+ -[WPTransfer receivedData:].cold.7
+ -[WPTransfer receivedData:].cold.8
+ -[WPTransfer receivedData:].cold.9
+ -[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:].cold.10
+ -[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:].cold.4
+ -[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:].cold.5
+ -[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:].cold.6
+ -[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:].cold.7
+ -[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:].cold.8
+ -[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:].cold.9
+ -[WPTransfer scanningFailedToStart:ofType:].cold.2
+ -[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:].cold.3
+ -[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:].cold.4
+ -[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:].cold.5
+ -[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:].cold.6
+ -[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:].cold.7
+ -[WPTransfer startAdvertising].cold.3
+ -[WPTransfer startAdvertising].cold.4
+ -[WPTransfer startAdvertising].cold.5
+ -[WPTransfer startScan].cold.3
+ -[WPTransfer startScan].cold.4
+ -[WPTransfer startScan].cold.5
+ -[WPTransfer stopAdvertising].cold.1
+ -[WPTransfer stopScan].cold.1
+ -[WPTransfer transferFailed:].cold.2
+ -[WPTransfer updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.1
+ -[WPZoneTracker enteredZone:manufacturerData:].cold.2
+ -[WPZoneTracker enteredZone:manufacturerData:].cold.3
+ -[WPZoneTracker enteredZone:manufacturerData:].cold.4
+ GCC_except_table161
+ OBJC_IVAR_$_WPScanRequest._requestedAtNsec
+ WPLoggingInit.cold.1
+ __22-[WPClient connection]_block_invoke.178
+ __22-[WPClient connection]_block_invoke.178.cold.1
+ __22-[WPClient connection]_block_invoke.182
+ __22-[WPClient connection]_block_invoke.cold.1
+ __22-[WPClient connection]_block_invoke_2.179
+ __23-[WPClient addServices]_block_invoke.404
+ __23-[WPClient addServices]_block_invoke.cold.1
+ __23-[WPClient addServices]_block_invoke_2.405
+ __23-[WPClient addServices]_block_invoke_2.405.cold.1
+ __23-[WPClient addServices]_block_invoke_2.405.cold.2
+ __23-[WPTransfer startScan]_block_invoke.165
+ __25-[WPClient stopScanning:]_block_invoke_2.cold.2
+ __26-[WPClient enableTestMode]_block_invoke.661
+ __26-[WPClient enableTestMode]_block_invoke.661.cold.1
+ __26-[WPClient enableTestMode]_block_invoke.661.cold.2
+ __26-[WPClient enableTestMode]_block_invoke.cold.2
+ __26-[WPClient enableTestMode]_block_invoke_2.664
+ __26-[WPClient startScanning:]_block_invoke_2.cold.2
+ __26-[WPHeySiri startScanning]_block_invoke.178
+ __26-[WPTest sendData:toPeer:]_block_invoke.287
+ __26-[WPTest sendData:toPeer:]_block_invoke.293
+ __26-[WPTest sendData:toPeer:]_block_invoke.299
+ __27-[WPClient disableScanning]_block_invoke.715
+ __27-[WPClient disableScanning]_block_invoke.715.cold.1
+ __27-[WPClient disableScanning]_block_invoke.715.cold.2
+ __27-[WPClient disableScanning]_block_invoke.cold.2
+ __27-[WPClient disableScanning]_block_invoke_2.718
+ __27-[WPClient dumpDaemonState]_block_invoke.707
+ __27-[WPClient dumpDaemonState]_block_invoke.707.cold.1
+ __27-[WPClient dumpDaemonState]_block_invoke.707.cold.2
+ __27-[WPClient dumpDaemonState]_block_invoke.cold.2
+ __27-[WPClient dumpDaemonState]_block_invoke_2.710
+ __27-[WPClient stateDidChange:]_block_invoke.643
+ __27-[WPRanging enableRanging:]_block_invoke.123
+ __27-[WPTransfer receivedData:]_block_invoke.293
+ __27-[WPTransfer receivedData:]_block_invoke.299
+ __27-[WPTransfer receivedData:]_block_invoke.318
+ __28-[WPClient sendTestRequest:]_block_invoke.723
+ __28-[WPClient sendTestRequest:]_block_invoke.723.cold.1
+ __28-[WPClient sendTestRequest:]_block_invoke.723.cold.2
+ __28-[WPClient sendTestRequest:]_block_invoke.cold.2
+ __28-[WPClient sendTestRequest:]_block_invoke_2.726
+ __28-[WPClient stopAdvertising:]_block_invoke_2.cold.2
+ __28-[WPNearby sendData:toPeer:]_block_invoke.355
+ __28-[WPNearby sendData:toPeer:]_block_invoke.361
+ __28-[WPNearby sendData:toPeer:]_block_invoke.365
+ __29-[WPClient getPowerLogStats:]_block_invoke.695
+ __29-[WPClient getPowerLogStats:]_block_invoke.695.cold.1
+ __29-[WPClient getPowerLogStats:]_block_invoke.695.cold.2
+ __29-[WPClient getPowerLogStats:]_block_invoke.701
+ __29-[WPClient getPowerLogStats:]_block_invoke.cold.2
+ __29-[WPClient getPowerLogStats:]_block_invoke_2.698
+ __29-[WPClient startAdvertising:]_block_invoke.432
+ __29-[WPClient startAdvertising:]_block_invoke.438
+ __29-[WPNearby deviceDiscovered:]_block_invoke.277
+ __29-[WPNearby deviceDiscovered:]_block_invoke.282
+ __29-[WPTest disconnectFromPeer:]_block_invoke.332
+ __30-[WPClient getAllTrackedZones]_block_invoke.607
+ __30-[WPClient getAllTrackedZones]_block_invoke.607.cold.1
+ __30-[WPClient getAllTrackedZones]_block_invoke.607.cold.2
+ __30-[WPClient getAllTrackedZones]_block_invoke.cold.2
+ __30-[WPClient getAllTrackedZones]_block_invoke_2.610
+ __30-[WPClient startTrackingZone:]_block_invoke.581
+ __30-[WPClient startTrackingZone:]_block_invoke.581.cold.1
+ __30-[WPClient startTrackingZone:]_block_invoke.581.cold.2
+ __30-[WPClient startTrackingZone:]_block_invoke.cold.2
+ __30-[WPClient startTrackingZone:]_block_invoke_2.584
+ __30-[WPClient stopTrackingZones:]_block_invoke.589
+ __30-[WPClient stopTrackingZones:]_block_invoke.589.cold.1
+ __30-[WPClient stopTrackingZones:]_block_invoke.589.cold.2
+ __30-[WPClient stopTrackingZones:]_block_invoke.cold.2
+ __30-[WPClient stopTrackingZones:]_block_invoke_2.592
+ __30-[WPContinuity connectToPeer:]_block_invoke.282
+ __30-[WPHeySiri deviceDiscovered:]_block_invoke.222
+ __30-[WPTransfer startAdvertising]_block_invoke.181
+ __31-[WPClient disconnectFromPeer:]_block_invoke_2.cold.2
+ __31-[WPClient establishConnection]_block_invoke.169
+ __31-[WPClient establishConnection]_block_invoke.cold.1
+ __31-[WPClient establishConnection]_block_invoke.cold.2
+ __31-[WPClient overrideAdvTimeout:]_block_invoke.687
+ __31-[WPClient overrideAdvTimeout:]_block_invoke.687.cold.1
+ __31-[WPClient overrideAdvTimeout:]_block_invoke.687.cold.2
+ __31-[WPClient overrideAdvTimeout:]_block_invoke.cold.1
+ __31-[WPClient overrideAdvTimeout:]_block_invoke_2.690
+ __31-[WPClient unregisterEndpoint:]_block_invoke_2.cold.2
+ __31-[WPNearby disconnectFromPeer:]_block_invoke.403
+ __31-[WPTransfer deviceDiscovered:]_block_invoke.220
+ __32-[WPClient enableBubbleTestMode]_block_invoke.669
+ __32-[WPClient enableBubbleTestMode]_block_invoke.669.cold.1
+ __32-[WPClient enableBubbleTestMode]_block_invoke.669.cold.2
+ __32-[WPClient enableBubbleTestMode]_block_invoke.cold.2
+ __32-[WPClient enableBubbleTestMode]_block_invoke_2.672
+ __32-[WPClient enableRanging:reply:]_block_invoke_2.cold.2
+ __32-[WPClient overrideScanTimeout:]_block_invoke.677
+ __32-[WPClient overrideScanTimeout:]_block_invoke.677.cold.1
+ __32-[WPClient overrideScanTimeout:]_block_invoke.677.cold.2
+ __32-[WPClient overrideScanTimeout:]_block_invoke.cold.1
+ __32-[WPClient overrideScanTimeout:]_block_invoke_2.680
+ __32-[WPClient stopTrackingAllZones]_block_invoke.597
+ __32-[WPClient stopTrackingAllZones]_block_invoke.597.cold.1
+ __32-[WPClient stopTrackingAllZones]_block_invoke.597.cold.2
+ __32-[WPClient stopTrackingAllZones]_block_invoke.cold.2
+ __32-[WPClient stopTrackingAllZones]_block_invoke_2.600
+ __32-[WPContinuity sendData:toPeer:]_block_invoke.363
+ __32-[WPContinuity sendData:toPeer:]_block_invoke.369
+ __32-[WPContinuity sendData:toPeer:]_block_invoke.373
+ __33-[WPClient checkAllowDuplicates:]_block_invoke.650
+ __33-[WPClient checkAllowDuplicates:]_block_invoke.650.cold.1
+ __33-[WPClient checkAllowDuplicates:]_block_invoke.650.cold.2
+ __33-[WPClient checkAllowDuplicates:]_block_invoke.656
+ __33-[WPClient checkAllowDuplicates:]_block_invoke.cold.2
+ __33-[WPClient checkAllowDuplicates:]_block_invoke_2.653
+ __33-[WPHomeKit stopScanningForType:]_block_invoke.201
+ __34-[WPClient dispatchAdvertisement:]_block_invoke_2.cold.2
+ __34-[WPClient isRangingEnabledReply:]_block_invoke_2.cold.2
+ __35-[WPClient initWithQueue:machName:]_block_invoke.154
+ __35-[WPContinuity disconnectFromPeer:]_block_invoke.337
+ __36-[WPDeviceScanner deviceDiscovered:]_block_invoke.194
+ __36-[WPTest connectToPeer:withOptions:]_block_invoke.265
+ __37-[WPClient sendDatatoLePipe:forPeer:]_block_invoke_2.cold.2
+ __38-[WPClient clearDuplicateFilterCache:]_block_invoke_2.cold.2
+ __38-[WPClient connectToPeer:withOptions:]_block_invoke.549
+ __38-[WPClient connectToPeer:withOptions:]_block_invoke.549.cold.1
+ __38-[WPClient connectToPeer:withOptions:]_block_invoke.549.cold.2
+ __38-[WPClient connectToPeer:withOptions:]_block_invoke.559
+ __38-[WPClient connectToPeer:withOptions:]_block_invoke_2.560
+ __38-[WPClient connectToPeer:withOptions:]_block_invoke_2.560.cold.1
+ __38-[WPClient connectToPeer:withOptions:]_block_invoke_2.560.cold.2
+ __38-[WPClient registerForAnyScanResults:]_block_invoke_2.cold.2
+ __38-[WPNearby connectToPeer:withOptions:]_block_invoke.299
+ __39-[WPContinuity initWithDelegate:queue:]_block_invoke.146
+ __39-[WPDeviceScanner anyDiscoveredDevice:]_block_invoke.163
+ __39-[WPObjectDiscovery devicesDiscovered:]_block_invoke.271
+ __39-[WPTest disconnectedDevice:withError:]_block_invoke.342
+ __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke.540.cold.2
+ __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke.543
+ __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke.543.cold.1
+ __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke.543.cold.2
+ __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke_2.544
+ __41-[WPClient startTrackingPeerWithRequest:]_block_invoke.525.cold.2
+ __41-[WPClient startTrackingPeerWithRequest:]_block_invoke.528
+ __41-[WPClient startTrackingPeerWithRequest:]_block_invoke.528.cold.1
+ __41-[WPClient startTrackingPeerWithRequest:]_block_invoke.528.cold.2
+ __41-[WPClient startTrackingPeerWithRequest:]_block_invoke_2.532
+ __41-[WPNearby disconnectedDevice:withError:]_block_invoke.411
+ __42-[WPAWDL initWithDelegate:queue:machName:]_block_invoke.119
+ __42-[WPClient listenToBandwidthNotifications]_block_invoke.626
+ __42-[WPClient listenToBandwidthNotifications]_block_invoke.626.cold.1
+ __42-[WPClient listenToBandwidthNotifications]_block_invoke.626.cold.2
+ __42-[WPClient listenToBandwidthNotifications]_block_invoke.cold.2
+ __42-[WPClient listenToBandwidthNotifications]_block_invoke_2.629
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.236
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.240
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.246
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.250
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.250.cold.1
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke_2.251
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke_2.cold.1
+ __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke_2.cold.2
+ __43-[WPHomeKit startScanningWithData:forType:]_block_invoke.175
+ __43-[WPHomeKit startScanningWithData:forType:]_block_invoke.185
+ __43-[WPHomeKit startScanningWithData:forType:]_block_invoke.191
+ __44-[WPObjectDiscovery initWithDelegate:queue:]_block_invoke.190
+ __45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.488
+ __45-[WPContinuity disconnectedDevice:withError:]_block_invoke.345
+ __45-[WPPairing initWithDelegate:queue:machName:]_block_invoke.147
+ __45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.193
+ __45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.198
+ __46-[WPHeySiri updateScanningRequest:withUpdate:]_block_invoke.193
+ __46-[WPObjectDiscovery startScanningWithOptions:]_block_invoke.250
+ __46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.165
+ __46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.170
+ __47-[WPNearby advertisingStoppedOfType:withError:]_block_invoke.233
+ __48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.450
+ __49-[WPHeySiri updateAdvertisingRequest:withUpdate:]_block_invoke.173
+ __51-[WPContinuity advertisingStoppedOfType:withError:]_block_invoke.206
+ __51-[WPObjectDiscovery startScanningWithMode:Timeout:]_block_invoke.225
+ __51-[WPTest connectedDevice:withError:shouldDiscover:]_block_invoke.272
+ __52-[WPMagicSwitch advertisingStoppedOfType:withError:]_block_invoke.192
+ __53-[WPNearby connectedDevice:withError:shouldDiscover:]_block_invoke.309
+ __54-[WPTest sentData:toEndpoint:forPeripheral:withError:]_block_invoke.306
+ __55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.571
+ __55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke_2.cold.2
+ __55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.227
+ __55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.233
+ __56-[WPNearby sentData:toEndpoint:forPeripheral:withError:]_block_invoke.377
+ __56-[WPTest central:subscribed:toCharacteristic:inService:]_block_invoke.322
+ __57-[WPContinuity connectedDevice:withError:shouldDiscover:]_block_invoke.292
+ __58-[WPClient registerEndpoint:requireAck:requireEncryption:]_block_invoke_2.cold.2
+ __58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.284
+ __58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.297
+ __58-[WPNearby central:subscribed:toCharacteristic:inService:]_block_invoke.393
+ __59-[WPDeviceScanner parseCompanyData:forSize:intoDictionary:]_block_invoke.215
+ __60-[WPAWDL startConnectionlessAWDLServiceAdvertisingWithData:]_block_invoke.147
+ __60-[WPTest startAdvertisingOfType:data:priority:mode:options:]_block_invoke.170
+ __60-[WPTransfer central:subscribed:toCharacteristic:inService:]_block_invoke.356
+ __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.150
+ __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.160
+ __61-[WPClient discoverCharacteristicsAndServices:forPeripheral:]_block_invoke_2.cold.2
+ __62-[WPContinuity central:subscribed:toCharacteristic:inService:]_block_invoke.400
+ __62-[WPNearby startAdvertisingOfType:data:priority:mode:options:]_block_invoke.208
+ __63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.321
+ __63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.323
+ __63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.328
+ __64-[WPClient shouldSubscribe:toPeer:withCharacteristic:inService:]_block_invoke_2.cold.2
+ __65-[WPTest receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.312
+ __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.242
+ __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.250
+ __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.250.cold.1
+ __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.254
+ __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.259
+ __67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.304
+ __67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.304.cold.1
+ __67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.308
+ __67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.313
+ __67-[WPNearby receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.383
+ __69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.267
+ __69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.277
+ __69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.283
+ __71-[WPContinuity receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.388
+ __73-[WPNearby sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.372
+ __75-[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.332
+ __77-[WPContinuity sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.380
+ __80-[WPContinuity startScanningForType:withData:mask:peers:boostedScan:duplicates:]_block_invoke.226
+ __80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.336
+ __80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.342
+ __82-[WPTest startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:]_block_invoke.209
+ __84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.321
+ __84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.327
+ __96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.249
+ __96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.253
+ __block_literal_global.121
+ __block_literal_global.122
+ __block_literal_global.128
+ __block_literal_global.130
+ __block_literal_global.142
+ __block_literal_global.147
+ __block_literal_global.148
+ __block_literal_global.152
+ __block_literal_global.157
+ __block_literal_global.163
+ __block_literal_global.167
+ __block_literal_global.171
+ __block_literal_global.173
+ __block_literal_global.182
+ __block_literal_global.195
+ __block_literal_global.203
+ __block_literal_global.212
+ __block_literal_global.220
+ __block_literal_global.228
+ __block_literal_global.230
+ __block_literal_global.235
+ __block_literal_global.236
+ __block_literal_global.237
+ __block_literal_global.242
+ __block_literal_global.244
+ __block_literal_global.254
+ __block_literal_global.256
+ __block_literal_global.267
+ __block_literal_global.269
+ __block_literal_global.279
+ __block_literal_global.284
+ __block_literal_global.288
+ __block_literal_global.289
+ __block_literal_global.294
+ __block_literal_global.299
+ __block_literal_global.301
+ __block_literal_global.306
+ __block_literal_global.313
+ __block_literal_global.323
+ __block_literal_global.324
+ __block_literal_global.330
+ __block_literal_global.332
+ __block_literal_global.334
+ __block_literal_global.339
+ __block_literal_global.347
+ __block_literal_global.353
+ __block_literal_global.357
+ __block_literal_global.361
+ __block_literal_global.363
+ __block_literal_global.365
+ __block_literal_global.367
+ __block_literal_global.374
+ __block_literal_global.375
+ __block_literal_global.383
+ __block_literal_global.385
+ __block_literal_global.390
+ __block_literal_global.394
+ __block_literal_global.395
+ __block_literal_global.403
+ __block_literal_global.408
+ __block_literal_global.413
+ __block_literal_global.421
+ __block_literal_global.427
+ __block_literal_global.429
+ __block_literal_global.434
+ __block_literal_global.443
+ __block_literal_global.445
+ __block_literal_global.447
+ __block_literal_global.452
+ __block_literal_global.454
+ __block_literal_global.459
+ __block_literal_global.467
+ __block_literal_global.475
+ __block_literal_global.480
+ __block_literal_global.485
+ __block_literal_global.490
+ __block_literal_global.492
+ __block_literal_global.497
+ __block_literal_global.501
+ __block_literal_global.506
+ __block_literal_global.508
+ __block_literal_global.527
+ __block_literal_global.534
+ __block_literal_global.542
+ __block_literal_global.546
+ __block_literal_global.548
+ __block_literal_global.554
+ __block_literal_global.562
+ __block_literal_global.564
+ __block_literal_global.566
+ __block_literal_global.568
+ __block_literal_global.573
+ __block_literal_global.586
+ __block_literal_global.594
+ __block_literal_global.602
+ __block_literal_global.612
+ __block_literal_global.614
+ __block_literal_global.619
+ __block_literal_global.621
+ __block_literal_global.631
+ __block_literal_global.645
+ __block_literal_global.647
+ __block_literal_global.655
+ __block_literal_global.666
+ __block_literal_global.674
+ __block_literal_global.682
+ __block_literal_global.692
+ __block_literal_global.700
+ __block_literal_global.712
+ __block_literal_global.720
+ __block_literal_global.728
+ __block_literal_global.730
+ __block_literal_global.877
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$requestedAtNsec
+ _objc_msgSend$setRequestedAtNsec:
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- __22-[WPClient connection]_block_invoke.175
- __22-[WPClient connection]_block_invoke.179
- __22-[WPClient connection]_block_invoke_2.176
- __23-[WPClient addServices]_block_invoke.401
- __23-[WPClient addServices]_block_invoke_2.402
- __23-[WPClient addServices]_block_invoke_2.402.cold.1
- __23-[WPTransfer startScan]_block_invoke.159
- __26-[WPClient enableTestMode]_block_invoke.658
- __26-[WPClient enableTestMode]_block_invoke.658.cold.1
- __26-[WPClient enableTestMode]_block_invoke_2.661
- __26-[WPHeySiri startScanning]_block_invoke.175
- __26-[WPTest sendData:toPeer:]_block_invoke.284
- __26-[WPTest sendData:toPeer:]_block_invoke.290
- __26-[WPTest sendData:toPeer:]_block_invoke.296
- __27-[WPClient disableScanning]_block_invoke.712
- __27-[WPClient disableScanning]_block_invoke.712.cold.1
- __27-[WPClient disableScanning]_block_invoke_2.715
- __27-[WPClient dumpDaemonState]_block_invoke.704
- __27-[WPClient dumpDaemonState]_block_invoke.704.cold.1
- __27-[WPClient dumpDaemonState]_block_invoke_2.707
- __27-[WPClient stateDidChange:]_block_invoke.631
- __27-[WPRanging enableRanging:]_block_invoke.120
- __27-[WPTransfer receivedData:]_block_invoke.290
- __27-[WPTransfer receivedData:]_block_invoke.296
- __27-[WPTransfer receivedData:]_block_invoke.303
- __28-[WPClient sendTestRequest:]_block_invoke.720
- __28-[WPClient sendTestRequest:]_block_invoke.720.cold.1
- __28-[WPClient sendTestRequest:]_block_invoke_2.723
- __28-[WPNearby sendData:toPeer:]_block_invoke.352
- __28-[WPNearby sendData:toPeer:]_block_invoke.358
- __28-[WPNearby sendData:toPeer:]_block_invoke.362
- __29-[WPClient getPowerLogStats:]_block_invoke.692
- __29-[WPClient getPowerLogStats:]_block_invoke.692.cold.1
- __29-[WPClient getPowerLogStats:]_block_invoke.698
- __29-[WPClient getPowerLogStats:]_block_invoke_2.695
- __29-[WPClient startAdvertising:]_block_invoke.429
- __29-[WPClient startAdvertising:]_block_invoke.435
- __29-[WPNearby deviceDiscovered:]_block_invoke.274
- __29-[WPNearby deviceDiscovered:]_block_invoke.279
- __29-[WPTest disconnectFromPeer:]_block_invoke.329
- __30-[WPClient getAllTrackedZones]_block_invoke.604
- __30-[WPClient getAllTrackedZones]_block_invoke.604.cold.1
- __30-[WPClient getAllTrackedZones]_block_invoke_2.607
- __30-[WPClient startTrackingZone:]_block_invoke.578
- __30-[WPClient startTrackingZone:]_block_invoke.578.cold.1
- __30-[WPClient startTrackingZone:]_block_invoke_2.581
- __30-[WPClient stopTrackingZones:]_block_invoke.586
- __30-[WPClient stopTrackingZones:]_block_invoke.586.cold.1
- __30-[WPClient stopTrackingZones:]_block_invoke_2.589
- __30-[WPContinuity connectToPeer:]_block_invoke.276
- __30-[WPHeySiri deviceDiscovered:]_block_invoke.219
- __30-[WPTransfer startAdvertising]_block_invoke.178
- __31-[WPClient establishConnection]_block_invoke.166
- __31-[WPClient overrideAdvTimeout:]_block_invoke.684
- __31-[WPClient overrideAdvTimeout:]_block_invoke.684.cold.1
- __31-[WPClient overrideAdvTimeout:]_block_invoke_2.687
- __31-[WPNearby disconnectFromPeer:]_block_invoke.400
- __31-[WPTransfer deviceDiscovered:]_block_invoke.199
- __32-[WPClient enableBubbleTestMode]_block_invoke.666
- __32-[WPClient enableBubbleTestMode]_block_invoke.666.cold.1
- __32-[WPClient enableBubbleTestMode]_block_invoke_2.669
- __32-[WPClient overrideScanTimeout:]_block_invoke.674
- __32-[WPClient overrideScanTimeout:]_block_invoke.674.cold.1
- __32-[WPClient overrideScanTimeout:]_block_invoke_2.677
- __32-[WPClient stopTrackingAllZones]_block_invoke.594
- __32-[WPClient stopTrackingAllZones]_block_invoke.594.cold.1
- __32-[WPClient stopTrackingAllZones]_block_invoke_2.597
- __32-[WPContinuity sendData:toPeer:]_block_invoke.357
- __32-[WPContinuity sendData:toPeer:]_block_invoke.366
- __32-[WPContinuity sendData:toPeer:]_block_invoke.370
- __33-[WPClient checkAllowDuplicates:]_block_invoke.647
- __33-[WPClient checkAllowDuplicates:]_block_invoke.647.cold.1
- __33-[WPClient checkAllowDuplicates:]_block_invoke.653
- __33-[WPClient checkAllowDuplicates:]_block_invoke_2.650
- __33-[WPHomeKit stopScanningForType:]_block_invoke.195
- __35-[WPClient initWithQueue:machName:]_block_invoke.151
- __35-[WPContinuity disconnectFromPeer:]_block_invoke.334
- __36-[WPDeviceScanner deviceDiscovered:]_block_invoke.191
- __36-[WPTest connectToPeer:withOptions:]_block_invoke.259
- __38-[WPClient connectToPeer:withOptions:]_block_invoke.546
- __38-[WPClient connectToPeer:withOptions:]_block_invoke.546.cold.1
- __38-[WPClient connectToPeer:withOptions:]_block_invoke.556
- __38-[WPClient connectToPeer:withOptions:]_block_invoke_2.557
- __38-[WPClient connectToPeer:withOptions:]_block_invoke_2.557.cold.1
- __38-[WPNearby connectToPeer:withOptions:]_block_invoke.293
- __39-[WPContinuity initWithDelegate:queue:]_block_invoke.143
- __39-[WPDeviceScanner anyDiscoveredDevice:]_block_invoke.160
- __39-[WPObjectDiscovery devicesDiscovered:]_block_invoke.268
- __39-[WPTest disconnectedDevice:withError:]_block_invoke.339
- __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke.534
- __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke.537.cold.1
- __40-[WPClient stopTrackingPeerWithRequest:]_block_invoke_2.541
- __41-[WPClient startTrackingPeerWithRequest:]_block_invoke.522
- __41-[WPClient startTrackingPeerWithRequest:]_block_invoke.522.cold.1
- __41-[WPClient startTrackingPeerWithRequest:]_block_invoke_2.529
- __41-[WPNearby disconnectedDevice:withError:]_block_invoke.408
- __42-[WPAWDL initWithDelegate:queue:machName:]_block_invoke.116
- __42-[WPClient listenToBandwidthNotifications]_block_invoke.623
- __42-[WPClient listenToBandwidthNotifications]_block_invoke.623.cold.1
- __42-[WPClient listenToBandwidthNotifications]_block_invoke_2.626
- __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.233
- __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.237
- __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.243
- __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.247
- __42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke_2.248
- __43-[WPHomeKit startScanningWithData:forType:]_block_invoke.172
- __43-[WPHomeKit startScanningWithData:forType:]_block_invoke.182
- __43-[WPHomeKit startScanningWithData:forType:]_block_invoke.188
- __44-[WPObjectDiscovery initWithDelegate:queue:]_block_invoke.187
- __45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.485
- __45-[WPContinuity disconnectedDevice:withError:]_block_invoke.342
- __45-[WPPairing initWithDelegate:queue:machName:]_block_invoke.144
- __45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.190
- __45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.195
- __46-[WPHeySiri updateScanningRequest:withUpdate:]_block_invoke.190
- __46-[WPObjectDiscovery startScanningWithOptions:]_block_invoke.247
- __46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.162
- __46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.167
- __47-[WPNearby advertisingStoppedOfType:withError:]_block_invoke.230
- __48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.447
- __49-[WPHeySiri updateAdvertisingRequest:withUpdate:]_block_invoke.170
- __51-[WPContinuity advertisingStoppedOfType:withError:]_block_invoke.203
- __51-[WPObjectDiscovery startScanningWithMode:Timeout:]_block_invoke.222
- __51-[WPTest connectedDevice:withError:shouldDiscover:]_block_invoke.269
- __52-[WPMagicSwitch advertisingStoppedOfType:withError:]_block_invoke.189
- __53-[WPNearby connectedDevice:withError:shouldDiscover:]_block_invoke.306
- __54-[WPTest sentData:toEndpoint:forPeripheral:withError:]_block_invoke.303
- __55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.568
- __55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.224
- __55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.230
- __56-[WPNearby sentData:toEndpoint:forPeripheral:withError:]_block_invoke.374
- __56-[WPTest central:subscribed:toCharacteristic:inService:]_block_invoke.316
- __57-[WPContinuity connectedDevice:withError:shouldDiscover:]_block_invoke.289
- __58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.281
- __58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.285
- __58-[WPNearby central:subscribed:toCharacteristic:inService:]_block_invoke.387
- __59-[WPDeviceScanner parseCompanyData:forSize:intoDictionary:]_block_invoke.212
- __60-[WPAWDL startConnectionlessAWDLServiceAdvertisingWithData:]_block_invoke.144
- __60-[WPTest startAdvertisingOfType:data:priority:mode:options:]_block_invoke.167
- __60-[WPTransfer central:subscribed:toCharacteristic:inService:]_block_invoke.338
- __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.138
- __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.154
- __62-[WPContinuity central:subscribed:toCharacteristic:inService:]_block_invoke.394
- __62-[WPNearby startAdvertisingOfType:data:priority:mode:options:]_block_invoke.205
- __63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.315
- __63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.320
- __63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.325
- __65-[WPTest receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.309
- __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.239
- __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.244
- __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.251
- __65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.256
- __67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.298
- __67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.305
- __67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.310
- __67-[WPNearby receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.380
- __69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.261
- __69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.268
- __69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.280
- __71-[WPContinuity receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.385
- __73-[WPNearby sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.369
- __75-[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.320
- __77-[WPContinuity sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.377
- __80-[WPContinuity startScanningForType:withData:mask:peers:boostedScan:duplicates:]_block_invoke.223
- __80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.333
- __80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.339
- __82-[WPTest startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:]_block_invoke.206
- __84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.318
- __84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.324
- __96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.246
- __96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.250
- __block_literal_global.118
- __block_literal_global.119
- __block_literal_global.125
- __block_literal_global.127
- __block_literal_global.137
- __block_literal_global.139
- __block_literal_global.144
- __block_literal_global.145
- __block_literal_global.150
- __block_literal_global.151
- __block_literal_global.155
- __block_literal_global.160
- __block_literal_global.169
- __block_literal_global.170
- __block_literal_global.174
- __block_literal_global.176
- __block_literal_global.185
- __block_literal_global.198
- __block_literal_global.206
- __block_literal_global.215
- __block_literal_global.223
- __block_literal_global.231
- __block_literal_global.233
- __block_literal_global.238
- __block_literal_global.239
- __block_literal_global.243
- __block_literal_global.245
- __block_literal_global.250
- __block_literal_global.260
- __block_literal_global.268
- __block_literal_global.270
- __block_literal_global.278
- __block_literal_global.282
- __block_literal_global.287
- __block_literal_global.291
- __block_literal_global.292
- __block_literal_global.300
- __block_literal_global.302
- __block_literal_global.307
- __block_literal_global.312
- __block_literal_global.319
- __block_literal_global.326
- __block_literal_global.327
- __block_literal_global.333
- __block_literal_global.335
- __block_literal_global.337
- __block_literal_global.350
- __block_literal_global.351
- __block_literal_global.359
- __block_literal_global.360
- __block_literal_global.364
- __block_literal_global.368
- __block_literal_global.372
- __block_literal_global.373
- __block_literal_global.380
- __block_literal_global.381
- __block_literal_global.386
- __block_literal_global.391
- __block_literal_global.393
- __block_literal_global.397
- __block_literal_global.407
- __block_literal_global.412
- __block_literal_global.424
- __block_literal_global.426
- __block_literal_global.428
- __block_literal_global.437
- __block_literal_global.442
- __block_literal_global.444
- __block_literal_global.446
- __block_literal_global.451
- __block_literal_global.456
- __block_literal_global.464
- __block_literal_global.472
- __block_literal_global.477
- __block_literal_global.482
- __block_literal_global.484
- __block_literal_global.489
- __block_literal_global.491
- __block_literal_global.498
- __block_literal_global.503
- __block_literal_global.505
- __block_literal_global.521
- __block_literal_global.531
- __block_literal_global.533
- __block_literal_global.543
- __block_literal_global.545
- __block_literal_global.551
- __block_literal_global.559
- __block_literal_global.561
- __block_literal_global.563
- __block_literal_global.565
- __block_literal_global.567
- __block_literal_global.577
- __block_literal_global.585
- __block_literal_global.593
- __block_literal_global.603
- __block_literal_global.611
- __block_literal_global.613
- __block_literal_global.618
- __block_literal_global.622
- __block_literal_global.630
- __block_literal_global.644
- __block_literal_global.646
- __block_literal_global.657
- __block_literal_global.665
- __block_literal_global.673
- __block_literal_global.683
- __block_literal_global.691
- __block_literal_global.703
- __block_literal_global.711
- __block_literal_global.719
- __block_literal_global.727
- __block_literal_global.874
CStrings:
+ "DCTProtocolDataAndTelephony"
+ "DCTProtocolTelephony"
+ "FindMyActionExtendedRange"
+ "FindMyActionExtendedRangeLE2M"
+ "FindMyActionExtendedRangeTransient"
+ "FindMyPlaySoundExtendedRange"
+ "SofrwareUpdateOutboxControllerAuth"
+ "SoftwareUpdateBTWake"
+ "Tq,V_requestedAtNsec"
+ "_requestedAtNsec"
+ "decodeInt64ForKey:"
+ "encodeInt64:forKey:"
+ "kRequestedAtNsec"
+ "requestedAtNsec"
+ "setRequestedAtNsec:"

```
