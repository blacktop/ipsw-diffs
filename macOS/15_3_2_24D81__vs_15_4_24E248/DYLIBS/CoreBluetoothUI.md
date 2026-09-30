## CoreBluetoothUI

> `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/CoreBluetoothUI`

```diff

-183.9.1.0.1
-  __TEXT.__text: 0x23a28
+184.42.0.3.0
+  __TEXT.__text: 0x21b7c
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x1f50
+  __TEXT.__objc_methlist: 0x2544
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x2301
   __TEXT.__ustring: 0x296
   __TEXT.__oslogstring: 0x4111
-  __TEXT.__gcc_except_tab: 0x1e0
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__gcc_except_tab: 0x1ec
+  __TEXT.__unwind_info: 0x650
   __TEXT.__objc_classname: 0x517
   __TEXT.__objc_methname: 0x67b3
   __TEXT.__objc_methtype: 0x1507

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a10
+  __DATA_CONST.__objc_selrefs: 0x1cf8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x26c0
-  __AUTH_CONST.__objc_const: 0x4260
+  __AUTH_CONST.__objc_const: 0x3710
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/Versions/A/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A384F5B-8170-3573-A798-9FE6F1B942C0
-  Functions: 688
-  Symbols:   1947
+  UUID: 9BDB6A54-0BC4-32AA-A9D2-5709190E0B7C
+  Functions: 687
+  Symbols:   2225
   CStrings:  2314
 
Symbols:
+ +[CBDeviceCollectionView deviceCollectionViewController].cold.1
+ +[CBDeviceCollectionView deviceCollectionViewController].cold.2
+ -[AudioOptionsViewSmartRouting loadPrefs].cold.1
+ -[CBClassicPeer(CBClassicDeviceImages) findAppleImageByIdentifier].cold.1
+ -[CBClassicPeer(CBClassicDeviceImages) findApplePIDVIDImageInPlist].cold.1
+ -[CBClassicPeer(CBClassicDeviceImages) findDefaultImage].cold.1
+ -[CBClassicPeer(CBClassicDeviceImages) findNonAppleImage].cold.1
+ -[CBDevice(CBDeviceImages) findAppleImageByDeviceType].cold.1
+ -[CBDevice(CBDeviceImages) findAppleImageByIdentifier].cold.1
+ -[CBDevice(CBDeviceImages) findApplePIDVIDImageInPlist].cold.1
+ -[CBDevice(CBDeviceImages) findDefaultImage].cold.1
+ -[CBDevice(CBDeviceImages) findGenericImageByDeviceType].cold.1
+ -[CBDevice(CBDeviceImages) findGenericImageByLEAppearance].cold.1
+ -[CBDeviceCollectionView _handleBrowseDevice:].cold.1
+ -[CBDeviceCollectionView _handleConnect:].cold.1
+ -[CBDeviceCollectionView _handlePANConnect:].cold.1
+ -[CBDeviceCollectionView _handlePANConnect:].cold.2
+ -[CBDeviceCollectionView _handleSendFilesToDevice:].cold.1
+ -[CBDeviceCollectionView _menuDisconnect:].cold.1
+ -[CBDeviceCollectionView acceptJustWorksPairingToPeer:].cold.1
+ -[CBDeviceCollectionView acceptJustWorksPairingToPeer:].cold.2
+ -[CBDeviceCollectionView addKeyValueObservingForPeers].cold.1
+ -[CBDeviceCollectionView addKeyValueObservingForPeers].cold.2
+ -[CBDeviceCollectionView appleOptions:].cold.1
+ -[CBDeviceCollectionView bindBatterySwatchColorToConnectedTextColor:].cold.2
+ -[CBDeviceCollectionView cancelAppleOptions:].cold.1
+ -[CBDeviceCollectionView cancelPairingToPeer:].cold.1
+ -[CBDeviceCollectionView cancelPairingToPeer:].cold.2
+ -[CBDeviceCollectionView cancelPairingToPeer:].cold.3
+ -[CBDeviceCollectionView cancelPairingToPeer:].cold.4
+ -[CBDeviceCollectionView cancelPairingToPeer:].cold.5
+ -[CBDeviceCollectionView centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.1
+ -[CBDeviceCollectionView centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.2
+ -[CBDeviceCollectionView centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.3
+ -[CBDeviceCollectionView centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.4
+ -[CBDeviceCollectionView centralManagerDidUpdateState:].cold.1
+ -[CBDeviceCollectionView centralManagerDidUpdateState:].cold.2
+ -[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:].cold.1
+ -[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:].cold.2
+ -[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:].cold.3
+ -[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:].cold.4
+ -[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:].cold.5
+ -[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:].cold.6
+ -[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:].cold.7
+ -[CBDeviceCollectionView cleanupTimerTask].cold.1
+ -[CBDeviceCollectionView cleanupTimerTask].cold.2
+ -[CBDeviceCollectionView connectPeerFromShim:].cold.1
+ -[CBDeviceCollectionView createDeviceDictForPeer:].cold.1
+ -[CBDeviceCollectionView createDeviceDictForPeer:].cold.2
+ -[CBDeviceCollectionView dealloc].cold.1
+ -[CBDeviceCollectionView dealloc].cold.2
+ -[CBDeviceCollectionView didConnectToPeer:withError:].cold.1
+ -[CBDeviceCollectionView didConnectToPeer:withError:].cold.2
+ -[CBDeviceCollectionView didConnectToPeer:withError:].cold.3
+ -[CBDeviceCollectionView didDisconnectFromPeer:withError:].cold.1
+ -[CBDeviceCollectionView didDisconnectFromPeer:withError:].cold.2
+ -[CBDeviceCollectionView didDisconnectFromPeer:withError:].cold.3
+ -[CBDeviceCollectionView didDisconnectFromPeer:withError:].cold.4
+ -[CBDeviceCollectionView didFindAndUpdateDeviceDictInDeviceCollectionArrayForPeer:].cold.1
+ -[CBDeviceCollectionView didFindAndUpdateDeviceDictInDeviceCollectionArrayForPeer:].cold.2
+ -[CBDeviceCollectionView dismissModalSheetForPairing].cold.1
+ -[CBDeviceCollectionView dismissModalSheetForPairing].cold.2
+ -[CBDeviceCollectionView handleBluetoothStateChange].cold.1
+ -[CBDeviceCollectionView handleBluetoothStateChange].cold.2
+ -[CBDeviceCollectionView handleBluetoothStateChange].cold.3
+ -[CBDeviceCollectionView handleBluetoothStateChange].cold.4
+ -[CBDeviceCollectionView handleBluetoothStateChange].cold.5
+ -[CBDeviceCollectionView handleBluetoothStateChange].cold.6
+ -[CBDeviceCollectionView handleBluetoothStateChange].cold.7
+ -[CBDeviceCollectionView handleConnectButtonPress:].cold.1
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.1
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.10
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.11
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.2
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.3
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.4
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.5
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.6
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.7
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.8
+ -[CBDeviceCollectionView handleTableViewCellDoubleClick:].cold.9
+ -[CBDeviceCollectionView hasPairingOptions:].cold.1
+ -[CBDeviceCollectionView hasPairingOptions:].cold.2
+ -[CBDeviceCollectionView hasPairingOptions:].cold.3
+ -[CBDeviceCollectionView hasPairingOptions:].cold.4
+ -[CBDeviceCollectionView initializeCurrentlyConnectedClassicPeers].cold.1
+ -[CBDeviceCollectionView initializeCurrentlyConnectedClassicPeers].cold.2
+ -[CBDeviceCollectionView initializeCurrentlyConnectedPeripherals].cold.1
+ -[CBDeviceCollectionView initializeCurrentlyConnectedPeripherals].cold.2
+ -[CBDeviceCollectionView initializeCurrentlyPairedPeers].cold.1
+ -[CBDeviceCollectionView initializeCurrentlyPairedPeers].cold.2
+ -[CBDeviceCollectionView lePairingConnectionTimeout:].cold.1
+ -[CBDeviceCollectionView lePairingConnectionTimeout:].cold.2
+ -[CBDeviceCollectionView lePairingConnectionTimeout:].cold.3
+ -[CBDeviceCollectionView listenForUserChange].cold.10
+ -[CBDeviceCollectionView listenForUserChange].cold.11
+ -[CBDeviceCollectionView listenForUserChange].cold.12
+ -[CBDeviceCollectionView listenForUserChange].cold.6
+ -[CBDeviceCollectionView listenForUserChange].cold.7
+ -[CBDeviceCollectionView listenForUserChange].cold.8
+ -[CBDeviceCollectionView listenForUserChange].cold.9
+ -[CBDeviceCollectionView numberOfRowsInTableView:].cold.1
+ -[CBDeviceCollectionView observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[CBDeviceCollectionView observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[CBDeviceCollectionView observeValueForKeyPath:ofObject:change:context:].cold.3
+ -[CBDeviceCollectionView observeValueForKeyPath:ofObject:change:context:].cold.4
+ -[CBDeviceCollectionView observeValueForKeyPath:ofObject:change:context:].cold.5
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.1
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.2
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.3
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.4
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.5
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.6
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.7
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.8
+ -[CBDeviceCollectionView pairToDeviceInDict:].cold.9
+ -[CBDeviceCollectionView pairingAgent:peerDidCompletePairing:].cold.1
+ -[CBDeviceCollectionView pairingAgent:peerDidFailToCompletePairing:error:].cold.1
+ -[CBDeviceCollectionView pairingAgent:peerDidFailToCompletePairing:error:].cold.2
+ -[CBDeviceCollectionView pairingAgent:peerDidFailToCompletePairing:error:].cold.3
+ -[CBDeviceCollectionView pairingAgent:peerDidFailToCompletePairing:error:].cold.4
+ -[CBDeviceCollectionView pairingAgent:peerDidFailToCompletePairing:error:].cold.5
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.1
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.10
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.11
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.12
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.13
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.14
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.2
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.3
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.4
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.5
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.6
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.7
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.8
+ -[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:].cold.9
+ -[CBDeviceCollectionView pairingAgent:peerDidUnpair:].cold.1
+ -[CBDeviceCollectionView pairingAgent:peerDidUnpair:].cold.2
+ -[CBDeviceCollectionView pairingAgent:peerDidUnpair:].cold.3
+ -[CBDeviceCollectionView pairingAgent:peerDidUnpair:].cold.4
+ -[CBDeviceCollectionView pairingCompletedWith:].cold.1
+ -[CBDeviceCollectionView pairingCompletedWith:].cold.2
+ -[CBDeviceCollectionView pairingCompletedWith:].cold.3
+ -[CBDeviceCollectionView pauseInquiry].cold.1
+ -[CBDeviceCollectionView peripheralDidConnect:].cold.1
+ -[CBDeviceCollectionView peripheralDidConnect:].cold.2
+ -[CBDeviceCollectionView peripheralDidDisconnect:].cold.1
+ -[CBDeviceCollectionView peripheralDidDisconnect:].cold.2
+ -[CBDeviceCollectionView peripheralDidDisconnect:].cold.3
+ -[CBDeviceCollectionView presentModalSheetForPairingType:withPasskey:withPeer:].cold.1
+ -[CBDeviceCollectionView presentModalSheetForPairingType:withPasskey:withPeer:].cold.2
+ -[CBDeviceCollectionView presentModalSheetForPairingType:withPasskey:withPeer:].cold.3
+ -[CBDeviceCollectionView refreshPrefpane].cold.1
+ -[CBDeviceCollectionView removeAllUnpairedDevices].cold.1
+ -[CBDeviceCollectionView removeAllUnpairedDevices].cold.2
+ -[CBDeviceCollectionView removeAllUnpairedDevices].cold.3
+ -[CBDeviceCollectionView removeCBPeerDicts:].cold.1
+ -[CBDeviceCollectionView removeKeyValueObservingForPeers].cold.1
+ -[CBDeviceCollectionView removeStaleUnpairedDevices].cold.1
+ -[CBDeviceCollectionView removeStaleUnpairedDevices].cold.2
+ -[CBDeviceCollectionView removeStaleUnpairedDevices].cold.3
+ -[CBDeviceCollectionView resumeInquiry:].cold.1
+ -[CBDeviceCollectionView resumeInquiry:].cold.2
+ -[CBDeviceCollectionView resumeInquiry:].cold.3
+ -[CBDeviceCollectionView resumeInquiry:].cold.4
+ -[CBDeviceCollectionView setDiscoverableAndConnectable:].cold.1
+ -[CBDeviceCollectionView setDiscoverableAndConnectable:].cold.2
+ -[CBDeviceCollectionView setStatusStringForPeer:].cold.1
+ -[CBDeviceCollectionView setStatusStringForPeer:].cold.2
+ -[CBDeviceCollectionView setStatusStringForPeer:].cold.3
+ -[CBDeviceCollectionView setupUIForPairingOptionsForDeviceDict:].cold.2
+ -[CBDeviceCollectionView setupUIForPairingOptionsForDeviceDict:].cold.3
+ -[CBDeviceCollectionView startInquiry:].cold.1
+ -[CBDeviceCollectionView startInquiry:].cold.2
+ -[CBDeviceCollectionView startLEScansWithDelay:forAPeriodOf:].cold.1
+ -[CBDeviceCollectionView startLEScansWithDelay:forAPeriodOf:].cold.2
+ -[CBDeviceCollectionView stopInquiry].cold.1
+ -[CBDeviceCollectionView stopLEScansWithDelay:ForAPeriodOf:].cold.1
+ -[CBDeviceCollectionView stopLEScansWithDelay:ForAPeriodOf:].cold.2
+ -[CBDeviceCollectionView stopLEScansWithDelay:ForAPeriodOf:].cold.3
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.10
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.11
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.12
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.13
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.14
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.15
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.16
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.17
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.18
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.19
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.20
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.21
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.6
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.7
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.8
+ -[CBDeviceCollectionView tableView:viewForTableColumn:row:].cold.9
+ -[CBDeviceCollectionView tableViewSelectionDidChange:].cold.1
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.10
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.11
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.12
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.13
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.14
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.15
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.16
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.17
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.18
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.19
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.2
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.20
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.21
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.22
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.23
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.24
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.25
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.26
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.3
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.4
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.5
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.6
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.7
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.8
+ -[CBDeviceCollectionView updateDeviceDict:forPeer:].cold.9
+ -[CBDeviceCollectionView updateRemoveButtonVisibility:].cold.1
+ -[CBDeviceCollectionView updateRemoveButtonVisibility:].cold.2
+ -[CBDeviceCollectionView updateRemoveButtonVisibility:].cold.3
+ -[CBDeviceCollectionView viewDidAppear].cold.1
+ -[CBDeviceCollectionView viewDidAppear].cold.2
+ -[CBDeviceCollectionView viewDidAppear].cold.3
+ -[CBDeviceCollectionView viewDidDisappear].cold.1
+ -[CBDeviceCollectionView viewDidDisappear].cold.2
+ -[CBDeviceCollectionView viewDidDisappear].cold.3
+ -[CBDeviceCollectionView viewDidLoad].cold.1
+ -[CBDeviceCollectionView viewDidLoad].cold.2
+ -[CBDeviceCollectionView viewDidLoad].cold.3
+ -[CBDeviceCollectionView viewDidLoad].cold.4
+ -[CBDeviceCollectionView viewDidLoad].cold.5
+ -[CBDeviceCollectionView viewDidLoad].cold.6
+ -[CBDeviceCollectionView viewDidLoad].cold.7
+ -[CBDeviceCollectionView viewDidLoad].cold.8
+ -[CBDeviceCollectionView viewDidLoad].cold.9
+ -[CBPeer(CBPeerImages) image].cold.1
+ -[CBPeripheral(CBLEDeviceImages) getImage:].cold.1
+ -[CBSortedDeviceArrayController addObject:].cold.2
+ -[CBSortedDeviceArrayController addObject:].cold.3
+ -[CBSortedDeviceArrayController addObject:].cold.4
+ -[CBSortedDeviceArrayController addObject:].cold.5
+ -[CBSortedDeviceArrayController addObject:].cold.6
+ -[CBSortedDeviceArrayController addObject:].cold.7
+ -[CBSortedDeviceArrayController addObjects:].cold.1
+ -[CBSortedDeviceArrayController arrangeObjects:].cold.2
+ -[CBSortedDeviceArrayController initWithCoder:].cold.1
+ -[CBSortedDeviceArrayController initWithContent:].cold.1
+ -[CBSortedDeviceArrayController initialize].cold.1
+ -[CBSortedDeviceArrayController removeObject:].cold.1
+ -[CBUIBatteryControl drawRect:].cold.1
+ -[CBUIBatteryControl drawRect:].cold.2
+ -[CBUIBatteryControl drawRect:].cold.3
+ _OUTLINED_FUNCTION_6
+ __33-[CBDeviceCollectionView unpair:]_block_invoke.cold.1
+ __33-[CBDeviceCollectionView unpair:]_block_invoke.cold.2
+ __41-[CBDeviceCollectionView addCBPeerDicts:]_block_invoke.cold.1
+ __42-[CBDeviceCollectionView renamePeer:name:]_block_invoke.cold.1
+ __60-[CBDeviceCollectionView stopLEScansWithDelay:ForAPeriodOf:]_block_invoke.249.cold.1
+ __60-[CBDeviceCollectionView stopLEScansWithDelay:ForAPeriodOf:]_block_invoke.cold.1
+ __61-[CBDeviceCollectionView startLEScansWithDelay:forAPeriodOf:]_block_invoke.cold.1
+ __64-[CBDeviceCollectionView setupUIForPairingOptionsForDeviceDict:]_block_invoke.cold.1
+ __64-[CBDeviceCollectionView setupUIForPairingOptionsForDeviceDict:]_block_invoke.cold.2
+ __64-[CBDeviceCollectionView setupUIForPairingOptionsForDeviceDict:]_block_invoke.cold.3
+ __72-[CBDeviceCollectionView classicManager:didFindPeer:withInquiryResults:]_block_invoke.cold.1
+ __74-[CBDeviceCollectionView pairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke.cold.1
+ dynamicStoreCallback.cold.1
+ dynamicStoreCallback.cold.2
+ initSiriUISetup.cold.1

```
