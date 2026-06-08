## HealthLEHeartRate

> `/System/Library/PrivateFrameworks/HealthLEHeartRate.framework/HealthLEHeartRate`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0x350c
-  __TEXT.__auth_stubs: 0x360
+7027.0.52.2.6
+  __TEXT.__text: 0x3048
   __TEXT.__objc_methlist: 0x574
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__cstring: 0x20f
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__cstring: 0x226
   __TEXT.__oslogstring: 0x643
-  __TEXT.__unwind_info: 0x1b0
-  __TEXT.__objc_classname: 0x16b
-  __TEXT.__objc_methname: 0xee7
-  __TEXT.__objc_methtype: 0x3c9
-  __TEXT.__objc_stubs: 0xa80
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_selrefs: 0x3f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0xc60
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2CB4517-C339-3EB0-B104-4EA293556FC7
-  Functions: 100
-  Symbols:   509
-  CStrings:  316
+  UUID: 997BFCD1-B27E-3876-982E-C3F04DE68188
+  Functions: 97
+  Symbols:   502
+  CStrings:  80
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _objc_retain_x24
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HLEBLESourceObserverDelegate>\""
- "@\"<HLEBLESourceServiceInfoDelegate>\""
- "@\"<HLEHeartRateCollectionObserverClientInterface>\""
- "@\"<HLEHeartRateCollectionObserverDelegate>\""
- "@\"<HLEHeartRateDelegate>\""
- "@\"HIDEventSystemClient\""
- "@\"HKDevice\""
- "@\"HLEBLESource\""
- "@\"HLEConnectionManager\""
- "@\"HLEHeartRateRequestor\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"NSXPCInterface\"16@0:8"
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
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
- "HLEBLESource:collectedDatum:forDevice:isManualConnection:"
- "HLEBLESource:connectedDevices:"
- "HLEBLESourceObserverDelegate"
- "HLEBLESourceServiceInfo"
- "HLEBLESourceServiceInfoDelegate"
- "HLECollectionObserverClient"
- "HLECollectionObserverListener"
- "HLEConnectionManager"
- "HLEHeartRateCollectionObserver"
- "HLEHeartRateCollectionObserverClientInterface"
- "HLEHeartRateCollectionObserverServerInterface"
- "HLEHeartRateRequestor"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<HLEBLESourceObserverDelegate>\",W,N,V_delegate"
- "T@\"<HLEBLESourceServiceInfoDelegate>\",W,N,V_delegate"
- "T@\"<HLEHeartRateCollectionObserverDelegate>\",W,N,V_delegate"
- "T@\"<HLEHeartRateDelegate>\",W,N,V_delegate"
- "T@\"HIDEventSystemClient\",&,N,V_client"
- "T@\"HKDevice\",R,N,V_device"
- "T@\"HLEConnectionManager\",R,N,V_connectionManager"
- "T@\"NSMutableDictionary\",&,V_services"
- "T@\"NSString\",&,N,V_processName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",W,N,V_connection"
- "T@\"NSXPCListener\",&,N,V_HLECollectionObserverListener"
- "T@?,C,N,V_configurationStateDidChange"
- "T@?,C,N,V_connectionStateDidChange"
- "TB,R,N,V_manualConnection"
- "TB,R,N,V_shouldCollectHeartRate"
- "TQ,R"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_HKXPCExportable"
- "_HLECollectionObserverListener"
- "_addClient:"
- "_bleSource"
- "_client"
- "_clientQueue"
- "_configurationStateDidChange"
- "_connection"
- "_connectionManager"
- "_connectionStateChange:"
- "_connectionStateDidChange"
- "_delegate"
- "_device"
- "_eventCollectedforClient:event:"
- "_getConnectedDevices"
- "_handleHeartRateEvent:serviceInfo:"
- "_heartRateCollectionNotifyToken"
- "_initialEventReceived"
- "_lock"
- "_lock_connectionEnabled"
- "_lock_connections"
- "_lock_devices"
- "_lock_heartRateState"
- "_manualConnection"
- "_newHLEBLESource"
- "_processName"
- "_queue"
- "_remoteObjectProxy"
- "_removeClient:"
- "_requestor"
- "_serviceListener"
- "_services"
- "_setupHIDClientHandlers"
- "_setupNotificationListener"
- "_setupServiceDidConnectOrDisconnect:"
- "_setupXPCConnection"
- "_shouldCollectHeartRate"
- "activate"
- "addObject:"
- "autorelease"
- "class"
- "client"
- "clientInterface"
- "client_didChangeShouldCollectHeartRate:"
- "configurationStateDidChange"
- "conformsToProtocol:"
- "connectedDevicesDidChange:"
- "connection"
- "connectionConfigured"
- "connectionInterrupted"
- "connectionInvalidated"
- "connectionManager"
- "connectionStateDidChange"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createListenerWithMachServiceName:"
- "currentConnectedDevices"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "device"
- "deviceFromService:"
- "dictionaryWithObjects:forKeys:count:"
- "didUpdateDeviceDetails"
- "doubleValueForField:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "exportedInterface"
- "getConnectionEnabled"
- "getDevice"
- "hash"
- "heartRateCollectionObserver:didChangeShouldCollectHeartRate:"
- "heartRateSampleWasCollected:device:"
- "hk_dateForMachAbsoluteTime:"
- "hk_instantaneousDateIntervalWithDate:"
- "init"
- "initWithDelegate:"
- "initWithDelegate:onQueue:"
- "initWithDelegate:service:"
- "initWithIdentifier:dateInterval:quantity:resumeContext:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithName:manufacturer:model:hardwareVersion:firmwareVersion:softwareVersion:localIdentifier:UDIDeviceIdentifier:"
- "initWithRequestor:"
- "initWithRequestor:remoteObjectProxy:"
- "initWithType:"
- "interfaceWithProtocol:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener:shouldAcceptNewConnection:"
- "manualConnection"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processIdentifier"
- "processInfo"
- "processName"
- "propertyForKey:"
- "quantityWithUnit:doubleValue:"
- "release"
- "remoteInterface"
- "remoteObjectProxy"
- "remote_setProcessName:"
- "removeObject:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "senderID"
- "serverInterface"
- "serviceID"
- "services"
- "setClient:"
- "setConfigurationStateDidChange:"
- "setConnection:"
- "setConnectionStateDidChange:"
- "setConnectionStateForAllClients:"
- "setDelegate:"
- "setDispatchQueue:"
- "setEventHandler:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHLECollectionObserverListener:"
- "setHeartRateState:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMatching:"
- "setObject:forKeyedSubscript:"
- "setProcessName:"
- "setRemoteObjectInterface:"
- "setRemovalHandler:"
- "setServiceNotificationHandler:"
- "setServices:"
- "shouldCollectHeartRate"
- "superclass"
- "timestamp"
- "type"
- "unitFromString:"
- "updateCollectionState:"
- "updateDeviceIfNeededForService:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@\"HLEBLESource\"16@\"NSSet\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"HLEBLESource\"16@\"HKQuantityDatum\"24@\"HKDevice\"32B40"
- "v44@0:8@16@24@32B40"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
