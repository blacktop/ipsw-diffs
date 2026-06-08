## AppleIDSSOAuthentication

> `/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication`

```diff

-110.0.0.0.0
-  __TEXT.__text: 0x46da4
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x7d4
+112.1.0.0.0
+  __TEXT.__text: 0x46f1c
+  __TEXT.__objc_methlist: 0x814
   __TEXT.__const: 0xd20
-  __TEXT.__cstring: 0x78c
-  __TEXT.__oslogstring: 0xc56
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x108
-  __TEXT.__objc_methname: 0x1957
-  __TEXT.__objc_methtype: 0x44a
-  __TEXT.__objc_stubs: 0x1280
-  __DATA_CONST.__got: 0x168
+  __TEXT.__cstring: 0x808
+  __TEXT.__oslogstring: 0xe77
+  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__unwind_info: 0x290
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x280
-  __AUTH_CONST.__const: 0x5960
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0xbb0
+  __DATA_CONST.__got: 0x168
+  __AUTH_CONST.__const: 0x5980
+  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__objc_const: 0xbe0
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x5c
+  __AUTH_CONST.__auth_got: 0x2c0
+  __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x2d0
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43805C9D-9B96-3EA8-A15F-883B632FACBD
-  Functions: 202
-  Symbols:   901
-  CStrings:  498
+  UUID: A5FA3FE5-ACBC-362B-9136-7AFBAA7DCE08
+  Functions: 212
+  Symbols:   939
+  CStrings:  190
 
Symbols:
+ +[AIDAServiceOwnersManager _serviceToBundleNameMapping]
+ +[AIDAServiceOwnersManager _serviceToBundleNameMapping].cold.1
+ -[AIDAServiceOwnersManager _loadAndValidateBundle:forService:result:]
+ -[AIDAServiceOwnersManager _loadAndValidateBundle:forService:result:].cold.1
+ -[AIDAServiceOwnersManager _loadAndValidateBundle:forService:result:].cold.2
+ -[AIDAServiceOwnersManager _loadAndValidateBundle:forService:result:].cold.3
+ -[AIDAServiceOwnersManager _loadAndValidateBundle:forService:result:].cold.4
+ -[AIDAServiceOwnersManager accountForSingleService:]
+ -[AIDAServiceOwnersManager setSignInDelegate:]
+ -[AIDAServiceOwnersManager signInDelegate]
+ GCC_except_table25
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table46
+ GCC_except_table47
+ _OBJC_IVAR_$_AIDAServiceOwnersManager._signInDelegate
+ ___55+[AIDAServiceOwnersManager _serviceToBundleNameMapping]_block_invoke
+ ___65-[AIDAServiceOwnersManager signInService:withContext:completion:]_block_invoke.cold.1
+ ___69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.121
+ ___69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.125
+ ___69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke_2.123
+ ___70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.127
+ ___70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.129
+ ___70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke_2.128
+ ___84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.115
+ ___84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.116
+ ___84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.120
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80w_e20_v20?0B8"NSError"12ls32l8w80l8s40l8s48l8s56l8s72l8s64l8
+ ___block_literal_global.131
+ ___block_literal_global.91
+ __serviceToBundleNameMapping.mapping
+ __serviceToBundleNameMapping.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$_loadAndValidateBundle:forService:result:
+ _objc_msgSend$_serviceToBundleNameMapping
+ _objc_msgSend$bundlePath
+ _objc_msgSend$pluginWithName:inSubpath:
+ _objc_msgSend$serviceOwnersManager:didFinishSignInForService:success:error:
+ _objc_msgSend$signInDelegate
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
- GCC_except_table21
- GCC_except_table26
- GCC_except_table32
- GCC_except_table33
- GCC_except_table38
- GCC_except_table43
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- ___69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.107
- ___69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.111
- ___69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke_2.109
- ___70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.113
- ___70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.115
- ___70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke_2.114
- ___84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.101
- ___84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.102
- ___84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.106
- ___block_descriptor_96_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s72l8s64l8
- ___block_literal_global.117
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "1"
+ "AACloudServiceOwner.bundle"
+ "AMSMediaServiceOwner.bundle"
+ "Bundle %@ does not support service type: %@"
+ "Bundle for service %@ is rejectionlisted, returning nil"
+ "Bundle not found: %@ in subpath: %@"
+ "Failed to load bundle (%@), error: %@"
+ "Found bundle: %@ at path: %@"
+ "GCCloudServiceOwner.bundle"
+ "IDSServiceOwner.bundle"
+ "Lazy load failed for service: %@, falling back to full load"
+ "No bundle mapping for service: %@, using full load"
+ "Non-conformant principal class for bundle: %@"
+ "Skipping rejectionlisted bundle: %@"
+ "Successfully loaded bundle: %@"
+ "Tier 1 lazy load requested for service: %@, bundle: %@"
+ "signInService: Lack reference to call _completeSignInSignpost."
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AASignInFlowControllerDelegate>\""
- "@\"<AASignOutFlowControllerDelegate>\""
- "@\"<AIDAAccountManagerDelegate>\""
- "@\"<AIDAServiceOwnerProtocol>\""
- "@\"<CDPStateUIProvider>\""
- "@\"AAFAnalyticsTransportRTC\""
- "@\"ACAccount\"24@0:8@\"NSString\"16"
- "@\"ACAccountStore\""
- "@\"NSArray\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSPersonNameComponents\"32@0:8@\"ACAccount\"16@\"NSString\"24"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"ACAccount\"16@\"NSString\"24"
- "@\"UIViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"ACAccountStore\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@36@0:8B16@20@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@52@0:8@16@24@32B40@44"
- "AIDAAccountManager"
- "AIDAAnalyticsReporterRTC"
- "AIDAMutableServiceContext"
- "AIDAServiceContext"
- "AIDAServiceOperationResult"
- "AIDAServiceOwnerProtocol"
- "AIDAServiceOwnersManager"
- "AppleIDAuthentication"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DSIDForAccount:service:"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<AASignInFlowControllerDelegate>\",&,N"
- "T@\"<AASignInFlowControllerDelegate>\",R,N,V_aaSignInFlowControllerDelegate"
- "T@\"<AASignOutFlowControllerDelegate>\",&,N"
- "T@\"<AASignOutFlowControllerDelegate>\",R,N,V_aaSignOutFlowControllerDelegate"
- "T@\"<AIDAAccountManagerDelegate>\",W,N,V_delegate"
- "T@\"<CDPStateUIProvider>\",R,W,N,V_cdpUiProvider"
- "T@\"<CDPStateUIProvider>\",W,N"
- "T@\"ACAccountStore\",R,N,V_accountStore"
- "T@\"NSArray\",R,C"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",C,N"
- "T@\"NSDictionary\",C,N,V_accounts"
- "T@\"NSDictionary\",C,N,V_serviceOwners"
- "T@\"NSDictionary\",R,C,N,V_authenticationResults"
- "T@\"NSDictionary\",R,N,V_signInContexts"
- "T@\"NSDictionary\",R,N,V_signOutContexts"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSMutableDictionary\",R,N,V__telemetryTimeSeries"
- "T@\"NSSet\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_type"
- "T@\"UIViewController\",&,N"
- "T@\"UIViewController\",R,N,V_viewController"
- "TB,N"
- "TB,R"
- "TB,R,N,V_shouldForceOperation"
- "TB,R,N,V_success"
- "TQ,R"
- "Tq,N"
- "Tq,R,N,V_operationUIPermissions"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "__telemetryTimeSeries"
- "_aaSignInFlowControllerDelegate"
- "_aaSignOutFlowControllerDelegate"
- "_accountManagerLock"
- "_accountStore"
- "_accountStoreChangeQueue"
- "_accountStoreDidChange:"
- "_accounts"
- "_authenticationResults"
- "_buildServiceOwnerMapping"
- "_cdpUiProvider"
- "_completeSignInSignpost:forService:context:success:error:"
- "_delegate"
- "_delegate_accountsForAccountManager"
- "_expirationCheckedTokenForCredential:"
- "_handlerByObserver"
- "_loadServiceOwnerBundles"
- "_loadServiceOwnerBundlesIfNeeded"
- "_operationUIPermissions"
- "_performSilentReauthForAccount:completionHandler:"
- "_postCloudSupportedServicesForAltDSID:"
- "_primaryiCloudAccount"
- "_publishSignInTelemetryEventForContext:"
- "_rejectionlistedBundleIDs"
- "_reporter"
- "_serviceOwners"
- "_serviceOwnersLock"
- "_serviceOwnersManager"
- "_set_loadServiceOwnerBundlesIfNeeded_onceToken:"
- "_sharedTelemetryReporter"
- "_shouldForceOperation"
- "_signInContexts"
- "_signOutContexts"
- "_supplementalServiceTypes"
- "_telemetryTimeSeries"
- "_viewController"
- "aaSignInFlowControllerDelegate"
- "aaSignOutFlowControllerDelegate"
- "aaf_map:"
- "accessInstanceVariablesDirectly"
- "accountForAuthenticationResults:accountManager:"
- "accountForService:"
- "accountPropertyForKey:"
- "accountStore"
- "accountTypeWithAccountTypeIdentifier:"
- "accounts"
- "accountsForAccountManager:"
- "accountsWithAccountType:"
- "addAccountChangeObserver:handler:"
- "addObserver:selector:name:object:"
- "aidaAccountForService:"
- "aida_AppleIDAuthenticationAccountType"
- "aida_AppleIDAuthenticationAccounts"
- "aida_accountForAltDSID:"
- "aida_accountForPrimaryiCloudAccount"
- "aida_accountForiCloudAccount:"
- "aida_alternateDSID"
- "aida_analyticsDurationEventForAIDAServiceType:accountManager:authenticationResults:"
- "aida_analyticsEventWithEventName:"
- "aida_analyticsEventWithEventName:accountManager:authenticationResults:"
- "aida_analyticsFinishEventForAIDAServiceType:accountManager:authenticationResults:success:error:"
- "aida_analyticsStartEventForAIDAServiceType:accountManager:authenticationResults:"
- "aida_deviceProvisioningInfo"
- "aida_dsid"
- "aida_errorWithCode:"
- "aida_errorWithCode:userInfo:"
- "aida_iCloudAccountMatchingAppleIDAuthAccount:"
- "aida_renewCredentialsForAccount:services:completion:"
- "aida_renewCredentialsForAccount:services:force:completion:"
- "aida_tokenForService:"
- "aida_tokenForService:completionHandler:"
- "aida_tokenWithExpirationCheck"
- "aida_tokenWithExpiryCheckForService:"
- "aida_updateEventWithSuccess:error:"
- "aida_updateTelemetryIdsWithAuthenticationResults:accountManager:"
- "allKeys"
- "allValues"
- "altDSIDForAccount:service:"
- "analyticsEventWithName:eventCategory:initData:"
- "analyticsReporterWithTransport:"
- "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
- "array"
- "authKitAccountWithAltDSID:error:"
- "authKitAccountWithDSID:"
- "authenticateWithContext:completion:"
- "authenticationResults"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "boolValue"
- "bundleIdentifier"
- "cdpUiProvider"
- "class"
- "code"
- "compare:"
- "configureProcessSpecificServiceOwnerRejectionlist:"
- "configureProcessSpecificSupplementalServiceTypes:"
- "conformsToProtocol:"
- "containsObject:"
- "contextWithContext:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credential"
- "credentialForAccount:serviceID:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultCenter"
- "defaultStore"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "doesNotRecognizeSelector:"
- "domain"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "eventNameForService:"
- "finishEventNameForService:"
- "hash"
- "init"
- "initWithAccountStore:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCoder:"
- "initWithEventName:eventCategory:initData:"
- "initWithSuccess:error:type:"
- "insertObject:atIndex:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isLoaded"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "loadAndReturnError:"
- "mainBundle"
- "mutableCopy"
- "mutableCopyWithZone:"
- "nameComponentsForAccount:service:"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "operationUIPermissions"
- "orderedSetWithArray:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginBundlesAtSubpath:"
- "populateUnderlyingErrorsStartingWithRootError:"
- "principalClass"
- "q"
- "q16@0:8"
- "release"
- "removeAccountChangeObserver:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "renewCredentialsForAccount:options:completion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scanUnsignedLongLong:"
- "scannerWithString:"
- "self"
- "sendEvent:"
- "serviceOwnerBundles"
- "serviceOwners"
- "setAaSignInFlowControllerDelegate:"
- "setAaSignOutFlowControllerDelegate:"
- "setAccounts:"
- "setAltDSID:"
- "setAuthenticationResults:"
- "setAuthenticationType:"
- "setCdpUiProvider:"
- "setDelegate:"
- "setIsUsernameEditable:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOperationUIPermissions:"
- "setServiceOwners:"
- "setServiceType:"
- "setShouldForceOperation:"
- "setShouldUpdatePersistentServiceTokens:"
- "setSignInContexts:"
- "setSignOutContexts:"
- "setViewController:"
- "sharedInstance"
- "sharedTelemetryReporter"
- "shouldForceOperation"
- "signInContexts"
- "signInService:withContext:completion:"
- "signInToAllServicesInBackground:usingContext:completion:"
- "signInToAllServicesInBackgroundUsingContext:completion:"
- "signInToServices:usingContext:completion:"
- "signOutContexts"
- "signOutOfAllServicesUsingContext:completion:"
- "signOutOfServices:usingContext:completion:"
- "signOutService:withContext:completion:"
- "startEventNameForService:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringValue"
- "stringWithFormat:"
- "success"
- "superclass"
- "supportedServices"
- "supportsSecureCoding"
- "telemetryDeviceSessionIDForAccount:"
- "token"
- "tokenExpiryDate"
- "type"
- "unionSet:"
- "username"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v28@0:8B16@20"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8B16@20@?28"
- "v40@0:8@\"NSString\"16@\"AIDAServiceContext\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v44@0:8@16@24B32@?36"
- "v60@0:8{?=QQ}16@32@40B48@52"
- "valueWithNonretainedObject:"
- "viewController"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
