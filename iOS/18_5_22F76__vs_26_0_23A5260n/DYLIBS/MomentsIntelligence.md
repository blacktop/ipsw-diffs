## MomentsIntelligence

> `/System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence`

```diff

-206.0.7.0.0
-  __TEXT.__text: 0x7b0
-  __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_methlist: 0xa4
-  __TEXT.__cstring: 0x99
-  __TEXT.__const: 0x10
-  __TEXT.__oslogstring: 0x15b
-  __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x4a
-  __TEXT.__objc_methname: 0x1eb
-  __TEXT.__objc_methtype: 0x6b
-  __TEXT.__objc_stubs: 0x220
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x8
+255.0.0.0.0
+  __TEXT.__text: 0x3c5c
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x374
+  __TEXT.__cstring: 0x2d7
+  __TEXT.__const: 0x38
+  __TEXT.__gcc_except_tab: 0x17c
+  __TEXT.__oslogstring: 0x471
+  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__objc_classname: 0xa1
+  __TEXT.__objc_methname: 0x879
+  __TEXT.__objc_methtype: 0x292
+  __TEXT.__objc_stubs: 0x6c0
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x108
-  __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x60
-  __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x18
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0x528
+  __DATA.__objc_ivar: 0x2c
+  __DATA.__data: 0x120
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C10EBC65-3552-3A06-9910-B579A6FF12C4
-  Functions: 17
-  Symbols:   111
-  CStrings:  51
+  UUID: 299CAE0B-26ED-35D7-9B2E-D28FF8F4F964
+  Functions: 90
+  Symbols:   394
+  CStrings:  213
 
Symbols:
+ +[NSError(MOError) errorUsingError:withUnderyingError:]
+ -[MOConnection .cxx_destruct]
+ -[MOConnection callBlock:onInterruption:]
+ -[MOConnection delegate]
+ -[MOConnection getConnectionName]
+ -[MOConnection initWithName:]
+ -[MOConnection onConnectionInterrupted]
+ -[MOConnection runBlockCompleted:]
+ -[MOConnection runBlockStarted:withConnectionError:]
+ -[MOConnection setDelegate:]
+ -[MOConnectionManager .cxx_destruct]
+ -[MOConnectionManager _callProxy:usingBlock:onError:]
+ -[MOConnectionManager _callProxyProvider:usingBlock:onError:]
+ -[MOConnectionManager _getActiveConnection]
+ -[MOConnectionManager _getActiveConnection].cold.1
+ -[MOConnectionManager _getActiveConnection].cold.2
+ -[MOConnectionManager _getActiveConnection].cold.3
+ -[MOConnectionManager _getSingleCallHandler:]
+ -[MOConnectionManager _makeConnectionErrorWithReason:]
+ -[MOConnectionManager _postProxy:usingBlock:onError:]
+ -[MOConnectionManager _postProxyProvider:usingBlock:onError:]
+ -[MOConnectionManager callAsyncProxyUsingBlock:onError:]
+ -[MOConnectionManager callSyncProxyUsingBlock:onError:]
+ -[MOConnectionManager dealloc]
+ -[MOConnectionManager delegate]
+ -[MOConnectionManager getAsyncProxyProvider]
+ -[MOConnectionManager getConnectionName]
+ -[MOConnectionManager getSyncProxyProvider]
+ -[MOConnectionManager initWithName:usingDelegate:]
+ -[MOConnectionManager invalidate]
+ -[MOConnectionManager postAsyncProxyUsingBlock:onError:]
+ -[MOConnectionManager postSyncProxyUsingBlock:onError:]
+ -[MOConnectionManager setDelegate:]
+ -[MOConnectionManager withProxyProvider:proxyHandler:onError:]
+ -[MOConnectionManager withProxyProvider:proxyHandler:onError:].cold.1
+ -[MOMomentsIntelligenceServiceManager classifyBundleForSystemPrompt:Input:WithReply:]
+ -[MOMomentsIntelligenceServiceManager generatePersonalizedReflectionPromptsWithSystemPrompt:Input:WithReply:]
+ -[MOMomentsIntelligenceServiceManager makeNewConnectionWithInterfaceFor:]
+ GCC_except_table2
+ GCC_except_table36
+ GCC_except_table4
+ GCC_except_table5
+ GCC_except_table7
+ GCC_except_table9
+ _MOErrorDomain
+ _MOLogFacilityGeneral
+ _NSLocalizedDescriptionKey
+ _NSPOSIXErrorDomain
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_MOConnection
+ _OBJC_CLASS_$_MOConnectionManager
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_IVAR_$_MOConnection._delegate
+ _OBJC_IVAR_$_MOConnection._interruptActive
+ _OBJC_IVAR_$_MOConnection._name
+ _OBJC_IVAR_$_MOConnection._pendingRequestCounter
+ _OBJC_IVAR_$_MOConnection._pendingRequests
+ _OBJC_IVAR_$_MOConnectionManager._connectionName
+ _OBJC_IVAR_$_MOConnectionManager._delegate
+ _OBJC_IVAR_$_MOConnectionManager._mo_connection
+ _OBJC_IVAR_$_MOConnectionManager._xpc_connection
+ _OBJC_IVAR_$_MOMomentsIntelligenceServiceManager.connectionManager
+ _OBJC_METACLASS_$_MOConnection
+ _OBJC_METACLASS_$_MOConnectionManager
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __Block_object_dispose
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_MOError
+ __OBJC_$_CATEGORY_NSError_$_MOError
+ __OBJC_$_INSTANCE_METHODS_MOConnection
+ __OBJC_$_INSTANCE_METHODS_MOConnectionManager
+ __OBJC_$_INSTANCE_VARIABLES_MOConnection
+ __OBJC_$_INSTANCE_VARIABLES_MOConnectionManager
+ __OBJC_$_PROP_LIST_MOConnection
+ __OBJC_$_PROP_LIST_MOConnectionManager
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MOConnectionManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOConnectionManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_MOConnectionManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MOMomentsIntelligenceServiceManager
+ __OBJC_CLASS_RO_$_MOConnection
+ __OBJC_CLASS_RO_$_MOConnectionManager
+ __OBJC_LABEL_PROTOCOL_$_MOConnectionManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_MOConnection
+ __OBJC_METACLASS_RO_$_MOConnectionManager
+ __OBJC_PROTOCOL_$_MOConnectionManagerDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ __Unwind_Resume
+ ___109-[MOMomentsIntelligenceServiceManager generatePersonalizedReflectionPromptsWithSystemPrompt:Input:WithReply:]_block_invoke
+ ___109-[MOMomentsIntelligenceServiceManager generatePersonalizedReflectionPromptsWithSystemPrompt:Input:WithReply:]_block_invoke_2
+ ___109-[MOMomentsIntelligenceServiceManager generatePersonalizedReflectionPromptsWithSystemPrompt:Input:WithReply:]_block_invoke_3
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.29
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.cold.1
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.cold.2
+ ___41-[MOConnection callBlock:onInterruption:]_block_invoke
+ ___43-[MOConnectionManager _getActiveConnection]_block_invoke
+ ___43-[MOConnectionManager _getActiveConnection]_block_invoke.8
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.34
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.cold.1
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.36
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.cold.1
+ ___45-[MOConnectionManager _getSingleCallHandler:]_block_invoke
+ ___45-[MOConnectionManager _getSingleCallHandler:]_block_invoke_2
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke.20
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.21
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.cold.1
+ ___53-[MOConnectionManager _postProxy:usingBlock:onError:]_block_invoke
+ ___53-[MOConnectionManager _postProxy:usingBlock:onError:]_block_invoke_2
+ ___61-[MOConnectionManager _callProxyProvider:usingBlock:onError:]_block_invoke
+ ___61-[MOConnectionManager _postProxyProvider:usingBlock:onError:]_block_invoke
+ ___61-[MOConnectionManager _postProxyProvider:usingBlock:onError:]_block_invoke_2
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27.cold.1
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.cold.1
+ ___82-[MOMomentsIntelligenceServiceManager fetchGenerativeModelsAvailabilityWithReply:]_block_invoke_2
+ ___82-[MOMomentsIntelligenceServiceManager fetchGenerativeModelsAvailabilityWithReply:]_block_invoke_3
+ ___85-[MOMomentsIntelligenceServiceManager classifyBundleForSystemPrompt:Input:WithReply:]_block_invoke
+ ___85-[MOMomentsIntelligenceServiceManager classifyBundleForSystemPrompt:Input:WithReply:]_block_invoke_2
+ ___85-[MOMomentsIntelligenceServiceManager classifyBundleForSystemPrompt:Input:WithReply:]_block_invoke_3
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e55_v24?0"<MomentsIntelligenceServiceProtocol>"8?<B?>16ls32l8
+ ___block_descriptor_40_e8_32s_e24_16?0?<v?"NSError">8ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e14_v16?0?<B?>8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v24?08?<B?>16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e5_B8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48w_e17_v16?0"NSError"8lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e8_v16?08ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e55_v24?0"<MomentsIntelligenceServiceProtocol>"8?<B?>16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40bs48bs56w_e17_v16?0"NSError"8lw56l8s40l8s48l8s32l8
+ ___objc_personality_v0
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_fault_impl
+ _objc_alloc_init
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_autoreleaseReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_callProxy:usingBlock:onError:
+ _objc_msgSend$_callProxyProvider:usingBlock:onError:
+ _objc_msgSend$_getActiveConnection
+ _objc_msgSend$_getSingleCallHandler:
+ _objc_msgSend$_makeConnectionErrorWithReason:
+ _objc_msgSend$_postProxy:usingBlock:onError:
+ _objc_msgSend$_postProxyProvider:usingBlock:onError:
+ _objc_msgSend$callAsyncProxyUsingBlock:onError:
+ _objc_msgSend$callBlock:onInterruption:
+ _objc_msgSend$callSyncProxyUsingBlock:onError:
+ _objc_msgSend$classifyBundleForSystemPrompt:Input:WithReply:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$currentHandler
+ _objc_msgSend$delegate
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$generatePersonalizedReflectionPromptsWithSystemPrompt:Input:WithReply:
+ _objc_msgSend$getAsyncProxyProvider
+ _objc_msgSend$getConnectionName
+ _objc_msgSend$getSyncProxyProvider
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithName:usingDelegate:
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$makeNewConnectionWithInterfaceFor:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$onConnectionInterrupted
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$runBlockCompleted:
+ _objc_msgSend$runBlockStarted:withConnectionError:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$userInfo
+ _objc_msgSend$withProxyProvider:proxyHandler:onError:
+ _objc_release
+ _objc_release_x22
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeWeak
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[MOMomentsIntelligenceServiceManager connection]
- -[MOMomentsIntelligenceServiceManager createConnection]
- -[MOMomentsIntelligenceServiceManager setConnection:]
- _OBJC_IVAR_$_MOMomentsIntelligenceServiceManager._connection
- ___55-[MOMomentsIntelligenceServiceManager createConnection]_block_invoke
- ___55-[MOMomentsIntelligenceServiceManager createConnection]_block_invoke.5
- ___82-[MOMomentsIntelligenceServiceManager fetchGenerativeModelsAvailabilityWithReply:]_block_invoke.16
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_literal_global.7
- _objc_msgSend$connection
- _objc_msgSend$createConnection
- _objc_msgSend$setConnection:
CStrings:
+ ""
+ "#16@0:8"
+ "%@ (due '%@')"
+ "%@: proxy error, %@, %@, retrying..."
+ "%@: proxy error, %@, %@."
+ "%@:%@"
+ "-[MOConnectionManager _getActiveConnection]"
+ "-[MOConnectionManager withProxyProvider:proxyHandler:onError:]"
+ "1"
+ "@\"<MOConnectionDelegate>\""
+ "@\"<MOConnectionManagerDelegate>\""
+ "@\"MOConnection\""
+ "@\"MOConnectionManager\""
+ "@\"NSMutableDictionary\""
+ "@\"NSString\""
+ "@\"NSString\"16@0:8"
+ "@\"NSXPCConnection\"24@0:8@\"MOConnectionManager\"16"
+ "@16@?0@?<v@?@\"NSError\">8"
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@32@0:8:16@24"
+ "@32@0:8@16@24"
+ "@32@0:8@?16@?24"
+ "@40@0:8:16@24@32"
+ "@?16@0:8"
+ "@?24@0:8@?16"
+ "A"
+ "Activating connection '%@'"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B8@?0"
+ "Called async proxy provider"
+ "Called sync proxy provider"
+ "Can't activate connection '%@': nil delegate"
+ "Connection '%@' Invalidated"
+ "GENERAL"
+ "Invalid '%@' connection .remoteObjectInterface (in %s:%d)"
+ "MIServiceMgr, calling classifyBundleForProcess"
+ "MIServiceMgr, calling generatePersonalizedReflectionPromptsWithSystemPrompt"
+ "MIServiceMgr, classifyBundleForProcess,XPCService asynchronous error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "MIServiceMgr, generatePersonalizedReflectionPromptsWithSystemPrompt,XPCService asynchronous error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "MOConnection"
+ "MOConnection managed interrupted, retrying..."
+ "MOConnectionManager"
+ "MOConnectionManagerDelegate"
+ "MOError"
+ "MOErrorDomain"
+ "NSObject"
+ "Q"
+ "Q16@0:8"
+ "Should use valid sync proxy block handler (in %s:%d)"
+ "T#,R"
+ "T@\"<MOConnectionDelegate>\",W,N,V_delegate"
+ "T@\"<MOConnectionManagerDelegate>\",W,N,V_delegate"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "Vv16@0:8"
+ "[%s] The connection has been interrupted with %lu pending tasks"
+ "[%s] The connection has been interrupted with zero pending tasks"
+ "^{_NSZone=}16@0:8"
+ "_callProxy:usingBlock:onError:"
+ "_callProxyProvider:usingBlock:onError:"
+ "_connectionName"
+ "_delegate"
+ "_getActiveConnection"
+ "_getSingleCallHandler:"
+ "_interruptActive"
+ "_makeConnectionErrorWithReason:"
+ "_mo_connection"
+ "_name"
+ "_pendingRequestCounter"
+ "_pendingRequests"
+ "_postProxy:usingBlock:onError:"
+ "_postProxyProvider:usingBlock:onError:"
+ "_xpc_connection"
+ "autorelease"
+ "callAsyncProxyUsingBlock:onError:"
+ "callBlock:onInterruption:"
+ "callSyncProxyUsingBlock:onError:"
+ "class"
+ "classifyBundleForSystemPrompt:Input:WithReply:"
+ "conformsToProtocol:"
+ "connectionManager"
+ "copy"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "currentHandler"
+ "debugDescription"
+ "delegate"
+ "description"
+ "dictionaryWithDictionary:"
+ "dictionaryWithObjects:forKeys:count:"
+ "due '%@'"
+ "errorUsingError:withUnderyingError:"
+ "errorWithDomain:code:userInfo:"
+ "generatePersonalizedReflectionPromptsWithSystemPrompt:Input:WithReply:"
+ "getAsyncProxyProvider"
+ "getConnectionName"
+ "getSyncProxyProvider"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "hash"
+ "initWithName:"
+ "initWithName:usingDelegate:"
+ "interruptionBlock"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "localizedFailureReason"
+ "makeNewConnectionWithInterfaceFor:"
+ "nil proxy"
+ "nil proxy @1"
+ "nil proxy @2"
+ "numberWithUnsignedLongLong:"
+ "objectForKeyedSubscript:"
+ "onConnectionInterrupted"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "postAsyncProxyUsingBlock:onError:"
+ "postSyncProxyUsingBlock:onError:"
+ "release"
+ "remote process execution was interrupted"
+ "remoteObjectInterface"
+ "remoteObjectProxyWithErrorHandler:"
+ "removeObjectForKey:"
+ "requestBlock"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "runBlockCompleted:"
+ "runBlockStarted:withConnectionError:"
+ "self"
+ "setDelegate:"
+ "setObject:forKeyedSubscript:"
+ "superclass"
+ "userInfo"
+ "v16@?0@8"
+ "v16@?0@?<B@?>8"
+ "v24@?0@\"<MomentsIntelligenceServiceProtocol>\"8@?<B@?>16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@8@?<B@?>16"
+ "v32@0:8@?16@?24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8@16@?24@?32"
+ "v40@0:8@?16@?24@?32"
+ "withProxyProvider:proxyHandler:onError:"
+ "zone"
- "Connection to XPC service interrupted"
- "Connection to XPC service invalidated"
- "MIServiceMgr,createConnection successful"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "_connection"
- "connection"
- "createConnection"
- "setConnection:"

```
