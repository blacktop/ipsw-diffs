## VoiceOverServices

> `/System/iOSSupport/System/Library/PrivateFrameworks/VoiceOverServices.framework/Versions/A/VoiceOverServices`

```diff

-3132.5.0.1.0
-  __TEXT.__text: 0x259e4
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x24dc
-  __TEXT.__cstring: 0x58e0
-  __TEXT.__const: 0x40
+3130.1.0.0.0
+  __TEXT.__text: 0x2bf2c
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x294c
+  __TEXT.__cstring: 0x68b5
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__oslogstring: 0x2f1
+  __TEXT.__oslogstring: 0x715
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x570
-  __TEXT.__objc_classname: 0x27f
-  __TEXT.__objc_methname: 0x4710
-  __TEXT.__objc_methtype: 0x3b8
-  __TEXT.__objc_stubs: 0x5080
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x378
+  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__objc_classname: 0x2e7
+  __TEXT.__objc_methname: 0x5883
+  __TEXT.__objc_methtype: 0xbfd
+  __TEXT.__objc_stubs: 0x5980
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16b0
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__const: 0x2cc0
-  __AUTH_CONST.__cfstring: 0x6b00
-  __AUTH_CONST.__objc_const: 0x3c30
-  __AUTH_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_selrefs: 0x19a8
+  __DATA_CONST.__objc_superrefs: 0x98
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__const: 0x2ce0
+  __AUTH_CONST.__cfstring: 0x7580
+  __AUTH_CONST.__objc_const: 0x4668
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0xf4
-  __DATA.__data: 0xca8
-  __DATA.__bss: 0x1630
+  __AUTH.__data: 0x60
+  __DATA.__objc_ivar: 0x13c
+  __DATA.__data: 0xe28
+  __DATA.__bss: 0x1648
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1177
-  Symbols:   3654
-  CStrings:  875
+  Functions: 1289
+  Symbols:   3961
+  CStrings:  961
 
Symbols:
+ +[VOSBluetoothManager lastInitError]
+ +[VOSCommand ToggleAudioDucking]
+ -[VOSBluetoothDevice .cxx_destruct]
+ -[VOSBluetoothDevice _clearName]
+ -[VOSBluetoothDevice acceptSSP:]
+ -[VOSBluetoothDevice address]
+ -[VOSBluetoothDevice authorizedServices]
+ -[VOSBluetoothDevice compare:]
+ -[VOSBluetoothDevice connectWithServices:]
+ -[VOSBluetoothDevice connect]
+ -[VOSBluetoothDevice connectedServicesCount]
+ -[VOSBluetoothDevice connectedServices]
+ -[VOSBluetoothDevice connected]
+ -[VOSBluetoothDevice connecting]
+ -[VOSBluetoothDevice copyWithZone:]
+ -[VOSBluetoothDevice description]
+ -[VOSBluetoothDevice deviceClass]
+ -[VOSBluetoothDevice device]
+ -[VOSBluetoothDevice disconnect]
+ -[VOSBluetoothDevice hasAddress:]
+ -[VOSBluetoothDevice hash]
+ -[VOSBluetoothDevice identifier]
+ -[VOSBluetoothDevice initWithDevice:address:]
+ -[VOSBluetoothDevice isAppleHIDDevice]
+ -[VOSBluetoothDevice isEqual:]
+ -[VOSBluetoothDevice isEqualToDevice:]
+ -[VOSBluetoothDevice isNameCached]
+ -[VOSBluetoothDevice isServiceSupported:]
+ -[VOSBluetoothDevice majorClass]
+ -[VOSBluetoothDevice minorClass]
+ -[VOSBluetoothDevice name]
+ -[VOSBluetoothDevice paired]
+ -[VOSBluetoothDevice productId]
+ -[VOSBluetoothDevice setDevice:]
+ -[VOSBluetoothDevice setPIN:]
+ -[VOSBluetoothDevice type]
+ -[VOSBluetoothDevice unpair]
+ -[VOSBluetoothDevice vendorId]
+ -[VOSBluetoothManager _attach:]
+ -[VOSBluetoothManager _cleanup:]
+ -[VOSBluetoothManager _connectabilityChanged]
+ -[VOSBluetoothManager _connectedStatusChanged]
+ -[VOSBluetoothManager _discoveryStateChanged]
+ -[VOSBluetoothManager _onlySensorsConnected]
+ -[VOSBluetoothManager _postNotification:]
+ -[VOSBluetoothManager _postNotificationWithArray:]
+ -[VOSBluetoothManager _powerChanged]
+ -[VOSBluetoothManager _removeDevice:]
+ -[VOSBluetoothManager _restartScan]
+ -[VOSBluetoothManager _setDiscoveryAgentScanning:]
+ -[VOSBluetoothManager _setup:]
+ -[VOSBluetoothManager _updateCentralManagerScan]
+ -[VOSBluetoothManager acceptSSP:forDevice:]
+ -[VOSBluetoothManager addDeviceIfNeeded:]
+ -[VOSBluetoothManager audioConnected]
+ -[VOSBluetoothManager authorizedServicesForDevice:]
+ -[VOSBluetoothManager authorizedServices]
+ -[VOSBluetoothManager available]
+ -[VOSBluetoothManager cancelPairing]
+ -[VOSBluetoothManager centralManagerDidUpdateState:]
+ -[VOSBluetoothManager centralManagerReadyCallback]
+ -[VOSBluetoothManager centralManager]
+ -[VOSBluetoothManager connectDevice:]
+ -[VOSBluetoothManager connectDevice:withServices:]
+ -[VOSBluetoothManager connectable]
+ -[VOSBluetoothManager connected]
+ -[VOSBluetoothManager connectingDevices]
+ -[VOSBluetoothManager dealloc]
+ -[VOSBluetoothManager deviceForPeripheral:]
+ -[VOSBluetoothManager devicePairingEnabled]
+ -[VOSBluetoothManager deviceScanningEnabled]
+ -[VOSBluetoothManager enabled]
+ -[VOSBluetoothManager init]
+ -[VOSBluetoothManager isAnyoneScanning]
+ -[VOSBluetoothManager isDiscoverable]
+ -[VOSBluetoothManager isServiceSupported:]
+ -[VOSBluetoothManager pairedBTLEDevices]
+ -[VOSBluetoothManager pairedDevices]
+ -[VOSBluetoothManager postNotification:]
+ -[VOSBluetoothManager postNotificationName:object:]
+ -[VOSBluetoothManager postNotificationName:object:error:]
+ -[VOSBluetoothManager powerState]
+ -[VOSBluetoothManager powered]
+ -[VOSBluetoothManager resetDeviceScanning]
+ -[VOSBluetoothManager setAudioConnected:]
+ -[VOSBluetoothManager setAuthorizedServices:]
+ -[VOSBluetoothManager setCentralManager:]
+ -[VOSBluetoothManager setCentralManagerReadyCallback:]
+ -[VOSBluetoothManager setConnectable:]
+ -[VOSBluetoothManager setDevicePairingEnabled:]
+ -[VOSBluetoothManager setDeviceScanningEnabled:]
+ -[VOSBluetoothManager setDiscoverable:]
+ -[VOSBluetoothManager setEnabled:]
+ -[VOSBluetoothManager setPincode:forDevice:]
+ -[VOSBluetoothManager setPowered:]
+ -[VOSBluetoothManager wasDeviceDiscovered:]
+ GCC_except_table74
+ OBJC_IVAR_$_VOSBluetoothDevice._address
+ OBJC_IVAR_$_VOSBluetoothDevice._device
+ OBJC_IVAR_$_VOSBluetoothDevice._name
+ OBJC_IVAR_$_VOSBluetoothManager._audioConnected
+ OBJC_IVAR_$_VOSBluetoothManager._authorizedServices
+ OBJC_IVAR_$_VOSBluetoothManager._available
+ OBJC_IVAR_$_VOSBluetoothManager._btAddrDict
+ OBJC_IVAR_$_VOSBluetoothManager._btDeviceDict
+ OBJC_IVAR_$_VOSBluetoothManager._btleDevices
+ OBJC_IVAR_$_VOSBluetoothManager._centralManager
+ OBJC_IVAR_$_VOSBluetoothManager._centralManagerReadyCallback
+ OBJC_IVAR_$_VOSBluetoothManager._discoveryAgent
+ OBJC_IVAR_$_VOSBluetoothManager._localDevice
+ OBJC_IVAR_$_VOSBluetoothManager._pairingAgent
+ OBJC_IVAR_$_VOSBluetoothManager._scanningEnabled
+ OBJC_IVAR_$_VOSBluetoothManager._session
+ OBJC_IVAR_$_VOSBluetoothManager._wantsDiscoveryEnabled
+ OBJC_IVAR_$_VOSBluetoothManager._wantsScanningEnabled
+ ToggleAudioDucking._Command
+ ToggleAudioDucking.onceToken
+ _AXPerformBlockAsynchronouslyOnMainThread
+ _BTDeviceConnectServices
+ _BTDeviceDisconnect
+ _BTDeviceGetAddressString
+ _BTDeviceGetAuthorizedServices
+ _BTDeviceGetConnectedServices
+ _BTDeviceGetDefaultName
+ _BTDeviceGetDeviceClass
+ _BTDeviceGetDeviceId
+ _BTDeviceGetDeviceType
+ _BTDeviceGetName
+ _BTDeviceGetPairingStatus
+ _BTDeviceGetSupportedServices
+ _BTDiscoveryAgentCreate
+ _BTDiscoveryAgentDestroy
+ _BTDiscoveryAgentGetDevices
+ _BTDiscoveryAgentStartScan
+ _BTDiscoveryAgentStopScan
+ _BTLocalDeviceAddCallbacks
+ _BTLocalDeviceGetConnectable
+ _BTLocalDeviceGetConnectedDevices
+ _BTLocalDeviceGetConnectingDevices
+ _BTLocalDeviceGetConnectionStatus
+ _BTLocalDeviceGetDefault
+ _BTLocalDeviceGetDiscoverable
+ _BTLocalDeviceGetModulePower
+ _BTLocalDeviceGetPairedDevices
+ _BTLocalDeviceGetScanning
+ _BTLocalDeviceRemoveCallbacks
+ _BTLocalDeviceSetConnectable
+ _BTLocalDeviceSetDiscoverable
+ _BTLocalDeviceSetModulePower
+ _BTLocalDeviceSupportsService
+ _BTPairingAgentAcceptSSP
+ _BTPairingAgentCancelPairing
+ _BTPairingAgentCreate
+ _BTPairingAgentDeletePairedDevice
+ _BTPairingAgentDestroy
+ _BTPairingAgentSetPincode
+ _BTPairingAgentStart
+ _BTPairingAgentStop
+ _BTServiceAddCallbacks
+ _BTServiceRemoveCallbacks
+ _BTSessionAttachWithQueue
+ _BTSessionDetachWithQueue
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
+ _DiscoveryAgentCallbacks
+ _LocalDeviceCallbacks
+ _NSLog
+ _OBJC_CLASS_$_BluetoothDevice
+ _OBJC_CLASS_$_BluetoothManager
+ _OBJC_CLASS_$_CBCentralManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNotificationCenter
+ _PairingAgentCallbacks
+ _SessionCallbacks
+ _VOSAddressForBTDevice
+ _VOSBluetoothAvailabilityChangedNotification
+ _VOSBluetoothConnectabilityChangedNotification
+ _VOSBluetoothConnectionStatusChangedNotification
+ _VOSBluetoothCoreBluetoothManagerReadyNotification
+ _VOSBluetoothDeviceConnectFailedNotification
+ _VOSBluetoothDeviceConnectSuccessNotification
+ _VOSBluetoothDeviceDisconnectFailedNotification
+ _VOSBluetoothDeviceDisconnectSuccessNotification
+ _VOSBluetoothDeviceDiscoveredNotification
+ _VOSBluetoothDeviceRemovedNotification
+ _VOSBluetoothDeviceUpdatedNotification
+ _VOSBluetoothDiscoveryStateChangedNotification
+ _VOSBluetoothErrorKey
+ _VOSBluetoothNotificationNameKey
+ _VOSBluetoothPairingPINRequestNotification
+ _VOSBluetoothPairingPINResultFailedNotification
+ _VOSBluetoothPairingPINResultSuccessNotification
+ _VOSBluetoothPairingPassKeyDisplayNotification
+ _VOSBluetoothPairingUserConfirmationNotification
+ _VOSBluetoothPairingUserNumericComparisionNotification
+ _VOSBluetoothPowerChangedNotification
+ __OBJC_$_INSTANCE_METHODS_VOSBluetoothDevice
+ __OBJC_$_INSTANCE_VARIABLES_VOSBluetoothDevice
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBCentralManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBCentralManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBCentralManagerPrivateDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBPairingAgentDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBPeripheralDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBCentralManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBCentralManagerPrivateDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBPairingAgentDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBPeripheralDelegate
+ __OBJC_$_PROTOCOL_REFS_CBCentralManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CBCentralManagerPrivateDelegate
+ __OBJC_$_PROTOCOL_REFS_CBPairingAgentDelegate
+ __OBJC_$_PROTOCOL_REFS_CBPeripheralDelegate
+ __OBJC_CLASS_PROTOCOLS_$_VOSBluetoothLowEnergyDevice
+ __OBJC_CLASS_PROTOCOLS_$_VOSBluetoothManager
+ __OBJC_LABEL_PROTOCOL_$_CBCentralManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CBCentralManagerPrivateDelegate
+ __OBJC_LABEL_PROTOCOL_$_CBPairingAgentDelegate
+ __OBJC_LABEL_PROTOCOL_$_CBPeripheralDelegate
+ __OBJC_PROTOCOL_$_CBCentralManagerDelegate
+ __OBJC_PROTOCOL_$_CBCentralManagerPrivateDelegate
+ __OBJC_PROTOCOL_$_CBPairingAgentDelegate
+ __OBJC_PROTOCOL_$_CBPeripheralDelegate
+ ___32+[VOSCommand ToggleAudioDucking]_block_invoke
+ ___40-[VOSBluetoothManager postNotification:]_block_invoke
+ ___51-[VOSBluetoothManager postNotificationName:object:]_block_invoke
+ ___57-[VOSBluetoothManager postNotificationName:object:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ __block_literal_global.1246
+ __block_literal_global.418
+ __btDiscoveryEventCallback
+ __btDiscoveryStatusEventCallback
+ __btLocalStatusEventCallback
+ __btServiceEventCallback
+ __btSessionEventCallback
+ __dispatch_main_q
+ __lastInitError
+ _getpid
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kVOTEventCommandToggleAudioDucking
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$ToggleAudioDucking
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_attach:
+ _objc_msgSend$_cleanup:
+ _objc_msgSend$_clearName
+ _objc_msgSend$_connectabilityChanged
+ _objc_msgSend$_connectedStatusChanged
+ _objc_msgSend$_discoveryStateChanged
+ _objc_msgSend$_onlySensorsConnected
+ _objc_msgSend$_postNotification:
+ _objc_msgSend$_postNotificationWithArray:
+ _objc_msgSend$_powerChanged
+ _objc_msgSend$_removeDevice:
+ _objc_msgSend$_restartScan
+ _objc_msgSend$_setDiscoveryAgentScanning:
+ _objc_msgSend$_setup:
+ _objc_msgSend$_updateCentralManagerScan
+ _objc_msgSend$acceptSSP:forDevice:
+ _objc_msgSend$addDeviceIfNeeded:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$authorizedServices
+ _objc_msgSend$authorizedServicesForDevice:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$cancelPairing
+ _objc_msgSend$connectDevice:
+ _objc_msgSend$connectDevice:withServices:
+ _objc_msgSend$connectedServicesCount
+ _objc_msgSend$connectingDevices
+ _objc_msgSend$containsString:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$device
+ _objc_msgSend$deviceForPeripheral:
+ _objc_msgSend$devicePairingEnabled
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$initWithDelegate:queue:options:
+ _objc_msgSend$initWithDevice:address:
+ _objc_msgSend$initWithPeripheral:manager:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqualToDevice:
+ _objc_msgSend$isNameCached
+ _objc_msgSend$isPairedDeviceBrailleDisplay:
+ _objc_msgSend$isPeerPaired:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$performSelector:withObject:afterDelay:
+ _objc_msgSend$postNotification:
+ _objc_msgSend$postNotificationName:object:error:
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$powerState
+ _objc_msgSend$powered
+ _objc_msgSend$productId
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$retrieveConnectedPeripheralsWithServices:allowAll:
+ _objc_msgSend$setAudioConnected:
+ _objc_msgSend$setCentralManager:
+ _objc_msgSend$setDevice:
+ _objc_msgSend$setDevicePairingEnabled:
+ _objc_msgSend$setDeviceScanningEnabled:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPincode:forDevice:
+ _objc_msgSend$setPowered:
+ _objc_msgSend$sharedPairingAgent
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$type
+ _objc_msgSend$unpairDevice:
+ _objc_msgSend$unpairPeer:
+ _objc_msgSend$valueWithPointer:
+ _objc_msgSend$vendorId
+ _pairingAgentAuthorizationCallback
+ _pairingAgentPassKeyDisplayCallback
+ _pairingAgentPincodeCallback
+ _pairingAgentStatusEventCallback
+ _pairingAgentUserConfirmationCallback
- -[VOSBluetoothLowEnergyDevice setPeripheral:]
- GCC_except_table9
- _OBJC_CLASS_$_AXUIBluetoothDevice
- _OBJC_CLASS_$_AXUIBluetoothHelper
- _OBJC_METACLASS_$_AXUIBluetoothDevice
- _OBJC_METACLASS_$_AXUIBluetoothHelper
- _VOBTDriverLoadingError
- _VOBTGeneralError
- _VOBTInvalidPINCodeError
- _VOBTNoServiceError
- _kVOTEventCommandBottomEdgePanExtraLong
- _objc_msgSend$attach:
CStrings:
+ "%!@(MISSING)<%!p(MISSING)>: name:'%!@(MISSING)' address:'%!@(MISSING)' BTDevice:%!p(MISSING), type:%!d(MISSING)"
+ "%!d(MISSING)"
+ "Apple Pencil"
+ "BT: BTLocalDeviceGetConnectable returned error %!d(MISSING)"
+ "BT_SESSION_ATTACHED"
+ "BT_SESSION_DETACHED"
+ "BT_SESSION_FAILED"
+ "BT_SESSION_TERMINATED"
+ "OFF"
+ "ON"
+ "ToggleAudioDucking"
+ "VOBTM%!@(MISSING)-%!u(MISSING)"
+ "VOBTM: BTLocalDeviceGetConnectionStatus failed with error %!d(MISSING)"
+ "VOBTM: failed to get authorized services with error %!d(MISSING)"
+ "VOSBluetoothAvailabilityChangedNotification"
+ "VOSBluetoothConnectabilityChangedNotification"
+ "VOSBluetoothConnectionStatusChangedNotification"
+ "VOSBluetoothCoreBluetoothManagerReadyNotification"
+ "VOSBluetoothDeviceConnectFailedNotification"
+ "VOSBluetoothDeviceConnectSuccessNotification"
+ "VOSBluetoothDeviceDisconnectFailedNotification"
+ "VOSBluetoothDeviceDisconnectSuccessNotification"
+ "VOSBluetoothDeviceDiscoveredNotification"
+ "VOSBluetoothDeviceRemovedNotification"
+ "VOSBluetoothDeviceUnpairedNotification"
+ "VOSBluetoothDeviceUpdatedNotification"
+ "VOSBluetoothDiscoveryStateChangedNotification"
+ "VOSBluetoothErrorKey"
+ "VOSBluetoothNotificationNameKey"
+ "VOSBluetoothPairingPINRequestNotification"
+ "VOSBluetoothPairingPINResultFailedNotification"
+ "VOSBluetoothPairingPINResultSuccessNotification"
+ "VOSBluetoothPairingPassKeyDisplayNotification"
+ "VOSBluetoothPairingUserConfirmationNotification"
+ "VOSBluetoothPairingUserNumericComparisionNotification"
+ "VOSBluetoothPowerChangedNotification"
+ "VOTBTM: BTLocalDeviceGetConnectedDevices failed with error %!d(MISSING)"
+ "VOTBTM: BTLocalDeviceGetConnectingDevices returned %!z(MISSING)d devices"
+ "VOTBTM: BTLocalDeviceGetDiscoverable returned error %!d(MISSING)"
+ "VOTBTM: BTLocalDeviceGetPairedDevices returned %!z(MISSING)d devices"
+ "VOTBTM: BTLocalDeviceGetScanning returned error %!d(MISSING)"
+ "VOTBTM: BTPairingAgentAcceptSSP returned error %!d(MISSING)"
+ "VOTBTM: Could not enable DiscoveryAgentScanning. session is nil"
+ "VOTBTM: _btServiceEventCallback: service = %!u(MISSING) eventType = %!d(MISSING) event = %!d(MISSING) result = %!d(MISSING)"
+ "VOTBTM: accepting SSP with error code %!l(MISSING)d for device %!{(MISSING)public}@"
+ "VOTBTM: connecting services 0x%!x(MISSING) to device %!{(MISSING)public}@"
+ "VOTBTM: connecting to device %!{(MISSING)public}@ failed with error %!d(MISSING)"
+ "VOTBTM: discovery agent creation failed with error %!d(MISSING)"
+ "VOTBTM: failed to cancel pairing with error %!d(MISSING)"
+ "VOTBTM: failed to disconnect device \"%!{(MISSING)public}@\""
+ "VOTBTM: failed to get connecting devices with error %!d(MISSING)"
+ "VOTBTM: failed to get paired devices with error %!d(MISSING)"
+ "VOTBTM: failed to restart scanning with error %!d(MISSING)"
+ "VOTBTM: failed to start pairing agent with error %!d(MISSING)"
+ "VOTBTM: failed to start scanning with error %!d(MISSING)"
+ "VOTBTM: failed to unpair from device %!{(MISSING)public}@ with error %!d(MISSING)"
+ "VOTBTM: pairing agent creation failed with error %!d(MISSING)"
+ "VOTBTM: received BT_DISCOVERY_DEVICE_FOUND event for device %!{(MISSING)public}@"
+ "VOTBTM: received BT_DISCOVERY_DEVICE_LOST event for device %!{(MISSING)public}@"
+ "VOTBTM: received BT_PAIRING_AGENT_STARTED event"
+ "VOTBTM: received BT_PAIRING_AGENT_STOPPED event"
+ "VOTBTM: received BT_PAIRING_ATTEMPT_COMPLETE event for device %!{(MISSING)public}@ with result %!d(MISSING)"
+ "VOTBTM: received BT_PAIRING_ATTEMPT_STARTED event for device %!{(MISSING)public}@"
+ "VOTBTM: received BT_SERVICE_CONNECT event type with %!l(MISSING)u currently connected services"
+ "VOTBTM: received BT_SERVICE_CONNECTION_RESULT event with %!l(MISSING)u currently connected services"
+ "VOTBTM: received BT_SERVICE_DEPENDENT_EVENT event for BT_SERVICE_ALL"
+ "VOTBTM: received BT_SERVICE_DEPENDENT_EVENT event for BT_SERVICE_HANDSFREE"
+ "VOTBTM: received BT_SERVICE_DISCONNECT event type with %!l(MISSING)u currently connected services"
+ "VOTBTM: received BT_SERVICE_DISCONNECTION_RESULT event with %!l(MISSING)u currently connected services"
+ "VOTBTM: received passkey display request for device %!{(MISSING)public}@"
+ "VOTBTM: received pincode request for device %!{(MISSING)public}@"
+ "VOTBTM: received user confirmation request (numeric comparison to %!u(MISSING)) for device %!{(MISSING)public}@"
+ "VOTBTM: received user confirmation request for device %!{(MISSING)public}@"
+ "VOTBTM: result = %!d(MISSING)"
+ "VOTBTM: session attach called back with %!{(MISSING)public}@ (%!d(MISSING))"
+ "VOTBTM: setting connectable status %!{(MISSING)public}s"
+ "VOTBTM: setting device pairing %!{(MISSING)public}s"
+ "VOTBTM: setting discoverable status %!{(MISSING)public}s"
+ "VOTBTM: setting pincode %!{(MISSING)public}@ for device %!{(MISSING)public}@"
+ "VOTBTM: stopping discovery agent"
+ "VOTBTM: stopping pairing agent"
+ "VOTEventCommandToggleAudioDucking"
+ "com.apple.bluetooth.power-changed"
+ "device"
+ "disabled"
+ "enabled"
+ "value"
- "VOTEventCommandBottomEdgePanExtraLong"

```
