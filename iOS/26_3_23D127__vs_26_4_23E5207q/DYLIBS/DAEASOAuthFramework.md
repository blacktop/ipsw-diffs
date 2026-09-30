## DAEASOAuthFramework

> `/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework`

```diff

-2074.60.1.0.0
-  __TEXT.__text: 0xcea4
-  __TEXT.__auth_stubs: 0x4f0
+2074.80.2.0.0
+  __TEXT.__text: 0xd994
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_methlist: 0xc40
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__gcc_except_tab: 0x340
   __TEXT.__cstring: 0xe36
   __TEXT.__oslogstring: 0x167d
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__unwind_info: 0x318
   __TEXT.__objc_classname: 0x249
   __TEXT.__objc_methname: 0x2a58
   __TEXT.__objc_methtype: 0x4d1

   __DATA_CONST.__objc_selrefs: 0xb30
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__cfstring: 0x1620
   __AUTH_CONST.__objc_const: 0x1ed0
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 838554E9-520C-3307-997F-CC2D5AB90840
+  UUID: BF36BA4F-A4B4-3E1B-A1F5-07B545913DE5
   Functions: 243
-  Symbols:   1192
+  Symbols:   1186
   CStrings:  1016
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
Functions:
~ +[DAEASOAuthTokenRequest claimsValueWithClaimsChallenge:] : 752 -> 792
~ +[DAEASOAuthTokenRequest urlRequestForTokenRequestURI:clientID:redirectURI:authCode:scope:codeVerifier:claims:] : 460 -> 428
~ +[DAEASOAuthTokenRequest oauthTokenRefreshRequestForTokenRequestURI:clientID:scope:refreshToken:claims:] : 364 -> 360
~ +[DAEASOAuthTokenRequest _urlRequestForTokenRequestURI:params:clientID:] : 680 -> 716
~ -[DAEASOAuthTokenResponse initWithData:urlResponse:error:] : 1336 -> 1400
~ -[DAEASOAuthTokenResponse usernameFromJWTToken:] : 544 -> 588
~ +[ESExchangeEmptyBearerRequest emptyBearerRequestForHost:] : 220 -> 228
~ -[ESExchangeEmptyBearerResponse initWithData:urlResponse:error:] : 788 -> 824
~ +[DAEASOpenIDMetadataRequest openIDrequestURLFor:] : 224 -> 236
~ -[DAEASOpenIDMetadataResponse initWithData:urlResponse:error:] : 1368 -> 1428
~ -[DAEASOAuthPKCEChallenge initWithCodeChallengeMethod:] : 192 -> 200
~ +[DAEASOAuthPKCEChallenge newCodeVerifier] : 168 -> 180
~ -[DAEASOAuthPKCEChallenge codeChallengeFromVerifier:withCodeChallengeMethod:] : 268 -> 280
~ +[DAEASOAuthPKCEChallenge base64URLEncode:] : 172 -> 188
~ -[DAEASOAuthPKCEChallenge setCodeVerifier:] : 12 -> 64
~ -[DAEASOAuthPKCEChallenge setCodeChallenge:] : 12 -> 64
~ -[ACAccount(AccountMigration) migrationStatus] : 120 -> 128
~ -[ACAccount(AccountMigration) setMigrationStatus:] : 104 -> 108
~ +[DAEASOAuthMigrationRequest urlRequestForOAuthTokenFromUsername:password:scope:] : 672 -> 716
~ +[DAEASExchangeOAuthMigrationRequest urlRequestForOAuthTokenFromUsername:tokenRequestURI:password:scope:] : 912 -> 948
~ -[DAEASOAuthTokenRefreshResponse initWithData:urlResponse:error:] : 1208 -> 1276
~ +[DAOAuthSafariViewController authenticationSessionWithURL:callbackURLScheme:handler:] : 392 -> 408
~ +[DAEASOAuthClient defaultScopeForOAuthType:withResourceIdentifier:forToken:isOnPrem:] : 620 -> 648
~ +[DAEASOAuthClient clientRedirectForOAuthType:] : 168 -> 180
~ +[DAEASOAuthClient clientRedirectURLSchemeForOAuthType:] : 124 -> 132
~ -[DAEASOAuthJWTValidator init] : 108 -> 112
~ -[DAEASOAuthJWTValidator initWithIdToken:] : 880 -> 920
~ -[DAEASOAuthJWTValidator personalAccount] : 160 -> 176
~ -[DAEASOAuthJWTValidator idTokenValidWithJWKS:withAudience:withIssuer:] : 1352 -> 1408
~ -[DAEASOAuthJWTValidator _signatureValid:] : 1652 -> 1724
~ +[DAEASOAuthJWTValidator base64URLDecode:] : 432 -> 464
~ +[DAEASOAuthJWTValidator base64URLEncode:] : 340 -> 360
~ -[DAEASOAuthJWTValidator setRawHeader:] : 12 -> 64
~ -[DAEASOAuthJWTValidator setRawPayload:] : 12 -> 64
~ -[DAEASOAuthJWTValidator setRawSignature:] : 12 -> 64
~ -[DAEASOAuthJWTValidator setDecodedHeader:] : 12 -> 64
~ -[DAEASOAuthJWTValidator setDecodedPayload:] : 12 -> 64
~ -[DAEASOAuthJWTValidator setDecodedSignature:] : 12 -> 64
~ -[DAEASOAuthJWTValidator setHeaderJSONObject:] : 12 -> 64
~ -[DAEASOAuthJWTValidator setPayloadJSONObject:] : 12 -> 64
~ -[DAEASOAuthFlowController initWithOAuthType:authURI:username:accountId:claims:isOnPrem:] : 428 -> 432
~ -[DAEASOAuthFlowController authURLForUsername:originalAuthURL:] : 428 -> 448
~ -[DAEASOAuthFlowController onPremAuthURLForUsername:originalAuthURL:resource:] : 304 -> 320
~ -[DAEASOAuthFlowController requestForAuthURL:] : 80 -> 84
~ -[DAEASOAuthFlowController shouldHideWebViewForLoadWithRequest:] : 992 -> 1052
~ ___64-[DAEASOAuthFlowController shouldHideWebViewForLoadWithRequest:]_block_invoke : 332 -> 304
~ ___64-[DAEASOAuthFlowController shouldHideWebViewForLoadWithRequest:]_block_invoke_2 : 664 -> 696
~ -[DAEASOAuthFlowController _urlRequestForOAuthTokenFromAuthCode:codeVerifier:claims:] : 352 -> 376
~ -[DAEASOAuthFlowController exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:] : 660 -> 680
~ ___100-[DAEASOAuthFlowController exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:]_block_invoke : 532 -> 512
~ -[DAEASOAuthFlowController retrieveOpenIDMetadataFromURI:withCompletion:] : 196 -> 188
~ ___73-[DAEASOAuthFlowController retrieveOpenIDMetadataFromURI:withCompletion:]_block_invoke : 304 -> 328
~ ___73-[DAEASOAuthFlowController retrieveOpenIDMetadataFromURI:withCompletion:]_block_invoke_2 : 544 -> 572
~ -[DAEASOAuthFlowController retrieveJWKSDataFromURI:withCompletion:] : 196 -> 188
~ ___67-[DAEASOAuthFlowController retrieveJWKSDataFromURI:withCompletion:]_block_invoke : 328 -> 348
~ ___67-[DAEASOAuthFlowController retrieveJWKSDataFromURI:withCompletion:]_block_invoke_2 : 276 -> 280
~ ___101-[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensAndUsernameWithCompletion:]_block_invoke : 312 -> 308
~ -[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensWithCompletion:] : 296 -> 272
~ ___90-[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensWithCompletion:]_block_invoke : 540 -> 568
~ ___90-[DAEASOAuthFlowController _exchangeAuthCode:codeVerifier:claims:forTokensWithCompletion:]_block_invoke.60 : 1000 -> 1072
~ -[DAEASOAuthFlowController _assignConnectionPropertiesToSessionConfiguration:] : 96 -> 104
~ +[DAEASOAuthFlowController upgradeAuthorizationEndpoint:] : 324 -> 364
~ -[DAEASOAuthFlowController setState:] : 12 -> 64
~ -[DAEASOAuthFlowController setChallenge:] : 12 -> 64
~ -[DAEASOAuthFlowController setTokenRequestURI:] : 12 -> 64
~ -[DAEASOAuthFlowController setJwksURI:] : 12 -> 64
~ -[DAEASOAuthFlowController setJwksData:] : 12 -> 64
~ -[DAEASOAuthFlowController setIssuer:] : 12 -> 64
~ -[DAEASOAuthFlowController setClaimsChallenge:] : 12 -> 64
~ -[DAExchangeOAuthFlowController initWithAuthURI:easEndPoint:username:accountId:claims:isOnPrem:] : 332 -> 320
~ ___85-[DAExchangeOAuthFlowController exchangeAuthCode:codeVerifier:claims:withCompletion:]_block_invoke : 424 -> 436
~ -[DAEASOAuthMigrationActivity scheduleActivity] : 400 -> 428
~ -[DAEASOAuthMigrationActivity invalidateActivity] : 112 -> 120
~ -[DAEASOAuthMigrationActivity _retrieveMigrationStatusFromConfigurationURI:withCompletion:] : 212 -> 204
~ ___91-[DAEASOAuthMigrationActivity _retrieveMigrationStatusFromConfigurationURI:withCompletion:]_block_invoke : 292 -> 312
~ ___91-[DAEASOAuthMigrationActivity _retrieveMigrationStatusFromConfigurationURI:withCompletion:]_block_invoke_2 : 976 -> 1012
~ -[DAEASOAuthMigrationActivity _serverMigrationStatus] : 332 -> 336
~ ___53-[DAEASOAuthMigrationActivity _serverMigrationStatus]_block_invoke : 216 -> 212
~ +[DAEASOAuthMigrationActivity profileMigrationEnabled] : 248 -> 264
~ +[DAEASOAuthMigrationActivity profileMigrationDisabled] : 248 -> 264
~ -[DAEASOAuthMigrationActivity _isExchangeBasicAccount:] : 436 -> 460
~ -[DAEASOAuthMigrationActivity _sendAnalyticsForMigratingAccount:withStatus:] : 196 -> 188
~ ___76-[DAEASOAuthMigrationActivity _sendAnalyticsForMigratingAccount:withStatus:]_block_invoke : 188 -> 192
~ -[DAEASOAuthMigrationActivity _migrateExchangeAccountToOAuthDecision:disallowedDomains:disallowedHosts:] : 1568 -> 1580
~ ___55-[DAEASOAuthMigrationActivity _triggerAccountMigration]_block_invoke : 1296 -> 1360
~ ___55-[DAEASOAuthMigrationActivity _triggerAccountMigration]_block_invoke.95 : 240 -> 248
~ -[DAEASOAuthMigrationActivity setScheduler:] : 12 -> 64
~ -[DAEASOAuthWebViewController initWithAccountDescription:presentationBlock:] : 152 -> 148
~ -[DAEASOAuthWebViewController initWithAccount:isFirstTimeSetup:accountStore:presentationBlock:] : 212 -> 208
~ -[DAEASOAuthWebViewController initWithAccount:accountStore:authURI:accountType:userName:accountDescription:isFirstTimeSetup:presentationBlock:] : 292 -> 276
~ -[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:] : 1688 -> 1756
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke : 216 -> 204
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke_2 : 236 -> 240
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.24 : 260 -> 240
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke_2.25 : 236 -> 240
~ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.58 : 300 -> 292
~ -[DAEASOAuthWebViewController _didInstantiateRemoteViewController] : 852 -> 900
~ -[DAEASOAuthWebViewController loadView] : 148 -> 160
~ -[DAEASOAuthWebViewController _extensionRequestDidCancelWithError:] : 20 -> 72
~ -[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:] : 408 -> 420
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke : 288 -> 296
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke_2 : 2348 -> 2416
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.76 : 700 -> 712
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.121 : 292 -> 296
~ -[DAEASOAuthWebViewController _dismissAndCompleteWithIdentity:error:extensionCompletion:] : 344 -> 332
~ ___89-[DAEASOAuthWebViewController _dismissAndCompleteWithIdentity:error:extensionCompletion:]_block_invoke : 204 -> 208
~ +[DAEASOAuthWebViewController presentUsernameMismatchAlert] : 404 -> 432
~ +[DAEASOAuthWebViewController presentInternetOfflineError] : 452 -> 480
~ +[DAEASOAuthWebViewController presentSSLError] : 452 -> 480
~ +[DAEASOAuthWebViewController _presentAlertWithAlertParameters:] : 220 -> 224
~ +[DAEASOAuthRequest urlForOAuthURI:clientID:redirectURI:scope:username:state:codeChallenge:codeChallengeMethod:] : 992 -> 1048
~ +[DAEASOAuthRequest urlForOnPremOAuthURI:clientID:redirectURI:username:state:resource:claims:] : 892 -> 960
~ +[DAEASOAuthRequest requestForURL:] : 76 -> 80
~ +[DAEASOAuthRequest urlPageWillContainAuthorizationCode:] : 68 -> 72
~ +[DAEASOAuthRequest authCodeFromRequest:] : 488 -> 512
~ +[DAEASOAuthRequest stateFromRequest:] : 488 -> 512
~ +[DAEASOAuthRequest errorDomainFromRequest:] : 540 -> 572
~ +[DAEASOAuthRequest errorDescriptionFromRequest:] : 540 -> 572
~ -[DAEASOAuthJWTValidator initWithIdToken:].cold.1 : 116 -> 120

```
