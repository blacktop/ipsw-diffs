## BLEPairing-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/BLEPairing-iOS.feature/BLEPairing-iOS`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x5c08
-  __TEXT.__auth_stubs: 0x440
+1176.0.26.502.1
+  __TEXT.__text: 0x53e4
   __TEXT.__objc_methlist: 0x4fc
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x241
+  __TEXT.__cstring: 0x249
   __TEXT.__oslogstring: 0xfa1
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methname: 0xe25
-  __TEXT.__objc_methtype: 0x5cd
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x140
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x228
-  __AUTH_CONST.__const: 0x20
+  __DATA_CONST.__got: 0x140
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x6c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x240
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7DF2B4D-F8F9-3EDA-AE49-028AA0A90E83
-  Functions: 97
-  Symbols:   564
-  CStrings:  305
+  UUID: 0D8E4BDA-92FC-3F1D-8C92-FB5E9F86523F
+  Functions: 103
+  Symbols:   577
+  CStrings:  82
 
Symbols:
+ ___block_literal_global.160
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACCBLEPairingShimProtocol>\""
- "@\"ACCBLEPairingAccessory\"20@0:8I16"
- "@\"ACCBLEPairingProvider\""
- "@\"ACCBLEPairingShim\""
- "@\"ACCiAP2ShimAccessory\""
- "@\"ACCiAP2ShimServer\""
- "@\"NSData\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACCBLEPairingAccessory"
- "ACCBLEPairingFeaturePlugin"
- "ACCBLEPairingProviderProtocol"
- "ACCBLEPairingShim"
- "ACCBLEPairingShimProtocol"
- "ACCFeaturePluginProtocol"
- "ACCPluginProtocol"
- "ACCiAP2ShimServerDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSObject<OS_xpc_object>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8C16@20"
- "B40@0:8@\"NSObject<OS_xpc_object>\"16@\"NSObject<OS_xpc_object>\"24@\"ACCiAP2ShimServer\"32"
- "B40@0:8@16@24@32"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ACCBLEPairingShimProtocol>\",W,N,V_delegate"
- "T@\"ACCBLEPairingProvider\",&,N,V_blePairingProvider"
- "T@\"ACCBLEPairingShim\",&,N,V_blePairingShim"
- "T@\"ACCiAP2ShimAccessory\",&,N,V_iap2ShimAccessory"
- "T@\"ACCiAP2ShimServer\",&,N,V_iap2server"
- "T@\"NSData\",&,N,V_blePairingUUID"
- "T@\"NSData\",&,N,V_supportedPairTypes"
- "T@\"NSMutableDictionary\",&,N,V_blePairingAccessoryList"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_blePairingQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,V_uid"
- "TB,N,V_isRunning"
- "TB,R,N"
- "TQ,R"
- "Ti,N,V_selectedPairType"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_blePairingAccessoryList"
- "_blePairingProvider"
- "_blePairingQueue"
- "_blePairingShim"
- "_blePairingUUID"
- "_delegate"
- "_iap2ShimAccessory"
- "_iap2server"
- "_isRunning"
- "_isSupportedType:supportedListData:"
- "_selectedPairType"
- "_supportedPairTypes"
- "_uid"
- "accessoryAttached:blePairingUUID:accInfoDict:supportedPairTypes:"
- "accessoryDetached:blePairingUUID:"
- "accessoryInfoDict"
- "accessoryUID"
- "addAccessory:"
- "addDelegate:"
- "addEntriesFromDictionary:"
- "addFeature:"
- "autorelease"
- "bleAccessoryForConnectionID:"
- "blePairing:accessoryAttached:blePairingUUID:accInfoDict:supportedPairTypes:"
- "blePairing:accessoryDetached:blePairingUUID:"
- "blePairing:accessoryDetect:"
- "blePairing:pairingFinished:blePairingUUID:"
- "blePairingAccessoryList"
- "blePairingDataUpdate:pairType:pairData:accessory:blePairingUUID:"
- "blePairingInfoUpdate:pairType:pairInfoList:accessory:blePairingUUID:"
- "blePairingNoAccessories:"
- "blePairingProvider"
- "blePairingQueue"
- "blePairingShim"
- "blePairingStateUpdate:validMask:btRadioOn:pairingState:pairingModeOn:accessory:blePairingUUID:"
- "blePairingUUID"
- "bytes"
- "class"
- "conformsToProtocol:"
- "connectionID"
- "connectionIDObj"
- "dataUpdate:blePairingUUID:pairType:pairData:"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "detachXPCConnection:"
- "devicePairingData:blePairingUUID:pairType:pairData:"
- "deviceSend:pairType:pairingData:"
- "deviceStartBLEUpdates:pairType:btRadio:pairInfo:"
- "deviceStateUpdate:blePairingUUID:bRadioOn:pairState:bPairModeOn:"
- "deviceStateUpdate:btRadio:pairStatus:pairModeOn:forceUpdates:"
- "deviceStopBLEUpdates:"
- "deviceUpdate:pairType:pairInfo:"
- "deviceUpdatePairingInfo:blePairingUUID:pairType:pairInfo:"
- "dictionaryWithObjects:forKeys:count:"
- "findAccessoryForAccessoryUID:andKeyTag:"
- "getUID"
- "hash"
- "i"
- "i16@0:8"
- "iap2ShimAccessory"
- "iap2server"
- "init"
- "initPlugin"
- "initWithDelegate:"
- "initWithUID:keyTag:features:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "length"
- "manufacturer"
- "markClientAsInterestedInBleNotifications:"
- "model"
- "mutableCopy"
- "notifyInterestedClientsOfACCBLEAccessoryEvent:withPayload:"
- "null"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginName"
- "postNotifydNotificationType:"
- "release"
- "removeAccessory:"
- "removeDelegate:"
- "removeObjectForKey:"
- "resetServerState"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "selectedPairType"
- "self"
- "setBlePairingAccessoryList:"
- "setBlePairingProvider:"
- "setBlePairingQueue:"
- "setBlePairingShim:"
- "setBlePairingUUID:"
- "setDelegate:"
- "setFirmwareVersion:"
- "setHardwareVersion:"
- "setIap2ShimAccessory:"
- "setIap2server:"
- "setIsRunning:"
- "setManufacturer:"
- "setModel:"
- "setName:"
- "setObject:forKey:"
- "setSelectedPairType:"
- "setSerialNumber:"
- "setSupportedPairTypes:"
- "sharedInstance"
- "startBLEUpdates:blePairingUUID:pairType:bRadioUpdatesOn:bPairInfoUpdatesOn:"
- "startPlugin"
- "startServer"
- "stateUpdate:blePairingUUID:pairType:pairInfoList:"
- "stateUpdate:blePairingUUID:validMask:btRadioOn:pairingState:pairingModeOn:"
- "stopBLEUpdates:blePairingUUID:"
- "stopPlugin"
- "stopServer"
- "stringWithFormat:"
- "superclass"
- "supportedPairTypes"
- "tryProcessXPCMessage:connection:server:"
- "uid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"ACCBLEPairingAccessory\"16"
- "v24@0:8@\"ACCBLEPairingProvider\"16"
- "v24@0:8@16"
- "v28@0:8@\"ACCBLEPairingProvider\"16i24"
- "v28@0:8@16i24"
- "v32@0:8@16@24"
- "v36@0:8@\"ACCBLEPairingAccessory\"16i24@\"NSData\"28"
- "v36@0:8@\"ACCBLEPairingAccessory\"16i24B28B32"
- "v36@0:8@16i24@28"
- "v36@0:8@16i24B28B32"
- "v40@0:8@\"ACCBLEPairingAccessory\"16C24i28B32B36"
- "v40@0:8@\"ACCBLEPairingProvider\"16@\"NSString\"24@\"NSData\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16C24i28B32B36"
- "v44@0:8@16@24i32@36"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24I32B36i40B44"
- "v52@0:8@\"ACCBLEPairingProvider\"16i24@\"NSArray\"28@\"NSString\"36@\"NSData\"44"
- "v52@0:8@\"ACCBLEPairingProvider\"16i24@\"NSData\"28@\"NSString\"36@\"NSData\"44"
- "v52@0:8@16i24@28@36@44"
- "v56@0:8@\"ACCBLEPairingProvider\"16@\"NSString\"24@\"NSData\"32@\"NSDictionary\"40@\"NSData\"48"
- "v56@0:8@\"ACCBLEPairingProvider\"16I24B28i32B36@\"NSString\"40@\"NSData\"48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16I24B28i32B36@40@48"
- "zone"

```
