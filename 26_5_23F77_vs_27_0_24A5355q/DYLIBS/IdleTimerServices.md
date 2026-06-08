## IdleTimerServices

> `/System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0x4e2c
-  __TEXT.__auth_stubs: 0x390
+  __TEXT.__text: 0x49d0
   __TEXT.__objc_methlist: 0x714
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x33b
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__cstring: 0x34e
   __TEXT.__oslogstring: 0x57a
   __TEXT.__unwind_info: 0x210
-  __TEXT.__objc_classname: 0x1bf
-  __TEXT.__objc_methname: 0x12cb
-  __TEXT.__objc_methtype: 0x6ea
-  __TEXT.__objc_stubs: 0xe20
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0x1998
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x3c8
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A933F1D1-DC0E-3942-BE2E-C86F16D9DB24
-  Functions: 138
-  Symbols:   676
-  CStrings:  360
+  UUID: A89BB8B4-5CE8-354F-84BB-D2B1785D89E3
+  Functions: 134
+  Symbols:   670
+  CStrings:  83
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<BSInvalidatable>\""
- "@\"<ITIdleTimerStateRequestDelegate>\""
- "@\"<ITIdleTimerStateRequestHandling>\""
- "@\"<ITIdleTimerStateServerDelegate>\""
- "@\"<ITIdleTimerStateServiceDelegate>\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"BSServiceConnection\""
- "@\"BSServiceConnectionListener\""
- "@\"ITIdleTimerConfiguration\""
- "@\"ITIdleTimerStateModel\""
- "@\"ITIdleTimerStateServer\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@36@0:8i16@20^@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24^@32"
- "@44@0:8i16@20@28^@36"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@\"NSNumber\"16@\"NSString\"24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8Q16@\"NSString\"24"
- "B32@0:8Q16@24"
- "B40@0:8@\"ITIdleTimerConfiguration\"16@\"BSProcessHandle\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B44@0:8i16@\"BSProcessHandle\"20@\"ITIdleTimerConfiguration\"28@\"NSString\"36"
- "B44@0:8i16@20@28@36"
- "BSDescriptionProviding"
- "BSServiceConnectionListenerDelegate"
- "BSXPCSecureCoding"
- "ITIdleTimerAssertion"
- "ITIdleTimerClientInterface"
- "ITIdleTimerConfiguration"
- "ITIdleTimerServerInterface"
- "ITIdleTimerServiceProvider"
- "ITIdleTimerState"
- "ITIdleTimerStateClient"
- "ITIdleTimerStateModel"
- "ITIdleTimerStateRequestDelegate"
- "ITIdleTimerStateRequestHandling"
- "ITIdleTimerStateServer"
- "ITIdleTimerStateServerDelegate"
- "ITIdleTimerStateService"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ITIdleTimerStateServerDelegate>\",W,N,V_delegate"
- "T@\"<ITIdleTimerStateServiceDelegate>\",W,N,V_delegate"
- "T@\"ITIdleTimerConfiguration\",R,C,N,V_configuration"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,G_identifier,V_identifier"
- "T@\"NSString\",R,C,N,G_uniqueReason"
- "T@?,C,N,G_idleEventHandlerBlock,S_setIdleEventHandlerBlock:,V_idleEventHandlerBlock"
- "TB,N,V_disablesTimer"
- "TB,R,GisIdleTimerServiceAvailable"
- "TB,R,N"
- "TQ,N,G_idleEventMask,S_setIdleEventMask:,V_idleEventMask"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessLock"
- "_access_addIdleTimerConfiguration:forReason:error:"
- "_access_addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
- "_access_idleTimerAssertionsByConfigIdentifier"
- "_access_newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
- "_access_newIdleTimerAssertionWithConfiguration:forReason:error:"
- "_access_removeIdleTimerConfiguration:forReason:"
- "_access_serviceAvailability"
- "_addConnection:"
- "_addStateCaptureHandler"
- "_assertionReasonsByClientID"
- "_assertionsByReason"
- "_calloutDispatchQueue"
- "_calloutQueue"
- "_clientTargetsByConfigIdentifier"
- "_configuration"
- "_connection"
- "_connectionInterrupted"
- "_connectionListener"
- "_connections"
- "_copyWithNewIdentifier"
- "_delegate"
- "_disablesTimer"
- "_hasIdleTimerServicesEntitlementForProcess:missingEntitlementError:"
- "_identifier"
- "_identifierForClientProcess:"
- "_idleEventHandlerBlock"
- "_idleEventMask"
- "_init"
- "_initWithConfiguration:forReason:invalidationBlock:"
- "_initWithModel:"
- "_model"
- "_removeConnection:"
- "_requestHandler"
- "_server"
- "_setIdleEventHandlerBlock:"
- "_setIdleEventMask:"
- "_stateCaptureAssertion"
- "_uniqueReason"
- "_uniquedReason:"
- "acquireIdleTimerAssertionOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:"
- "acquireIdleTimerAssertionWithConfiguration:fromClient:forReason:"
- "activate"
- "addIdleTimerConfiguration:forReason:error:"
- "addIdleTimerConfiguration:fromProcess:forReason:"
- "addIdleTimerOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:"
- "addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
- "addIdleTimerServiceConfiguration:forReason:error:"
- "addIdleTimerServiceOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
- "addObject:"
- "allValues"
- "appendBool:withName:"
- "appendObject:withName:"
- "appendUnsignedInteger:withName:"
- "autorelease"
- "build"
- "builderWithObject:"
- "bundleIdentifier"
- "class"
- "clientConfiguration:handleIdleEvent:"
- "clientDidDisconnect:"
- "configurationToDisableIdleTimer"
- "configureConnection:"
- "conformsToProtocol:"
- "connectionWithEndpoint:"
- "copy"
- "copyWithZone:"
- "countByEnumeratingWithState:objects:count:"
- "currentContext"
- "currentHandler"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeStringForKey:"
- "decodeUInt64ForKey:"
- "delegate"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "dictionaryWithObjects:forKeys:count:"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeUInt64:forKey:"
- "encodeWithBSXPCCoder:"
- "endpointForMachName:service:instance:"
- "errorWithDomain:code:userInfo:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleIdleEvent:usingConfigurationWithIdentifier:"
- "hasEntitlement:"
- "hash"
- "idleEventHandlerBlock"
- "idleTimerServiceAvailable"
- "init"
- "initWithBSXPCCoder:"
- "initWithCalloutQueue:delegate:"
- "initWithConfiguration:"
- "initWithDelegate:"
- "initWithDispatchQueue:"
- "initWithDispatchQueue:delegate:"
- "initWithDomain:code:userInfo:"
- "initWithIdentifier:forReason:invalidationBlock:"
- "intValue"
- "interfaceWithServer:client:"
- "invalidate"
- "isEqual:"
- "isIdleTimerServiceAvailable"
- "isIdleTimerServiceAvailableWithError:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener:didReceiveConnection:withContext:"
- "listenerWithConfigurator:"
- "makeRequestHandlerWithDelegate:"
- "newAssertionToDisableIdleTimerForReason:"
- "newAssertionToDisableIdleTimerForReason:error:"
- "newAssertionToDisableIdleTimerOnBehalfOfSceneWithPID:forReason:error:"
- "newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
- "newIdleTimerAssertionWithConfiguration:forReason:"
- "newIdleTimerAssertionWithConfiguration:forReason:error:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "protocolForProtocol:"
- "release"
- "remoteProcess"
- "remoteTarget"
- "removeIdleTimerConfiguration:forReason:"
- "removeIdleTimerConfigurationFromProcess:forReason:"
- "removeIdleTimerServiceConfiguration:forReason:error:"
- "removeObject:"
- "removeObjectForKey:"
- "resendIdleTimerAssertions"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setDelegate:"
- "setDisablesTimer:"
- "setDomain:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setService:"
- "setServiceQuality:"
- "setTargetQueue:"
- "sharedInstance"
- "stringWithFormat:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "supportsBSXPCSecureCoding"
- "unsignedIntegerValue"
- "utility"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"BSProcessHandle\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@\"BSProcessHandle\"16@\"NSString\"24"
- "v32@0:8@\"ITIdleTimerConfiguration\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
- "v40@0:8@\"ITIdleTimerConfiguration\"16@\"NSString\"24^@32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24^@32"
- "v44@0:8i16@\"ITIdleTimerConfiguration\"20@\"NSString\"28^@36"
- "v44@0:8i16@20@28^@36"
- "v48@0:8@\"NSNumber\"16@\"ITIdleTimerConfiguration\"24@\"NSString\"32^@40"
- "v48@0:8@16@24@32^@40"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
