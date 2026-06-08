## OOBBTPairing-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/OOBBTPairing-iOS.feature/OOBBTPairing-iOS`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x5834
-  __TEXT.__auth_stubs: 0x4b0
+1176.0.26.502.1
+  __TEXT.__text: 0x5044
   __TEXT.__objc_methlist: 0x59c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x231
+  __TEXT.__cstring: 0x23b
   __TEXT.__oslogstring: 0xebc
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__objc_classname: 0xde
-  __TEXT.__objc_methname: 0xf70
-  __TEXT.__objc_methtype: 0x591
-  __TEXT.__objc_stubs: 0x9a0
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0x20
+  __DATA_CONST.__got: 0xf8
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x8a8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x258
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x10

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F60B7D5A-399E-3365-9069-6E01B36ED874
-  Functions: 121
-  Symbols:   622
-  CStrings:  342
+  UUID: 8BF6FAC0-B486-3F9A-B578-80A2D89B1534
+  Functions: 128
+  Symbols:   638
+  CStrings:  91
 
Symbols:
+ ___block_literal_global.141
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _OUTLINED_FUNCTION_5
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACCOOBBTPairingShimProtocol>\""
- "@\"ACCOOBBTPairingAccessory\"20@0:8I16"
- "@\"ACCOOBBTPairingProvider\""
- "@\"ACCOOBBTPairingShim\""
- "@\"ACCiAP2ShimAccessory\""
- "@\"ACCiAP2ShimServer\""
- "@\"NSData\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACCFeaturePluginProtocol"
- "ACCOOBBTPairingAccessory"
- "ACCOOBBTPairingFeaturePlugin"
- "ACCOOBBTPairingProviderProtocol"
- "ACCOOBBTPairingShim"
- "ACCOOBBTPairingShimProtocol"
- "ACCPluginProtocol"
- "ACCiAP2ShimServerDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSObject<OS_xpc_object>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B40@0:8@\"NSObject<OS_xpc_object>\"16@\"NSObject<OS_xpc_object>\"24@\"ACCiAP2ShimServer\"32"
- "B40@0:8@16@24@32"
- "BTAccessoryManager"
- "BTSession"
- "BTSessionQueue"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ACCOOBBTPairingShimProtocol>\",W,N,V_delegate"
- "T@\"ACCOOBBTPairingProvider\",&,N,V_oobBtPairingProvider"
- "T@\"ACCOOBBTPairingShim\",&,N,V_oobBtPairingShim"
- "T@\"ACCiAP2ShimAccessory\",&,N,V_iap2ShimAccessory"
- "T@\"ACCiAP2ShimServer\",&,N,V_iap2server"
- "T@\"NSData\",&,N,V_currentRemoteMACAddress"
- "T@\"NSData\",&,V_certData"
- "T@\"NSData\",&,V_certSerial"
- "T@\"NSMutableDictionary\",&,N,V_oobBtPairingAccessoryList"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_oobBtPairingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_BTSessionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_processingQueue"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,V_setup_complete_semaphore"
- "T@\"NSString\",&,N,V_currentOOBBTPairingUID"
- "T@\"NSString\",&,V_displayName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,V_uid"
- "TB,N,V_isRunning"
- "TB,R,N"
- "TB,V_carPlaySupported"
- "TB,V_isBTReady"
- "TB,V_oobPairing2Supported"
- "TQ,R"
- "T^{BTAccessoryManagerImpl=},V_BTAccessoryManager"
- "T^{BTDeviceImpl=},V_currentRemoteBTDevice"
- "T^{BTSessionImpl=},V_BTSession"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{BTAccessoryManagerImpl=}"
- "^{BTAccessoryManagerImpl=}16@0:8"
- "^{BTDeviceImpl=}"
- "^{BTDeviceImpl=}16@0:8"
- "^{BTSessionImpl=}"
- "^{BTSessionImpl=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_BTAccessoryManager"
- "_BTSession"
- "_BTSessionQueue"
- "_carPlaySupported"
- "_certData"
- "_certSerial"
- "_currentOOBBTPairingUID"
- "_currentRemoteBTDevice"
- "_currentRemoteMACAddress"
- "_delegate"
- "_displayName"
- "_iap2ShimAccessory"
- "_iap2server"
- "_isBTReady"
- "_isRunning"
- "_oobBtPairingAccessoryList"
- "_oobBtPairingProvider"
- "_oobBtPairingQueue"
- "_oobBtPairingShim"
- "_oobPairing2Supported"
- "_processingQueue"
- "_setup_complete_semaphore"
- "_uid"
- "accessoryAttached:accInfoDict:"
- "accessoryDetached:"
- "accessoryInfo:oobBtPairingUID:accessoryMacAddr:deviceClass:"
- "accessoryInfoDictionaryForLogging:"
- "accessoryPairingCompletion:oobBtPairingUID:accessoryMacAddr:sendStop:result:"
- "accessoryUID"
- "addAccessory:"
- "addDelegate:"
- "addFeature:"
- "autorelease"
- "beginPairingWithCurrentAccessory:"
- "boolValue"
- "bytes"
- "carPlaySupported"
- "certData"
- "certSerial"
- "charValue"
- "class"
- "conformsToProtocol:"
- "connectionID"
- "connectionIDObj"
- "context"
- "currentOOBBTPairingUID"
- "currentRemoteBTDevice"
- "currentRemoteMACAddress"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "detachXPCConnection:"
- "displayName"
- "findAccessoryForAccessoryUID:andKeyTag:"
- "getUID"
- "hash"
- "iap2ShimAccessory"
- "iap2server"
- "init"
- "initPlugin"
- "initWithDelegate:"
- "initWithUID:keyTag:features:"
- "isBTReady"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "length"
- "linkKey:deviceMacAddr:accessory:"
- "linkKeyInfo:oobBtPairingUID:linkKey:deviceMacAddr:"
- "name"
- "numberWithUnsignedLong:"
- "objectForKey:"
- "oobBtAccessoryForConnectionID:"
- "oobBtPairing:accessoryAttached:accInfoDict:"
- "oobBtPairing:accessoryDetached:"
- "oobBtPairing:accessoryInfo:oobBtPairingUID:accessoryMacAddr:deviceClass:"
- "oobBtPairing:completion:oobBtPairingUID:accessoryMacAddr:result:"
- "oobBtPairing:legacyConnectionIDForAccessoryUID:connectionID:"
- "oobBtPairingAccessoryList"
- "oobBtPairingProvider"
- "oobBtPairingQueue"
- "oobBtPairingShim"
- "oobPairing2Supported"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginName"
- "processingQueue"
- "release"
- "removeAccessory:"
- "removeDelegate:"
- "removeObjectForKey:"
- "requestLegacyConnectionIDForAccessoryUID:"
- "resetServerState"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setBTAccessoryManager:"
- "setBTSession:"
- "setBTSessionQueue:"
- "setCarPlaySupported:"
- "setCertData:"
- "setCertSerial:"
- "setConnectionID:"
- "setContext:"
- "setCurrentOOBBTPairingUID:"
- "setCurrentRemoteBTDevice:"
- "setCurrentRemoteMACAddress:"
- "setDelegate:"
- "setDisplayName:"
- "setDontPublish:"
- "setFirmwareVersion:"
- "setHardwareVersion:"
- "setIap2ShimAccessory:"
- "setIap2server:"
- "setIsBTReady:"
- "setIsRunning:"
- "setManufacturer:"
- "setModel:"
- "setName:"
- "setObject:forKey:"
- "setOobBtPairingAccessoryList:"
- "setOobBtPairingProvider:"
- "setOobBtPairingQueue:"
- "setOobBtPairingShim:"
- "setOobPairing2Supported:"
- "setProcessingQueue:"
- "setSerialNumber:"
- "setSetup_complete_semaphore:"
- "setup_complete_semaphore"
- "sharedInstance"
- "startOOBBTPairing:"
- "startPlugin"
- "startServer"
- "stopOOBBTPairing:"
- "stopPlugin"
- "stopServer"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "superclass"
- "tryProcessXPCMessage:connection:server:"
- "uid"
- "unsignedLongValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"ACCOOBBTPairingAccessory\"16"
- "v24@0:8@16"
- "v24@0:8^{BTAccessoryManagerImpl=}16"
- "v24@0:8^{BTDeviceImpl=}16"
- "v24@0:8^{BTSessionImpl=}16"
- "v32@0:8@\"ACCOOBBTPairingProvider\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v36@0:8@\"ACCOOBBTPairingProvider\"16@\"NSString\"24I32"
- "v36@0:8@16@24I32"
- "v40@0:8@\"ACCOOBBTPairingProvider\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSData\"16@\"NSData\"24@\"ACCOOBBTPairingAccessory\"32"
- "v40@0:8@16@24@32"
- "v44@0:8@16@24@32I40"
- "v48@0:8@16@24@32B40C44"
- "v52@0:8@\"ACCOOBBTPairingProvider\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40C48"
- "v52@0:8@\"ACCOOBBTPairingProvider\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40I48"
- "v52@0:8@16@24@32@40C48"
- "v52@0:8@16@24@32@40I48"
- "zone"

```
