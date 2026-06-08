## AccessibilityUI

> `/System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x4fc8
-  __TEXT.__auth_stubs: 0x470
+3229.1.6.0.0
+  __TEXT.__text: 0x4410
   __TEXT.__objc_methlist: 0x484
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x2f4
+  __TEXT.__gcc_except_tab: 0x26c
   __TEXT.__oslogstring: 0x812
-  __TEXT.__cstring: 0x26c
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0x13e1
-  __TEXT.__objc_methtype: 0x3fd
-  __TEXT.__objc_stubs: 0xe60
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x278
+  __TEXT.__cstring: 0x272
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x128
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x610
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5AACFE3-604B-354A-B626-6D18254DDF1A
-  Functions: 131
-  Symbols:   573
-  CStrings:  310
+  UUID: 7995CE8B-62C2-397B-8911-7354BC61CC0F
+  Functions: 96
+  Symbols:   503
+  CStrings:  66
 
Symbols:
+ GCC_except_table19
+ GCC_except_table52
+ GCC_except_table58
+ GCC_except_table62
+ GCC_except_table68
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table90
+ ___49-[AXUIClientConnection _processXPCReply:context:]_block_invoke.413
+ ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.367
+ ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.370
+ ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.372
+ ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke_2.371
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$remoteToken
+ _objc_msgSend$setRemoteToken:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- +[AXUIClientConnection sharedClientConnection].cold.1
- -[AXUIClient messageSender:processCustomDataFromXPCReply:].cold.1
- -[AXUIClient messageSender:willSendXPCMessage:context:].cold.1
- -[AXUIClient messageSender:willSendXPCMessage:context:].cold.2
- -[AXUIClientConnection _initializeServiceConnection].cold.1
- -[AXUIClientConnection _processXPCReply:context:].cold.1
- -[AXUIClientConnection _processXPCReply:context:].cold.2
- -[AXUIClientConnection _processXPCReply:context:].cold.3
- -[AXUIClientConnection _processXPCReply:context:].cold.4
- -[AXUIClientConnection performLaunchAngelQueuedTasks].cold.1
- -[AXUIClientConnection performLaunchAngelTask:].cold.1
- GCC_except_table10
- GCC_except_table11
- GCC_except_table12
- GCC_except_table13
- GCC_except_table18
- GCC_except_table20
- GCC_except_table25
- GCC_except_table34
- GCC_except_table36
- GCC_except_table4
- GCC_except_table42
- GCC_except_table67
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- ___31-[AXUIClientConnection cleanUp]_block_invoke.cold.1
- ___42-[AXUIClientConnection tearDownConnection]_block_invoke.cold.1
- ___47-[AXUIClientConnection performLaunchAngelTask:]_block_invoke.cold.1
- ___47-[AXUIClientConnection performLaunchAngelTask:]_block_invoke.cold.2
- ___47-[AXUIClientConnection performLaunchAngelTask:]_block_invoke.cold.3
- ___47-[AXUIClientConnection performLaunchAngelTask:]_block_invoke.cold.4
- ___49-[AXUIClientConnection _processXPCReply:context:]_block_invoke.392
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.346
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.349
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.351
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.351.cold.1
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.cold.1
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke_2.350
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke_2.350.cold.1
- ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke_2.cold.1
- ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- _objc_msgSend$remoteProcess
- _objc_msgSend$setProcessHandle:
- _objc_release_x26
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AXUIClientDelegate>\""
- "@\"AXAccessQueue\""
- "@\"AXUIClientConnection\""
- "@\"AXUIMessageSender\""
- "@\"BSServiceConnection<BSServiceConnectionClient>\""
- "@\"NSDictionary\""
- "@\"NSHashTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16Q24^@32"
- "AXUIClient"
- "AXUIClientConnection"
- "AXUIClientConnectionStateObserver"
- "AXUIMessageSenderDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AXUIClientDelegate>\",W,N,V_delegate"
- "T@\"AXAccessQueue\",&,N,V_connectionAccessQueue"
- "T@\"AXAccessQueue\",&,N,V_registeredClientsAccessQueue"
- "T@\"AXUIClientConnection\",&,N,V_clientConnection"
- "T@\"AXUIMessageSender\",&,N,V_messageSender"
- "T@\"BSServiceConnection<BSServiceConnectionClient>\",&,N,V_serviceConnection"
- "T@\"NSDictionary\",C,N,V_initializationMessage"
- "T@\"NSHashTable\",&,N,V_stateObservers"
- "T@\"NSMutableArray\",&,N,V_serviceRequests"
- "T@\"NSMutableDictionary\",&,N,V_registeredClients"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serviceConnectionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stateObserverQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_clientIdentifier"
- "T@\"NSString\",C,N,V_serviceBundleName"
- "T@\"NSString\",R,C"
- "TB,N,GisRegisteredWithServer,V_registeredWithServer"
- "TB,R,N,GisConnected"
- "TQ,R"
- "Tq,N,V_connectionState"
- "UTF8String"
- "Vv16@0:8"
- "Vv32@0:8@16@?24"
- "^v40@0:8@\"AXUIMessageSender\"16@\"NSObject<OS_xpc_object>\"24^Q32"
- "^v40@0:8@16@24^Q32"
- "^{_NSZone=}16@0:8"
- "_broadcastConnectedStateChange"
- "_cleanUp"
- "_clientConnection"
- "_clientIdentifier"
- "_clientWithIdentifier:"
- "_connectionAccessQueue"
- "_connectionState"
- "_delegate"
- "_initializationMessage"
- "_initializeServiceConnection"
- "_messageSender"
- "_processXPCReply:context:"
- "_registeredClients"
- "_registeredClientsAccessQueue"
- "_registeredWithServer"
- "_requestInitializationMessageFromDelegateIfNeeded"
- "_serverConnectionLock"
- "_serviceBundleName"
- "_serviceConnection"
- "_serviceConnectionQueue"
- "_serviceRequests"
- "_stateObserverQueue"
- "_stateObservers"
- "activate"
- "addObject:"
- "arrayWithObjects:count:"
- "attributeWithDomain:name:"
- "autorelease"
- "axSafelyAddObject:"
- "ax_errorWithDomain:description:"
- "backgroundAccessQueue"
- "canReadInCurrentExecutionThread"
- "canWriteInCurrentExecutionThread"
- "class"
- "cleanUp"
- "clientConnection"
- "clientConnection:didChangeConnectedState:"
- "clientIdentifier"
- "configureConnection:"
- "conformsToProtocol:"
- "connected"
- "connection"
- "connectionAccessQueue"
- "connectionState"
- "connectionWithEndpoint:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "copy"
- "copyXPCMessageFromDictionary:inReplyToXPCMessage:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentContext"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "dictionary"
- "dictionaryFromXPCMessage:error:"
- "endpointForMachName:service:instance:"
- "hash"
- "identifier"
- "init"
- "initWithIdentifier:serviceBundleName:"
- "initWithParentClass:description:appendUUIDToLabel:"
- "initWithUTF8String:"
- "initializationMessage"
- "invalidate"
- "invalidate:"
- "isConnected"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRegisteredWithServer"
- "label"
- "length"
- "messageSchedulingSerializationQueue"
- "messageSender"
- "messageSender:accessLaunchAngelConnectionForMessageWithContext:usingBlock:"
- "messageSender:extractCustomDataFromXPCReply:numberOfKeyValuePairsForCustomData:"
- "messageSender:processCustomDataFromXPCReply:"
- "messageSender:willSendXPCMessage:context:"
- "nonretainedObjectValue"
- "numberWithInteger:"
- "objectForKey:"
- "performAsynchronousReadingBlock:"
- "performAsynchronousWritingBlock:"
- "performLaunchAngelQueuedTasks"
- "performLaunchAngelTask:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSynchronousReadingBlock:"
- "performSynchronousWritingBlock:"
- "q"
- "q16@0:8"
- "registerClient:withIdentifier:"
- "registerConnectionStateObserver:"
- "registeredClients"
- "registeredClientsAccessQueue"
- "registeredWithServer"
- "release"
- "remoteProcess"
- "remoteTarget"
- "remoteTargetWithLaunchingAssertionAttributes:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completionRequiresWritingBlock:completion:"
- "sendBoardServiceMessage:callback:"
- "sendReply:withError:andOriginalXPCMessage:usingConnection:customDataAddingBlock:"
- "sendSynchronousMessage:withIdentifier:context:error:"
- "sendSynchronousMessage:withIdentifier:error:"
- "serviceBundleName"
- "serviceConnection"
- "serviceConnectionQueue"
- "serviceRequests"
- "setActivationHandler:"
- "setClientConnection:"
- "setClientIdentifier:"
- "setConnectionAccessQueue:"
- "setConnectionState:"
- "setDelegate:"
- "setInitializationMessage:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMessageSender:"
- "setObject:forKey:"
- "setProcessHandle:"
- "setRegisteredClients:"
- "setRegisteredClientsAccessQueue:"
- "setRegisteredWithServer:"
- "setServiceBundleName:"
- "setServiceConnection:"
- "setServiceConnectionQueue:"
- "setServiceQuality:"
- "setServiceRequests:"
- "setStateObserverQueue:"
- "setStateObservers:"
- "setTargetQueue:"
- "setXpc_handler:"
- "sharedClientConnection"
- "stateObserverQueue"
- "stateObservers"
- "stringWithFormat:"
- "superclass"
- "tearDownConnection"
- "unregisterClient:withIdentifier:"
- "unregisterConnectionStateObserver:"
- "userInitiated"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v28@0:8@\"AXUIClientConnection\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"AXUIMessageSender\"16^v24"
- "v32@0:8@16@24"
- "v32@0:8@16^v24"
- "v40@0:8@\"AXUIMessageSender\"16@\"NSObject<OS_xpc_object>\"24^v32"
- "v40@0:8@\"AXUIMessageSender\"16^v24@?<v@?@\"<AccessibilityBoardServices_ServerProtocol>\">32"
- "v40@0:8@16@24^v32"
- "v40@0:8@16^v24@?32"
- "v48@0:8@16Q24@32@?40"
- "v52@0:8@16Q24@32B40@?44"
- "valueWithNonretainedObject:"
- "weakObjectsHashTable"
- "xpc_handler"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
