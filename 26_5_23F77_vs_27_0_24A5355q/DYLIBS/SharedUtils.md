## SharedUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

```diff

-2005.120.18.0.0
-  __TEXT.__text: 0x4ca8
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x954
+2305.0.0.0.1
+  __TEXT.__text: 0x415c
+  __TEXT.__objc_methlist: 0x88c
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x3ec
-  __TEXT.__oslogstring: 0x318
+  __TEXT.__cstring: 0x2d6
+  __TEXT.__oslogstring: 0x2e8
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0x2da
-  __TEXT.__objc_methname: 0x131f
-  __TEXT.__objc_methtype: 0xb6a
-  __TEXT.__objc_stubs: 0xb60
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0xa8
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x620
+  __DATA_CONST.__objc_selrefs: 0x5e8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1c0
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x1108
-  __AUTH_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__got: 0x148
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__objc_const: 0xe70
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x7e8
-  __DATA.__bss: 0x68
-  __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x48
+  __DATA.__data: 0x788
+  __DATA.__bss: 0x58
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A5D5754-B69A-3823-BA46-FEAB036EE75A
-  Functions: 158
-  Symbols:   786
-  CStrings:  461
+  UUID: 4F22104D-FC27-356A-A4F7-D30D58524CB6
+  Functions: 138
+  Symbols:   701
+  CStrings:  82
 
Symbols:
+ _NSStringFromLACPasscodeType
+ ___block_literal_global.51
+ ___block_literal_global.77
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$operationNotSupportedError
+ _objc_msgSend$operationNotSupportedOnDeviceError:
+ _objc_msgSend$operationNotSupportedOnPlatformError:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- +[LAErrorHelper _errorNotSupportedAction:on:]
- +[LAErrorHelper _errorNotSupportedAction:on:].cold.1
- +[LAPasscodeHelperPasscodeStateRepository currentState]
- +[LAPasscodeHelperPasscodeStateRepository currentState].cold.1
- +[LAUtils isDaytona]
- +[LAUtils isSharedIPad]
- +[LAUtils isSharedIPad].cold.1
- +[LAUtils isSharedIPad].cold.2
- -[LAPasscodeHelper passcodeScreenStyleWithPolicy:options:darkInterface:]
- -[LAPasscodeHelper passcodeType]
- -[LAPasscodeHelperPasscodeStateManagedSettings _managedConfiguration]
- -[LAPasscodeHelperPasscodeStateManagedSettings isPasscodeSet]
- -[LAPasscodeHelperPasscodeStateManagedSettings passcodeType]
- -[LAPasscodeHelperPasscodeStateSimulator isPasscodeSet]
- -[LAPasscodeHelperPasscodeStateSimulator passcodeType]
- _LACLogSubsystem
- _MKBUserTypeDeviceMode
- _NSStringFromLAPasscodeType
- _OBJC_CLASS_$_LACManagedConfiguration
- _OBJC_CLASS_$_LAPasscodeHelperPasscodeStateManagedSettings
- _OBJC_CLASS_$_LAPasscodeHelperPasscodeStateRepository
- _OBJC_CLASS_$_LAPasscodeHelperPasscodeStateSimulator
- _OBJC_CLASS_$_NSNumberFormatter
- _OBJC_CLASS_$_NSProcessInfo
- _OBJC_METACLASS_$_LAPasscodeHelperPasscodeStateManagedSettings
- _OBJC_METACLASS_$_LAPasscodeHelperPasscodeStateRepository
- _OBJC_METACLASS_$_LAPasscodeHelperPasscodeStateSimulator
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- __OBJC_$_CLASS_METHODS_LAPasscodeHelperPasscodeStateRepository
- __OBJC_$_INSTANCE_METHODS_LAPasscodeHelperPasscodeStateManagedSettings
- __OBJC_$_INSTANCE_METHODS_LAPasscodeHelperPasscodeStateSimulator
- __OBJC_$_PROP_LIST_LAPasscodeHelperPasscodeStateManagedSettings
- __OBJC_$_PROP_LIST_LAPasscodeHelperPasscodeStateSimulator
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAPasscodeHelperPasscodeState
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAPasscodeHelperPasscodeState
- __OBJC_$_PROTOCOL_REFS_LAPasscodeHelperPasscodeState
- __OBJC_CLASS_PROTOCOLS_$_LAPasscodeHelperPasscodeStateManagedSettings
- __OBJC_CLASS_PROTOCOLS_$_LAPasscodeHelperPasscodeStateSimulator
- __OBJC_CLASS_RO_$_LAPasscodeHelperPasscodeStateManagedSettings
- __OBJC_CLASS_RO_$_LAPasscodeHelperPasscodeStateRepository
- __OBJC_CLASS_RO_$_LAPasscodeHelperPasscodeStateSimulator
- __OBJC_LABEL_PROTOCOL_$_LAPasscodeHelperPasscodeState
- __OBJC_METACLASS_RO_$_LAPasscodeHelperPasscodeStateManagedSettings
- __OBJC_METACLASS_RO_$_LAPasscodeHelperPasscodeStateRepository
- __OBJC_METACLASS_RO_$_LAPasscodeHelperPasscodeStateSimulator
- __OBJC_PROTOCOL_$_LAPasscodeHelperPasscodeState
- ___54-[LAPasscodeHelperPasscodeStateSimulator passcodeType]_block_invoke
- ___55+[LAPasscodeHelperPasscodeStateRepository currentState]_block_invoke
- ___block_literal_global.52
- ___block_literal_global.78
- __isSharedIPad
- _currentState.onceToken
- _currentState.sharedInstance
- _kMKBDeviceModeKey
- _kMKBDeviceModeSharedIPad
- _objc_msgSend$_errorNotSupportedAction:on:
- _objc_msgSend$_managedConfiguration
- _objc_msgSend$currentState
- _objc_msgSend$environment
- _objc_msgSend$errorPlatformDoesNotSupportAction:
- _objc_msgSend$isDaytona
- _objc_msgSend$isPasscodeSet
- _objc_msgSend$numberFromString:
- _objc_msgSend$processInfo
- _objc_opt_isKindOfClass
- _objc_release_x25
- _objc_retainAutoreleasedReturnValue
- _os_variant_allows_internal_security_policies
CStrings:
- "#16@0:8"
- "%@ is not available in this platform"
- "%@ is not supported on %@."
- ".cxx_destruct"
- "@\"<LACEvaluationRequest>\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSError\"24@0:8@\"NSError\"16"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16r*24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24@32"
- "@40@0:8q16q24@32"
- "@48@0:8q16q24@32@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16q24"
- "B40@0:8@16q24q32"
- "I16@0:8"
- "LA.simulator.passcodeType"
- "LAACMBiometricAttemptNotifier"
- "LAADMUser"
- "LAAssertionsProxy"
- "LAAssertionsXPC"
- "LACContextCallbackXPC"
- "LACContextExternalizingXPC"
- "LACDarwinNotificationCenterObserver"
- "LACRemoteContext"
- "LACRemoteUI"
- "LACRemoteUIHost"
- "LACUIMechanism"
- "LAContextClientEvaluationProt"
- "LAContextEventFeedbackProt"
- "LAContextPropertiesProt"
- "LAContextXPC"
- "LADFRDelegate"
- "LADFRXPC"
- "LADaemonXPC"
- "LADecriptionBuilder"
- "LAErrorOysterRedactor"
- "LAErrorRedacting"
- "LAErrorRedactor"
- "LAInternalProtocols"
- "LAPasscodeHelper"
- "LAPasscodeHelperPasscodeState"
- "LAPasscodeHelperPasscodeStateManagedSettings"
- "LAPasscodeHelperPasscodeStateRepository"
- "LAPasscodeHelperPasscodeStateSimulator"
- "LAPasscodeType unknown (%d)"
- "LAPasscodeTypeAlphanumeric"
- "LAPasscodeTypeNone"
- "LAPasscodeTypeNumericCustomDigits"
- "LAPasscodeTypeNumericFourDigits"
- "LAPasscodeTypeNumericSixDigits"
- "LAPrearmContextXPC"
- "LAScheduler"
- "LASerialSchedulerInternal"
- "LAUIDelegate"
- "LAUtils"
- "MKBUserTypeDeviceMode returned NULL: %{public}@"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<LACEvaluationRequest>\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,V_agentConnection"
- "TB,R,N"
- "TI,R,N"
- "TQ,R"
- "This call"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_agentConnection"
- "_components"
- "_connectToUIAgent"
- "_connection"
- "_defaults"
- "_errorNotSupportedAction:on:"
- "_managedConfiguration"
- "_minSDKVersion"
- "_object"
- "_pendingOperations"
- "_performPendingOperations"
- "_performPendingOperationsWithCompletion:"
- "_performingPendingOperations"
- "_queue"
- "_remoteObjectProxyWithErrorHandler:"
- "_resume"
- "_running"
- "_schedule:"
- "_setQueue:"
- "_workQueue"
- "_xpcQueue"
- "addEntriesFromDictionary:"
- "addObject:"
- "agentConnection"
- "allowTransferToProcess:receiverAuditTokenData:reply:"
- "appendBool:withName:"
- "appendInteger:withName:"
- "appendObject:withName:"
- "appendString:"
- "appendString:withName:"
- "authMethodWithReply:"
- "autorelease"
- "boolValue"
- "bootstrapSessionServiceType:serviceClientID:completionHandler:"
- "build"
- "checkHasPendingUIRequestsForRemoteUI:completion:"
- "class"
- "clearDFR:"
- "code"
- "conformsToProtocol:"
- "connectRemoteUI:requestID:reply:"
- "connectToContextWithUUID:callback:clientId:token:senderAuditTokenData:reply:"
- "connectToExistingContext:callback:clientId:flags:reply:"
- "containsObject:"
- "count"
- "createDefaultQueueWithIdentifier:concurrencyAttribute:"
- "createUserInitiatedSerialQueueWithIdentifier:"
- "credentialEncodingSeedWithReply:"
- "credentialOfType:reply:"
- "credentialsUUIDWithReply:"
- "currentState"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "disconnectRemoteUI"
- "dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:"
- "domain"
- "dropTouchIdAssertionWithReason:reply:"
- "dumpStatus"
- "dumpStatusWithCompletion:"
- "environment"
- "error:hasCode:"
- "error:hasCode:subcode:"
- "error:hasCodeFromArray:"
- "errorDeviceDoesNotSupportAction:"
- "errorNotSupported"
- "errorPlatformDoesNotSupportAction:"
- "errorWithCode:"
- "errorWithCode:message:"
- "errorWithCode:message:moreInfo:"
- "errorWithCode:message:suberror:"
- "errorWithCode:subcode:message:"
- "errorWithCode:subcode:message:suberror:"
- "errorWithCode:userInfo:"
- "errorWithDomain:code:userInfo:"
- "evaluateACL:operation:options:uiDelegate:reply:"
- "evaluatePolicy:options:uiDelegate:reply:"
- "event:params:reply:"
- "eventDFR:eventHints:"
- "externalizedContextWithReply:"
- "failAuthenticationWithError:"
- "failProcessedEvent:failureError:reply:"
- "firstObject"
- "getDomainStateWithOptions:reply:"
- "hasBridge"
- "hash"
- "iOS"
- "init"
- "initWithMachServiceName:options:"
- "initWithObject:"
- "initWithQueue:"
- "initWithXpcQueue:"
- "instanceId"
- "integerValue"
- "interfaceForXPCProtocol:"
- "interfaceWithInternalProtocol:"
- "interfaceWithProtocol:"
- "internalErrorWithMessage:"
- "internalErrorWithMessage:suberror:"
- "internalInfoWithReply:"
- "invalidate"
- "invalidateWithReply:"
- "invalidatedWithError:"
- "isApplePayPolicy:"
- "isAppleSilicon"
- "isConnected"
- "isCredentialSet:reply:"
- "isDaytona"
- "isEqual:"
- "isEqualToString:"
- "isGibraltar"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPasscodeSet"
- "isPasscodeSetForUser:error:"
- "isProxy"
- "isRunning"
- "isSecureBootCapable"
- "isSharedIPad"
- "length"
- "localizedStringForError:"
- "mechanismEvent:reply:"
- "mechanismEvent:value:reply:"
- "missingEntitlementError:"
- "mutableCopy"
- "notificationCenter:didReceiveNotification:"
- "notifyBiometricMatchOperationStartAttempted"
- "notifyEvent:options:reply:"
- "null"
- "numberFromString:"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "optionsForInternalOperation:reply:"
- "parameterErrorForMissingOrInvalidObject:name:"
- "parameterErrorWithMessage:"
- "passcodeScreenStyleWithPolicy:options:darkInterface:"
- "passcodeType"
- "pauseProcessedEvent:pause:reply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentDomainForName:"
- "prearmTouchIdWithReply:"
- "processInfo"
- "q16@0:8"
- "q36@0:8q16@24B32"
- "raise:format:"
- "raiseExceptionOnError:"
- "redactError:"
- "redactInternalError:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectAtIndex:"
- "request"
- "resetProcessedEvent:reply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retryProcessedEvent:reply:"
- "schedule:"
- "self"
- "serverPropertyForOption:reply:"
- "setAgentConnection:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setCredential:forProcessedEvent:credentialType:reply:"
- "setCredential:type:options:reply:"
- "setCredentialsUUID:reply:"
- "setDefaults:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMinSDKVersion:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:forInternalOperation:reply:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setServerPropertyForOption:value:reply:"
- "setShowingCoachingHint:event:reply:"
- "setWithArray:"
- "setWithObjects:"
- "sharedInstance"
- "silentInternalErrorWithMessage:"
- "standardUserDefaults"
- "storageError:hasCode:"
- "storageErrorWithCode:message:"
- "storageErrorWithCode:message:suberror:"
- "stringByAppendingString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "takeTouchIdAssertionWithReason:reply:"
- "this device"
- "tokenForTransferToUnknownProcess:"
- "transitionToController:internalInfo:completionHandler:"
- "uiEvent:options:"
- "uiFailureWithError:"
- "uiSuccessWithResult:"
- "unsafeResume"
- "unsafeSchedule:"
- "updateDFR:options:delegate:reply:"
- "userInfo"
- "v16@0:8"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<LAPrearmContextXPC>\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSUUID\"@\"NSError\">16"
- "v24@0:8@?<v@?@?<v@?>>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8{?=II}16"
- "v28@0:8B16@20"
- "v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24"
- "v32@0:8@\"<LACRemoteUI>\"16@?<v@?q>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16^{__CFString=}24"
- "v32@0:8q16@\"NSDictionary\"24"
- "v32@0:8q16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?>24"
- "v32@0:8q16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8q16@?<v@?@@\"NSError\">24"
- "v32@0:8q16@?<v@?B@\"NSError\">24"
- "v36@0:8@\"NSXPCListenerEndpoint\"16B24@?<v@?>28"
- "v36@0:8@16B24@?28"
- "v36@0:8B16q20@?28"
- "v36@0:8B16q20@?<v@?B@\"NSError\">28"
- "v36@0:8i16@\"NSData\"20@?<v@?B@\"NSError\">28"
- "v36@0:8i16@20@?28"
- "v36@0:8q16B24@?28"
- "v36@0:8q16B24@?<v@?B@\"NSError\">28"
- "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16q24@?32"
- "v40@0:8@16q24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8q16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@\"NSError\"24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "v40@0:8q16@24@?<v@?>32"
- "v40@0:8q16@24@?<v@?B@\"NSError\">32"
- "v48@0:8@\"NSData\"16q24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@\"NSData\"16q24q32@?<v@?B@\"NSError\">40"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24Q32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16q24@32@?40"
- "v48@0:8@16q24q32@?40"
- "v48@0:8q16@\"NSDictionary\"24@\"<LACContextUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8q16@\"NSDictionary\"24@\"<LADFRDelegate>\"32@?<v@?B@\"NSError\">40"
- "v48@0:8q16@24@32@?40"
- "v56@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32q40@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">48"
- "v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24Q32q40@?48"
- "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
- "v64@0:8@16@24Q32@40@48@?56"
- "verifyFileVaultUser:volumeUuid:options:reply:"
- "xctErrorWithMessage:suberror:"
- "zone"
- "{?=\"platform\"I\"version\"I}"

```
