## SoftwareUpdateCoreConnect

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`

```diff

-2422.120.23.0.9
-  __TEXT.__text: 0xb68c
-  __TEXT.__auth_stubs: 0x480
+2717.0.0.0.0
+  __TEXT.__text: 0xa6b4
   __TEXT.__objc_methlist: 0x9c8
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x340
-  __TEXT.__cstring: 0xb6b
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__cstring: 0xb0a
   __TEXT.__oslogstring: 0x1de0
-  __TEXT.__unwind_info: 0x348
-  __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methname: 0x1b8b
-  __TEXT.__objc_methtype: 0x5b3
-  __TEXT.__objc_stubs: 0x12a0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x338
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x330
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x670
+  __DATA_CONST.__objc_selrefs: 0x678
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x12d8
+  __AUTH_CONST.__objc_const: 0x1238
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x360
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B6E9E50-852F-3E28-A9E2-F321F5412105
-  Functions: 263
-  Symbols:   1013
-  CStrings:  611
+  UUID: 064C779E-FA0D-316F-A39C-38E947D03DD5
+  Functions: 257
+  Symbols:   997
+  CStrings:  225
 
Symbols:
+ +[SUCoreConnectMessage generateRequestID]
+ -[SUCoreConnectMessage constructedClientID]
+ -[SUCoreConnectMessage initWithType:messageName:clientID:requestID:message:]
+ -[SUCoreConnectMessage requestID]
+ GCC_except_table5
+ GCC_except_table9
+ _OBJC_IVAR_$_SUCoreConnectMessage._requestID
+ ___block_literal_global.11
+ ___block_literal_global.23
+ _generateRequestID.sRequestID
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$constructedClientID
+ _objc_msgSend$generateRequestID
+ _objc_msgSend$initWithType:messageName:clientID:requestID:message:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$requestID
+ _objc_msgSend$unsignedLongLongValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- +[SUCoreConnectMessage validateMessageDictionary:]
- -[SUCoreConnectClientPolicy clientProcessIdentifier]
- -[SUCoreConnectClientProxy clientProcessIdentifier]
- -[SUCoreConnectMessage clientProcessIdentifier]
- GCC_except_table4
- GCC_except_table50
- GCC_except_table51
- GCC_except_table8
- _OBJC_IVAR_$_SUCoreConnectClientPolicy._clientIDRaw
- _OBJC_IVAR_$_SUCoreConnectClientPolicy._clientProcessIdentifier
- _OBJC_IVAR_$_SUCoreConnectClientProxy._clientProcessIdentifier
- _OBJC_IVAR_$_SUCoreConnectMessage._clientIDRaw
- _OBJC_IVAR_$_SUCoreConnectMessage._clientProcessIdentifier
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- ___block_literal_global.16
- ___block_literal_global.27
- _objc_msgSend$clientIDRaw
- _objc_msgSend$clientProcessIdentifier
- _objc_msgSend$decodeIntForKey:
- _objc_msgSend$encodeInt:forKey:
- _objc_msgSend$processIdentifier
- _objc_msgSend$validateMessageDictionary:
- _objc_retain_x27
CStrings:
+ "\t\t%@\n"
+ "\t%@: %@\t]\n"
+ "%@.<REQ-%llu>"
+ "RequestID"
+ "SUCoreConnectMessage(type:%@|name:%@|clientID:%@|error:%@|message:%@)"
+ "[\n"
- "#16@0:8"
- "%@.<%d>"
- ".cxx_destruct"
- "7"
- "@\"<NSObject>\""
- "@\"<SUCoreConnectClientDelegate>\""
- "@\"<SUCoreConnectServerDelegate>\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSSet\"24@0:8@\"NSString\"16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"SUCoreConnectClientPolicy\""
- "@\"SUCoreConnectServerPolicy\""
- "@\"SUCoreConnectVersion\""
- "@\"SUCoreLog\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@?32@?40"
- "@56@0:8q16@24@32@40@48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "ClientIDRaw"
- "ClientProcessIdentifier"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "SUCoreConnectClient"
- "SUCoreConnectClientProtocol"
- "SUCoreConnectClientProxy"
- "SUCoreConnectClientProxyProtocol"
- "SUCoreConnectConstants"
- "SUCoreConnectMessage requires a valid message dictionary"
- "SUCoreConnectMessage(type:%@|name:%@|clientID:%@|clientIDRaw:%@|clientProcessIdentifier:%d|version:%@|error:%@|message:%@)"
- "SUCoreConnectPolicyProtocol"
- "SUCoreConnectPolicyProtocolPrivate"
- "SUCoreConnectServer"
- "SUCoreConnectServerProtocol"
- "SUCoreConnectVersion"
- "T#,R"
- "T@\"<NSObject>\",&,V_xpcActivityBoost"
- "T@\"<SUCoreConnectClientDelegate>\",R,W,N,V_clientDelegate"
- "T@\"<SUCoreConnectServerDelegate>\",R,W,N,V_serverDelegate"
- "T@\"NSDictionary\",R,&,N,V_message"
- "T@\"NSError\",R,&,N,V_error"
- "T@\"NSMutableDictionary\",R,&,N,V_connections"
- "T@\"NSMutableSet\",R,&,N,V_observerConnections"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_clientCompletionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_clientDelegateCallbackQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_clientMessageQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_clientReplyCompletionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_completionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_connectionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_connectionSendMessageQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_connectionsAccessQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_delegateQueue"
- "T@\"NSSet\",&,N,V_proxyObjectClasses"
- "T@\"NSSet\",R,&,N,V_allowlistedClasses"
- "T@\"NSSet\",R,&,N,V_entitlements"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,&,N,V_clientID"
- "T@\"NSString\",R,&,N,V_clientIDRaw"
- "T@\"NSString\",R,&,N,V_messageName"
- "T@\"NSString\",R,&,N,V_selectorString"
- "T@\"NSString\",R,&,N,V_serviceName"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_messageClientID"
- "T@\"NSString\",R,N,V_messageName"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "T@\"NSXPCListener\",&,N,V_listener"
- "T@\"SUCoreConnectClientPolicy\",R,&,N,V_policy"
- "T@\"SUCoreConnectServerPolicy\",R,&,N,V_connectionPolicy"
- "T@\"SUCoreConnectVersion\",R,&,N,V_version"
- "T@\"SUCoreLog\",R,&,N,V_logger"
- "T@?,R,N,V_genericBlock"
- "T@?,R,N,V_progressBlock"
- "TB,GisBoostable,V_boostable"
- "TB,N,V_usesPersistentXPCConnections"
- "TB,R"
- "TQ,R"
- "Ti,R,N,V_clientProcessIdentifier"
- "Tq,R,N,V_messageType"
- "T{?=[8I]},N,V_clientConnectionAuditToken"
- "T{os_unfair_lock_s=I},N,V_stateLock"
- "T{os_unfair_lock_s=I},R,N,V_stateLock"
- "UTF8String"
- "Version"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_allowlistedClasses"
- "_boostable"
- "_clientCompletionQueue"
- "_clientConnectionAuditToken"
- "_clientDelegate"
- "_clientDelegateCallbackQueue"
- "_clientID"
- "_clientIDForConnection:"
- "_clientIDRaw"
- "_clientMessageQueue"
- "_clientProcessIdentifier"
- "_clientReplyCompletionQueue"
- "_completionQueue"
- "_connectMessageMatchesClient:errorPtr:"
- "_connectionPolicy"
- "_connectionQueue"
- "_connectionSendMessageQueue"
- "_connections"
- "_connectionsAccessQueue"
- "_connectionsForClientID:"
- "_delegateQueue"
- "_droppedConnection:"
- "_entitlements"
- "_error"
- "_genericBlock"
- "_getAllObserverConnections"
- "_getAllowlistedClassesForKey:"
- "_getSharedClientAccessQueue"
- "_getSharedClientAllowlistedClasses"
- "_getSharedServerAccessQueue"
- "_getSharedServerAllowlistedClasses"
- "_informObserversOfCompletionReplyWithMessage:error:"
- "_internalConnectToServer"
- "_invalidateConnectionIfNonPersistent:"
- "_listener"
- "_logger"
- "_message"
- "_messageClientID"
- "_messageName"
- "_messageType"
- "_observerConnections"
- "_policy"
- "_progressBlock"
- "_proxyObjectClasses"
- "_removeConnection:"
- "_selectorString"
- "_serverConnection"
- "_serverDelegate"
- "_serviceName"
- "_setConnection:forClientID:"
- "_setQueue:"
- "_sharedClientLogger"
- "_stateLock"
- "_usesPersistentXPCConnections"
- "_version"
- "_xpcActivityBoost"
- "addObject:"
- "allowlistedClasses"
- "arrayWithObjects:count:"
- "auditToken"
- "autorelease"
- "beginActivityWithOptions:reason:"
- "boolValue"
- "boostable"
- "buildError:underlying:description:"
- "checkedDescription"
- "class"
- "clearAllowlistedClasses"
- "clientCompletionQueue"
- "clientConnectionAuditToken"
- "clientDelegate"
- "clientDelegateCallbackQueue"
- "clientID"
- "clientIDRaw"
- "clientMessageQueue"
- "clientProcessIdentifier"
- "clientReplyCompletionQueue"
- "code"
- "completionQueue"
- "conformsToProtocol:"
- "connectClientSendServerMessage:"
- "connectClientSendServerMessage:proxyObject:withReply:"
- "connectClientSendSynchronousServerMessage:proxyObject:errorPtr:"
- "connectProtocolFromClientSendServerMessage:"
- "connectProtocolFromClientSendServerMessage:proxyObject:withReply:"
- "connectProtocolFromServerRequestClientID:"
- "connectProtocolFromServerSendClientMessage:"
- "connectProtocolFromServerSendClientMessage:reply:"
- "connectServerSendClientMessage:"
- "connectToServerWithCompletion:"
- "connectToServerWithSynchronousCompletion:"
- "connectionClosed"
- "connectionClosedForClientID:"
- "connectionPolicy"
- "connectionQueue"
- "connectionSendMessageQueue"
- "connections"
- "connectionsAccessQueue"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentConnection"
- "dealloc"
- "debugDescription"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultClasses"
- "delegateQueue"
- "description"
- "enableTransactions"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endActivity:"
- "entitlements"
- "error"
- "executeGenericBlock:"
- "executeGenericBlock:disableVerboseLogging:"
- "executeProgressBlock:"
- "executeProgressBlock:disableVerboseLogging:"
- "forceCloseConnection"
- "genericBlock"
- "getAllowlistedClassesForKey:"
- "handleMessage:proxyObject:reply:"
- "handleMessage:reply:"
- "handleResponse:error:"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initForServiceName:delegate:"
- "initForServiceName:delegate:clientID:"
- "initWithCategory:"
- "initWithClientID:completionQueue:genericBlock:"
- "initWithClientID:completionQueue:genericBlock:progressBlock:"
- "initWithClientID:completionQueue:progressBlock:"
- "initWithClientPolicy:"
- "initWithCoder:"
- "initWithFormat:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithMessage:"
- "initWithSelector:"
- "initWithServerPolicy:"
- "initWithServiceName:entitlements:serverDelegate:"
- "initWithString:"
- "initWithType:messageName:clientID:version:message:"
- "interfaceWithProtocol:"
- "invalidate"
- "isBoostable"
- "isConnection:authorizedForMessage:"
- "isConnectionAuthorized:"
- "isConnectionEntitled:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "logger"
- "message"
- "messageClientID"
- "messageName"
- "messageType"
- "mutableCopy"
- "nameForMessageType:"
- "objectForKey:"
- "observerConnections"
- "oslog"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "policy"
- "processIdentifier"
- "processInfo"
- "progressBlock"
- "proxyObjectClasses"
- "q"
- "q16@0:8"
- "reason"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "safeObjectForKey:ofClass:"
- "selectorString"
- "self"
- "serverConnection"
- "serverDelegate"
- "serviceName"
- "setAllowlistedClass:forKey:"
- "setAllowlistedClasses:forKey:"
- "setAllowlistedClasses:forKeys:"
- "setBoostable:"
- "setByAddingObject:"
- "setByAddingObjectsFromSet:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientConnectionAuditToken:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setListener:"
- "setProxyObjectClasses:"
- "setRemoteObjectInterface:"
- "setSafeObject:forKey:"
- "setServerConnection:"
- "setStateLock:"
- "setUsesPersistentXPCConnections:"
- "setWithArray:"
- "setWithObject:"
- "setXpcActivityBoost:"
- "setupListenerAndResumeConnection"
- "sharedCore"
- "sharedDiag"
- "sharedLogger"
- "stateLock"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringIsEqual:to:"
- "stringWithFormat:"
- "summary"
- "superclass"
- "supportsSecureCoding"
- "suspend"
- "suspendListenerAndInvalidate"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "trackAnomaly:forReason:withResult:withError:"
- "trackError:forReason:withResult:withError:"
- "trackFault:forReason:withResult:withError:"
- "usesPersistentXPCConnections"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"SUCoreConnectMessage\"16"
- "v24@0:8@\"SUCoreProgress\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v28@0:8@\"SUCoreProgress\"16B24"
- "v28@0:8@16B24"
- "v32@0:8#16@\"NSString\"24"
- "v32@0:8#16@24"
- "v32@0:8@\"NSSet\"16@\"NSSet\"24"
- "v32@0:8@\"NSSet\"16@\"NSString\"24"
- "v32@0:8@\"SUCoreConnectMessage\"16@?<v@?@\"SUCoreConnectMessage\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"SUCoreConnectMessage\"16@\"SUCoreConnectClientProxy\"24@?<v@?@\"SUCoreConnectMessage\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8{?=[8I]}16"
- "validateMessageDictionary:"
- "valueForEntitlement:"
- "version"
- "xpcActivityBoost"
- "xpcBoost"
- "zone"
- "{?=\"val\"[8I]}"
- "{?=[8I]}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
