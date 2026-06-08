## Weave

> `/System/Library/PrivateFrameworks/Weave.framework/Weave`

```diff

-5.100.6.0.0
-  __TEXT.__text: 0x882c
-  __TEXT.__auth_stubs: 0x4f0
+8.0.0.0.0
+  __TEXT.__text: 0x7acc
   __TEXT.__objc_methlist: 0xa1c
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x269
-  __TEXT.__oslogstring: 0xd4b
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0x209
-  __TEXT.__objc_methname: 0x1633
-  __TEXT.__objc_methtype: 0x5dc
-  __TEXT.__objc_stubs: 0x1420
-  __DATA_CONST.__got: 0x98
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x254
+  __TEXT.__oslogstring: 0xcbb
+  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__unwind_info: 0x268
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c8
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x288
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1a0
+  __DATA_CONST.__got: 0xa0
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1398
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x480
-  __DATA.__bss: 0x1
   __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/Polaris.framework/Polaris
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E28779E-C90D-3EED-859E-3CD88EBDCFEC
-  Functions: 180
-  Symbols:   864
-  CStrings:  509
+  UUID: CC4608C0-6A5B-31B0-BD69-0888857104C2
+  Functions: 172
+  Symbols:   841
+  CStrings:  109
 
Symbols:
+ _PLSResourceKeyTimer
+ ___19-[WVServer _update]_block_invoke.92
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x25
- -[WVServer createSessionIfNeeded].cold.1
- _WVGetBootArgs
- _WVGetBootArgs.bootArgs
- _WVGetBootArgs.cold.1
- _WVGetBootArgs.onceToken
- _WVPolarisOOLBootArgSet
- _WVPolarisOOLBootArgSet.cold.1
- _WVPolarisOOLBootArgSet.isBootArgSet
- _WVPolarisOOLBootArgSet.onceToken
- ___19-[WVServer _update]_block_invoke.94
- ___33-[WVServer createSessionIfNeeded]_block_invoke.77
- ___WVGetBootArgs_block_invoke
- ___WVPolarisOOLBootArgSet_block_invoke
- ___block_literal_global.9
- _createSessionIfNeeded.onceToken
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$rangeOfString:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$substringFromIndex:
- _objc_msgSend$substringToIndex:
- _objc_retainAutoreleasedReturnValue
- _sysctlbyname
CStrings:
- " "
- "#16@0:8"
- "%04d: WARNING: ool_port_array_enforced=0 boot arg is not set! Polaris functionality is disabled. "
- "%04d: unable to query sysctl 'kern.bootargs' "
- ".cxx_destruct"
- "0"
- "="
- "@"
- "@\"<WVClientProtocol>\""
- "@\"<WVPowerManagerDelegate>\""
- "@\"<WVServiceDelegate>\""
- "@\"<WVServiceListenerDelegate>\""
- "@\"<WVServiceProtocol>\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"32@0:8@\"PSContext\"16@\"NSArray\"24"
- "@\"NSCondition\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSSet\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCInterface\"16@0:8"
- "@\"PSContext\""
- "@\"PSExecutionSession\""
- "@\"WVCalibrationSnapshot\""
- "@\"WVCalibrationSnapshotImpl\""
- "@\"WVGraphProviderParameters\""
- "@\"WVPolarisService\""
- "@\"WVPowerManager\""
- "@\"WVReplaySession\""
- "@\"WVServiceListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"WVGraphProviderParameters\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@28@0:8B16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8@16@24B32"
- "@36@0:8B16@20@28"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCConnection\"16#24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16#24"
- "B32@0:8@16@24"
- "B40@0:8@16@24o^@32"
- "I"
- "I16@0:8"
- "NSCopying"
- "NSObject"
- "NSXPCListenerDelegate"
- "PSExecutionSessionDelegate"
- "PSExecutionSessionResourceDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<WVClientProtocol>\",R,N,V_client"
- "T@\"<WVClientProtocol>\",R,N,V_synchronousClient"
- "T@\"<WVPowerManagerDelegate>\",W,N,V_delegate"
- "T@\"<WVServiceDelegate>\",W,N,V_delegate"
- "T@\"<WVServiceListenerDelegate>\",R,W,N,V_delegate"
- "T@\"<WVServiceProtocol>\",R,N,V_service"
- "T@\"<WVServiceProtocol>\",R,N,V_synchronousService"
- "T@\"NSData\",&,N,V_calibrationBlob"
- "T@\"NSData\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_notificationQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSURL\",&,N,V_replayURL"
- "T@\"NSURL\",R,N,V_replayURL"
- "T@\"NSXPCInterface\",R,N"
- "T@,R,W,N,V_object"
- "TB,?,R,N"
- "TB,N,V_replay"
- "TI,N,V_pm_ack_port"
- "TI,N,V_systemPowerNotifier"
- "TQ,R"
- "T^{IONotificationPort=},N,V_systemPowerPort"
- "UTF8String"
- "Vv16@0:8"
- "WVCalibrationSnapshot"
- "WVCalibrationSnapshotImpl"
- "WVCalibrationSnapshotLiveImpl"
- "WVCalibrationSnapshotReplayImpl"
- "WVClient"
- "WVClientProtocol"
- "WVGraphProviderParameters"
- "WVGraphProviderProtocol"
- "WVPolarisService"
- "WVPowerManager"
- "WVPowerManagerDelegate"
- "WVReplaySession"
- "WVServer"
- "WVService"
- "WVServiceDelegate"
- "WVServiceGraphProtocol"
- "WVServiceListener"
- "WVServiceListenerDelegate"
- "WVServiceProtocol"
- "WVWeakReference"
- "^{IONotificationPort=}"
- "^{IONotificationPort=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_addServiceByName:serviceClass:"
- "_cachedGraphProviders"
- "_calibrationBlob"
- "_calibrationSnapshot"
- "_client"
- "_connect"
- "_connection"
- "_context"
- "_createKeyToProviderMapWithProviders:"
- "_createService:"
- "_currentGraphProviders"
- "_currentServicesNotProvidingGraphs"
- "_currentServicesProvidingGraphs"
- "_delegate"
- "_enableAnonymousListeners"
- "_graphCache"
- "_graphProviderClasses"
- "_graphProviderParameters"
- "_isSleeping"
- "_listener"
- "_listenerQueue"
- "_noOp"
- "_notificationQueue"
- "_object"
- "_pImpl"
- "_pm_ack_port"
- "_polarisExecutionSessionCallback:eventContext:"
- "_polarisService"
- "_powerManager"
- "_removeService:"
- "_replay"
- "_replaySession"
- "_replayURL"
- "_requestedKeys"
- "_requestedKeysLock"
- "_resourceKeyToGraphProviderClass"
- "_serverParameters"
- "_service"
- "_serviceNameToClass"
- "_serviceNameToListener"
- "_serviceQueue"
- "_servicesNotProvidingGraphsLock"
- "_session"
- "_setQueue:"
- "_sleepingCondition"
- "_synchronousClient"
- "_synchronousService"
- "_systemPowerNotifier"
- "_systemPowerPort"
- "_transaction"
- "_update"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addService:"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "anonymousListener"
- "autorelease"
- "broadcast"
- "cacheProvider"
- "calibrationBlob"
- "calibrationSnapshot"
- "checkResourceIsReachableAndReturnError:"
- "class"
- "classesConformingToGraphProviderProtocol"
- "classesConformingToServiceProtocol"
- "clean"
- "client"
- "clientClass"
- "clientInterface"
- "code"
- "commitAddedGraphs:removedGraphs:error:"
- "commitAddedGraphs:removedGraphs:option:error:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "computeInputKeysFromGraphs:"
- "computeOutputKeysFromGraphs:"
- "configureServerWithParameters:"
- "configureWithParameters:"
- "conformsToProtocol:"
- "containsObject:"
- "context"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createGraphs:forResourceKeys:"
- "createObserverGraphsWithContext:forResourceKeys:"
- "createSessionAtInit"
- "createSessionIfNeeded"
- "deadlineMissThresholdExceededForGraph:"
- "deadlineMissThresholdExceededForGraph:name:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "deleteSession"
- "description"
- "didDiscoverService:"
- "dynamicResourcesAreAvailable:"
- "dynamicResourcesAreNoLongerAvailable:"
- "endpoint"
- "endpointForServiceWithName:"
- "enteringSleep"
- "enumerateKeysAndObjectsUsingBlock:"
- "exceptionWithName:reason:userInfo:"
- "executionSession"
- "exitingSleep"
- "forwardInvocation:"
- "graphsSubmitted"
- "graphsWillBeRemoved:"
- "hash"
- "init"
- "initAsLocalService"
- "initForLocalReplay"
- "initInProcess"
- "initInProcess:recordingURL:"
- "initInProcess:replaySession:recordingURL:"
- "initInProcessWithRecordingURL:"
- "initWithCapacity:"
- "initWithConnection:"
- "initWithDelegate:serviceClasses:"
- "initWithDelegate:serviceClasses:enableAnonymousListeners:"
- "initWithEndpoint:"
- "initWithIsReplayEnabled:replayURL:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithObject:"
- "initWithParameters:"
- "initWithReplaySession:"
- "initWithReplaySession:inProcess:"
- "initWithReplayURL:"
- "initWithSnapshot:"
- "initWithURL:"
- "input"
- "inputs"
- "intersectSet:"
- "invalidate"
- "invokeWithTarget:"
- "isCurrentServicesContainsClass:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "kern.bootargs"
- "listener:shouldAcceptNewConnection:"
- "listenerForServiceWithName:"
- "listenerShouldAcceptNewConnection:forClass:"
- "lock"
- "methodSignatureForSelector:"
- "minusSet:"
- "mutableCopy"
- "notificationQueue"
- "object"
- "objectForKeyedSubscript:"
- "ool_port_array_enforced"
- "output"
- "outputKeys"
- "outputs"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pm_ack_port"
- "prepopulateGraphContext:"
- "publishContext"
- "raise:format:"
- "rangeOfString:"
- "readers"
- "recordingURL"
- "registerSessionCallback:withContext:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "replay"
- "replayURL"
- "requestServerUpdate"
- "requestedResourceKeys"
- "resourceKey"
- "resourceRequestsAreComplete:"
- "resourceStreamForKey:"
- "resourcesNoLongerWanted:"
- "resourcesRequested:"
- "respondsToSelector:"
- "restartIfNeed"
- "resume"
- "retain"
- "retainCount"
- "runningReplaySession"
- "self"
- "service"
- "serviceDidInterrupt"
- "serviceDidInterrupt:"
- "serviceDidInvalidate"
- "serviceDidInvalidate:"
- "serviceInterface"
- "serviceName"
- "serviceWithErrorHandler:"
- "set"
- "setCalibrationBlob:"
- "setDelegate:"
- "setDelegate:delegateQueue:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNotificationQueue:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPm_ack_port:"
- "setRemoteObjectInterface:"
- "setReplay:"
- "setReplayURL:"
- "setSystemPowerNotifier:"
- "setSystemPowerPort:"
- "setValue:forKey:"
- "setWithArray:"
- "shutdown"
- "shutdownIfNeeded"
- "snapshotData"
- "sourceTasks"
- "start"
- "start:"
- "startPolarisServiceAtInit"
- "startPowerManagement"
- "stopSynchronously"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "superclass"
- "synchronousClient"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "synchronousService"
- "synchronousServiceWithErrorHandler:"
- "systemHasPoweredOn"
- "systemHasPoweredOnNotification"
- "systemPowerNotifier"
- "systemPowerPort"
- "systemWillSleep"
- "systemWillSleepNotification"
- "tasks"
- "tearDown"
- "unionSet:"
- "unlock"
- "updateParametersForGraphProvider:"
- "updateResourcesWithAddedResources:removedResources:"
- "updateWithGraphProviders:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"PSContext\"16"
- "v24@0:8@\"WVGraphProviderParameters\"16"
- "v24@0:8@\"WVService\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8^{IONotificationPort=}16"
- "v32@0:8@\"PSGraph\"16@\"NSString\"24"
- "v32@0:8@16#24"
- "v32@0:8@16@24"
- "v32@0:8Q16^v24"
- "wait"
- "waitForContextFromExecutionSessionsProvidingResources:"
- "weakReferenceWithObject:"
- "writers"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
