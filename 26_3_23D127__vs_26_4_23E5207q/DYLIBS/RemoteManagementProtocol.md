## RemoteManagementProtocol

> `/System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/RemoteManagementProtocol`

```diff

-585.80.2.0.0
-  __TEXT.__text: 0x5c24
-  __TEXT.__auth_stubs: 0x1b0
+585.100.8.0.0
+  __TEXT.__text: 0x5d88
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_methlist: 0xb80
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x909

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xd60
   __AUTH_CONST.__objc_const: 0x1658

   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81F045A3-55CD-3A47-AF56-B877325F0C7B
+  UUID: F402603C-5893-3AF6-85C9-CC55732F2358
   Functions: 234
-  Symbols:   884
+  Symbols:   878
   CStrings:  489
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
Functions:
~ +[RMProtocolCommandRequest requestWithStatus:identifier:result:reasons:] : 188 -> 176
~ -[RMProtocolCommandRequest serializeWithType:] : 464 -> 480
~ +[RMProtocolCommandRequest_StatusReason allowedRequestKeys] : 192 -> 200
~ +[RMProtocolCommandRequest_StatusReason buildWithCode:description:details:] : 152 -> 144
~ -[RMProtocolCommandRequest_StatusReason loadFromDictionary:serializationType:error:] : 524 -> 552
~ -[RMProtocolCommandRequest_StatusReason serializeWithType:] : 336 -> 348
~ +[RMProtocolCommandResponse requestWithCommandToken:command:] : 124 -> 120
~ -[RMProtocolCommandResponse serializeWithType:] : 284 -> 292
~ +[RMProtocolCommandResponse_Command allowedResponseKeys] : 192 -> 200
~ +[RMProtocolCommandResponse_Command buildWithType:identifier:payload:] : 152 -> 144
~ +[RMProtocolCommandResponse_Command buildRequiredOnlyWithType:identifier:] : 124 -> 120
~ -[RMProtocolCommandResponse_Command loadFromDictionary:serializationType:error:] : 524 -> 552
~ -[RMProtocolCommandResponse_Command serializeWithType:] : 336 -> 348
~ +[RMProtocolDeclarationItemsResponse requestWithDeclarations:declarationsToken:] : 124 -> 120
~ -[RMProtocolDeclarationItemsResponse serializeWithType:] : 284 -> 292
~ +[RMProtocolDeclarationItemsResponse_Declarations allowedResponseKeys] : 200 -> 208
~ +[RMProtocolDeclarationItemsResponse_Declarations buildWithActivations:configurations:assets:management:] : 188 -> 176
~ +[RMProtocolDeclarationItemsResponse_Declarations buildRequiredOnlyWithActivations:configurations:assets:management:] : 188 -> 176
~ -[RMProtocolDeclarationItemsResponse_Declarations loadFromDictionary:serializationType:error:] : 632 -> 660
~ -[RMProtocolDeclarationItemsResponse_Declarations serializeWithType:] : 584 -> 600
~ +[RMProtocolDeclarationItemsResponse_DeclarationItem allowedResponseKeys] : 180 -> 188
~ +[RMProtocolDeclarationItemsResponse_DeclarationItem buildWithIdentifier:serverToken:] : 124 -> 120
~ +[RMProtocolDeclarationItemsResponse_DeclarationItem buildRequiredOnlyWithIdentifier:serverToken:] : 124 -> 120
~ -[RMProtocolDeclarationItemsResponse_DeclarationItem loadFromDictionary:serializationType:error:] : 452 -> 480
~ -[RMProtocolDeclarationItemsResponse_DeclarationItem serializeWithType:] : 196 -> 204
~ +[RMProtocolDeclarationResponse requestWithType:identifier:serverToken:payload:] : 188 -> 176
~ -[RMProtocolDeclarationResponse serializeWithType:] : 388 -> 404
~ -[RMProtocolEnrollReferralResponse serializeWithType:] : 144 -> 148
~ +[RMProtocolEnrollRequest requestWithEnrollmentToken:statusItems:] : 124 -> 120
~ -[RMProtocolEnrollRequest serializeWithType:] : 284 -> 292
~ +[RMProtocolEnrollResponse requestWithPushTopic:pushEnvironment:statusItems:] : 164 -> 156
~ -[RMProtocolEnrollResponse serializeWithType:] : 260 -> 272
~ ___46-[RMProtocolEnrollResponse serializeWithType:]_block_invoke : 8 -> 56
~ +[RMProtocolErrorResponse requestWithCode:description:details:] : 152 -> 144
~ -[RMProtocolErrorResponse serializeWithType:] : 336 -> 348
~ +[RMProtocolPushMessage requestWithEnrollmentToken:syncTokens:] : 124 -> 120
~ -[RMProtocolPushMessage serializeWithType:] : 284 -> 292
~ +[RMProtocolStatusReport requestWithStatusItems:errors:fullReport:] : 164 -> 156
~ -[RMProtocolStatusReport serializeWithType:] : 416 -> 428
~ +[RMProtocolStatusReport_Errors allowedReportKeys] : 180 -> 188
~ +[RMProtocolStatusReport_Errors buildWithStatusItem:reasons:] : 124 -> 120
~ -[RMProtocolStatusReport_Errors loadFromDictionary:serializationType:error:] : 484 -> 512
~ -[RMProtocolStatusReport_Errors serializeWithType:] : 284 -> 292
~ +[RMProtocolStatusReport_StatusReason allowedReportKeys] : 192 -> 200
~ +[RMProtocolStatusReport_StatusReason buildWithCode:description:details:] : 152 -> 144
~ -[RMProtocolStatusReport_StatusReason loadFromDictionary:serializationType:error:] : 524 -> 552
~ -[RMProtocolStatusReport_StatusReason serializeWithType:] : 336 -> 348
~ +[RMProtocolSynchronizationTokens requestWithTimestamp:declarationsToken:] : 124 -> 120
~ -[RMProtocolSynchronizationTokens serializeWithType:] : 204 -> 212
~ -[RMProtocolTokensResponse serializeWithType:] : 232 -> 236
~ -[RMProtocolWellKnownResponse serializeWithType:] : 232 -> 236
~ +[RMProtocolWellKnownResponse_WellKnownResponseServer allowedResponseKeys] : 180 -> 188
~ +[RMProtocolWellKnownResponse_WellKnownResponseServer buildWithVersion:baseURL:] : 124 -> 120
~ +[RMProtocolWellKnownResponse_WellKnownResponseServer buildRequiredOnlyWithVersion:baseURL:] : 124 -> 120
~ -[RMProtocolWellKnownResponse_WellKnownResponseServer loadFromDictionary:serializationType:error:] : 452 -> 480
~ -[RMProtocolWellKnownResponse_WellKnownResponseServer serializeWithType:] : 196 -> 204

```
