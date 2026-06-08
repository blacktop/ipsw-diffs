## NearFieldAccessory

> `/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0xc488
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x908
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1135
-  __TEXT.__oslogstring: 0x6d2
-  __TEXT.__unwind_info: 0x2a8
-  __TEXT.__objc_classname: 0x16a
-  __TEXT.__objc_methname: 0xf2f
-  __TEXT.__objc_methtype: 0x70b
-  __TEXT.__objc_stubs: 0xe60
-  __DATA_CONST.__got: 0xd0
+370.33.1.0.0
+  __TEXT.__text: 0xb708
+  __TEXT.__objc_methlist: 0x924
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x112f
+  __TEXT.__oslogstring: 0x637
+  __TEXT.__unwind_info: 0x290
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b0
+  __DATA_CONST.__objc_selrefs: 0x5a8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1e8
-  __AUTH_CONST.__const: 0x140
+  __DATA_CONST.__got: 0xd8
+  __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x540
-  __AUTH_CONST.__objc_const: 0xe80
+  __AUTH_CONST.__objc_const: 0xe28
   __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x480

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24C79E97-DE61-39D3-9A52-7A0B1D772ACA
-  Functions: 195
-  Symbols:   98
-  CStrings:  560
+  UUID: 4A8560E6-A919-3892-B3C2-74D785A97C5C
+  Functions: 193
+  Symbols:   107
+  CStrings:  228
 
Symbols:
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_NFXPCServiceClient
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
- _OBJC_CLASS_$_NSXPCConnection
- _dispatch_get_global_queue
- _objc_retainAutoreleasedReturnValue
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "%s:%i %@"
+ "%s:%i Connection has refreshed"
+ "%s:%i Failed to update HW support: %@"
+ "%s:%i Invalid connection, retry..."
+ "%s:%i Unexpected connectionID (%lu vs %lu); dropping request"
+ "%{public}s:%i %@"
+ "%{public}s:%i Connection has refreshed"
+ "%{public}s:%i Failed to update HW support: %@"
+ "%{public}s:%i Invalid connection, retry..."
+ "%{public}s:%i Unexpected connectionID (%lu vs %lu); dropping request"
+ "-[NFAccessoryHardwareManager _connectIfNeeded:]"
+ "-[NFAccessoryHardwareManager didInterrupt:connectionID:]"
+ "-[NFAccessoryHardwareManager didInvalidate:]"
+ "-[NFAccessoryHardwareManager restartMultiTag]_block_invoke"
+ "-[NFAccessoryHardwareManager setClientName:onConnection:]_block_invoke"
+ "-[NFAccessoryHardwareManager updateHWSupport:error:]"
+ "-[NFAccessoryHardwareManager updateHWSupport:error:]_block_invoke"
+ "-[NFAccessoryReaderSession(InternalTest) sendMFGCommand:payload:error:]_block_invoke"
+ "Hardware is not supported"
+ "v24@?0@\"NSError\"8@\"NSData\"16"
- "#16@0:8"
- "%s:%i Accessory framwork - connecting XPC"
- "%s:%i Connecting to %s"
- "%s:%i Connection interrupted"
- "%s:%i Connection invalidated"
- "%s:%i Failed to update client name : %{public}@"
- "%s:%i XPC interrupted"
- "%s:%i XPC invalidated"
- "%s:%i failed to connect to daemon"
- "%{public}s:%i Accessory framwork - connecting XPC"
- "%{public}s:%i Connecting to %s"
- "%{public}s:%i Connection interrupted"
- "%{public}s:%i Connection invalidated"
- "%{public}s:%i Failed to update client name : %{public}@"
- "%{public}s:%i XPC interrupted"
- "%{public}s:%i XPC invalidated"
- "%{public}s:%i failed to connect to daemon"
- "-[NFAccessoryHardwareManager _connectIfNeeded]"
- "-[NFAccessoryHardwareManager _connectIfNeeded]_block_invoke"
- "-[NFAccessoryHardwareManager _connectIfNeeded]_block_invoke_2"
- "-[NFAccessoryHardwareManager didInterruptXPCConnection:]"
- "-[NFAccessoryHardwareManager didInvalidateXPCConnection:]"
- "-[NFAccessoryHardwareManager shutdownAndLeaveHWEnabled:]_block_invoke"
- "-[NFAccessoryHardwareManager updateHWSupport:]"
- "-[NFAccessoryHardwareManager updateHWSupport:]_block_invoke"
- ".cxx_destruct"
- "@\"<NFAccessoryReaderSessionDelegate>\""
- "@\"<NSSecureCoding>\"40@0:8@\"NSXPCConnection\"16@\"NSXPCCoder\"24@32"
- "@\"NFTimer\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableSet\""
- "@\"NSObject<NFSessionAccessoryInterface><NSXPCProxyCreating>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@?"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8C16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8I16^@20"
- "B32@0:8@16^@24"
- "B40@0:8^B16^B24^@32"
- "C"
- "C16@0:8"
- "I16@0:8"
- "I28@0:8B16^@20"
- "IDm"
- "InternalTest"
- "NFACTag"
- "NFAccessoryHardwareManager"
- "NFAccessoryReaderSession"
- "NFAccessorySession"
- "NFHardwareManagerAccessoryCallbacks"
- "NFHardwareManagerAccessoryInterface"
- "NFReaderSessionAccessoryCallbacks"
- "NFReaderSessionAccessoryInterface"
- "NFSessionAccessoryCallbackInterface"
- "NFSessionAccessoryInterface"
- "NF_asHexString"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSXPCConnectionDelegate"
- "Q"
- "Q16@0:8"
- "SystemCode"
- "T#,R"
- "T@\"<NFAccessoryReaderSessionDelegate>\",W"
- "T@\"NSData\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R"
- "TB,R,N"
- "TC,R,N"
- "TI,R,N"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,V_state"
- "Vv16@0:8"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@16"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?>16"
- "Vv24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSError\"@\"NSDictionary\">16"
- "Vv24@0:8@?<v@?B@\"NSError\">16"
- "Vv24@0:8@?<v@?BB@\"NSError\">16"
- "Vv24@0:8@?<v@?I>16"
- "Vv28@0:8B16@?20"
- "Vv28@0:8B16@?<v@?@\"NSError\">20"
- "Vv28@0:8C16@?20"
- "Vv28@0:8C16@?<v@?@\"NSError\">20"
- "Vv32@0:8@\"NFTagInternal\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "Vv32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSObject<NFReaderSessionAccessoryCallbacks>\"16@?<v@?@\"NSObject<NFReaderSessionAccessoryInterface>\"@\"NSError\">24"
- "Vv32@0:8@16@?24"
- "Vv32@0:8B16B20@?24"
- "Vv32@0:8B16B20@?<v@?@\"NSError\">24"
- "Vv32@0:8I16B20@?24"
- "Vv32@0:8I16B20@?<v@?@\"NSError\">24"
- "Vv32@0:8q16@?24"
- "Vv32@0:8q16@?<v@?@\"NSError\">24"
- "^{_NSZone=}16@0:8"
- "_allSystemCodes"
- "_appData"
- "_atqa"
- "_callbackQueue"
- "_cleanupSessions"
- "_connectIfNeeded"
- "_connection"
- "_delegate"
- "_description"
- "_didEndCallback"
- "_didEndSession"
- "_didStartCallback"
- "_didStartSession:"
- "_endProxySession"
- "_historicalBytes"
- "_hwSupport"
- "_isCallbackQueueSuspended"
- "_isFirstInQueue"
- "_ndefAvailability"
- "_ndefContainerSize"
- "_ndefMessageSize"
- "_pmm"
- "_proxy"
- "_refCount"
- "_sak"
- "_sessionTimeout"
- "_sessions"
- "_setQueue:"
- "_setSessionTimeLimit:"
- "_silentType"
- "_state"
- "_tagID"
- "_technology"
- "_type"
- "_uid"
- "addObject:"
- "applicationData"
- "applicationDataCoding"
- "asDictionary"
- "autorelease"
- "bytes"
- "callbackQueue"
- "checkNdefSupport:"
- "class"
- "clearMultiTagState:"
- "coder:decodeArrayOfClass:forKey:"
- "conformsToProtocol:"
- "connect"
- "connectTag:callback:"
- "connection:handleInvocation:isReply:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "decodeInt32ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "dictionaryWithObjects:forKeys:count:"
- "didDetectTags:"
- "didEnd"
- "didEndUnexpectedly"
- "didInterruptXPCConnection:"
- "didInvalidateXPCConnection:"
- "didStartSession:"
- "didStartSessionWithoutQueue:"
- "didTerminate:"
- "didTimeout"
- "disconnect"
- "enableContinuousWave:withFrequencySweep:"
- "enableContinuousWave:withFrequencySweep:callback:"
- "enableLPCD:"
- "enableLPCD:callback:"
- "enableMultiTag:"
- "enableMultiTag:callback:"
- "encodeInt32:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endSession:"
- "enumerateObjectsUsingBlock:"
- "getHwSupport:error:"
- "getInfo:"
- "getPowerCounters:"
- "hash"
- "init"
- "initSleepTimerWithCallback:queue:"
- "initWithCoder:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithFormat:"
- "initWithInternalTag:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "interfaceWithProtocol:"
- "invalidate"
- "isActive"
- "isEqual:"
- "isFirstInQueue"
- "isHWSupported:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSilent"
- "no xpc connection"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLong:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "processName"
- "proxy"
- "pupi"
- "pushSignedRF:callback:"
- "queueReaderSession:callback:"
- "readRawNdef:"
- "readerSession:didDetectTags:"
- "readerSessionDidEndUnexpectedly:"
- "readerSessionDidTimeout:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "replacementObjectForXPCConnection:encoder:object:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "selectedAID"
- "self"
- "sendAuthProtocolCommand:error:"
- "sessionDidEnd:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientName:"
- "setDelegate:"
- "setDidEndCallback:"
- "setDidStartCallback:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsFirstInQueue:"
- "setObject:forKeyedSubscript:"
- "setProxy:"
- "setRemoteObjectInterface:"
- "setTagDataRate:callback:"
- "sharedHardwareManager"
- "shutdownAndLeaveHWEnabled:"
- "shutdownAndLeaveHWEnabled:N"
- "shutdownAndLeaveHWEnabled:Y"
- "shutdownAndLeaveHWEnabled:callback:"
- "somethingDidHappen:"
- "startLpcdPolling:"
- "startPolling:"
- "startPollingForTechnology:lpcd:callback:"
- "startTimer:"
- "state"
- "stopTimer"
- "stringWithUTF8String:"
- "subdataWithRange:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "tagID"
- "transceive:callback:"
- "transceiveAccessoryCommand:callback:"
- "triggerDelayedWake:callback:"
- "updateHWSupport:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8d16"
- "v36@0:8@\"NSXPCConnection\"16@\"NSInvocation\"24B32"
- "v36@0:8@16@24B32"
- "zone"

```
