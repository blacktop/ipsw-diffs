## SocialServices

> `/System/Library/PrivateFrameworks/SocialServices.framework/Versions/A/SocialServices`

```diff

-763.0.0.0.0
-  __TEXT.__text: 0x26ec
+762.0.0.0.0
+  __TEXT.__text: 0x25ec
   __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_methlist: 0xf4
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0x4ac
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__cstring: 0x4d9
+  __TEXT.__unwind_info: 0xf0
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x7cd
-  __TEXT.__objc_methtype: 0x12c
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__objc_methname: 0x75e
+  __TEXT.__objc_methtype: 0x129
+  __TEXT.__objc_stubs: 0x6a0
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x248
+  __DATA_CONST.__objc_selrefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0xb8
   __AUTH_CONST.__const: 0x1b0

   - /System/Library/Frameworks/Social.framework/Versions/A/Social
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 45
-  Symbols:   184
+  Functions: 47
+  Symbols:   177
   CStrings:  29
 
Symbols:
+ +[SLGoogleAuthController _identityFromUsername:displayName:token:refreshToken:idToken:]
+ __57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke.66
+ ___block_descriptor_40_e8_32s_e92_v64?0"NSString"8"NSString"16"NSString"24"NSDate"32"NSArray"40"NSString"48"NSError"56l
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s
+ _objc_msgSend$_identityFromUsername:displayName:token:refreshToken:idToken:
+ _objc_msgSend$exchangeAuthCode:usingRedirect:codeVerifier:forTokensAndUsernameWithCompletion:
+ _objc_msgSend$initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:
- +[SLGoogleAuthController _identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:]
- _ACAccountPropertyGrantedDataclasses
- __57-[SLGoogleAuthController _didRedirectToURL:codeVerifier:]_block_invoke.68
- ___block_descriptor_40_e8_32s_e47_v24?0"SLWebTokenHandlerResponse"8"NSError"16l
- ___block_descriptor_48_e8_32s40s_e5_v8?0l
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0l
- ___copy_helper_block_e8_32s40s
- ___destroy_helper_block_e8_32s40s
- _objc_msgSend$_identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:
- _objc_msgSend$displayName
- _objc_msgSend$exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:
- _objc_msgSend$expiryDate
- _objc_msgSend$grantedDataclasses
- _objc_msgSend$idToken
- _objc_msgSend$initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:grantedDataclasses:
- _objc_msgSend$refreshToken
- _objc_msgSend$setToken:
- _objc_msgSend$token
- _objc_msgSend$usernames
CStrings:
+ "v64@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSDate\"32@\"NSArray\"40@\"NSString\"48@\"NSError\"56"
- "v24@?0@\"SLWebTokenHandlerResponse\"8@\"NSError\"16"

```
