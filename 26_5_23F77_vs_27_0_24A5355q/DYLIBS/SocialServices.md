## SocialServices

> `/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices`

```diff

-772.0.0.0.0
-  __TEXT.__text: 0x2a20
-  __TEXT.__auth_stubs: 0x2b0
+774.0.0.0.0
+  __TEXT.__text: 0x2908
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x5c1
+  __TEXT.__cstring: 0x5c3
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0xa65
-  __TEXT.__objc_methtype: 0x174
-  __TEXT.__objc_stubs: 0x900
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2b8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x178
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x14
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8FDB122-DABB-3A34-9D1E-3993CF92E0F8
+  UUID: 9F7FCE19-6F05-3678-BCBC-11C28D547D49
   Functions: 41
-  Symbols:   261
-  CStrings:  192
+  Symbols:   265
+  CStrings:  76
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x8
- _objc_release_x10
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
Functions:
~ -[ACAccountStore(SLGoogle) sl_openGoogleAuthenticationSheetWithAccountDescription:completion:] : 260 -> 264
~ ___94-[ACAccountStore(SLGoogle) sl_openGoogleAuthenticationSheetWithAccountDescription:completion:]_block_invoke : 232 -> 220
~ -[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithAccountDescription:completion:] : 268 -> 272
~ ___95-[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithAccountDescription:completion:]_block_invoke : 276 -> 260
~ -[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithUsername:accountDescription:completion:] : 292 -> 308
~ ___104-[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithUsername:accountDescription:completion:]_block_invoke : 276 -> 260
~ -[ACAccountStore(SLGoogle) sl_openGoogleAuthenticationSheetForAccount:shouldConfirm:delegateClassName:completion:] : 264 -> 268
~ -[SLGoogleAuthController _webClient] : 76 -> 80
~ +[SLGoogleAuthController googleAuthControllerWithPresentationBlock:completion:] : 136 -> 140
~ +[SLGoogleAuthController googleAuthControllerWithAccount:accountStore:presentationBlock:completion:] : 168 -> 180
~ +[SLGoogleAuthController googleAuthControllerWithYouTubeUsername:presentationBlock:completion:] : 148 -> 156
~ -[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:] : 1044 -> 1020
~ ___121-[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:]_block_invoke : 324 -> 332
~ ___121-[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:]_block_invoke_2 : 524 -> 508
~ ___121-[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:]_block_invoke.27 : 276 -> 280
~ ___121-[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:]_block_invoke_2.31 : 368 -> 356
~ -[SLGoogleAuthController cancelAuthorization] : 16 -> 20
~ -[SLGoogleAuthController dealloc] : 84 -> 88
~ -[SLGoogleAuthController _redirectPathForURI:] : 288 -> 260
~ +[SLGoogleAuthController _identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:] : 216 -> 228
~ -[SLGoogleAuthController _didRedirectToURL:codeVerifier:] : 548 -> 528
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke : 1412 -> 1340
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke_2 : 192 -> 196
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke_3 : 412 -> 376
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke_4 : 320 -> 288
~ -[SLGoogleAuthController _completeWithIdentity:error:] : 336 -> 328
~ +[SLGoogleAuthController _presentUsernameMismatchAlert] : 588 -> 548
~ +[SLGoogleAuthController _presentInternetOfflineError] : 644 -> 604
CStrings:
- ".cxx_destruct"
- "@\"ACAccount\""
- "@\"ACAccountStore\""
- "@\"ASWebAuthenticationSession\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8B16@?20"
- "@32@0:8@16@?24"
- "@32@0:8@?16@?24"
- "@36@0:8@16B24@?28"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@?24@?32"
- "@48@0:8@16@24@?32@?40"
- "@64@0:8@16@24@32@40@48@56"
- "@72@0:8@16@24@32B40B44@48@?56@?64"
- "@?"
- "SLGoogle"
- "SLGoogleAuthController"
- "URLWithString:"
- "UUID"
- "UUIDString"
- "_account"
- "_accountStore"
- "_authenticationSession"
- "_clientID"
- "_completeWithIdentity:error:"
- "_didRedirectToURL:codeVerifier:"
- "_dismissAndCompleteWithIdentity:error:"
- "_identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:"
- "_init"
- "_initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:"
- "_presentInternetOfflineError"
- "_presentUsernameMismatchAlert"
- "_presentationBlock"
- "_redirectPathForURI:"
- "_webClient"
- "accountTypeWithAccountTypeIdentifier:"
- "authCodeFromRedirectURL:"
- "authRequestURL"
- "cancel"
- "cancelAuthorization"
- "clientID"
- "clientRedirectForAppOpenURL"
- "code"
- "compare:options:"
- "completion"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultScope"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "displayName"
- "domain"
- "emailScope"
- "errorWithDomain:code:userInfo:"
- "exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:"
- "expiryDate"
- "firstObject"
- "googleAuthControllerWithAccount:accountStore:presentationBlock:completion:"
- "googleAuthControllerWithPresentationBlock:completion:"
- "googleAuthControllerWithYouTubeUsername:presentationBlock:completion:"
- "grantedDataclasses"
- "hasPrefix:"
- "host"
- "idToken"
- "initForPermissionToAccessURL:fromURLString:completion:"
- "initWithAccount:accountStore:presentationBlock:"
- "initWithAccountDescription:presentationBlock:"
- "initWithAccountType:"
- "initWithClientID:"
- "initWithClientID:emailOnlyScope:presentationBlock:"
- "initWithEmailOnlyScope:presentationBlock:"
- "initWithOAuth2Token:refreshToken:expiryDate:"
- "initWithURL:callbackURLScheme:usingEphemeralSession:completionHandler:"
- "initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:grantedDataclasses:"
- "initWithWebClient:"
- "isEqualToString:"
- "localizedStringForKey:value:table:"
- "numberWithBool:"
- "numberWithInt:"
- "objectForKeyedSubscript:"
- "objectID"
- "openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:"
- "path"
- "resourceURL"
- "saveAccount:withCompletionHandler:"
- "scheme"
- "setAccountDescription:"
- "setAccountProperty:forKey:"
- "setCompletion:"
- "setCredential:"
- "setToken:"
- "setUsername:"
- "sl_openGoogleAuthenticationSheetForAccount:shouldConfirm:completion:"
- "sl_openGoogleAuthenticationSheetForAccount:shouldConfirm:delegateClassName:completion:"
- "sl_openGoogleAuthenticationSheetWithAccountDescription:completion:"
- "sl_openYouTubeAuthenticationSheetWithAccountDescription:completion:"
- "sl_openYouTubeAuthenticationSheetWithUsername:accountDescription:completion:"
- "sl_urlEncodedSHA256"
- "start"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "substringFromIndex:"
- "urlForClientID:redirectURI:scope:username:authRequestURL:codeChallenge:"
- "usernames"
- "v16@0:8"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@16B24@?28"
- "v40@0:8@16@24@?32"
- "v44@0:8@16B24@28@?36"
- "youTubeScope"

```
