## Navigation-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/Navigation-iOS.feature/Navigation-iOS`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x4714
-  __TEXT.__auth_stubs: 0x430
+1176.0.26.502.1
+  __TEXT.__text: 0x40c8
   __TEXT.__objc_methlist: 0x4b4
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x315
+  __TEXT.__cstring: 0x31d
   __TEXT.__oslogstring: 0xa80
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0xd6
-  __TEXT.__objc_methname: 0xd59
-  __TEXT.__objc_methtype: 0x3e2
-  __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x220
-  __AUTH_CONST.__const: 0x20
+  __DATA_CONST.__got: 0xb0
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x668
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x240
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x10

   - /System/Library/PrivateFrameworks/IAP.framework/IAP
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE9209F2-E806-3645-A5AF-E4EC0CF3FB69
-  Functions: 90
-  Symbols:   496
-  CStrings:  296
+  UUID: 6C896BB9-BF18-30AF-8FFA-97EF7585633A
+  Functions: 97
+  Symbols:   511
+  CStrings:  88
 
Symbols:
+ ___block_literal_global.144
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x8
- _OUTLINED_FUNCTION_4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACCNavigationShimProtocol>\""
- "@\"ACCNavigationAccessory\""
- "@\"ACCNavigationProvider\""
- "@\"ACCNavigationShim\""
- "@\"ACCNavigationShimAccessory\"20@0:8I16"
- "@\"ACCiAP2ShimAccessory\""
- "@\"ACCiAP2ShimServer\""
- "@\"NSArray\"16@0:8"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ACCFeaturePluginProtocol"
- "ACCNavigationFeaturePlugin"
- "ACCNavigationProviderProtocol"
- "ACCNavigationShim"
- "ACCNavigationShimAccessory"
- "ACCNavigationShimProtocol"
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
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ACCNavigationShimProtocol>\",W,N,V_delegate"
- "T@\"ACCNavigationAccessory\",&,N,V_navigationAccessory"
- "T@\"ACCNavigationProvider\",&,N,V_navigationProvider"
- "T@\"ACCNavigationShim\",&,N,V_navigationShim"
- "T@\"ACCiAP2ShimAccessory\",&,N,V_iap2ShimAccessory"
- "T@\"ACCiAP2ShimServer\",&,N,V_iap2server"
- "T@\"NSMutableDictionary\",&,N,V_navigationShimAccessoryList"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_navigationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_processingQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,V_uid"
- "TB,N,V_isRunning"
- "TB,R,N"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_delegate"
- "_iap2ShimAccessory"
- "_iap2server"
- "_isRunning"
- "_navigationAccessory"
- "_navigationProvider"
- "_navigationQueue"
- "_navigationShim"
- "_navigationShimAccessoryForConnectionIDNoLock:"
- "_navigationShimAccessoryList"
- "_processingQueue"
- "_uid"
- "accessoryAttached:"
- "accessoryDetached:"
- "accessoryNavigation:updateManeuverInfo:"
- "accessoryNavigation:updateRouteGuidanceInfo:"
- "accessoryStartRouteGuidance:componentList:"
- "accessoryStopRouteGuidance:componentList:"
- "accessoryUID"
- "addAccessory:"
- "addDelegate:"
- "addFeature:"
- "addObject:"
- "allKeys"
- "allValues"
- "arrayWithObjects:count:"
- "autorelease"
- "cStringUsingEncoding:"
- "class"
- "componentList"
- "componentListForIdList:"
- "conformsToProtocol:"
- "connectionID"
- "connectionIDObj"
- "convertIAP2ACCManeuverInfo:forAccessory:"
- "convertIAP2ACCRouteGuidanceInfo:forAccessory:"
- "countByEnumeratingWithState:objects:count:"
- "create_xpc_representation"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "detachXPCConnection:"
- "findAccessoryForAccessoryUID:andKeyTag:"
- "getUID"
- "hash"
- "iap2ShimAccessory"
- "iap2server"
- "init"
- "initPlugin"
- "initWithArray:"
- "initWithDelegate:"
- "initWithUID:keyTag:features:"
- "integerValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "navigation:accessoryAttached:"
- "navigation:accessoryDetached:"
- "navigation:startRouteGuidance:componentList:"
- "navigation:stopRouteGuidance:componentList:"
- "navigationAccessory"
- "navigationProvider"
- "navigationQueue"
- "navigationShim"
- "navigationShimAccessoryForConnectionID:"
- "navigationShimAccessoryList"
- "notifyNavigationAccessoryClientsOfStateChange"
- "numberWithInt:"
- "numberWithUnsignedLong:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginName"
- "postNSDistributeNotificationType:notifyDict:"
- "processingQueue"
- "release"
- "removeAccessory:"
- "removeDelegate:"
- "removeObjectForKey:"
- "resetServerState"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setContext:"
- "setDelegate:"
- "setDontPublish:"
- "setFirmwareVersion:"
- "setHardwareVersion:"
- "setIap2ShimAccessory:"
- "setIap2server:"
- "setInfo:data:"
- "setIsRunning:"
- "setManufacturer:"
- "setModel:"
- "setName:"
- "setNavigationAccessory:"
- "setNavigationProvider:"
- "setNavigationQueue:"
- "setNavigationShim:"
- "setNavigationShimAccessoryList:"
- "setObject:forKey:"
- "setProcessingQueue:"
- "setSerialNumber:"
- "sharedInstance"
- "startPlugin"
- "startServer"
- "stopPlugin"
- "stopServer"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "tryProcessXPCMessage:connection:server:"
- "uid"
- "unarchivedObjectOfClasses:fromData:error:"
- "updateManeuverInfo:componentIdList:accessory:"
- "updateManeuverInfo:componentList:"
- "updateRouteGuidanceInfo:componentIdList:accessory:"
- "updateRouteGuidanceInfo:componentList:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v32@0:8@\"ACCNavigationProvider\"16@\"ACCNavigationAccessory\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"ACCNavigationManeuverUpdateInfo\"16@\"NSArray\"24@\"ACCNavigationShimAccessory\"32"
- "v40@0:8@\"ACCNavigationProvider\"16@\"ACCNavigationAccessory\"24@\"NSArray\"32"
- "v40@0:8@\"ACCNavigationRouteGuidanceUpdateInfo\"16@\"NSArray\"24@\"ACCNavigationShimAccessory\"32"
- "v40@0:8@16@24@32"
- "zone"

```
