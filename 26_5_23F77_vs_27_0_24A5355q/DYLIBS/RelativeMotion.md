## RelativeMotion

> `/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion`

```diff

-333.0.0.0.0
-  __TEXT.__text: 0xa08c
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x824
+375.0.0.0.0
+  __TEXT.__text: 0x9c3c
+  __TEXT.__objc_methlist: 0x884
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xdfe
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__oslogstring: 0x1811
-  __TEXT.__unwind_info: 0x448
-  __TEXT.__objc_classname: 0x1c6
-  __TEXT.__objc_methname: 0x13c5
-  __TEXT.__objc_methtype: 0x636
-  __TEXT.__objc_stubs: 0xca0
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x3b8
+  __TEXT.__cstring: 0xe20
+  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__oslogstring: 0x18d2
+  __TEXT.__unwind_info: 0x408
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0x118
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x1890
+  __AUTH_CONST.__objc_const: 0x1860
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x3a0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DD938ECC-F9B8-3439-8D1B-4FD427260B7A
-  Functions: 348
-  Symbols:   1357
-  CStrings:  541
+  UUID: 07337E71-7E41-3FF9-B854-002408BC598F
+  Functions: 336
+  Symbols:   1338
+  CStrings:  220
 
Symbols:
+ -[RMConnectionClient connect].cold.1
+ -[RMConnectionClient handleDaemonStart].cold.1
+ -[RMConnectionClient stopStreamingInternal].cold.1
+ -[RMConnectionClient stopStreamingInternal].cold.2
+ -[RMRelativeMotionManager publishAudioListenerPoseInternal:withError:]
+ GCC_except_table0
+ GCC_except_table18
+ GCC_except_table27
+ GCC_except_table30
+ _OBJC_IVAR_$_RMRelativeMotionManager._audioListenerPosePublishedSlot
+ _OBJC_IVAR_$_RMRelativeMotionManager._audioListenerPoseReaderSlot
+ _OBJC_IVAR_$_RMRelativeMotionManager._audioListenerPoseWriterSlot
+ ___39-[RMConnectionClient handleDaemonStart]_block_invoke_2.cold.1
+ ___45-[RMConnectionClient endpointWasInvalidated:]_block_invoke.cold.1
+ ___53-[RMDummyDataManager startReceivingDummyDataUpdates:]_block_invoke.cold.2
+ ___block_descriptor_40_e8_32w_e33_v24?0"RMDummyData"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e58_v32?0"NSString"8"NSData"16?<v?"NSString""NSData">24lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_literal_global.117
+ ___block_literal_global.59
+ ___block_literal_global.60
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$connect
+ _objc_msgSend$initWithQueue:serviceName:messageHandler:
+ _objc_msgSend$requestStreamingWithMessage:data:callback:
+ _objc_msgSend$sendMessage:withData:reply:
+ _objc_msgSend$serviceName
+ _objc_msgSend$stopStreaming
+ _objc_msgSend$stopStreamingInternal
+ _objc_retainAutoreleaseReturnValue
- -[RMAudioListenerPoseManager isReceivingRelatveData]
- -[RMAudioListenerPoseManager setIsReceivingRelatveData:]
- -[RMConnectionClient endpointWasInterrupted:].cold.1
- -[RMConnectionClient endpointWasInterrupted:].cold.2
- -[RMConnectionClient endpointWasInvalidated:].cold.1
- -[RMConnectionClient endpointWasInvalidated:].cold.2
- -[RMConnectionClient endpointWasInvalidated:].cold.3
- -[RMConnectionClient requestStreamingWithMessage:data:callback:].cold.1
- -[RMDummyDataManager isReceivingRelatveData]
- -[RMDummyDataManager setIsReceivingRelatveData:]
- -[RMRelativeMotionManager currentAudioListenerPoseBufferIndex]
- -[RMRelativeMotionManager setCurrentAudioListenerPoseBufferIndex:]
- GCC_except_table14
- GCC_except_table24
- GCC_except_table43
- GCC_except_table45
- _OBJC_IVAR_$_RMAudioListenerPoseManager._isReceivingRelatveData
- _OBJC_IVAR_$_RMDummyDataManager._isReceivingRelatveData
- _OBJC_IVAR_$_RMRelativeMotionManager._audioListenerPoseBufferIndex
- _OBJC_IVAR_$_RMRelativeMotionManager._audioListenerPoseBufferLock
- _OBJC_IVAR_$_RMRelativeMotionManager._currentAudioListenerPoseBufferIndex
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- ___block_descriptor_40_e8_32s_e58_v32?0"NSString"8"NSData"16?<v?"NSString""NSData">24ls32l8
- ___block_descriptor_48_e8_32s40w_e33_v24?0"RMDummyData"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_literal_global.118
- ___block_literal_global.67
- ___block_literal_global.68
- _objc_msgSend$isReceivingRelatveData
- _objc_msgSend$setIsReceivingRelatveData:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/RelativeMotion/RMConnection/RMConnectionClient.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/RelativeMotion/RMConnection/RMConnectionEndpoint.m"
+ "Connection still invalid, next reconnection attempt will be in %{public}lu seconds"
+ "Reconnection timer fired after client was deallocated, ignoring"
+ "Stream XPC reply missing key \"%{public}s\""
+ "received dummy data with unexpected length: %{public}zu (expected %{public}zu)"
- "#16@0:8"
- ".cxx_destruct"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/RelativeMotion/Common/RMConnectionClient.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/RelativeMotion/Common/RMConnectionEndpoint.m"
- "@"
- "@\"<RMConnectionDataDelegate>\""
- "@\"<RMConnectionLifecycleDelegate>\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@\"RMAttitude\""
- "@\"RMAudioListenerPoseManager\""
- "@\"RMConnectionClient\""
- "@\"RMConnectionEndpoint\""
- "@\"RMDummyDataManager\""
- "@\"RMRelativeMotionManager\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@56@0:8@16d24d32d40d48"
- "@56@0:8{?=dddd}16d48"
- "@80@0:8{?=(?=[16f]Q)}16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"RMConnectionEndpoint\"16@?<v@?@\"NSData\">24"
- "B32@0:8@16@?24"
- "Connection still invalid, next reconnection attempt will be in %lu seconds"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "RMAttitude"
- "RMAudioListenerPoseManager"
- "RMConnectionClient"
- "RMConnectionClientCachedMessage"
- "RMConnectionDataDelegate"
- "RMConnectionEndpoint"
- "RMConnectionLifecycleDelegate"
- "RMConnectionStreamConsumingDelegate"
- "RMConnectionStreamProducingDelegate"
- "RMDummyData"
- "RMDummyDataManager"
- "RMInternalServiceClient"
- "RMLogItem"
- "RMLogItemInternal"
- "RMMediaSession"
- "RMMediaSessionOptions"
- "RMPose"
- "RMRelativeMotionManager"
- "T#,R"
- "T@\"NSDictionary\",&,N,V_audioListenerPoseOptions"
- "T@\"NSDictionary\",&,N,V_tempestOptions"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"RMAttitude\",R,N,V_attitude"
- "T@\"RMConnectionClient\",&,N,V_connectionClient"
- "T@\"RMConnectionClient\",&,N,V_spiClient"
- "T@\"RMRelativeMotionManager\",&,N,V_manager"
- "T@?,C,N,V_relativeDataCallback"
- "TB,N,V_isReceivingRelatveData"
- "TB,R"
- "TB,V_sessionStartedWithTracking"
- "TQ,N,V_predictionIntervalMicroseconds"
- "TQ,R"
- "Td,N,V_sessionStartTimestamp"
- "Td,R,N"
- "Td,R,N,V_consumedAuxTimestamp"
- "Td,R,N,V_machAbsTimestamp"
- "Td,R,N,V_presentationTimestamp"
- "Td,R,N,V_receivedAuxTimestamp"
- "Tq,N,V_clientMode"
- "T{?=(?=[16f]Q)},R,N,V_payload"
- "T{?=dddd},R,N,V_quaternion"
- "UTF8String"
- "Vv16@0:8"
- "[2@\"RMDummyData\"]"
- "[2q]"
- "[2{?=\"quaternion\"{?=\"x\"d\"y\"d\"z\"d\"w\"d}\"timestamp\"d\"error\"q\"consumedAuxTimestamp\"d\"receivedAuxTimestamp\"d\"machAbsTimestamp\"d\"presentationTimestamp\"d}]"
- "^{_NSZone=}16@0:8"
- "^{__CFNotificationCenter=}16@0:8"
- "_attitude"
- "_audioListenerPoseBuffer"
- "_audioListenerPoseBufferIndex"
- "_audioListenerPoseBufferLock"
- "_audioListenerPoseErrorBuffer"
- "_audioListenerPoseManager"
- "_audioListenerPoseOptions"
- "_clientMode"
- "_connectionClient"
- "_connectionDelegate"
- "_connectionTimer"
- "_connectionTimerDelay"
- "_consumedAuxTimestamp"
- "_currentAudioListenerPose:"
- "_currentAudioListenerPose:timestamp:"
- "_currentAudioListenerPoseBufferIndex"
- "_currentDummyDataBufferIndex"
- "_data"
- "_dataDelegate"
- "_defaults"
- "_dummyDataBuffer"
- "_dummyDataBufferIndex"
- "_dummyDataBufferLock"
- "_dummyDataManager"
- "_endpoint"
- "_initWithAttitude:consumedAuxTimestamp:receivedAuxTimestamp:machAbsTimestamp:presentationTimestamp:"
- "_initWithOptions:"
- "_initWithQuaternion:timestamp:"
- "_initWithTimestamp:"
- "_internalLogItem"
- "_isClientModeAvailable:"
- "_isReceivingRelatveData"
- "_machAbsTimestamp"
- "_manager"
- "_messageCache"
- "_messageHandler"
- "_messagingConnection"
- "_name"
- "_payload"
- "_poseCallbackInternal"
- "_predictionIntervalMicroseconds"
- "_presentationTimestamp"
- "_priorityBoostReplyMessage"
- "_quaternion"
- "_queue"
- "_receivedAuxTimestamp"
- "_relativeDataCallback"
- "_resetTrackingForAllClients"
- "_serviceName"
- "_sessionStartTimestamp"
- "_sessionStartedWithTracking"
- "_shouldReceiveAudioListenerPose"
- "_shouldReceiveDummyData"
- "_spiClient"
- "_start"
- "_stop"
- "_streamingCallback"
- "_streamingClientConnection"
- "_streamingClientListener"
- "_streamingDataCallback"
- "_streamingServerConnection"
- "_tempestOptions"
- "_valid"
- "_verboseLatencyAnalysisLogging"
- "addObject:"
- "allocWithZone:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "attitude"
- "audioListenerPoseOptions"
- "autorelease"
- "axHeadTrackingSettingChanged"
- "axNotificationCenter"
- "boolForKey:"
- "bytes"
- "class"
- "clientMode"
- "code"
- "conformsToProtocol:"
- "connectionClient"
- "consumedAuxTimestamp"
- "copyWithZone:"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "decodeBytesForKey:returnedLength:"
- "decodeDoubleForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultFaceToDevicePitchAngle"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "disconnectAllClientsWithReply:"
- "disconnectClient:withReply:"
- "dummyDataConfiguration"
- "encodeBytes:length:forKey:"
- "encodeDouble:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endpoint:didReceiveMessage:withData:replyBlock:"
- "endpoint:didReceiveStreamedData:"
- "endpoint:didReceiveStreamingRequest:withData:"
- "endpoint:shouldStartStreamingDataToReceiver:"
- "endpointShouldStopStreamingData:"
- "endpointWasInterrupted:"
- "endpointWasInvalidated:"
- "errorWithDomain:code:userInfo:"
- "fTimestamp"
- "getCurrentAudioListenerPose:timestamp:"
- "getCurrentAudioListenerPoseWithError:"
- "getCurrentDummyData"
- "getNumClientsWithReply:"
- "handleSpiIncomingMessage:data:replyBlock:"
- "hash"
- "init"
- "initWithBytes:length:"
- "initWithCoder:"
- "initWithDomain:code:userInfo:"
- "initWithPayload:"
- "initWithQueue:"
- "initWithSuiteName:"
- "initWithTimestamp:"
- "integerValue"
- "invalidate"
- "isAXHeadTrackingSettingEnabled"
- "isAudioListenerPoseAvailable"
- "isAvailable"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isReceivingRelatveData"
- "length"
- "listClientsWithReply:"
- "machAbsTimestamp"
- "manager"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "parseSpiErrorReply:forMessage:"
- "payload"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "predictionIntervalMicroseconds"
- "presentationTimestamp"
- "q"
- "q16@0:8"
- "q24@0:8^@16"
- "q32@0:8^{?=dddd}16^d24"
- "quaternion"
- "queue"
- "receivedAuxTimestamp"
- "relativeDataCallback"
- "release"
- "removeAllObjects"
- "removeObjectAtIndex:"
- "resetAudioListenerPoseTrackingForAllClients"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sessionStartTimestamp"
- "sessionStartedWithTracking"
- "setAudioListenerPoseOptions:"
- "setClientMode:"
- "setConnectionClient:"
- "setIsReceivingRelatveData:"
- "setManager:"
- "setObject:forKeyedSubscript:"
- "setPredictionIntervalMicroseconds:"
- "setQueue:"
- "setRelativeDataCallback:"
- "setSessionStartTimestamp:"
- "setSessionStartedWithTracking:"
- "setSpiClient:"
- "setTempestOptions:"
- "setWithObject:"
- "setWithObjects:"
- "spiClient"
- "startMonitoringAXHeadTrackingSetting"
- "startReceivingAudioListenerPose"
- "startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallback:"
- "startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:"
- "startReceivingDummyData"
- "startReceivingDummyDataUpdates:"
- "stopMonitoringAXHeadTrackingSetting"
- "stopReceivingAudioListenerPose"
- "stopReceivingAudioListenerPoseUpdates"
- "stopReceivingDummyData"
- "stopReceivingDummyDataUpdates"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsSecureCoding"
- "tempestOptions"
- "timestamp"
- "unarchivedObjectOfClass:fromData:error:"
- "unarchivedObjectOfClasses:fromData:error:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"RMConnectionEndpoint\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8B16@?20"
- "v32@0:8@\"RMConnectionEndpoint\"16@\"NSData\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"RMConnectionEndpoint\"16@\"NSString\"24@\"NSData\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"RMConnectionEndpoint\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSString\"@\"NSData\">40"
- "v48@0:8@16@24@32@?40"
- "zone"
- "{?=\"\"(?=\"data\"[16f]\"abstime\"Q)}"
- "{?=\"x\"d\"y\"d\"z\"d\"w\"d}"
- "{?=(?=[16f]Q)}16@0:8"
- "{?=dddd}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
