## SocialServices

> `/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices`

```diff

 772.0.0.0.0
-  __TEXT.__text: 0x28e0
-  __TEXT.__auth_stubs: 0x300
+  __TEXT.__text: 0x2a20
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x5c1
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x22
   __TEXT.__objc_methname: 0xa65
   __TEXT.__objc_methtype: 0x174

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2b8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x168
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x178
   __DATA.__objc_ivar: 0x14

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65624F2A-4DDB-3427-8225-C670D9C14F19
+  UUID: 64253D0F-565C-342F-9B62-BB569A296E82
   Functions: 41
-  Symbols:   266
+  Symbols:   261
   CStrings:  192
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x8
Functions:
~ -[ACAccountStore(SLGoogle) sl_openGoogleAuthenticationSheetWithAccountDescription:completion:] : 264 -> 260
~ ___94-[ACAccountStore(SLGoogle) sl_openGoogleAuthenticationSheetWithAccountDescription:completion:]_block_invoke : 220 -> 232
~ -[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithAccountDescription:completion:] : 272 -> 268
~ ___95-[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithAccountDescription:completion:]_block_invoke : 260 -> 276
~ -[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithUsername:accountDescription:completion:] : 308 -> 292
~ ___104-[ACAccountStore(SLGoogle) sl_openYouTubeAuthenticationSheetWithUsername:accountDescription:completion:]_block_invoke : 260 -> 276
~ -[ACAccountStore(SLGoogle) sl_openGoogleAuthenticationSheetForAccount:shouldConfirm:delegateClassName:completion:] : 268 -> 264
~ +[SLGoogleAuthController googleAuthControllerWithPresentationBlock:completion:] : 140 -> 136
~ +[SLGoogleAuthController googleAuthControllerWithAccount:accountStore:presentationBlock:completion:] : 180 -> 168
~ +[SLGoogleAuthController googleAuthControllerWithYouTubeUsername:presentationBlock:completion:] : 156 -> 148
~ -[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:] : 1016 -> 1044
~ ___121-[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:]_block_invoke : 332 -> 324
~ ___121-[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:]_block_invoke_2 : 504 -> 524
~ ___121-[SLGoogleAuthController _initWithAccount:accountStore:username:youTube:emailOnly:clientID:presentationBlock:completion:]_block_invoke_2.31 : 356 -> 368
~ -[SLGoogleAuthController _redirectPathForURI:] : 260 -> 288
~ +[SLGoogleAuthController _identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:] : 228 -> 216
~ -[SLGoogleAuthController _didRedirectToURL:codeVerifier:] : 528 -> 548
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke : 1328 -> 1412
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke_2 : 196 -> 192
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke_3 : 376 -> 412
~ ___57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke_4 : 288 -> 320
~ -[SLGoogleAuthController _dismissAndCompleteWithIdentity:error:] : 176 -> 180
~ -[SLGoogleAuthController _completeWithIdentity:error:] : 328 -> 336
~ +[SLGoogleAuthController _presentUsernameMismatchAlert] : 548 -> 588
~ +[SLGoogleAuthController _presentInternetOfflineError] : 604 -> 644

```
