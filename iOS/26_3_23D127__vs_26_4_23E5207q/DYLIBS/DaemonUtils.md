## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0xa8a8
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x1320
-  __TEXT.__const: 0x168
+2005.100.174.0.0
+  __TEXT.__text: 0xb70c
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x1518
+  __TEXT.__const: 0x178
   __TEXT.__cstring: 0x6fd
   __TEXT.__oslogstring: 0xab6
-  __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x450
-  __TEXT.__objc_classname: 0x2bd
-  __TEXT.__objc_methname: 0x2ac0
-  __TEXT.__objc_methtype: 0x81b
-  __TEXT.__objc_stubs: 0x22c0
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x258
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__objc_classname: 0x2e4
+  __TEXT.__objc_methname: 0x2c67
+  __TEXT.__objc_methtype: 0x864
+  __TEXT.__objc_stubs: 0x23e0
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba8
+  __DATA_CONST.__objc_selrefs: 0xc10
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__objc_arraydata: 0x48
+  __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0x2e70
-  __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_const: 0x34b8
+  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x170
-  __DATA.__data: 0x360
+  __DATA.__objc_ivar: 0x188
+  __DATA.__data: 0x420
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x110

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C59FDA13-3148-3146-A702-26CBF4B87201
-  Functions: 399
-  Symbols:   1625
-  CStrings:  885
+  UUID: 57A42FB0-4DC5-36F0-932E-8D67B68E6117
+  Functions: 423
+  Symbols:   1714
+  CStrings:  912
 
