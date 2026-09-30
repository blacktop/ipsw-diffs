## SharedUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x7484
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0xc6c
-  __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x517
-  __TEXT.__oslogstring: 0x643
-  __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__objc_classname: 0x385
-  __TEXT.__objc_methname: 0x1a14
-  __TEXT.__objc_methtype: 0xd84
-  __TEXT.__objc_stubs: 0x1100
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x1e0
-  __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0xc8
+2005.100.174.0.0
+  __TEXT.__text: 0x4ca8
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x954
+  __TEXT.__const: 0x1a8
+  __TEXT.__cstring: 0x3ec
+  __TEXT.__oslogstring: 0x318
+  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_classname: 0x2da
+  __TEXT.__objc_methname: 0x131f
+  __TEXT.__objc_methtype: 0xb6a
+  __TEXT.__objc_stubs: 0xb60
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b8
-  __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x230
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x560
-  __AUTH_CONST.__objc_const: 0x18b8
-  __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x70
-  __DATA.__data: 0x968
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_CONST.__objc_selrefs: 0x620
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x1108
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x7e8
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F00EF1F-3878-334F-84AD-FDAD6CE0EEC7
-  Functions: 233
-  Symbols:   1093
-  CStrings:  606
+  UUID: 28C10945-0E68-33FF-9806-E947DB38B4E3
+  Functions: 158
+  Symbols:   786
+  CStrings:  461
 
