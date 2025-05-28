## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-1394.62.1.0.0
-  __TEXT.__text: 0xb424
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0xeec
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0xca8
-  __TEXT.__oslogstring: 0xa0e
-  __TEXT.__gcc_except_tab: 0x158
+1394.82.1.0.0
+  __TEXT.__text: 0xd9c0
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x10c4
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0xe2e
+  __TEXT.__oslogstring: 0xd84
+  __TEXT.__gcc_except_tab: 0x1a0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x44c
-  __TEXT.__objc_classname: 0x234
-  __TEXT.__objc_methname: 0x2ae6
-  __TEXT.__objc_methtype: 0x5bc
-  __TEXT.__objc_stubs: 0x21e0
+  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__objc_classname: 0x286
+  __TEXT.__objc_methname: 0x333c
+  __TEXT.__objc_methtype: 0x7af
+  __TEXT.__objc_stubs: 0x28c0
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x438
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__const: 0x460
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ef8
-  __DATA_CONST.__objc_selrefs: 0xb28
-  __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__cfstring: 0xcc0
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__objc_const: 0x8f8
-  __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_classrefs: 0x150
-  __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x144
-  __DATA.__data: 0x180
+  __DATA_CONST.__objc_const: 0x26a8
+  __DATA_CONST.__objc_selrefs: 0xd00
+  __DATA_CONST.__objc_arraydata: 0x60
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__objc_const: 0x940
+  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__auth_got: 0x368
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_protorefs: 0x8
+  __DATA.__objc_classrefs: 0x180
+  __DATA.__objc_superrefs: 0xa0
+  __DATA.__objc_ivar: 0x178
+  __DATA.__data: 0x240
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__bss: 0x128
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 387
-  Symbols:   1569
-  CStrings:  866
+  Functions: 444
+  Symbols:   1789
+  CStrings:  998
 
