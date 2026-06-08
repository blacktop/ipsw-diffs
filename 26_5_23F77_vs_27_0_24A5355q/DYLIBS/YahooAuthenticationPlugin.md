## YahooAuthenticationPlugin

> `/System/Library/Accounts/Authentication/YahooAuthenticationPlugin.bundle/YahooAuthenticationPlugin`

```diff

-772.0.0.0.0
-  __TEXT.__text: 0x3094
-  __TEXT.__auth_stubs: 0x300
+774.0.0.0.0
+  __TEXT.__text: 0x2d0c
   __TEXT.__objc_methlist: 0x23c
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x50

   __TEXT.__oslogstring: 0x4ef
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0xa2a
-  __TEXT.__objc_methtype: 0x419
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x158
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x350
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76EA13E9-0966-30C4-9050-F158D2AE2694
-  Functions: 43
-  Symbols:   97
-  CStrings:  206
+  UUID: 00AD9680-B4F6-3B02-9857-438A58CD688F
+  Functions: 42
+  Symbols:   101
+  CStrings:  59
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
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
- "SLYahooAuthenticationPlugin"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_displayBadCredentialsAlertForAccount:clientName:reason:accountStore:resetAuthenticatedOnAlertFailure:handler:"
- "_getLegacyTokenForAccount:password:username:"
- "_migrateLegacyToken:account:completion:"
- "_refreshTokenForAccount:store:completion:"
- "accessToken"
- "accountType"
- "accountTypeWithIdentifier:"
- "accountWithPersistentAccount:error:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "canReceiveNewMailNotifications"
- "class"
- "client"
- "clientID"
- "clientSecret"
- "code"
- "conformsToProtocol:"
- "copy"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "credentialItemForKey:"
- "currentHandler"
- "data"
- "dataTaskWithRequest:completionHandler:"
- "debugDescription"
- "defaultWorkspace"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "domain"
- "ephemeralSessionConfiguration"
- "error"
- "errorMessage"
- "errorWithDomain:code:userInfo:"
- "expiryDate"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasEntitlement:"
- "hasSuffix:"
- "hash"
- "identifier"
- "initWithAccountType:"
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
- "loginToken"
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
- "setAuthenticated:"
- "setCredential:"
- "setOauthRefreshToken:"
- "setObject:forKey:"
- "setUsername:"
- "showUserAlertWithTitle:message:cancelButtonTitle:otherButtonTitle:withCompletionBlock:"
- "source"
- "statusCode"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsAccountType:"
- "token"
- "tokenURL"
- "urlRequestForClientID:secret:refreshToken:tokenURL:"
- "urlRequestForLoginTokenFromUsername:password:src:"
- "urlRequestForOAuthTokenFromLoginToken:clientID:clientSecret:src:"
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
- "verifyCredentialsForAccount:options:completion:"
- "webClientForAccount:"
- "zone"

```
