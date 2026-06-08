## ESAccountAuthenticator

> `/System/Library/Accounts/Authentication/ESAccountAuthenticator.bundle/ESAccountAuthenticator`

```diff

-2074.80.2.0.0
-  __TEXT.__text: 0x71a4
-  __TEXT.__auth_stubs: 0x380
+2075.0.0.0.0
+  __TEXT.__text: 0x6a68
   __TEXT.__objc_methlist: 0x31c
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x148
-  __TEXT.__cstring: 0x57a
+  __TEXT.__gcc_except_tab: 0x110
+  __TEXT.__cstring: 0x57c
   __TEXT.__oslogstring: 0xd40
-  __TEXT.__unwind_info: 0x130
-  __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x123c
-  __TEXT.__objc_methtype: 0x504
-  __TEXT.__objc_stubs: 0x11c0
-  __DATA_CONST.__got: 0x2a8
+  __TEXT.__unwind_info: 0x138
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x300
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x598
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x5a0
   __AUTH_CONST.__objc_const: 0x2c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2C272B2-2DB7-317F-9C92-ABA1A0BFB4AF
+  UUID: D9ED38CA-4273-36E9-8780-ECDE6E310504
   Functions: 64
-  Symbols:   152
-  CStrings:  385
+  Symbols:   156
+  CStrings:  151
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
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
- "DAValidityCheckConsumer"
- "ESAccountAuthenticator"
- "NSObject"
- "Q16@0:8"
- "Q24@0:8@16"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URL"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accountIDToAccount"
- "_accountIDToVerificationHandler"
- "_accountOAuthVersion:"
- "_addPropertiesToAccount:oauthURI:tokenRequestURI:jwksURI:issuer:oauthVersion:jwksData:jwksDataCacheDate:"
- "_assignConnectionPropertiesToSessionConfiguration:withAccountId:"
- "_currentDateString"
- "_displayBadCredentialsAlertForAccount:clientName:reason:accountStore:resetAuthenticatedOnAlertFailure:handler:"
- "_displayMigrationPendingAlertForAccount:accountStore:handler:"
- "_handlePasswordNotification:response:callback:account:accountStore:resetAuthenticatedOnAlertFailure:"
- "_isExchangeBasicAccount:"
- "_isExchangeOAuthAccount:"
- "_isTransientNetworkError:"
- "_jwksDataCacheValidForAccount:"
- "_refreshTokenForAccount:store:completion:"
- "_renewCredentialsForAccount:accountStore:completion:"
- "_retrieveAuthURIForAccount:withHost:withCompletion:"
- "_retrieveJWKSDataForAccount:fromURI:withCompletion:"
- "_retrieveOpenIDMetadataForAccount:fromURI:withCompletion:"
- "_setNonAppInitiated:"
- "_shouldUpgradeAccountToOAuth2:withCredential:"
- "absoluteString"
- "accessToken"
- "account:isValid:validationError:"
- "accountType"
- "addObject:"
- "allHTTPHeaderFields"
- "appIdsForPromptingForDAAccount:"
- "arrayWithObjects:"
- "authURI"
- "autorelease"
- "backgroundThread"
- "backingAccountInfo"
- "boolValue"
- "bundleForClass:"
- "class"
- "client"
- "clientIDForOAuthType:"
- "code"
- "conformsToProtocol:"
- "copy"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "credentialType"
- "credentialWithPassword:"
- "currentHandler"
- "currentRunLoop"
- "daemonAppropriateAccountClassForACAccount:"
- "dataTaskWithRequest:completionHandler:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "debugDescription"
- "defaultScopeForOAuthType:withResourceIdentifier:isOnPrem:"
- "defaultWorkspace"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "discoverInitialPropertiesWithConsumer:"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "domain"
- "doubleValue"
- "emptyBearerRequestForHost:"
- "enabledForDADataclass:"
- "ephemeralSessionConfiguration"
- "error"
- "errorMessage"
- "errorName"
- "errorWithDomain:code:userInfo:"
- "expiryDate"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasEntitlement:"
- "hash"
- "host"
- "idToken"
- "idTokenValidWithJWKS:withAudience:withIssuer:"
- "identifier"
- "identityPersist"
- "init"
- "initWithBackingAccountInfo:"
- "initWithData:urlResponse:error:"
- "initWithIdToken:"
- "initWithOAuth2Token:refreshToken:expiryDate:"
- "initWithString:"
- "initWithTarget:selector:object:"
- "initWithURL:"
- "invokeAndReleaseBlock:"
- "isAuthenticated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "issuer"
- "jwksURI"
- "length"
- "localeWithLocaleIdentifier:"
- "localizedAppName"
- "localizedInvalidPasswordMessage"
- "localizedStringForKey:value:table:"
- "migrationStatus"
- "migrationStatusString"
- "mutableCopy"
- "numberWithDouble:"
- "oauthRefreshToken"
- "oauthToken"
- "oauthTokenRefreshRequestForTokenRequestURI:clientID:scope:refreshToken:claims:"
- "objectForKeyedSubscript:"
- "openIDrequestURLFor:"
- "openSensitiveURL:withOptions:"
- "parkBackgroundThread:"
- "password"
- "performSelector:"
- "performSelector:onThread:withObject:waitUntilDone:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentUUID"
- "port"
- "refreshToken"
- "release"
- "removeObjectForKey:"
- "removePersistentCredentials"
- "renewCredentialsForAccount:accountStore:options:completion:"
- "renewCredentialsForAccount:accountStore:reason:completion:"
- "renewalIDForAccount:"
- "renewalIDsForAccount:accountStore:options:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "saveAccount:withHandler:"
- "scheduleInRunLoop:forMode:"
- "scopeForUpgradingFromBasicCreds"
- "self"
- "sessionWithConfiguration:"
- "setAuthenticated:"
- "setCredential:"
- "setCredentialForAccount:"
- "setDateFormat:"
- "setHost:"
- "setIsValidating:"
- "setLocale:"
- "setMigrationStatus:"
- "setOauthRefreshToken:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setScheme:"
- "setTimeZone:"
- "setUsername:"
- "setWasUserInitiated:"
- "set_sourceApplicationBundleIdentifier:"
- "set_sourceApplicationSecondaryIdentifier:"
- "sharedInstance"
- "sharedKeychain"
- "showUserAlertWithTitle:message:cancelButtonTitle:otherButtonTitle:textFieldTitle:keyboardType:withCompletionBlock:"
- "showUserNotification:groupIdentifier:withCompletionBlock:"
- "start"
- "statusCode"
- "stringFromDate:"
- "stringWithFormat:"
- "superclass"
- "timeIntervalSince1970"
- "timeIntervalSinceNow"
- "timeZoneForSecondsFromGMT:"
- "tokenRequestURI"
- "unsignedIntegerValue"
- "upgradeAuthorizationEndpoint:"
- "upgradeTokenEndpoint:"
- "urlRequestForOAuthTokenFromUsername:password:scope:"
- "urlRequestForOAuthTokenFromUsername:tokenRequestURI:password:scope:"
- "username"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@24"
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
- "v80@0:8@16@24@32@40@48@56@64@72"
- "verifyCredentialsForAccount:accountStore:completion:"
- "verifyCredentialsForAccount:accountStore:options:completion:"
- "verifyCredentialsForAccount:client:withHandler:"
- "zone"

```
