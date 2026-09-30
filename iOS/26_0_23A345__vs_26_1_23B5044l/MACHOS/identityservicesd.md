## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1968.100.1.2.1
-  __TEXT.__text: 0x924ef4
-  __TEXT.__auth_stubs: 0x5a50
-  __TEXT.__objc_stubs: 0x46020
-  __TEXT.__objc_methlist: 0x29274
-  __TEXT.__const: 0x638d0
-  __TEXT.__gcc_except_tab: 0x29c98
-  __TEXT.__objc_methname: 0x725e9
-  __TEXT.__cstring: 0x59127
-  __TEXT.__oslogstring: 0x7a3bb
-  __TEXT.__objc_classname: 0x43a3
-  __TEXT.__objc_methtype: 0x12303
+1968.200.31.2.1
+  __TEXT.__text: 0x927f38
+  __TEXT.__auth_stubs: 0x5a70
+  __TEXT.__objc_stubs: 0x46220
+  __TEXT.__objc_methlist: 0x2936c
+  __TEXT.__const: 0x63910
+  __TEXT.__gcc_except_tab: 0x29c80
+  __TEXT.__objc_methname: 0x72985
+  __TEXT.__cstring: 0x593a7
+  __TEXT.__oslogstring: 0x7a82b
+  __TEXT.__objc_classname: 0x43a8
+  __TEXT.__objc_methtype: 0x1232c
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__swift5_typeref: 0x5c90
+  __TEXT.__swift5_typeref: 0x5db8
   __TEXT.__swift5_capture: 0x12f8
   __TEXT.__constg_swiftt: 0x50a0
   __TEXT.__swift5_reflstr: 0x4ef4

   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_assocty: 0xfa8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x121b8
-  __TEXT.__eh_frame: 0x9934
-  __DATA_CONST.__auth_got: 0x2d38
-  __DATA_CONST.__got: 0x3820
-  __DATA_CONST.__auth_ptr: 0x770
-  __DATA_CONST.__const: 0x2dc68
-  __DATA_CONST.__cfstring: 0x34560
+  __TEXT.__unwind_info: 0x12210
+  __TEXT.__eh_frame: 0x99d4
+  __DATA_CONST.__auth_got: 0x2d48
+  __DATA_CONST.__got: 0x3860
+  __DATA_CONST.__auth_ptr: 0x780
+  __DATA_CONST.__const: 0x2dca8
+  __DATA_CONST.__cfstring: 0x34760
   __DATA_CONST.__objc_classlist: 0x1110
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x750
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0xb90
-  __DATA_CONST.__objc_intobj: 0x1aa0
-  __DATA_CONST.__objc_arraydata: 0x5a0
+  __DATA_CONST.__objc_intobj: 0x1b18
+  __DATA_CONST.__objc_arraydata: 0x5b0
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x479c0
-  __DATA.__objc_selrefs: 0x15b68
-  __DATA.__objc_ivar: 0x3278
+  __DATA.__objc_const: 0x47b08
+  __DATA.__objc_selrefs: 0x15c10
+  __DATA.__objc_ivar: 0x3294
   __DATA.__objc_data: 0xd260
-  __DATA.__data: 0xea60
+  __DATA.__data: 0xead0
   __DATA.__bss: 0x16de8
   __DATA.__common: 0xf18
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 16B16CEE-DA29-3091-ADA0-D88F0DCB3EDA
-  Functions: 25132
-  Symbols:   2736
-  CStrings:  41282
+  UUID: 65D2060E-5CF4-39DE-B33B-71C719C30272
+  Functions: 25165
+  Symbols:   2739
+  CStrings:  41367
 
