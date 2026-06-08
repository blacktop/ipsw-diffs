## DEPClientLibrary

> `/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary`

```diff

-59.120.4.0.0
-  __TEXT.__text: 0x531c
-  __TEXT.__auth_stubs: 0x2b0
+105.0.0.0.0
+  __TEXT.__text: 0x4ea4
   __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__cstring: 0xdb5
+  __TEXT.__cstring: 0xdfb
   __TEXT.__oslogstring: 0x2b
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0x12b
-  __TEXT.__objc_methname: 0x15af
-  __TEXT.__objc_methtype: 0x526
-  __TEXT.__objc_stubs: 0xbe0
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x610
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__cfstring: 0x1860
   __AUTH_CONST.__objc_const: 0x1428
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x180
   __DATA.__bss: 0x48

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4457B055-7CD1-3788-88BA-8AD16CC147A1
+  UUID: F1E140E6-B631-33D1-99F6-629246840414
   Functions: 164
-  Symbols:   850
-  CStrings:  697
+  Symbols:   861
+  CStrings:  399
 
Symbols:
+ _kCCSkipKeyDeviceFeaturesTour
+ _kCCSkipKeyLiquidGlass
+ _kCCSkipKeySecuritySettingsMigration
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[DEPClient init] : 380 -> 388
~ ___17-[DEPClient init]_block_invoke : 100 -> 96
~ ___17-[DEPClient init]_block_invoke_2 : 100 -> 96
~ -[DEPClient dealloc] : 92 -> 88
~ -[DEPClient _connectionError] : 160 -> 152
~ -[DEPClient _completeServiceWithSuccess:response:error:] : 256 -> 252
~ -[DEPClient _callServiceByType:onProxy:completionBlock:] : 772 -> 728
~ -[DEPClient _retrieveProxyObjectAndRunServiceType:completionBlock:] : 444 -> 432
~ ___67-[DEPClient _retrieveProxyObjectAndRunServiceType:completionBlock:]_block_invoke_2 : 124 -> 128
~ -[DEPClient provisionallyEnrollWithNonce:completionBlock:] : 176 -> 180
~ ___58-[DEPClient provisionallyEnrollWithNonce:completionBlock:]_block_invoke : 240 -> 236
~ -[DEPClient fetchConfigurationWithCompletionBlock:] : 92 -> 88
~ -[DEPClient fetchConfigurationWithoutValidationWithCompletionBlock:] : 92 -> 88
~ ___41-[DEPClient unenrollWithCompletionBlock:]_block_invoke : 240 -> 236
~ -[DEPClient retrieveDeviceUploadOrganizationsWithCredentials:completionBlock:] : 176 -> 180
~ ___78-[DEPClient retrieveDeviceUploadOrganizationsWithCredentials:completionBlock:]_block_invoke : 296 -> 280
~ -[DEPClient retrieveDeviceUploadRequestTypesWithCredentials:completionBlock:] : 176 -> 180
~ ___77-[DEPClient retrieveDeviceUploadRequestTypesWithCredentials:completionBlock:]_block_invoke : 264 -> 252
~ -[DEPClient retrieveDeviceUploadSoldToIdsForOrganization:credentials:completionBlock:] : 200 -> 208
~ ___86-[DEPClient retrieveDeviceUploadSoldToIdsForOrganization:credentials:completionBlock:]_block_invoke : 264 -> 252
~ -[DEPClient submitDeviceUploadRequest:credentials:completionBlock:] : 200 -> 208
~ ___67-[DEPClient submitDeviceUploadRequest:credentials:completionBlock:]_block_invoke : 272 -> 268
~ -[DEPClient syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:] : 248 -> 260
~ ___100-[DEPClient syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:]_block_invoke : 244 -> 240
~ ___61-[DEPClient makeStartMDMMigrationRequestWithCompletionBlock:]_block_invoke : 244 -> 240
~ -[DEPClient makeEndMDMMigrationRequestWithServerUID:status:completionBlock:] : 200 -> 208
~ ___76-[DEPClient makeEndMDMMigrationRequestWithServerUID:status:completionBlock:]_block_invoke : 244 -> 240
~ ___65-[DEPClient _cloudConfigRetrievalBlockWithClientCompletionBlock:]_block_invoke : 304 -> 296
~ -[DEPClient _soldToIdsFromDict:] : 452 -> 440
~ -[DEPClient setConnection:] : 64 -> 12
~ -[DEPClient setNonce:] : 64 -> 12
~ -[DEPClient setUserCredentials:] : 64 -> 12
~ -[DEPClient setOrganization:] : 64 -> 12
~ -[DEPClient setDeviceUploadRequest:] : 64 -> 12
~ -[DEPClient setPushToken:] : 64 -> 12
~ -[DEPClient setPushTopic:] : 64 -> 12
~ -[DEPClient setEligibilityDescription:] : 64 -> 12
~ -[DEPClient setServerUID:] : 64 -> 12
~ -[DEPClient setMigrationStatus:] : 64 -> 12
~ -[DEPDeviceUploadCredentials initWithDsid:dsToken:] : 144 -> 152
~ -[DEPDeviceUploadCredentials initWithCoder:] : 200 -> 192
~ -[DEPDeviceUploadCredentials encodeWithCoder:] : 116 -> 108
~ -[DEPDeviceUploadDeviceDetails encodeWithCoder:] : 136 -> 128
~ -[DEPDeviceUploadDeviceDetails initWithCoder:] : 248 -> 236
~ -[DEPDeviceUploadDeviceDetails initWithDict:] : 212 -> 200
~ -[DEPDeviceUploadOrganization encodeWithCoder:] : 236 -> 228
~ -[DEPDeviceUploadOrganization initWithCoder:] : 628 -> 588
~ -[DEPDeviceUploadOrganization initWithDict:] : 448 -> 412
~ -[DEPDeviceUploadOrganization _approversFromApproversArray:] : 340 -> 344
~ -[DEPDeviceUploadOrganization setSkipItrackCheckNum:] : 64 -> 12
~ -[DEPDeviceUploadOrganization setDeviceAdditionDepEnabledNum:] : 64 -> 12
~ -[DEPDeviceUploadOrganization setIdmsWhitelistingEnabledNum:] : 64 -> 12
~ -[DEPDeviceUploadOrganization setIdmsRemoveDeviceEnabledNum:] : 64 -> 12
~ -[DEPDeviceUploadOrganization setDeviceAdditionGbiEnabledNum:] : 64 -> 12
~ -[DEPDeviceUploadRequestType initWithCode:name:] : 144 -> 152
~ -[DEPDeviceUploadRequestType encodeWithCoder:] : 116 -> 108
~ -[DEPDeviceUploadRequestType initWithCoder:] : 200 -> 192
~ -[DEPDeviceUploadSubmissionResponse encodeWithCoder:] : 156 -> 148
~ -[DEPDeviceUploadSubmissionResponse initWithCoder:] : 432 -> 408
~ -[DEPDeviceUploadSubmissionResponse initWithDict:] : 288 -> 268
~ -[DEPDeviceUploadSubmissionResponse _devicesFromDeviceArray:] : 340 -> 344
~ -[DEPDeviceUploadSubmitDeviceRequestPayload initWithOrgId:orgName:requestType:submitter:approver:soldToId:] : 272 -> 292
~ -[DEPDeviceUploadSubmitDeviceRequestPayload encodeWithCoder:] : 196 -> 188
~ -[DEPDeviceUploadSubmitDeviceRequestPayload initWithCoder:] : 400 -> 376
~ -[DEPDeviceUploadUser initWithDsid:name:] : 144 -> 152
~ -[DEPDeviceUploadUser encodeWithCoder:] : 116 -> 108
~ -[DEPDeviceUploadUser initWithCoder:] : 200 -> 192
~ -[DEPDeviceUploadUser initWithApproverDict:] : 172 -> 164
~ _DEPLocalizedString : 120 -> 112
~ __bundle : 84 -> 68
~ _DEPUSEnglishString : 128 -> 120
~ _DEPErrorArray : 220 -> 232
~ __DEPStashFormattedStringInArray : 284 -> 276
~ +[NSError(DEPError) DEPErrorWithDomain:code:descriptionArray:suggestion:USEnglishSuggestion:underlyingError:errorType:] : 844 -> 848
~ -[NSError(DEPError) DEPUSEnglishDescription] : 92 -> 84
~ -[NSError(DEPError) DEPFindPrimaryError] : 300 -> 284
~ ____bundle_block_invoke : 96 -> 92
~ +[DEPSkipKeys allSkipKeys] : 176 -> 160
~ ___26+[DEPSkipKeys allSkipKeys]_block_invoke : 64 -> 60
~ +[DEPSkipKeys _visionOS_skipKeys] : 268 -> 264
~ +[DEPSkipKeys _iOS_skipKeys] : 616 -> 640
~ +[DEPSkipKeys _osx_skipKeys] : 404 -> 412
~ +[DEPSkipKeys _tvOS_skipKeys] : 248 -> 244
CStrings:
+ "DeviceFeaturesTour"
+ "LiquidGlass"
+ "SecuritySettingsMigration"
- "#16@0:8"
- ".cxx_destruct"
- "@\"DEPDeviceUploadCredentials\""
- "@\"DEPDeviceUploadOrganization\""
- "@\"DEPDeviceUploadRequestType\""
- "@\"DEPDeviceUploadSubmitDeviceRequestPayload\""
- "@\"DEPDeviceUploadUser\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16q24@32@40"
- "@56@0:8@16q24@32@40@48"
- "@60@0:8@16@24@32B40B44B48B52B56"
- "@64@0:8@16@24@32@40@48@56"
- "@72@0:8@16q24@32@40@48@56@64"
- "@?"
- "@?16@0:8"
- "@?24@0:8@?16"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DEPDeviceUploadCredentials"
- "DEPDeviceUploadDeviceDetails"
- "DEPDeviceUploadOrganization"
- "DEPDeviceUploadRequestType"
- "DEPDeviceUploadSubmissionResponse"
- "DEPDeviceUploadSubmitDeviceRequestPayload"
- "DEPDeviceUploadUser"
- "DEPError"
- "DEPErrorWithDomain:code:descriptionArray:errorType:"
- "DEPErrorWithDomain:code:descriptionArray:suggestion:USEnglishSuggestion:underlyingError:errorType:"
- "DEPErrorWithDomain:code:descriptionArray:underlyingError:errorType:"
- "DEPFindPrimaryError"
- "DEPSkipKeys"
- "DEPUSEnglishDescription"
- "DEPXPCProtocol"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"DEPDeviceUploadCredentials\",&,N,V_userCredentials"
- "T@\"DEPDeviceUploadOrganization\",&,N,V_organization"
- "T@\"DEPDeviceUploadRequestType\",R,N,V_requestType"
- "T@\"DEPDeviceUploadSubmitDeviceRequestPayload\",&,N,V_deviceUploadRequest"
- "T@\"DEPDeviceUploadUser\",R,N,V_approver"
- "T@\"DEPDeviceUploadUser\",R,N,V_submitter"
- "T@\"NSArray\",R,N,V_approvers"
- "T@\"NSArray\",R,N,V_devices"
- "T@\"NSData\",&,N,V_pushToken"
- "T@\"NSNumber\",&,N,V_deviceAdditionDepEnabledNum"
- "T@\"NSNumber\",&,N,V_deviceAdditionGbiEnabledNum"
- "T@\"NSNumber\",&,N,V_idmsRemoveDeviceEnabledNum"
- "T@\"NSNumber\",&,N,V_idmsWhitelistingEnabledNum"
- "T@\"NSNumber\",&,N,V_skipItrackCheckNum"
- "T@\"NSString\",&,N,V_eligibilityDescription"
- "T@\"NSString\",&,N,V_migrationStatus"
- "T@\"NSString\",&,N,V_nonce"
- "T@\"NSString\",&,N,V_pushTopic"
- "T@\"NSString\",&,N,V_serverUID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_code"
- "T@\"NSString\",R,N,V_deviceUploadStatus"
- "T@\"NSString\",R,N,V_dsToken"
- "T@\"NSString\",R,N,V_dsid"
- "T@\"NSString\",R,N,V_errorMessage"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_orgId"
- "T@\"NSString\",R,N,V_orgName"
- "T@\"NSString\",R,N,V_requestId"
- "T@\"NSString\",R,N,V_requestStatus"
- "T@\"NSString\",R,N,V_serialNumber"
- "T@\"NSString\",R,N,V_soldToId"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@?,C,N,V_callback"
- "TB,N,V_eligibleForMigration"
- "TB,R"
- "TB,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_approver"
- "_approvers"
- "_approversFromApproversArray:"
- "_callServiceByType:onProxy:completionBlock:"
- "_callback"
- "_cloudConfigRetrievalBlockWithClientCompletionBlock:"
- "_code"
- "_completeServiceWithSuccess:response:error:"
- "_connection"
- "_connectionError"
- "_deviceAdditionDepEnabledNum"
- "_deviceAdditionGbiEnabledNum"
- "_deviceUploadRequest"
- "_deviceUploadStatus"
- "_devices"
- "_devicesFromDeviceArray:"
- "_dsToken"
- "_dsid"
- "_eligibilityDescription"
- "_eligibleForMigration"
- "_errorMessage"
- "_iOS_skipKeys"
- "_idmsRemoveDeviceEnabledNum"
- "_idmsWhitelistingEnabledNum"
- "_migrationStatus"
- "_name"
- "_nonce"
- "_orgId"
- "_orgName"
- "_organization"
- "_organizationFromDict:"
- "_organizationsFromArray:"
- "_osx_skipKeys"
- "_pushToken"
- "_pushTopic"
- "_requestId"
- "_requestStatus"
- "_requestType"
- "_requestTypesFromDict:"
- "_retrieveProxyObjectAndRunServiceType:completionBlock:"
- "_serialNumber"
- "_serverUID"
- "_skipItrackCheckNum"
- "_soldToId"
- "_soldToIdsFromDict:"
- "_submitter"
- "_tvOS_skipKeys"
- "_userCredentials"
- "_visionOS_skipKeys"
- "_watchOS_skipKeys"
- "addObject:"
- "allSkipKeys"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "callback"
- "class"
- "conformsToProtocol:"
- "connection"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentLocale"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "deviceUploadRequest"
- "dictionary"
- "eligibilityDescription"
- "eligibleForMigration"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "fetchConfigurationWithCompletionBlock:"
- "fetchConfigurationWithoutValidationWithCompletionBlock:"
- "hash"
- "init"
- "initWithApproverDict:"
- "initWithCode:name:"
- "initWithCoder:"
- "initWithDict:"
- "initWithDsid:dsToken:"
- "initWithDsid:name:"
- "initWithFormat:locale:arguments:"
- "initWithLocaleIdentifier:"
- "initWithMachServiceName:options:"
- "initWithOrgId:orgName:approvers:skipItrackCheck:deviceAdditionDepEnabled:idmsWhitelistingEnabled:idmsRemoveDeviceEnabled:deviceAdditionGbiEnabled:"
- "initWithOrgId:orgName:requestType:submitter:approver:soldToId:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "localizedStringForKey:value:table:localization:"
- "makeEndMDMMigrationRequestWithServerUID:status:completionBlock:"
- "makeStartMDMMigrationRequestWithCompletionBlock:"
- "migrationStatus"
- "mutableCopy"
- "nonce"
- "null"
- "numberWithBool:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "organization"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pingWithCompletionBlock:"
- "provisionallyEnrollWithNonce:completionBlock:"
- "pushToken"
- "pushTopic"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retrieveDeviceUploadOrganizationsWithCredentials:completionBlock:"
- "retrieveDeviceUploadRequestTypesWithCredentials:completionBlock:"
- "retrieveDeviceUploadSoldToIdsForOrganization:credentials:completionBlock:"
- "self"
- "serverUID"
- "setCallback:"
- "setConnection:"
- "setDeviceAdditionDepEnabledNum:"
- "setDeviceAdditionGbiEnabledNum:"
- "setDeviceUploadRequest:"
- "setEligibilityDescription:"
- "setEligibleForMigration:"
- "setIdmsRemoveDeviceEnabledNum:"
- "setIdmsWhitelistingEnabledNum:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMigrationStatus:"
- "setNonce:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOrganization:"
- "setPushToken:"
- "setPushTopic:"
- "setRemoteObjectInterface:"
- "setServerUID:"
- "setSkipItrackCheckNum:"
- "setUserCredentials:"
- "setWithArray:"
- "subarrayWithRange:"
- "submitDeviceUploadRequest:credentials:completionBlock:"
- "superclass"
- "supportsSecureCoding"
- "syncDEPPushToken:pushTopic:completionBlock:"
- "syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:"
- "unenrollWithCompletionBlock:"
- "userCredentials"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSDictionary\"@\"NSError\">16"
- "v32@0:8@\"DEPDeviceUploadCredentials\"16@?<v@?B@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8q16@?24"
- "v36@0:8B16@20@28"
- "v40@0:8@\"DEPDeviceUploadOrganization\"16@\"DEPDeviceUploadCredentials\"24@?<v@?B@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"DEPDeviceUploadSubmitDeviceRequestPayload\"16@\"DEPDeviceUploadCredentials\"24@?<v@?B@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8q16@24@?32"
- "v52@0:8@\"NSData\"16@\"NSString\"24B32@\"NSString\"36@?<v@?B@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16@24B32@36@?44"
- "zone"

```
