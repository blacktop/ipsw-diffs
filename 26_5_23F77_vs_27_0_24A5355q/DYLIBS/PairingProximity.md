## PairingProximity

> `/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity`

```diff

-1310.13.0.0.0
-  __TEXT.__text: 0x25e4
-  __TEXT.__auth_stubs: 0x2b0
+1350.1.0.0.0
+  __TEXT.__text: 0x21f8
   __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1fe
+  __TEXT.__cstring: 0x203
   __TEXT.__oslogstring: 0x31b
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x180
-  __TEXT.__objc_classname: 0x7d
-  __TEXT.__objc_methname: 0xb94
-  __TEXT.__objc_methtype: 0x406
-  __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x340
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x568
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA3943E4-B06E-3D67-83FE-E016E01A582A
+  UUID: 27260BFA-9604-3FDB-A797-13833D6902C8
   Functions: 92
-  Symbols:   419
-  CStrings:  240
+  Symbols:   424
+  CStrings:  55
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PPDiscoveryManagerDelegate>\""
- "@\"CBCentralManager\""
- "@\"NRDevicePairingManager\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"PPDiscoveryManager\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8d16q24@?32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "CBCentralManagerDelegate"
- "NSObject"
- "PPDiscoveryManager"
- "PPDiscoveryManagerDelegate"
- "PPNearbyWatchNotifier"
- "PPNotifierService"
- "Q16@0:8"
- "T#,R"
- "T@\"<PPDiscoveryManagerDelegate>\",N,V_discoveryDelegate"
- "T@\"CBCentralManager\",&,N,V_central"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_discoveryQueue"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_timerSource"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_notificationService"
- "T@\"PPDiscoveryManager\",&,N,V_discoveryManager"
- "T@?,C,N,V_discoveryCompletion"
- "TB,N,V_bluetoothIsScanning"
- "TQ,R"
- "Tq,N,V_signalLimitOverride"
- "UUIDWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_beginDiscovery"
- "_bluetoothIsScanning"
- "_central"
- "_cleanupDiscoveryDidFindDevice:error:"
- "_discoveryCompletion"
- "_discoveryDelegate"
- "_discoveryManager"
- "_discoveryQueue"
- "_forceEndDiscovery"
- "_networkRelayPairingEnabled"
- "_notificationService"
- "_scanningManager"
- "_signalLimitOverride"
- "_timerSource"
- "activateWithCompletion:"
- "applicationState"
- "arrayWithObjects:count:"
- "autorelease"
- "begin"
- "bluetoothIsScanning"
- "cancelDiscovery"
- "central"
- "centralManager:connectionEventDidOccur:forPeripheral:"
- "centralManager:didConnectPeripheral:"
- "centralManager:didDisconnectPeripheral:error:"
- "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
- "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
- "centralManager:didFailToConnectPeripheral:error:"
- "centralManager:didUpdateANCSAuthorizationForPeripheral:"
- "centralManager:willRestoreState:"
- "centralManagerDidUpdateState:"
- "class"
- "conformsToProtocol:"
- "copy"
- "debugDescription"
- "defaultCenter"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didDiscoverDeviceWithAdvertisingID:signalStrength:"
- "didStopDiscovering"
- "discoverForNearbyWatchesWithCompletion:"
- "discoverForTimeInterval:signalLimit:completion:"
- "discoveryCompletion"
- "discoveryDelegate"
- "discoveryManager"
- "discoveryQueue"
- "end"
- "foundAcceptableDeviceWithAdvertisingID:signalStrength:"
- "hash"
- "humanReadableName"
- "identifier"
- "init"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithDelegate:queue:options:"
- "initWithIdentifier:pairingCriteria:metadata:queue:"
- "initWithPackedIdentifierData:"
- "initWithServiceName:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isBluetoothConnected:"
- "isBluetoothPoweredOn:"
- "isEqual:"
- "isInstalled"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPlaceholder"
- "isProxy"
- "isWatchAppRemoved"
- "length"
- "notificationService"
- "notifyOfNearbyDevice:withReply:"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationName:object:userInfo:"
- "prepareServiceConnectionIfNeeded"
- "q16@0:8"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "scanForPeripheralsWithServices:options:"
- "self"
- "setBluetoothIsScanning:"
- "setCandidateDiscoveredHandler:"
- "setCentral:"
- "setDeviceType:"
- "setDiscoveryCompletion:"
- "setDiscoveryDelegate:"
- "setDiscoveryManager:"
- "setDiscoveryQueue:"
- "setNotificationService:"
- "setPairingTransport:"
- "setRemoteObjectInterface:"
- "setRssi:"
- "setSignalLimitOverride:"
- "setTimerSource:"
- "sharedDiscoveryManager"
- "sharedNotifier"
- "shouldScanForNearbyDevices"
- "signalLimitOverride"
- "startDiscoveryWithCompletion:"
- "state"
- "stopScan"
- "superclass"
- "timerSource"
- "updateFromBTState:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"CBCentralManager\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v28@0:8B16@20"
- "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
- "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
- "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"
- "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
- "v48@0:8@16@24@32@40"
- "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
- "v52@0:8@16@24d32B40@44"
- "zone"

```
