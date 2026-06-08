## AccessoryNavigation

> `/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0xc154
-  __TEXT.__auth_stubs: 0x410
+1176.0.26.502.1
+  __TEXT.__text: 0xb30c
   __TEXT.__objc_methlist: 0xb74
   __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0x1a1c
-  __TEXT.__cstring: 0x149b
-  __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__unwind_info: 0x2e8
-  __TEXT.__objc_classname: 0x1fd
-  __TEXT.__objc_methname: 0x1544
-  __TEXT.__objc_methtype: 0x30c
-  __TEXT.__objc_stubs: 0xde0
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x180
+  __TEXT.__cstring: 0x14a5
+  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__const: 0x20
+  __DATA_CONST.__got: 0xd0
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0x1070
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x4f8
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0xf8
-  __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x20
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AC234BF7-F5A8-308F-B163-41EC5D675E15
-  Functions: 245
-  Symbols:   1103
-  CStrings:  608
+  UUID: 18012A37-045B-3052-8007-9D3449071114
+  Functions: 257
+  Symbols:   1154
+  CStrings:  322
 
Symbols:
+ -[ACCNavigationAccessory objectDetectionComponentIdListIsEnabled:].cold.2
+ -[ACCNavigationAccessory objectDetectionComponentIdListIsEnabled:].cold.3
+ -[ACCNavigationProvider accessoryNavigationAttached:componentList:].cold.7
+ -[ACCNavigationProvider accessoryNavigationAttached:componentList:].cold.8
+ -[ACCNavigationProvider accessoryNavigationDetached:].cold.10
+ -[ACCNavigationProvider accessoryNavigationDetached:].cold.9
+ -[ACCNavigationProvider accessoryNavigationObjectDetection:componentIdList:updateInfo:].cold.6
+ -[ACCNavigationProvider accessoryNavigationStartRouteGuidance:componentIdList:options:].cold.6
+ -[ACCNavigationProvider accessoryNavigationStartRouteGuidance:componentIdList:options:].cold.7
+ -[ACCNavigationProvider accessoryNavigationStopRouteGuidance:componentIdList:].cold.6
+ -[ACCNavigationProvider objectDetection:startComponentIdList:objectTypes:].cold.3
+ __MergedGlobals.4
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_tmp.3
+ ___block_literal_global.130
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_8
- __MergedGlobals.2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACCNavigationXPCServerProtocol>\""
- "@\"ACCNavigationProvider\""
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8S16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ACCNavigationAccessory"
- "ACCNavigationAccessoryComponent"
- "ACCNavigationAccessoryObjectDetectionComponent"
- "ACCNavigationLaneGuidanceInfo"
- "ACCNavigationLaneGuidanceLaneInfo"
- "ACCNavigationManeuverUpdateInfo"
- "ACCNavigationProvider"
- "ACCNavigationRoadObjectDetectionInfo"
- "ACCNavigationRoadObjectRoadLaneInfo"
- "ACCNavigationRoadObjectRoadObjectInfo"
- "ACCNavigationRoadObjectRoadSignInfo"
- "ACCNavigationRouteGuidanceUpdateInfo"
- "ACCNavigationXPCClientProtocol"
- "ACCNavigationXPCServerProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8S16@20"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<ACCNavigationXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"ACCNavigationProvider\",R,W,N,V_provider"
- "T@\"NSArray\",&,V_supportedTypes"
- "T@\"NSDictionary\",R"
- "T@\"NSMutableArray\",&,N,V_delegates"
- "T@\"NSMutableDictionary\",&,N,V_accessories"
- "T@\"NSMutableDictionary\",&,V_componentListInternal"
- "T@\"NSMutableDictionary\",&,V_infoDict"
- "T@\"NSMutableDictionary\",&,V_objectDetectionComponentListInternal"
- "T@\"NSString\",&,N,V_accessoryUID"
- "T@\"NSString\",&,N,V_providerUID"
- "T@\"NSString\",&,V_name"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "TB,N,V_isEnabled"
- "TB,N,V_requestSourceName"
- "TB,N,V_requestSourceSupportsRouteGuidance"
- "TB,N,V_supportsExitInfo"
- "TB,N,V_supportsLaneGuidance"
- "TB,N,V_supportsPreconditioning"
- "TB,N,V_supportsTimeZoneOffset"
- "TB,R"
- "TB,V_isEnabled"
- "TQ,N,V_identifier"
- "TQ,N,V_maxCapacity_GuidanceManeuver"
- "TQ,N,V_maxCapacity_LaneGuidance"
- "TQ,N,V_maxLength_CurrentRoadName"
- "TQ,N,V_maxLength_DestinationRoadName"
- "TQ,N,V_maxLength_LaneGuidanceDescription"
- "TQ,N,V_maxLength_ManeuverDescription"
- "TQ,N,V_maxLength_PostManeuverRoadName"
- "TQ,R"
- "TQ,V_identifier"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessories"
- "_accessoryUID"
- "_checkDataClassForType:data:"
- "_componentListInternal"
- "_delegates"
- "_identifier"
- "_infoDict"
- "_isEnabled"
- "_maxCapacity_GuidanceManeuver"
- "_maxCapacity_LaneGuidance"
- "_maxLength_CurrentRoadName"
- "_maxLength_DestinationRoadName"
- "_maxLength_LaneGuidanceDescription"
- "_maxLength_ManeuverDescription"
- "_maxLength_PostManeuverRoadName"
- "_name"
- "_objectDetectionComponentListInternal"
- "_provider"
- "_providerUID"
- "_remoteObject"
- "_requestSourceName"
- "_requestSourceSupportsRouteGuidance"
- "_serverConnection"
- "_supportedTypes"
- "_supportsExitInfo"
- "_supportsLaneGuidance"
- "_supportsPreconditioning"
- "_supportsTimeZoneOffset"
- "accessories"
- "accessoryForUID:"
- "accessoryNavigationAttached:componentList:"
- "accessoryNavigationDetached:"
- "accessoryNavigationObjectDetection:componentIdList:updateInfo:"
- "accessoryNavigationStartRouteGuidance:componentIdList:options:"
- "accessoryNavigationStopRouteGuidance:componentIdList:"
- "accessoryUID"
- "addObject:"
- "allValues"
- "appendFormat:"
- "autorelease"
- "class"
- "componentIdListIsEnabled:"
- "componentList"
- "componentListForIdList:"
- "componentListInternal"
- "conformsToProtocol:"
- "connectToServer"
- "containsObject:"
- "copy"
- "copyDictionary"
- "copyInfo:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "delegates"
- "delegatesImplementing:"
- "description"
- "detachAllAccessories"
- "dictionaryWithDictionary:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "hash"
- "identifier"
- "infoDict"
- "init"
- "initConnection:"
- "initWithAccessoryUID:provider:"
- "initWithCoder:"
- "initWithDelegate:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "iterateComponentIdList:block:"
- "keyForChargingStationInfoType:"
- "keyForType:"
- "maxCapacity_GuidanceManeuver"
- "maxCapacity_LaneGuidance"
- "maxLength_CurrentRoadName"
- "maxLength_DestinationRoadName"
- "maxLength_LaneGuidanceDescription"
- "maxLength_ManeuverDescription"
- "maxLength_PostManeuverRoadName"
- "name"
- "navigation:accessoryAttached:"
- "navigation:accessoryDetached:"
- "navigation:startRouteGuidance:componentList:"
- "navigation:stopRouteGuidance:componentList:"
- "navigationObjectDetection:accessory:updateObjectDetectionInfo:componentList:"
- "navigationObjectDetection:accessoryAttached:"
- "navigationObjectDetection:accessoryDetached:"
- "notifyOfProvider:"
- "numberWithUnsignedLong:"
- "objectDetection:startComponentIdList:objectTypes:"
- "objectDetection:stopComponentIdList:"
- "objectDetectionComponentIdListIsEnabled:"
- "objectDetectionComponentList"
- "objectDetectionComponentListForIdList:"
- "objectDetectionComponentListInternal"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "provider"
- "providerUID"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObjectForKey:"
- "requestSourceName"
- "requestSourceSupportsRouteGuidance"
- "requestedSourceNameForAnyComponent"
- "requestedSourceSupportsRouteGuidanceForAnyComponent"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "routeGuidance:laneGuidanceInfo:componentIdList:"
- "routeGuidance:maneuverUpdateInfo:componentIdList:"
- "routeGuidance:updateInfo:componentIdList:"
- "self"
- "serverConnection"
- "setAccessories:"
- "setAccessoryUID:"
- "setComponentListInternal:"
- "setDelegates:"
- "setExportedInterface:"
- "setExportedObject:"
- "setIdentifier:"
- "setInfo:data:"
- "setInfoDict:"
- "setInfoFromDictionary:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsEnabled:"
- "setMaxCapacity_GuidanceManeuver:"
- "setMaxCapacity_LaneGuidance:"
- "setMaxLength_CurrentRoadName:"
- "setMaxLength_DestinationRoadName:"
- "setMaxLength_LaneGuidanceDescription:"
- "setMaxLength_ManeuverDescription:"
- "setMaxLength_PostManeuverRoadName:"
- "setName:"
- "setObject:forKey:"
- "setObjectDetectionComponentListInternal:"
- "setProviderUID:"
- "setRemoteObject:"
- "setRemoteObjectInterface:"
- "setRequestSourceName:"
- "setRequestSourceSupportsRouteGuidance:"
- "setServerConnection:"
- "setSupportedTypes:"
- "setSupportsExitInfo:"
- "setSupportsLaneGuidance:"
- "setSupportsPreconditioning:"
- "setSupportsTimeZoneOffset:"
- "setWithArray:"
- "stringWithFormat:"
- "superclass"
- "supportedTypes"
- "supportsExitInfo"
- "supportsExitInfoForAnyComponent"
- "supportsLaneGuidance"
- "supportsLaneGuidanceForAnyComponent"
- "supportsPreconditioning"
- "supportsPreconditioningForAnyComponent"
- "supportsSecureCoding"
- "supportsTimeZoneOffset"
- "supportsTimeZoneOffsetForAnyComponent"
- "unsignedIntegerValue"
- "updateLaneGuidanceInfo:componentList:"
- "updateManeuverInfo:componentList:"
- "updateRouteGuidanceInfo:componentList:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8Q16"
- "v32@0:8@\"NSString\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@\"NSArray\"32"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16@\"NSArray\"24Q32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSArray\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24Q32"
- "zone"

```
