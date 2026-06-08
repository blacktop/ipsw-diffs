## AppleIDAuthentication

> `/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication`

```diff

-1037.575.5.0.0
-  __TEXT.__text: 0xb578
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x444
+1059.1.1.0.0
+  __TEXT.__text: 0x9cd8
+  __TEXT.__objc_methlist: 0x404
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x1a0
-  __TEXT.__cstring: 0x762
-  __TEXT.__oslogstring: 0x291b
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__cstring: 0x6c9
+  __TEXT.__oslogstring: 0x2542
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x1a18
-  __TEXT.__objc_methtype: 0x5e4
-  __TEXT.__objc_stubs: 0x1820
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x6b0
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x740
+  __DATA_CONST.__objc_selrefs: 0x6d8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x280
+  __DATA_CONST.__objc_arraydata: 0x90
+  __DATA_CONST.__got: 0x288
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x5e0
-  __AUTH_CONST.__objc_const: 0x468
+  __AUTH_CONST.__cfstring: 0x560
+  __AUTH_CONST.__objc_const: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x120
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F662F8B-B19D-3FAE-82EE-BE00D6EF75EC
-  Functions: 121
-  Symbols:   180
-  CStrings:  554
+  UUID: 229BBC2B-2A2E-3798-9861-CFDE4C152D47
+  Functions: 111
+  Symbols:   168
+  CStrings:  234
 
Symbols:
+ _OBJC_CLASS_$_AAAccountServiceController
+ _OBJC_CLASS_$_AACompanionDeviceHelper
+ _OBJC_CLASS_$_AAGrayModeHelper
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x8
- _CFUserNotificationCancel
- _CFUserNotificationCreate
- _OBJC_CLASS_$_AARequester
- _OBJC_CLASS_$_AAUpdateProvisioningRequest
- _OBJC_CLASS_$_AppleIDAuthenticationUtil
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_METACLASS_$_AppleIDAuthenticationUtil
- __dispatch_main_q
- __dispatch_source_type_timer
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _dispatch_time
- _kACIDServiceCommandPromptUser
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlertTopMostKey
- _kCFUserNotificationDefaultButtonTitleKey
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "appleaccountd"
- ""
- "#16@0:8"
- ".cxx_destruct"
- "@\"AAFollowUpController\""
- "@\"ACAccountCredential\"32@0:8@\"ACAccount\"16@\"ACDClient\"24"
- "@\"ACAccountCredential\"40@0:8@\"ACAccount\"16@\"ACDClient\"24^@32"
- "@\"ACAccountCredential\"48@0:8@\"ACAccount\"16@\"ACDClient\"24@\"ACDAccountStore\"32^@40"
- "@\"AKAppleIDAuthenticationController\""
- "@\"NSArray\"40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32"
- "@\"NSMutableSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"ACAccount\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32^@40"
- "ACDAccountAuthenticationPlugin"
- "ACRemoteDeviceProxy reports that renewCredentials succeeded, but no password is in the response!"
- "ACRemoteDeviceProxy reports that renewCredentials succeeded, but response is not a string! %@"
- "ACRemoteDeviceProxy successfully provided us with a password for %@"
- "AKAppleIDAuthenticationDelegate"
- "AppleIDAuthenticationPlugin"
- "AppleIDAuthenticationUtil"
- "AppleIDTokenMigrator"
- "Asking ACRemoteDeviceProxy to obtain password for account %@ with options: %@"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"ACAccount\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B48@0:8@\"AKAppleIDAuthenticationController\"16@\"NSMutableDictionary\"24@\"NSError\"32@\"AKAppleIDAuthenticationContext\"40"
- "B48@0:8@16@24@32@40"
- "CFUserNotificationCreate in renewCredentials!"
- "Can't get password from companion, told to avoid UI"
- "Dismissing renew-credentials prompt."
- "Failed to encode AKDevice! Proxied auth is doomed."
- "Failed to obtain a password from ACRemoteDeviceProxy for account %@! Error: %@"
- "Failed to save account after marking it as not in grey mode anymore. %@"
- "Got an error, may still be in Grey Mode. %@"
- "Localizable"
- "Make a quick round-trip to the server to see if we really need to accept new terms"
- "NSObject"
- "PASSWORD_ENTRY_DISMISS_BUTTON"
- "PASSWORD_ENTRY_REQUIRED_MESSAGE"
- "PASSWORD_ENTRY_REQUIRED_TITLE"
- "Q16@0:8"
- "Server auth was successful, not in Grey Mode anymore"
- "Showing renew-credentials prompt..."
- "Something went wrong and we couldn't contact the server. %@"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_idmsDataToken"
- "T@\"NSString\",C,N,V_passwordlessToken"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "We timed out waiting on the server"
- "^{_NSZone=}16@0:8"
- "^{__CFDictionary=}32@0:8@16@24"
- "_aa_clearRawPassword"
- "_aa_rawPassword"
- "_aa_setRawPassword:"
- "_accountTypeIDsThatReplacedAppleIDAccountType"
- "_accountsAwaitingRemotePasswordEntry"
- "_authController"
- "_authenticateAccount:inStore:options:errorMessage:completion:"
- "_beginPETBasedLoginWithAccount:PET:store:completion:"
- "_clientHasEntitlement:"
- "_convertPasswordToPETForAppleID:altDSID:password:services:completion:"
- "_fetchTokenForAccount:accountStore:forceFetch:withHandler:"
- "_fetchTokenForAccount:accountStore:withHandler:"
- "_findAndRemoveOldFMIPTokenForAccount:"
- "_findAndRemoveOldiCloudTokenForAccount:"
- "_followUpController"
- "_frontmostApplicationId"
- "_getPasswordFromCompanionForAccount:store:options:completion:"
- "_grayModeWhitelist"
- "_handleAuthenticationResults:error:forAccount:inStore:resetAuthenticatedOnAlertFailure:context:completion:"
- "_handleDelegatesResponseForAccount:store:response:error:handler:"
- "_handleRenewFailure:forAccount:accountStore:options:completion:"
- "_idmsDataToken"
- "_invokeDelegatesWithAuthenticationResponse:password:store:account:completion:"
- "_isAccountInGrayMode:"
- "_isAccountReallyInGreyMode:accountStore:completion:"
- "_isProxiedAuthenticationWithContext:"
- "_loginDelegatesParameters"
- "_loginWithAccount:store:companionDevice:options:completion:"
- "_migrateAppleIDTokensIfNeededForAccount:credential:store:"
- "_migrateFMIPTokenIfNeededForAccount:credential:"
- "_migrateiCloudTokenIfNeededForAccount:credential:"
- "_mostRecentTokenWithServiceName:matchingAccountNames:"
- "_newKeychainQueryForAllItemsMatchingAccountName:serviceName:"
- "_parametersForIDSAlertFromLoginResponse:"
- "_parametersForProxiedAuthentication"
- "_passwordlessToken"
- "_performLoginDelegatesRequestForAccount:store:handler:"
- "_potentialServiceNamesForTokenOfAccount:"
- "_removeKeychainItemForUsernames:services:"
- "_renewCredentialsForAccount:accountStore:options:errorMessage:completion:"
- "_setPassword:"
- "_setProxiedAppBundleID:"
- "_setProxiedAppName:"
- "_setProxyingForApp:"
- "_silentlyAuthenticateAppleID:altDSID:companionDevice:services:completion:"
- "_tryPasswordLoginWithAccount:store:services:completion:"
- "_updateDSID:withRawPassword:suggestedAccount:store:completion:"
- "_validateAuthenticationResults:error:forContext:completion:"
- "aa_altDSID"
- "aa_appleAccountWithPersonID:"
- "aa_errorWithCode:underlyingError:"
- "aa_isAARecoverableError"
- "aa_isSuspended"
- "aa_isXPCError"
- "aa_loginAndUpdateiCloudAccount:delegateParams:withCompletion:"
- "aa_loginAndUpdateiCloudAccount:withCompletion:"
- "aa_personID"
- "aa_registerAppleAccountWithHSA:completion:"
- "aa_setNeedsToVerifyTerms:"
- "aa_setPassword:"
- "aa_updatePropertiesForAppleAccount:options:completion:"
- "aa_updateWithProvisioningResponse:"
- "aaf_isSubsetOfArray:"
- "accountPropertyForKey:"
- "accountType"
- "accountTypeDescription"
- "addEntriesFromDictionary:"
- "addObject:"
- "addOperation:"
- "addProvisioningInfoToAARequest:"
- "ak_isAuthenticationErrorWithCode:"
- "ak_isServiceError"
- "ak_isUnableToPromptError"
- "ak_isUserCancelError"
- "allKeys"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "authenticateWithContext:completion:"
- "authenticationController:shouldContinueWithAuthenticationResults:error:forContext:"
- "authenticationController:shouldContinueWithAuthenticationResults:error:forContext:completion:"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "bundleID"
- "cancelAllOperations"
- "class"
- "client"
- "clientInfo"
- "code"
- "compare:"
- "conformsToProtocol:"
- "containsObject:"
- "convertToLoginDelegatesResponse"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:"
- "credentialForAccount:clientID:error:"
- "credentialItemForKey:"
- "credentialWithPassword:"
- "currentDevice"
- "currentHandler"
- "data"
- "debugDescription"
- "delegateServiceIdentifier"
- "description"
- "deviceWithSerializedData:"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveAuthenticationResponseParameters:accountStore:account:completion:"
- "didReceiveAuthenticationResponseParameters:accountStore:completion:"
- "dirtyProperties"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "doesRelyOnCompanionAccounts"
- "error"
- "errorWithDomain:code:userInfo:"
- "fetchCachedLoginResponseForAccount:completion:"
- "findMyiPhoneToken"
- "followUpPostAnalyticsInfoWithContext:identifier:error:"
- "handleAuthenticationError:resetAuthenticatedOnAlertFailure:forAccount:inStore:completion:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasEntitlement:"
- "hash"
- "httpResponse"
- "identifier"
- "idmsDataToken"
- "init"
- "initWithAccount:parameters:"
- "initWithAccount:token:"
- "initWithArray:"
- "initWithDSID:"
- "initWithData:encoding:"
- "initWithHTTPResponse:data:mediaType:"
- "initWithRequest:handler:"
- "intValue"
- "integerValue"
- "isAuthenticated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "lastObject"
- "localizedStringForKey:value:table:"
- "longLongValue"
- "mediaType"
- "migrateAppleIDBasedCredentialForAccount:"
- "mutableCopy"
- "name"
- "needsLostModeExitAuth"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectID"
- "parentAccount"
- "passwordForServiceName:username:accessGroup:"
- "passwordlessToken"
- "performRequestWithHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginBundlesAtSubpath:"
- "postFollowUpWithIdentifier:forAccount:userInfo:completion:"
- "principalClass"
- "proxiedDevice"
- "refresh"
- "release"
- "remoteDeviceProxy"
- "removeObject:"
- "removePasswordForService:username:accessGroup:"
- "renewCredentialsForAccount:accountStore:options:completion:"
- "renewCredentialsForAccount:accountStore:reason:completion:"
- "renewalIDForAccount:"
- "renewalIDsForAccount:accountStore:options:"
- "respondsToSelector:"
- "responseParameters"
- "responseParametersForServiceIdentifier:"
- "retain"
- "retainCount"
- "saveAccount:withHandler:"
- "saveVerifiedAccount:withCompletionHandler:"
- "self"
- "sendCommand:withAccount:options:completion:"
- "serializedData"
- "serviceType"
- "setAccountProperty:forKey:"
- "setAltDSID:"
- "setAnalyticsInfo:"
- "setAnticipateEscrowAttempt:"
- "setAuthenticated:"
- "setAuthenticationType:"
- "setClientInfo:"
- "setCompanionDevice:"
- "setCredential:"
- "setCredentialForAccount:"
- "setCredentialForAccount:error:"
- "setDSID:"
- "setFindMyiPhoneToken:"
- "setIdmsDataToken:"
- "setIsUsernameEditable:"
- "setLinkType:"
- "setObject:forKey:"
- "setPassword:"
- "setPasswordlessToken:"
- "setProxiedDevice:"
- "setReason:"
- "setServerFriendlyDescription:"
- "setServiceIdentifiers:"
- "setServiceType:"
- "setShouldUpdatePersistentServiceTokens:"
- "setToken:"
- "setUniqueDeviceIdentifier:"
- "setUsername:"
- "sharedInstance"
- "shortDebugName"
- "shouldUseUnifiedLoginEndpoint"
- "sortedArrayUsingComparator:"
- "statusMessage"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "userInfo"
- "username"
- "v16@0:8"
- "v16@?0@\"AAResponse\"8"
- "v24@0:8@16"
- "v28@?0B8@\"NSObject<NSCoding>\"12@\"NSError\"20"
- "v32@0:8@16@24"
- "v40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@\"ACAccount\"16@\"ACDClient\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16^@24@32"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?@\"ACAccount\"@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSString\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"AKAppleIDAuthenticationController\"16@\"NSMutableDictionary\"24@\"NSError\"32@\"AKAppleIDAuthenticationContext\"40@?<v@?B>48"
- "v56@0:8@16@24@32@40@?48"
- "v68@0:8@16@24@32@40B48@52@?60"
- "verifyCredentialsForAccount:accountStore:completion:"
- "verifyCredentialsForAccount:accountStore:options:completion:"
- "verifyCredentialsForAccount:client:withHandler:"
- "zone"

```
