## SymptomPresentationLite

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationLite.framework/SymptomPresentationLite`

```diff

-2169.120.7.0.0
+2357.0.0.0.2
   __TEXT.__text: 0x550
-  __TEXT.__auth_stubs: 0x60
-  __TEXT.__objc_methlist: 0x1f0
-  __TEXT.__cstring: 0xbec
+  __TEXT.__objc_methlist: 0x1fc
+  __TEXT.__cstring: 0xc1f
   __TEXT.__const: 0x8
   __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0x2b
-  __TEXT.__objc_methname: 0x74d
-  __TEXT.__objc_methtype: 0x705
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x6a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x38
-  __AUTH_CONST.__cfstring: 0x1820
-  __AUTH_CONST.__objc_const: 0x1e0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x1880
+  __AUTH_CONST.__objc_const: 0x1e8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x60

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 61214C76-AD32-3D7A-B8A8-AE5389414256
+  UUID: F05DD2B9-2C77-3F30-A258-9A98B200A221
   Functions: 9
-  Symbols:   269
-  CStrings:  493
+  Symbols:   272
+  CStrings:  395
 
Symbols:
+ _kPerformanceNetAttachFallbacks
+ _kPerformanceNetAttachMigrations
+ _kPerformanceNetAttachPartialConnectivityDetections
CStrings:
+ "fallbacks"
+ "migrations"
+ "partialConnectivityDetections"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@16"
- "B36@0:8i16@20@?28"
- "NetworkPerformanceQuery"
- "SFServiceInterface"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "_connection"
- "_formatInstantRouteMetrics:"
- "cleanupNDFDeviceRecordsWithReply:"
- "connection"
- "createSnapshotFor:pred:actions:reply:"
- "currentScorecardFor:queue:reply:"
- "dealloc"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjectsAndKeys:"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:"
- "errorWithDomain:code:userInfo:"
- "fetchNDFDeviceRecordsWithReply:"
- "getOption:inScopes:reply:"
- "getPreferCellOverWiFiWithOptions:reply:"
- "identifierForUUID:reply:"
- "init"
- "initWithCapacity:"
- "initWithMachServiceName:options:"
- "inquireNOIFor:orPredicate:requestedKeys:options:reply:"
- "interfaceWithProtocol:"
- "invalidate"
- "listNDFDeviceObjectsWithIdentifier:reply:"
- "ndfClientCheckInWithReply:"
- "ndfClientSubscriptionIsActive:reply:"
- "networkRestrictsMulticastTrafficWithReply:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "performActionWithOptions:inScopes:reply:"
- "performAppEndpointTrackingPeriodicTasksWithReply:"
- "performAppExperiencePeriodicTasksWithReply:"
- "performAppPeriodicTasksWithReply:"
- "performAppTrackingPeriodicTasksWithReply:"
- "performPersistentStoreHealthCheckWithReply:"
- "performQueryOnEntity:fetchRequestProperties:pred:sort:actions:reply:"
- "performQueryOnEntity:pred:sort:actions:reply:"
- "pingEndpoints:reply:"
- "predicateWithFormat:"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectForKey:"
- "resetDataFor:nameKind:inScopes:reply:"
- "resetUsageFor:nameKind:reply:"
- "resume"
- "retrieveActivityMetrics:reply:"
- "sendMessage:toEndpoints:reply:"
- "sendPayloadToDaemonWithReply:"
- "setConnection:"
- "setObject:forKeyedSubscript:"
- "setOption:inScopes:reply:"
- "setPreferCellOverWiFiWithOptions:reply:"
- "setRemoteObjectInterface:"
- "setUsageOption:reply:"
- "subscribeToNOIsFor:orPredicate:options:"
- "trainModelAndScore:lastScoreDate:reply:"
- "triggerSendPayloadToDaemonWithInterval:leeway:reply:"
- "unsubscribeToNOIs:"
- "updatedNDFDeviceRecords:reply:"
- "v16@0:8"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSObject<OS_xpc_object>\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v36@0:8B16@\"NSDate\"20@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "v36@0:8B16@20@?28"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSObject<OS_xpc_object>\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NWNetworkOfInterest\"16@\"NSPredicate\"24@\"NSDictionary\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8q16q24@?32"
- "v40@0:8q16q24@?<v@?B>32"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?B>40"
- "v48@0:8@\"NSString\"16@\"NSPredicate\"24@\"NSDictionary\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"NSString\"16@\"NSPredicate\"24@\"NSSortDescriptor\"32@\"NSDictionary\"40@?<v@?@\"NSArray\">48"
- "v56@0:8@\"NWNetworkOfInterest\"16@\"NSPredicate\"24@\"NSDictionary\"32@\"NSDictionary\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@\"NSString\"16@\"FetchRequestPropertiesDescriptor\"24@\"NSPredicate\"32@\"NSSortDescriptor\"40@\"NSDictionary\"48@?<v@?@\"NSArray\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40d48d56@?<v@?@\"NSDictionary\"@\"NSError\">64"
- "v72@0:8@16@24@32@40d48d56@?64"

```
