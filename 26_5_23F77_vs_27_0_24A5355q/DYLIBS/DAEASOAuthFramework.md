## DAEASOAuthFramework

> `/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework`

```diff

-2074.80.2.0.0
-  __TEXT.__text: 0xd994
-  __TEXT.__auth_stubs: 0x490
+2075.0.0.0.0
+  __TEXT.__text: 0xcb70
   __TEXT.__objc_methlist: 0xc40
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x340
-  __TEXT.__cstring: 0xe36
+  __TEXT.__gcc_except_tab: 0x2a4
+  __TEXT.__cstring: 0xe4e
   __TEXT.__oslogstring: 0x167d
-  __TEXT.__unwind_info: 0x318
-  __TEXT.__objc_classname: 0x249
-  __TEXT.__objc_methname: 0x2a58
-  __TEXT.__objc_methtype: 0x4d1
-  __TEXT.__objc_stubs: 0x2240
-  __DATA_CONST.__got: 0x2f0
+  __TEXT.__unwind_info: 0x290
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4c0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0xb30
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x2f0
   __AUTH_CONST.__cfstring: 0x1620
   __AUTH_CONST.__objc_const: 0x1ed0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x280
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0D46589-3C2C-388C-8329-50E0704B8AED
+  UUID: D3D43612-A6F5-3942-A54D-6657486B20BA
   Functions: 243
-  Symbols:   1186
-  CStrings:  1016
+  Symbols:   1191
+  CStrings:  457
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
Functions:
~ +[DAEASOAuthTokenRequest claimsValueWithClaimsChallenge:] : 792 -> 756
~ +[DAEASOAuthTokenRequest urlRequestForTokenRequestURI:clientID:redirectURI:authCode:scope:codeVerifier:claims:] : 428 -> 460
~ +[DAEASOAuthTokenRequest oauthTokenRefreshRequestForTokenRequestURI:clientID:scope:refreshToken:claims:] : 360 -> 364
~ +[DAEASOAuthTokenRequest _urlRequestForTokenRequestURI:params:clientID:] : 716 -> 684
~ -[DAEASOAuthTokenResponse initWithData:urlResponse:error:] : 1400 -> 1260
~ -[DAEASOAuthTokenResponse usernameFromJWTToken:] : 588 -> 544
~ +[ESExchangeEmptyBearerRequest emptyBearerRequestForHost:] : 228 -> 220
~ -[ESExchangeEmptyBearerResponse initWithData:urlResponse:error:] : 824 -> 792
~ +[DAEASOpenIDMetadataRequest openIDrequestURLFor:] : 236 -> 224
~ -[DAEASOpenIDMetadataResponse initWithData:urlResponse:error:] : 1428 -> 1300
~ -[DAEASOAuthPKCEChallenge initWithCodeChallengeMethod:] : 200 -> 192
~ +[DAEASOAuthPKCEChallenge newCodeVerifier] : 180 -> 168
~ -[DAEASOAuthPKCEChallenge codeChallengeFromVerifier:withCodeChallengeMethod:] : 280 -> 268
~ +[DAEASOAuthPKCEChallenge base64URLEncode:] : 188 -> 172
~ -[DAEASOAuthPKCEChallenge setCodeVerifier:] : 64 -> 12
~ -[DAEASOAuthPKCEChallenge setCodeChallenge:] : 64 -> 12
~ -[ACAccount(AccountMigration) migrationStatus] : 128 -> 120
~ -[ACAccount(AccountMigration) setMigrationStatus:] : 108 -> 104
~ +[DAEASOAuthMigrationRequest urlRequestForOAuthTokenFromUsername:password:scope:] : 716 -> 672
~ +[DAEASExchangeOAuthMigrationRequest urlRequestForOAuthTokenFromUsername:tokenRequestURI:password:scope:] : 948 -> 912
~ -[DAEASOAuthTokenRefreshResponse initWithData:urlResponse:error:] : 1276 -> 1140
~ +[DAOAuthSafariViewController authenticationSessionWithURL:callbackURLScheme:handler:] : 408 -> 392
~ +[DAEASOAuthClient clientIDForOAuthType:] : 416 -> 424
~ +[DAEASOAuthClient defaultScopeForOAuthType:withResourceIdentifier:forToken:isOnPrem:] : 648 -> 624
~ +[DAEASOAuthClient clientRedirectForOAuthType:] : 180 -> 168
~ +[DAEASOAuthClient clientRedirectURLSchemeForOAuthType:] : 132 -> 124
~ -[DAEASOAuthJWTValidator init] : 112 -> 108
~ -[DAEASOAuthJWTValidator initWithIdToken:] : 920 -> 836
~ -[DAEASOAuthJWTValidator personalAccount] : 176 -> 160
~ -[DAEASOAuthJWTValidator idTokenValidWithJWKS:withAudience:withIssuer:] : 1408 -> 1308
~ -[DAEASOAuthJWTValidator _signatureValid:] : 1724 -> 1636
~ +[DAEASOAuthJWTValidator base64URLDecode:] : 464 -> 388
~ +[DAEASOAuthJWTValidator base64URLEncode:] : 360 -> 296
~ -[DAEASOAuthJWTValidator setRawHeader:] : 64 -> 12
~ -[DAEASOAuthJWTValidator setRawPayload:] : 64 -> 12
~ -[DAEASOAuthJWTValidator setRawSignature:] : 64 -> 12
~ -[DAEASOAuthJWTValidator setDecodedHeader:] : 64 -> 12
~ -[DAEASOAuthJWTValidator setDecodedPayload:] : 64 -> 12
~ -[DAEASOAuthJWTValidator setDecodedSignature:] : 64 -> 12
~ -[DAEASOAuthJWTValidator setHeaderJSONObject:] : 64 -> 12
~ -[DAEASOAuthJWTValidator setPayloadJSONObject:] : 64 -> 12
~ -[DAEASOAuthFlowController initWithOAuthType:authURI:username:accountId:claims:isOnPrem:] : 432 -> 428
~ -[DAEASOAuthFlowController authURLForUsername:originalAuthURL:] : 448 -> 428
~ -[DAEASOAuthFlowController onPremAuthURLForUsername:originalAuthURL:resource:] : 320 -> 304
~ -[DAEASOAuthFlowController requestForAuthURL:] : 84 -> 80
~ -[DAEASOAuthFlowController shouldHideWebViewForLoadWithRequest:] : 1052 -> 948
~ ___64-[DAEASOAuthFlowController shouldHideWebViewForLoadWithRequest:]_block_invoke : 304 -> 332
~ ___64-[DAEASOAuthFlowController shouldHideWebViewForLoadWithRequest:]_block_invoke_2 : 696 -> 664
~ -[DAEASOAuthFlowController _urlRequestForOAuthTokenFromAuthCode:codeVerifier:claims:] : 376 -> 352
~ -[DAEASOAuthFlowController exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:] : 680 -> 660
~ ___100-[DAEASOAuthFlowController exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:]_block_invoke : 512 -> 516
~ -[DAEASOAuthFlowController retrieveOpenIDMetadataFromURI:withCompletion:] : 188 -> 196
~ ___73-[DAEASOAuthFlowController retrieveOpenIDMetadataFromURI:withCompletion:]_block_invoke : 328 -> 304
~ ___73-[DAEASOAuthFlowController retrieveOpenIDMetadataFromURI:withCompletion:]_block_invoke_2 : 572 -> 500
~ -[DAEASOAuthFlowController retrieveJWKSDataFromURI:withCompletion:] : 188 -> 196
~ ___67-[DAEASOAuthFlowController retrieveJWKSDataFromURI:withCompletion:]_block_invoke : 348 -> 328
~ ___67-[DAEASOAuthFlowController retrieveJWKSDataFromURI:withCompletion:]_block_invoke_2 : 280 -> 232
~ ___101-[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:]_block_invoke : 308 -> 312
~ -[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensWithCompletion:] : 272 -> 296
~ ___90-[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensWithCompletion:]_block_invoke : 568 -> 496
~ ___90-[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensWithCompletion:]_block_invoke.60 : 1072 -> 1000
~ -[DAEASOAuthFlowController _assignConnectionPropertiesToSessionConfiguration:] : 104 -> 96
~ +[DAEASOAuthFlowController upgradeAuthorizationEndpoint:] : 364 -> 324
~ -[DAEASOAuthFlowController setState:] : 64 -> 12
~ -[DAEASOAuthFlowController setChallenge:] : 64 -> 12
~ -[DAEASOAuthFlowController setTokenRequestURI:] : 64 -> 12
~ -[DAEASOAuthFlowController setJwksURI:] : 64 -> 12
~ -[DAEASOAuthFlowController setJwksData:] : 64 -> 12
~ -[DAEASOAuthFlowController setIssuer:] : 64 -> 12
~ -[DAEASOAuthFlowController setClaimsChallenge:] : 64 -> 12
~ -[DAExchangeOAuthFlowController initWithAuthURI:easEndPoint:username:accountId:claims:isOnPrem:] : 320 -> 332
~ ___85-[DAExchangeOAuthFlowController exchangeAuthCode:codeVerifier:claims:withCompletion:]_block_invoke : 436 -> 424
~ -[DAEASOAuthMigrationActivity scheduleActivity] : 428 -> 400
~ -[DAEASOAuthMigrationActivity invalidateActivity] : 120 -> 112
~ -[DAEASOAuthMigrationActivity _retrieveMigrationStatusFromConfigurationURI:withCompletion:] : 204 -> 212
~ ___91-[DAEASOAuthMigrationActivity _retrieveMigrationStatusFromConfigurationURI:withCompletion:]_block_invoke : 312 -> 292
~ ___91-[DAEASOAuthMigrationActivity _retrieveMigrationStatusFromConfigurationURI:withCompletion:]_block_invoke_2 : 1012 -> 932
~ -[DAEASOAuthMigrationActivity _serverMigrationStatus] : 336 -> 332
~ ___53-[DAEASOAuthMigrationActivity _serverMigrationStatus]_block_invoke : 212 -> 216
~ +[DAEASOAuthMigrationActivity profileMigrationEnabled] : 264 -> 248
~ +[DAEASOAuthMigrationActivity profileMigrationDisabled] : 264 -> 248
~ -[DAEASOAuthMigrationActivity _isExchangeBasicAccount:] : 460 -> 392
~ -[DAEASOAuthMigrationActivity _sendAnalyticsForMigratingAccount:withStatus:] : 188 -> 196
~ ___76-[DAEASOAuthMigrationActivity _sendAnalyticsForMigratingAccount:withStatus:]_block_invoke : 192 -> 188
~ -[DAEASOAuthMigrationActivity _migrateExchangeAccountToOAuthDecision:disallowedDomains:disallowedHosts:] : 1580 -> 1556
~ ___55-[DAEASOAuthMigrationActivity _triggerAccountMigration]_block_invoke : 1360 -> 1300
~ ___55-[DAEASOAuthMigrationActivity _triggerAccountMigration]_block_invoke.95 : 248 -> 196
~ -[DAEASOAuthMigrationActivity setScheduler:] : 64 -> 12
~ -[DAEASOAuthWebViewController initWithAccountDescription:presentationBlock:] : 148 -> 152
~ -[DAEASOAuthWebViewController initWithAccount:isFirstTimeSetup:accountStore:presentationBlock:] : 208 -> 216
~ -[DAEASOAuthWebViewController initWithAccount:accountStore:authURI:accountType:userName:accountDescription:isFirstTimeSetup:presentationBlock:] : 276 -> 300
~ -[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:] : 1756 -> 1704
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke : 204 -> 216
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke_2 : 240 -> 192
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.24 : 240 -> 260
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke_2.25 : 240 -> 192
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.58 : 292 -> 260
~ -[DAEASOAuthWebViewController _didInstantiateRemoteViewController] : 900 -> 872
~ ___66-[DAEASOAuthWebViewController _didInstantiateRemoteViewController]_block_invoke : 92 -> 96
~ -[DAEASOAuthWebViewController loadView] : 160 -> 148
~ -[DAEASOAuthWebViewController _extensionRequestDidCancelWithError:] : 72 -> 20
~ -[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:] : 420 -> 412
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke_2 : 2416 -> 2368
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.76 : 712 -> 656
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.121 : 296 -> 248
~ -[DAEASOAuthWebViewController _dismissAndCompleteWithIdentity:error:extensionCompletion:] : 332 -> 344
~ +[DAEASOAuthWebViewController presentUsernameMismatchAlert] : 432 -> 404
~ +[DAEASOAuthWebViewController presentInternetOfflineError] : 480 -> 452
~ +[DAEASOAuthWebViewController presentSSLError] : 480 -> 452
~ +[DAEASOAuthWebViewController _presentAlertWithAlertParameters:] : 224 -> 220
~ -[DAEASOAuthWebViewController completion] : 16 -> 20
~ +[DAEASOAuthRequest urlForOAuthURI:clientID:redirectURI:scope:username:state:codeChallenge:codeChallengeMethod:] : 1048 -> 992
~ +[DAEASOAuthRequest urlForOnPremOAuthURI:clientID:redirectURI:username:state:resource:claims:] : 960 -> 892
~ +[DAEASOAuthRequest requestForURL:] : 80 -> 76
~ +[DAEASOAuthRequest urlPageWillContainAuthorizationCode:] : 72 -> 68
~ +[DAEASOAuthRequest authCodeFromRequest:] : 512 -> 492
~ +[DAEASOAuthRequest stateFromRequest:] : 512 -> 492
~ +[DAEASOAuthRequest errorDomainFromRequest:] : 572 -> 544
~ +[DAEASOAuthRequest errorDescriptionFromRequest:] : 572 -> 544
~ -[DAEASOAuthJWTValidator initWithIdToken:].cold.1 : 120 -> 116
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"ACAccount\""
- "@\"ACAccountStore\""
- "@\"DAEASOAuthPKCEChallenge\""
- "@\"NSBackgroundActivityScheduler\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSExtension\""
- "@\"NSMutableURLRequest\"24@0:8@\"NSURL\"16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\"24@0:8@\"NSString\"16"
- "@\"UIViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@28@0:8Q16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16q24"
- "@36@0:8Q16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8Q16@24B32B36"
- "@44@0:8@16B24@28@?36"
- "@48@0:8@16@24@32@40"
- "@56@0:8@16@24@32@40@48"
- "@60@0:8@16@24@32@40@48B56"
- "@60@0:8Q16@24@32@40@48B56"
- "@72@0:8@16@24@32@40@48@56@64"
- "@76@0:8@16@24@32Q40@48@56B64@?68"
- "@80@0:8@16@24@32@40@48@56@64q72"
- "@?"
- "@?16@0:8"
- "AccountMigration"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSURLRequest\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B40@0:8@\"UIWebView\"16@\"NSURLRequest\"24q32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24q32"
- "DAEASExchangeOAuthMigrationRequest"
- "DAEASOAuthClient"
- "DAEASOAuthFlowController"
- "DAEASOAuthIdentity"
- "DAEASOAuthJWTValidator"
- "DAEASOAuthMigrationActivity"
- "DAEASOAuthMigrationRequest"
- "DAEASOAuthPKCEChallenge"
- "DAEASOAuthRequest"
- "DAEASOAuthTokenRefreshResponse"
- "DAEASOAuthTokenRequest"
- "DAEASOAuthTokenResponse"
- "DAEASOAuthWebViewController"
- "DAEASOpenIDMetadataRequest"
- "DAEASOpenIDMetadataResponse"
- "DAExchangeOAuthFlowController"
- "DAOAuthSafariViewController"
- "ESExchangeEmptyBearerRequest"
- "ESExchangeEmptyBearerResponse"
- "HTTPBody"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "Q16@0:8"
- "Q40@0:8@16@24@32"
- "SL_OOPAuthFlowDelegate"
- "T#,R"
- "T@\"DAEASOAuthPKCEChallenge\",&,N,V_challenge"
- "T@\"NSBackgroundActivityScheduler\",&,N,V_scheduler"
- "T@\"NSData\",&,N,V_decodedHeader"
- "T@\"NSData\",&,N,V_decodedPayload"
- "T@\"NSData\",&,N,V_decodedSignature"
- "T@\"NSData\",&,N,V_jwksData"
- "T@\"NSData\",C,N,V_jwksData"
- "T@\"NSDate\",R,N,V_expiryDate"
- "T@\"NSDictionary\",R,N,V_data"
- "T@\"NSDictionary\",R,N,V_responseBody"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSString\",&,N,V_claimsChallenge"
- "T@\"NSString\",&,N,V_codeChallenge"
- "T@\"NSString\",&,N,V_codeVerifier"
- "T@\"NSString\",&,N,V_issuer"
- "T@\"NSString\",&,N,V_jwksURI"
- "T@\"NSString\",&,N,V_rawHeader"
- "T@\"NSString\",&,N,V_rawPayload"
- "T@\"NSString\",&,N,V_rawSignature"
- "T@\"NSString\",&,N,V_state"
- "T@\"NSString\",&,N,V_tokenRequestURI"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_accessToken"
- "T@\"NSString\",C,N,V_accountId"
- "T@\"NSString\",C,N,V_clientID"
- "T@\"NSString\",C,N,V_displayName"
- "T@\"NSString\",C,N,V_easEndPoint"
- "T@\"NSString\",C,N,V_issuer"
- "T@\"NSString\",C,N,V_jwksURI"
- "T@\"NSString\",C,N,V_oauthURI"
- "T@\"NSString\",C,N,V_redirectURI"
- "T@\"NSString\",C,N,V_refreshToken"
- "T@\"NSString\",C,N,V_tokenRequestURI"
- "T@\"NSString\",C,N,V_username"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_accessToken"
- "T@\"NSString\",R,N,V_authURI"
- "T@\"NSString\",R,N,V_authorizationURI"
- "T@\"NSString\",R,N,V_errorMessage"
- "T@\"NSString\",R,N,V_errorName"
- "T@\"NSString\",R,N,V_idToken"
- "T@\"NSString\",R,N,V_issuer"
- "T@\"NSString\",R,N,V_jwksURI"
- "T@\"NSString\",R,N,V_refreshToken"
- "T@\"NSString\",R,N,V_tokenRequestURI"
- "T@\"NSString\",R,N,V_user_id"
- "T@,&,N,V_headerJSONObject"
- "T@,&,N,V_payloadJSONObject"
- "T@?,C,N,V_completion"
- "TB,N,V_isOnPrem"
- "TQ,N,V_oauthType"
- "TQ,R"
- "Tq,N,V_codeChallengeMethod"
- "Tq,R,N,V_statusCode"
- "UIWebViewDelegate"
- "URL"
- "URLByAppendingPathComponent:"
- "URLByDeletingLastPathComponent"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessToken"
- "_account"
- "_accountDescription"
- "_accountId"
- "_accountStore"
- "_assignConnectionPropertiesToSessionConfiguration:"
- "_authURI"
- "_authorizationURI"
- "_challenge"
- "_claimsChallenge"
- "_clientID"
- "_codeChallenge"
- "_codeChallengeMethod"
- "_codeVerifier"
- "_commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:"
- "_completion"
- "_data"
- "_decodedHeader"
- "_decodedPayload"
- "_decodedSignature"
- "_defaultScopeWithDomainForOAuthType:"
- "_defaultScopeWithoutDomainForOAuthType:forToken:"
- "_didInstantiateRemoteViewController"
- "_dismissAndCompleteWithIdentity:error:extensionCompletion:"
- "_displayName"
- "_easEndPoint"
- "_error"
- "_errorMessage"
- "_errorName"
- "_exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:"
- "_exchangeAuthCode:codeVerifier:claims:forTokensWithCompletion:"
- "_expiryDate"
- "_extension"
- "_extensionCancellationError"
- "_extensionRequestDidCancelWithError:"
- "_extensionRequestDidComplete"
- "_extensionRequestDidCompleteWithTokens:extensionCompletion:"
- "_headerJSONObject"
- "_idToken"
- "_isExchangeBasicAccount:"
- "_isFirstTimeSetup"
- "_isOnPrem"
- "_issuer"
- "_jwksData"
- "_jwksURI"
- "_migrateExchangeAccountToOAuthDecision:disallowedDomains:disallowedHosts:"
- "_migrationDecisionString:"
- "_oauthType"
- "_oauthURI"
- "_payloadJSONObject"
- "_presentAlertWithAlertParameters:"
- "_presentationBlock"
- "_rawHeader"
- "_rawPayload"
- "_rawSignature"
- "_redirectURI"
- "_refreshToken"
- "_responseBody"
- "_retrieveMigrationStatusFromConfigurationURI:withCompletion:"
- "_scheduler"
- "_sendAnalyticsForMigratingAccount:withStatus:"
- "_serverMigrationStatus"
- "_serviceViewController"
- "_setNonAppInitiated:"
- "_signatureValid:"
- "_state"
- "_statusCode"
- "_tokenRequestURI"
- "_triggerAccountMigration"
- "_urlRequestForOAuthTokenFromAuthCode:codeVerifier:claims:"
- "_urlRequestForTokenRequestURI:params:clientID:"
- "_user_id"
- "_username"
- "absoluteString"
- "accountDescription"
- "accountType"
- "accountTypeWithAccountTypeIdentifier:"
- "accountsWithAccountType:"
- "activateConstraints:"
- "addChildViewController:"
- "addObject:"
- "addObjectsFromArray:"
- "addSubview:"
- "allKeys"
- "arrayByAddingObject:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "attachments"
- "authCodeFromRequest:"
- "authURLForUsername:"
- "authURLForUsername:originalAuthURL:"
- "authenticationSessionWithURL:callbackURLScheme:handler:"
- "authorizationURI"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "base64URLDecode:"
- "base64URLEncode:"
- "boolValue"
- "bringSubviewToFront:"
- "bundleForClass:"
- "bundleIdentifier"
- "bytes"
- "callbackWithCustomScheme:"
- "caseInsensitiveCompare:"
- "challenge"
- "claimsValueWithClaimsChallenge:"
- "class"
- "clearColor"
- "clientID"
- "clientIDForOAuthType:"
- "clientRedirect"
- "clientRedirectForOAuthType:"
- "clientRedirectURLSchemeForOAuthType:"
- "codeChallenge"
- "codeChallengeFromVerifier:withCodeChallengeMethod:"
- "codeChallengeMethod"
- "codeVerifier"
- "compare:options:"
- "completion"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "conformsToProtocol:"
- "constraintsWithVisualFormat:options:metrics:views:"
- "convertToString:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credentialForAccount:clientID:error:"
- "currentHandler"
- "currentLocale"
- "data"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceNow:"
- "debugDescription"
- "decodedHeader"
- "decodedPayload"
- "decodedSignature"
- "defaultScopeForOAuthType:withResourceIdentifier:forToken:isOnPrem:"
- "defaultScopeForOAuthType:withResourceIdentifier:isOnPrem:"
- "dictionaryRepresentation"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didMoveToParentViewController:"
- "dismissViewControllerAnimated:completion:"
- "domain"
- "doubleValue"
- "emptyBearerRequestForHost:"
- "ephemeralSessionConfiguration"
- "errorDescriptionFromRequest:"
- "errorDomainFromRequest:"
- "errorMessage"
- "errorName"
- "errorWithDomain:code:userInfo:"
- "exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:"
- "exchangeAuthCode:codeVerifier:claims:withCompletion:"
- "expiryDate"
- "extensionWithIdentifier:error:"
- "firstObject"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasPrefix:"
- "hasSuffix:"
- "hash"
- "headerJSONObject"
- "host"
- "idToken"
- "idTokenValidWithJWKS:withAudience:withIssuer:"
- "identifier"
- "init"
- "initWithAccount:accountStore:authURI:accountType:userName:accountDescription:isFirstTimeSetup:presentationBlock:"
- "initWithAccount:isFirstTimeSetup:accountStore:presentationBlock:"
- "initWithAccountDescription:presentationBlock:"
- "initWithArray:"
- "initWithAuthURI:easEndPoint:username:accountId:claims:isOnPrem:"
- "initWithBase64EncodedString:options:"
- "initWithBool:"
- "initWithCapacity:"
- "initWithCodeChallengeMethod:"
- "initWithData:encoding:"
- "initWithData:urlResponse:error:"
- "initWithDomain:code:userInfo:"
- "initWithIdToken:"
- "initWithIdentifier:"
- "initWithName:value:"
- "initWithNibName:bundle:"
- "initWithOAuth2Token:refreshToken:expiryDate:"
- "initWithOAuthType:authURI:username:accountId:claims:isOnPrem:"
- "initWithString:"
- "initWithTimeIntervalSinceNow:"
- "initWithURL:"
- "initWithURL:callback:completionHandler:"
- "initWithURL:callbackURLScheme:completionHandler:"
- "initialRedirectURL"
- "instantiateViewControllerWithInputItems:listenerEndpoint:connectionHandler:"
- "integerValue"
- "invalidate"
- "invalidateActivity"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isOnPrem"
- "isProxy"
- "lastPathComponent"
- "length"
- "loadItemForTypeIdentifier:options:completionHandler:"
- "loadView"
- "localeIdentifier"
- "localizedStringForKey:value:table:"
- "lowercaseString"
- "mainBundle"
- "managingOwnerIdentifier"
- "mf_isLegalEmailAddress"
- "migrationStatusString"
- "mutableBytes"
- "mutableCopy"
- "name"
- "newCodeVerifier"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "oauthRefreshToken"
- "oauthTokenRefreshRequestForTokenRequestURI:clientID:scope:refreshToken:claims:"
- "oauthType"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "onPremAuthURLForUsername:originalAuthURL:resource:"
- "openIDrequestURLFor:"
- "path"
- "payloadJSONObject"
- "percentEncodedQuery"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personalAccount"
- "presentInternetOfflineError"
- "presentSSLError"
- "presentUsernameMismatchAlert"
- "presentingViewController"
- "profileMigrationDisabled"
- "profileMigrationEnabled"
- "propertyListWithData:options:format:error:"
- "q"
- "q16@0:8"
- "queryItemWithName:value:"
- "queryItems"
- "rangeOfString:"
- "rawHeader"
- "rawPayload"
- "rawSignature"
- "redirectURI"
- "release"
- "reload"
- "renewCredentialsForAccount:options:completion:"
- "requestForAuthURL:"
- "requestForURL:"
- "requestWithURL:"
- "respondsToSelector:"
- "responseBody"
- "resume"
- "retain"
- "retainCount"
- "retrieveJWKSDataFromURI:withCompletion:"
- "retrieveOpenIDMetadataFromURI:withCompletion:"
- "saveAccount:withCompletionHandler:"
- "scheduleActivity"
- "scheduleWithBlock:"
- "scheduler"
- "scheme"
- "scopeForUpgradingFromBasicCreds"
- "self"
- "sessionWithConfiguration:"
- "setAccessToken:"
- "setAccountId:"
- "setAuthFlowCompletion:"
- "setBackgroundColor:"
- "setCachePolicy:"
- "setChallenge:"
- "setClaimsChallenge:"
- "setClientID:"
- "setCodeChallenge:"
- "setCodeChallengeMethod:"
- "setCodeVerifier:"
- "setCompletion:"
- "setCredential:"
- "setDecodedHeader:"
- "setDecodedPayload:"
- "setDecodedSignature:"
- "setDisplayName:"
- "setEasEndPoint:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHeaderJSONObject:"
- "setHost:"
- "setInterval:"
- "setIsOnPrem:"
- "setIssuer:"
- "setJwksData:"
- "setJwksURI:"
- "setMigrationStatus:"
- "setModalPresentationStyle:"
- "setNeedsLayout"
- "setOauthType:"
- "setOauthURI:"
- "setObject:forKeyedSubscript:"
- "setOpaque:"
- "setPath:"
- "setPayloadJSONObject:"
- "setQualityOfService:"
- "setQueryItems:"
- "setRawHeader:"
- "setRawPayload:"
- "setRawSignature:"
- "setRedirectURI:"
- "setRefreshToken:"
- "setRepeats:"
- "setRequestCancellationBlock:"
- "setScheduler:"
- "setScheme:"
- "setState:"
- "setTokenRequestURI:"
- "setTolerance:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUserInfo:"
- "setUsername:"
- "setValue:forHTTPHeaderField:"
- "setValue:forKey:"
- "setViewServiceTerminationBlock:"
- "setWithObjects:"
- "set_requestPostCompletionBlockWithItems:"
- "set_sourceApplicationBundleIdentifier:"
- "set_sourceApplicationSecondaryIdentifier:"
- "shouldDefer"
- "shouldHideWebViewForLoadWithRequest:"
- "sortedArrayUsingSelector:"
- "standardUserDefaults"
- "stateFromRequest:"
- "statusCode"
- "string"
- "stringByAddingPercentEscapesUsingEncoding:"
- "stringByAppendingString:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "timeIntervalSince1970"
- "timeIntervalSinceNow"
- "unarchivedObjectOfClasses:fromData:error:"
- "unsignedIntegerValue"
- "upgradeAuthorizationEndpoint:"
- "upgradeTokenEndpoint:"
- "urlForOAuthURI:clientID:redirectURI:scope:username:state:codeChallenge:codeChallengeMethod:"
- "urlForOnPremOAuthURI:clientID:redirectURI:username:state:resource:claims:"
- "urlPageWillContainAuthorizationCode:"
- "urlRequestForOAuthTokenFromUsername:password:scope:"
- "urlRequestForOAuthTokenFromUsername:tokenRequestURI:password:scope:"
- "urlRequestForTokenRequestURI:clientID:redirectURI:authCode:scope:codeVerifier:claims:"
- "user_id"
- "usernameFromJWTToken:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"UIWebView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@?<v@?@\"NSString\">>16"
- "v24@0:8@?<v@?B@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@\"UIWebView\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "value"
- "valueForHTTPHeaderField:"
- "valueForKey:"
- "view"
- "webView:didFailLoadWithError:"
- "webView:shouldStartLoadWithRequest:navigationType:"
- "webViewDidFinishLoad:"
- "webViewDidFinishLoadWithPageTitleSupplier:"
- "webViewDidStartLoad:"
- "whitespaceCharacterSet"
- "willMoveToParentViewController:"
- "zone"

```
