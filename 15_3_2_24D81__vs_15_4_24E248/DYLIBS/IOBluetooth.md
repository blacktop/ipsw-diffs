## IOBluetooth

> `/System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth`

```diff

-183.9.1.0.1
-  __TEXT.__text: 0x794e8
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0x84e8
+184.42.0.3.0
+  __TEXT.__text: 0x753c4
+  __TEXT.__auth_stubs: 0x1420
+  __TEXT.__objc_methlist: 0x8c64
   __TEXT.__cstring: 0xbdb6
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__const: 0x46c
+  __TEXT.__gcc_except_tab: 0x3f4
+  __TEXT.__const: 0x49c
   __TEXT.__oslogstring: 0x4efc
-  __TEXT.__unwind_info: 0x1a00
+  __TEXT.__unwind_info: 0x1970
   __TEXT.__objc_classname: 0x971
   __TEXT.__objc_methname: 0x1551c
   __TEXT.__objc_methtype: 0x4a16

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d30
+  __DATA_CONST.__objc_selrefs: 0x4f10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0xa28
+  __AUTH_CONST.__auth_got: 0xa20
   __AUTH_CONST.__const: 0x8e0
   __AUTH_CONST.__cfstring: 0x77c0
-  __AUTH_CONST.__objc_const: 0xd5d0
+  __AUTH_CONST.__objc_const: 0xc7d0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x14a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23BED04A-DE8E-3952-B04E-4C32E340DD34
-  Functions: 3513
-  Symbols:   6844
+  UUID: 6CE1DBCE-5F4B-3770-9237-A5D99E5C41C3
+  Functions: 3511
+  Symbols:   7345
   CStrings:  6928
 
Symbols:
+ +[BluetoothDeviceManager sharedDeviceManager].cold.1
+ +[FrameworkAnalyticsManager sharedManager].cold.1
+ +[FrameworksAnalyticsPackager sharedPackager].cold.1
+ +[IOBluetoothCoreBluetoothCoordinator sharedInstance].cold.1
+ +[IOBluetoothDevice connectedDevices].cold.2
+ +[IOBluetoothDevice pairedDevices].cold.2
+ +[IOBluetoothDevice pairedDevices].cold.3
+ +[IOBluetoothDevice registerForConnectNotifications:selector:].cold.1
+ +[IOBluetoothDevice registerForConnectNotifications:selector:].cold.2
+ +[IOBluetoothDevice registerForPairingNotifications:selector:].cold.1
+ +[IOBluetoothHostController defaultController].cold.1
+ +[IOBluetoothL2CAPChannel registerForChannelOpenNotifications:selector:withPSM:direction:].cold.1
+ +[IOBluetoothL2CAPChannel registerForChannelOpenNotifications:selector:withPSM:direction:].cold.2
+ +[IOBluetoothL2CAPChannel withObjectID:].cold.1
+ +[IOBluetoothPreferences sharedPreferences].cold.1
+ +[IOBluetoothRFCOMMChannel registerForChannelOpenNotifications:selector:withChannelID:direction:].cold.1
+ +[IOBluetoothRFCOMMChannel registerForChannelOpenNotifications:selector:withChannelID:direction:].cold.2
+ +[IOBluetoothRFCOMMChannel withObjectID:].cold.1
+ +[IOBluetoothSerialPortManager sharedSerialPortManager].cold.1
+ -[BluetoothDeviceManager _elementToNSData:].cold.18
+ -[BluetoothDeviceManager _elementToNSData:].cold.19
+ -[BluetoothDeviceManager _elementToNSData:].cold.20
+ -[BluetoothDeviceManager _elementToNSData:].cold.21
+ -[BluetoothDeviceManager _elementToNSData:].cold.22
+ -[BluetoothDeviceManager _elementToNSData:].cold.23
+ -[BluetoothDeviceManager _elementToNSData:].cold.24
+ -[BluetoothDeviceManager _elementToNSData:].cold.25
+ -[BluetoothDeviceManager _elementToNSData:].cold.26
+ -[BluetoothDeviceManager _elementToNSData:].cold.27
+ -[BluetoothDeviceManager _elementToNSData:].cold.28
+ -[BluetoothDeviceManager _elementToNSData:].cold.29
+ -[BluetoothDeviceManager _elementToNSData:].cold.30
+ -[BluetoothDeviceManager _elementToNSData:].cold.31
+ -[BluetoothDeviceManager _elementToNSData:].cold.32
+ -[BluetoothDeviceManager _elementToNSData:].cold.33
+ -[BluetoothDeviceManager _elementToNSData:].cold.34
+ -[BluetoothDeviceManager _serviceToNSData:].cold.2
+ -[BluetoothDeviceManager addServiceDict:andSDPRecord:].cold.2
+ -[BluetoothDeviceManager addServiceDict:andSDPRecord:].cold.3
+ -[BluetoothDeviceManager addServiceDict:andSDPRecord:].cold.4
+ -[BluetoothDeviceManager configureHIDDevice:].cold.2
+ -[BluetoothDeviceManager getLocalServices].cold.2
+ -[BluetoothDeviceManager getLocalServices].cold.3
+ -[BluetoothDeviceManager ignoreHIDDevice:].cold.1
+ -[BluetoothDeviceManager init].cold.1
+ -[BluetoothDeviceManager removeIgnoredHIDDevice:].cold.1
+ -[BluetoothDeviceManager secureBluetooth:].cold.3
+ -[BluetoothDeviceManager secureBluetooth:].cold.4
+ -[BluetoothDeviceManager secureBluetooth:].cold.5
+ -[IOBluetoothAutomaticDeviceSetup bluetoothDone:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup centralManager:didConnectPeripheral:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup centralManager:didDisconnectPeripheral:error:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup centralManager:didFailToConnectPeripheral:error:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup centralManagerDidUpdateState:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup clearCurrentDevice].cold.1
+ -[IOBluetoothAutomaticDeviceSetup clearCurrentDevice].cold.2
+ -[IOBluetoothAutomaticDeviceSetup deviceAppearanceTimeoutTimerFired].cold.1
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryComplete:error:aborted:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryComplete:error:aborted:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryComplete:error:aborted:].cold.3
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryComplete:error:aborted:].cold.4
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryDeviceFound:device:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryDeviceFound:device:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryDeviceNameUpdated:device:devicesRemaining:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryStarted:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup deviceInquiryUpdatingDeviceNamesStarted:devicesRemaining:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup devicePairingConnected:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup devicePairingConnecting:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup devicePairingFinished:error:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup devicePairingPINCodeRequest:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup devicePairingPINCodeRequest:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup devicePairingStarted:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup init].cold.1
+ -[IOBluetoothAutomaticDeviceSetup newBluetoothHIDDevice:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup newBluetoothHIDDevice:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup newBluetoothHIDDeviceDisconnected:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup newBluetoothHIDDeviceDisconnected:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup pairWithNextDevice].cold.1
+ -[IOBluetoothAutomaticDeviceSetup pairWithNextDevice].cold.2
+ -[IOBluetoothAutomaticDeviceSetup pairWithNextDevice].cold.3
+ -[IOBluetoothAutomaticDeviceSetup pairWithNextDevice].cold.4
+ -[IOBluetoothAutomaticDeviceSetup pairWithNextDevice].cold.5
+ -[IOBluetoothAutomaticDeviceSetup pairWithNextDevice].cold.6
+ -[IOBluetoothAutomaticDeviceSetup pairWithNextDevice].cold.7
+ -[IOBluetoothAutomaticDeviceSetup performUSBPairing].cold.1
+ -[IOBluetoothAutomaticDeviceSetup registerForKeyboardNotifications].cold.1
+ -[IOBluetoothAutomaticDeviceSetup registerForMouseNotifications].cold.1
+ -[IOBluetoothAutomaticDeviceSetup registerForSystemSleepNotifications].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setAfterPairUserAcknowledgementTimeLimit:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setDelegate:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setInquiryLength:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setNonNULLPIN:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setNotifyOnKeyboard:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setNotifyOnMouse:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setNumberOfPairingAttemptsPerDevice:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setPreventSleepFor:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup setSearchCriteria:majorDeviceClass:minorDeviceClass:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup skipCurrentDevice].cold.1
+ -[IOBluetoothAutomaticDeviceSetup startDeviceAppearanceTimeoutTimer].cold.1
+ -[IOBluetoothAutomaticDeviceSetup startInquiry].cold.1
+ -[IOBluetoothAutomaticDeviceSetup startInquiry].cold.2
+ -[IOBluetoothAutomaticDeviceSetup startLEScans].cold.1
+ -[IOBluetoothAutomaticDeviceSetup startUpdateSystemActivityTimer].cold.1
+ -[IOBluetoothAutomaticDeviceSetup startUserAckTimer].cold.1
+ -[IOBluetoothAutomaticDeviceSetup stopAllBluetooth:clearInquiry:clearCurrentDevice:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup stopAndAcceptCurrentDevice].cold.1
+ -[IOBluetoothAutomaticDeviceSetup stopAndUnPairCurrentDevice:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup stopDeviceAppearanceTimeoutTimer].cold.1
+ -[IOBluetoothAutomaticDeviceSetup stopInquiry].cold.1
+ -[IOBluetoothAutomaticDeviceSetup stopUpdateSystemActivityTimer].cold.1
+ -[IOBluetoothAutomaticDeviceSetup stopUserAckTimer].cold.1
+ -[IOBluetoothAutomaticDeviceSetup systemPowerNotification:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup systemPowerNotification:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup unregisterForKeyboardNotifications].cold.1
+ -[IOBluetoothAutomaticDeviceSetup unregisterForMouseNotifications].cold.1
+ -[IOBluetoothAutomaticDeviceSetup unregisterForSystemSleepNotifications].cold.1
+ -[IOBluetoothAutomaticDeviceSetup updateSystemActivityTimerFired:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup updateSystemActivityTimerFired:].cold.2
+ -[IOBluetoothAutomaticDeviceSetup usbHIDDeviceConnected:result:sender:device:].cold.1
+ -[IOBluetoothAutomaticDeviceSetup userAckTimerFired].cold.1
+ -[IOBluetoothConcreteUserNotification peerConnected:error:].cold.1
+ -[IOBluetoothConcreteUserNotification peerConnected:error:].cold.2
+ -[IOBluetoothConcreteUserNotification peerDisconnected:withError:].cold.3
+ -[IOBluetoothConcreteUserNotification peerDisconnected:withError:].cold.4
+ -[IOBluetoothConcreteUserNotification peerDisconnected:withError:].cold.5
+ -[IOBluetoothConcreteUserNotification peerDisconnected:withError:].cold.6
+ -[IOBluetoothConcreteUserNotification peerDisconnected:withError:].cold.7
+ -[IOBluetoothConcreteUserNotification peerL2CAPChannelConnected:error:].cold.1
+ -[IOBluetoothConcreteUserNotification peerL2CAPChannelConnected:error:].cold.2
+ -[IOBluetoothConcreteUserNotification peerL2CAPChannelDisconnected:error:].cold.1
+ -[IOBluetoothConcreteUserNotification peerL2CAPChannelDisconnected:error:].cold.2
+ -[IOBluetoothConcreteUserNotification peerL2CAPChannelDisconnected:error:].cold.3
+ -[IOBluetoothConcreteUserNotification peerRFCOMMChannelConnected:error:].cold.1
+ -[IOBluetoothConcreteUserNotification peerRFCOMMChannelConnected:error:].cold.2
+ -[IOBluetoothConcreteUserNotification peerRFCOMMChannelConnected:error:].cold.3
+ -[IOBluetoothConcreteUserNotification peerRFCOMMChannelDisconnected:error:].cold.1
+ -[IOBluetoothConcreteUserNotification peerRFCOMMChannelDisconnected:error:].cold.2
+ -[IOBluetoothConcreteUserNotification peerRFCOMMChannelDisconnected:error:].cold.3
+ -[IOBluetoothCoreBluetoothCoordinator _updatePowerState].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator addDelegate:].cold.3
+ -[IOBluetoothCoreBluetoothCoordinator addDelegate:].cold.4
+ -[IOBluetoothCoreBluetoothCoordinator cancelPeerConnection:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator cancelPeerConnection:].cold.3
+ -[IOBluetoothCoreBluetoothCoordinator connectPeer:options:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator connectPeer:options:].cold.3
+ -[IOBluetoothCoreBluetoothCoordinator init].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator isDeviceDiscoverable].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator isDeviceDiscoverable].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator isPeerCloudPaired:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator isPeerDOAPSupported:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator isPeerMagicPaired:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator isPeerPaired:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator pairPeer:forType:withKey:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator pairPeer:forType:withKey:].cold.3
+ -[IOBluetoothCoreBluetoothCoordinator pairingAgent:peerDidCompletePairing:].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator pairingAgent:peerDidFailToCompletePairing:error:].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator pairingAgent:peerDidRequestPairing:type:passkey:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator pairingAgent:peerDidRequestPairing:type:passkey:].cold.3
+ -[IOBluetoothCoreBluetoothCoordinator pairingAgent:peerDidUnpair:].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator peerForAddressString:].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator peerForIdentifier:].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator removeDelegate:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator startScanning:].cold.1
+ -[IOBluetoothCoreBluetoothCoordinator stopScanning].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator unpairPeer:].cold.2
+ -[IOBluetoothCoreBluetoothCoordinator unpairPeer:].cold.3
+ -[IOBluetoothDevice classOfDevice].cold.2
+ -[IOBluetoothDevice closeConnection].cold.1
+ -[IOBluetoothDevice dealloc].cold.2
+ -[IOBluetoothDevice deviceClassMajor].cold.2
+ -[IOBluetoothDevice deviceClassMinor].cold.2
+ -[IOBluetoothDevice initWithCBPeripheral:].cold.1
+ -[IOBluetoothDevice isPointingDevice].cold.1
+ -[IOBluetoothDevice isPointingDevice].cold.2
+ -[IOBluetoothDevice l2capChannels].cold.1
+ -[IOBluetoothDevice l2capChannels].cold.2
+ -[IOBluetoothDevice matchesSearchAttributes:ignoreDeviceNameIfNil:].cold.1
+ -[IOBluetoothDevice matchesSearchAttributes:ignoreDeviceNameIfNil:].cold.2
+ -[IOBluetoothDevice matchesSearchAttributes:ignoreDeviceNameIfNil:].cold.3
+ -[IOBluetoothDevice openConnection:withPageTimeout:authenticationRequired:allowRoleSwitch:forPairing:].cold.2
+ -[IOBluetoothDevice openConnection:withPageTimeout:authenticationRequired:allowRoleSwitch:forPairing:].cold.3
+ -[IOBluetoothDevice openConnection:withPageTimeout:authenticationRequired:allowRoleSwitch:forPairing:].cold.4
+ -[IOBluetoothDevice openConnection:withPageTimeout:authenticationRequired:allowRoleSwitch:forPairing:].cold.5
+ -[IOBluetoothDevice openL2CAPChannel:findExisting:newChannel:].cold.2
+ -[IOBluetoothDevice openL2CAPChannelAsync:withPSM:withConfiguration:delegate:].cold.2
+ -[IOBluetoothDevice openL2CAPChannelAsync:withPSM:withConfiguration:delegate:].cold.3
+ -[IOBluetoothDevice openL2CAPChannelAsync:withPSM:withConfiguration:delegate:].cold.4
+ -[IOBluetoothDevice openL2CAPChannelAsync:withPSM:withConfiguration:delegate:].cold.5
+ -[IOBluetoothDevice openL2CAPChannelSync:withPSM:withConfiguration:delegate:].cold.2
+ -[IOBluetoothDevice openL2CAPChannelSync:withPSM:withConfiguration:delegate:].cold.3
+ -[IOBluetoothDevice openL2CAPChannelSync:withPSM:withConfiguration:delegate:].cold.4
+ -[IOBluetoothDevice openRFCOMMChannel:channel:].cold.1
+ -[IOBluetoothDevice openRFCOMMChannelAsync:withChannelID:delegate:].cold.1
+ -[IOBluetoothDevice openRFCOMMChannelSync:withChannelID:delegate:].cold.2
+ -[IOBluetoothDevice openRFCOMMChannelSync:withChannelID:delegate:].cold.3
+ -[IOBluetoothDevice openRFCOMMChannelSync:withChannelID:delegate:].cold.4
+ -[IOBluetoothDevice peerConnected:error:].cold.1
+ -[IOBluetoothDevice peerDisconnected:withError:].cold.1
+ -[IOBluetoothDevice peerDiscovered:withResults:].cold.1
+ -[IOBluetoothDevice peerPairingCompleted:withError:].cold.1
+ -[IOBluetoothDevice peerUnpaired:].cold.1
+ -[IOBluetoothDevice peerUpdated:withResults:].cold.1
+ -[IOBluetoothDevice performSDPQuery:].cold.2
+ -[IOBluetoothDevice registerForDisconnectNotification:selector:].cold.1
+ -[IOBluetoothDevice registerForDisconnectNotification:selector:].cold.2
+ -[IOBluetoothDevice remove].cold.2
+ -[IOBluetoothDevice remove].cold.3
+ -[IOBluetoothDevice sendL2CAPEchoRequest:length:].cold.1
+ -[IOBluetoothDevice services].cold.2
+ -[IOBluetoothDeviceInquiry addInquiryToDaemon].cold.2
+ -[IOBluetoothDeviceInquiry inquiryStateChanged:].cold.1
+ -[IOBluetoothDeviceInquiry inquiryStateChanged:].cold.2
+ -[IOBluetoothDeviceInquiry peerDiscovered:withResults:].cold.1
+ -[IOBluetoothDeviceInquiry removeInquiryFromDaemon].cold.2
+ -[IOBluetoothDeviceInquiry setSearchAttributes:].cold.1
+ -[IOBluetoothDeviceInquiry setSearchCriteria:majorDeviceClass:minorDeviceClass:].cold.1
+ -[IOBluetoothDeviceInquiry stopInquiryInDaemon].cold.2
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.10
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.11
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.12
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.13
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.6
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.7
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.8
+ -[IOBluetoothDevicePair _peerDidRequestPairing:type:passkey:].cold.9
+ -[IOBluetoothDevicePair _peerDiscovered:withResults:].cold.10
+ -[IOBluetoothDevicePair _peerDiscovered:withResults:].cold.11
+ -[IOBluetoothDevicePair _peerDiscovered:withResults:].cold.6
+ -[IOBluetoothDevicePair _peerDiscovered:withResults:].cold.7
+ -[IOBluetoothDevicePair _peerDiscovered:withResults:].cold.8
+ -[IOBluetoothDevicePair _peerDiscovered:withResults:].cold.9
+ -[IOBluetoothDevicePair centralManager:didConnectPeripheral:].cold.1
+ -[IOBluetoothDevicePair connectionComplete:status:].cold.1
+ -[IOBluetoothDevicePair connectionCompleteContinue:].cold.1
+ -[IOBluetoothDevicePair openPairingConnection].cold.1
+ -[IOBluetoothDevicePair pairingAgent:peerDidFailToCompletePairing:error:].cold.1
+ -[IOBluetoothDevicePair pairingAgent:peerDidRequestPairing:type:passkey:].cold.1
+ -[IOBluetoothDevicePair pairingAgent:peerDidRequestPairing:type:passkey:].cold.2
+ -[IOBluetoothDevicePair pairingAgent:peerDidRequestPairing:type:passkey:].cold.3
+ -[IOBluetoothDevicePair pairingAgent:peerDidRequestPairing:type:passkey:].cold.4
+ -[IOBluetoothDevicePair peerConnected:error:].cold.1
+ -[IOBluetoothDevicePair peerDisconnected:withError:].cold.1
+ -[IOBluetoothDevicePair peerPairingCompleted:withError:].cold.2
+ -[IOBluetoothDevicePair peerPairingCompleted:withError:].cold.3
+ -[IOBluetoothDevicePair pinCodeRequest:].cold.1
+ -[IOBluetoothDevicePair replyPINCode:PINCode:].cold.1
+ -[IOBluetoothDevicePair replyPINCode:PINCode:].cold.2
+ -[IOBluetoothDevicePair replyPINCodeWithNumber:].cold.1
+ -[IOBluetoothDevicePair replyUserConfirmation:].cold.1
+ -[IOBluetoothDevicePair sdpQueryComplete:status:].cold.1
+ -[IOBluetoothDevicePair sdpQueryComplete:status:].cold.2
+ -[IOBluetoothDevicePair simplePairingComplete:status:].cold.1
+ -[IOBluetoothDevicePair start].cold.2
+ -[IOBluetoothDevicePair start].cold.3
+ -[IOBluetoothDevicePair start].cold.4
+ -[IOBluetoothDevicePair stop].cold.2
+ -[IOBluetoothDevicePair userConfirmationRequest:numericValue:].cold.1
+ -[IOBluetoothDevicePair userPasskeyNotification:passkey:].cold.1
+ -[IOBluetoothHostController BluetoothHCIReadDeviceAddress:].cold.2
+ -[IOBluetoothHostController BluetoothHCIReadLocalName:].cold.2
+ -[IOBluetoothHostController cachedDeviceAddress].cold.2
+ -[IOBluetoothHostController cachedDeviceAddress].cold.3
+ -[IOBluetoothL2CAPChannel _initWithDevice:andClassicPeer:PSM:withServiceUUID:].cold.2
+ -[IOBluetoothL2CAPChannel _initWithDevice:andClassicPeer:PSM:withServiceUUID:].cold.3
+ -[IOBluetoothL2CAPChannel _initWithDevice:andClassicPeer:PSM:withServiceUUID:].cold.4
+ -[IOBluetoothL2CAPChannel _initWithDevice:andClassicPeer:PSM:withServiceUUID:].cold.5
+ -[IOBluetoothL2CAPChannel closeChannel].cold.1
+ -[IOBluetoothL2CAPChannel connectionComplete:status:].cold.2
+ -[IOBluetoothL2CAPChannel connectionComplete:status:].cold.3
+ -[IOBluetoothL2CAPChannel dealloc].cold.1
+ -[IOBluetoothL2CAPChannel initWithCBL2CAPChannel:].cold.3
+ -[IOBluetoothL2CAPChannel initWithCBL2CAPChannel:].cold.4
+ -[IOBluetoothL2CAPChannel initWithDevice:andClassicPeer:PSM:].cold.4
+ -[IOBluetoothL2CAPChannel initWithDevice:andClassicPeer:PSM:].cold.5
+ -[IOBluetoothL2CAPChannel initWithDevice:andClassicPeer:PSM:].cold.6
+ -[IOBluetoothL2CAPChannel peerConnected:error:].cold.1
+ -[IOBluetoothL2CAPChannel peerDisconnected:withError:].cold.1
+ -[IOBluetoothL2CAPChannel peerL2CAPChannelConnected:error:].cold.1
+ -[IOBluetoothL2CAPChannel peerL2CAPChannelConnected:error:].cold.2
+ -[IOBluetoothL2CAPChannel peerL2CAPChannelConnected:error:].cold.3
+ -[IOBluetoothL2CAPChannel peerL2CAPChannelDisconnected:error:].cold.1
+ -[IOBluetoothL2CAPChannel registerForChannelCloseNotification:selector:].cold.1
+ -[IOBluetoothL2CAPChannel registerIncomingDataListener:refCon:].cold.1
+ -[IOBluetoothL2CAPChannel registerIncomingEventListener:refCon:].cold.1
+ -[IOBluetoothL2CAPChannel removeL2CAPChannelforDevice].cold.2
+ -[IOBluetoothL2CAPChannel removeL2CAPChannelforDevice].cold.3
+ -[IOBluetoothL2CAPChannel removeL2CAPChannelforDevice].cold.4
+ -[IOBluetoothL2CAPChannel setDelegate:].cold.1
+ -[IOBluetoothL2CAPChannel setupL2CAPChannelForDevice].cold.2
+ -[IOBluetoothL2CAPChannel setupL2CAPChannelForDevice].cold.3
+ -[IOBluetoothL2CAPChannel setupL2CAPChannelForDevice].cold.4
+ -[IOBluetoothL2CAPChannel stream:handleEvent:].cold.1
+ -[IOBluetoothL2CAPChannel stream:handleEvent:].cold.2
+ -[IOBluetoothL2CAPChannel stream:handleEvent:].cold.3
+ -[IOBluetoothL2CAPChannel stream:handleEvent:].cold.4
+ -[IOBluetoothL2CAPChannel waitforChanneOpen].cold.2
+ -[IOBluetoothL2CAPChannel waitforChanneOpen].cold.3
+ -[IOBluetoothL2CAPChannel writeAsync:length:refcon:].cold.4
+ -[IOBluetoothL2CAPChannel writeAsync:length:refcon:].cold.5
+ -[IOBluetoothL2CAPChannel writeAsync:length:refcon:].cold.6
+ -[IOBluetoothL2CAPChannel writeAsyncTrap:length:refcon:].cold.2
+ -[IOBluetoothL2CAPChannel writeSync:length:].cold.5
+ -[IOBluetoothL2CAPChannel writeSync:length:].cold.6
+ -[IOBluetoothL2CAPChannel writeSync:length:].cold.7
+ -[IOBluetoothL2CAPChannel writeSync:length:].cold.8
+ -[IOBluetoothNSCUserNotification initWithCallback:refCon:name:object:].cold.1
+ -[IOBluetoothNSObjCUserNotification initWithObserver:selector:name:object:].cold.1
+ -[IOBluetoothRFCOMMChannel _initWithDevice:andClassicPeer:channelID:withServiceUUID:delegate:].cold.2
+ -[IOBluetoothRFCOMMChannel _initWithDevice:andClassicPeer:channelID:withServiceUUID:delegate:].cold.3
+ -[IOBluetoothRFCOMMChannel _initWithDevice:andClassicPeer:channelID:withServiceUUID:delegate:].cold.4
+ -[IOBluetoothRFCOMMChannel _initWithDevice:andClassicPeer:channelID:withServiceUUID:delegate:].cold.5
+ -[IOBluetoothRFCOMMChannel _initWithDevice:andClassicPeer:channelID:withServiceUUID:delegate:].cold.6
+ -[IOBluetoothRFCOMMChannel closeChannel].cold.1
+ -[IOBluetoothRFCOMMChannel dealloc].cold.1
+ -[IOBluetoothRFCOMMChannel initWithCBRFCOMMChannel:delegate:].cold.3
+ -[IOBluetoothRFCOMMChannel initWithCBRFCOMMChannel:delegate:].cold.4
+ -[IOBluetoothRFCOMMChannel initWithDevice:andClassicPeer:channelID:delegate:].cold.4
+ -[IOBluetoothRFCOMMChannel initWithDevice:andClassicPeer:channelID:delegate:].cold.5
+ -[IOBluetoothRFCOMMChannel initWithDevice:andClassicPeer:channelID:delegate:].cold.6
+ -[IOBluetoothRFCOMMChannel peerConnected:error:].cold.1
+ -[IOBluetoothRFCOMMChannel peerConnected:error:].cold.2
+ -[IOBluetoothRFCOMMChannel peerDisconnected:withError:].cold.1
+ -[IOBluetoothRFCOMMChannel peerRFCOMMChannelConnected:error:].cold.1
+ -[IOBluetoothRFCOMMChannel peerRFCOMMChannelConnected:error:].cold.2
+ -[IOBluetoothRFCOMMChannel peerRFCOMMChannelConnected:error:].cold.3
+ -[IOBluetoothRFCOMMChannel peerRFCOMMChannelDisconnected:error:].cold.1
+ -[IOBluetoothRFCOMMChannel registerForChannelCloseNotification:selector:].cold.2
+ -[IOBluetoothRFCOMMChannel registerForChannelCloseNotification:selector:].cold.3
+ -[IOBluetoothRFCOMMChannel removeRFCOMMChannelforDevice].cold.2
+ -[IOBluetoothRFCOMMChannel removeRFCOMMChannelforDevice].cold.3
+ -[IOBluetoothRFCOMMChannel removeRFCOMMChannelforDevice].cold.4
+ -[IOBluetoothRFCOMMChannel setSerialParameters:dataBits:parity:stopBits:].cold.1
+ -[IOBluetoothRFCOMMChannel setupRFCOMMChannelForDevice].cold.2
+ -[IOBluetoothRFCOMMChannel setupRFCOMMChannelForDevice].cold.3
+ -[IOBluetoothRFCOMMChannel setupRFCOMMChannelForDevice].cold.4
+ -[IOBluetoothRFCOMMChannel setupRFCOMMChannelForDevice].cold.5
+ -[IOBluetoothRFCOMMChannel stream:handleEvent:].cold.1
+ -[IOBluetoothRFCOMMChannel stream:handleEvent:].cold.2
+ -[IOBluetoothRFCOMMChannel stream:handleEvent:].cold.3
+ -[IOBluetoothRFCOMMChannel stream:handleEvent:].cold.4
+ -[IOBluetoothRFCOMMChannel waitforChanneOpen].cold.2
+ -[IOBluetoothRFCOMMChannel waitforChanneOpen].cold.3
+ -[IOBluetoothRFCOMMChannel waitforChanneOpen].cold.4
+ -[IOBluetoothRFCOMMChannel writeAsync:length:refcon:].cold.3
+ -[IOBluetoothRFCOMMChannel writeAsync:length:refcon:].cold.4
+ -[IOBluetoothRFCOMMChannel writeSimple:length:sleep:bytesSent:].cold.2
+ -[IOBluetoothRFCOMMChannel writeSync:length:].cold.5
+ -[IOBluetoothRFCOMMChannel writeSync:length:].cold.6
+ -[IOBluetoothRFCOMMChannel writeSync:length:].cold.7
+ -[IOBluetoothRFCOMMChannel writeSync:length:].cold.8
+ -[IOBluetoothSDPServiceRecord hasServiceFromArray:].cold.2
+ -[IOBluetoothSDPServiceRecord initWithServiceDictionary:device:].cold.2
+ -[IOBluetoothSDPServiceRecord initWithServiceDictionary:device:].cold.3
+ -[IOBluetoothSDPServiceRecord initWithServiceDictionary:device:].cold.4
+ -[IOBluetoothSDPServiceRecord matchesSearchArray:].cold.2
+ BTNSObjectFromXPCObject.cold.2
+ BluetoothHCISetupUserClient.cold.1
+ FileHasResourceFork.cold.1
+ IOBluetoothBroadcomSchedulerWorkaround.cold.10
+ IOBluetoothBroadcomSchedulerWorkaround.cold.11
+ IOBluetoothBroadcomSchedulerWorkaround.cold.12
+ IOBluetoothBroadcomSchedulerWorkaround.cold.13
+ IOBluetoothBroadcomSchedulerWorkaround.cold.2
+ IOBluetoothBroadcomSchedulerWorkaround.cold.3
+ IOBluetoothBroadcomSchedulerWorkaround.cold.4
+ IOBluetoothBroadcomSchedulerWorkaround.cold.5
+ IOBluetoothBroadcomSchedulerWorkaround.cold.6
+ IOBluetoothBroadcomSchedulerWorkaround.cold.7
+ IOBluetoothBroadcomSchedulerWorkaround.cold.8
+ IOBluetoothBroadcomSchedulerWorkaround.cold.9
+ IOBluetoothDeviceRegisterForDisconnectNotification.cold.1
+ IOBluetoothFindNumberOfRegistryEntriesOfClassName.cold.2
+ IOBluetoothFindNumberOfRegistryEntriesOfClassName.cold.3
+ IOBluetoothFindNumberOfRegistryEntriesOfClassName.cold.4
+ IOBluetoothFindNumberOfRegistryEntriesOfClassName.cold.5
+ IOBluetoothFrameworkInit.cold.1
+ IOBluetoothIsMachinePortable.cold.1
+ IOBluetoothL2CAPChannelRegisterForChannelCloseNotification.cold.1
+ IOBluetoothPreferenceGetControllerPowerState.cold.2
+ IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications.cold.1
+ IOBluetoothRegisterForL2CAPChannelOpenNotifications.cold.1
+ IOBluetoothRegisterForNotifications.cold.2
+ IOBluetoothRegisterForNotifications.cold.3
+ IOBluetoothSecureBluetooth.cold.1
+ ReturnAllCurrentL2Channels.cold.2
+ ReturnAllCurrentRFCOMMChannels.cold.2
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ __37-[IOBluetoothDevice performSDPQuery:]_block_invoke.cold.1
+ __41-[IOBluetoothDevice peerConnected:error:]_block_invoke.cold.1
+ __43-[IOBluetoothCoreBluetoothCoordinator init]_block_invoke.14.cold.1
+ __43-[IOBluetoothCoreBluetoothCoordinator init]_block_invoke.16.cold.1
+ __43-[IOBluetoothCoreBluetoothCoordinator init]_block_invoke.17.cold.1
+ __43-[IOBluetoothCoreBluetoothCoordinator init]_block_invoke.21.cold.1
+ __43-[IOBluetoothCoreBluetoothCoordinator init]_block_invoke.cold.1
+ __43-[IOBluetoothCoreBluetoothCoordinator init]_block_invoke.cold.2
+ __43-[IOBluetoothCoreBluetoothCoordinator init]_block_invoke.cold.3
+ __46-[IOBluetoothL2CAPChannel stream:handleEvent:]_block_invoke.98.cold.2
+ __46-[IOBluetoothL2CAPChannel stream:handleEvent:]_block_invoke.98.cold.3
+ __46-[IOBluetoothL2CAPChannel stream:handleEvent:]_block_invoke.cold.4
+ __46-[IOBluetoothL2CAPChannel stream:handleEvent:]_block_invoke.cold.5
+ __46-[IOBluetoothL2CAPChannel stream:handleEvent:]_block_invoke.cold.6
+ __47-[IOBluetoothAutomaticDeviceSetup startInquiry]_block_invoke.cold.1
+ __47-[IOBluetoothAutomaticDeviceSetup startInquiry]_block_invoke.cold.2
+ __47-[IOBluetoothAutomaticDeviceSetup startLEScans]_block_invoke.cold.1
+ __47-[IOBluetoothRFCOMMChannel stream:handleEvent:]_block_invoke.42.cold.2
+ __47-[IOBluetoothRFCOMMChannel stream:handleEvent:]_block_invoke.cold.4
+ __47-[IOBluetoothRFCOMMChannel stream:handleEvent:]_block_invoke.cold.5
+ __47-[IOBluetoothRFCOMMChannel stream:handleEvent:]_block_invoke.cold.6
+ __48-[IOBluetoothDevice peerDisconnected:withError:]_block_invoke.cold.1
+ __48-[IOBluetoothDevice peerDiscovered:withResults:]_block_invoke.cold.1
+ __48-[IOBluetoothDeviceInquiry inquiryStateChanged:]_block_invoke.cold.1
+ __51-[IOBluetoothCoreBluetoothCoordinator stopScanning]_block_invoke.cold.2
+ __51-[IOBluetoothCoreBluetoothCoordinator stopScanning]_block_invoke.cold.3
+ __52-[IOBluetoothL2CAPChannel writeAsync:length:refcon:]_block_invoke.cold.1
+ __53-[IOBluetoothCoreBluetoothCoordinator startScanning:]_block_invoke.32.cold.2
+ __53-[IOBluetoothCoreBluetoothCoordinator startScanning:]_block_invoke.cold.2
+ __53-[IOBluetoothCoreBluetoothCoordinator startScanning:]_block_invoke.cold.3
+ __53-[IOBluetoothL2CAPChannel connectionComplete:status:]_block_invoke.cold.1
+ __53-[IOBluetoothL2CAPChannel setupL2CAPChannelForDevice]_block_invoke.cold.1
+ __53-[IOBluetoothRFCOMMChannel writeAsync:length:refcon:]_block_invoke.cold.4
+ __53-[IOBluetoothRFCOMMChannel writeAsync:length:refcon:]_block_invoke.cold.5
+ __53-[IOBluetoothRFCOMMChannel writeAsync:length:refcon:]_block_invoke.cold.6
+ __54-[IOBluetoothL2CAPChannel removeL2CAPChannelforDevice]_block_invoke.cold.1
+ __55-[IOBluetoothRFCOMMChannel setupRFCOMMChannelForDevice]_block_invoke.cold.1
+ __56-[IOBluetoothRFCOMMChannel removeRFCOMMChannelforDevice]_block_invoke.cold.1
+ __59-[IOBluetoothDevice callConnectionCompleteCallback:status:]_block_invoke.cold.1
+ __60-[IOBluetoothCoreBluetoothCoordinator updateBTPowerStateTo:]_block_invoke.cold.2
+ __60-[IOBluetoothCoreBluetoothCoordinator updateBTPowerStateTo:]_block_invoke.cold.3
+ __62-[IOBluetoothCoreBluetoothCoordinator updateConnectableState:]_block_invoke.cold.2
+ __63-[IOBluetoothCoreBluetoothCoordinator updateDiscoverableState:]_block_invoke.cold.2
+ __63-[IOBluetoothRFCOMMChannel writeSimple:length:sleep:bytesSent:]_block_invoke.cold.3
+ __63-[IOBluetoothRFCOMMChannel writeSimple:length:sleep:bytesSent:]_block_invoke.cold.4
+ __68-[IOBluetoothCoreBluetoothCoordinator centralManagerDidUpdateState:]_block_invoke.cold.1
+ __71-[IOBluetoothConcreteUserNotification peerL2CAPChannelConnected:error:]_block_invoke.cold.1
+ __86-[IOBluetoothCoreBluetoothCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke.62.cold.1
+ __86-[IOBluetoothCoreBluetoothCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.1
+ __94-[IOBluetoothRFCOMMChannel _initWithDevice:andClassicPeer:channelID:withServiceUUID:delegate:]_block_invoke.14.cold.1
+ __94-[IOBluetoothRFCOMMChannel _initWithDevice:andClassicPeer:channelID:withServiceUUID:delegate:]_block_invoke.cold.1
+ internetSharingIsEnabledForBluetooth.cold.1
+ internetSharingIsEnabledForBluetooth.cold.2
- -[IOBluetoothDeviceInquiry abort].cold.1
- -[IOBluetoothDeviceInquiry startInquiryInDaemon].cold.1
- -[IOBluetoothDeviceInquiry start].cold.1
- -[IOBluetoothDeviceInquiry stop].cold.1
- _strncmp
CStrings:
+ "/AppleInternal/Library/BuildRoots/d4447ec1-02f4-11f0-bf02-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileBluetoothFramework/macOS/IOBluetoothFramework/Profiles/HCRP/HardcopyCableReplacement.m"
- "/AppleInternal/Library/BuildRoots/c0edb659-d02e-11ef-97ed-7675e0905095/Library/Caches/com.apple.xbs/Sources/MobileBluetoothFramework/macOS/IOBluetoothFramework/Profiles/HCRP/HardcopyCableReplacement.m"

```