Symbols:
+ -[EvaluationRequest _updateDTOStatusWithCompletion:]
+ -[EvaluationRequest dtoAnalytics]
+ -[EvaluationRequest dtoEnvironment]
+ -[EvaluationRequest dtoRequestIdentifier]
+ -[EvaluationRequest setDtoEnvironment:]
+ -[EvaluationRequest setDtoRequestIdentifier:]
+ -[LAAnalytics allowsMultipleCollections]
+ -[LAAnalytics logLevel]
+ -[LAAnalytics setAllowsMultipleCollections:]
+ -[LAAnalyticsDTO .cxx_destruct]
+ -[LAAnalyticsDTO _checkStatusWithEnvironment:]
+ -[LAAnalyticsDTO _checkStatusWithReason:]
+ -[LAAnalyticsDTO _coolDownTimeInterval]
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:]
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.1
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.2
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.3
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.4
+ -[LAAnalyticsDTO _isLocationBasedPolicyEvaluation]
+ -[LAAnalyticsDTO _isRatchetArmingEvaluation]
+ -[LAAnalyticsDTO _isRatchetCollapsed]
+ -[LAAnalyticsDTO _monitoringInterval]
+ -[LAAnalyticsDTO _setupStatusMonitoring]
+ -[LAAnalyticsDTO _stateWithEnvironment:]
+ -[LAAnalyticsDTO _uid]
+ -[LAAnalyticsDTO buildPayload]
+ -[LAAnalyticsDTO collectIfNeeded]
+ -[LAAnalyticsDTO coolDownBucket]
+ -[LAAnalyticsDTO description]
+ -[LAAnalyticsDTO evaluationResult:error:]
+ -[LAAnalyticsDTO initForStatusMonitoringWithEnvironment:workQueue:]
+ -[LAAnalyticsDTO initWithEvaluationRequest:]
+ -[LAAnalyticsDTO initWithEvaluationRequest:].cold.1
+ -[LAAnalyticsDTO logLevel]
+ -[LAAnalyticsDTO pendingEvaluationController:updatedPendingEvaluation:]
+ -[LAAnalyticsDTO pendingEvaluationControllerDidStartTrackingPendingEvaluations:]
+ -[LAAnalyticsDTO pendingEvaluationControllerDidStopTrackingPendingEvaluations:]
+ -[LAAnalyticsDTO persistentStatusCheckTime]
+ -[LAAnalyticsDTO policyResult]
+ -[LAAnalyticsDTO ratchetResult]
+ -[LAAnalyticsDTO request]
+ -[LAAnalyticsDTO setPersistentStatusCheckTime:]
+ -[LAAnalyticsDTO shouldCollect]
+ -[LAAnalyticsDTO state]
+ GCC_except_table17
+ _LAEventFromBiometryType
+ _NSGlobalDomain
+ _NSStringFromProtocol
+ _OBJC_CLASS_$_LAAnalyticsDTO
+ _OBJC_CLASS_$_LAPasscodeHelper
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_EvaluationRequest._dtoAnalytics
+ _OBJC_IVAR_$_EvaluationRequest._dtoEnvironment
+ _OBJC_IVAR_$_EvaluationRequest._dtoRequestIdentifier
+ _OBJC_IVAR_$_LAAnalytics._allowsMultipleCollections
+ _OBJC_IVAR_$_LAAnalyticsDTO._coolOffStarted
+ _OBJC_IVAR_$_LAAnalyticsDTO._dtoService
+ _OBJC_IVAR_$_LAAnalyticsDTO._environment
+ _OBJC_IVAR_$_LAAnalyticsDTO._environmentProvider
+ _OBJC_IVAR_$_LAAnalyticsDTO._evaluationFinished
+ _OBJC_IVAR_$_LAAnalyticsDTO._evaluationSuccessful
+ _OBJC_IVAR_$_LAAnalyticsDTO._policyResult
+ _OBJC_IVAR_$_LAAnalyticsDTO._ratchetResult
+ _OBJC_IVAR_$_LAAnalyticsDTO._request
+ _OBJC_METACLASS_$_LAAnalyticsDTO
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_INSTANCE_METHODS_LAAnalyticsDTO
+ __OBJC_$_INSTANCE_VARIABLES_LAAnalyticsDTO
+ __OBJC_$_PROP_LIST_LAAnalyticsDTO
+ __OBJC_$_PROP_LIST_LACDTOService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOService
+ __OBJC_$_PROTOCOL_REFS_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_REFS_LACDTOService
+ __OBJC_CLASS_PROTOCOLS_$_LAAnalyticsDTO
+ __OBJC_CLASS_RO_$_LAAnalyticsDTO
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_LABEL_PROTOCOL_$_LACDTOService
+ __OBJC_METACLASS_RO_$_LAAnalyticsDTO
+ __OBJC_PROTOCOL_$_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_PROTOCOL_$_LACDTOService
+ __OBJC_PROTOCOL_REFERENCE_$_LACDTOService
+ ___37-[LAAnalyticsDTO _monitoringInterval]_block_invoke
+ ___40-[LAAnalyticsDTO _setupStatusMonitoring]_block_invoke
+ ___41-[LAAnalyticsDTO _checkStatusWithReason:]_block_invoke
+ ___41-[LAAnalyticsDTO _checkStatusWithReason:]_block_invoke.cold.1
+ ___67-[LAAnalyticsDTO initForStatusMonitoringWithEnvironment:workQueue:]_block_invoke
+ ___block_descriptor_40_e8_32w_e41_v24?0"<LACDTOEnvironment>"8"NSError"16lw32l8
+ ___block_literal_global.200
+ ___block_literal_global.54
+ _objc_msgSend$_checkStatusWithEnvironment:
+ _objc_msgSend$_checkStatusWithReason:
+ _objc_msgSend$_coolDownTimeInterval
+ _objc_msgSend$_dtoResultFromLAResult:error:inFamiliarLocation:
+ _objc_msgSend$_isLocationBasedPolicyEvaluation
+ _objc_msgSend$_isRatchetArmingEvaluation
+ _objc_msgSend$_monitoringInterval
+ _objc_msgSend$_setupStatusMonitoring
+ _objc_msgSend$_stateWithEnvironment:
+ _objc_msgSend$_uid
+ _objc_msgSend$_updateDTOStatusWithCompletion:
+ _objc_msgSend$acl
+ _objc_msgSend$addObserver:
+ _objc_msgSend$allowsMultipleCollections
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$coolDownBucket
+ _objc_msgSend$coolOffStarted
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$dtoEnvironment
+ _objc_msgSend$dtoRequestIdentifier
+ _objc_msgSend$environment
+ _objc_msgSend$error:hasCode:
+ _objc_msgSend$error:hasCode:subcode:
+ _objc_msgSend$error:hasCodeFromArray:
+ _objc_msgSend$evaluationUserId
+ _objc_msgSend$featureState
+ _objc_msgSend$fetchEnvironmentForPolicy:options:completion:
+ _objc_msgSend$inFamiliarLocation
+ _objc_msgSend$isAvailable
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isEnrolled:error:
+ _objc_msgSend$isLocationBasedPolicy:
+ _objc_msgSend$isPasscodeSetForUser:error:
+ _objc_msgSend$isSupported
+ _objc_msgSend$localizedStringFromDate:dateStyle:timeStyle:
+ _objc_msgSend$logLevel
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$options
+ _objc_msgSend$pendingPolicyEvaluationController
+ _objc_msgSend$persistentDomainForName:
+ _objc_msgSend$persistentStatusCheckTime
+ _objc_msgSend$policyResult
+ _objc_msgSend$processInfo
+ _objc_msgSend$ratchetResult
+ _objc_msgSend$ratchetState
+ _objc_msgSend$rawValue
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$serviceLocator
+ _objc_msgSend$serviceWithIdentifier:
+ _objc_msgSend$setAllowsMultipleCollections:
+ _objc_msgSend$setPersistentStatusCheckTime:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$state
+ _os_variant_has_internal_content
- ___NSArray0__struct
CStrings:
+ "\x04\x11"
+ "#\x14"
+ "%{public}@ is missing LACDTOService dependency"
+ "<LAAnalyticsDTO RatchetResult:%d, PolicyResult:%d, State:%d, CoolDownBucket:%d (coolOffStarted: %@)>"
+ "@\"<LACDTOEnvironment>\""
+ "@\"<LACDTOEnvironmentProviding>\""
+ "@\"<LACDTOEnvironmentProviding>\"16@0:8"
+ "@\"<LACDTOFeatureControlling>\"16@0:8"
+ "@\"<LACDTOPendingPolicyEvaluationController>\"16@0:8"
+ "@\"<LACDTOPolicyEvaluationController>\"16@0:8"
+ "@\"<LACDTORatchetStateProvider>\"16@0:8"
+ "@\"<LACDTOService>\""
+ "@\"<LACDTOServiceXPC>\"16@0:8"
+ "@\"LAAnalyticsDTO\""
+ "Both result and error were set by client %{public}@ for policy %d with options %{public}@ in DTO environment %{public}@: %{public}@, %{public}@"
+ "C"
+ "Checking status now (%{public}@)"
+ "CoolDownBucket"
+ "DTO parameter failure for client %{public}@ evaluating policy %d with options %{public}@ in DTO environment: %{public}@"
+ "Failed to acquire DTO environment"
+ "Failed to query the environment: %{public}@"
+ "LA.dto.AnalyticsStatusCheckInterval"
+ "LA.dto.statusCheckTime"
+ "LAAnalyticsDTO"
+ "LACDTOPendingPolicyEvaluationControllerObserver"
+ "LACDTOService"
+ "Neither result nor error were set by client %{public}@ for policy %d with options %{public}@ in DTO environment %{public}@"
+ "PolicyResult"
+ "RatchetResult"
+ "Received DTO environment: %@"
+ "Scheduling status check at %{public}@ (%.0f seconds from now)"
+ "State"
+ "T@\"<LACDTOEnvironment>\",&,N,V_dtoEnvironment"
+ "T@\"<LACDTOEnvironmentProviding>\",R,N"
+ "T@\"<LACDTOFeatureControlling>\",R,N"
+ "T@\"<LACDTOPendingPolicyEvaluationController>\",R,N"
+ "T@\"<LACDTOPolicyEvaluationController>\",R,N"
+ "T@\"<LACDTORatchetStateProvider>\",R,N"
+ "T@\"<LACDTOServiceXPC>\",R,N"
+ "T@\"LAAnalyticsDTO\",R,N,V_dtoAnalytics"
+ "T@\"NSDate\",R,N"
+ "T@\"NSString\",&,N,V_dtoRequestIdentifier"
+ "TB,N,V_allowsMultipleCollections"
+ "Tq,R,N,V_policyResult"
+ "Tq,R,N,V_ratchetResult"
+ "Unexpected fallback to no auth for client %{public}@ evaluating policy %d with options %{public}@ in DTO environment %{public}@. Result: %{public}@"
+ "Unexpected success for client %{public}@ evaluating policy %d with options %{public}@ in DTO environment %{public}@. Result: %{public}@"
+ "_allowsMultipleCollections"
+ "_checkStatusWithEnvironment:"
+ "_checkStatusWithReason:"
+ "_coolDownTimeInterval"
+ "_coolOffStarted"
+ "_dtoAnalytics"
+ "_dtoEnvironment"
+ "_dtoRequestIdentifier"
+ "_dtoResultFromLAResult:error:inFamiliarLocation:"
+ "_dtoService"
+ "_environment"
+ "_environmentProvider"
+ "_evaluationFinished"
+ "_evaluationSuccessful"
+ "_isLocationBasedPolicyEvaluation"
+ "_isRatchetArmingEvaluation"
+ "_isRatchetCollapsed"
+ "_monitoringInterval"
+ "_policyResult"
+ "_ratchetResult"
+ "_setupStatusMonitoring"
+ "_stateWithEnvironment:"
+ "_uid"
+ "_updateDTOStatusWithCompletion:"
+ "a"
+ "addObserver:"
+ "allowsMultipleCollections"
+ "com.apple.LocalAuthentication.DTO"
+ "coolDownBucket"
+ "coolOffStarted"
+ "dateByAddingTimeInterval:"
+ "doubleValue"
+ "dtoAnalytics"
+ "dtoEnvironment"
+ "dtoRequestIdentifier"
+ "environment"
+ "environmentProvider"
+ "error:hasCode:"
+ "error:hasCode:subcode:"
+ "error:hasCodeFromArray:"
+ "evaluationResult:error:"
+ "featureController"
+ "featureState"
+ "fetchEnvironmentForPolicy:options:completion:"
+ "inFamiliarLocation"
+ "initForStatusMonitoringWithEnvironment:workQueue:"
+ "isAvailable"
+ "isEnabled"
+ "isLocationBasedPolicy:"
+ "isPasscodeSetForUser:error:"
+ "isSupported"
+ "localizedStringFromDate:dateStyle:timeStyle:"
+ "logLevel"
+ "no scheduled check time"
+ "numberFromString:"
+ "numberWithDouble:"
+ "past scheduled check time: %@"
+ "pendingEvaluationController:updatedPendingEvaluation:"
+ "pendingEvaluationControllerDidStartTrackingPendingEvaluations:"
+ "pendingEvaluationControllerDidStopTrackingPendingEvaluations:"
+ "pendingPolicyEvaluationController"
+ "persistentDomainForName:"
+ "persistentStatusCheckTime"
+ "policyController"
+ "policyResult"
+ "processInfo"
+ "q24@0:8@16"
+ "q36@0:8@16@24B32"
+ "ratchetResult"
+ "ratchetState"
+ "ratchetStateProvider"
+ "rawValue"
+ "removeObserver:"
+ "scheduled check"
+ "serviceWithIdentifier:"
+ "setAllowsMultipleCollections:"
+ "setDtoEnvironment:"
+ "setDtoRequestIdentifier:"
+ "setPersistentStatusCheckTime:"
+ "standardUserDefaults"
+ "startServices"
+ "state"
+ "v24@0:8@\"<LACDTOPendingPolicyEvaluationController>\"16"
+ "v24@?0@\"<LACDTOEnvironment>\"8@\"NSError\"16"
+ "v32@0:8@\"<LACDTOPendingPolicyEvaluationController>\"16@\"<LACDTOPendingPolicyEvaluation>\"24"
+ "xpcController"
- "#\x11"

```
