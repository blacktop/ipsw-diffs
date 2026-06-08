## DAAccountAuthenticator

> `/System/Library/Accounts/Authentication/DAAccountAuthenticator.bundle/DAAccountAuthenticator`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0x3374
-  __TEXT.__auth_stubs: 0x2f0
+2703.0.0.0.0
+  __TEXT.__text: 0x3008
   __TEXT.__objc_methlist: 0x2bc
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x253
+  __TEXT.__cstring: 0x255
   __TEXT.__oslogstring: 0x5fa
-  __TEXT.__unwind_info: 0xe8
-  __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0xc3a
-  __TEXT.__objc_methtype: 0x4cb
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0x198
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x2c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A69D60AA-6A92-3CD8-949E-5860CB1A06F9
+  UUID: 664AD1B9-F4EB-3423-9221-E3DB9E850AA4
   Functions: 33
-  Symbols:   107
-  CStrings:  234
+  Symbols:   109
+  CStrings:  63
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"ACAccountCredential\"32@0:8@\"ACAccount\"16@\"ACDClient\"24"
- "@\"ACAccountCredential\"40@0:8@\"ACAccount\"16@\"ACDClient\"24^@32"
- "@\"ACAccountCredential\"48@0:8@\"ACAccount\"16@\"ACDClient\"24@\"ACDAccountStore\"32^@40"
- "@\"NSArray\"40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32"
- "@\"NSMutableDictionary\""
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
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"ACAccount\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "DAAccountAuthenticator"
- "DAAccountDoNotSaveReason"
- "DAValidityCheckConsumer"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_acceptCertificatesIfNeededForOptions:"
- "_accountIDToAccount"
- "_accountIDToVerificationHandler"
- "_displayBadCredentialsAlertForAccount:clientName:reason:accountStore:resetAuthenticatedOnAlertFailure:handler:"
- "_handlePasswordNotification:response:callback:account:accountStore:resetAuthenticatedOnAlertFailure:"
- "_isExchangeOAuthAccount:"
- "_isTransientNetworkError:"
- "_needToAcceptCertificatesForOptions:"
- "_refreshTokenForAccount:store:completion:"
- "_renewCredentialsForAccount:accountStore:completion:"
- "_shouldUpgradeAccountToOAuth2:withCredential:"
- "account:isValid:validationError:"
- "accountType"
- "addObject:"
- "allKeys"
- "appIdsForPromptingForDAAccount:"
- "arrayWithObjects:"
- "autorelease"
- "backgroundThread"
- "backingAccountInfo"
- "boolValue"
- "bundleForClass:"
- "class"
- "client"
- "code"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "credentialType"
- "credentialWithPassword:"
- "currentHandler"
- "currentRunLoop"
- "daAccountSubclassWithBackingAccountInfo:"
- "daemonAppropriateAccountClassForACAccount:"
- "debugDescription"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "discoverInitialPropertiesWithConsumer:"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "domain"
- "enabledForDADataclass:"
- "errorWithDomain:code:userInfo:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasEntitlement:"
- "hash"
- "host"
- "identifier"
- "identityPersist"
- "init"
- "initWithBackingAccountInfo:"
- "initWithTarget:selector:object:"
- "invokeAndReleaseBlock:"
- "isAuthenticated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "length"
- "localizedAppName"
- "localizedInvalidPasswordMessage"
- "localizedStringForKey:value:table:"
- "mainPrincipal"
- "mobileCalDAVAccount"
- "oauthRefreshToken"
- "oauthToken"
- "objectForKeyedSubscript:"
- "parkBackgroundThread:"
- "password"
- "performSelector:"
- "performSelector:onThread:withObject:waitUntilDone:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentUUID"
- "port"
- "release"
- "removeObjectForKey:"
- "removePersistentCredentials"
- "renewCredentialsForAccount:accountStore:options:completion:"
- "renewCredentialsForAccount:accountStore:reason:completion:"
- "renewalIDForAccount:"
- "renewalIDsForAccount:accountStore:options:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "saveAccount:withHandler:"
- "scheduleInRunLoop:forMode:"
- "self"
- "setAllowsSpecificHTTPSCertificate:forHost:"
- "setAuthenticated:"
- "setCredential:"
- "setCredentialForAccount:"
- "setIsValidating:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setUsername:"
- "setWasUserInitiated:"
- "sharedInstance"
- "sharedKeychain"
- "showUserAlertWithTitle:message:cancelButtonTitle:otherButtonTitle:textFieldTitle:keyboardType:withCompletionBlock:"
- "showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:"
- "start"
- "stringWithFormat:"
- "superclass"
- "supportsPush"
- "username"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v36@0:8@\"DAAccount\"16B24@\"NSError\"28"
- "v36@0:8@16B24@28"
- "v40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@\"ACAccount\"16@\"ACDClient\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?@\"ACAccount\"@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSString\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v60@0:8@16@24@32@40B48@?52"
- "v60@0:8^{__CFUserNotification=}16Q24@?32@40@48B56"
- "v72@0:8@16@24@32@40@48@56@?64"
- "verifyCredentialsForAccount:accountStore:completion:"
- "verifyCredentialsForAccount:accountStore:options:completion:"
- "verifyCredentialsForAccount:client:withHandler:"
- "zone"

```
