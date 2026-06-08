## AccessoryiAP2Shim

> `/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0xcee8
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x778
-  __TEXT.__const: 0x640
-  __TEXT.__cstring: 0x1057
+1176.0.26.502.1
+  __TEXT.__text: 0xc0a8
+  __TEXT.__objc_methlist: 0x740
+  __TEXT.__const: 0x541
+  __TEXT.__cstring: 0x1039
   __TEXT.__oslogstring: 0x22e4
-  __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0x1b2b
-  __TEXT.__objc_methtype: 0x2a2
-  __TEXT.__objc_stubs: 0x1180
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x940
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__gcc_except_tab: 0x5c
+  __TEXT.__unwind_info: 0x308
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x928
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0xd10
+  __DATA_CONST.__got: 0x168
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x15e0
+  __AUTH_CONST.__objc_const: 0xc40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x80
-  __DATA.__bss: 0xd8
-  __DATA.__common: 0x8
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x68
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED91B5E3-6EAE-3520-B660-1D7007CF2EF8
-  Functions: 303
-  Symbols:   1520
-  CStrings:  860
+  UUID: 779A1AC7-F5BF-3D05-90E7-75270AEC305F
+  Functions: 306
+  Symbols:   1513
+  CStrings:  504
 
Symbols:
+ +[ACCiAP2ShimServer markClientAsInterestedInBleNotifications:].cold.4
+ +[ACCiAP2ShimServer markClientAsInterestedInBleNotifications:].cold.5
+ +[ACCiAP2ShimServer markClientAsInterestedInBleNotifications:].cold.6
+ -[ACCiAP2ShimServer _iterateAccessories:].cold.3
+ -[ACCiAP2ShimServer _takeClientAssertionsForAccessoryConnection].cold.1
+ GCC_except_table4
+ GCC_except_table46
+ ___33-[ACCiAP2ShimServer _startServer]_block_invoke.52
+ ___33-[ACCiAP2ShimServer _startServer]_block_invoke.52.cold.1
+ ___33-[ACCiAP2ShimServer _startServer]_block_invoke.52.cold.2
+ ____xpc_iap2d_handle_incoming_request_block_invoke.214
+ ____xpc_iap2d_handle_incoming_request_block_invoke.214.cold.1
+ ____xpc_iap2d_handle_incoming_request_block_invoke.214.cold.2
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.211
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- -[ACCiAP2ShimServerDelegateInfo .cxx_destruct]
- -[ACCiAP2ShimServerDelegateInfo dealloc]
- -[ACCiAP2ShimServerDelegateInfo delegate]
- -[ACCiAP2ShimServerDelegateInfo initWithDelegate:]
- GCC_except_table50
- GCC_except_table8
- _EAManagerAccessorySessions
- _EAProcessAssertionIdentifierAccessoryConnect
- _EAProcessAssertionIdentifierAccessoryDisconnect
- _OBJC_CLASS_$_ACCiAP2ShimServerDelegateInfo
- _OBJC_IVAR_$_ACCiAP2ShimServerDelegateInfo._delegate
- _OBJC_METACLASS_$_ACCiAP2ShimServerDelegateInfo
- _OUTLINED_FUNCTION_11
- __OBJC_$_INSTANCE_METHODS_ACCiAP2ShimServerDelegateInfo
- __OBJC_$_INSTANCE_VARIABLES_ACCiAP2ShimServerDelegateInfo
- __OBJC_$_PROP_LIST_ACCiAP2ShimServerDelegateInfo
- __OBJC_CLASS_RO_$_ACCiAP2ShimServerDelegateInfo
- __OBJC_METACLASS_RO_$_ACCiAP2ShimServerDelegateInfo
- ___33-[ACCiAP2ShimServer _startServer]_block_invoke.21
- ___33-[ACCiAP2ShimServer _startServer]_block_invoke.21.cold.1
- ___33-[ACCiAP2ShimServer _startServer]_block_invoke.21.cold.2
- ____xpc_iap2d_handle_incoming_request_block_invoke.183
- ____xpc_iap2d_handle_incoming_request_block_invoke.183.cold.1
- ____xpc_iap2d_handle_incoming_request_block_invoke.183.cold.2
- ___block_literal_global.139
- _iap2ServerPortName
- _kIap2dConnectionIDMask
- _kIap2dInternalConnectionIDMask
- _kIapdConnectionIDMask
- _kIapdInternalConnectionIDMask
- _kInvalidConnectionID
- _kInvalidConnectionIDMask
- _kUnknownConnectionIDMask
- _kXPCClientIDStr
- _kXPCCloseWasSuccessfulStr
- _kXPCEANotifyAppOfSessionCloseStr
- _kXPCEAProtocolIDStr
- _kXPCEAProtocolTransportConnectedState
- _kXPCEAProtocolTransportNotification
- _kXPCEAProtocolTransportRegistryID
- _kXPCEAProtocolTransportUpstreamRegistryID
- _kXPCEASessionIDStr
- _kXPCOpenWasSuccessfulStr
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "PearlIDCapability"
- "%@-%lu"
- ".cxx_destruct"
- "8olRm6C1xqr7AJGpLRnpSw"
- "@"
- "@\"<ACCiAP2ShimServerDelegate>\""
- "@\"NSArray\""
- "@\"NSLock\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@28@0:8I16@20"
- "@32@0:8@16@24"
- "@36@0:8@16@24I32"
- "@76@0:8I16{?=[8I]}20@52@60@68"
- "ACCUserDefaults"
- "ACCiAP2ShimAccessory"
- "ACCiAP2ShimServer"
- "ACCiAP2ShimServerClient"
- "ACCiAP2ShimServerDelegateInfo"
- "ACCiAP2ShimServerUnregisteredClient"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "EAManagerAccessorySessions"
- "I"
- "I16@0:8"
- "I84@0:8I16{?=[8I]}20I52@56@64B72@76"
- "T@\"<ACCiAP2ShimServerDelegate>\",R,V_delegate"
- "T@\"NSArray\",R,N,V_clientEAProtocols"
- "T@\"NSLock\",R,V_clientLock"
- "T@\"NSMutableDictionary\",&,N,V_accessoryViaConnectionIDList"
- "T@\"NSMutableDictionary\",&,N,V_accessoryViaKeyUIDList"
- "T@\"NSMutableDictionary\",&,N,V_delegateList"
- "T@\"NSMutableDictionary\",R,V_clients"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_iap2dhighPriorityRootQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_internalListenerQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_listQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_processAssertionQ"
- "T@\"NSObject<OS_dispatch_source>\",R,N,V_processAssertionTimer"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_listener"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_xpcConnection"
- "T@\"NSString\",&,V_firmwareVersion"
- "T@\"NSString\",&,V_hardwareVersion"
- "T@\"NSString\",&,V_manufacturer"
- "T@\"NSString\",&,V_model"
- "T@\"NSString\",&,V_name"
- "T@\"NSString\",&,V_serialNumber"
- "T@\"NSString\",R,N,V_bundleId"
- "T@\"NSString\",R,V_accessoryUID"
- "T@\"NSString\",R,V_keyAccessoryUID"
- "T@\"NSString\",R,V_keyConnectionID"
- "T@\"NSString\",R,V_keyTag"
- "T@,&,V_context"
- "TB,N,V_cameraSupportedByClient"
- "TB,N,V_clientRequiresAccReset"
- "TB,N,V_interestedInBLENotifications"
- "TB,N,V_locationSupportedByClient"
- "TB,R,N,V_entitlementForAllAccessories"
- "TB,R,N,V_isShuttingDown"
- "TB,R,N,V_supportsAccessibility"
- "TB,V_dontPublish"
- "TI,N,V_applicationState"
- "TI,N,V_clientID"
- "TI,R,N,V_capabilities"
- "TI,R,V_featureTypeMask"
- "TI,V_connectionID"
- "T^{SBSProcessAssertion=},R,N,V_processAssertion"
- "Ti,R,N,V_iapSessionRefCount"
- "Ti,R,N,V_processId"
- "Ti,R,V_iap2AvailableNotifyToken"
- "Tq,R,N,V_processAssertionStartTime"
- "T{?=[8I]},R,N,V_auditToken"
- "T{__serverFlags=b1b1b30},R,V_serverFlags"
- "^{SBSProcessAssertion=}"
- "^{SBSProcessAssertion=}16@0:8"
- "_accessoryUID"
- "_accessoryViaConnectionIDList"
- "_accessoryViaKeyUIDList"
- "_addAccessory:"
- "_addDelegate:"
- "_applicationInfoForBundleIDSync:"
- "_applicationState"
- "_attachAccessory:"
- "_auditToken"
- "_bundleId"
- "_cameraSupportedByClient"
- "_capabilities"
- "_clientEAProtocols"
- "_clientID"
- "_clientLock"
- "_clientRequiresAccReset"
- "_clients"
- "_connectionID"
- "_context"
- "_delegate"
- "_delegateList"
- "_detachAccessory:"
- "_dontPublish"
- "_entitlementForAllAccessories"
- "_featureTypeMask"
- "_findAccessoryForAccessoryUID:andKeyTag:"
- "_findAccessoryForConnectionID:"
- "_findAccessoryForConnectionID:andKeyTag:"
- "_firmwareVersion"
- "_getProcessId"
- "_hardwareVersion"
- "_iap2AvailableNotifyToken"
- "_iap2dhighPriorityRootQueue"
- "_iapSessionRefCount"
- "_interestedInBLENotifications"
- "_internalListenerQueue"
- "_isShuttingDown"
- "_iterateAccessories:"
- "_iterateDelegates:"
- "_keyAccessoryUID"
- "_keyConnectionID"
- "_keyTag"
- "_listQueue"
- "_listener"
- "_locationSupportedByClient"
- "_manufacturer"
- "_model"
- "_name"
- "_pollForDeathAfterPromptCompletes"
- "_processAssertion"
- "_processAssertionQ"
- "_processAssertionStartTime"
- "_processAssertionTimer"
- "_processId"
- "_removeAccessory:"
- "_removeDelegate:"
- "_resetServerState"
- "_serialNumber"
- "_serverFlags"
- "_startServer"
- "_stopServer"
- "_supportsAccessibility"
- "_takeClientAssertionsForAccessoryConnection"
- "_takeClientAssertionsForAccessoryDisconnection"
- "_xpcConnection"
- "accessoryInfoDict"
- "accessoryUID"
- "accessoryViaConnectionIDList"
- "accessoryViaKeyUIDList"
- "addAccessory:"
- "addClientWithCapabilities:auditToken:currentClientID:xpcConnection:eaProtocols:notifyOfAlreadyConnectedAccessories:andBundleId:"
- "addDelegate:"
- "addFeature:"
- "addObject:"
- "allKeys"
- "allValues"
- "applicationInfoForApplication:"
- "applicationState"
- "arrayForKey:"
- "arrayWithObjects:count:"
- "auditToken"
- "boolForKey:"
- "bundleId"
- "bytes"
- "cStringUsingEncoding:"
- "cameraSupportedByClient"
- "canSendConnectionEventForAccessory:"
- "capabilities"
- "caseInsensitiveCompare:"
- "clientEAProtocols"
- "clientID"
- "clientLock"
- "clientRequiresAccReset"
- "clients"
- "compare:"
- "componentsSeparatedByCharactersInSet:"
- "connectionID"
- "connectionIDObj"
- "containsObject:"
- "containsString:"
- "context"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentCalendar"
- "dataWithBytes:length:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dateFromComponents:"
- "dateWithTimeInterval:sinceDate:"
- "dealloc"
- "defaultCenter"
- "delegate"
- "delegateList"
- "description"
- "detachXPCConnection:"
- "dictionaryForKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dontPublish"
- "doubleForKey:"
- "duration"
- "entitlementForAllAccessories"
- "enumerateKeysAndObjectsUsingBlock:"
- "featureTypeMask"
- "findAccessoryForAccessoryUID:andKeyTag:"
- "findAccessoryForConnectionID:"
- "findAccessoryForConnectionID:andKeyTag:"
- "findClientWithID:"
- "findClientWithXPCConnection:"
- "firmwareVersion"
- "generateClientID"
- "getUID"
- "hardwareVersion"
- "hasEntitlementForAllAccessories"
- "i16@0:8"
- "iap2AvailableNotifyToken"
- "iap2dhighPriorityRootQueue"
- "iapSessionRefCount"
- "indexOfObjectPassingTest:"
- "init"
- "initWithBundleIDs:states:"
- "initWithBundleId:"
- "initWithCapabilities:auditToken:xpcConnection:eaProtocols:andBundleId:"
- "initWithDelegate:"
- "initWithStartDate:endDate:"
- "initWithSuiteName:"
- "initWithUID:keyTag:features:"
- "intValue"
- "integerForKey:"
- "integerValue"
- "interestedInBLENotifications"
- "internalListenerQueue"
- "isEqualToString:"
- "isShuttingDown"
- "iterateAccessoriesAsync:"
- "iterateAccessoriesSync:"
- "iterateDelegatesAsync:"
- "iterateDelegatesSync:"
- "keyAccessoryUID"
- "keyConnectionID"
- "keyTag"
- "length"
- "listQueue"
- "listener"
- "locationSupportedByClient"
- "lock"
- "manufacturer"
- "markClientAsInterestedInBleNotifications:"
- "model"
- "name"
- "notifyEAClient:ofAccessoryEvent:accessory:"
- "notifyEAClientsOfAccessoryConnection:"
- "notifyEAClientsOfAccessoryDisconnection:"
- "notifyEAClientsOfAccessoryEvent:accessory:"
- "notifyEAClientsOfAccessoryReconnection:"
- "notifyInterestedClientsOfACCBLEAccessoryEvent:withPayload:"
- "numberWithBool:"
- "numberWithLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "performSelectorOnMainThread:withObject:waitUntilDone:"
- "postNSDistributeNotificationType:notifyDict:"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "postNotifydNotificationType:"
- "processAssertion"
- "processAssertionQ"
- "processAssertionStartTime"
- "processAssertionTimer"
- "processDetachXPCConnection:"
- "processId"
- "processXPCMessage:connection:"
- "propertyListWithData:options:format:error:"
- "punctuationCharacterSet"
- "q"
- "q16@0:8"
- "raise:format:"
- "releaseProcessAssertion"
- "removeAccessory:"
- "removeAllClients"
- "removeAllObjects"
- "removeClientForXPCConnection:"
- "removeClientWithID:"
- "removeDelegate:"
- "removeFeature:"
- "removeObjectForKey:"
- "resetServerState"
- "sendToClient:notification:withPayload:"
- "sendToInterestedClientsACCBLENotification:withPayload:"
- "serialNumber"
- "serverFlags"
- "setAccessoryViaConnectionIDList:"
- "setAccessoryViaKeyUIDList:"
- "setApplicationState:"
- "setBool:forKey:"
- "setCameraSupportedByClient:"
- "setClientID:"
- "setClientRequiresAccReset:"
- "setConnectionID:"
- "setContext:"
- "setDay:"
- "setDelegateList:"
- "setDontPublish:"
- "setDouble:forKey:"
- "setFirmwareVersion:"
- "setHardwareVersion:"
- "setInteger:forKey:"
- "setInterestedInBLENotifications:"
- "setLocationSupportedByClient:"
- "setManufacturer:"
- "setModel:"
- "setMonth:"
- "setName:"
- "setObject:forKey:"
- "setSerialNumber:"
- "setYear:"
- "sharedDefaults"
- "sharedDefaultsIapd"
- "sharedDefaultsLogging"
- "sharedInstance"
- "startServer"
- "stopServer"
- "stringByTrimmingCharactersInSet:"
- "stringForClientID:"
- "stringForKey:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "supportsAccessibility"
- "takeProcessAssertion:"
- "timeIntervalSince1970"
- "tryProcessXPCMessage:connection:server:"
- "unlock"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@24"
- "v32@0:8r*16@24"
- "v40@0:8@16r*24@32"
- "valueForKey:"
- "whitespaceAndNewlineCharacterSet"
- "xpcConnection"
- "{?=\"val\"[8I]}"
- "{?=[8I]}16@0:8"
- "{__serverFlags=\"deathBecomesUs\"b1\"serverExiting\"b1\"reserved\"b30}"
- "{__serverFlags=b1b1b30}16@0:8"

```
