## VoiceOverServices

> `/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices`

```diff

-3093.2.4.0.2
-  __TEXT.__text: 0x32e8c
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x2c48
-  __TEXT.__cstring: 0x75c8
+3093.2.4.4.10
+  __TEXT.__text: 0x3308c
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_methlist: 0x2cd8
+  __TEXT.__cstring: 0x731f
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__oslogstring: 0x4ba
+  __TEXT.__oslogstring: 0x887
   __TEXT.__dlopen_cstrs: 0xf0
-  __TEXT.__unwind_info: 0x82c
-  __TEXT.__objc_classname: 0x2eb
-  __TEXT.__objc_methname: 0x61de
-  __TEXT.__objc_methtype: 0x5f7
-  __TEXT.__objc_stubs: 0x6f80
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__objc_classname: 0x350
+  __TEXT.__objc_methname: 0x6cca
+  __TEXT.__objc_methtype: 0xcc6
+  __TEXT.__objc_stubs: 0x7100
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3748
-  __DATA_CONST.__objc_selrefs: 0x1f40
+  __DATA_CONST.__objc_const: 0x3ec8
+  __DATA_CONST.__objc_selrefs: 0x1fc0
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x8620
+  __AUTH_CONST.__cfstring: 0x84a0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__const: 0x20e0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x4d0
-  __DATA.__objc_classrefs: 0x200
+  __AUTH_CONST.__auth_got: 0x4e8
+  __DATA.__objc_classrefs: 0x208
   __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x15c
-  __DATA.__data: 0xce0
+  __DATA.__objc_ivar: 0x168
+  __DATA.__data: 0xe60
   __DATA.__bss: 0x838
   __DATA_DIRTY.__const: 0x1020
   __DATA_DIRTY.__objc_const: 0xd38
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__bss: 0xf58
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1411
-  Symbols:   5806
-  CStrings:  2435
+  Functions: 1424
+  Symbols:   5875
+  CStrings:  2551
 
Symbols:
+ -[VOSBluetoothManager _removeDeviceFromBrailleCache:]
+ -[VOSBluetoothManager _updateCentralManagerScan]
+ -[VOSBluetoothManager btleDeviceIsPaired:]
+ -[VOSBluetoothManager centralManagerDidUpdateState:]
+ -[VOSBluetoothManager centralManagerReadyCallback]
+ -[VOSBluetoothManager centralManager]
+ -[VOSBluetoothManager deviceForPeripheral:]
+ -[VOSBluetoothManager isPairedDeviceBrailleDisplay:]
+ -[VOSBluetoothManager pairedBTLEDevices]
+ -[VOSBluetoothManager setCentralManager:]
+ -[VOSBluetoothManager setCentralManagerReadyCallback:]
+ -[VOSBluetoothManager unpairBTLEDevice:]
+ GCC_except_table77
+ _OBJC_CLASS_$_CBCentralManager
+ _OBJC_IVAR_$_VOSBluetoothManager._audioConnected
+ _OBJC_IVAR_$_VOSBluetoothManager._authorizedServices
+ _OBJC_IVAR_$_VOSBluetoothManager._available
+ _OBJC_IVAR_$_VOSBluetoothManager._btAddrDict
+ _OBJC_IVAR_$_VOSBluetoothManager._btDeviceDict
+ _OBJC_IVAR_$_VOSBluetoothManager._btleDevices
+ _OBJC_IVAR_$_VOSBluetoothManager._centralManager
+ _OBJC_IVAR_$_VOSBluetoothManager._centralManagerReadyCallback
+ _OBJC_IVAR_$_VOSBluetoothManager._discoveryAgent
+ _OBJC_IVAR_$_VOSBluetoothManager._localDevice
+ _OBJC_IVAR_$_VOSBluetoothManager._pairingAgent
+ _OBJC_IVAR_$_VOSBluetoothManager._scanningEnabled
+ _OBJC_IVAR_$_VOSBluetoothManager._session
+ _VOSBluetoothCoreBluetoothManagerReadyNotification
+ _VOTLogBraille
+ __AXSVoiceOverTouchCopyTactileGraphicsDisplay
+ __AXSVoiceOverTouchSetTactileGraphicsDisplay
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
+ __OBJC_CLASS_PROTOCOLS_$_VOSBluetoothManager
+ __OBJC_LABEL_PROTOCOL_$_CBCentralManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CBCentralManagerPrivateDelegate
+ __OBJC_LABEL_PROTOCOL_$_CBPairingAgentDelegate
+ __OBJC_LABEL_PROTOCOL_$_CBPeripheralDelegate
+ __OBJC_PROTOCOL_$_CBCentralManagerDelegate
+ __OBJC_PROTOCOL_$_CBCentralManagerPrivateDelegate
+ __OBJC_PROTOCOL_$_CBPairingAgentDelegate
+ __OBJC_PROTOCOL_$_CBPeripheralDelegate
+ ___42-[VOSBluetoothManager btleDeviceIsPaired:]_block_invoke
+ ___53-[VOSBluetoothManager _removeDeviceFromBrailleCache:]_block_invoke
+ ___block_descriptor_40_e8_32s_e22_B16?0"NSDictionary"8ls32l8
+ _objc_msgSend$_removeDeviceFromBrailleCache:
+ _objc_msgSend$_updateCentralManagerScan
+ _objc_msgSend$ax_containsObjectUsingBlock:
+ _objc_msgSend$btleDeviceIsPaired:
+ _objc_msgSend$cancelPeripheralConnection:options:
+ _objc_msgSend$containsString:
+ _objc_msgSend$deviceForPeripheral:
+ _objc_msgSend$initWithDelegate:queue:options:
+ _objc_msgSend$initWithPeripheral:manager:
+ _objc_msgSend$isPairedDeviceBrailleDisplay:
+ _objc_msgSend$retrieveConnectedPeripheralsWithServices:allowAll:
+ _objc_msgSend$setCentralManager:
+ _objc_msgSend$state
+ _objc_msgSend$unpairBTLEDevice:
- GCC_except_table70
- OBJC_IVAR_$_VOSBluetoothManager._audioConnected
- OBJC_IVAR_$_VOSBluetoothManager._authorizedServices
- OBJC_IVAR_$_VOSBluetoothManager._available
- OBJC_IVAR_$_VOSBluetoothManager._btAddrDict
- OBJC_IVAR_$_VOSBluetoothManager._btDeviceDict
- OBJC_IVAR_$_VOSBluetoothManager._discoveryAgent
- OBJC_IVAR_$_VOSBluetoothManager._localDevice
- OBJC_IVAR_$_VOSBluetoothManager._pairingAgent
- OBJC_IVAR_$_VOSBluetoothManager._scanningEnabled
- OBJC_IVAR_$_VOSBluetoothManager._session
- ___36-[VOSBluetoothManager unpairDevice:]_block_invoke
- _objc_msgSend$cancelPeripheralConnection:
- _objc_msgSend$connected
CStrings:
+ "\x11e"
+ "@\"NSArray\"16@0:8"
+ "Apple Pencil"
+ "Attempt connect: Current peripheral state: %@"
+ "B16@?0@\"NSDictionary\"8"
+ "CBCentralManagerDelegate"
+ "CBCentralManagerPrivateDelegate"
+ "CBPairingAgentDelegate"
+ "CBPeripheralDelegate"
+ "Connecting: %@"
+ "Skipping paired device %@ because did not match paired Braille devices"
+ "T@\"CBCentralManager\",&,N,V_centralManager"
+ "T@?,C,N,V_centralManagerReadyCallback"
+ "Unpairing BTLE device: %@"
+ "VOSBluetoothCoreBluetoothManagerReadyNotification"
+ "VOTBTM: This was the tactile display, removing:"
+ "_btleDevices"
+ "_centralManagerReadyCallback"
+ "_removeDeviceFromBrailleCache:"
+ "_updateCentralManagerScan"
+ "ax_containsObjectUsingBlock:"
+ "btleDeviceIsPaired:"
+ "cancelPeripheralConnection:options:"
+ "centralManager:application:isActive:"
+ "centralManager:canSendDataToPeripheral:"
+ "centralManager:connectionEventDidOccur:forPeripheral:"
+ "centralManager:didChannelSoundingProcedureEvent:results:error:"
+ "centralManager:didConnectPeripheral:"
+ "centralManager:didDisconnectPeripheral:error:"
+ "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
+ "centralManager:didDiscoverMultiplePeripherals:"
+ "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
+ "centralManager:didFailToConnectPeripheral:error:"
+ "centralManager:didFailToScanWithError:"
+ "centralManager:didFindPeripheral:forType:"
+ "centralManager:didLosePeripheral:forType:"
+ "centralManager:didLoseZone:mask:"
+ "centralManager:didReceiveData:fromPeripheral:"
+ "centralManager:didSendBytes:toPeripheral:withError:"
+ "centralManager:didUpdateANCSAuthorizationForPeripheral:"
+ "centralManager:didUpdateConnectionParameters:interval:latency:supervisionTimeout:"
+ "centralManager:didUpdateControllerBTClockDictForPeripheral:results:"
+ "centralManager:didUpdateControllerBTClockForPeripheral:eventType:seconds:microseconds:localClock:remoteClock:"
+ "centralManager:didUpdateFindMyPeripherals:"
+ "centralManager:didUpdateMTUForPeripheral:"
+ "centralManager:didUpdatePeripheralConnectionState:"
+ "centralManager:didUpdateRSSIStatisticsDetectionForPeripheral:results:error:"
+ "centralManager:didUpdateScanParams:"
+ "centralManager:didUpdateUsageStatisticEvent:results:error:"
+ "centralManager:willRestoreState:"
+ "centralManagerDidUpdateState:"
+ "centralManagerReadyCallback"
+ "containsString:"
+ "deviceForPeripheral:"
+ "initWithDelegate:queue:options:"
+ "isPairedDeviceBrailleDisplay:"
+ "pairedBTLEDevices"
+ "pairingAgent:peerDidCompletePairing:"
+ "pairingAgent:peerDidFailToCompletePairing:error:"
+ "pairingAgent:peerDidRequestPairing:type:passkey:"
+ "pairingAgent:peerDidUnpair:"
+ "peripheral:didDiscoverCharacteristicsForService:error:"
+ "peripheral:didDiscoverDescriptorsForCharacteristic:error:"
+ "peripheral:didDiscoverIncludedServicesForService:error:"
+ "peripheral:didDiscoverServices:"
+ "peripheral:didModifyServices:"
+ "peripheral:didOpenL2CAPChannel:error:"
+ "peripheral:didReadRSSI:error:"
+ "peripheral:didUpdateNotificationStateForCharacteristic:error:"
+ "peripheral:didUpdateValueForCharacteristic:error:"
+ "peripheral:didUpdateValueForDescriptor:error:"
+ "peripheral:didWriteValueForCharacteristic:error:"
+ "peripheral:didWriteValueForDescriptor:error:"
+ "peripheralDidUpdateName:"
+ "peripheralDidUpdateRSSI:error:"
+ "peripheralIsReadyToSendWriteWithoutResponse:"
+ "retrieveConnectedPeripheralsWithServices:allowAll:"
+ "retrieveConnectingPeripherals"
+ "setCentralManager:"
+ "setCentralManagerReadyCallback:"
+ "state"
+ "unpairBTLEDevice:"
+ "v24@0:8@\"CBCentralManager\"16"
+ "v24@0:8@\"CBPeripheral\"16"
+ "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
+ "v32@0:8@\"CBCentralManager\"16@\"NSArray\"24"
+ "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
+ "v32@0:8@\"CBCentralManager\"16@\"NSError\"24"
+ "v32@0:8@\"CBPairingAgent\"16@\"CBPeer\"24"
+ "v32@0:8@\"CBPeripheral\"16@\"NSArray\"24"
+ "v32@0:8@\"CBPeripheral\"16@\"NSError\"24"
+ "v36@0:8@\"CBCentralManager\"16@\"NSString\"24B32"
+ "v36@0:8@16@24B32"
+ "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32"
+ "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
+ "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSNumber\"32"
+ "v40@0:8@\"CBCentralManager\"16@\"NSData\"24@\"CBPeripheral\"32"
+ "v40@0:8@\"CBCentralManager\"16@\"NSData\"24@\"NSData\"32"
+ "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
+ "v40@0:8@\"CBPairingAgent\"16@\"CBPeer\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBCharacteristic\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBDescriptor\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBL2CAPChannel\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBService\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"NSNumber\"24@\"NSError\"32"
+ "v40@0:8@16q24@32"
+ "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSError\"40"
+ "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
+ "v48@0:8@\"CBCentralManager\"16@\"NSNumber\"24@\"CBPeripheral\"32@\"NSError\"40"
+ "v48@0:8@\"CBPairingAgent\"16@\"CBPeer\"24q32@\"NSNumber\"40"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8@16@24q32@40"
+ "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
+ "v52@0:8@16@24d32B40@44"
+ "v56@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48"
+ "v56@0:8@16@24@32@40@48"
+ "v72@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64"
+ "v72@0:8@16@24@32@40@48@56@64"
- "b\x11"
- "cancelPeripheralConnection:"

```
