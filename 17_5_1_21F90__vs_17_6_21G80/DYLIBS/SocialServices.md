## SocialServices

> `/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices`

```diff

-759.0.0.0.0
-  __TEXT.__text: 0x2798
-  __TEXT.__auth_stubs: 0x320
+759.1.0.0.0
+  __TEXT.__text: 0x28b4
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x5d8
+  __TEXT.__cstring: 0x5ab
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__unwind_info: 0xe4
   __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0xa15
-  __TEXT.__objc_methtype: 0x171
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_methname: 0xa87
+  __TEXT.__objc_methtype: 0x174
+  __TEXT.__objc_stubs: 0x8e0
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa8
-  __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x2b0
   __DATA_CONST.__objc_classrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_const: 0xd0
-  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH_CONST.__auth_got: 0x190
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x14
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 979DFC0C-EB11-39DF-AB69-469CED58CD73
+  UUID: 872ABA2D-9E5D-34FE-949C-D137ABD6276E
   Functions: 41
-  Symbols:   258
-  CStrings:  182
+  Symbols:   265
+  CStrings:  190
 
Symbols:
+ +[SLGoogleAuthController _identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:]
+ _ACAccountPropertyGrantedDataclasses
+ ___block_descriptor_40_e8_32s_e47_v24?0"SLWebTokenHandlerResponse"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$_identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:
+ _objc_msgSend$displayName
+ _objc_msgSend$exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:
+ _objc_msgSend$expiryDate
+ _objc_msgSend$grantedDataclasses
+ _objc_msgSend$idToken
+ _objc_msgSend$initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:grantedDataclasses:
+ _objc_msgSend$refreshToken
+ _objc_msgSend$setToken:
+ _objc_msgSend$token
+ _objc_msgSend$usernames
+ _objc_retain_x7
- +[SLGoogleAuthController _identityFromUsername:displayName:token:refreshToken:idToken:]
- ___block_descriptor_40_e8_32s_e92_v64?0"NSString"8"NSString"16"NSString"24"NSDate"32"NSArray"40"NSString"48"NSError"56ls32l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_89_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- _objc_msgSend$_identityFromUsername:displayName:token:refreshToken:idToken:
- _objc_msgSend$exchangeAuthCode:usingRedirect:codeVerifier:forTokensAndUsernameWithCompletion:
- _objc_msgSend$initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:
- _objc_retain_x26
- _objc_retain_x28
- _objc_retain_x6
CStrings:
+ "@64@0:8@16@24@32@40@48@56"
+ "_identityFromUsername:displayName:token:refreshToken:idToken:grantedDataclasses:"
+ "displayName"
+ "exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:"
+ "expiryDate"
+ "grantedDataclasses"
+ "idToken"
+ "initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:grantedDataclasses:"
+ "setToken:"
+ "usernames"
+ "v24@?0@\"SLWebTokenHandlerResponse\"8@\"NSError\"16"
- "@56@0:8@16@24@32@40@48"
- "_identityFromUsername:displayName:token:refreshToken:idToken:"
- "exchangeAuthCode:usingRedirect:codeVerifier:forTokensAndUsernameWithCompletion:"
- "initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:"
- "v64@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSDate\"32@\"NSArray\"40@\"NSString\"48@\"NSError\"56"

```
