## ConnectivityModule

> `/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule`

```diff

-592.100.0.0.0
-  __TEXT.__text: 0x11568
+593.102.0.0.0
+  __TEXT.__text: 0xfdd4
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x1a44
+  __TEXT.__objc_methlist: 0x1924
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x204
-  __TEXT.__cstring: 0x12b9
-  __TEXT.__oslogstring: 0x85c
-  __TEXT.__unwind_info: 0x6c0
-  __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methname: 0x642e
-  __TEXT.__objc_methtype: 0x1758
-  __TEXT.__objc_stubs: 0x3b80
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xa8
+  __TEXT.__gcc_except_tab: 0x194
+  __TEXT.__cstring: 0x1215
+  __TEXT.__oslogstring: 0x85e
+  __TEXT.__unwind_info: 0x668
+  __TEXT.__objc_classname: 0x5a9
+  __TEXT.__objc_methname: 0x5b8c
+  __TEXT.__objc_methtype: 0x1277
+  __TEXT.__objc_stubs: 0x37e0
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12e0
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_selrefs: 0x11d8
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0x4728
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x1140
+  __AUTH_CONST.__objc_const: 0x4138
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x1a4
-  __DATA.__data: 0x7e0
-  __DATA_DIRTY.__objc_data: 0x550
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x198
+  __DATA.__data: 0x720
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 619
-  Symbols:   242
-  CStrings:  1394
+  Functions: 591
+  Symbols:   230
+  CStrings:  1292
 
Symbols:
- _BluetoothAvailabilityChangedNotification
- _BluetoothDeviceConnectFailedNotification
- _BluetoothDeviceConnectSuccessNotification
- _BluetoothDeviceDisconnectFailedNotification
- _BluetoothDeviceDisconnectSuccessNotification
- _BluetoothDeviceRemovedNotification
- _CBCentralManagerOptionShowPowerAlertKey
- _OBJC_CLASS_$_CBCentralManager
- _OBJC_CLASS_$_CCUIMenuModuleViewController
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_METACLASS_$_CCUIBluetoothMenuModuleViewController
- _OBJC_METACLASS_$_CCUIMenuModuleViewController
CStrings:
+ "ControlCenterUI+SystemModules"
+ "[Bluetooth (Connectivity)] Bluetooth connection status changed"
+ "[Bluetooth (Connectivity)] Bluetooth state changed"
+ "[Bluetooth (Connectivity)] Bluetooth state updated to %!{(MISSING)public}@ [ inoperative: %!d(MISSING) enabled: %!d(MISSING) useAlternateBackground: %!d(MISSING) subtitle: %!{(MISSING)private}@ ]"
+ "[Bluetooth (Connectivity)] Toggle Bluetooth state from %!{(MISSING)public}@"
+ "[Bluetooth (Connectivity)] Toggled Bluetooth state from %!{(MISSING)public}@ to %!{(MISSING)public}@"
- "\x04"
- "@\"CBCentralManager\""
- "@\"NSMutableSet\""
- "ASK_DISPLAY_NAME"
- "Bluetooth connection status changed"
- "Bluetooth connection status changed: %!{(MISSING)public}@"
- "Bluetooth device availability changed: %!{(MISSING)BOOL}d"
- "Bluetooth device removed: %!{(MISSING)public}@"
- "Bluetooth state changed"
- "Bluetooth state updated to %!{(MISSING)public}@ [ inoperative: %!d(MISSING) enabled: %!d(MISSING) useAlternateBackground: %!d(MISSING) subtitle: %!{(MISSING)private}@ ]"
- "CBCentralManagerDelegate"
- "CBCentralManagerPrivateDelegate"
- "CCUIAlwaysExpandedMenuModuleViewController"
- "CCUIBluetoothMenuModuleViewController"
- "CONTROL_CENTER_STATUS_BLUETOOTH_CONNECTED"
- "CONTROL_CENTER_STATUS_BLUETOOTH_SETTINGS"
- "DA_ASK_RETAIN_DEVICE"
- "Toggle Bluetooth state from %!{(MISSING)public}@"
- "Toggled Bluetooth state from %!{(MISSING)public}@ to %!{(MISSING)public}@"
- "_bluetoothAvailabilityChanged:"
- "_bluetoothDeviceConnectionStatusDidChange:"
- "_bluetoothDeviceRemoved:"
- "_busyIdentifiers"
- "_centralManager"
- "_menuItemForBluetoothDevice:"
- "_menuItemForBluetoothPeripheral:"
- "_shouldHideBluetoothPeripheral:"
- "_subtitleForConnected:"
- "_updateBluetoothMenuItems"
- "address"
- "cancelPeripheralConnection:"
- "centralManager:application:isActive:"
- "centralManager:canSendDataToPeripheral:"
- "centralManager:connectionEventDidOccur:forPeripheral:"
- "centralManager:didChannelSoundingProcedureEvent:results:error:"
- "centralManager:didConnectPeripheral:"
- "centralManager:didDisconnectPeripheral:error:"
- "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
- "centralManager:didDiscoverMultiplePeripherals:"
- "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
- "centralManager:didFailToConnectPeripheral:error:"
- "centralManager:didFailToScanWithError:"
- "centralManager:didFindPeripheral:forType:"
- "centralManager:didLosePeripheral:forType:"
- "centralManager:didLoseZone:mask:"
- "centralManager:didReceiveData:fromPeripheral:"
- "centralManager:didSendBytes:toPeripheral:withError:"
- "centralManager:didUpdateANCSAuthorizationForPeripheral:"
- "centralManager:didUpdateConnectionParameters:interval:latency:supervisionTimeout:"
- "centralManager:didUpdateControllerBTClockDictForPeripheral:results:"
- "centralManager:didUpdateControllerBTClockForPeripheral:eventType:seconds:microseconds:localClock:remoteClock:"
- "centralManager:didUpdateFindMyPeripherals:"
- "centralManager:didUpdateMTUForPeripheral:"
- "centralManager:didUpdatePeripheralConnectionState:"
- "centralManager:didUpdatePhyStatisticEvent:results:error:"
- "centralManager:didUpdateRSSIStatisticsDetectionForPeripheral:results:error:"
- "centralManager:didUpdateScanParams:"
- "centralManager:didUpdateUsageStatisticEvent:results:error:"
- "centralManager:willRestoreState:"
- "centralManagerDidUpdateState:"
- "connectPeripheral:options:"
- "connectedTransport"
- "containsObject:"
- "customProperty:"
- "hasTag:"
- "initWithDelegate:queue:options:"
- "isConnectedToSystem"
- "isPeerCloudPaired:"
- "localizedStandardCompare:"
- "name"
- "object"
- "pairedDevices"
- "prefs:root=Bluetooth"
- "q24@?0@\"CCUIMenuModuleItem\"8@\"CCUIMenuModuleItem\"16"
- "retrieveConnectedPeripheralsWithServices:allowAll:"
- "retrieveConnectingPeripherals"
- "retrievePairedPeers"
- "sharedPairingAgent"
- "sortUsingComparator:"
- "v24@0:8@\"CBCentralManager\"16"
- "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
- "v32@0:8@\"CBCentralManager\"16@\"NSArray\"24"
- "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
- "v32@0:8@\"CBCentralManager\"16@\"NSError\"24"
- "v36@0:8@\"CBCentralManager\"16@\"NSString\"24B32"
- "v36@0:8@16@24B32"
- "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32"
- "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
- "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSNumber\"32"
- "v40@0:8@\"CBCentralManager\"16@\"NSData\"24@\"CBPeripheral\"32"
- "v40@0:8@\"CBCentralManager\"16@\"NSData\"24@\"NSData\"32"
- "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"
- "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSError\"40"
- "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
- "v48@0:8@\"CBCentralManager\"16@\"NSNumber\"24@\"CBPeripheral\"32@\"NSError\"40"
- "v48@0:8@16@24@32@40"
- "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
- "v52@0:8@16@24d32B40@44"
- "v56@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48"
- "v56@0:8@16@24@32@40@48"
- "v72@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64"
- "v72@0:8@16@24@32@40@48@56@64"
- "visibleInSettings"

```