Symbols:
+ -[DomainStateRequest clientInfo]
+ -[DomainStateRequest initWithOptions:client:contextID:originatorId:]
+ -[DomainStateRequest originatorId]
+ -[DomainStateRequest setClientInfo:]
+ -[EvaluationRequest callback]
+ -[EvaluationRequest clientInfo]
+ -[EvaluationRequest isEventPaused:]
+ -[EvaluationRequest originatorId]
+ -[EvaluationRequest pause:event:]
+ -[EvaluationRequest pausedEvents]
+ -[EvaluationRequest resetPausedEvents]
+ -[EvaluationRequest setCallback:]
+ -[EvaluationRequest setClientInfo:]
+ -[EvaluationRequest setOriginatorId:]
+ -[EvaluationRequest setPausedEvents:]
+ -[LAAnalyticsDTO _dtoResultFromLACResult:error:locationState:]
+ -[LAAnalyticsDTO _dtoResultFromLACResult:error:locationState:].cold.1
+ -[LAAnalyticsDTO _dtoResultFromLACResult:error:locationState:].cold.2
+ -[LAAnalyticsDTO _dtoResultFromLACResult:error:locationState:].cold.3
+ -[LAAnalyticsDTO _dtoResultFromLACResult:error:locationState:].cold.4
+ -[Request init]
+ -[StorageRequest clientInfo]
+ -[StorageRequest initWithStorageDomain:key:options:contextID:originatorId:connection:]
+ -[StorageRequest originatorId]
+ -[StorageRequest setClientInfo:]
+ _LACBiometryTypeFaceID
+ _LACEvaluationRequestPayloadKeySecureIntentRequested
+ _LACPolicyDeviceOwnerAuthentication
+ _LACPolicyLocationBasedDeviceOwnerAuthenticationWithBiometricRatchet
+ _LACPolicyOptionFallbackToNoAuthentication
+ _LACPolicyOptionMatchForUnlock
+ _LACPolicyOptionNotInteractive
+ _LACPolicyOptionUserId
+ _LACPolicyOslo
+ _LACPolicyOsloWithPIN
+ _LACPolicyStockholm
+ _LACResultPassedBiometry
+ _LACResultPassedPasscode
+ _OBJC_CLASS_$_LACClientInfoProvider
+ _OBJC_CLASS_$_LACPasscodeHelper
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_DomainStateRequest._clientInfo
+ _OBJC_IVAR_$_DomainStateRequest._originatorId
+ _OBJC_IVAR_$_EvaluationRequest._callback
+ _OBJC_IVAR_$_EvaluationRequest._clientInfo
+ _OBJC_IVAR_$_EvaluationRequest._originatorId
+ _OBJC_IVAR_$_EvaluationRequest._pausedEvents
+ _OBJC_IVAR_$_StorageRequest._clientInfo
+ _OBJC_IVAR_$_StorageRequest._originatorId
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_PROP_LIST_LACClientRequest
+ __OBJC_$_PROP_LIST_LACEvaluationAnalytics
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACClientRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACEvaluationAnalytics
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACClientRequest
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACEvaluationAnalytics
+ __OBJC_$_PROTOCOL_REFS_LACClientRequest
+ __OBJC_$_PROTOCOL_REFS_LACEvaluationAnalytics
+ __OBJC_CLASS_PROTOCOLS_$_LAAnalyticsEvaluation
+ __OBJC_LABEL_PROTOCOL_$_LACClientRequest
+ __OBJC_LABEL_PROTOCOL_$_LACEvaluationAnalytics
+ __OBJC_PROTOCOL_$_LACClientRequest
+ __OBJC_PROTOCOL_$_LACEvaluationAnalytics
+ ___block_literal_global.195
+ ___block_literal_global.38
+ ___block_literal_global.89
+ _objc_msgSend$_dtoResultFromLACResult:error:locationState:
+ _objc_msgSend$callback
+ _objc_msgSend$infoForXPCClient:evaluationOptions:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$originatorId
+ _objc_msgSend$pausedEvents
+ _objc_msgSend$setCallback:
+ _objc_msgSend$setClientInfo:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOriginatorId:
+ _objc_msgSend$setPausedEvents:
+ _objc_msgSend$updatePayload:
- -[DomainStateRequest initWithOptions:client:contextID:]
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:]
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.1
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.2
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.3
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.4
- -[StorageRequest acl]
- -[StorageRequest initWithStorageDomain:key:acl:options:contextID:connection:]
- _OBJC_CLASS_$_LAPasscodeHelper
- _OBJC_IVAR_$_EvaluationRequest._secureIntentRequested
- _OBJC_IVAR_$_StorageRequest._acl
- ___block_literal_global.103
- ___block_literal_global.201
- ___block_literal_global.50
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_dtoResultFromLAResult:error:locationState:
- _objc_msgSend$secureIntentRequested
- _objc_msgSend$setSecureIntentRequested:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "@\"<LACContextCallbackXPC>\""
+ "@\"LACClientInfo\""
+ "@\"LACClientInfo\"16@0:8"
+ "@\"NSMutableSet\""
+ "@48@0:8@16@24@32Q40"
+ "@64@0:8q16q24@32@40Q48@56"
+ "LACClientRequest"
+ "LACEvaluationAnalytics"
+ "T@\"<LACContextCallbackXPC>\",&,N,V_callback"
+ "T@\"<LACXPCClient>\",&,N,V_client"
+ "T@\"LACClientInfo\",&,N,V_clientInfo"
+ "T@\"LACClientInfo\",R,N"
+ "T@\"NSMutableSet\",&,N,V_pausedEvents"
+ "TB,N"
+ "TQ,N,V_originatorId"
+ "TQ,R,N"
+ "TQ,R,N,V_originatorId"
+ "_callback"
+ "_clientInfo"
+ "_dtoResultFromLACResult:error:locationState:"
+ "_originatorId"
+ "_pausedEvents"
+ "callback"
+ "infoForXPCClient:evaluationOptions:"
+ "initWithOptions:client:contextID:originatorId:"
+ "initWithStorageDomain:key:options:contextID:originatorId:connection:"
+ "isEventPaused:"
+ "numberWithBool:"
+ "originatorId"
+ "pause:event:"
+ "pausedEvents"
+ "resetPausedEvents"
+ "setCallback:"
+ "setClientInfo:"
+ "setObject:forKeyedSubscript:"
+ "setOriginatorId:"
+ "setPausedEvents:"
+ "v28@0:8B16q20"
- "@40@0:8@16@24@32"
- "@64@0:8q16q24@32@40@48@56"
- "T@\"<LACXPCClient>\",W,N"
- "T@\"NSData\",R,N,V_acl"
- "TB,N,V_secureIntentRequested"
- "_dtoResultFromLAResult:error:locationState:"
- "_secureIntentRequested"
- "initWithOptions:client:contextID:"
- "initWithStorageDomain:key:acl:options:contextID:connection:"
- "v24@0:8@\"<LACXPCClient>\"16"

```