Symbols:
+ _IDSGlobalLinkOptionAllowExpensiveQualityMetrics
+ _IDSMessageContextQueueOneIdentifierKey
+ _IDSRegistrationPropertySupportsAskToResponseUI
CStrings:
+ "%@[%@][%@]"
+ "23:17:22"
+ "Attempting to go offgrid, resetting offgrid timer"
+ "B16@?0@\"IDSPhoneSubscription\"8"
+ "B56@0:8@\"IDSURI\"16@\"IDSURI\"24@\"NSString\"32@\"NSDate\"40^Q48"
+ "B56@0:8@16@24@32@40^Q48"
+ "CKVOptionalEnforcementMetrics"
+ "Client valid through date: %@"
+ "Client's valid through date was too big, default time instead. { timeInSeconds: %@, newValidThroughDate: %@ }"
+ "Dropping message %@"
+ "Enforcing incoming push constraint for %@ Service %@ ConstraintType %u AllowedCommandGroups %u IncomingCommand %@"
+ "IDSDSession initWithAccount: allowExpensiveQualityMetrics: %@ (for service: %@)"
+ "IDSKTEnforcementEnabled"
+ "IDSKTEnforcementMetrics"
+ "IDSSessionEndedReasonClientChannelCacheFull"
+ "IDSSessionEndedReasonNoSessionState"
+ "KT enforcement conditional, still allowing. { service: %@ }"
+ "KT enforcement success. { service: %@ }"
+ "KT metrics mode. { service: %@ }"
+ "KT opt out, allowing. { service: %@ }"
+ "KT pending resolutions, allowing. { service: %@ }"
+ "KT rejected with failure: %@. { service: %@ }"
+ "KTMessageEnforcementPedantic"
+ "Phone number validation mode overridde to unsupported legacy mode attempted -- rejecting { modeFromDefaults: %ld }"
+ "Rate limit cleared"
+ "Rate limit reached for %@"
+ "Recipient endpoint is opted into KT but not supporting enforcement, send with warning { service: %{public}@, uri: %{public}@, token: %{public}@ }: %@"
+ "Recipient endpoint is opted into KT, supporting metrics, will fall back to warning { service: %{public}@, uri: %{public}@, token: %{public}@ }: %@"
+ "Recipient endpoint not resolved transparency status, allowing due to feature flag { service: %{public}@, uri: %{public}@, token: %{public}@, transparency: %{public}@ }"
+ "Recipient endpoint not resolved transparency status, will fail { service: %{public}@, uri: %{public}@, token: %{public}@, transparency: %{public}@ }"
+ "Requesting publish for status : %ld"
+ "Sep 16 2025"
+ "Status payload is invalid"
+ "TB,N,V_isRunning"
+ "TB,N,V_pedanticEnforcementFailure"
+ "TB,V_messageEnforcementPedantic"
+ "TB,V_supportConditionalEnforcement"
+ "There is already a request in progress"
+ "Tq,N,V_currentOffGridModeBeingPublished"
+ "_allowExpensiveQualityMetrics"
+ "_currentOffGridModeBeingPublished"
+ "_fetchKTDataSignatureForServiceTypes:publicIdentityData:registerID:keyStore:withCompletion:"
+ "_isRunning"
+ "_messageEnforcementPedantic"
+ "_pedanticEnforcementFailure"
+ "_rateLimitCount"
+ "_rateLimitTime"
+ "_stringFromQueryReasonExtensionSet:"
+ "_supportConditionalEnforcement"
+ "allowExpensiveQualityMetrics"
+ "clientDatasForRegistrations:registerID:keyStore:keyTransparencyVerifier:"
+ "currentOffGridModeBeingPublished"
+ "defaultEndpointValidThroughTimeInterval"
+ "fetchKTSignatureDataForServiceTypes:publicIdentityData:registerID:applicationKeyManager:withCompletion:"
+ "fetchKTSignatureDataForServiceTypes:publicIdentityData:registerID:withCompletion:"
+ "hasPeerTokensForURI:fromURI:service:validThrough:outReason:"
+ "ids-endpoint-vt-time-interval"
+ "invalidPublishStatusPayloadError"
+ "isRunning"
+ "messageEnforcementPedantic"
+ "payload provision"
+ "pedanticEnforcementFailure"
+ "prepareSessionInfoForGlobalLink:"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "rateLimitErrorForItem:"
+ "requestInProgressError"
+ "resetRateLimit"
+ "setCurrentOffGridModeBeingPublished:"
+ "setIsRunning:"
+ "setMessageEnforcementPedantic:"
+ "setPedanticEnforcementFailure:"
+ "setSupportConditionalEnforcement:"
+ "setTraceUUID:"
+ "status publish"
+ "status-rate-limit-count"
+ "status-rate-limit-time"
+ "statusPayloadForOffGridMode:"
+ "supportConditionalEnforcement"
+ "v48@0:8@\"NSDictionary\"16@\"IDSPublicIdentityData\"24@\"NSString\"32@?<v@?@\"NSDictionary\">40"
- "21:57:25"
- "Aug 12 2025"
- "B48@0:8@\"IDSURI\"16@\"IDSURI\"24@\"NSString\"32@\"NSDate\"40"
- "Error while publishing status: %@"
- "Recipient endpoint not resolved transparency status, allowing { service: %{public}@, uri: %{public}@, token: %{public}@, transparency: %{public}@ }"
- "Requesting publish for status payload: %@"
- "Service %@ ConstraintType %u AllowedCommandGroups %u IncomingCommand %@. Dropping message %@"
- "_fetchKTDataSignatureForServiceTypes:publicIdentityData:keyStore:withCompletion:"
- "_statusPayloadForOffGridMode:"
- "clientDatasForRegistrations:keyStore:keyTransparencyVerifier:"
- "fetchKTSignatureDataForServiceTypes:publicIdentityData:applicationKeyManager:withCompletion:"
- "fetchKTSignatureDataForServiceTypes:publicIdentityData:withCompletion:"
- "hasPeerTokensForURI:fromURI:service:validThrough:"
- "v40@0:8@\"NSDictionary\"16@\"IDSPublicIdentityData\"24@?<v@?@\"NSDictionary\">32"

```
