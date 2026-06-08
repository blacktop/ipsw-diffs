## HeartRateCoordinator

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator`

```diff

-31.2.0.0.0
-  __TEXT.__text: 0x4648
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x784
+38.0.0.0.0
+  __TEXT.__text: 0x46b0
+  __TEXT.__objc_methlist: 0x81c
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__oslogstring: 0x3f8
-  __TEXT.__cstring: 0x240
-  __TEXT.__unwind_info: 0x268
-  __TEXT.__objc_classname: 0x1ce
-  __TEXT.__objc_methname: 0x11b9
-  __TEXT.__objc_methtype: 0x417
-  __TEXT.__objc_stubs: 0x9a0
-  __DATA_CONST.__got: 0x78
+  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__oslogstring: 0x44f
+  __TEXT.__cstring: 0x25a
+  __TEXT.__unwind_info: 0x280
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e0
+  __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x10e8
+  __AUTH_CONST.__objc_const: 0x1190
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x3c0
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15EEEC2B-0779-3517-867A-65D7EB4DAAAE
-  Functions: 138
-  Symbols:   621
-  CStrings:  326
+  UUID: 6BF7E403-5B1D-3329-A1B1-E90076B675F4
+  Functions: 151
+  Symbols:   666
+  CStrings:  44
 
