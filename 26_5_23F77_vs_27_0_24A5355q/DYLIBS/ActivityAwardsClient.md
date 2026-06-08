## ActivityAwardsClient

> `/System/Library/PrivateFrameworks/ActivityAwardsClient.framework/ActivityAwardsClient`

```diff

-2026.5.2.0.0
-  __TEXT.__text: 0x57a0
-  __TEXT.__auth_stubs: 0x340
+2027.0.18.0.0
+  __TEXT.__text: 0x55e8
   __TEXT.__objc_methlist: 0x33c
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x168
-  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__cstring: 0x16c
+  __TEXT.__gcc_except_tab: 0x134
   __TEXT.__oslogstring: 0x839
   __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x7e
-  __TEXT.__objc_methname: 0x8ec
-  __TEXT.__objc_methtype: 0x24b
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x740
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BD8D8DA-B864-3593-A16B-EFBDB5B6F194
-  Functions: 133
-  Symbols:   475
-  CStrings:  194
+  UUID: 20AE356C-622F-33DF-B2F4-40BBF2143662
+  Functions: 131
+  Symbols:   474
+  CStrings:  53
 
Symbols:
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.423
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.424
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.433
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.433.cold.1
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.434
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.434.cold.1
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.435
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.435.cold.1
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.425
+ ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.425.cold.1
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.437
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.437.cold.1
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.440
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.440.cold.1
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.443
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.443.cold.1
+ ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.415
+ ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.415.cold.1
+ ___61-[AACXPCClient sendSynchronousRequest:payload:resultHandler:]_block_invoke.422
+ ___block_literal_global.417
+ ___block_literal_global.439
+ ___block_literal_global.442
+ ___block_literal_global.445
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.402
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.403
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.412
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.412.cold.1
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.413
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.413.cold.1
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.414
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke.414.cold.1
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.404
- ___42-[AACXPCClient _remoteProxy:errorHandler:]_block_invoke_2.404.cold.1
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.416
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.416.cold.1
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.419
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.419.cold.1
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.422
- ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke.422.cold.1
- ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.394
- ___55-[AACXPCClient _serverQueue_initializeDaemonConnection]_block_invoke.394.cold.1
- ___61-[AACXPCClient sendSynchronousRequest:payload:resultHandler:]_block_invoke.401
- ___block_literal_global.396
- ___block_literal_global.418
- ___block_literal_global.421
- ___block_literal_global.424
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AACXPCClient\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "AACAwardsClient"
- "AACInitialHistoricalRunStatus"
- "AACTransportInterface"
- "AACXPCClient"
- "AACXPCListenerEndpointInterface"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"AACXPCClient\",&,N,V_client"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R,V_isComplete"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_client"
- "_clientQueue"
- "_discardEndpointConnection:"
- "_endpointConnection"
- "_handleError:"
- "_isComplete"
- "_lock"
- "_mainDaemonConnection"
- "_remoteProxy:errorHandler:"
- "_remoteSynchronousProxy:errorHandler:"
- "_resetEndpointConnection"
- "_serverQueue"
- "_serverQueue_initializeDaemonConnection"
- "achievements"
- "achievementsForTemplateNames:completion:"
- "addEarnedInstances:completion:"
- "addObject:"
- "addTemplates:completion:"
- "allAchievementsWithCompletion:"
- "allAchievementsWithError:"
- "anniversaryAchievementsForDate:templateNames:completion:"
- "autorelease"
- "boolValue"
- "class"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createEndpointNamed:completion:"
- "data"
- "dataWithJSONObject:options:error:"
- "dealloc"
- "debugDescription"
- "description"
- "earnedAchievementsForDateInterval:completion:"
- "ephemeralAchievementWithTemplateUniqueName:error:"
- "hash"
- "hk_isXPCConnectionError"
- "init"
- "initWithCodable:"
- "initWithData:"
- "initWithIsComplete:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:options:"
- "initialHistoricalRunStatusWithError:"
- "interfaceWithProtocol:"
- "invalidate"
- "isComplete"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "numberWithUnsignedInteger:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "provideAchievementProgressUpdates:completion:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeEarnedInstances:completion:"
- "removeTemplates:completion:"
- "removeTemplatesForSource:completion:"
- "removeTemplatesWithUniqueNames:completion:"
- "requestAwardingWithTriggers:completion:"
- "requestProgressUpdateForProgressProviderIdentifier:completion:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "scheduleAwardingWithCompletion:"
- "self"
- "sendRequest:completion:"
- "sendRequest:payload:completion:"
- "sendRequest:payloadData:completion:"
- "sendSynchronousRequest:payload:resultHandler:"
- "sendSynchronousRequest:resultHandler:"
- "setAchievementProgressUpdates:"
- "setClient:"
- "setEarnedInstances:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setTemplates:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "templates"
- "templatesForSource:completion:"
- "transportEvent:data:"
- "transportRequest:data:completion:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v32@0:8Q16@\"NSData\"24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
