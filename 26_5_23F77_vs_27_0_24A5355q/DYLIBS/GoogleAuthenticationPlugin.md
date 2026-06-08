## GoogleAuthenticationPlugin

> `/System/Library/Accounts/Authentication/GoogleAuthenticationPlugin.bundle/GoogleAuthenticationPlugin`

```diff

-772.0.0.0.0
-  __TEXT.__text: 0x26e0
-  __TEXT.__auth_stubs: 0x260
+774.0.0.0.0
+  __TEXT.__text: 0x23a4
   __TEXT.__objc_methlist: 0x24c
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0x1a4
   __TEXT.__oslogstring: 0x43d
   __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0x9d7
-  __TEXT.__objc_methtype: 0x419
-  __TEXT.__objc_stubs: 0x800
-  __DATA_CONST.__got: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x308
-  __AUTH_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84F4A780-7472-328F-B17B-05B9ACB5CBA1
-  Functions: 33
-  Symbols:   78
-  CStrings:  179
+  UUID: C36CCC6F-DE53-315C-AFC3-6A4735AE8466
+  Functions: 31
+  Symbols:   84
+  CStrings:  41
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
- "#16@0:8"
- "@\"ACAccountCredential\"32@0:8@\"ACAccount\"16@\"ACDClient\"24"
- "@\"ACAccountCredential\"40@0:8@\"ACAccount\"16@\"ACDClient\"24^@32"
- "@\"ACAccountCredential\"48@0:8@\"ACAccount\"16@\"ACDClient\"24@\"ACDAccountStore\"32^@40"
- "@\"NSArray\"40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32"
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
- "NSObject"
- "Q16@0:8"
- "SLGoogleAuthenticationPlugin"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_cancelButtonTitleForBadCredentialsAlert"
- "_displayBadCredentialsAlertForAccount:clientName:reason:accountStore:resetAuthenticatedOnAlertFailure:handler:"
- "_messageForBadCredentialsAlertWithReason:account:"
- "_migrateLegacyToken:account:password:completion:"
- "_otherButtonTitleForBadCredentialsAlert"
- "_refreshTokenForAccount:store:completion:"
- "_titleForBadCredentialsAlertForAccount:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "class"
- "client"
- "clientID"
- "clientRedirect"
- "clientSecret"
- "clientTokenForAccount:"
- "code"
- "conformsToProtocol:"
- "copy"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "credentialType"
- "dataTaskWithRequest:completionHandler:"
- "debugDescription"
- "defaultScope"
- "defaultWorkspace"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "domain"
- "ephemeralSessionConfiguration"
- "error"
- "errorWithDomain:code:userInfo:"
- "expiryDate"
- "grantedDataclasses"
- "hasEntitlement:"
- "hash"
- "identifier"
- "initWithData:urlResponse:error:"
- "initWithOAuth2Token:refreshToken:expiryDate:"
- "isAuthenticated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "localizedAppName"
- "localizedStringForKey:value:table:"
- "oauthRefreshToken"
- "oauthToken"
- "objectForKeyedSubscript:"
- "openSensitiveURL:withOptions:"
- "password"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "refreshToken"
- "release"
- "renewCredentialsForAccount:accountStore:options:completion:"
- "renewCredentialsForAccount:accountStore:reason:completion:"
- "renewalIDForAccount:"
- "renewalIDsForAccount:accountStore:options:"
- "resourceURL"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "saveAccount:withHandler:"
- "self"
- "sessionWithConfiguration:"
- "setAccountProperty:forKey:"
- "setAuthenticated:"
- "setCredential:"
- "setObject:forKey:"
- "showUserAlertWithTitle:message:cancelButtonTitle:otherButtonTitle:withCompletionBlock:"
- "statusCode"
- "stringWithFormat:"
- "superclass"
- "supportsAccountType:"
- "token"
- "tokenURL"
- "urlRequestForAuthCodeFromAuthToken:clientID:scope:"
- "urlRequestForAuthTokenFromLegacyClientToken:username:password:"
- "urlRequestForClientID:secret:redirectURI:authCode:tokenURL:codeVerifier:"
- "urlRequestForClientID:secret:refreshToken:tokenURL:"
- "username"
- "v40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@\"ACAccount\"16@\"ACDClient\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?@\"ACAccount\"@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSString\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "v60@0:8@16@24@32@40B48@?52"
- "verifyCredentialsForAccount:accountStore:completion:"
- "verifyCredentialsForAccount:accountStore:options:completion:"
- "verifyCredentialsForAccount:client:withHandler:"
- "zone"

```