Symbols:
+ -[HRCHeartRateData deliveryMode]
+ -[HRCHeartRateData initWithHeartRate:confidence:confidenceLevel:arbitrationStatus:context:hrContext:timestamp:sampleUuid:sourceType:streamingThrottleStatus:deviceUuid:device:sensorLocation:flags:deliveryMode:machContinuousTimestamp:]
+ -[HRCHeartRateData machContinuousTimestamp]
+ -[HRCHeartRateData setTimestamp:]
+ -[HRCHeartRateRequestor handleMostRecentHighConfidenceHeartRate:]
+ -[HRCHeartRateRequestor handleMostRecentHighConfidenceHeartRate:].cold.1
+ -[HRCHeartRateRequestor mostRecentHighConfidenceHeartRateRequested]
+ -[HRCHeartRateRequestor setMostRecentHighConfidenceHeartRateRequested:]
+ -[HRCHeartRateRequestorXPCHelper handleMostRecentHighConfidenceHeartRate:]
+ -[HRCHeartRateRequestorXPCHelper requestMostRecentHighConfidenceHeartRate]
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table8
+ _OBJC_IVAR_$_HRCHeartRateData._deliveryMode
+ _OBJC_IVAR_$_HRCHeartRateData._machContinuousTimestamp
+ _OBJC_IVAR_$_HRCHeartRateRequestor._mostRecentHighConfidenceHeartRateRequested
+ ___41-[HRCHeartRateRequestorXPCHelper connect]_block_invoke.57
+ ___41-[HRCHeartRateRequestorXPCHelper connect]_block_invoke.58
+ ___65-[HRCHeartRateRequestor handleMostRecentHighConfidenceHeartRate:]_block_invoke
+ ___65-[HRCHeartRateRequestor handleMostRecentHighConfidenceHeartRate:]_block_invoke_2
+ ___82-[HRCHeartRateRequestor initWithDelegate:onQueue:connectionHelper:privacyMonitor:]_block_invoke_2
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$deliveryMode
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$handleMostRecentHighConfidenceHeartRate:
+ _objc_msgSend$initWithHeartRate:confidence:confidenceLevel:arbitrationStatus:context:hrContext:timestamp:sampleUuid:sourceType:streamingThrottleStatus:deviceUuid:device:sensorLocation:flags:deliveryMode:machContinuousTimestamp:
+ _objc_msgSend$mostRecentHighConfidenceHeartRateRequested
+ _objc_msgSend$requestMostRecentHighConfidenceHeartRate
+ _objc_msgSend$setMostRecentHighConfidenceHeartRateRequested:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table11
- GCC_except_table14
- GCC_except_table6
- GCC_except_table9
- ___41-[HRCHeartRateRequestorXPCHelper connect]_block_invoke.54
- ___41-[HRCHeartRateRequestorXPCHelper connect]_block_invoke.55
- _objc_msgSend$initWithHeartRate:confidence:confidenceLevel:arbitrationStatus:context:hrContext:timestamp:sampleUuid:sourceType:streamingThrottleStatus:deviceUuid:device:sensorLocation:flags:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "handling most recent high confidence heart rate in client process"
+ "received heart rate sample in client process with uuid : %{private}@, deliveryMode=0x%02x"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HRCBluetoothLESourceObserverDelegate>\""
- "@\"<HRCBluetoothLESourceObserverXPCHelperDelegate>\""
- "@\"<HRCHeartRateOutputDelegate>\""
- "@\"<HRCPrivacyToggleMonitorDelegate>\""
- "@\"<HRCXPCConnectionHelperDelegate>\""
- "@\"HRCBluetoothLESourceObserverXPCHelper\""
- "@\"HRCDevice\""
- "@\"HRCHeartRateRequestorXPCHelper\""
- "@\"HRCPrivacyToggleMonitor\""
- "@\"NSDate\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@104@0:8d16@24C32C36q40q48@56@64C72C76@80@88C96I100"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8Q16^@24"
- "C"
- "C16@0:8"
- "HRCBluetoothLESourceObserver"
- "HRCBluetoothLESourceObserverXPCHelper"
- "HRCBluetoothLESourceObserverXPCHelperDelegate"
- "HRCDevice"
- "HRCFrontEndBluetoothLESourceObserverClient"
- "HRCFrontEndBluetoothLESourceObserverService"
- "HRCFrontEndClient"
- "HRCFrontEndService"
- "HRCHeartRateData"
- "HRCHeartRateRequestor"
- "HRCHeartRateRequestorXPCHelper"
- "HRCPrivacyToggleMonitor"
- "HRCPrivacyToggleMonitorDelegate"
- "HRCXPCConnectionHelperDelegate"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<HRCBluetoothLESourceObserverDelegate>\",W,N,V_delegate"
- "T@\"<HRCBluetoothLESourceObserverXPCHelperDelegate>\",W,N,V_delegate"
- "T@\"<HRCHeartRateOutputDelegate>\",W,N,V_delegate"
- "T@\"<HRCPrivacyToggleMonitorDelegate>\",W,N,V_delegate"
- "T@\"<HRCXPCConnectionHelperDelegate>\",W,N,V_delegate"
- "T@\"HRCBluetoothLESourceObserverXPCHelper\",&,N,V_connectionHelper"
- "T@\"HRCDevice\",R,N,V_device"
- "T@\"HRCHeartRateRequestorXPCHelper\",&,N,V_connectionHelper"
- "T@\"HRCPrivacyToggleMonitor\",&,N,V_privacyToggleMonitor"
- "T@\"NSDate\",R,N,V_timestamp"
- "T@\"NSNumber\",R,N,V_confidence"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_primaryQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_UDIDeviceIdentifier"
- "T@\"NSString\",R,N,V_bluetoothIdentifier"
- "T@\"NSString\",R,N,V_firmwareVersion"
- "T@\"NSString\",R,N,V_hardwareVersion"
- "T@\"NSString\",R,N,V_localIdentifier"
- "T@\"NSString\",R,N,V_manufacturer"
- "T@\"NSString\",R,N,V_model"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_softwareVersion"
- "T@\"NSUUID\",R,N,V_deviceUuid"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"NSXPCConnection\",W,N,V_connection"
- "TB,N,V_connected"
- "TB,N,V_heartRatePrivacyToggleEnabled"
- "TB,N,V_opportunisticUpdatesEnabled"
- "TB,R"
- "TC,R,N,V_arbitrationStatus"
- "TC,R,N,V_confidenceLevel"
- "TC,R,N,V_sensorLocation"
- "TC,R,N,V_sourceType"
- "TC,R,N,V_streamingThrottleStatus"
- "TI,R,N,V_flags"
- "TQ,N,V_activityType"
- "TQ,N,V_requestedStreamingMode"
- "TQ,R"
- "Td,R,N,V_heartRate"
- "Tq,N,V_locationType"
- "Tq,R,N,V_context"
- "Tq,R,N,V_hrContext"
- "UDIDeviceIdentifier"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFNotificationCenter=}"
- "_UDIDeviceIdentifier"
- "_activityType"
- "_arbitrationStatus"
- "_bluetoothIdentifier"
- "_center"
- "_clientQueue"
- "_confidence"
- "_confidenceLevel"
- "_connected"
- "_connection"
- "_connectionHelper"
- "_context"
- "_delegate"
- "_delegateQueue"
- "_device"
- "_deviceUuid"
- "_firmwareVersion"
- "_flags"
- "_hardwareVersion"
- "_heartRate"
- "_heartRateFeatureEnabled:"
- "_heartRatePrivacyToggleEnabled"
- "_hrContext"
- "_localIdentifier"
- "_locationType"
- "_manufacturer"
- "_model"
- "_name"
- "_opportunisticUpdatesEnabled"
- "_primaryQueue"
- "_privacyToggleMonitor"
- "_requestedStreamingMode"
- "_sensorLocation"
- "_softwareVersion"
- "_sourceType"
- "_streamingThrottleStatus"
- "_timestamp"
- "_uuid"
- "activate"
- "activityType"
- "arbitrationStatus"
- "arrayWithObjects:count:"
- "autorelease"
- "bluetoothIdentifier"
- "class"
- "confidence"
- "confidenceLevel"
- "conformsToProtocol:"
- "connect"
- "connected"
- "connection"
- "connectionHelper"
- "context"
- "count"
- "d"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "decodeDoubleForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "description"
- "device"
- "deviceUuid"
- "disconnect"
- "doubleValue"
- "encodeDouble:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "exportedInterface"
- "firmwareVersion"
- "flags"
- "handleFilteredHeartRate:"
- "handleHeartRateData:"
- "handleOneSecondStreamingHeartRate:"
- "handleSourceListUpdate:"
- "handleUpdatedSourceList:"
- "hardwareVersion"
- "hash"
- "heartRate"
- "heartRateFeatureEnabled:"
- "heartRatePrivacyToggleEnabled"
- "hrContext"
- "init"
- "initWithCoder:"
- "initWithDelegate:onQueue:"
- "initWithDelegate:onQueue:connectionHelper:"
- "initWithDelegate:onQueue:connectionHelper:privacyMonitor:"
- "initWithDomain:code:userInfo:"
- "initWithHeartRate:confidence:confidenceLevel:arbitrationStatus:context:hrContext:timestamp:sampleUuid:sourceType:streamingThrottleStatus:deviceUuid:device:sensorLocation:flags:"
- "initWithMachServiceName:options:"
- "initWithName:manufacturer:model:hardwareVersion:firmwareVersion:softwareVersion:localIdentifier:UDIDeviceIdentifier:bluetoothIdentifier:"
- "interfaceWithProtocol:"
- "invalidate"
- "invalidateConnection"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "localIdentifier"
- "locationType"
- "manufacturer"
- "model"
- "name"
- "opportunisticUpdatesEnabled"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "primaryQueue"
- "privacyToggleMonitor"
- "processInfo"
- "processName"
- "q"
- "q16@0:8"
- "reassessServerConnection"
- "received heart rate sample in client process with uuid : %{private}@"
- "refreshRequiredWithCompletionHandler:"
- "release"
- "remoteObjectProxy"
- "requestOpportunisticUpdates:"
- "requestStreamingMode:"
- "requestStreamingMode:withError:"
- "requestedStreamingMode"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sensorLocation"
- "setActivityType:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnected:"
- "setConnection:"
- "setConnectionHelper:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHeartRatePrivacyToggleEnabled:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLocationType:"
- "setOpportunisticUpdatesEnabled:"
- "setPrimaryQueue:"
- "setPrivacyToggleMonitor:"
- "setRemoteObjectInterface:"
- "setRequestedStreamingMode:"
- "setUserWorkoutActivitySession:isIndoor:"
- "setUserWorkoutActivityType:locationType:"
- "setWithArray:"
- "setupWithDelegate:onQueue:"
- "softwareVersion"
- "sourceType"
- "startObservingWithDelegate:onQueue:"
- "streamingThrottleStatus"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "timestamp"
- "updateProcessName:"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"HRCHeartRateData\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\"QBQq>16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v32@0:8Q16q24"
- "zone"

```
