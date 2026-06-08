## LowPowerMode

> `/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode`

```diff

-1846.120.8.0.1
-  __TEXT.__text: 0x5e34
-  __TEXT.__auth_stubs: 0x380
+2015.0.0.0.1
+  __TEXT.__text: 0x5718
   __TEXT.__objc_methlist: 0x954
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__cstring: 0x3c5
+  __TEXT.__cstring: 0x3cd
   __TEXT.__oslogstring: 0x677
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x1ab
-  __TEXT.__objc_methname: 0xedc
-  __TEXT.__objc_methtype: 0x3ab
-  __TEXT.__objc_stubs: 0xa80
-  __DATA_CONST.__got: 0x80
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0xc38
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x44
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E9B480A-EFF1-34B4-9E07-7C61A3A8918C
-  Functions: 219
-  Symbols:   856
-  CStrings:  371
+  UUID: D6FA0B34-647A-3847-B159-B524A701876B
+  Functions: 214
+  Symbols:   852
+  CStrings:  115
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"PMPowerMitigationInfo\"24@0:8@\"NSString\"16"
- "@\"PMPowerMitigationSession\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16q24q32"
- "@48@0:8@16q24q32d40"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8q16@24"
- "B40@0:8q16@24@32"
- "C"
- "C16@0:8"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "PMPowerMitigationInfo"
- "PMPowerMitigationSession"
- "PMPowerMitigationsObservable"
- "PMPowerMitigationsServiceCallbackProtocol"
- "PMPowerMitigationsServiceProtocol"
- "Q16@0:8"
- "T#,R"
- "T@\"NSMutableDictionary\",&,V_observersByClientId"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callback_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSObject<OS_os_log>\",&,V_log"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_clientIdentifier"
- "T@\"NSString\",R,C,N,V_sessionSource"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"PMPowerMitigationSession\",&,V_currentMitigationSession"
- "T@,R,W,N"
- "T@?,C,N,V_callback"
- "TB,R"
- "TB,V_connectionInterrupted"
- "TB,V_connection_interrupted"
- "TC,N,V_current_state"
- "TQ,R"
- "Td,R,N,V_timeDuration"
- "Tq,R,N,V_engagementReason"
- "Tq,R,N,V_mitigationLevel"
- "Tq,R,N,V_systemWideMitigationLevel"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_PMCoreSmartPowerNap"
- "_PMCoreSmartPowerNapCallbackProtocol"
- "_PMCoreSmartPowerNapProtocol"
- "_PMLowPowerMode"
- "_PMLowPowerModeProtocol"
- "_PMSmartPowerNap"
- "_PMSmartPowerNapCallbackProtocol"
- "_PMSmartPowerNapProtocol"
- "_PMWeakProxy"
- "_callback"
- "_callback_queue"
- "_clientIdentifier"
- "_connection"
- "_connectionInterrupted"
- "_connection_interrupted"
- "_currentMitigationSession"
- "_current_state"
- "_engagementReason"
- "_identifier"
- "_log"
- "_mitigationLevel"
- "_observersByClientId"
- "_queue"
- "_sessionSource"
- "_systemWideMitigationLevel"
- "_target"
- "_timeDuration"
- "activate"
- "addObject:"
- "addObserver:forClientIdentifier:"
- "autorelease"
- "callback"
- "callback_queue"
- "class"
- "clientIdentifier"
- "configureConnectionInterruptionHandler"
- "configureConnectionInvalidationHandler"
- "configureConnectionReconnectionOnServiceRestart"
- "conformsToProtocol:"
- "connection"
- "connectionInterrupted"
- "connection_interrupted"
- "copyCurrentMitigationInfoForClientIdentifier:"
- "countByEnumeratingWithState:objects:count:"
- "currentMitigationSession"
- "current_state"
- "d"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "decodeDoubleForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictionary"
- "didChangeToMitigations:withSessionInfo:"
- "didUpdateToMitigation:fromMitigation:"
- "encodeDouble:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "forwardInvocation:"
- "getCurrentMitigationInfoForClientIdentifier:"
- "getPowerMode"
- "hash"
- "identifier"
- "init"
- "initConnectionToService"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithMitigationLevel:"
- "initWithMitigationLevel:clientIdentifier:"
- "initWithSource:reason:level:"
- "initWithSource:reason:level:duration:"
- "initWithTarget:"
- "interfaceWithProtocol:"
- "invalidate"
- "invoke"
- "isEqual:"
- "isKindOfClass:"
- "isLowPowerModeEnabled"
- "isMemberOfClass:"
- "isProxy"
- "isTimedSession"
- "log"
- "methodReturnType"
- "methodSignature"
- "methodSignatureForSelector:"
- "mitigationLevel"
- "newMitigationInfoForClientIdentifier:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observersByClientId"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "proxyWithTarget:"
- "q"
- "q16@0:8"
- "queue"
- "reRegister"
- "registerForMitigationUpdates"
- "registerForPowerMitigations"
- "registerWithCallback:callback:"
- "registerWithIdentifier:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeObject:"
- "removeObserver:forClientIdentifier:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "selector"
- "self"
- "set"
- "setCSPNIgnoreRemoteClient:"
- "setCSPNMotionAlarmStartThreshold:"
- "setCSPNMotionAlarmThreshold:"
- "setCSPNQueryDelta:"
- "setCSPNRequeryDelta:"
- "setCallback:"
- "setCallback_queue:"
- "setConnection:"
- "setConnectionInterrupted:"
- "setConnection_interrupted:"
- "setCurrentMitigationSession:"
- "setCurrent_state:"
- "setExportedInterface:"
- "setExportedObject:"
- "setIdentifier:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLog:"
- "setObject:forKeyedSubscript:"
- "setObserversByClientId:"
- "setPowerMode:fromSource:"
- "setPowerMode:fromSource:withCompletion:"
- "setPowerMode:fromSource:withParams:"
- "setPowerMode:fromSource:withParams:withCompletion:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setReturnValue:"
- "setSPNMotionAlarmStartThreshold:"
- "setSPNMotionAlarmThreshold:"
- "setSPNReentryCoolOffPeriod:"
- "setSPNReentryDelaySeconds:"
- "setSPNRequeryDelta:"
- "setState:"
- "setTarget:"
- "sharedInstance"
- "signatureWithObjCTypes:"
- "state"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "syncState"
- "syncStateWithHandler:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "target"
- "unregister"
- "unregisterWithIdentifier:"
- "updateState:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?C>16"
- "v32@0:8@\"<PMPowerMitigationsObserver>\"16@\"NSString\"24"
- "v32@0:8@\"PMPowerMitigationSession\"16@\"PMPowerMitigationSession\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8q16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "v48@0:8q16@\"NSString\"24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
- "v48@0:8q16@24@32@?40"
- "zone"

```
