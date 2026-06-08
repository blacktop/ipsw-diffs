## AXIDSServices

> `/System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x1b60
-  __TEXT.__auth_stubs: 0x270
+3229.1.6.0.0
+  __TEXT.__text: 0x1874
   __TEXT.__objc_methlist: 0x414
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x19a
+  __TEXT.__cstring: 0x1b0
   __TEXT.__oslogstring: 0x1e7
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x39
-  __TEXT.__objc_methname: 0xdf9
-  __TEXT.__objc_methtype: 0x50e
-  __TEXT.__objc_stubs: 0x6a0
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x128
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x450
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A622638-6C8B-3E7B-AF6C-4F35019D5D4E
-  Functions: 52
-  Symbols:   280
-  CStrings:  249
+  UUID: 24892BE5-1B32-32EF-B6BB-B02B9B343355
+  Functions: 44
+  Symbols:   267
+  CStrings:  65
 
Symbols:
+ _AXIDSServiceDeviceNearbyStatusKey
+ ___block_literal_global.511
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
- +[AXIDSServices sharedInstance].cold.1
- -[AXIDSServices _sendSynchronousMessage:withMessageID:].cold.1
- -[AXIDSServices connectionWithServiceWasInterruptedForUserInterfaceClient:].cold.1
- -[AXIDSServices localService].cold.1
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- ___56-[AXIDSServices _sendAsynchronousMessage:withMessageID:]_block_invoke.cold.1
- ___block_literal_global.487
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "deviceNearbyStatus"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AXUIService>\""
- "@\"AXAccessQueue\"24@0:8Q16"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXUIClient\""
- "@\"NSArray\""
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSDictionary\"48@0:8@\"NSDictionary\"16Q24@\"NSString\"32^@40"
- "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
- "@\"NSHashTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\"24@0:8Q16"
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8Q16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@36@0:8@16Q24B32"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "@48@0:8@16Q24@32^@40"
- "@52@0:8@16Q24@32i40^@44"
- "AXIDSServices"
- "AXUIClientDelegate"
- "AXUIService"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AXUIService>\",R,N,V_localService"
- "T@\"AXUIClient\",R,N,V_idsServerClient"
- "T@\"NSArray\",&,N,V_cachedConnectedDevices"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_availableDevices"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_localServiceQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N,V_isConnectingToAXUIServer"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_availableDevices"
- "_cachedConnectedDevices"
- "_clients"
- "_clientsLock"
- "_connectedDevicesLock"
- "_handleConnectedDevicesChanged:"
- "_handleIncomingDataWithMessage:"
- "_idsServerClient"
- "_init"
- "_initializeServerConnection"
- "_isConnectingToAXUIServer"
- "_localService"
- "_localServiceQueue"
- "_performBlockOnClients:"
- "_sendAsynchronousMessage:withMessageID:"
- "_sendSynchronousMessage:withMessageID:"
- "accessQueueForProcessingMessageWithIdentifier:"
- "addObject:"
- "allObjects"
- "arrayWithArray:"
- "autorelease"
- "availableDevices"
- "backgroundAccessQueue"
- "bundleWithPath:"
- "cachedConnectedDevices"
- "class"
- "conformsToProtocol:"
- "connectedDevices"
- "connectedDevicesDidChange:"
- "connectionWillBeInterruptedForClientWithIdentifier:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "containsClient:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "deregisterForIncomingData:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveIncomingData:"
- "handleMessage:withMessageID:"
- "hash"
- "i24@0:8@\"NSString\"16"
- "i24@0:8@16"
- "idsServerClient"
- "init"
- "initWithIdentifier:serviceBundleName:"
- "isConnectingToAXUIServer"
- "isEqual:"
- "isKindOfClass:"
- "isLoaded"
- "isMemberOfClass:"
- "isProxy"
- "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
- "loadAndReturnError:"
- "localService"
- "localServiceQueue"
- "messageWithIdentifierRequiresWritingBlock:"
- "messageWithIdentifierShouldBeProcessedAsynchronously:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "possibleRequiredEntitlementsForProcessingMessageWithIdentifier:"
- "principalClass"
- "processInitializationMessage:"
- "processMessage:withIdentifier:fromClientWithIdentifier:error:"
- "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:completion:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
- "publishData:"
- "publishData:priority:requestingResponse:"
- "publishData:requestingResponse:"
- "publishDirectIDSData:"
- "publishDirectIDSMessage:"
- "publishMessage:"
- "publishMessage:priority:requestingResponse:"
- "publishMessage:requestingResponse:"
- "publishResourceAtURL:"
- "publishResourceAtURL:priority:requestingResponse:"
- "publishResourceAtURL:requestingResponse:"
- "registerForIncomingData:"
- "release"
- "removeObject:"
- "requiredEntitlementForProcessingMessageWithIdentifier:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "sendPublishMessageToServer:"
- "sendSynchronousMessage:withIdentifier:error:"
- "serverConnectionWasInterrupted"
- "serviceTypeForClientWithIdentifier:"
- "serviceWasFullyInitialized"
- "setCachedConnectedDevices:"
- "setDelegate:"
- "setIsConnectingToAXUIServer:"
- "setLocalServiceQueue:"
- "sharedInstance"
- "shouldUseLocalServiceBundle"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "superclass"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSDictionary\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24@32@?40"
- "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16Q24@32i40@?44"
- "weakObjectsHashTable"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
