## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/Versions/A/WPDaemon`

```diff

-183.9.1.0.1
-  __TEXT.__text: 0x58984
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x3584
-  __TEXT.__cstring: 0x3bfc
-  __TEXT.__const: 0x1c8
-  __TEXT.__oslogstring: 0x95bb
-  __TEXT.__gcc_except_tab: 0x14f8
-  __TEXT.__unwind_info: 0x1570
+184.42.0.3.0
+  __TEXT.__text: 0x5b1a0
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x3f1c
+  __TEXT.__cstring: 0x3cee
+  __TEXT.__const: 0x1c0
+  __TEXT.__oslogstring: 0x94cc
+  __TEXT.__gcc_except_tab: 0x1514
+  __TEXT.__unwind_info: 0x1bf0
   __TEXT.__objc_classname: 0x35c
-  __TEXT.__objc_methname: 0x94da
+  __TEXT.__objc_methname: 0x957b
   __TEXT.__objc_methtype: 0x15b6
-  __TEXT.__objc_stubs: 0x7440
-  __DATA_CONST.__got: 0x420
+  __TEXT.__objc_stubs: 0x7500
+  __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2368
+  __DATA_CONST.__objc_selrefs: 0x24b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x2b8
-  __AUTH_CONST.__auth_got: 0x348
-  __AUTH_CONST.__const: 0x6cf0
-  __AUTH_CONST.__cfstring: 0x31c0
-  __AUTH_CONST.__objc_const: 0x8fd8
+  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__const: 0x6cc0
+  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__objc_const: 0x7e28
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x4b4
+  __DATA.__objc_ivar: 0x4b8
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x8c
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD70F7E2-F4C0-3222-9A96-BEA61BFA5611
-  Functions: 2384
-  Symbols:   5259
-  CStrings:  3694
+  UUID: 52809A50-76C9-3596-A0A1-A52E76FE2547
+  Functions: 3100
+  Symbols:   5987
+  CStrings:  3710
 
Symbols:
+ +[WPDClient approvedBundleIDs].cold.1
+ +[WPDClient approvedProcesses].cold.1
+ +[WPDClient generateStateDump].cold.1
+ +[WPDClient generateStateDump].cold.2
+ +[WPDClient initialize].cold.2
+ +[WPDClient unknownUseCases].cold.1
+ +[WPDManager initializeAdvDenylist:AdvAllowlist:ScanDenylist:ScanAllowlist:].cold.1
+ +[WPDManager initializeAdvDenylist:AdvAllowlist:ScanDenylist:ScanAllowlist:].cold.2
+ +[WPDManager initialize].cold.1
+ +[WPDManager initialize].cold.2
+ +[WPDManager initialize].cold.3
+ +[WPDObjectDiscoveryData applyMaskToAddress:].cold.2
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.10
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.11
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.12
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.13
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.7
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.8
+ +[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:].cold.9
+ +[WPDScanManager zonesAvailableForType:].cold.2
+ +[WPDSearchPartyAgent spBeaconKeyFromTestKey:].cold.3
+ +[WPDSearchPartyAgent spBeaconKeyFromTestKey:].cold.4
+ +[WPDXPCInterfaces clientInterface].cold.1
+ +[WPDXPCInterfaces serverInterface].cold.1
+ +[WPDaemonServer initialize].cold.2
+ +[WPDaemonServer isInternalBuild].cold.1
+ +[WPDaemonServer supportsRanging].cold.1
+ -[PipeDataTransfer generateSequenceNumber].cold.2
+ -[PipeDataTransfer generateSequenceNumber].cold.3
+ -[PipeInfo dealloc].cold.1
+ -[WPDAdvertisingData addAdvertisingRequest:].cold.1
+ -[WPDAdvertisingData addAdvertisingRequest:].cold.2
+ -[WPDAdvertisingManager addAdvertisingRequest:forClient:].cold.3
+ -[WPDAdvertisingManager addAdvertisingRequest:forClient:].cold.4
+ -[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:].cold.1
+ -[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:].cold.2
+ -[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:].cold.3
+ -[WPDAdvertisingManager addCharacteristic:forService:forClient:].cold.3
+ -[WPDAdvertisingManager addCharacteristic:forService:forClient:].cold.4
+ -[WPDAdvertisingManager addCharacteristic:forService:forClient:].cold.5
+ -[WPDAdvertisingManager addCharacteristic:forService:forClient:].cold.6
+ -[WPDAdvertisingManager addCharacteristic:forService:forClient:].cold.7
+ -[WPDAdvertisingManager addCharacteristic:forService:forClient:].cold.8
+ -[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:].cold.1
+ -[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:].cold.2
+ -[WPDAdvertisingManager advertisingRules].cold.1
+ -[WPDAdvertisingManager advertisingRules].cold.2
+ -[WPDAdvertisingManager advertisingRules].cold.3
+ -[WPDAdvertisingManager advertisingRules].cold.4
+ -[WPDAdvertisingManager advertisingRules].cold.5
+ -[WPDAdvertisingManager enableRanging:forClient:].cold.2
+ -[WPDAdvertisingManager heySiriAdvertActive:].cold.1
+ -[WPDAdvertisingManager heySiriAdvertActive:].cold.2
+ -[WPDAdvertisingManager heySiriAdvertActiveAllDevices].cold.1
+ -[WPDAdvertisingManager heySiriAdvertActiveAllDevices].cold.2
+ -[WPDAdvertisingManager initWithServer:].cold.2
+ -[WPDAdvertisingManager initWithServer:].cold.3
+ -[WPDAdvertisingManager isAdvertiserTestMode].cold.2
+ -[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:].cold.2
+ -[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:].cold.3
+ -[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:].cold.4
+ -[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:].cold.5
+ -[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:].cold.6
+ -[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:].cold.7
+ -[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:].cold.1
+ -[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:].cold.2
+ -[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:].cold.3
+ -[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:].cold.4
+ -[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:].cold.5
+ -[WPDAdvertisingManager peripheralManager:didAddService:error:].cold.2
+ -[WPDAdvertisingManager peripheralManager:didAddService:error:].cold.3
+ -[WPDAdvertisingManager peripheralManager:didReceiveReadRequest:].cold.1
+ -[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:].cold.1
+ -[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:].cold.2
+ -[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:].cold.3
+ -[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:].cold.2
+ -[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:].cold.3
+ -[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:].cold.4
+ -[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:].cold.5
+ -[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:].cold.6
+ -[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:].cold.2
+ -[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:].cold.3
+ -[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:].cold.4
+ -[WPDAdvertisingManager peripheralManagerIsReadyToUpdateSubscribers:].cold.1
+ -[WPDAdvertisingManager preallocateServices].cold.2
+ -[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:].cold.1
+ -[WPDAdvertisingManager removeServiceForClient:].cold.1
+ -[WPDAdvertisingManager removeServiceForClient:].cold.2
+ -[WPDAdvertisingManager requestFromAdvertisingDataFromInstance:AddressChangeNotificationNeeded:].cold.1
+ -[WPDAdvertisingManager updateAdvertiser].cold.2
+ -[WPDAdvertisingManager updateAdvertiser].cold.3
+ -[WPDAdvertisingManager updateAdvertiser].cold.4
+ -[WPDAdvertisingManager updateAdvertiser].cold.5
+ -[WPDAdvertisingManager update].cold.1
+ -[WPDAdvertisingManager update].cold.2
+ -[WPDAdvertisingManager update].cold.3
+ -[WPDAdvertisingManager update].cold.4
+ -[WPDClient addCharacteristic:forService:].cold.1
+ -[WPDClient advertisingFailedToStart:ofType:].cold.1
+ -[WPDClient advertisingPendingOfType:].cold.1
+ -[WPDClient advertisingStartedOfType:].cold.1
+ -[WPDClient advertisingStoppedOfType:withError:].cold.1
+ -[WPDClient advertisingStoppedOfType:withError:].cold.2
+ -[WPDClient cancelConnectionTimer:].cold.1
+ -[WPDClient central:subscribed:toCharacteristic:inService:].cold.3
+ -[WPDClient central:subscribed:toCharacteristic:inService:].cold.4
+ -[WPDClient central:subscribed:toCharacteristic:inService:].cold.5
+ -[WPDClient central:subscribed:toCharacteristic:inService:].cold.6
+ -[WPDClient checkAllowDuplicates:].cold.2
+ -[WPDClient clearDuplicateFilterCache_async:].cold.4
+ -[WPDClient clearDuplicateFilterCache_async:].cold.5
+ -[WPDClient clearDuplicateFilterCache_async:].cold.6
+ -[WPDClient clearDuplicateFilterCache_async:].cold.7
+ -[WPDClient clearDuplicateFilterCache_async:].cold.8
+ -[WPDClient connectToPeer:withOptions:].cold.3
+ -[WPDClient connectToPeer:withOptions:].cold.4
+ -[WPDClient connectToPeer:withOptions:].cold.5
+ -[WPDClient connectToPeer:withOptions:].cold.6
+ -[WPDClient connectToPeer:withOptions:].cold.7
+ -[WPDClient connectToPeer:withOptions:].cold.8
+ -[WPDClient connectedDevice:withError:shouldDiscover:].cold.2
+ -[WPDClient connectedDevice:withError:shouldDiscover:].cold.3
+ -[WPDClient connectedDevice:withError:shouldDiscover:].cold.4
+ -[WPDClient connectedDevice:withError:shouldDiscover:].cold.5
+ -[WPDClient connectedDeviceOverLEPipe:].cold.1
+ -[WPDClient connectedDeviceOverLEPipe:].cold.2
+ -[WPDClient connectedDeviceOverLEPipe:].cold.3
+ -[WPDClient createdConnection:].cold.1
+ -[WPDClient createdConnection:].cold.2
+ -[WPDClient createdConnection:].cold.3
+ -[WPDClient createdConnection:].cold.4
+ -[WPDClient dealloc].cold.1
+ -[WPDClient destroy].cold.1
+ -[WPDClient destroy].cold.2
+ -[WPDClient destroy_async].cold.3
+ -[WPDClient destroy_async].cold.4
+ -[WPDClient disableScanning].cold.1
+ -[WPDClient disconnectFromPeer:].cold.3
+ -[WPDClient disconnectFromPeer:].cold.4
+ -[WPDClient disconnectFromPeer:].cold.5
+ -[WPDClient disconnectFromPeer:].cold.6
+ -[WPDClient disconnectFromPeer:].cold.7
+ -[WPDClient disconnectedDeviceOverLEPipe:withError:].cold.1
+ -[WPDClient disconnectedPeer:error:].cold.3
+ -[WPDClient disconnectedPeer:error:].cold.4
+ -[WPDClient disconnectedPeer:error:].cold.5
+ -[WPDClient discoverCharacteristicsAndServices:forPeripheral:].cold.2
+ -[WPDClient discoverCharacteristicsAndServices:forPeripheral:].cold.3
+ -[WPDClient discoveredCharacteristicsAndServices:forPeripheral:].cold.1
+ -[WPDClient dumpDaemonState].cold.1
+ -[WPDClient enteredZone:manufacturerData:].cold.2
+ -[WPDClient foundPeer:ofType:].cold.1
+ -[WPDClient getAllTrackedZones].cold.2
+ -[WPDClient initWithXPCConnection:server:].cold.3
+ -[WPDClient initWithXPCConnection:server:].cold.4
+ -[WPDClient initWithXPCConnection:server:].cold.5
+ -[WPDClient listenToBandwidthNotifications].cold.1
+ -[WPDClient lostPeer:ofType:].cold.1
+ -[WPDClient notifyClientStateChange:Restricted:].cold.3
+ -[WPDClient notifyClientStateChange:Restricted:].cold.4
+ -[WPDClient overrideAdvTimeout:].cold.1
+ -[WPDClient overrideScanTimeout:].cold.1
+ -[WPDClient queueBlock:].cold.1
+ -[WPDClient rangingEnabled:withError:].cold.1
+ -[WPDClient receivedData:fromCharacteristic:inService:forPeripheral:].cold.1
+ -[WPDClient receivedData:fromEndpoint:forPeripheral:].cold.2
+ -[WPDClient receivedTestResponse:].cold.2
+ -[WPDClient registerEndpoint:requireAck:requireEncryption:].cold.1
+ -[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:].cold.2
+ -[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:].cold.3
+ -[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:].cold.4
+ -[WPDClient resumeCommunicationWithConnection:andProcessID:].cold.1
+ -[WPDClient sendDataToCharacteristic:inService:forPeer:].cold.3
+ -[WPDClient sendDataToCharacteristic:inService:forPeer:].cold.4
+ -[WPDClient sendDataToCharacteristic:inService:forPeer:].cold.5
+ -[WPDClient sendDataToCharacteristic:inService:forPeer:].cold.6
+ -[WPDClient sendTestRequest:].cold.4
+ -[WPDClient sendTestRequest:].cold.5
+ -[WPDClient sendTestRequest:].cold.6
+ -[WPDClient sentData:forCharacteristic:inService:forPeripheral:withError:].cold.1
+ -[WPDClient sentData:toEndpoint:forPeripheral:withError:].cold.1
+ -[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:].cold.3
+ -[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:].cold.4
+ -[WPDClient startAdvertising:].cold.2
+ -[WPDClient startAdvertising_async:].cold.4
+ -[WPDClient startAdvertising_async:].cold.5
+ -[WPDClient startAdvertising_async:].cold.6
+ -[WPDClient startAdvertising_async:].cold.7
+ -[WPDClient startAdvertising_async:].cold.8
+ -[WPDClient startAdvertising_async:].cold.9
+ -[WPDClient startScanning:].cold.2
+ -[WPDClient startScanning_async:].cold.10
+ -[WPDClient startScanning_async:].cold.11
+ -[WPDClient startScanning_async:].cold.12
+ -[WPDClient startScanning_async:].cold.13
+ -[WPDClient startScanning_async:].cold.6
+ -[WPDClient startScanning_async:].cold.7
+ -[WPDClient startScanning_async:].cold.8
+ -[WPDClient startScanning_async:].cold.9
+ -[WPDClient startTrackingZone:].cold.2
+ -[WPDClient stopAdvertising:].cold.2
+ -[WPDClient stopAdvertising_async:].cold.4
+ -[WPDClient stopAdvertising_async:].cold.5
+ -[WPDClient stopAdvertising_async:].cold.6
+ -[WPDClient stopAdvertising_async:].cold.7
+ -[WPDClient stopScanning:].cold.2
+ -[WPDClient stopScanning_async:].cold.4
+ -[WPDClient stopScanning_async:].cold.5
+ -[WPDClient stopScanning_async:].cold.6
+ -[WPDClient stopScanning_async:].cold.7
+ -[WPDClient stopScanning_async:].cold.8
+ -[WPDClient stopScans].cold.2
+ -[WPDClient stopTrackingAllZones].cold.2
+ -[WPDClient stopTrackingZones:].cold.2
+ -[WPDClient tickleMachPort].cold.2
+ -[WPDClient tickleMachPort].cold.3
+ -[WPDClient unregisterEndpoint:].cold.1
+ -[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.2
+ -[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:].cold.3
+ -[WPDClient verifyApprovedUseCase].cold.4
+ -[WPDClient verifyApprovedUseCase].cold.5
+ -[WPDClient verifyApprovedUseCase].cold.6
+ -[WPDConnection dealloc].cold.1
+ -[WPDConnection dealloc].cold.2
+ -[WPDConnection dealloc].cold.3
+ -[WPDConnection discoverCharacteristicsAndServices:forPeripheral:].cold.1
+ -[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:].cold.3
+ -[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:].cold.4
+ -[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:].cold.5
+ -[WPDConnection holdVoucher].cold.1
+ -[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:].cold.2
+ -[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:].cold.3
+ -[WPDConnection peripheral:didDiscoverServices:].cold.1
+ -[WPDConnection peripheral:didDiscoverServices:].cold.2
+ -[WPDConnection peripheral:didModifyServices:].cold.3
+ -[WPDConnection peripheral:didModifyServices:].cold.4
+ -[WPDConnection peripheral:didModifyServices:].cold.5
+ -[WPDConnection peripheral:didModifyServices:].cold.6
+ -[WPDConnection peripheral:didUpdateNotificationStateForCharacteristic:error:].cold.2
+ -[WPDConnection peripheral:didUpdateNotificationStateForCharacteristic:error:].cold.3
+ -[WPDConnection peripheral:didUpdateValueForCharacteristic:error:].cold.3
+ -[WPDConnection peripheral:didUpdateValueForCharacteristic:error:].cold.4
+ -[WPDConnection peripheral:didWriteValueForCharacteristic:error:].cold.3
+ -[WPDConnection peripheral:didWriteValueForCharacteristic:error:].cold.4
+ -[WPDConnection peripheral:didWriteValueForCharacteristic:error:].cold.5
+ -[WPDConnection resetData].cold.2
+ -[WPDConnection sendDataToCentral].cold.3
+ -[WPDConnection sendDataToCentral].cold.4
+ -[WPDConnection sendDataToCentral].cold.5
+ -[WPDConnection sendDataToCentral].cold.6
+ -[WPDConnection sendDataToCentral].cold.7
+ -[WPDConnection sendDataToCharacteristic:inService:forPeer:].cold.5
+ -[WPDConnection sendDataToCharacteristic:inService:forPeer:].cold.6
+ -[WPDConnection sendDataToCharacteristic:inService:forPeer:].cold.7
+ -[WPDConnection sendDataToCharacteristic:inService:forPeer:].cold.8
+ -[WPDConnection sendDataToCharacteristic:inService:forPeer:].cold.9
+ -[WPDConnection sendDataToPeripheral].cold.5
+ -[WPDConnection sendDataToPeripheral].cold.6
+ -[WPDConnection sendDataToPeripheral].cold.7
+ -[WPDConnection sendDataToPeripheral].cold.8
+ -[WPDConnection sendDataToPeripheral].cold.9
+ -[WPDConnection subscribe:toPeer:withCharacteristic:inService:].cold.1
+ -[WPDManager cbManagerDidUpdateState:].cold.2
+ -[WPDManager cleanup].cold.1
+ -[WPDManager generateStateDump].cold.1
+ -[WPDManager updateState:Restricted:].cold.1
+ -[WPDManager update].cold.2
+ -[WPDObjectDiscoveryClient completeSPBeaconingWithSuccess:].cold.2
+ -[WPDObjectDiscoveryClient dealloc].cold.1
+ -[WPDObjectDiscoveryClient destroy].cold.1
+ -[WPDObjectDiscoveryClient endTestMode].cold.1
+ -[WPDObjectDiscoveryClient generateStateDump].cold.1
+ -[WPDObjectDiscoveryClient generateStateDump].cold.2
+ -[WPDObjectDiscoveryClient initWithXPCConnection:server:].cold.1
+ -[WPDObjectDiscoveryClient notifyClientObjectDiscoveryStateChange:].cold.2
+ -[WPDObjectDiscoveryClient sendTestRequest:].cold.4
+ -[WPDObjectDiscoveryClient sendTestRequest:].cold.5
+ -[WPDObjectDiscoveryClient sendTestRequest:].cold.6
+ -[WPDObjectDiscoveryClient startAdvertising:].cold.10
+ -[WPDObjectDiscoveryClient startAdvertising:].cold.11
+ -[WPDObjectDiscoveryClient startAdvertising:].cold.6
+ -[WPDObjectDiscoveryClient startAdvertising:].cold.7
+ -[WPDObjectDiscoveryClient startAdvertising:].cold.8
+ -[WPDObjectDiscoveryClient startAdvertising:].cold.9
+ -[WPDObjectDiscoveryClient startSPBeaconing].cold.3
+ -[WPDObjectDiscoveryClient startSPBeaconing].cold.4
+ -[WPDObjectDiscoveryClient stopAdvertising:].cold.5
+ -[WPDObjectDiscoveryClient stopAdvertising:].cold.6
+ -[WPDObjectDiscoveryClient stopAdvertising:].cold.7
+ -[WPDObjectDiscoveryClient stopAdvertising:].cold.8
+ -[WPDObjectDiscoveryClient stopAdvertising:].cold.9
+ -[WPDObjectDiscoveryClient updateSPBeaconing].cold.2
+ -[WPDObjectDiscoveryClient updateSPBeaconing].cold.3
+ -[WPDObjectDiscoveryClient updateSPNearbyTokens].cold.2
+ -[WPDObjectDiscoveryManager addAdvertisingRequest:forClient:].cold.2
+ -[WPDObjectDiscoveryManager advertOptionsChanged:].cold.2
+ -[WPDObjectDiscoveryManager advertOptionsChanged:].cold.3
+ -[WPDObjectDiscoveryManager advertOptionsChanged:].cold.4
+ -[WPDObjectDiscoveryManager peripheralManager:didStopAdvertisingWithError:].cold.2
+ -[WPDObjectDiscoveryManager peripheralManager:didStopAdvertisingWithError:].cold.3
+ -[WPDObjectDiscoveryManager peripheralManager:didStopAdvertisingWithError:].cold.4
+ -[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:].cold.4
+ -[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:].cold.5
+ -[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:].cold.6
+ -[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:].cold.7
+ -[WPDObjectDiscoveryManager removeAdvertisingRequest:forClient:].cold.2
+ -[WPDObjectDiscoveryManager removeAdvertisingRequestsForClient:].cold.2
+ -[WPDObjectDiscoveryManager resetAdvertiser].cold.1
+ -[WPDObjectDiscoveryManager startAdvertiser].cold.1
+ -[WPDObjectDiscoveryManager stopAdvertiser].cold.1
+ -[WPDObjectDiscoveryManager updateAdvertiser].cold.3
+ -[WPDObjectDiscoveryManager updateAdvertiser].cold.4
+ -[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:].cold.2
+ -[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:].cold.3
+ -[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:].cold.4
+ -[WPDObjectDiscoveryManager update].cold.2
+ -[WPDObjectDiscoveryManager update].cold.3
+ -[WPDObjectDiscoveryManager update].cold.4
+ -[WPDObjectDiscoveryManager update].cold.5
+ -[WPDObjectDiscoveryManager update].cold.6
+ -[WPDPendingCompletions addCompletion:].cold.2
+ -[WPDPendingCompletions addCompletion:].cold.3
+ -[WPDPendingCompletions completeID:success:].cold.2
+ -[WPDPendingCompletions completeID:success:].cold.3
+ -[WPDPendingCompletions completeID:success:].cold.4
+ -[WPDPersistence deletePropertyValue:].cold.2
+ -[WPDPersistence firstUnlockedWithEvent:].cold.3
+ -[WPDPersistence firstUnlockedWithEvent:].cold.4
+ -[WPDPersistence init].cold.1
+ -[WPDPersistence readBoolPropertyValue:].cold.1
+ -[WPDPersistence readStringPropertyValue:].cold.2
+ -[WPDPersistence synchronisePrefs].cold.2
+ -[WPDPersistence writeBoolProperty:Value:].cold.2
+ -[WPDPersistence writeStringProperty:Value:].cold.2
+ -[WPDPipeManager channelHasData:].cold.3
+ -[WPDPipeManager channelHasData:].cold.4
+ -[WPDPipeManager channelHasData:].cold.5
+ -[WPDPipeManager channelHasData:].cold.6
+ -[WPDPipeManager channelHasData:].cold.7
+ -[WPDPipeManager handleIncomingPipeData:data:dataSize:].cold.2
+ -[WPDPipeManager handleIncomingPipeData:data:dataSize:].cold.3
+ -[WPDPipeManager handleIncomingPipeData:data:dataSize:].cold.4
+ -[WPDPipeManager handleIncomingPipeData:data:dataSize:].cold.5
+ -[WPDPipeManager handleIncomingPipeData:data:dataSize:].cold.6
+ -[WPDPipeManager invalidatePipeInfo:forPeer:].cold.3
+ -[WPDPipeManager invalidatePipeInfo:forPeer:].cold.4
+ -[WPDPipeManager invalidatePipeInfo:forPeer:].cold.5
+ -[WPDPipeManager pipeInfo:forClient:].cold.2
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.10
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.11
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.12
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.13
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.14
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.15
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.6
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.7
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.8
+ -[WPDPipeManager receivedAck:data:dataSize:].cold.9
+ -[WPDPipeManager receivedConnectStatus:data:dataSize:].cold.1
+ -[WPDPipeManager receivedError:data:dataSize:].cold.4
+ -[WPDPipeManager receivedError:data:dataSize:].cold.5
+ -[WPDPipeManager receivedError:data:dataSize:].cold.6
+ -[WPDPipeManager receivedError:data:dataSize:].cold.7
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.10
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.11
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.12
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.13
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.14
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.15
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.16
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.17
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.18
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.19
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.5
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.6
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.7
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.8
+ -[WPDPipeManager receivedPayload:data:dataSize:].cold.9
+ -[WPDPipeManager receivedVersionInfo:data:dataSize:].cold.1
+ -[WPDPipeManager receivedVersionInfo:data:dataSize:].cold.2
+ -[WPDPipeManager receivedVersionInfo:data:dataSize:].cold.3
+ -[WPDPipeManager receivedVersionInfo:data:dataSize:].cold.4
+ -[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:].cold.1
+ -[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:].cold.2
+ -[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:].cold.3
+ -[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:].cold.4
+ -[WPDPipeManager scalablePipeManager:didRegisterEndpoint:error:].cold.1
+ -[WPDPipeManager scalablePipeManager:didUnregisterEndpoint:].cold.1
+ -[WPDPipeManager scalablePipeManager:pipeDidConnect:].cold.1
+ -[WPDPipeManager scalablePipeManager:pipeDidConnect:].cold.2
+ -[WPDPipeManager scalablePipeManager:pipeDidConnect:].cold.3
+ -[WPDPipeManager scalablePipeManager:pipeDidConnect:].cold.4
+ -[WPDPipeManager scalablePipeManager:pipeDidConnect:].cold.5
+ -[WPDPipeManager scalablePipeManager:pipeDidDisconnect:error:].cold.3
+ -[WPDPipeManager scalablePipeManager:pipeDidDisconnect:error:].cold.4
+ -[WPDPipeManager scalablePipeManager:pipeDidDisconnect:error:].cold.5
+ -[WPDPipeManager sendAck:errorCode:].cold.4
+ -[WPDPipeManager sendAck:errorCode:].cold.5
+ -[WPDPipeManager sendAck:errorCode:].cold.6
+ -[WPDPipeManager sendChannelData:].cold.3
+ -[WPDPipeManager sendChannelData:].cold.4
+ -[WPDPipeManager sendChannelData:].cold.5
+ -[WPDPipeManager sendChannelData:].cold.6
+ -[WPDPipeManager sendChannelData:].cold.7
+ -[WPDPipeManager sendChannelData:].cold.8
+ -[WPDPipeManager sendConnectStatus:connectStatus:].cold.1
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.10
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.11
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.12
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.13
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.14
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.15
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.16
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.17
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.18
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.19
+ -[WPDPipeManager sendData:forPeer:forClient:].cold.9
+ -[WPDPipeManager sendErrorResponse:errorCode:].cold.1
+ -[WPDPipeManager sendRemainingData:wpClient:].cold.2
+ -[WPDPipeManager sendRemainingData:wpClient:].cold.3
+ -[WPDPipeManager sendRemainingData:wpClient:].cold.4
+ -[WPDPipeManager sendRemainingData:wpClient:].cold.5
+ -[WPDPipeManager sendRemainingData:wpClient:].cold.6
+ -[WPDPipeManager sendVersionInfo:].cold.1
+ -[WPDPipeManager setConnectionInitiator:forPeer:forClient:].cold.1
+ -[WPDPipeManager setConnectionInitiator:forPeer:forClient:].cold.2
+ -[WPDPipeManager setConnectionInitiator:forPeer:forClient:].cold.3
+ -[WPDPipeManager setConnectionInitiator:forPeer:forClient:].cold.4
+ -[WPDPipeManager setConnectionInitiator:forPeer:forClient:].cold.5
+ -[WPDPipeManager setPipeClientConnectionStatus:forPeer:forClient:].cold.1
+ -[WPDPipeManager setPipeClientConnectionStatus:forPeer:forClient:].cold.2
+ -[WPDPipeManager stream:handleEvent:].cold.10
+ -[WPDPipeManager stream:handleEvent:].cold.11
+ -[WPDPipeManager stream:handleEvent:].cold.12
+ -[WPDPipeManager stream:handleEvent:].cold.13
+ -[WPDPipeManager stream:handleEvent:].cold.14
+ -[WPDPipeManager stream:handleEvent:].cold.15
+ -[WPDPipeManager stream:handleEvent:].cold.16
+ -[WPDPipeManager stream:handleEvent:].cold.17
+ -[WPDPipeManager stream:handleEvent:].cold.18
+ -[WPDPipeManager stream:handleEvent:].cold.19
+ -[WPDPipeManager stream:handleEvent:].cold.20
+ -[WPDPipeManager stream:handleEvent:].cold.21
+ -[WPDPipeManager stream:handleEvent:].cold.22
+ -[WPDPipeManager stream:handleEvent:].cold.6
+ -[WPDPipeManager stream:handleEvent:].cold.7
+ -[WPDPipeManager stream:handleEvent:].cold.8
+ -[WPDPipeManager stream:handleEvent:].cold.9
+ -[WPDPipeManager unregisterEndpoint:forClient:].cold.1
+ -[WPDPipeManager unregisterEndpoint:forClient:].cold.2
+ -[WPDPipeManager unregisterEndpoint:forClient:].cold.3
+ -[WPDPipeManager update].cold.1
+ -[WPDPipeManager update].cold.2
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.10
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.11
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.4
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.5
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.6
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.7
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.8
+ -[WPDPipeManager writeDataToPipe:pipe:].cold.9
+ -[WPDScanManager addPeerTrackingRequest:forClient:].cold.4
+ -[WPDScanManager addPeerTrackingRequest:forClient:].cold.5
+ -[WPDScanManager addPeerTrackingRequest:forClient:].cold.6
+ -[WPDScanManager addPeerTrackingRequest:forClient:].cold.7
+ -[WPDScanManager addPeerTrackingRequest:forClient:].cold.8
+ -[WPDScanManager addPeerTrackingRequest:forClient:].cold.9
+ -[WPDScanManager addScanRequest:forClient:].cold.2
+ -[WPDScanManager addScanRequest:forClient:].cold.3
+ -[WPDScanManager addScanRequest:forClient:].cold.4
+ -[WPDScanManager addScanRequest:forClient:].cold.5
+ -[WPDScanManager addSpyScanClient:].cold.1
+ -[WPDScanManager addSpyScanClient:].cold.2
+ -[WPDScanManager assertCBDiscoveryScan:].cold.3
+ -[WPDScanManager assertCBDiscoveryScan:].cold.4
+ -[WPDScanManager assertCBDiscoveryScan:].cold.5
+ -[WPDScanManager centralManager:didConnectPeripheral:].cold.1
+ -[WPDScanManager centralManager:didConnectPeripheral:].cold.2
+ -[WPDScanManager centralManager:didDisconnectPeripheral:error:].cold.1
+ -[WPDScanManager centralManager:didDiscoverMultiplePeripherals:].cold.2
+ -[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.2
+ -[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.3
+ -[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.4
+ -[WPDScanManager centralManager:didFailToConnectPeripheral:error:].cold.2
+ -[WPDScanManager centralManager:didFailToScanWithError:].cold.1
+ -[WPDScanManager centralManager:didFailToScanWithError:].cold.2
+ -[WPDScanManager centralManager:didFindPeripheral:forType:].cold.1
+ -[WPDScanManager centralManager:didLosePeripheral:forType:].cold.1
+ -[WPDScanManager clearDuplicateFilterCache:forClient:].cold.2
+ -[WPDScanManager clearDuplicateFilterCache:forClient:].cold.3
+ -[WPDScanManager clearDuplicateFilterCache:forClient:].cold.4
+ -[WPDScanManager connectToPeripheral:fromClient:withOptions:].cold.4
+ -[WPDScanManager connectToPeripheral:fromClient:withOptions:].cold.5
+ -[WPDScanManager connectToPeripheral:fromClient:withOptions:].cold.6
+ -[WPDScanManager connectToPeripheral:fromClient:withOptions:].cold.7
+ -[WPDScanManager disconnectFromCentral:forClient:].cold.1
+ -[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:].cold.2
+ -[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:].cold.3
+ -[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:].cold.4
+ -[WPDScanManager enableRanging:].cold.2
+ -[WPDScanManager heySiriScanActive:].cold.2
+ -[WPDScanManager heySiriScanActive:].cold.3
+ -[WPDScanManager isScannerTestMode].cold.2
+ -[WPDScanManager logScanRequests:method:window:interval:].cold.1
+ -[WPDScanManager logScanTypes:method:window:interval:].cold.1
+ -[WPDScanManager reconcileScanRule:withRule:].cold.3
+ -[WPDScanManager reconcileScanRule:withRule:].cold.4
+ -[WPDScanManager removeAllPeerTrackingRequestsForClient:].cold.1
+ -[WPDScanManager removeConflictingRequest:forClient:].cold.1
+ -[WPDScanManager removeConflictingRequest:forClient:].cold.2
+ -[WPDScanManager removeConflictingRequest:forClient:].cold.3
+ -[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:].cold.3
+ -[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:].cold.4
+ -[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:].cold.5
+ -[WPDScanManager removePeripheralConnection:forClient:].cold.1
+ -[WPDScanManager removeScanRequest:forClient:].cold.2
+ -[WPDScanManager removeScanRequest:forClient:].cold.3
+ -[WPDScanManager removeScanRequest:forClient:].cold.4
+ -[WPDScanManager removeScanRequestsForClient:].cold.1
+ -[WPDScanManager removeSpyScanClient:].cold.1
+ -[WPDScanManager removeSpyScanClient:].cold.2
+ -[WPDScanManager retrievePeripheralWithUUID:].cold.2
+ -[WPDScanManager scanOptionsChanged:ForRequests:].cold.2
+ -[WPDScanManager scanOptionsChanged:ForRequests:].cold.3
+ -[WPDScanManager scanOptionsChanged:ForRequests:].cold.4
+ -[WPDScanManager scanOptionsChanged:ForRequests:].cold.5
+ -[WPDScanManager scanOptionsChanged:ForRequests:].cold.6
+ -[WPDScanManager scanOptionsChanged:ForRequests:].cold.7
+ -[WPDScanManager startTrackingPeripheral:ofType:].cold.3
+ -[WPDScanManager startTrackingPeripheral:ofType:].cold.4
+ -[WPDScanManager stopTrackingPeripheral:ofType:].cold.2
+ -[WPDScanManager updateScanRules].cold.1
+ -[WPDScanManager updateScanRules].cold.10
+ -[WPDScanManager updateScanRules].cold.11
+ -[WPDScanManager updateScanRules].cold.12
+ -[WPDScanManager updateScanRules].cold.13
+ -[WPDScanManager updateScanRules].cold.14
+ -[WPDScanManager updateScanRules].cold.15
+ -[WPDScanManager updateScanRules].cold.2
+ -[WPDScanManager updateScanRules].cold.3
+ -[WPDScanManager updateScanRules].cold.4
+ -[WPDScanManager updateScanRules].cold.5
+ -[WPDScanManager updateScanRules].cold.6
+ -[WPDScanManager updateScanRules].cold.7
+ -[WPDScanManager updateScanRules].cold.8
+ -[WPDScanManager updateScanRules].cold.9
+ -[WPDScanManager updateScanner].cold.1
+ -[WPDScanManager updateScanner].cold.2
+ -[WPDScanManager update].cold.1
+ -[WPDScanManager update].cold.2
+ -[WPDScanManager update].cold.3
+ -[WPDScanManager update].cold.4
+ -[WPDScanManager update].cold.5
+ -[WPDSearchPartyAgent generateStateDump].cold.1
+ -[WPDSearchPartyAgent generateStateDump].cold.2
+ -[WPDSearchPartyAgent generateStateDump].cold.3
+ -[WPDSearchPartyAgent generateStateDump].cold.4
+ -[WPDSearchPartyAgent generateStateDump].cold.5
+ -[WPDSearchPartyAgent generateStateDump].cold.6
+ -[WPDSearchPartyAgent generateStateDump].cold.7
+ -[WPDSearchPartyAgent generateStateDump].cold.8
+ -[WPDSearchPartyAgent generateStateDump].cold.9
+ -[WPDSearchPartyAgent initSPObjects].cold.2
+ -[WPDSearchPartyAgent initSPObjects].cold.3
+ -[WPDSearchPartyAgent initWithQueue:beaconChange:tokensChange:].cold.2
+ -[WPDSearchPartyAgent initWithQueue:beaconChange:tokensChange:].cold.3
+ -[WPDSearchPartyAgent rollKeysWithRequestID:].cold.3
+ -[WPDSearchPartyAgent rollKeysWithRequestID:].cold.4
+ -[WPDSearchPartyAgent rollKeysWithRequestID:].cold.5
+ -[WPDSearchPartyAgent rollKeysWithRequestID:].cold.6
+ -[WPDSearchPartyAgent rollKeysWithRequestID:].cold.7
+ -[WPDSearchPartyAgent rollTokensWithRequestID:].cold.1
+ -[WPDSearchPartyAgent startTest].cold.2
+ -[WPDSearchPartyAgent stopTest].cold.2
+ -[WPDSearchPartyAgent updateTestBeaconExtended:].cold.2
+ -[WPDSearchPartyAgent updateTestBeaconKeys:].cold.2
+ -[WPDSearchPartyAgent updateTestBeaconState:].cold.2
+ -[WPDSearchPartyAgent updateTestBeaconStatus:].cold.2
+ -[WPDSearchPartyAgent updateTestNearOwnerTokens:].cold.2
+ -[WPDState coalesceState:Restricted:UpdateCache:].cold.1
+ -[WPDState registerManager:].cold.2
+ -[WPDState updateWithCompletion:].cold.2
+ -[WPDState updateWithManager:Completion:].cold.3
+ -[WPDState updateWithManager:Completion:].cold.4
+ -[WPDState updateWithManager:Completion:].cold.5
+ -[WPDStatsManager generateStateDump].cold.1
+ -[WPDStatsManager startActivity:forType:scanRate:].cold.2
+ -[WPDZoneManager addSingleZoneTrackingRequest:forClient:].cold.1
+ -[WPDZoneManager addSingleZoneTrackingRequest:forClient:].cold.2
+ -[WPDZoneManager addSingleZoneTrackingRequest:forClient:].cold.3
+ -[WPDZoneManager addZoneTrackingRequest:forClient:].cold.2
+ -[WPDZoneManager addZoneTrackingRequest:forClient:].cold.3
+ -[WPDZoneManager addZoneTrackingRequest:forClient:].cold.4
+ -[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.1
+ -[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.2
+ -[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.3
+ -[WPDZoneManager centralManager:didLoseZone:mask:].cold.2
+ -[WPDZoneManager exitTimerFired].cold.2
+ -[WPDZoneManager initWithServer:].cold.2
+ -[WPDZoneManager startExitTimer].cold.2
+ -[WPDZoneManager startExitTimer].cold.3
+ -[WPDZoneManager unregisterAllZones].cold.2
+ -[WPDZoneManager unregisterZones:forClient:].cold.1
+ -[WPDZoneManager unregisterZones:forClient:].cold.2
+ -[WPDZoneManager unregisterZones:forClient:].cold.3
+ -[WPDZoneManager unregisterZones:forClient:].cold.4
+ -[WPDZoneManager unregisterZonesForClient:updateScanner:].cold.3
+ -[WPDZoneManager unregisterZonesForClient:updateScanner:].cold.4
+ -[WPDZoneManager unregisterZonesForClient:updateScanner:].cold.5
+ -[WPDZoneManager unregisterZonesForClient:updateScanner:].cold.6
+ -[WPDZoneManager updateScanner].cold.2
+ -[WPDZoneManager updateScanner].cold.3
+ -[WPDZoneManager updateScanner].cold.4
+ -[WPDZoneManager updateScanner].cold.5
+ -[WPDZoneManager updateScanner].cold.6
+ -[WPDZoneManager updateScanner].cold.7
+ -[WPDZoneManager update].cold.1
+ -[WPDZoneManager update].cold.2
+ -[WPDZoneManager update].cold.3
+ -[WPDaemonServer addClient:].cold.3
+ -[WPDaemonServer addClient:].cold.4
+ -[WPDaemonServer addClient:].cold.5
+ -[WPDaemonServer dumpDaemonStateAsync].cold.1
+ -[WPDaemonServer dumpDaemonStateAsync].cold.2
+ -[WPDaemonServer dumpDaemonState].cold.1
+ -[WPDaemonServer enableRanging:].cold.2
+ -[WPDaemonServer enableTestMode:].cold.1
+ -[WPDaemonServer generateStateDump].cold.1
+ -[WPDaemonServer generateStateDump].cold.2
+ -[WPDaemonServer generateStateDump].cold.3
+ -[WPDaemonServer generateStateDump].cold.4
+ -[WPDaemonServer generateStateDump].cold.5
+ -[WPDaemonServer generateStateDump].cold.6
+ -[WPDaemonServer generateStateDump].cold.7
+ -[WPDaemonServer generateStateDump].cold.8
+ -[WPDaemonServer generateStateDump].cold.9
+ -[WPDaemonServer getClientForUUID:].cold.1
+ -[WPDaemonServer initClients].cold.1
+ -[WPDaemonServer init].cold.4
+ -[WPDaemonServer init].cold.5
+ -[WPDaemonServer init].cold.6
+ -[WPDaemonServer init].cold.7
+ -[WPDaemonServer removeClient:].cold.4
+ -[WPDaemonServer removeClient:].cold.5
+ -[WPDaemonServer removeClient:].cold.6
+ -[WPDaemonServer removeClient:].cold.7
+ -[WPDaemonServer removeClient:].cold.8
+ -[WPScanRequest requestedAtNsec]
+ -[WPScanRequest setRequestedAtNsec:]
+ GCC_except_table10
+ GCC_except_table101
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table143
+ GCC_except_table152
+ GCC_except_table173
+ GCC_except_table180
+ GCC_except_table184
+ GCC_except_table245
+ GCC_except_table248
+ GCC_except_table278
+ GCC_except_table375
+ GCC_except_table409
+ GCC_except_table418
+ GCC_except_table425
+ GCC_except_table446
+ GCC_except_table448
+ GCC_except_table450
+ GCC_except_table452
+ GCC_except_table459
+ GCC_except_table466
+ GCC_except_table475
+ GCC_except_table48
+ GCC_except_table496
+ GCC_except_table570
+ GCC_except_table572
+ GCC_except_table574
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table90
+ GCC_except_table92
+ OBJC_IVAR_$_WPScanRequest._requestedAtNsec
+ WPLoggingInit.cold.1
+ _CBCentralManagerScanOptionScanProcessedAtNsec
+ _CBCentralManagerScanOptionScanRequestedAtNsec
+ __20-[WPDClient destroy]_block_invoke.586
+ __22-[WPDaemonServer init]_block_invoke.175
+ __22-[WPDaemonServer init]_block_invoke.181
+ __22-[WPDaemonServer init]_block_invoke.181.cold.1
+ __22-[WPDaemonServer init]_block_invoke.181.cold.2
+ __22-[WPDaemonServer init]_block_invoke.186
+ __22-[WPDaemonServer init]_block_invoke.190
+ __24+[WPDManager initialize]_block_invoke.120
+ __24-[WPDConnection dealloc]_block_invoke.122
+ __24-[WPDPipeManager update]_block_invoke.773
+ __24-[WPDPipeManager update]_block_invoke.774
+ __24-[WPDScanManager update]_block_invoke.399
+ __24-[WPDScanManager update]_block_invoke.402
+ __24-[WPDScanManager update]_block_invoke.405
+ __24-[WPDScanManager update]_block_invoke.408
+ __24-[WPDZoneManager update]_block_invoke.168
+ __26-[WPDClient destroy_async]_block_invoke.593
+ __26-[WPDClient stopScanning:]_block_invoke.765
+ __27-[WPDClient tickleMachPort]_block_invoke.567
+ __28-[WPDClient setupConnection]_block_invoke.577
+ __28-[WPDClient setupConnection]_block_invoke.577.cold.1
+ __28-[WPDClient setupConnection]_block_invoke.cold.1
+ __28-[WPDClient setupConnection]_block_invoke_2.578
+ __28-[WPDaemonServer addClient:]_block_invoke.237
+ __28-[WPDaemonServer addClient:]_block_invoke.238
+ __29-[WPDClient sendTestRequest:]_block_invoke.987
+ __29-[WPDaemonServer initClients]_block_invoke.215
+ __29-[WPDaemonServer updateState]_block_invoke.225
+ __29-[WPDaemonServer updateState]_block_invoke.cold.2
+ __29-[WPDaemonServer updateState]_block_invoke.cold.3
+ __29-[WPDaemonServer updateState]_block_invoke.cold.4
+ __30+[WPDClient generateStateDump]_block_invoke.465
+ __30-[WPDClient discoveredDevice:]_block_invoke.cold.1
+ __30-[WPDClient startAdvertising:]_block_invoke.613
+ __30-[WPDaemonServer initManagers]_block_invoke.203
+ __30-[WPDaemonServer initManagers]_block_invoke.203.cold.1
+ __30-[WPDaemonServer initManagers]_block_invoke.203.cold.2
+ __31-[WPDAdvertisingManager update]_block_invoke.410
+ __31-[WPDAdvertisingManager update]_block_invoke.413
+ __31-[WPDClient createdConnection:]_block_invoke.880
+ __31-[WPDClient discoveredDevices:]_block_invoke_2.cold.1
+ __31-[WPDScanManager updateScanner]_block_invoke.413
+ __31-[WPDZoneManager updateScanner]_block_invoke.229
+ __31-[WPDZoneManager updateScanner]_block_invoke.233
+ __31-[WPDaemonServer removeClient:]_block_invoke.246
+ __32-[WPDClient disconnectFromPeer:]_block_invoke.853
+ __32-[WPDClient stopScanning_async:]_block_invoke.768
+ __32-[WPDZoneManager exitTimerFired]_block_invoke.244
+ __32-[WPDZoneManager exitTimerFired]_block_invoke.244.cold.1
+ __32-[WPDZoneManager startExitTimer]_block_invoke.239
+ __32-[WPDaemonServer startListening]_block_invoke.cold.1
+ __33-[WPDClient anyDiscoveredDevice:]_block_invoke.cold.1
+ __33-[WPDClient startScanning_async:]_block_invoke.744.cold.1
+ __33-[WPDClient startScanning_async:]_block_invoke.744.cold.2
+ __33-[WPDClient startScanning_async:]_block_invoke.750.cold.1
+ __33-[WPDClient startScanning_async:]_block_invoke.750.cold.2
+ __33-[WPDClient startScanning_async:]_block_invoke.750.cold.3
+ __33-[WPDClient startScanning_async:]_block_invoke.754
+ __33-[WPDClient startScanning_async:]_block_invoke_2.751
+ __33-[WPDPipeManager channelHasData:]_block_invoke.827
+ __33-[WPDPipeManager channelHasData:]_block_invoke.831
+ __33-[WPDPipeManager channelHasData:]_block_invoke_2.828
+ __33-[WPDScanManager updateScanRules]_block_invoke.289
+ __33-[WPDScanManager updateScanRules]_block_invoke.294
+ __33-[WPDScanManager updateScanRules]_block_invoke.303
+ __33-[WPDScanManager updateScanRules]_block_invoke.305
+ __33-[WPDScanManager updateScanRules]_block_invoke.315
+ __33-[WPDScanManager updateScanRules]_block_invoke.317
+ __33-[WPDScanManager updateScanRules]_block_invoke_2.316
+ __33-[WPDScanManager updateScanRules]_block_invoke_2.318
+ __33-[WPDScanManager updateScanRules]_block_invoke_3.319
+ __34-[WPDClient verifyApprovedUseCase]_block_invoke.460
+ __34-[WPDConnection sendDataToCentral]_block_invoke.245
+ __34-[WPDPipeManager sendChannelData:]_block_invoke.816
+ __35-[WPDObjectDiscoveryManager update]_block_invoke.154
+ __35-[WPDScanManager addSpyScanClient:]_block_invoke.165
+ __35-[WPDScanManager isScannerTestMode]_block_invoke.235
+ __35-[WPDZoneManager printTrackedZones]_block_invoke.cold.2
+ __35-[WPDaemonServer generateStateDump]_block_invoke.283
+ __35-[WPDaemonServer generateStateDump]_block_invoke.293
+ __35-[WPDaemonServer generateStateDump]_block_invoke.298
+ __35-[WPDaemonServer generateStateDump]_block_invoke.301
+ __35-[WPDaemonServer generateStateDump]_block_invoke.304
+ __35-[WPDaemonServer generateStateDump]_block_invoke.307
+ __35-[WPDaemonServer getClientForUUID:]_block_invoke.222
+ __36-[WPDClient disconnectedPeer:error:]_block_invoke.867
+ __36-[WPDClient disconnectedPeer:error:]_block_invoke.873
+ __36-[WPDClient startAdvertising_async:]_block_invoke.616
+ __36-[WPDClient startAdvertising_async:]_block_invoke.626.cold.1
+ __36-[WPDClient startAdvertising_async:]_block_invoke.626.cold.2
+ __36-[WPDClient startAdvertising_async:]_block_invoke.632.cold.1
+ __36-[WPDClient startAdvertising_async:]_block_invoke.632.cold.2
+ __36-[WPDClient startAdvertising_async:]_block_invoke.632.cold.3
+ __36-[WPDPipeManager sendAck:errorCode:]_block_invoke.703
+ __36-[WPDScanManager heySiriScanActive:]_block_invoke.246
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.226
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.226.cold.1
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.226.cold.2
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.226.cold.3
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.230
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.236
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.236.cold.1
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.243
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.243.cold.1
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.243.cold.2
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.243.cold.3
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.247
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.251
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.258
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.cold.1
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.227
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.237
+ __36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.244
+ __36-[WPDaemonServer SetupSignalHandler]_block_invoke.161
+ __36-[WPDaemonServer SetupSignalHandler]_block_invoke.cold.1
+ __36-[WPDaemonServer SetupSignalHandler]_block_invoke.cold.2
+ __37-[WPDConnection sendDataToPeripheral]_block_invoke.265
+ __37-[WPDPipeManager pipeInfo:forClient:]_block_invoke.495
+ __37-[WPDPipeManager stream:handleEvent:]_block_invoke.559
+ __37-[WPDPipeManager stream:handleEvent:]_block_invoke.569
+ __37-[WPDPipeManager stream:handleEvent:]_block_invoke_2.560
+ __38-[WPDScanManager removeSpyScanClient:]_block_invoke.170
+ __38-[WPDaemonServer dumpDaemonStateAsync]_block_invoke.314
+ __39-[WPDClient connectToPeer:withOptions:]_block_invoke.814
+ __39-[WPDClient connectedDeviceOverLEPipe:]_block_invoke.845
+ __39-[WPDPendingCompletions addCompletion:]_block_invoke.126
+ __39-[WPDPipeManager writeDataToPipe:pipe:]_block_invoke.747
+ __40-[WPDAdvertisingManager initWithServer:]_block_invoke.199
+ __40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.225
+ __40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.232
+ __40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.cold.2
+ __40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.cold.3
+ __40-[WPDSearchPartyAgent generateStateDump]_block_invoke.215
+ __41-[WPDAdvertisingManager advertisingRules]_block_invoke.356
+ __41-[WPDAdvertisingManager advertisingRules]_block_invoke.359
+ __41-[WPDAdvertisingManager advertisingRules]_block_invoke.371
+ __41-[WPDAdvertisingManager advertisingRules]_block_invoke.375
+ __41-[WPDAdvertisingManager advertisingRules]_block_invoke.378
+ __41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.336
+ __41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.339
+ __41-[WPDState updateWithManager:Completion:]_block_invoke.128
+ __41-[WPDState updateWithManager:Completion:]_block_invoke.133
+ __42-[PipeDataTransfer generateSequenceNumber]_block_invoke.143
+ __42-[WPDClient initWithXPCConnection:server:]_block_invoke.480
+ __42-[WPDClient initWithXPCConnection:server:]_block_invoke.486
+ __42-[WPDClient initWithXPCConnection:server:]_block_invoke.486.cold.1
+ __42-[WPDClient initWithXPCConnection:server:]_block_invoke.486.cold.2
+ __42-[WPDScanManager clearExistingConnections]_block_invoke.392
+ __42-[WPDScanManager clearExistingConnections]_block_invoke.cold.3
+ __42-[WPDScanManager clearExistingConnections]_block_invoke.cold.4
+ __43-[WPDScanManager addScanRequest:forClient:]_block_invoke.197
+ __43-[WPDScanManager addScanRequest:forClient:]_block_invoke.201
+ __44-[WPDAdvertisingData addAdvertisingRequest:]_block_invoke.125
+ __44-[WPDObjectDiscoveryClient sendTestRequest:]_block_invoke.249
+ __44-[WPDObjectDiscoveryClient startSPBeaconing]_block_invoke.191
+ __44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.227
+ __44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.236
+ __44-[WPDPendingCompletions completeID:success:]_block_invoke.137
+ __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.662
+ __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.668
+ __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.675
+ __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke_2.669
+ __44-[WPDSearchPartyAgent updateTestBeaconKeys:]_block_invoke.293
+ __44-[WPDZoneManager unregisterZones:forClient:]_block_invoke.282
+ __44-[WPDaemonServer notifyClientsOfStateChange]_block_invoke_2.cold.2
+ __45-[WPDAdvertisingManager heySiriAdvertActive:]_block_invoke.393
+ __45-[WPDAdvertisingManager isAdvertiserTestMode]_block_invoke.382
+ __45-[WPDClient clearDuplicateFilterCache_async:]_block_invoke.782
+ __45-[WPDObjectDiscoveryClient generateStateDump]_block_invoke.165
+ __45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.200
+ __45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.207
+ __45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.219
+ __45-[WPDObjectDiscoveryClient updateSPBeaconing]_block_invoke.185
+ __45-[WPDObjectDiscoveryManager updateAdvertiser]_block_invoke.198
+ __45-[WPDPipeManager invalidatePipeInfo:forPeer:]_block_invoke.847
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.434
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.438
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.444
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.448
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.458
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.462
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.469
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.470
+ __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.466
+ __45-[WPDPipeManager sendRemainingData:wpClient:]_block_invoke.726
+ __45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.251
+ __45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.251.cold.1
+ __45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.251.cold.2
+ __45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.256
+ __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.263.cold.1
+ __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.263.cold.2
+ __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.263.cold.3
+ __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.263.cold.4
+ __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.266
+ __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.279
+ __46+[WPDSearchPartyAgent spBeaconKeyFromTestKey:]_block_invoke.319
+ __46-[WPDConnection peripheral:didModifyServices:]_block_invoke.199
+ __46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.683
+ __46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.692
+ __46-[WPDScanManager removeScanRequest:forClient:]_block_invoke.212
+ __47-[WPDPipeManager unregisterEndpoint:forClient:]_block_invoke.420
+ __48-[WPDAdvertisingManager removeServiceForClient:]_block_invoke.289
+ __48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.152
+ __48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.160
+ __48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.160.cold.1
+ __48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.160.cold.2
+ __48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.632
+ __48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.632.cold.1
+ __48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.642
+ __48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke_2.633
+ __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.335
+ __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.338
+ __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.341
+ __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.344
+ __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.347
+ __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.350
+ __49-[WPDScanManager startTrackingPeripheral:ofType:]_block_invoke.513
+ __49-[WPDState coalesceState:Restricted:UpdateCache:]_block_invoke.139
+ __50-[WPDObjectDiscoveryManager advertOptionsChanged:]_block_invoke.162
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.1
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.2
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.3
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.4
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.5
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.6
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.7
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.8
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.193.cold.9
+ __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.205
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.471
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.477
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.480
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.483
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.489
+ __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.264
+ __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.271
+ __52-[WPDPipeManager receivedVersionInfo:data:dataSize:]_block_invoke.594
+ __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.783
+ __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.783.cold.1
+ __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.783.cold.2
+ __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.795
+ __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.799
+ __53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.175
+ __53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.185
+ __53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke_2.cold.1
+ __54-[WPDAdvertisingManager heySiriAdvertActiveAllDevices]_block_invoke.398
+ __54-[WPDClient connectedDevice:withError:shouldDiscover:]_block_invoke.834
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.560
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.1
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.10
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.2
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.3
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.4
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.5
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.6
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.7
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.8
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563.cold.9
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.566
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.569
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.572
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.575
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.578
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.581
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.584
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.588
+ __54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.379
+ __54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.382
+ __54-[WPDScanManager logScanTypes:method:window:interval:]_block_invoke.374
+ __55-[WPDPipeManager handleIncomingPipeData:data:dataSize:]_block_invoke.583
+ __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.600
+ __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.600.cold.1
+ __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.600.cold.2
+ __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.603
+ __56-[WPDClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.924
+ __56-[WPDScanManager centralManager:didFailToScanWithError:]_block_invoke.460
+ __57-[WPDAdvertisingManager addAdvertisingRequest:forClient:]_block_invoke.308
+ __57-[WPDAdvertisingManager informClientsAdvertisingPending:]_block_invoke.401
+ __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.152
+ __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.152.cold.1
+ __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.152.cold.2
+ __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.156
+ __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.cold.2
+ __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke_2.153
+ __57-[WPDScanManager logScanRequests:method:window:interval:]_block_invoke.368
+ __57-[WPDScanManager removeAllPeerTrackingRequestsForClient:]_block_invoke.505
+ __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.251
+ __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.255
+ __57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.290.cold.1
+ __57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.296
+ __59-[WPDClient central:subscribed:toCharacteristic:inService:]_block_invoke.903
+ __59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.480
+ __59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.490
+ __59-[WPDScanManager centralManager:didFindPeripheral:forType:]_block_invoke.529
+ __59-[WPDScanManager centralManager:didLosePeripheral:forType:]_block_invoke.524
+ __60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.224
+ __60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.230
+ __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.150
+ __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.160
+ __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.532
+ __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.535
+ __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.539
+ __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.545
+ __61-[WPDaemonServer registerClient:withMachName:withCompletion:]_block_invoke.cold.1
+ __62-[WPDClient discoverCharacteristicsAndServices:forPeripheral:]_block_invoke.917
+ __62-[WPDPipeManager scalablePipeManager:pipeDidDisconnect:error:]_block_invoke.839
+ __63-[WPDAdvertisingManager peripheralManager:didAddService:error:]_block_invoke.294
+ __63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.169
+ __63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.178
+ __63-[WPDSearchPartyAgent initWithQueue:beaconChange:tokensChange:]_block_invoke.184
+ __63-[WPDSearchPartyAgent initWithQueue:beaconChange:tokensChange:]_block_invoke.185
+ __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.262
+ __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.272
+ __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.281
+ __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.284
+ __65-[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:]_block_invoke.518
+ __65-[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:]_block_invoke.893
+ __65-[WPDConnection peripheral:didWriteValueForCharacteristic:error:]_block_invoke.273
+ __66-[WPDConnection peripheral:didUpdateValueForCharacteristic:error:]_block_invoke.188
+ __66-[WPDPipeManager setPipeClientConnectionStatus:forPeer:forClient:]_block_invoke.475
+ __66-[WPDScanManager centralManager:didFailToConnectPeripheral:error:]_block_invoke.595
+ __67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.501
+ __67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.504
+ __67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke.278
+ __67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke.285
+ __67-[WPDObjectDiscoveryClient notifyClientObjectDiscoveryStateChange:]_block_invoke.241
+ __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.424
+ __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.424.cold.1
+ __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.427
+ __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.428
+ __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.428.cold.1
+ __69-[WPDAdvertisingManager peripheralManagerIsReadyToUpdateSubscribers:]_block_invoke.509
+ __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.437
+ __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.440
+ __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.447
+ __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.450
+ __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.455
+ __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.458
+ __71-[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke.165
+ __71-[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke.169
+ __72-[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:]_block_invoke.216
+ __73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.316
+ __73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.316.cold.1
+ __74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.405
+ __74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.412
+ __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.494
+ __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.500
+ __75-[WPDObjectDiscoveryManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.224
+ __76+[WPDManager initializeAdvDenylist:AdvAllowlist:ScanDenylist:ScanAllowlist:]_block_invoke.177
+ __78-[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:]_block_invoke.515
+ __78-[WPDConnection peripheral:didUpdateNotificationStateForCharacteristic:error:]_block_invoke.183
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.418
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.421
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.428
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.428.cold.1
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.431
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.442
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.442.cold.1
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.442.cold.2
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.442.cold.3
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.446
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.452
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.443
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.cold.1
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.cold.2
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.173
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.180
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.180.cold.1
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.180.cold.2
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.180.cold.3
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.180.cold.4
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.180.cold.5
+ __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.187
+ __79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.255
+ __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.470
+ __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.473
+ __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.477
+ __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.480
+ __81-[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.898
+ __83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.550
+ __83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.553
+ __84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.491
+ __84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.494
+ ___block_descriptor_49_e8_32w_e23_v16?0"WPScanRequest"8l
+ ___block_descriptor_49_e8_32w_e30_v16?0"WPAdvertisingRequest"8l
+ ___block_descriptor_64_e8_32s40r48r56r_e30_v32?0"WPScanRequest"8Q16^B24l
+ ___block_descriptor_65_e8_32s40s48w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48w
+ ___destroy_helper_block_e8_32s40s48w
+ ___getCombinedAllowlist_block_invoke.358
+ __block_literal_global.128
+ __block_literal_global.135
+ __block_literal_global.137
+ __block_literal_global.139
+ __block_literal_global.141
+ __block_literal_global.145
+ __block_literal_global.151
+ __block_literal_global.160
+ __block_literal_global.162
+ __block_literal_global.163
+ __block_literal_global.170
+ __block_literal_global.178
+ __block_literal_global.185
+ __block_literal_global.203
+ __block_literal_global.207
+ __block_literal_global.252
+ __block_literal_global.302
+ __block_literal_global.303
+ __block_literal_global.309
+ __block_literal_global.311
+ __block_literal_global.319
+ __block_literal_global.321
+ __block_literal_global.337
+ __block_literal_global.340
+ __block_literal_global.343
+ __block_literal_global.346
+ __block_literal_global.358
+ __block_literal_global.360
+ __block_literal_global.361
+ __block_literal_global.370
+ __block_literal_global.377
+ __block_literal_global.380
+ __block_literal_global.381
+ __block_literal_global.387
+ __block_literal_global.392
+ __block_literal_global.395
+ __block_literal_global.397
+ __block_literal_global.422
+ __block_literal_global.423
+ __block_literal_global.426
+ __block_literal_global.427
+ __block_literal_global.436
+ __block_literal_global.439
+ __block_literal_global.445
+ __block_literal_global.446
+ __block_literal_global.448
+ __block_literal_global.462
+ __block_literal_global.467
+ __block_literal_global.472
+ __block_literal_global.475
+ __block_literal_global.482
+ __block_literal_global.493
+ __block_literal_global.496
+ __block_literal_global.498
+ __block_literal_global.503
+ __block_literal_global.504
+ __block_literal_global.515
+ __block_literal_global.517
+ __block_literal_global.521
+ __block_literal_global.538
+ __block_literal_global.541
+ __block_literal_global.558
+ __block_literal_global.574
+ __block_literal_global.580
+ __block_literal_global.583
+ __block_literal_global.596
+ __block_literal_global.599
+ __block_literal_global.602
+ __block_literal_global.605
+ __block_literal_global.618
+ __block_literal_global.644
+ __block_literal_global.661
+ __block_literal_global.667
+ __block_literal_global.694
+ __block_literal_global.705
+ __block_literal_global.709
+ __block_literal_global.711
+ __block_literal_global.753
+ __block_literal_global.764
+ __block_literal_global.772
+ __block_literal_global.778
+ __block_literal_global.780
+ __block_literal_global.781
+ __block_literal_global.785
+ __block_literal_global.794
+ __block_literal_global.797
+ __block_literal_global.799
+ __block_literal_global.801
+ __block_literal_global.805
+ __block_literal_global.807
+ __block_literal_global.816
+ __block_literal_global.818
+ __block_literal_global.826
+ __block_literal_global.831
+ __block_literal_global.833
+ __block_literal_global.841
+ __block_literal_global.844
+ __block_literal_global.849
+ __block_literal_global.852
+ __block_literal_global.866
+ __block_literal_global.875
+ __block_literal_global.877
+ __block_literal_global.879
+ __block_literal_global.890
+ __block_literal_global.892
+ __block_literal_global.897
+ __block_literal_global.902
+ __block_literal_global.916
+ __block_literal_global.921
+ __block_literal_global.923
+ __block_literal_global.937
+ __block_literal_global.939
+ __block_literal_global.941
+ __block_literal_global.943
+ __block_literal_global.951
+ __block_literal_global.955
+ __block_literal_global.959
+ __block_literal_global.961
+ __block_literal_global.969
+ __block_literal_global.971
+ __block_literal_global.976
+ __block_literal_global.978
+ __block_literal_global.980
+ __block_literal_global.982
+ __block_literal_global.984
+ __block_literal_global.986
+ __block_literal_global.994
+ _getCombinedAllowlist.cold.1
+ _getCombinedAllowlist.cold.2
+ _getCombinedAllowlist.cold.3
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$requestedAtNsec
+ _objc_msgSend$setRequestedAtNsec:
+ getFirstCharacteristicForService.cold.2
+ updateScanRules.latestProcessedAtNsec
+ updateScanRules.latestRequestedAtNsec
- GCC_except_table103
- GCC_except_table105
- GCC_except_table113
- GCC_except_table118
- GCC_except_table125
- GCC_except_table128
- GCC_except_table132
- GCC_except_table145
- GCC_except_table154
- GCC_except_table182
- GCC_except_table183
- GCC_except_table247
- GCC_except_table250
- GCC_except_table280
- GCC_except_table284
- GCC_except_table342
- GCC_except_table378
- GCC_except_table382
- GCC_except_table383
- GCC_except_table385
- GCC_except_table386
- GCC_except_table393
- GCC_except_table395
- GCC_except_table396
- GCC_except_table397
- GCC_except_table398
- GCC_except_table428
- GCC_except_table429
- GCC_except_table430
- GCC_except_table80
- GCC_except_table89
- GCC_except_table91
- GCC_except_table93
- _GestaltGetDeviceClass
- _OUTLINED_FUNCTION_20
- __20-[WPDClient destroy]_block_invoke.580
- __22-[WPDaemonServer init]_block_invoke.178
- __22-[WPDaemonServer init]_block_invoke.184
- __22-[WPDaemonServer init]_block_invoke.189
- __22-[WPDaemonServer init]_block_invoke.193
- __24+[WPDManager initialize]_block_invoke.114
- __24-[WPDConnection dealloc]_block_invoke.116
- __24-[WPDPipeManager update]_block_invoke.770
- __24-[WPDPipeManager update]_block_invoke.771
- __24-[WPDScanManager update]_block_invoke.394
- __24-[WPDScanManager update]_block_invoke.397
- __24-[WPDScanManager update]_block_invoke.400
- __24-[WPDScanManager update]_block_invoke.403
- __24-[WPDZoneManager update]_block_invoke.162
- __26-[WPDClient destroy_async]_block_invoke.587
- __26-[WPDClient stopScanning:]_block_invoke.768
- __27-[WPDClient tickleMachPort]_block_invoke.564
- __28-[WPDClient setupConnection]_block_invoke.574
- __28-[WPDClient setupConnection]_block_invoke_2.575
- __28-[WPDaemonServer addClient:]_block_invoke.240
- __28-[WPDaemonServer addClient:]_block_invoke.244
- __29-[WPDClient sendTestRequest:]_block_invoke.993
- __29-[WPDaemonServer initClients]_block_invoke.218
- __29-[WPDaemonServer updateState]_block_invoke.231
- __30+[WPDClient generateStateDump]_block_invoke.462
- __30-[WPDClient startAdvertising:]_block_invoke.610
- __30-[WPDaemonServer initManagers]_block_invoke.206
- __30-[WPDaemonServer initManagers]_block_invoke.206.cold.1
- __31-[WPDAdvertisingManager update]_block_invoke.401
- __31-[WPDAdvertisingManager update]_block_invoke.404
- __31-[WPDClient createdConnection:]_block_invoke.889
- __31-[WPDScanManager updateScanner]_block_invoke.408
- __31-[WPDZoneManager updateScanner]_block_invoke.217
- __31-[WPDZoneManager updateScanner]_block_invoke.230
- __31-[WPDaemonServer removeClient:]_block_invoke.258
- __32-[WPDClient disconnectFromPeer:]_block_invoke.865
- __32-[WPDClient stopScanning_async:]_block_invoke.780
- __32-[WPDZoneManager exitTimerFired]_block_invoke.241
- __32-[WPDZoneManager startExitTimer]_block_invoke.233
- __33-[WPDClient startScanning_async:]_block_invoke.753
- __33-[WPDClient startScanning_async:]_block_invoke.760
- __33-[WPDClient startScanning_async:]_block_invoke_2.754
- __33-[WPDPipeManager channelHasData:]_block_invoke.818
- __33-[WPDPipeManager channelHasData:]_block_invoke.828
- __33-[WPDPipeManager channelHasData:]_block_invoke_2.825
- __33-[WPDScanManager updateScanRules]_block_invoke.262
- __33-[WPDScanManager updateScanRules]_block_invoke.291
- __33-[WPDScanManager updateScanRules]_block_invoke.297
- __33-[WPDScanManager updateScanRules]_block_invoke.304
- __33-[WPDScanManager updateScanRules]_block_invoke.307
- __33-[WPDScanManager updateScanRules]_block_invoke_2.313
- __33-[WPDScanManager updateScanRules]_block_invoke_3.314
- __34-[WPDClient verifyApprovedUseCase]_block_invoke.454
- __34-[WPDConnection sendDataToCentral]_block_invoke.233
- __34-[WPDPipeManager sendChannelData:]_block_invoke.801
- __35-[WPDObjectDiscoveryManager update]_block_invoke.142
- __35-[WPDScanManager addSpyScanClient:]_block_invoke.162
- __35-[WPDScanManager isScannerTestMode]_block_invoke.232
- __35-[WPDaemonServer generateStateDump]_block_invoke.292
- __35-[WPDaemonServer generateStateDump]_block_invoke.296
- __35-[WPDaemonServer generateStateDump]_block_invoke.299
- __35-[WPDaemonServer generateStateDump]_block_invoke.302
- __35-[WPDaemonServer generateStateDump]_block_invoke.305
- __35-[WPDaemonServer generateStateDump]_block_invoke.308
- __35-[WPDaemonServer getClientForUUID:]_block_invoke.225
- __36-[WPDClient disconnectedPeer:error:]_block_invoke.870
- __36-[WPDClient disconnectedPeer:error:]_block_invoke.876
- __36-[WPDClient startAdvertising_async:]_block_invoke.613
- __36-[WPDClient startAdvertising_async:]_block_invoke.617
- __36-[WPDPipeManager sendAck:errorCode:]_block_invoke.697
- __36-[WPDScanManager heySiriScanActive:]_block_invoke.243
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.223
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.223.cold.1
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.227
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.233
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.240
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.240.cold.1
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.244
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.248
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke.252
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.224
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.234
- __36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.241
- __36-[WPDaemonServer SetupSignalHandler]_block_invoke.164
- __37-[WPDConnection sendDataToPeripheral]_block_invoke.253
- __37-[WPDPipeManager pipeInfo:forClient:]_block_invoke.492
- __37-[WPDPipeManager stream:handleEvent:]_block_invoke.517
- __37-[WPDPipeManager stream:handleEvent:]_block_invoke.560
- __37-[WPDPipeManager stream:handleEvent:]_block_invoke_2.557
- __38-[WPDScanManager removeSpyScanClient:]_block_invoke.167
- __38-[WPDaemonServer dumpDaemonStateAsync]_block_invoke.315
- __39-[WPDClient connectToPeer:withOptions:]_block_invoke.829
- __39-[WPDClient connectedDeviceOverLEPipe:]_block_invoke.851
- __39-[WPDPendingCompletions addCompletion:]_block_invoke.123
- __39-[WPDPipeManager writeDataToPipe:pipe:]_block_invoke.726
- __40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.219
- __40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.226
- __40-[WPDSearchPartyAgent generateStateDump]_block_invoke.191
- __41-[WPDAdvertisingManager advertisingRules]_block_invoke.350
- __41-[WPDAdvertisingManager advertisingRules]_block_invoke.353
- __41-[WPDAdvertisingManager advertisingRules]_block_invoke.365
- __41-[WPDAdvertisingManager advertisingRules]_block_invoke.369
- __41-[WPDAdvertisingManager advertisingRules]_block_invoke.372
- __41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.324
- __41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.327
- __41-[WPDState updateWithManager:Completion:]_block_invoke.125
- __41-[WPDState updateWithManager:Completion:]_block_invoke.130
- __42-[PipeDataTransfer generateSequenceNumber]_block_invoke.140
- __42-[WPDClient initWithXPCConnection:server:]_block_invoke.477
- __42-[WPDClient initWithXPCConnection:server:]_block_invoke.483
- __42-[WPDClient initWithXPCConnection:server:]_block_invoke.483.cold.1
- __42-[WPDScanManager clearExistingConnections]_block_invoke.387
- __43-[WPDScanManager addScanRequest:forClient:]_block_invoke.191
- __43-[WPDScanManager addScanRequest:forClient:]_block_invoke.198
- __44-[WPDAdvertisingData addAdvertisingRequest:]_block_invoke.122
- __44-[WPDObjectDiscoveryClient sendTestRequest:]_block_invoke.243
- __44-[WPDObjectDiscoveryClient startSPBeaconing]_block_invoke.188
- __44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.221
- __44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.230
- __44-[WPDPendingCompletions completeID:success:]_block_invoke.128
- __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.644
- __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.665
- __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.669
- __44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke_2.666
- __44-[WPDSearchPartyAgent updateTestBeaconKeys:]_block_invoke.290
- __44-[WPDZoneManager unregisterZones:forClient:]_block_invoke.273
- __45-[WPDAdvertisingManager heySiriAdvertActive:]_block_invoke.387
- __45-[WPDAdvertisingManager isAdvertiserTestMode]_block_invoke.376
- __45-[WPDClient clearDuplicateFilterCache_async:]_block_invoke.794
- __45-[WPDObjectDiscoveryClient generateStateDump]_block_invoke.162
- __45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.197
- __45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.204
- __45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.210
- __45-[WPDObjectDiscoveryClient updateSPBeaconing]_block_invoke.182
- __45-[WPDObjectDiscoveryManager updateAdvertiser]_block_invoke.195
- __45-[WPDPipeManager invalidatePipeInfo:forPeer:]_block_invoke.841
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.422
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.435
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.441
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.445
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.449
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.456
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.466
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.467
- __45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.463
- __45-[WPDPipeManager sendRemainingData:wpClient:]_block_invoke.711
- __45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.248
- __45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.248.cold.1
- __45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.253
- __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.260
- __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.260.cold.1
- __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.260.cold.2
- __45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.267
- __46+[WPDSearchPartyAgent spBeaconKeyFromTestKey:]_block_invoke.316
- __46-[WPDConnection peripheral:didModifyServices:]_block_invoke.190
- __46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.677
- __46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.686
- __46-[WPDScanManager removeScanRequest:forClient:]_block_invoke.206
- __47-[WPDPipeManager unregisterEndpoint:forClient:]_block_invoke.414
- __48-[WPDAdvertisingManager removeServiceForClient:]_block_invoke.283
- __48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.149
- __48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.154
- __48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.157.cold.1
- __48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.596
- __48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.633
- __48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke_2.630
- __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.330
- __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.333
- __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.336
- __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.339
- __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.342
- __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.345
- __49-[WPDScanManager startTrackingPeripheral:ofType:]_block_invoke.508
- __49-[WPDState coalesceState:Restricted:UpdateCache:]_block_invoke.136
- __50-[WPDObjectDiscoveryManager advertOptionsChanged:]_block_invoke.156
- __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.190
- __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.190.cold.1
- __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.190.cold.2
- __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.190.cold.3
- __50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.190.cold.4
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.466
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.472
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.475
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.478
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.484
- __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.261
- __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.268
- __52-[WPDPipeManager receivedVersionInfo:data:dataSize:]_block_invoke.585
- __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.780
- __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.780.cold.1
- __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.786
- __53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.793
- __53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.172
- __53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.179
- __54-[WPDAdvertisingManager heySiriAdvertActiveAllDevices]_block_invoke.392
- __54-[WPDClient connectedDevice:withError:shouldDiscover:]_block_invoke.843
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.555
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.558
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.558.cold.1
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.561
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.564
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.567
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.570
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.573
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.576
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.579
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.583
- __54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.374
- __54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.377
- __54-[WPDScanManager logScanTypes:method:window:interval:]_block_invoke.369
- __55-[WPDPipeManager handleIncomingPipeData:data:dataSize:]_block_invoke.571
- __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.595
- __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.598
- __56-[WPDClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.933
- __56-[WPDScanManager centralManager:didFailToScanWithError:]_block_invoke.455
- __57-[WPDAdvertisingManager addAdvertisingRequest:forClient:]_block_invoke.302
- __57-[WPDAdvertisingManager informClientsAdvertisingPending:]_block_invoke.395
- __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.149
- __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.149.cold.1
- __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.153
- __57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke_2.150
- __57-[WPDScanManager logScanRequests:method:window:interval:]_block_invoke.363
- __57-[WPDScanManager removeAllPeerTrackingRequestsForClient:]_block_invoke.500
- __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.248
- __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.252
- __57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.284
- __59-[WPDClient central:subscribed:toCharacteristic:inService:]_block_invoke.912
- __59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.477
- __59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.481
- __59-[WPDScanManager centralManager:didFindPeripheral:forType:]_block_invoke.524
- __59-[WPDScanManager centralManager:didLosePeripheral:forType:]_block_invoke.519
- __60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.215
- __60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.227
- __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.138
- __61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.154
- __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.527
- __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.530
- __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.534
- __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.540
- __62-[WPDClient discoverCharacteristicsAndServices:forPeripheral:]_block_invoke.920
- __62-[WPDPipeManager scalablePipeManager:pipeDidDisconnect:error:]_block_invoke.833
- __63-[WPDAdvertisingManager peripheralManager:didAddService:error:]_block_invoke.288
- __63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.166
- __63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.175
- __63-[WPDSearchPartyAgent initWithQueue:beaconChange:tokensChange:]_block_invoke.181
- __63-[WPDSearchPartyAgent initWithQueue:beaconChange:tokensChange:]_block_invoke.182
- __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.256
- __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.266
- __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.269
- __64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.278
- __65-[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:]_block_invoke.509
- __65-[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:]_block_invoke.896
- __65-[WPDConnection peripheral:didWriteValueForCharacteristic:error:]_block_invoke.267
- __66-[WPDConnection peripheral:didUpdateValueForCharacteristic:error:]_block_invoke.185
- __66-[WPDPipeManager setPipeClientConnectionStatus:forPeer:forClient:]_block_invoke.472
- __66-[WPDScanManager centralManager:didFailToConnectPeripheral:error:]_block_invoke.590
- __67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.495
- __67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.498
- __67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke.275
- __67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke.276
- __67-[WPDObjectDiscoveryClient notifyClientObjectDiscoveryStateChange:]_block_invoke.238
- __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.412
- __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.415
- __68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.422
- __69-[WPDAdvertisingManager peripheralManagerIsReadyToUpdateSubscribers:]_block_invoke.503
- __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.431
- __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.434
- __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.438
- __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.441
- __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.449
- __71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.452
- __71-[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke.162
- __71-[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke.166
- __72-[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:]_block_invoke.207
- __73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.310
- __74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.399
- __74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.409
- __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.489
- __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.495
- __75-[WPDObjectDiscoveryManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.218
- __76+[WPDManager initializeAdvDenylist:AdvAllowlist:ScanDenylist:ScanAllowlist:]_block_invoke.174
- __78-[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:]_block_invoke.509
- __78-[WPDConnection peripheral:didUpdateNotificationStateForCharacteristic:error:]_block_invoke.180
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.413
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.416
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.423
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.426
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.437
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.437.cold.1
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.441
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.447
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.438
- __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.170
- __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.174
- __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.177.cold.1
- __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.177.cold.2
- __78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.181
- __79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.243
- __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.461
- __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.464
- __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.471
- __80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.474
- __81-[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.901
- __83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.545
- __83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.548
- __84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.479
- __84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.482
- ___33-[WPDScanManager updateScanRules]_block_invoke_5
- ___33-[WPDScanManager updateScanRules]_block_invoke_6
- ___33-[WPDScanManager updateScanRules]_block_invoke_7
- ___48+[WPDaemonServer supportsNC2AdvertisingInstance]_block_invoke
- ___48+[WPDaemonServer supportsNC2AdvertisingInstance]_block_invoke_2
- ___block_descriptor_57_e8_32s40w_e23_v16?0"WPScanRequest"8l
- ___block_descriptor_57_e8_32s40w_e30_v16?0"WPAdvertisingRequest"8l
- ___block_descriptor_73_e8_32s40s48s56w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56w
- ___destroy_helper_block_e8_32s40s48s56w
- ___getCombinedAllowlist_block_invoke.352
- __block_literal_global.115
- __block_literal_global.116
- __block_literal_global.132
- __block_literal_global.134
- __block_literal_global.138
- __block_literal_global.140
- __block_literal_global.142
- __block_literal_global.144
- __block_literal_global.148
- __block_literal_global.157
- __block_literal_global.165
- __block_literal_global.166
- __block_literal_global.173
- __block_literal_global.181
- __block_literal_global.206
- __block_literal_global.210
- __block_literal_global.213
- __block_literal_global.233
- __block_literal_global.242
- __block_literal_global.249
- __block_literal_global.255
- __block_literal_global.271
- __block_literal_global.280
- __block_literal_global.294
- __block_literal_global.297
- __block_literal_global.314
- __block_literal_global.317
- __block_literal_global.318
- __block_literal_global.323
- __block_literal_global.326
- __block_literal_global.341
- __block_literal_global.347
- __block_literal_global.351
- __block_literal_global.365
- __block_literal_global.371
- __block_literal_global.373
- __block_literal_global.374
- __block_literal_global.379
- __block_literal_global.382
- __block_literal_global.386
- __block_literal_global.391
- __block_literal_global.393
- __block_literal_global.396
- __block_literal_global.399
- __block_literal_global.402
- __block_literal_global.403
- __block_literal_global.405
- __block_literal_global.411
- __block_literal_global.413
- __block_literal_global.418
- __block_literal_global.421
- __block_literal_global.425
- __block_literal_global.428
- __block_literal_global.437
- __block_literal_global.443
- __block_literal_global.451
- __block_literal_global.452
- __block_literal_global.456
- __block_literal_global.458
- __block_literal_global.460
- __block_literal_global.463
- __block_literal_global.465
- __block_literal_global.471
- __block_literal_global.476
- __block_literal_global.478
- __block_literal_global.480
- __block_literal_global.481
- __block_literal_global.483
- __block_literal_global.495
- __block_literal_global.497
- __block_literal_global.499
- __block_literal_global.505
- __block_literal_global.507
- __block_literal_global.510
- __block_literal_global.511
- __block_literal_global.516
- __block_literal_global.518
- __block_literal_global.519
- __block_literal_global.526
- __block_literal_global.529
- __block_literal_global.532
- __block_literal_global.536
- __block_literal_global.542
- __block_literal_global.544
- __block_literal_global.550
- __block_literal_global.554
- __block_literal_global.560
- __block_literal_global.563
- __block_literal_global.566
- __block_literal_global.570
- __block_literal_global.572
- __block_literal_global.575
- __block_literal_global.578
- __block_literal_global.581
- __block_literal_global.584
- __block_literal_global.595
- __block_literal_global.600
- __block_literal_global.609
- __block_literal_global.632
- __block_literal_global.643
- __block_literal_global.664
- __block_literal_global.668
- __block_literal_global.676
- __block_literal_global.688
- __block_literal_global.706
- __block_literal_global.708
- __block_literal_global.710
- __block_literal_global.752
- __block_literal_global.762
- __block_literal_global.769
- __block_literal_global.774
- __block_literal_global.775
- __block_literal_global.777
- __block_literal_global.788
- __block_literal_global.796
- __block_literal_global.800
- __block_literal_global.802
- __block_literal_global.804
- __block_literal_global.808
- __block_literal_global.810
- __block_literal_global.817
- __block_literal_global.827
- __block_literal_global.828
- __block_literal_global.832
- __block_literal_global.834
- __block_literal_global.840
- __block_literal_global.845
- __block_literal_global.853
- __block_literal_global.867
- __block_literal_global.872
- __block_literal_global.878
- __block_literal_global.880
- __block_literal_global.891
- __block_literal_global.893
- __block_literal_global.898
- __block_literal_global.903
- __block_literal_global.914
- __block_literal_global.922
- __block_literal_global.924
- __block_literal_global.935
- __block_literal_global.940
- __block_literal_global.942
- __block_literal_global.944
- __block_literal_global.946
- __block_literal_global.954
- __block_literal_global.958
- __block_literal_global.962
- __block_literal_global.964
- __block_literal_global.972
- __block_literal_global.974
- __block_literal_global.979
- __block_literal_global.981
- __block_literal_global.983
- __block_literal_global.985
- __block_literal_global.987
- __block_literal_global.995
- __block_literal_global.997
- supportsNC2AdvertisingInstance.sOnce
- supportsNC2AdvertisingInstance.supported
CStrings:
+ "DCTProtocolDataAndTelephony"
+ "DCTProtocolTelephony"
+ "FindMyActionExtendedRange"
+ "FindMyActionExtendedRangeLE2M"
+ "FindMyActionExtendedRangeTransient"
+ "FindMyPlaySoundExtendedRange"
+ "Platform supports supportsNC2AdvertisingInstance: %d"
+ "SofrwareUpdateOutboxControllerAuth"
+ "SoftwareUpdateBTWake"
+ "Tq,V_requestedAtNsec"
+ "WPDaemon macOS 15.4 (24E241) (WirelessProximity-184.42.0.3) (Release) built on 2025-03-17 20:04:58"
+ "[28Q]"
+ "[28[28Q]]"
+ "_requestedAtNsec"
+ "decodeInt64ForKey:"
+ "encodeInt64:forKey:"
+ "kRequestedAtNsec"
+ "numberWithLongLong:"
+ "numberWithUnsignedLongLong:"
+ "requestedAtNsec"
+ "setRequestedAtNsec:"
- "Platform supports NonConnectable Secondary AdvertisingInstance: %s"
- "WPDaemon macOS 15.3 (24D55) (WirelessProximity-183.9.1.0.1) (Release) built on 2025-01-11 18:14:57"
- "Warning: Client has exceeded adv limit! Client: %d , Process: %{public}@ (%d) , Advertising interval: %ld (%.2f ms) "
- "Warning: Client has exceeded scan limit! Client: %d , Process: %{public}@ (%d) , Scan interval: %{public}@ "
- "[27Q]"
- "[27[27Q]]"

```
