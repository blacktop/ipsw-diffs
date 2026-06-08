## RemoteManagementProtocol

> `/System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/RemoteManagementProtocol`

```diff

-585.120.2.0.0
-  __TEXT.__text: 0x5d88
-  __TEXT.__auth_stubs: 0x150
+621.0.0.502.1
+  __TEXT.__text: 0x5e70
   __TEXT.__objc_methlist: 0xb80
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x909
+  __TEXT.__cstring: 0x912
   __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x28a
-  __TEXT.__objc_methname: 0x19a1
-  __TEXT.__objc_methtype: 0x148
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0xb0
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xd60
   __AUTH_CONST.__objc_const: 0x1658
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc4
   __DATA_DIRTY.__objc_data: 0x640
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D08463D-37A0-39FA-AB44-D83623C8919F
+  UUID: 65690A9B-9E8F-34CB-919A-86A1836F6E29
   Functions: 234
-  Symbols:   878
-  CStrings:  489
+  Symbols:   884
+  CStrings:  222
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[RMProtocolCommandRequest requestWithStatus:identifier:result:reasons:] : 176 -> 188
~ -[RMProtocolCommandRequest serializeWithType:] : 480 -> 464
~ -[RMProtocolCommandRequest copyWithZone:] : 196 -> 228
~ -[RMProtocolCommandRequest requestStatus] : 16 -> 20
~ -[RMProtocolCommandRequest requestIdentifier] : 16 -> 20
~ -[RMProtocolCommandRequest requestResult] : 16 -> 20
~ -[RMProtocolCommandRequest requestReasons] : 16 -> 20
~ +[RMProtocolCommandRequest_StatusReason allowedRequestKeys] : 200 -> 192
~ +[RMProtocolCommandRequest_StatusReason buildWithCode:description:details:] : 144 -> 152
~ -[RMProtocolCommandRequest_StatusReason loadFromDictionary:serializationType:error:] : 552 -> 524
~ -[RMProtocolCommandRequest_StatusReason serializeWithType:] : 348 -> 336
~ -[RMProtocolCommandRequest_StatusReason copyWithZone:] : 168 -> 192
~ -[RMProtocolCommandRequest_StatusReason requestCode] : 16 -> 20
~ -[RMProtocolCommandRequest_StatusReason requestDescription] : 16 -> 20
~ -[RMProtocolCommandRequest_StatusReason requestDetails] : 16 -> 20
~ +[RMProtocolCommandResponse requestWithCommandToken:command:] : 120 -> 124
~ -[RMProtocolCommandResponse serializeWithType:] : 292 -> 284
~ -[RMProtocolCommandResponse copyWithZone:] : 140 -> 156
~ -[RMProtocolCommandResponse responseCommandToken] : 16 -> 20
~ -[RMProtocolCommandResponse responseCommand] : 16 -> 20
~ +[RMProtocolCommandResponse_Command allowedResponseKeys] : 200 -> 192
~ +[RMProtocolCommandResponse_Command buildWithType:identifier:payload:] : 144 -> 152
~ +[RMProtocolCommandResponse_Command buildRequiredOnlyWithType:identifier:] : 120 -> 124
~ -[RMProtocolCommandResponse_Command loadFromDictionary:serializationType:error:] : 552 -> 524
~ -[RMProtocolCommandResponse_Command serializeWithType:] : 348 -> 336
~ -[RMProtocolCommandResponse_Command copyWithZone:] : 168 -> 192
~ -[RMProtocolCommandResponse_Command responseType] : 16 -> 20
~ -[RMProtocolCommandResponse_Command responseIdentifier] : 16 -> 20
~ -[RMProtocolCommandResponse_Command responsePayload] : 16 -> 20
~ +[RMProtocolDeclarationItemsResponse requestWithDeclarations:declarationsToken:] : 120 -> 124
~ -[RMProtocolDeclarationItemsResponse serializeWithType:] : 292 -> 284
~ -[RMProtocolDeclarationItemsResponse copyWithZone:] : 140 -> 156
~ -[RMProtocolDeclarationItemsResponse responseDeclarations] : 16 -> 20
~ -[RMProtocolDeclarationItemsResponse responseDeclarationsToken] : 16 -> 20
~ +[RMProtocolDeclarationItemsResponse_Declarations allowedResponseKeys] : 208 -> 200
~ +[RMProtocolDeclarationItemsResponse_Declarations buildWithActivations:configurations:assets:management:] : 176 -> 188
~ +[RMProtocolDeclarationItemsResponse_Declarations buildRequiredOnlyWithActivations:configurations:assets:management:] : 176 -> 188
~ -[RMProtocolDeclarationItemsResponse_Declarations loadFromDictionary:serializationType:error:] : 660 -> 632
~ -[RMProtocolDeclarationItemsResponse_Declarations serializeWithType:] : 600 -> 584
~ -[RMProtocolDeclarationItemsResponse_Declarations copyWithZone:] : 196 -> 228
~ -[RMProtocolDeclarationItemsResponse_Declarations responseActivations] : 16 -> 20
~ -[RMProtocolDeclarationItemsResponse_Declarations responseConfigurations] : 16 -> 20
~ -[RMProtocolDeclarationItemsResponse_Declarations responseAssets] : 16 -> 20
~ -[RMProtocolDeclarationItemsResponse_Declarations responseManagement] : 16 -> 20
~ +[RMProtocolDeclarationItemsResponse_DeclarationItem allowedResponseKeys] : 188 -> 180
~ +[RMProtocolDeclarationItemsResponse_DeclarationItem buildWithIdentifier:serverToken:] : 120 -> 124
~ +[RMProtocolDeclarationItemsResponse_DeclarationItem buildRequiredOnlyWithIdentifier:serverToken:] : 120 -> 124
~ -[RMProtocolDeclarationItemsResponse_DeclarationItem loadFromDictionary:serializationType:error:] : 480 -> 452
~ -[RMProtocolDeclarationItemsResponse_DeclarationItem serializeWithType:] : 204 -> 196
~ -[RMProtocolDeclarationItemsResponse_DeclarationItem copyWithZone:] : 140 -> 156
~ -[RMProtocolDeclarationItemsResponse_DeclarationItem responseIdentifier] : 16 -> 20
~ -[RMProtocolDeclarationItemsResponse_DeclarationItem responseServerToken] : 16 -> 20
~ +[RMProtocolDeclarationResponse requestWithType:identifier:serverToken:payload:] : 176 -> 188
~ -[RMProtocolDeclarationResponse serializeWithType:] : 404 -> 388
~ -[RMProtocolDeclarationResponse copyWithZone:] : 196 -> 228
~ -[RMProtocolDeclarationResponse responseType] : 16 -> 20
~ -[RMProtocolDeclarationResponse responseIdentifier] : 16 -> 20
~ -[RMProtocolDeclarationResponse responseServerToken] : 16 -> 20
~ -[RMProtocolDeclarationResponse responsePayload] : 16 -> 20
~ -[RMProtocolEnrollReferralResponse serializeWithType:] : 148 -> 144
~ -[RMProtocolEnrollReferralResponse copyWithZone:] : 112 -> 120
~ -[RMProtocolEnrollReferralResponse responseReferralBaseURL] : 16 -> 20
~ +[RMProtocolEnrollRequest requestWithEnrollmentToken:statusItems:] : 120 -> 124
~ -[RMProtocolEnrollRequest serializeWithType:] : 292 -> 284
~ -[RMProtocolEnrollRequest copyWithZone:] : 140 -> 156
~ -[RMProtocolEnrollRequest requestEnrollmentToken] : 16 -> 20
~ -[RMProtocolEnrollRequest requestStatusItems] : 16 -> 20
~ +[RMProtocolEnrollResponse requestWithPushTopic:pushEnvironment:statusItems:] : 156 -> 164
~ -[RMProtocolEnrollResponse serializeWithType:] : 272 -> 260
~ ___46-[RMProtocolEnrollResponse serializeWithType:]_block_invoke : 56 -> 8
~ -[RMProtocolEnrollResponse copyWithZone:] : 168 -> 192
~ -[RMProtocolEnrollResponse responsePushTopic] : 16 -> 20
~ -[RMProtocolEnrollResponse responsePushEnvironment] : 16 -> 20
~ -[RMProtocolEnrollResponse responseStatusItems] : 16 -> 20
~ +[RMProtocolErrorResponse requestWithCode:description:details:] : 144 -> 152
~ -[RMProtocolErrorResponse serializeWithType:] : 348 -> 336
~ -[RMProtocolErrorResponse copyWithZone:] : 168 -> 192
~ -[RMProtocolErrorResponse responseCode] : 16 -> 20
~ -[RMProtocolErrorResponse responseDescription] : 16 -> 20
~ -[RMProtocolErrorResponse responseDetails] : 16 -> 20
~ +[RMProtocolPushMessage requestWithEnrollmentToken:syncTokens:] : 120 -> 124
~ -[RMProtocolPushMessage serializeWithType:] : 292 -> 284
~ -[RMProtocolPushMessage copyWithZone:] : 140 -> 156
~ -[RMProtocolPushMessage messageEnrollmentToken] : 16 -> 20
~ -[RMProtocolPushMessage messageSyncTokens] : 16 -> 20
~ +[RMProtocolStatusReport requestWithStatusItems:errors:fullReport:] : 156 -> 164
~ -[RMProtocolStatusReport serializeWithType:] : 428 -> 416
~ -[RMProtocolStatusReport copyWithZone:] : 168 -> 192
~ -[RMProtocolStatusReport reportStatusItems] : 16 -> 20
~ -[RMProtocolStatusReport reportErrors] : 16 -> 20
~ -[RMProtocolStatusReport reportFullReport] : 16 -> 20
~ +[RMProtocolStatusReport_Errors allowedReportKeys] : 188 -> 180
~ +[RMProtocolStatusReport_Errors buildWithStatusItem:reasons:] : 120 -> 124
~ -[RMProtocolStatusReport_Errors loadFromDictionary:serializationType:error:] : 512 -> 484
~ -[RMProtocolStatusReport_Errors serializeWithType:] : 292 -> 284
~ -[RMProtocolStatusReport_Errors copyWithZone:] : 140 -> 156
~ -[RMProtocolStatusReport_Errors reportStatusItem] : 16 -> 20
~ -[RMProtocolStatusReport_Errors reportReasons] : 16 -> 20
~ +[RMProtocolStatusReport_StatusReason allowedReportKeys] : 200 -> 192
~ +[RMProtocolStatusReport_StatusReason buildWithCode:description:details:] : 144 -> 152
~ -[RMProtocolStatusReport_StatusReason loadFromDictionary:serializationType:error:] : 552 -> 524
~ -[RMProtocolStatusReport_StatusReason serializeWithType:] : 348 -> 336
~ -[RMProtocolStatusReport_StatusReason copyWithZone:] : 168 -> 192
~ -[RMProtocolStatusReport_StatusReason reportCode] : 16 -> 20
~ -[RMProtocolStatusReport_StatusReason reportDescription] : 16 -> 20
~ -[RMProtocolStatusReport_StatusReason reportDetails] : 16 -> 20
~ +[RMProtocolSynchronizationTokens requestWithTimestamp:declarationsToken:] : 120 -> 124
~ -[RMProtocolSynchronizationTokens serializeWithType:] : 212 -> 204
~ -[RMProtocolSynchronizationTokens copyWithZone:] : 140 -> 156
~ -[RMProtocolSynchronizationTokens tokensTimestamp] : 16 -> 20
~ -[RMProtocolSynchronizationTokens tokensDeclarationsToken] : 16 -> 20
~ -[RMProtocolTokensResponse serializeWithType:] : 236 -> 232
~ -[RMProtocolTokensResponse copyWithZone:] : 112 -> 120
~ -[RMProtocolTokensResponse responseSyncTokens] : 16 -> 20
~ -[RMProtocolWellKnownResponse serializeWithType:] : 236 -> 232
~ -[RMProtocolWellKnownResponse copyWithZone:] : 112 -> 120
~ -[RMProtocolWellKnownResponse responseServers] : 16 -> 20
~ +[RMProtocolWellKnownResponse_WellKnownResponseServer allowedResponseKeys] : 188 -> 180
~ +[RMProtocolWellKnownResponse_WellKnownResponseServer buildWithVersion:baseURL:] : 120 -> 124
~ +[RMProtocolWellKnownResponse_WellKnownResponseServer buildRequiredOnlyWithVersion:baseURL:] : 120 -> 124
~ -[RMProtocolWellKnownResponse_WellKnownResponseServer loadFromDictionary:serializationType:error:] : 480 -> 452
~ -[RMProtocolWellKnownResponse_WellKnownResponseServer serializeWithType:] : 204 -> 196
~ -[RMProtocolWellKnownResponse_WellKnownResponseServer copyWithZone:] : 140 -> 156
~ -[RMProtocolWellKnownResponse_WellKnownResponseServer responseVersion] : 16 -> 20
~ -[RMProtocolWellKnownResponse_WellKnownResponseServer responseBaseURL] : 16 -> 20
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"RMModelAnyPayload\""
- "@\"RMProtocolCommandResponse_Command\""
- "@\"RMProtocolDeclarationItemsResponse_Declarations\""
- "@\"RMProtocolSynchronizationTokens\""
- "@16@0:8"
- "@20@0:8s16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "B36@0:8@16s24^@28"
- "RMProtocolCommandRequest"
- "RMProtocolCommandRequest_StatusReason"
- "RMProtocolCommandResponse"
- "RMProtocolCommandResponse_Command"
- "RMProtocolDeclarationItemsResponse"
- "RMProtocolDeclarationItemsResponse_DeclarationItem"
- "RMProtocolDeclarationItemsResponse_Declarations"
- "RMProtocolDeclarationResponse"
- "RMProtocolEnrollReferralResponse"
- "RMProtocolEnrollRequest"
- "RMProtocolEnrollResponse"
- "RMProtocolErrorResponse"
- "RMProtocolPushMessage"
- "RMProtocolStatusReport"
- "RMProtocolStatusReport_Errors"
- "RMProtocolStatusReport_StatusReason"
- "RMProtocolSynchronizationTokens"
- "RMProtocolTokensResponse"
- "RMProtocolWellKnownResponse"
- "RMProtocolWellKnownResponse_WellKnownResponseServer"
- "T@\"NSArray\",C,N,V_reportErrors"
- "T@\"NSArray\",C,N,V_reportReasons"
- "T@\"NSArray\",C,N,V_requestReasons"
- "T@\"NSArray\",C,N,V_responseActivations"
- "T@\"NSArray\",C,N,V_responseAssets"
- "T@\"NSArray\",C,N,V_responseConfigurations"
- "T@\"NSArray\",C,N,V_responseManagement"
- "T@\"NSArray\",C,N,V_responseServers"
- "T@\"NSArray\",C,N,V_responseStatusItems"
- "T@\"NSDate\",C,N,V_tokensTimestamp"
- "T@\"NSNumber\",C,N,V_reportFullReport"
- "T@\"NSSet\",R,C"
- "T@\"NSString\",C,N,V_messageEnrollmentToken"
- "T@\"NSString\",C,N,V_reportCode"
- "T@\"NSString\",C,N,V_reportDescription"
- "T@\"NSString\",C,N,V_reportStatusItem"
- "T@\"NSString\",C,N,V_requestCode"
- "T@\"NSString\",C,N,V_requestDescription"
- "T@\"NSString\",C,N,V_requestEnrollmentToken"
- "T@\"NSString\",C,N,V_requestIdentifier"
- "T@\"NSString\",C,N,V_requestStatus"
- "T@\"NSString\",C,N,V_responseBaseURL"
- "T@\"NSString\",C,N,V_responseCode"
- "T@\"NSString\",C,N,V_responseCommandToken"
- "T@\"NSString\",C,N,V_responseDeclarationsToken"
- "T@\"NSString\",C,N,V_responseDescription"
- "T@\"NSString\",C,N,V_responseIdentifier"
- "T@\"NSString\",C,N,V_responsePushEnvironment"
- "T@\"NSString\",C,N,V_responsePushTopic"
- "T@\"NSString\",C,N,V_responseReferralBaseURL"
- "T@\"NSString\",C,N,V_responseServerToken"
- "T@\"NSString\",C,N,V_responseType"
- "T@\"NSString\",C,N,V_responseVersion"
- "T@\"NSString\",C,N,V_tokensDeclarationsToken"
- "T@\"RMModelAnyPayload\",C,N,V_reportDetails"
- "T@\"RMModelAnyPayload\",C,N,V_reportStatusItems"
- "T@\"RMModelAnyPayload\",C,N,V_requestDetails"
- "T@\"RMModelAnyPayload\",C,N,V_requestResult"
- "T@\"RMModelAnyPayload\",C,N,V_requestStatusItems"
- "T@\"RMModelAnyPayload\",C,N,V_responseDetails"
- "T@\"RMModelAnyPayload\",C,N,V_responsePayload"
- "T@\"RMProtocolCommandResponse_Command\",C,N,V_responseCommand"
- "T@\"RMProtocolDeclarationItemsResponse_Declarations\",C,N,V_responseDeclarations"
- "T@\"RMProtocolSynchronizationTokens\",C,N,V_messageSyncTokens"
- "T@\"RMProtocolSynchronizationTokens\",C,N,V_responseSyncTokens"
- "_messageEnrollmentToken"
- "_messageSyncTokens"
- "_reportCode"
- "_reportDescription"
- "_reportDetails"
- "_reportErrors"
- "_reportFullReport"
- "_reportReasons"
- "_reportStatusItem"
- "_reportStatusItems"
- "_requestCode"
- "_requestDescription"
- "_requestDetails"
- "_requestEnrollmentToken"
- "_requestIdentifier"
- "_requestReasons"
- "_requestResult"
- "_requestStatus"
- "_requestStatusItems"
- "_responseActivations"
- "_responseAssets"
- "_responseBaseURL"
- "_responseCode"
- "_responseCommand"
- "_responseCommandToken"
- "_responseConfigurations"
- "_responseDeclarations"
- "_responseDeclarationsToken"
- "_responseDescription"
- "_responseDetails"
- "_responseIdentifier"
- "_responseManagement"
- "_responsePayload"
- "_responsePushEnvironment"
- "_responsePushTopic"
- "_responseReferralBaseURL"
- "_responseServerToken"
- "_responseServers"
- "_responseStatusItems"
- "_responseSyncTokens"
- "_responseType"
- "_responseVersion"
- "_tokensDeclarationsToken"
- "_tokensTimestamp"
- "allKeys"
- "allowedReportKeys"
- "allowedRequestKeys"
- "allowedResponseKeys"
- "arrayWithObjects:count:"
- "buildRequiredOnlyWithActivations:configurations:assets:management:"
- "buildRequiredOnlyWithCode:"
- "buildRequiredOnlyWithIdentifier:serverToken:"
- "buildRequiredOnlyWithStatusItem:"
- "buildRequiredOnlyWithType:identifier:"
- "buildRequiredOnlyWithVersion:baseURL:"
- "buildWithActivations:configurations:assets:management:"
- "buildWithCode:description:details:"
- "buildWithIdentifier:serverToken:"
- "buildWithStatusItem:reasons:"
- "buildWithType:identifier:payload:"
- "buildWithVersion:baseURL:"
- "copy"
- "copyWithZone:"
- "count"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "loadArrayFromDictionary:usingKey:forKeyPath:classType:nested:isRequired:defaultValue:serializationType:error:"
- "loadArrayFromDictionary:usingKey:forKeyPath:validator:isRequired:defaultValue:error:"
- "loadBooleanFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:error:"
- "loadDateFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:serializationType:error:"
- "loadDictionaryFromDictionary:usingKey:forKeyPath:classType:isRequired:defaultValue:serializationType:error:"
- "loadFromDictionary:serializationType:error:"
- "loadStringFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:error:"
- "minusSet:"
- "requestWithCode:description:details:"
- "requestWithCommandToken:command:"
- "requestWithDeclarations:declarationsToken:"
- "requestWithEnrollmentToken:statusItems:"
- "requestWithEnrollmentToken:syncTokens:"
- "requestWithPushTopic:pushEnvironment:statusItems:"
- "requestWithReferralBaseURL:"
- "requestWithServers:"
- "requestWithStatus:identifier:result:reasons:"
- "requestWithStatusItems:errors:fullReport:"
- "requestWithSyncTokens:"
- "requestWithTimestamp:declarationsToken:"
- "requestWithType:identifier:serverToken:payload:"
- "serializeArrayIntoDictionary:usingKey:value:itemSerializer:isRequired:defaultValue:"
- "serializeBooleanIntoDictionary:usingKey:value:isRequired:defaultValue:"
- "serializeDateIntoDictionary:usingKey:value:isRequired:defaultValue:serializationType:"
- "serializeDictionaryIntoDictionary:usingKey:value:dictSerializer:isRequired:defaultValue:"
- "serializeStringIntoDictionary:usingKey:value:isRequired:defaultValue:"
- "serializeWithType:"
- "setMessageEnrollmentToken:"
- "setMessageSyncTokens:"
- "setReportCode:"
- "setReportDescription:"
- "setReportDetails:"
- "setReportErrors:"
- "setReportFullReport:"
- "setReportReasons:"
- "setReportStatusItem:"
- "setReportStatusItems:"
- "setRequestCode:"
- "setRequestDescription:"
- "setRequestDetails:"
- "setRequestEnrollmentToken:"
- "setRequestIdentifier:"
- "setRequestReasons:"
- "setRequestResult:"
- "setRequestStatus:"
- "setRequestStatusItems:"
- "setResponseActivations:"
- "setResponseAssets:"
- "setResponseBaseURL:"
- "setResponseCode:"
- "setResponseCommand:"
- "setResponseCommandToken:"
- "setResponseConfigurations:"
- "setResponseDeclarations:"
- "setResponseDeclarationsToken:"
- "setResponseDescription:"
- "setResponseDetails:"
- "setResponseIdentifier:"
- "setResponseManagement:"
- "setResponsePayload:"
- "setResponsePushEnvironment:"
- "setResponsePushTopic:"
- "setResponseReferralBaseURL:"
- "setResponseServerToken:"
- "setResponseServers:"
- "setResponseStatusItems:"
- "setResponseSyncTokens:"
- "setResponseType:"
- "setResponseVersion:"
- "setTokensDeclarationsToken:"
- "setTokensTimestamp:"
- "setWithArray:"
- "stringWithFormat:"
- "v16@0:8"
- "v24@0:8@16"

```
