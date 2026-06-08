## NFC

> `/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x9fc8
-  __TEXT.__auth_stubs: 0x760
+1176.0.26.502.1
+  __TEXT.__text: 0x94ec
   __TEXT.__objc_methlist: 0x3c4
   __TEXT.__cstring: 0xd76
   __TEXT.__const: 0x18ec
   __TEXT.__oslogstring: 0x17a2
-  __TEXT.__gcc_except_tab: 0x174
+  __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0xe05
-  __TEXT.__objc_methtype: 0x394
-  __TEXT.__objc_stubs: 0xde0
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x900
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x478
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__const: 0x120
+  __DATA_CONST.__got: 0x180
+  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0xfe0
   __AUTH_CONST.__objc_const: 0x5d8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x120
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3001153-6D45-350B-A61B-641C1D4548E6
-  Functions: 154
-  Symbols:   1038
-  CStrings:  623
+  UUID: 738A447D-F85D-3C8A-83EF-003EAF86A104
+  Functions: 150
+  Symbols:   1051
+  CStrings:  396
 
Symbols:
+ -[AccessoryTransportPluginNFC _createEndpointsForTags:skipWalletAuth:].cold.1
+ -[AccessoryTransportPluginNFC _createEndpointsForTags:skipWalletAuth:].cold.2
+ -[AccessoryTransportPluginNFC _createEndpointsForTags:skipWalletAuth:].cold.3
+ -[AccessoryTransportPluginNFC _createEndpointsForTags:skipWalletAuth:].cold.4
+ -[AccessoryTransportPluginNFC _pollTags:].cold.3
+ -[AccessoryTransportPluginNFC _pollTags:].cold.4
+ -[AccessoryTransportPluginNFC _pollTags:].cold.5
+ -[AccessoryTransportPluginNFC _pollTags:].cold.6
+ -[AccessoryTransportPluginNFC _pollTags:].cold.7
+ -[AccessoryTransportPluginNFC _pollTags:].cold.8
+ ___block_literal_global.251
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
+ _objc_retain_x9
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "PearlIDCapability"
- "#16@0:8"
- ".cxx_destruct"
- "8olRm6C1xqr7AJGpLRnpSw"
- "@\"NFACTag\""
- "@\"NFAccessoryReaderSession\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACCPluginProtocol"
- "ACCTransportPluginProtocol"
- "ACCUserDefaults"
- "AccessoryTransportPluginNFC"
- "B"
- "B16@0:8"
- "B20@0:8C16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8C16^@20"
- "B36@0:8B16@20@28"
- "B40@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "C24@0:8@16"
- "I16@0:8"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "TB,N,V_isRunning"
- "TB,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__IOHIDEventSystemClient=}"
- "_animationDelayMs:"
- "_checkLRC:"
- "_checkProductTypeCompatibility:"
- "_closeReaderSession"
- "_connectPeer:"
- "_connectToTagId:"
- "_connectedTag"
- "_connectedTagEndpointUuid"
- "_connectedTagId"
- "_connectionUuidForEndpointUuid"
- "_createEndpointsForTags:skipWalletAuth:"
- "_decodeTagIdentifier:"
- "_didNfcTagsListChange:"
- "_didScreenStateChange:"
- "_getAccessoryFamily:"
- "_getAccessoryType:"
- "_getNfcStateMachineState"
- "_getTimeSinceLastRequestPowerPauseMs"
- "_getpowerPauseStatus"
- "_handleIOHIDEvent:"
- "_handleNearFieldAccessoryEventNotification:"
- "_handleSessionOpen:forEndpointWithUUID:connectionUUID:"
- "_hasWalletOnClearCase2020:"
- "_hidEventClient"
- "_initXPC"
- "_isRunning"
- "_lastRequestPowerPauseTime"
- "_notifyAuthReadyAfterPowerPauseComplete"
- "_peers"
- "_pollTags:"
- "_polledSem"
- "_polledTags"
- "_proxRequestTime"
- "_proximityOcclusionState"
- "_queue"
- "_readerSession"
- "_requestPowerPause"
- "_requestedOpenEndpointUUID"
- "_requiresLegacyAuth:"
- "_requiresMfi40Auth:"
- "_screenState"
- "_screenStateToken"
- "_setProximityMonitoringEnabled:"
- "_setScreenStateMonitoringEnabled:"
- "_tagForConnectionUuid"
- "_tagsArrivalTime"
- "_tagsHavePowerBits:uuid:"
- "_updateAccessoryPower:"
- "_waitProxState"
- "addObject:"
- "allKeys"
- "appendBytes:length:"
- "appendData:"
- "arrayForKey:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "authStatusDidChange:forConnectionWithUUID:previousAuthStatus:authType:connectionIsAuthenticated:connectionWasAuthenticated:"
- "autorelease"
- "boolForKey:"
- "boolValue"
- "class"
- "clearMultiTagState"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "connectTag:error:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createConnectionWithType:andIdentifier:"
- "createEndpointWithTransportType:andProtocol:andIdentifier:forConnectionWithUUID:publishConnection:"
- "dataWithBytes:length:"
- "date"
- "debugDescription"
- "defaultCenter"
- "description"
- "destroyConnectionWithUUID:"
- "destroyEndpointWithUUID:"
- "dictionaryForKey:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "disconnectTag:"
- "doubleForKey:"
- "doubleValue"
- "enableMultiTag:"
- "endSessionWithCompletion:"
- "enumerateKeysAndObjectsUsingBlock:"
- "firstObject"
- "getBytes:length:"
- "getMultiTagState:"
- "hash"
- "i20@0:8C16"
- "init"
- "initPlugin"
- "initWithSuiteName:"
- "integerForKey:"
- "isEqual:"
- "isEqualToData:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "length"
- "null"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithInt:"
- "objectAtIndexedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginName"
- "postNotificationName:object:userInfo:"
- "processIncomingData:forEndpointWithUUID:"
- "propertiesDidChange:forConnectionWithUUID:previousProperties:"
- "propertiesDidChange:forEndpointWithUUID:previousProperties:connectionUUID:"
- "publishConnectionWithUUID:"
- "raise:format:"
- "readTypeIdentifier:"
- "readerSession:didDetectTags:"
- "readerSessionDidEndUnexpectedly:"
- "release"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectIdenticalTo:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAccessoryProtocolCommand:outError:"
- "sendOutgoingData:forEndpointWithUUID:connectionUUID:"
- "setDelegate:"
- "setDouble:forKey:"
- "setInteger:forKey:"
- "setIsRunning:"
- "setObject:forKey:"
- "setProperties:forConnectionWithUUID:"
- "setProperties:forEndpointWithUUID:"
- "setValue:forKey:"
- "sharedDefaults"
- "sharedDefaultsIapd"
- "sharedDefaultsLogging"
- "sharedHardwareManager"
- "silentType"
- "startPlugin"
- "startPollingForTechnology:error:"
- "startReaderSession:"
- "stopPlugin"
- "stopPolling:"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringWithFormat:"
- "subdataWithRange:"
- "superclass"
- "tagID"
- "technology"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "transceive:error:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8^{__IOHIDEvent=}16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@16@24@32"
- "v44@0:8i16@\"NSString\"20i28i32B36B40"
- "v44@0:8i16@20i28i32B36B40"
- "v48@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40"
- "v48@0:8@16@24@32@40"
- "valueForKey:"
- "whitespaceAndNewlineCharacterSet"
- "whitespaceCharacterSet"
- "zone"
- "{timespec=\"tv_sec\"q\"tv_nsec\"q}"

```