Symbols:
+ _OUTLINED_FUNCTION_3
+ __OBJC_$_PROP_LIST_LACUIMechanism
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizingXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizingXPC
+ __OBJC_$_PROTOCOL_REFS_LACContextExternalizingXPC
+ __OBJC_LABEL_PROTOCOL_$_LACContextExternalizingXPC
+ __OBJC_PROTOCOL_$_LACContextExternalizingXPC
+ _objc_retainAutoreleasedReturnValue
- +[LAErrorHelper errorWithCode:withUnderlyingErrors:]
- +[LAErrorHelper errorWithCode:withUnderlyingErrors:].cold.1
- +[LAInstanceIDGenerator sharedInstance]
- +[LAInstanceIDGenerator sharedInstance].cold.1
- +[LAUtils callerRunningOnForeground:pid:]
- -[LABaseService .cxx_destruct]
- -[LABaseService _assertRunningInCorrectQueue]
- -[LABaseService _disconnectClient:]
- -[LABaseService _disconnectClient:].cold.1
- -[LABaseService _disconnectClient:].cold.2
- -[LABaseService _disconnectClient:].cold.3
- -[LABaseService clientsCount]
- -[LABaseService dealloc]
- -[LABaseService dealloc].cold.1
- -[LABaseService endpoint]
- -[LABaseService exportedInterface]
- -[LABaseService exportedInterface].cold.1
- -[LABaseService exportedObject]
- -[LABaseService init]
- -[LABaseService init].cold.1
- -[LABaseService listener:shouldAcceptNewConnection:]
- -[LABaseService listener:shouldAcceptNewConnection:].cold.1
- -[LABaseService manager]
- -[LABaseService queue]
- -[LABaseService serviceID]
- -[LABaseService setManager:]
- -[LABaseServiceManager .cxx_destruct]
- -[LABaseServiceManager _shutdownSessionsWithServiceType:]
- -[LABaseServiceManager allowsMultipleClientsForServiceType:]
- -[LABaseServiceManager bootstrapServiceWithType:clientConnection:completionHandler:]
- -[LABaseServiceManager bootstrapServiceWithType:clientConnection:completionHandler:].cold.1
- -[LABaseServiceManager bootstrapSessionServiceType:clientID:clientConnection:completionHandler:]
- -[LABaseServiceManager bootstrapSessionServiceType:clientID:clientConnection:completionHandler:].cold.1
- -[LABaseServiceManager bootstrapSessionServiceType:clientID:completionHandler:]
- -[LABaseServiceManager exportedInterface]
- -[LABaseServiceManager init]
- -[LABaseServiceManager sessionsCount]
- -[LABaseServiceManager shutdownSessionsWithMatchingID:]
- -[LADefaultServiceSession .cxx_destruct]
- -[LADefaultServiceSession clientID]
- -[LADefaultServiceSession dealloc]
- -[LADefaultServiceSession dealloc].cold.1
- -[LADefaultServiceSession initWithService:serviceType:client:]
- -[LADefaultServiceSession initWithService:serviceType:client:].cold.1
- -[LADefaultServiceSession serviceType]
- -[LADefaultServiceSession service]
- -[LADefaultServiceSession sessionID]
- -[LAInstanceIDGenerator .cxx_destruct]
- -[LAInstanceIDGenerator init]
- -[LAInstanceIDGenerator nextInstanceIDInDomain:]
- -[LAPasscodeHelper accountBlockedForUserID:]
- -[LAPasscodeHelper backoffTimeIntervalForUserID:]
- -[LAPasscodeHelper createStash:mode:manifest:]
- -[LAPasscodeHelper failedAttemptsForUserID:]
- -[LAPasscodeHelper isPasscodeSetForUser:error:]
- -[LAPasscodeHelper isPasscodeSetWithError:]
- -[LAPasscodeHelper maxUnlockAttemptsForUserID:]
- -[LAServiceAdapter .cxx_destruct]
- -[LAServiceAdapter exportedInterface]
- -[LAServiceAdapter exportedObject]
- -[LAServiceAdapter initWithExportedInterface:exportedObject:queue:]
- -[LAServiceAdapter queue]
- GCC_except_table11
- GCC_except_table20
- GCC_except_table6
- OBJC_IVAR_$_LABaseService._clients
- OBJC_IVAR_$_LABaseService._listener
- OBJC_IVAR_$_LABaseService._terminating
- OBJC_IVAR_$_LABaseServiceManager._sessions
- _LACLogService
- _LALogTypeForInternalError
- _LA_LOG_INTERACTIVE
- _LA_LOG_INTERACTIVE.cold.1
- _LA_LOG_INTERACTIVE.log
- _LA_LOG_INTERACTIVE.once
- _NSMultipleUnderlyingErrorsKey
- _OBJC_CLASS_$_LABaseService
- _OBJC_CLASS_$_LABaseServiceManager
- _OBJC_CLASS_$_LACWeakBox
- _OBJC_CLASS_$_LADefaultServiceSession
- _OBJC_CLASS_$_LAInstanceIDGenerator
- _OBJC_CLASS_$_LAServiceAdapter
- _OBJC_CLASS_$_NSUUID
- _OBJC_CLASS_$_NSXPCListener
- _OBJC_CLASS_$_RBSProcessHandle
- _OBJC_CLASS_$_RBSProcessIdentifier
- _OBJC_CLASS_$_RBSProcessPredicate
- _OBJC_CLASS_$_RBSProcessState
- _OBJC_IVAR_$_LABaseService._endpoint
- _OBJC_IVAR_$_LABaseService._queue
- _OBJC_IVAR_$_LABaseService._serviceID
- _OBJC_IVAR_$_LABaseService.manager
- _OBJC_IVAR_$_LADefaultServiceSession._clientID
- _OBJC_IVAR_$_LADefaultServiceSession._service
- _OBJC_IVAR_$_LADefaultServiceSession._serviceType
- _OBJC_IVAR_$_LADefaultServiceSession._sessionID
- _OBJC_IVAR_$_LAInstanceIDGenerator._currentIDs
- _OBJC_IVAR_$_LAServiceAdapter._exportedInterface
- _OBJC_IVAR_$_LAServiceAdapter._exportedObject
- _OBJC_IVAR_$_LAServiceAdapter._queue
- _OBJC_METACLASS_$_LABaseService
- _OBJC_METACLASS_$_LABaseServiceManager
- _OBJC_METACLASS_$_LADefaultServiceSession
- _OBJC_METACLASS_$_LAInstanceIDGenerator
- _OBJC_METACLASS_$_LAServiceAdapter
- __OBJC_$_CLASS_METHODS_LAInstanceIDGenerator
- __OBJC_$_CLASS_PROP_LIST_LAInstanceIDGenerator
- __OBJC_$_INSTANCE_METHODS_LABaseService
- __OBJC_$_INSTANCE_METHODS_LABaseServiceManager
- __OBJC_$_INSTANCE_METHODS_LADefaultServiceSession
- __OBJC_$_INSTANCE_METHODS_LAInstanceIDGenerator
- __OBJC_$_INSTANCE_METHODS_LAServiceAdapter
- __OBJC_$_INSTANCE_VARIABLES_LABaseService
- __OBJC_$_INSTANCE_VARIABLES_LABaseServiceManager
- __OBJC_$_INSTANCE_VARIABLES_LADefaultServiceSession
- __OBJC_$_INSTANCE_VARIABLES_LAInstanceIDGenerator
- __OBJC_$_INSTANCE_VARIABLES_LAServiceAdapter
- __OBJC_$_PROP_LIST_LABaseService
- __OBJC_$_PROP_LIST_LABaseServiceManager
- __OBJC_$_PROP_LIST_LADefaultServiceSession
- __OBJC_$_PROP_LIST_LAService
- __OBJC_$_PROP_LIST_LAServiceSession
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizing
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAServiceManager
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAServiceSession
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACContextExternalizing
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizing
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAService
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAServiceManager
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAServiceSession
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_REFS_LACContextExternalizing
- __OBJC_$_PROTOCOL_REFS_LAService
- __OBJC_$_PROTOCOL_REFS_LAServiceManager
- __OBJC_$_PROTOCOL_REFS_LAServiceSession
- __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
- __OBJC_CLASS_PROTOCOLS_$_LABaseService
- __OBJC_CLASS_PROTOCOLS_$_LABaseServiceManager
- __OBJC_CLASS_PROTOCOLS_$_LADefaultServiceSession
- __OBJC_CLASS_RO_$_LABaseService
- __OBJC_CLASS_RO_$_LABaseServiceManager
- __OBJC_CLASS_RO_$_LADefaultServiceSession
- __OBJC_CLASS_RO_$_LAInstanceIDGenerator
- __OBJC_CLASS_RO_$_LAServiceAdapter
- __OBJC_LABEL_PROTOCOL_$_LACContextExternalizing
- __OBJC_LABEL_PROTOCOL_$_LAService
- __OBJC_LABEL_PROTOCOL_$_LAServiceManager
- __OBJC_LABEL_PROTOCOL_$_LAServiceSession
- __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_METACLASS_RO_$_LABaseService
- __OBJC_METACLASS_RO_$_LABaseServiceManager
- __OBJC_METACLASS_RO_$_LADefaultServiceSession
- __OBJC_METACLASS_RO_$_LAInstanceIDGenerator
- __OBJC_METACLASS_RO_$_LAServiceAdapter
- __OBJC_PROTOCOL_$_LACContextExternalizing
- __OBJC_PROTOCOL_$_LAService
- __OBJC_PROTOCOL_$_LAServiceManager
- __OBJC_PROTOCOL_$_LAServiceSession
- __OBJC_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_PROTOCOL_REFERENCE_$_LAServiceManager
- __OBJC_PROTOCOL_REFERENCE_$_NSObject
- ___39+[LAInstanceIDGenerator sharedInstance]_block_invoke
- ___52-[LABaseService listener:shouldAcceptNewConnection:]_block_invoke
- ___52-[LABaseService listener:shouldAcceptNewConnection:]_block_invoke.cold.1
- ___96-[LABaseServiceManager bootstrapSessionServiceType:clientID:clientConnection:completionHandler:]_block_invoke
- ___96-[LABaseServiceManager bootstrapSessionServiceType:clientID:clientConnection:completionHandler:]_block_invoke.cold.1
- ___96-[LABaseServiceManager bootstrapSessionServiceType:clientID:clientConnection:completionHandler:]_block_invoke.cold.2
- ___96-[LABaseServiceManager bootstrapSessionServiceType:clientID:clientConnection:completionHandler:]_block_invoke.cold.3
- ___LA_LOG_INTERACTIVE_block_invoke
- ___NSDictionary0__struct
- ___block_descriptor_40_e8_32s_e15_"NSString"8?0ls32l8
- ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
- ___block_descriptor_64_e8_32s40s48bs56w_e33_v24?0"<LAService>"8"NSError"16ls32l8s40l8s48l8w56l8
- ___block_literal_global.17
- _objc_claimAutoreleasedReturnValue
- _objc_enumerationMutation
- _objc_msgSend$_assertRunningInCorrectQueue
- _objc_msgSend$_disconnectClient:
- _objc_msgSend$_shutdownSessionsWithServiceType:
- _objc_msgSend$accountBlockedForUserID:
- _objc_msgSend$allValues
- _objc_msgSend$allowsMultipleClientsForServiceType:
- _objc_msgSend$anonymousListener
- _objc_msgSend$backoffTimeIntervalForUserID:
- _objc_msgSend$bootstrapServiceWithType:clientConnection:completionHandler:
- _objc_msgSend$bootstrapSessionServiceType:clientID:clientConnection:completionHandler:
- _objc_msgSend$clientID
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$createStash:mode:manifest:
- _objc_msgSend$currentConnection
- _objc_msgSend$doesNotRecognizeSelector:
- _objc_msgSend$endowmentNamespaces
- _objc_msgSend$endpoint
- _objc_msgSend$errorWithCode:
- _objc_msgSend$exportedInterface
- _objc_msgSend$exportedObject
- _objc_msgSend$failedAttemptsForUserID:
- _objc_msgSend$handleForIdentifier:error:
- _objc_msgSend$handleForPredicate:error:
- _objc_msgSend$identifierWithPid:
- _objc_msgSend$initWithReceiver:
- _objc_msgSend$initWithService:serviceType:client:
- _objc_msgSend$interruptionHandler
- _objc_msgSend$isPasscodeSetWithError:
- _objc_msgSend$maxUnlockAttemptsForUserID:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$predicateMatchingBundleIdentifier:
- _objc_msgSend$queue
- _objc_msgSend$service
- _objc_msgSend$serviceID
- _objc_msgSend$serviceType
- _objc_msgSend$sessionID
- _objc_msgSend$setDelegate:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setManager:
- _objc_msgSend$setWithObject:
- _objc_msgSend$shutdownSessionsWithMatchingID:
- _objc_msgSend$taskState
- _objc_msgSend$unsignedIntegerValue
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ "@\"<LACEvaluationRequest>\"16@0:8"
+ "I16@0:8"
+ "LACContextExternalizingXPC"
+ "T@\"<LACEvaluationRequest>\",R,N"
+ "TB,R,N"
+ "TI,R,N"
+ "failAuthenticationWithError:"
+ "instanceId"
+ "isRunning"
+ "request"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSData\"@\"NSError\">32"
+ "v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "%p"
- "%{public}@[%u] %s visible"
- "%{public}@[%u] is not running scheduled, task state: %u"
- "+[LAErrorHelper errorWithCode:withUnderlyingErrors:]"
- "@"
- "@\"<LAService>\""
- "@\"<LAService>\"16@0:8"
- "@\"<LAServiceManager>\""
- "@\"NSData\"24@0:8^@16"
- "@\"NSString\""
- "@\"NSString\"8@?0"
- "@\"NSUUID\""
- "@\"NSUUID\"16@0:8"
- "@\"NSXPCInterface\""
- "@\"NSXPCListener\""
- "@\"NSXPCListenerEndpoint\""
- "@\"NSXPCListenerEndpoint\"16@0:8"
- "@24@0:8^@16"
- "@40@0:8@16@24@32"
- "Added client to service: %@ clientID: %@"
- "Allocated service: %@"
- "Allocated session service: %@ clientID: %@"
- "B24@0:8^@16"
- "B28@0:8@16i24"
- "B28@0:8I16^@20"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "Could not bootstrap service with type: %{public}@ (%{public}@)"
- "Deallocated service: %@ clients: %ld"
- "Deallocated session service: %@ clientID: %@"
- "Failed service bootstrap serviceType: %@ clientID: %@ error: %@"
- "Failed to get process handle for %{public}@[%u]: %{public}@"
- "Interruption invoked in service: %@"
- "Keeping service alive because there are still %d clients"
- "LABaseService"
- "LABaseServiceManager"
- "LACContextExternalizing"
- "LADefaultServiceSession"
- "LAErrorHelper.m"
- "LAInstanceIDGenerator"
- "LAService"
- "LAServiceAdapter"
- "LAServiceManager"
- "LAServiceSession"
- "NSXPCListenerDelegate"
- "Q24@0:8@16"
- "Registered session service: %@ client: %@"
- "Removed client from service: %@ clientID: %@"
- "Requested termination of service: %@"
- "Reused session service: %@ clientID: %@"
- "Service bootstrapping service not implemented"
- "ServiceKitErrorDomain"
- "ServiceManager did become unavailable"
- "Subclasses of %@ must provide an `exportedInterface`"
- "T@\"<LAService>\",R,N"
- "T@\"<LAService>\",R,N,V_service"
- "T@\"<LAServiceManager>\",W,N,Vmanager"
- "T@\"LAInstanceIDGenerator\",R"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_clientID"
- "T@\"NSString\",R,N,V_serviceID"
- "T@\"NSString\",R,N,V_serviceType"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_sessionID"
- "T@\"NSXPCListenerEndpoint\",R,N"
- "T@\"NSXPCListenerEndpoint\",R,N,V_endpoint"
- "TQ,R,N"
- "Unregistered session service: %@ client: %@"
- "_assertRunningInCorrectQueue"
- "_clientID"
- "_clients"
- "_currentIDs"
- "_disconnectClient:"
- "_endpoint"
- "_exportedInterface"
- "_exportedObject"
- "_listener"
- "_service"
- "_serviceID"
- "_serviceType"
- "_sessionID"
- "_sessions"
- "_shutdownSessionsWithServiceType:"
- "_terminating"
- "accountBlockedForUserID:"
- "allValues"
- "allowsMultipleClientsForServiceType:"
- "anonymousListener"
- "backoffTimeIntervalForUserID:"
- "bootstrapServiceWithType:clientConnection:completionHandler:"
- "bootstrapSessionServiceType:clientID:clientConnection:completionHandler:"
- "bootstrapSessionServiceType:clientID:completionHandler:"
- "callerRunningOnForeground:pid:"
- "clientID"
- "clientsCount"
- "com.apple.frontboard.visibility"
- "countByEnumeratingWithState:objects:count:"
- "createStash:mode:manifest:"
- "currentConnection"
- "d24@0:8@16"
- "doesNotRecognizeSelector:"
- "endowmentNamespaces"
- "endpoint"
- "errorWithCode:withUnderlyingErrors:"
- "exportedInterface"
- "exportedObject"
- "failedAttemptsForUserID:"
- "forciblyInvalidate"
- "handleForIdentifier:error:"
- "handleForPredicate:error:"
- "i"
- "identifierWithPid:"
- "initWithExportedInterface:exportedObject:queue:"
- "initWithReceiver:"
- "initWithService:serviceType:client:"
- "interruptionHandler"
- "is"
- "is not"
- "isPasscodeSetWithError:"
- "listener:shouldAcceptNewConnection:"
- "manager"
- "maxUnlockAttemptsForUserID:"
- "nextInstanceIDInDomain:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "predicateMatchingBundleIdentifier:"
- "q24@0:8@16"
- "q36@0:8@16i24@28"
- "queue"
- "service"
- "serviceID"
- "serviceType"
- "sessionID"
- "sessionsCount"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setManager:"
- "setWithObject:"
- "shutdownSessionsWithMatchingID:"
- "synchronousExternalizedContextWithError:"
- "taskState"
- "underlyingErrors.count > 1"
- "unsignedIntegerValue"
- "v24@0:8@\"NSString\"16"
- "v24@?0@\"<LAService>\"8@\"NSError\"16"
- "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSXPCConnection\"32@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8q16@\"NSDictionary\"24@\"<LAUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LAUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"

```
